#!/usr/bin/env python3
"""Ranking de setores a partir do registro de horas de uma semana.

Lê:
  1. o registro de horas (CSV ou TSV) com as colunas do método:
     Data | Pessoa | Setor | Atividade (verbo + objeto) | Início | Fim | Minutos | Canal |
     Interrompida? | S / A / H (opcional) | Observação
     (também aceita a exportação da aba Registro da planilha, com "Minutos considerados");
  2. o incômodo e o potencial de IA por setor (CSV com Setor, Incômodo, Potencial, ou JSON).

Calcula horas por setor e por pessoa, as 10 atividades que mais consumiram horas, as linhas
suspeitas, a pontuação do diagnóstico (horas × incômodo), a pontuação completa
(horas × incômodo × potencial de IA), o ranking com desempate e a regra de quando as duas
contas discordam. Saída em markdown. Só biblioteca padrão.

Uso:
  python3 ranking_setores.py REGISTRO.csv SETORES.csv [--dias 5] [--escritorio NOME]
      [--dono FUNÇÃO] [--alvo-diagnostico "Setor"] [--sem-pessoas] [--saida ARQUIVO.md]
"""
import argparse
import csv
import datetime
import io
import json
import re
import sys
import unicodedata
from collections import defaultdict, Counter

SETORES = [
    "Atendimento e triagem", "Comercial", "Produção de peças", "Prazos e controladoria",
    "Audiências e diligências", "Financeiro e cobrança", "Relacionamento com o cliente",
    "Marketing e conteúdo", "Gestão de equipe", "Administrativo",
]
APELIDOS = {
    "atendimento": "Atendimento e triagem", "triagem": "Atendimento e triagem",
    "comercial": "Comercial", "producao": "Produção de peças", "pecas": "Produção de peças",
    "producao de pecas": "Produção de peças", "prazos": "Prazos e controladoria",
    "controladoria": "Prazos e controladoria", "audiencias": "Audiências e diligências",
    "diligencias": "Audiências e diligências", "financeiro": "Financeiro e cobrança",
    "cobranca": "Financeiro e cobrança", "relacionamento": "Relacionamento com o cliente",
    "marketing": "Marketing e conteúdo", "conteudo": "Marketing e conteúdo",
    "equipe": "Gestão de equipe", "gestao": "Gestão de equipe", "gestao de equipe": "Gestão de equipe",
    "administrativo": "Administrativo",
}
VAGAS = {"cliente", "clientes", "financeiro", "prazos", "prazo", "cuidar do cliente", "cuidar dos clientes",
         "ver os prazos", "ver prazos", "fazer a inicial", "whatsapp", "email", "e-mail", "reuniao",
         "reunioes", "diversos", "outros", "outro", "geral", "administrativo", "tarefas", "trabalho",
         "pecas", "peticoes", "atendimento", "processos", "demandas", "coisas"}
RE_CPF = re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b")
RE_CNJ = re.compile(r"\b\d{7}-?\d{2}\.?\d{4}\.?\d\.?\d{2}\.?\d{4}\b")
RE_NUM_LONGO = re.compile(r"\d[\d.\-/]{7,}\d")


