#!/usr/bin/env python3
"""Calculadora de investimento e retorno da automação (projeção).

Entrada: um JSON com as variáveis da calculadora. Saída: horas devolvidas por setor e por
mês, valor da hora, valor das horas devolvidas, custo mensal, investimento inicial,
retorno líquido mensal, ROI em 12 meses, payback e os avisos automáticos.

Fórmulas (SEM = 52/12, cerca de 4,33 semanas por mês):
  vh = modo "direto" ? valor_hora : faturamento_mensal / horas_produtivas
  horas devolvidas no setor por mês = h × min(%, 100)/100 × SEM
  horas devolvidas por mês = max(0, soma(h × %) - revisão) × SEM
  valor por mês = horas por mês × vh × min(aproveitamento, 100)/100
  custo mensal = ferramentas por mês
  investimento inicial = horas de implantação × (vh de implantação ou vh) + custos únicos
  líquido mensal = valor por mês - custo mensal
  ROI 12 meses = (12 × valor - (12 × custo + inicial)) / (12 × custo + inicial) × 100
  payback = inicial / líquido (meses); "não se paga" se líquido <= 0; "imediato" se inicial = 0

Chaves aceitas no JSON (nome longo ou curto):
  modo: "fat" | "direto"            metodo_valor_hora: texto livre (ex.: "faturamento")
  faturamento_mensal | fat          horas_produtivas | hp          valor_hora | vh
  ferramentas_mes | ferr            horas_implantacao | himp       valor_hora_implantacao | vimp
  custos_unicos | unico             revisao_h_semana | rev         aproveitamento_pct | aprov
  setores: lista de {"setor", "horas_semana", "reducao_pct", "origem": "estimado"|"medido"}
           reducao_pct pode ser um número ou {"min": x, "max": y} (faixa do POP).

Uso:
  python3 calcular_roi.py ENTRADA.json [--valor-hora 40] [--json] [--saida ARQUIVO.md]
Só biblioteca padrão. Todo resultado é projeção até a medição confirmar.
"""
import argparse
import json
import math
import sys

SEM = 52 / 12
CURTO = {"fat": "faturamento_mensal", "hp": "horas_produtivas", "vh": "valor_hora", "ferr": "ferramentas_mes",
         "himp": "horas_implantacao", "vimp": "valor_hora_implantacao", "unico": "custos_unicos",
         "rev": "revisao_h_semana", "aprov": "aproveitamento_pct"}


def num(v):
    """Número positivo ou 0 (negativo, vazio e inválido viram 0, como na calculadora original)."""
    try:
        x = float(str(v).replace(",", ".")) if v not in (None, "") else 0.0
    except ValueError:
        return 0.0
    return x if math.isfinite(x) and x > 0 else 0.0


def br(n, casas=1):
    s = f"{n:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def brl(n):
    return "R$ " + br(round(n), 0)


def calcular(d, reducao_de):
    """reducao_de(setor_dict) devolve o % daquele setor no cenário."""
    modo = "direto" if str(d.get("modo", "fat")).lower().startswith("dir") else "fat"
    if modo == "direto":
        vh = num(d.get("valor_hora"))
    else:
        hp = num(d.get("horas_produtivas"))
        vh = num(d.get("faturamento_mensal")) / hp if hp > 0 else 0.0
    linhas = []
    semanal = 0.0
    for s in d.get("setores", []):
        h = num(s.get("horas_semana"))
        p = min(num(reducao_de(s)), 100)
        dev = h * p / 100
        semanal += dev
        linhas.append({"setor": s.get("setor", "[SETOR]"), "h": h, "p": p, "dev_sem": dev, "dev_mes": dev * SEM,
                       "origem": s.get("origem", "estimado")})
    rev = num(d.get("revisao_h_semana"))
    horas_mes = max(0.0, semanal - rev) * SEM
    aprov = min(num(d.get("aproveitamento_pct")), 100)
    valor_mes = horas_mes * vh * aprov / 100
    custo_mes = num(d.get("ferramentas_mes"))
    vimp = num(d.get("valor_hora_implantacao")) or vh
    inicial = num(d.get("horas_implantacao")) * vimp + num(d.get("custos_unicos"))
    liquido = valor_mes - custo_mes
    base = 12 * custo_mes + inicial
    roi = (12 * valor_mes - base) / base * 100 if base > 0 else None
    if liquido <= 0:
        payback = "não se paga" if (valor_mes > 0 or custo_mes > 0 or inicial > 0) else "n/d"
        payback_meses = None
    elif inicial <= 0:
        payback, payback_meses = "imediato", 0.0
    else:
        payback_meses = inicial / liquido
        payback = br(payback_meses) + (" mês" if payback_meses <= 1 else " meses")
    avisos = []
    if vh <= 0:
        avisos.append("Falta o valor da hora." if modo == "direto" else
                      "Falta o valor da hora: preencha o faturamento médio e as horas produtivas.")
    if semanal <= 0:
        avisos.append("Preencha as horas por semana e a redução estimada em pelo menos um setor.")
    if semanal > 0 and rev >= semanal:
        avisos.append("A revisão humana nova é igual ou maior que as horas devolvidas. Do jeito que está, "
                      "a automação não devolve tempo.")
    if horas_mes > 0 and aprov <= 0:
        avisos.append("Informe o aproveitamento: quanto das horas devolvidas vai virar trabalho de fato. "
                      "Sem ele, o valor fica zero.")
    if custo_mes <= 0 and inicial <= 0:
        avisos.append("Sem custo informado, não dá para calcular ROI nem payback.")
    for s in d.get("setores", []):
        bruto = reducao_de(s)
        if num(bruto) > 100:
            avisos.append(f"Redução acima de 100% em {s.get('setor')}: a conta usou 100%. Confira o número.")
    if num(d.get("aproveitamento_pct")) > 100:
        avisos.append("Aproveitamento acima de 100%: a conta usou 100%.")
    return {"modo": modo, "vh": vh, "linhas": linhas, "semanal": semanal, "rev": rev, "horas_mes": horas_mes,
            "aprov": aprov, "valor_mes": valor_mes, "custo_mes": custo_mes, "inicial": inicial,
            "liquido": liquido, "roi": roi, "payback": payback, "payback_meses": payback_meses, "avisos": avisos}


