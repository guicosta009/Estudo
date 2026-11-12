#!/usr/bin/env python3
"""Consolida o registro do piloto de duas semanas de um POP e compara com a linha de base.

Entrada: o registro do piloto em texto separado por tabulação, com a linha de cabeçalho do
modelo `assets/piloto-modelo.md`. Pode ser um .tsv ou o próprio `piloto-<sigla>-<nn>.md`:
só as linhas com tabulação são lidas (a primeira é o cabeçalho), e as que começam com "#"
são ignoradas.
Colunas lidas (pelo começo do nome, sem diferenciar maiúsculas e acentos):
  Semana · Caso · Tipo de caso · Executor · Min. execução · Min. revisão ·
  Voltou para retrabalho? · Min. retrabalho · Erros pegos na revisão (tipo) ·
  Erro chegou ao cliente ou tribunal? · Desvio do POP? Por quê
"Erros pegos" aceita "0", "1 (data)", "2 (fato, tom)".

Contas:
  tempo total por execução = (execução + revisão + retrabalho) / execuções
  retrabalho (%) = execuções que voltaram / execuções x 100
  execuções com correção = execuções com pelo menos um erro pego na revisão
  peso da revisão = minutos de revisão / (minutos de execução + minutos de revisão)
  sinal de carimbo = N execuções seguidas (padrão 5) com revisão de até M minutos
                     (padrão 2) e nenhuma correção
  comparação: semana 2 contra a linha de base (a semana 1 fica fora, é a curva de aprendizado)
  horas por mês = (antes - semana 2) x execuções por mês / 60

Uso:
  python3 analisar_piloto.py REGISTRO.tsv --antes 150 [--retrabalho-antes 15]
      [--execucoes-mes 80] [--carimbo-seguidas 5] [--carimbo-min 2] [--saida ARQUIVO.md]
Só biblioteca padrão. Os números saem do registro; nada é estimado.
"""
import argparse
import re
import sys
import unicodedata


def norm(texto):
    t = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip().lower()


def num(valor):
    try:
        return float(str(valor).replace(",", ".").strip() or 0)
    except ValueError:
        return 0.0


def sim(valor):
    return norm(valor).startswith("sim") or norm(valor) in ("s", "x", "yes")


COLUNAS = {
    "semana": "semana",
    "caso": "caso",
    "tipo": "tipo de caso",
    "executor": "executor",
    "exec": "min. execucao",
    "rev": "min. revisao",
    "voltou": "voltou para retrabalho",
    "retrab": "min. retrabalho",
    "erros": "erros pegos",
    "chegou": "erro chegou",
    "desvio": "desvio do pop",
}


def ler(caminho):
    linhas = []
    with open(caminho, encoding="utf-8") as f:
        brutas = [l.rstrip("\n") for l in f
                  if "\t" in l and l.strip() and not l.lstrip().startswith("#")]
    if not brutas:
        sys.exit("Registro vazio.")
    cab = [norm(c) for c in brutas[0].split("\t")]
    idx = {}
    for chave, inicio in COLUNAS.items():
        for i, c in enumerate(cab):
            if c.startswith(inicio):
                idx[chave] = i
                break
    faltando = [COLUNAS[k] for k in ("semana", "exec", "rev") if k not in idx]
    if faltando:
        sys.exit("Faltam colunas no cabeçalho: " + ", ".join(faltando))
    for bruta in brutas[1:]:
        cel = bruta.split("\t")
        pega = lambda k: cel[idx[k]] if k in idx and idx[k] < len(cel) else ""
        erros_txt = pega("erros")
        m = re.match(r"\s*(\d+)", erros_txt)
        qtd = int(m.group(1)) if m else 0
        tipos = re.findall(r"\(([^)]*)\)", erros_txt)
        tipos = [t.strip().lower() for grupo in tipos for t in grupo.split(",") if t.strip()]
        linhas.append({
            "semana": str(int(num(pega("semana")))) if num(pega("semana")) else pega("semana").strip(),
            "caso": pega("caso").strip(),
            "tipo": pega("tipo").strip() or "sem tipo",
            "exec": num(pega("exec")),
            "rev": num(pega("rev")),
            "voltou": sim(pega("voltou")),
            "retrab": num(pega("retrab")),
            "erros": qtd,
            "tipos": tipos,
            "chegou": sim(pega("chegou")),
            "desvio": sim(pega("desvio")),
        })
    return linhas