def sem_acento(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def norm(s):
    return re.sub(r"\s+", " ", sem_acento(s).strip().lower())


SETOR_POR_NORM = {norm(s): s for s in SETORES}


def setor_canonico(txt):
    """Devolve (rótulo, base). Aceita setor separado por área: 'Produção de peças · Previdenciário'."""
    t = (txt or "").strip()
    if not t:
        return "", None
    partes = re.split(r"\s+[·|/]\s+", t, maxsplit=1)
    b = norm(partes[0])
    base = SETOR_POR_NORM.get(b) or APELIDOS.get(b)
    if base is None:
        return t, None
    if len(partes) == 2 and partes[1].strip():
        return f"{base} · {partes[1].strip()}", base
    return base, base


def fmt(n, casas=1):
    if n is None:
        return "·"
    s = f"{n:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if casas and s.endswith("," + "0" * casas):
        s = s[: -(casas + 1)]
    return s


def ler_tabela(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        texto = f.read()
    primeira = texto.splitlines()[0] if texto.strip() else ""
    delim = max(["\t", ";", ","], key=lambda d: primeira.count(d))
    leitor = csv.reader(io.StringIO(texto), delimiter=delim)
    linhas = [l for l in leitor]
    return linhas


def mapear_colunas(cab):
    m = {}
    for i, c in enumerate(cab):
        n = norm(c)
        if n == "data":
            m["data"] = i
        elif n.startswith("pessoa"):
            m["pessoa"] = i
        elif n.startswith("setor"):
            m["setor"] = i
        elif n.startswith("atividade") or n.startswith("tarefa"):
            m["atividade"] = i
        elif n.startswith("inicio"):
            m["inicio"] = i
        elif n == "fim" or n.startswith("fim"):
            m["fim"] = i
        elif n.startswith("minutos considerados"):
            m["min_calc"] = i
        elif n.startswith("minutos") and "revisao" not in n:
            m["minutos"] = i
        elif n.startswith("canal"):
            m["canal"] = i
        elif n.startswith("interrompida"):
            m["interrompida"] = i
        elif n.replace(" ", "") in ("s/a/h", "sah", "marcacao", "marcacaos/a/h", "sigla"):
            m["sah"] = i
        elif n.startswith("observ"):
            m["obs"] = i
    return m


def num(txt):
    t = (txt or "").strip().replace(",", ".")
    if not t:
        return None
    try:
        return float(t)
    except ValueError:
        return None


def hora(txt):
    t = (txt or "").strip()
    mm = re.match(r"^(\d{1,2})[:h](\d{2})(?::\d{2})?$", t)
    if not mm:
        return None
    return int(mm.group(1)) * 60 + int(mm.group(2))


def ler_setores(caminho):
    """Lê incômodo, potencial e dono por setor. Devolve (dict, avisos)."""
    avisos = []
    dados = {}
    if caminho.lower().endswith(".json"):
        with open(caminho, encoding="utf-8") as f:
            bruto = json.load(f)
        itens = []
        if isinstance(bruto, dict):
            for k, v in bruto.items():
                v = v if isinstance(v, dict) else {}
                itens.append((k, v.get("incomodo", v.get("incômodo")), v.get("potencial"), v.get("dono", "")))
        else:
            for v in bruto:
                itens.append((v.get("setor", ""), v.get("incomodo", v.get("incômodo")), v.get("potencial"), v.get("dono", "")))
    else:
        linhas = ler_tabela(caminho)
        cab = [norm(c) for c in linhas[0]]

        def idx(prefixo):
            for i, c in enumerate(cab):
                if c.startswith(prefixo):
                    return i
            return None
        i_s, i_i, i_p, i_d = idx("setor"), idx("incomodo"), idx("potencial"), idx("dono")
        itens = []
        for l in linhas[1:]:
            if not any(x.strip() for x in l):
                continue
            g = lambda i: l[i] if i is not None and i < len(l) else ""
            itens.append((g(i_s), g(i_i), g(i_p), g(i_d)))
    for setor, inc, pot, dono in itens:
        rotulo, base = setor_canonico(str(setor))
        if not rotulo:
            continue
        if base is None:
            avisos.append(f"Setor fora da lista dos 10 no arquivo de incômodo: \"{setor}\". Confira o nome.")

        def nota(v, nome):
            if v in (None, ""):
                return None
            try:
                x = int(float(str(v).replace(",", ".")))
            except ValueError:
                avisos.append(f"{nome} inválido para {rotulo}: \"{v}\". Use um número de 1 a 5.")
                return None
            if not 1 <= x <= 5:
                avisos.append(f"{nome} fora da escala para {rotulo}: {v}. Use um número de 1 a 5.")
                return None
            return x
        dados[rotulo] = {"inc": nota(inc, "Incômodo"), "pot": nota(pot, "Potencial"), "dono": str(dono or "").strip()}
    return dados, avisos


def potencial_por_pct(p):
    if p < 20:
        return 1
    if p < 40:
        return 2
    if p < 60:
        return 3
    if p <= 80:
        return 4
    return 5


def main():
    ap = argparse.ArgumentParser(description="Ranking de setores a partir do registro de horas.")
    ap.add_argument("registro", help="CSV ou TSV do registro de horas")
    ap.add_argument("setores", help="CSV ou JSON com incômodo e potencial de IA por setor")
    ap.add_argument("--dias", type=float, default=5, help="dias úteis registrados (padrão 5)")
    ap.add_argument("--escritorio", default="[NOME DO ESCRITÓRIO]")
    ap.add_argument("--dono", default="[A DEFINIR]", help="dono do documento (função)")
    ap.add_argument("--versao", default="1")
    ap.add_argument("--alvo-diagnostico", default="", help="setor-alvo provisório que saiu do diagnóstico")
    ap.add_argument("--sem-pessoas", action="store_true", help="não mostra a tabela por pessoa")
    ap.add_argument("--saida", default="", help="arquivo .md de saída (padrão: tela)")
    a = ap.parse_args()
    dias = a.dias if a.dias > 0 else 5

    linhas = ler_tabela(a.registro)
    if not linhas:
        sys.exit("Registro vazio.")
    col = mapear_colunas(linhas[0])
    faltam = [c for c in ("setor", "atividade") if c not in col]
    if faltam or not ({"minutos", "min_calc"} & set(col) or {"inicio", "fim"} <= set(col)):
        sys.exit("O registro precisa das colunas Setor, Atividade e Minutos (ou Início e Fim). "
                 f"Colunas encontradas: {', '.join(linhas[0])}")

    def g(l, chave):
        i = col.get(chave)
        return l[i].strip() if i is not None and i < len(l) else ""

    suspeitas = []
    blocos = []
    vistos = Counter()
    datas = set()
    for n, l in enumerate(linhas[1:], start=2):
        if not any(x.strip() for x in l):
            continue
        data, pessoa, setor_txt, ativ = g(l, "data"), g(l, "pessoa"), g(l, "setor"), g(l, "atividade")
        if data:
            datas.add(data)
        minutos = num(g(l, "min_calc")) if g(l, "min_calc") else None
        if minutos in (None, 0):
            minutos = num(g(l, "minutos"))
        ini, fim = hora(g(l, "inicio")), hora(g(l, "fim"))
        if minutos is None and ini is not None and fim is not None:
            minutos = fim - ini
            if minutos < 0:
                suspeitas.append((n, "Fim antes do início. Confira os horários."))
                minutos = None
        if minutos is None or minutos <= 0:
            suspeitas.append((n, "Sem minutos (nem início e fim). A linha ficou fora da soma."))
            continue
        rotulo, base = setor_canonico(setor_txt)
        if not setor_txt:
            suspeitas.append((n, f"Setor em branco ({fmt(minutos, 0)} min ficaram fora da soma). Qual é o setor?"))
        elif base is None:
            suspeitas.append((n, f"Setor fora da lista dos 10: \"{setor_txt}\". Corrija o nome ou diga a qual setor pertence."))
        na = norm(ativ)
        if not ativ:
            suspeitas.append((n, "Atividade em branco. Escreva em verbo + objeto."))
        elif na in VAGAS or len(na.split()) < 2:
            suspeitas.append((n, f"Atividade vaga: \"{ativ}\". Reescreva em verbo + objeto (ex.: \"Responder dúvida de andamento\")."))
        elif not re.match(r"^[a-z]+(r|r-se|rse)$", na.split()[0]):
            suspeitas.append((n, f"Atividade sem verbo no início: \"{ativ}\". Confira se dá para escrever em verbo + objeto."))
        if minutos > 120:
            suspeitas.append((n, f"Bloco de {fmt(minutos, 0)} min, acima de 2 h. Pode esconder outras atividades: vale quebrar."))
        elif minutos < 5 and "rajada" not in na:
            suspeitas.append((n, "Bloco abaixo de 5 min. O método manda lançar na contagem de rajada, numa linha só por dia."))
        for chave, nome_col in (("atividade", "Atividade"), ("obs", "Observação")):
            v = g(l, chave)
            if v and (RE_CPF.search(v) or RE_CNJ.search(v) or RE_NUM_LONGO.search(v)):
                suspeitas.append((n, f"Possível dado de cliente na coluna {nome_col} (número longo). "
                                     "Troque por [PROCESSO] ou [DOC] antes de seguir. O valor não foi repetido aqui."))
        chave_dup = tuple(x.strip() for x in l)
        vistos[chave_dup] += 1
        if vistos[chave_dup] == 2:
            suspeitas.append((n, "Linha repetida, igual a uma anterior. Foi lançada duas vezes?"))
        blocos.append({
            "linha": n, "data": data, "pessoa": pessoa or "[sem pessoa]", "setor": rotulo if setor_txt else "",
            "base": base, "atividade": ativ, "min": minutos,
            "sah": g(l, "sah").upper()[:1] if g(l, "sah") else "",
            "interr": norm(g(l, "interrompida")) in ("sim", "s"),
        })

    # mais de 10 h no mesmo dia para a mesma pessoa
    por_dia = defaultdict(float)
    for b in blocos:
        if b["data"]:
            por_dia[(b["pessoa"], b["data"])] += b["min"]
    for (p, d), m in sorted(por_dia.items()):
        if m > 600:
            suspeitas.append((0, f"{p} somou {fmt(m / 60)} h em {d}, mais de 10 h no mesmo dia. Confira se há linha lançada duas vezes."))

    setores_info, avisos_set = ler_setores(a.setores)

    # somas
    min_setor = defaultdict(float)
    sah_setor = defaultdict(lambda: defaultdict(float))
    interr_setor = Counter()
    pessoa_setor = defaultdict(lambda: defaultdict(float))
    ativ = defaultdict(lambda: {"min": 0.0, "vezes": 0, "nome": "", "sah": Counter()})
    for b in blocos:
        if not b["setor"]:
            continue
        min_setor[b["setor"]] += b["min"]
        if b["sah"] in ("S", "A", "H"):
            sah_setor[b["setor"]][b["sah"]] += b["min"]
        if b["interr"]:
            interr_setor[b["setor"]] += 1
        pessoa_setor[b["pessoa"]][b["setor"]] += b["min"]
        k = (b["setor"], norm(b["atividade"]))
        ativ[k]["min"] += b["min"]
        ativ[k]["vezes"] += 1
        ativ[k]["nome"] = ativ[k]["nome"] or b["atividade"]
        if b["sah"]:
            ativ[k]["sah"][b["sah"]] += 1

    ordem = [s for s in SETORES]
    for s in list(min_setor) + list(setores_info):
        if s not in ordem:
            ordem.append(s)
    total_min = sum(min_setor.values())
    fator = 5.0 / dias

    linhas_setor = []
    for s in ordem:
        h = min_setor.get(s, 0) / 60.0
        hs = h * fator
        info = setores_info.get(s, {})
        inc, pot = info.get("inc"), info.get("pot")
        sm = sah_setor.get(s, {})
        marc = sum(sm.values())
        pot_sug = None
        cobertura = (marc / min_setor[s] * 100) if min_setor.get(s) else 0
        if marc > 0:
            pct_sa = (sm.get("S", 0) + sm.get("A", 0)) / marc * 100
            pot_sug = potencial_por_pct(pct_sa)
        pot_uso, pot_origem = pot, "informado"
        if pot_uso is None and pot_sug is not None:
            pot_uso, pot_origem = pot_sug, "sugerido pelas marcações"
        d = hs * inc if (hs > 0 and inc) else None
        sc = d * pot_uso if (d is not None and pot_uso) else None
        linhas_setor.append({"setor": s, "h": h, "hs": hs, "inc": inc, "pot": pot_uso, "pot_origem": pot_origem,
                             "pot_sug": pot_sug, "cobertura": cobertura, "d": d, "s": sc, "sm": sm,
                             "interr": interr_setor.get(s, 0), "dono": info.get("dono", "")})

    full = sorted([x for x in linhas_setor if x["s"] is not None], key=lambda x: (-x["s"], -x["hs"], -x["d"]))
    diag = sorted([x for x in linhas_setor if x["d"] is not None], key=lambda x: (-x["d"], -x["hs"]))
    pos = {x["setor"]: i + 1 for i, x in enumerate(full)}
    top = full[0] if full else None
    top_d = diag[0] if diag else None

    # setor do diagnóstico: o informado (setor-alvo provisório) ou o 1º de horas × incômodo medido
    alvo_diag_txt = a.alvo_diagnostico.strip()
    if alvo_diag_txt:
        rot, _ = setor_canonico(alvo_diag_txt)
        ref = next((x for x in linhas_setor if x["setor"] == rot), None)
        nome_ref = rot
        origem_ref = "setor-alvo provisório do diagnóstico"
    else:
        ref = top_d
        nome_ref = top_d["setor"] if top_d else ""
        origem_ref = "1º lugar em horas × incômodo, com as horas medidas"

    def proximo_depois(alvo):
        for x in full:
            if x["setor"] != alvo:
                return x["setor"]
        return "[A DEFINIR]"

    alerta_ref = ""
    if not top:
        alvo, prox = "[A DEFINIR]", "[A DEFINIR]"
        msg = ("Dê a nota de potencial de IA dos setores para calcular a pontuação completa." if top_d
               else "Preencha horas, incômodo e potencial de IA de pelo menos um setor.")
    elif not nome_ref:
        alvo, prox = top["setor"], proximo_depois(top["setor"])
        msg = f"Sem setor do diagnóstico para comparar. Pela pontuação completa, o setor-alvo é {top['setor']}."
    elif nome_ref == top["setor"]:
        alvo, prox = top["setor"], proximo_depois(top["setor"])
        msg = f"As duas contas apontam o mesmo setor: {top['setor']}. Está decidido: é o setor-alvo confirmado."
    else:
        pot_ref = ref["pot"] if ref else (setores_info.get(nome_ref, {}).get("pot"))
        if ref and ref["h"] == 0:
            alerta_ref = (f"Atenção: {nome_ref} não teve nenhuma hora no registro desta semana. "
                          "A semana foi atípica para esse setor? [A CONFIRMAR]")
        if not pot_ref:
            alvo, prox = "[A CONFIRMAR]", "[A CONFIRMAR]"
            msg = (f"O diagnóstico aponta {nome_ref}, mas ele está sem nota de potencial de IA. "
                   f"Dê a nota para comparar com {top['setor']}.")
        elif pot_ref <= 2:
            alvo, prox = top["setor"], proximo_depois(top["setor"])
            msg = (f"O diagnóstico aponta {nome_ref}, mas o potencial de IA dele é {pot_ref}: a maior parte das "
                   f"horas é trabalho humano. Troque o setor-alvo para {top['setor']}.")
        else:
            alvo, prox = nome_ref, top["setor"]
            msg = (f"O diagnóstico aponta {nome_ref} e a pontuação completa aponta {top['setor']}. Como o potencial "
                   f"de IA de {nome_ref} é {pot_ref}, fique com ele e deixe {top['setor']} como o próximo da fila.")

    hoje = datetime.date.today().isoformat()
    out = []
    w = out.append
    w(f"# Ranking de setores · {a.escritorio}")
    w("")
    w(f"Versão: {a.versao} · Data da revisão: {hoje} · Dono: {a.dono}")
    w("")
    if datas:
        w(f"Semana registrada: {len(datas)} data(s) distinta(s) no registro ({', '.join(sorted(datas)[:7])}"
          f"{'...' if len(datas) > 7 else ''}). Dias úteis considerados na conta: {fmt(dias)}.")
        if abs(len(datas) - dias) >= 1:
            w("")
            w(f"> Aviso: o registro tem {len(datas)} data(s) e a conta usa {fmt(dias)} dia(s) útil(eis). "
              "Confira o parâmetro --dias. [A CONFIRMAR]")
    w("")
    w(f"Horas registradas: {fmt(total_min / 60)} h · Horas por semana (registradas ÷ dias × 5): {fmt(total_min / 60 * fator)} h")
    w("")
    w("Como ler: horas por semana × incômodo é a conta do diagnóstico. Horas por semana × incômodo × potencial "
      "de IA é a pontuação completa. Empate: vence o setor com mais horas.")
    w("")

    w("## 1. Horas por setor")
    w("")
    w("| Setor | Horas registradas | Horas por semana | Horas por mês | % das horas | Horas S | Horas A | Horas H | Sem marcação | Blocos interrompidos |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for x in linhas_setor:
        if x["h"] == 0 and x["setor"] not in setores_info:
            continue
        sm = x["sm"]
        sem = x["h"] - sum(sm.values()) / 60
        pct = (x["h"] * 60 / total_min * 100) if total_min else 0
        w(f"| {x['setor']} | {fmt(x['h'], 2)} | {fmt(x['hs'], 2)} | {fmt(x['hs'] * 52 / 12)} | {fmt(pct, 0)}% | "
          f"{fmt(sm.get('S', 0) / 60, 2)} | {fmt(sm.get('A', 0) / 60, 2)} | {fmt(sm.get('H', 0) / 60, 2)} | "
          f"{fmt(sem, 2)} | {x['interr']} |")
    w(f"| **Total** | **{fmt(total_min / 60, 2)}** | **{fmt(total_min / 60 * fator, 2)}** | "
      f"**{fmt(total_min / 60 * fator * 52 / 12)}** | 100% | | | | | **{sum(interr_setor.values())}** |")
    w("")
    w("Horas por mês = horas por semana × 52 ÷ 12. Muitos blocos interrompidos no mesmo setor indicam setor sem fluxo e pesam no incômodo.")
    w("")

    pessoas = sorted(pessoa_setor)
    if not a.sem_pessoas and len(pessoas) > 1:
        cols = [s for s in ordem if min_setor.get(s)]
        w("## 2. Horas por pessoa")
        w("")
        w("Para a conversa com a equipe e para decidir quem entrevistar de novo. Nunca como cobrança individual.")
        w("")
        w("| Pessoa | " + " | ".join(cols) + " | Total | Setor com mais horas |")
        w("|---|" + "---|" * (len(cols) + 2))
        for p in pessoas:
            vals = [pessoa_setor[p].get(s, 0) / 60 for s in cols]
            tot = sum(vals)
            mais = cols[vals.index(max(vals))] if tot else ""
            w(f"| {p} | " + " | ".join(fmt(v, 2) for v in vals) + f" | {fmt(tot, 2)} | {mais} |")
        w("")

    w("## 3. As 10 atividades que mais consumiram horas")
    w("")
    w("| # | Atividade | Setor | Horas na semana registrada | Blocos | Marcação mais usada |")
    w("|---|---|---|---|---|---|")
    top10 = sorted(ativ.items(), key=lambda kv: -kv[1]["min"])[:10]
    for i, ((s, _), v) in enumerate(top10, 1):
        marc = v["sah"].most_common(1)[0][0] if v["sah"] else "sem marcação"
        w(f"| {i} | {v['nome']} | {s} | {fmt(v['min'] / 60, 2)} | {v['vezes']} | {marc} |")
    w("")

    w("## 4. Linhas suspeitas (confirme antes de corrigir)")
    w("")
    if suspeitas or avisos_set:
        for n, t in sorted(suspeitas, key=lambda x: x[0]):
            w(f"- {'Linha ' + str(n) + ': ' if n else ''}{t}")
        for t in avisos_set:
            w(f"- {t}")
    else:
        w("- Nenhuma linha suspeita.")
    w("")

    w("## 5. Pontuação por setor")
    w("")
    w("| Posição | Setor | Horas por semana | Incômodo | Horas × incômodo | Potencial de IA | Pontuação completa | Dono |")
    w("|---|---|---|---|---|---|---|---|")
    fora = []
    for x in full + [y for y in linhas_setor if y["s"] is None and (y["h"] > 0 or y["setor"] in setores_info)]:
        if x["s"] is None:
            motivo = []
            if x["h"] == 0:
                motivo.append("sem horas no registro")
            if not x["inc"]:
                motivo.append("sem incômodo")
            if not x["pot"]:
                motivo.append("sem potencial")
            fora.append(f"{x['setor']} ({', '.join(motivo)})")
            continue
        pot_txt = f"{x['pot']}" + (" (sugerido pelas marcações, confirmar)" if x["pot_origem"] != "informado" else "")
        w(f"| {pos[x['setor']]} | {x['setor']} | {fmt(x['hs'])} | {x['inc']} | {fmt(x['d'])} | {pot_txt} | "
          f"**{fmt(x['s'])}** | {x['dono'] or '[A DEFINIR]'} |")
    w("")
    if fora:
        w("Fora da pontuação: " + "; ".join(fora) + ".")
        w("")
    sugestoes = [x for x in linhas_setor if x["pot_sug"] is not None and x["pot_origem"] == "informado"
                 and x["pot_sug"] != x["pot"]]
    if sugestoes:
        w("Potencial informado diferente do que as marcações S, A e H do registro sugerem "
          "(parte das horas marcadas que está em S ou A):")
        for x in sugestoes:
            w(f"- {x['setor']}: informado {x['pot']}, marcações sugerem {x['pot_sug']} "
              f"(marcação em {fmt(x['cobertura'], 0)}% das horas do setor). Vale rever na classificação.")
        w("")

    w("## 6. Leitura do resultado")
    w("")
    w(f"- Setor-alvo pela pontuação completa: {top['setor'] if top else '[A DEFINIR]'}")
    w(f"- Setor-alvo pelo diagnóstico (horas × incômodo, com horas medidas): {top_d['setor'] if top_d else '[A DEFINIR]'}")
    if alvo_diag_txt:
        w(f"- Setor-alvo provisório do diagnóstico (informado): {nome_ref}")
    w(f"- Comparação usada na regra: {origem_ref}.")
    w("")
    w(msg)
    if alerta_ref:
        w("")
        w(alerta_ref)
    w("")
    w(f"**setor_alvo:** {alvo}  ")
    w(f"**proximo_da_fila:** {prox}")
    w("")
    w("O modelo de negócio orienta, o mapa decide. A decisão final é do escritório.")
    w("")

    w("## 7. Ranking em texto")
    w("")
    w("Para colar no Projeto do escritório no Claude ou na pasta do escritório.")
    w("")
    w("```")
    w("Ranking de setores · pontuação = horas por semana × incômodo × potencial de IA")
    w("")
    if not full:
        w("Nenhum setor com os três campos preenchidos.")
    for i, x in enumerate(full, 1):
        w(f"{i}. {x['setor']}: {fmt(x['hs'])} h × {x['inc']} × {x['pot']} = {fmt(x['s'])} (horas × incômodo = {fmt(x['d'])})")
    w("")
    if top:
        w(f"Setor-alvo pela pontuação completa: {top['setor']}")
    if top_d:
        w(f"Setor-alvo pelo diagnóstico (horas × incômodo): {top_d['setor']}")
    w(f"Setor-alvo decidido: {alvo} · Próximo da fila: {prox}")
    w(f"Horas por semana mapeadas: {fmt(total_min / 60 * fator)}")
    w("```")

    texto = "\n".join(out) + "\n"
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Ranking gravado em {a.saida}")
    else:
        sys.stdout.write(texto)


if __name__ == "__main__":
    main()