def red(chave):
    def f(s):
        r = s.get("reducao_pct")
        if isinstance(r, dict):
            return r.get(chave, r.get("max" if chave == "min" else "min"))
        return r
    return f


def bloco(r, titulo, d):
    o = []
    w = o.append
    w(f"## {titulo}")
    w("")
    w("| Setor | Horas por semana hoje | Redução (%) | Horas devolvidas por semana | Horas devolvidas por mês | Medido ou estimado |")
    w("|---|---|---|---|---|---|")
    for x in r["linhas"]:
        w(f"| {x['setor']} | {br(x['h'])} | {br(x['p'], 0)}% | {br(x['dev_sem'])} | {br(x['dev_mes'])} | {x['origem']} |")
    w("")
    w(f"Nos setores: {br(r['semanal'])} h por semana, {br(r['semanal'] * SEM)} h por mês. "
      f"Menos revisão humana: {br(r['rev'])} h por semana, {br(r['rev'] * SEM)} h por mês. "
      f"Horas devolvidas líquidas: {br(r['horas_mes'])} h por mês.")
    w("")
    met = d.get("metodo_valor_hora") or ("faturamento" if r["modo"] == "fat" else "informado direto")
    w("| Resultado | Valor |")
    w("|---|---|")
    w(f"| Valor da hora ({met}) | {brl(r['vh'])} |")
    w(f"| Horas devolvidas por mês (já descontada a revisão) | {br(r['horas_mes'])} h |")
    w(f"| Aproveitamento | {br(r['aprov'], 0)}% |")
    w(f"| Valor das horas devolvidas por mês | {brl(r['valor_mes'])} |")
    w(f"| Custo mensal (ferramentas) | {brl(r['custo_mes'])} |")
    w(f"| Investimento inicial (implantação e custos únicos) | {brl(r['inicial'])} |")
    w(f"| Retorno líquido mensal | {brl(r['liquido'])} |")
    w(f"| ROI em 12 meses | {'n/d' if r['roi'] is None else br(r['roi'], 0) + '%'} |")
    w(f"| Payback | {r['payback']} |")
    w("")
    if r["avisos"]:
        w("Avisos:")
        for a in r["avisos"]:
            w(f"- {a}")
        w("")
    return o


def main():
    ap = argparse.ArgumentParser(description="Calculadora de investimento e retorno da automação.")
    ap.add_argument("entrada", help="arquivo JSON com as variáveis")
    ap.add_argument("--valor-hora", type=float, default=None,
                    help="roda com este valor da hora (modo direto), por exemplo o custo-hora do colaborador")
    ap.add_argument("--json", action="store_true", help="saída em JSON em vez de markdown")
    ap.add_argument("--saida", default="")
    a = ap.parse_args()
    with open(a.entrada, encoding="utf-8") as f:
        bruto = json.load(f)
    d = {CURTO.get(k, k): v for k, v in bruto.items()}
    if isinstance(d.get("set"), list) and not d.get("setores"):
        d["setores"] = [{"setor": f"Setor {i + 1}", "horas_semana": x[0], "reducao_pct": x[1]}
                        for i, x in enumerate(d["set"])]
    if a.valor_hora is not None:
        d["modo"], d["valor_hora"] = "direto", a.valor_hora
        d["metodo_valor_hora"] = (d.get("metodo_valor_hora_alternativo") or "informado na linha de comando")
    faixa = any(isinstance(s.get("reducao_pct"), dict) for s in d.get("setores", []))
    cenarios = [("min", "Cenário mínimo"), ("max", "Cenário máximo")] if faixa else [("min", "Projeção")]
    res = {nome: calcular(d, red(ch)) for ch, nome in cenarios}

    if a.json:
        texto = json.dumps(res, ensure_ascii=False, indent=2) + "\n"
    else:
        o = ["# Calculadora de investimento e retorno", "",
             "Projeção a partir das estimativas do escritório. Vira resultado só depois da medição "
             "(linha de base e medição depois de pelo menos 4 semanas de uso). Números de exemplo vêm "
             "marcados como exemplo.", ""]
        if d.get("descricao"):
            o += [f"Caso: {d['descricao']}", ""]
        for nome, r in res.items():
            o += bloco(r, nome, d)
        o += ["A calculadora usa um valor de hora só. Se a maior parte das horas devolvidas é de um colaborador, "
              "rode de novo com o custo-hora dele (método 3), com `--valor-hora`, e compare. A conta mais "
              "honesta costuma ficar entre as duas.", ""]
        texto = "\n".join(o)
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Resultado gravado em {a.saida}")
    else:
        sys.stdout.write(texto)


if __name__ == "__main__":
    main()