def resumo(linhas):
    n = len(linhas)
    if n == 0:
        return None
    soma = lambda k: sum(l[k] for l in linhas)
    tipos = {}
    for l in linhas:
        for t in l["tipos"]:
            tipos[t] = tipos.get(t, 0) + 1
    casos = {}
    for l in linhas:
        casos[l["tipo"]] = casos.get(l["tipo"], 0) + 1
    exec_rev = soma("exec") + soma("rev")
    return {
        "n": n,
        "exec": soma("exec") / n,
        "rev": soma("rev") / n,
        "retrab": soma("retrab") / n,
        "total": (soma("exec") + soma("rev") + soma("retrab")) / n,
        "pct_retrab": 100 * sum(1 for l in linhas if l["voltou"]) / n,
        "com_correcao": sum(1 for l in linhas if l["erros"] > 0),
        "erros": sum(l["erros"] for l in linhas),
        "tipos": tipos,
        "chegou": sum(1 for l in linhas if l["chegou"]),
        "desvios": sum(1 for l in linhas if l["desvio"]),
        "peso_rev": 100 * soma("rev") / exec_rev if exec_rev else 0.0,
        "casos": casos,
    }


def carimbo(linhas, seguidas, minutos):
    sequencia, maior, inicio, achados = 0, 0, None, []
    for i, l in enumerate(linhas):
        if l["rev"] <= minutos and l["erros"] == 0:
            sequencia += 1
            if sequencia == 1:
                inicio = i
            if sequencia == seguidas:
                achados.append((linhas[inicio]["caso"] or f"linha {inicio + 1}", l["semana"]))
        else:
            sequencia = 0
        maior = max(maior, sequencia)
    return maior, achados


def f1(x):
    return f"{x:.1f}".replace(".", ",")


def montar(linhas, a):
    semanas = sorted({l["semana"] for l in linhas}, key=lambda s: (len(s), s))
    out = ["# Análise do registro do piloto", "",
           f"Execuções no registro: {len(linhas)} · Semanas: {', '.join(semanas)}", ""]
    out += ["| Indicador | " + " | ".join(f"Semana {s}" for s in semanas) + " |",
            "|---|" + "---|" * len(semanas)]
    res = {s: resumo([l for l in linhas if l["semana"] == s]) for s in semanas}
    filas = [
        ("Execuções", lambda r: str(r["n"])),
        ("Min. de execução (média)", lambda r: f1(r["exec"])),
        ("Min. de revisão (média)", lambda r: f1(r["rev"])),
        ("Min. de retrabalho (média)", lambda r: f1(r["retrab"])),
        ("Tempo total por execução (min)", lambda r: f1(r["total"])),
        ("Retrabalho (%)", lambda r: f1(r["pct_retrab"])),
        ("Execuções com correção na revisão", lambda r: f"{r['com_correcao']} em {r['n']}"),
        ("Erros pegos na revisão", lambda r: str(r["erros"])),
        ("Erros que chegaram ao cliente ou ao tribunal", lambda r: str(r["chegou"])),
        ("Desvios do POP", lambda r: str(r["desvios"])),
        ("Peso da revisão (%)", lambda r: f1(r["peso_rev"])),
    ]
    for nome, fn in filas:
        out.append(f"| {nome} | " + " | ".join(fn(res[s]) for s in semanas) + " |")
    out.append("")
    for s in semanas:
        r = res[s]
        tipos = ", ".join(f"{t}: {q}" for t, q in sorted(r["tipos"].items())) or "nenhum"
        casos = ", ".join(f"{t}: {q}" for t, q in sorted(r["casos"].items()))
        out.append(f"- Semana {s}. Erros por tipo: {tipos}. Tipos de caso: {casos}.")
    out.append("")

    maior, achados = carimbo(linhas, a.carimbo_seguidas, a.carimbo_min)
    out.append("## Sinal de revisão que virou carimbo")
    if achados:
        out.append(f"ATENÇÃO: {len(achados)} sequência(s) de {a.carimbo_seguidas} ou mais execuções seguidas "
                   f"com revisão de até {f1(a.carimbo_min)} min e nenhuma correção (a primeira começa em "
                   f"{achados[0][0]}). Plante um erro discreto num caso fictício e veja se a revisão pega.")
    else:
        out.append(f"Nenhuma sequência de {a.carimbo_seguidas} execuções seguidas com revisão curta e sem "
                   f"correção (maior sequência: {maior}).")
    out.append("")

    out.append("## Antes e depois (semana 2 contra a linha de base)")
    s2 = res.get("2")
    if not s2:
        out.append("Sem semana 2 no registro. A comparação usa só a semana 2; a semana 1 é curva de aprendizado.")
        return "\n".join(out) + "\n", None
    if a.antes is None:
        out.append("Linha de base não informada (--antes). Rode a medir-retorno antes de comparar.")
        return "\n".join(out) + "\n", None
    dif = a.antes - s2["total"]
    pct = 100 * dif / a.antes if a.antes else 0.0
    out += ["| Indicador | Antes | Piloto, semana 2 |", "|---|---|---|",
            f"| Tempo por execução (min) | {f1(a.antes)} | {f1(s2['total'])} |",
            f"| Retrabalho (%) | {f1(a.retrabalho_antes) if a.retrabalho_antes is not None else 'não medido'} | {f1(s2['pct_retrab'])} |",
            f"| Execuções com correção | não medido | {s2['com_correcao']} em {s2['n']} |",
            f"| Erros que passaram | não medido | {s2['chegou']} |", ""]
    out.append(f"- Por execução: {f1(abs(dif))} min {'a menos' if dif >= 0 else 'a mais'} "
               f"({f1(abs(pct))}% {'menos' if dif >= 0 else 'mais'} tempo).")
    if a.execucoes_mes:
        horas = dif * a.execucoes_mes / 60
        out.append(f"- Por mês, com {f1(a.execucoes_mes)} execuções: {f1(abs(horas))} h "
                   f"{'devolvidas ao escritório' if horas >= 0 else 'a mais de trabalho'}.")
    if a.retrabalho_antes is not None:
        pts = a.retrabalho_antes - s2["pct_retrab"]
        out.append(f"- Retrabalho: {f1(abs(pts))} pontos {'a menos' if pts >= 0 else 'a mais'}.")
    out.append("")
    total_chegou = sum(r["chegou"] for r in res.values())
    piorou_retrab = a.retrabalho_antes is not None and s2["pct_retrab"] > a.retrabalho_antes
    if total_chegou:
        leitura = ("Não pronto. Erro chegou ao cliente ou ao tribunal durante o piloto: isso zera o ganho de "
                   "tempo. O passo volta de sigla até a causa estar corrigida e testada de novo.")
    elif dif <= 0:
        leitura = ("Sem ganho. O tempo não caiu. Olhe a revisão e o retrabalho passo a passo antes de seguir.")
    elif piorou_retrab:
        leitura = ("Troca ruim. O tempo caiu, mas o retrabalho subiu. Ajuste a instrução ou a base e meça de novo.")
    else:
        leitura = ("Ganho consistente. O tempo caiu sem aumentar o retrabalho e nenhum erro passou. "
                   "Este é o número de partida para a automação.")
    ressalvas = []
    if achados:
        ressalvas.append("há sinal de revisão que virou carimbo; teste a revisão com um erro plantado antes de aceitar o número")
    inventou = sum(q for r in res.values() for t, q in r["tipos"].items() if norm(t).startswith("invenc"))
    if inventou:
        ressalvas.append(f"a revisão pegou {inventou} invenção(ões); o passo que inventou sai de S e o ponto entra em \"nunca sai sem revisão humana\"")
    if ressalvas and not total_chegou:
        leitura += " Ressalvas: " + "; ".join(ressalvas) + "."
    out.append("Leitura: " + leitura)
    out.append("")
    out.append("Confira se os tipos de caso da semana 2 se parecem com os da linha de base: se o piloto "
               "teve só casos fáceis, o ganho está inflado. Hora devolvida precisa de destino (medir-retorno).")
    return "\n".join(out) + "\n", leitura


def main():
    p = argparse.ArgumentParser(description="Analisa o registro do piloto de um POP.")
    p.add_argument("registro")
    p.add_argument("--antes", type=float, help="minutos por execução na linha de base")
    p.add_argument("--retrabalho-antes", type=float, help="retrabalho na linha de base, em %%")
    p.add_argument("--execucoes-mes", type=float, help="execuções por mês no volume normal")
    p.add_argument("--carimbo-seguidas", type=int, default=5)
    p.add_argument("--carimbo-min", type=float, default=2)
    p.add_argument("--saida")
    a = p.parse_args()
    linhas = ler(a.registro)
    if not linhas:
        sys.exit("Registro sem execuções (só o cabeçalho ou linhas de exemplo com #).")
    texto, _ = montar(linhas, a)
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as f:
            f.write(texto)
    print(texto)


if __name__ == "__main__":
    main()
