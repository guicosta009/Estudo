#!/usr/bin/env python3
"""Gera a planilha de registro de horas do escritório (.xlsx).

Abas: Comece aqui, Configuração, Registro, Resumo por setor, Por pessoa,
Classificação de atividades. As colunas cinzas têm fórmula; as amarelas são
para preencher. Nada de dado de cliente na planilha.

Uso:
  python3 gerar_planilha_horas.py SAIDA.xlsx --escritorio "Nome do escritório"
      [--pessoas "Advogada titular; Assistente; Estagiário"]
      [--inicio 2026-03-02] [--dias 5] [--valor-hora 120]
      [--setor-extra "Produção de peças · Previdenciário"] [--solo]

Requer openpyxl. Sem ele, o script explica como instalar e indica o modelo
em CSV/TSV (assets/registro-de-horas.tsv) como alternativa.
"""
import argparse
import datetime
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.formatting.rule import FormulaRule, ColorScaleRule
    from openpyxl.utils import get_column_letter as L
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "A biblioteca openpyxl não está instalada, e ela é necessária para gerar o .xlsx.\n"
        "Para instalar, rode no terminal:\n"
        "    python3 -m pip install openpyxl\n"
        "(se o pip reclamar de ambiente gerenciado, use: python3 -m pip install --user openpyxl)\n"
        "Alternativa sem instalar nada: use o modelo assets/registro-de-horas.tsv desta skill.\n"
        "Ele tem as mesmas colunas da aba Registro e abre em qualquer planilha.\n"
    )
    sys.exit(2)

SETORES = [
    "Atendimento e triagem", "Comercial", "Produção de peças", "Prazos e controladoria",
    "Audiências e diligências", "Financeiro e cobrança", "Relacionamento com o cliente",
    "Marketing e conteúdo", "Gestão de equipe", "Administrativo",
]
CANAIS = ["WhatsApp", "E-mail", "Telefone", "Presencial", "Software jurídico",
          "Sistema do tribunal", "Planilha ou documento", "Reunião on-line", "Outro"]
N_REG = 500     # linhas de registro
N_PESS = 12     # linhas de pessoas
N_CLASS = 100   # linhas de classificação

# Paleta neutra
TITULO = "1F3A4D"; CAB = "2F5D73"; TOTAL = "1F3A4D"; CLARO = "E9EFF2"; CINZA_TXT = "5F6B70"
AMARELO = "FFF8E1"; CINZA = "EEF2F3"; DESTAQUE = "FCE6D6"; ESCALA = "9FC9DA"


def parse_args():
    p = argparse.ArgumentParser(description="Gera a planilha de registro de horas do escritório.")
    p.add_argument("saida", help="caminho do arquivo .xlsx a gerar")
    p.add_argument("--escritorio", default="", help="nome do escritório")
    p.add_argument("--pessoas", default="",
                   help="lista de pessoas por função, separadas por ponto e vírgula")
    p.add_argument("--inicio", default="", help="data de início do registro (AAAA-MM-DD ou DD/MM/AAAA)")
    p.add_argument("--dias", type=int, default=5, help="dias úteis que serão registrados (padrão 5)")
    p.add_argument("--valor-hora", type=float, default=None, help="valor da hora em reais (opcional)")
    p.add_argument("--setor-extra", action="append", default=[],
                   help="setor separado por área, ex.: 'Produção de peças · Previdenciário' (pode repetir)")
    p.add_argument("--solo", action="store_true", help="ajusta as instruções para o escritório solo")
    return p.parse_args()


def parse_data(txt):
    if not txt:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.datetime.strptime(txt, fmt).date()
        except ValueError:
            pass
    sys.stderr.write("Data de início não reconhecida (use AAAA-MM-DD ou DD/MM/AAAA). Campo deixado em branco.\n")
    return None


def main():
    a = parse_args()
    setores = SETORES + [s for s in a.setor_extra if s.strip()]
    ns = len(setores)
    pessoas = [x.strip() for x in a.pessoas.replace("\n", ";").split(";") if x.strip()]
    if not pessoas and a.solo:
        pessoas = ["Titular"]
    if len(pessoas) > N_PESS:
        sys.stderr.write(f"Só cabem {N_PESS} pessoas na Configuração. As demais foram ignoradas.\n")
        pessoas = pessoas[:N_PESS]

    hfont = Font(name="Arial", bold=True, color="FFFFFF", size=10)
    hfill = PatternFill("solid", fgColor=CAB)
    tfill = PatternFill("solid", fgColor=TOTAL)
    lfill = PatternFill("solid", fgColor=CLARO)
    infill = PatternFill("solid", fgColor=AMARELO)
    gfill = PatternFill("solid", fgColor=CINZA)
    thin = Side(style="thin", color="CFDCE1")
    box = Border(left=thin, right=thin, top=thin, bottom=thin)
    base = Font(name="Arial", size=10)
    bold = Font(name="Arial", size=10, bold=True)
    nota = Font(name="Arial", size=9, italic=True, color=CINZA_TXT)
    wrap = Alignment(wrap_text=True, vertical="top")

    wb = Workbook()

    def title(ws, text, sub=None):
        ws["A1"] = text
        ws["A1"].font = Font(name="Arial", size=16, bold=True, color=TITULO)
        if sub:
            ws["A2"] = sub
            ws["A2"].font = Font(name="Arial", size=10, italic=True, color=CINZA_TXT)

    def header(ws, row, cols):
        for i, c in enumerate(cols, 1):
            x = ws.cell(row=row, column=i, value=c)
            x.font = hfont; x.fill = hfill; x.border = box
            x.alignment = Alignment(wrap_text=True, vertical="center")
        ws.row_dimensions[row].height = 44

    def dv_list(ws, formula, rng):
        d = DataValidation(type="list", formula1=formula, allow_blank=True, showErrorMessage=False)
        ws.add_data_validation(d)
        d.add(rng)

    nome = a.escritorio.strip() or "[NOME DO ESCRITÓRIO]"

    # ---------- Comece aqui ----------
    ws = wb.active
    ws.title = "Comece aqui"
    title(ws, f"Registro de horas · {nome}",
          "Uma semana normal de trabalho, anotada na hora. Faça uma cópia antes de usar.")
    if a.solo:
        passo2 = ("Durante a semana, lance na aba Registro o que fez: data, setor, atividade (verbo + objeto, "
                  "como 'Responder dúvida de andamento'), início e fim ou só os minutos, canal e, se quiser, "
                  "a marcação S, A ou H. No escritório solo este registro é o que mostra a verdade: anote em "
                  "que hora do dia fez cada coisa e, na Observação, o que ficou para trás enquanto fazia.")
        passo4 = ("A aba Por pessoa serve para separar o seu tempo do tempo da pessoa de apoio, se houver. "
                  "Se você trabalha sozinho, pode ignorar.")
    else:
        passo2 = ("Durante a semana, cada pessoa lança na aba Registro o que fez: data, pessoa, setor, atividade "
                  "(verbo + objeto, como 'Responder dúvida de andamento'), início e fim ou só os minutos, canal e "
                  "a marcação S, A ou H. As colunas cinzas calculam sozinhas. Ninguém está batendo ponto: o "
                  "número que interessa é o do setor.")
        passo4 = ("A aba Por pessoa mostra quanto do tempo de cada um vai para cada setor. Use para a conversa "
                  "com a equipe e para decidir quem entrevistar de novo, nunca como cobrança individual.")
    linhas = [
        ("Para que serve", "Descobrir, com número, para onde vão as horas do escritório numa semana normal. "
         "O resultado aponta o setor-alvo, por onde a organização e a automação começam."),
        ("Passo 1 · Configuração", "Na aba Configuração, preencha o nome do escritório, a data de início, quantos "
         "dias úteis você vai registrar (o ideal é 5), o valor da hora (opcional), as pessoas (por função) e, "
         "para cada setor, o incômodo (1 a 5), o potencial de IA (1 a 5) e o dono do setor."),
        ("Passo 2 · Registro", passo2),
        ("Tempo picado", "WhatsApp, ligação rápida e procurar documento somam muito. Bloco abaixo de 5 minutos "
         "vai para a rajada: um risquinho por mensagem e, no fim do dia, uma linha só com o total "
         "('12 mensagens × 4 min' = 48 minutos). No primeiro dia, cronometre 10 respostas para achar o "
         "tempo médio. Ligações: some pelo histórico do celular e acrescente uns minutos por ligação."),
        ("Passo 3 · Resumo por setor", "A aba Resumo por setor calcula sozinha as horas por semana e por mês de "
         "cada setor, a pontuação do diagnóstico (horas × incômodo), a pontuação completa (horas × incômodo × "
         "potencial de IA), o ranking e o setor-alvo pelas duas contas."),
        ("Passo 4 · Por pessoa", passo4),
        ("Passo 5 · Classificação", "A aba Classificação de atividades é o inventário do setor-alvo: uma linha "
         "por atividade, com volume, regra, risco, dado sensível e a marcação S, A ou H. É a matéria-prima do "
         "POP do setor-alvo."),
        ("S, A e H", "S · Substituição: a IA faz no lugar e alguém confere por amostra. A · Auxílio: a IA prepara, "
         "resume ou rascunha e a pessoa decide. H · Humano: continua com a pessoa (decisão, ética, conversa "
         "delicada, assinatura)."),
        ("Sigilo", "Não escreva nome de cliente, número de processo, CPF ou dado de saúde nesta planilha. "
         "Descreva a atividade, nunca o caso ('cliente de auxílio-doença' basta)."),
        ("Semana atípica", "Feriado, mutirão, metade da equipe de férias: anote o motivo na Observação e, se "
         "der, repita o registro numa semana normal."),
    ]
    r = 4
    for k, v in linhas:
        c1 = ws.cell(row=r, column=1, value=k); c1.font = Font(name="Arial", size=10, bold=True, color=CAB); c1.alignment = wrap
        c2 = ws.cell(row=r, column=2, value=v); c2.font = base; c2.alignment = wrap
        ws.row_dimensions[r].height = 58
        r += 1
    ws.column_dimensions["A"].width = 26
    ws.column_dimensions["B"].width = 110
    ws.cell(row=r + 1, column=1, value="Legenda de cores").font = bold
    c = ws.cell(row=r + 2, column=1, value="Amarelo claro"); c.fill = infill; c.font = base
    ws.cell(row=r + 2, column=2, value="Você preenche.").font = base
    c = ws.cell(row=r + 3, column=1, value="Cinza claro"); c.fill = gfill; c.font = base
    ws.cell(row=r + 3, column=2, value="Fórmula: não precisa mexer.").font = base

    # ---------- Configuração ----------
    cf = wb.create_sheet("Configuração")
    title(cf, "Configuração", "Preencha antes de começar o registro. As células amarelas são suas.")
    campos = [("Escritório", a.escritorio.strip() or None), ("Início do registro", parse_data(a.inicio)),
              ("Dias úteis registrados", a.dias if a.dias > 0 else 5), ("Valor da hora (R$)", a.valor_hora)]
    for i, (k, v) in enumerate(campos):
        cf.cell(row=4 + i, column=1, value=k).font = bold
        x = cf.cell(row=4 + i, column=2, value=v); x.fill = infill; x.border = box; x.font = base
    cf["B5"].number_format = "DD/MM/YYYY"
    cf["B7"].number_format = '"R$" #,##0.00'
    cf.cell(row=4, column=4, value="O valor da hora é opcional. Os três métodos de cálculo estão na skill medir-retorno.").font = nota

    cf.cell(row=10, column=1, value="Pessoas (por função)").font = Font(name="Arial", size=12, bold=True, color=TITULO)
    header(cf, 11, ["Nome ou função", "Observação"])
    P0 = 12
    for i in range(N_PESS):
        for j in (1, 2):
            x = cf.cell(row=P0 + i, column=j); x.fill = infill; x.border = box; x.font = base
        if i < len(pessoas):
            cf.cell(row=P0 + i, column=1, value=pessoas[i])
    PESS = f"'Configuração'!$A${P0}:$A${P0 + N_PESS - 1}"

    S0 = P0 + N_PESS + 4  # linha do primeiro setor
    cf.cell(row=S0 - 2, column=1, value="Setores").font = Font(name="Arial", size=12, bold=True, color=TITULO)
    header(cf, S0 - 1, ["Setor", "Incômodo (1 a 5)", "Potencial de IA (1 a 5)", "Dono do setor"])
    for i, s in enumerate(setores):
        x = cf.cell(row=S0 + i, column=1, value=s); x.font = bold; x.border = box
        for j in (2, 3, 4):
            y = cf.cell(row=S0 + i, column=j); y.fill = infill; y.border = box; y.font = base
            if j < 4:
                y.alignment = Alignment(horizontal="center")
    S1 = S0 + ns - 1
    SETR = f"'Configuração'!$A${S0}:$A${S1}"
    n1 = S1 + 2
    cf.cell(row=n1, column=1, value="Incômodo: 1 quase não lembro que existe · 2 dá trabalho, mas anda sozinho · 3 incomoda toda semana · 4 gera retrabalho, atraso ou hora extra · 5 cliente reclama, prazo em risco ou tira o sono.").font = nota
    cf.cell(row=n1 + 1, column=1, value="Potencial de IA (parte das horas do setor que cabe em S ou A): 1 menos de 20% · 2 de 20% a 40% · 3 de 40% a 60% · 4 de 60% a 80% · 5 mais de 80%.").font = nota
    cf.cell(row=n1 + 2, column=1, value="Setor que não existe no escritório: deixe incômodo e potencial em branco. Setor terceirizado continua: contam as horas de coordenação.").font = nota
    C0 = n1 + 5
    cf.cell(row=C0 - 1, column=1, value="Listas (não mexer)").font = Font(name="Arial", size=9, bold=True, color=CINZA_TXT)
    for i, c in enumerate(CANAIS):
        cf.cell(row=C0 + i, column=1, value=c).font = Font(name="Arial", size=9, color=CINZA_TXT)
    CANR = f"'Configuração'!$A${C0}:$A${C0 + len(CANAIS) - 1}"
    for col, w in zip("ABCD", (40, 22, 22, 26)):
        cf.column_dimensions[col].width = w
    dv15 = DataValidation(type="whole", operator="between", formula1="1", formula2="5", showErrorMessage=True,
                          errorTitle="Valor inválido", error="Use um número inteiro de 1 a 5.")
    cf.add_data_validation(dv15)
    dv15.add(f"B{S0}:C{S1}")
    dvd = DataValidation(type="whole", operator="between", formula1="1", formula2="31", showErrorMessage=True,
                         errorTitle="Valor inválido", error="Informe quantos dias úteis foram registrados.")
    cf.add_data_validation(dvd)
    dvd.add("B6")

    # ---------- Registro ----------
    rg = wb.create_sheet("Registro")
    title(rg, "Registro da semana", "Uma linha por bloco de trabalho. Preencha as colunas amarelas; as cinzas calculam sozinhas.")
    cols = ["Data", "Pessoa", "Setor", "Atividade (verbo + objeto)", "Início", "Fim",
            "Minutos (se não usou início e fim)", "Canal", "Interrompida?", "S / A / H", "Observação",
            "Minutos considerados", "Horas"]
    header(rg, 4, cols)
    for i, w in enumerate([12, 20, 30, 40, 9, 9, 16, 18, 13, 10, 34, 14, 9], 1):
        rg.column_dimensions[L(i)].width = w
    R0, R1 = 5, 4 + N_REG
    for r in range(R0, R1 + 1):
        for c in range(1, 12):
            x = rg.cell(row=r, column=c); x.fill = infill; x.border = box; x.font = base
        rg.cell(row=r, column=1).number_format = "DD/MM/YYYY"
        rg.cell(row=r, column=5).number_format = "HH:MM"
        rg.cell(row=r, column=6).number_format = "HH:MM"
        m = rg.cell(row=r, column=12, value=f'=IF(G{r}<>"",G{r},IF(AND(E{r}<>"",F{r}<>""),ROUND((F{r}-E{r})*1440,0),0))')
        h = rg.cell(row=r, column=13, value=f'=IF(L{r}=0,"",ROUND(L{r}/60,2))')
        for x in (m, h):
            x.fill = gfill; x.border = box; x.font = base
    rg.freeze_panes = "A5"
    dv_list(rg, "=" + PESS, f"B{R0}:B{R1}")
    dv_list(rg, "=" + SETR, f"C{R0}:C{R1}")
    dv_list(rg, "=" + CANR, f"H{R0}:H{R1}")
    dv_list(rg, '"Sim,Não"', f"I{R0}:I{R1}")
    dv_list(rg, '"S,A,H"', f"J{R0}:J{R1}")
    RS = f"Registro!$C${R0}:$C${R1}"
    RH = f"Registro!$L${R0}:$L${R1}"
    RP = f"Registro!$B${R0}:$B${R1}"
    RJ = f"Registro!$J${R0}:$J${R1}"
    RI = f"Registro!$I${R0}:$I${R1}"

    # ---------- Resumo por setor ----------
    rs = wb.create_sheet("Resumo por setor")
    title(rs, "Resumo por setor", "Calculado a partir do Registro e da Configuração. Não precisa preencher nada aqui.")
    T0 = 10
    T1 = T0 + ns - 1
    rs["A4"] = "Horas registradas no total"; rs["B4"] = f"=ROUND(SUM({RH})/60,1)"
    rs["A5"] = "Horas por semana (estimadas)"; rs["B5"] = f"=ROUND(SUM(C{T0}:C{T1}),1)"
    rs["A6"] = "Setor-alvo pelo diagnóstico (horas × incômodo)"
    rs["B6"] = f'=IF(MAX(G{T0}:G{T1})=0,"Preencha o registro e o incômodo",INDEX(A{T0}:A{T1},MATCH(MAX(G{T0}:G{T1}),G{T0}:G{T1},0)))'
    rs["A7"] = "Setor-alvo pela pontuação completa (× potencial de IA)"
    rs["B7"] = f'=IF(MAX(H{T0}:H{T1})=0,"Preencha também o potencial de IA",INDEX(A{T0}:A{T1},MATCH(MAX(H{T0}:H{T1}),H{T0}:H{T1},0)))'
    for r in range(4, 8):
        rs.cell(row=r, column=1).font = bold
        x = rs.cell(row=r, column=2); x.font = Font(name="Arial", size=11, bold=True, color=CAB); x.fill = lfill; x.border = box
    rs["B4"].number_format = "0.0"; rs["B5"].number_format = "0.0"
    cols = ["Setor", "Horas registradas", "Horas por semana", "Horas por mês", "Incômodo", "Potencial de IA",
            "Pontuação diagnóstico", "Pontuação completa", "Ranking", "% das horas", "Horas S", "Horas A",
            "Horas H", "Horas sem marcação", "Valor das horas por mês (R$)", "Blocos interrompidos"]
    header(rs, T0 - 1, cols)
    for i, s in enumerate(setores):
        r = T0 + i
        cr = S0 + i
        rs.cell(row=r, column=1, value=s).font = bold
        rs.cell(row=r, column=2, value=f"=ROUND(SUMIF({RS},A{r},{RH})/60,2)")
        rs.cell(row=r, column=3, value=f"=IF('Configuração'!$B$6>0,ROUND(B{r}/'Configuração'!$B$6*5,2),B{r})")
        rs.cell(row=r, column=4, value=f"=ROUND(C{r}*52/12,1)")
        rs.cell(row=r, column=5, value=f"=IF('Configuração'!B{cr}=\"\",0,'Configuração'!B{cr})")
        rs.cell(row=r, column=6, value=f"=IF('Configuração'!C{cr}=\"\",0,'Configuração'!C{cr})")
        rs.cell(row=r, column=7, value=f"=ROUND(C{r}*E{r},1)")
        rs.cell(row=r, column=8, value=f"=ROUND(C{r}*E{r}*F{r},1)")
        rs.cell(row=r, column=9, value=f'=IF(H{r}=0,"",RANK(H{r},$H${T0}:$H${T1}))')
        rs.cell(row=r, column=10, value=f"=IF(SUM($B${T0}:$B${T1})=0,0,B{r}/SUM($B${T0}:$B${T1}))")
        rs.cell(row=r, column=11, value=f'=ROUND(SUMIFS({RH},{RS},A{r},{RJ},"S")/60,2)')
        rs.cell(row=r, column=12, value=f'=ROUND(SUMIFS({RH},{RS},A{r},{RJ},"A")/60,2)')
        rs.cell(row=r, column=13, value=f'=ROUND(SUMIFS({RH},{RS},A{r},{RJ},"H")/60,2)')
        rs.cell(row=r, column=14, value=f"=ROUND(B{r}-K{r}-L{r}-M{r},2)")
        rs.cell(row=r, column=15, value=f"=IF('Configuração'!$B$7=\"\",\"\",ROUND(D{r}*'Configuração'!$B$7,2))")
        rs.cell(row=r, column=16, value=f'=COUNTIFS({RS},A{r},{RI},"Sim")')
        for c in range(1, 17):
            x = rs.cell(row=r, column=c); x.border = box
            if c > 1:
                x.font = base; x.alignment = Alignment(horizontal="center")
            if c in (2, 3, 4, 7, 8, 11, 12, 13, 14):
                x.number_format = "0.0#"
        rs.cell(row=r, column=10).number_format = "0%"
        rs.cell(row=r, column=15).number_format = '"R$" #,##0.00'
    r = T1 + 1
    rs.cell(row=r, column=1, value="Total").font = hfont
    for c in range(1, 17):
        rs.cell(row=r, column=c).fill = tfill; rs.cell(row=r, column=c).border = box
    for c in (2, 3, 4, 11, 12, 13, 14, 15, 16):
        col = L(c)
        x = rs.cell(row=r, column=c, value=f"=SUM({col}{T0}:{col}{T1})"); x.font = hfont
        x.alignment = Alignment(horizontal="center")
    rs.cell(row=r, column=15).number_format = '"R$" #,##0.00'
    rs.column_dimensions["A"].width = 50
    for c in range(2, 17):
        rs.column_dimensions[L(c)].width = 14
    rs.column_dimensions["O"].width = 20
    rs.conditional_formatting.add(f"A{T0}:P{T1}", FormulaRule(formula=[f"$I{T0}=1"],
                                  fill=PatternFill("solid", fgColor=DESTAQUE), font=Font(bold=True, color="6B2A10")))
    rs.conditional_formatting.add(f"H{T0}:H{T1}", ColorScaleRule(start_type="min", start_color="FFFFFF",
                                  end_type="max", end_color=ESCALA))
    k = T1 + 3
    rs.cell(row=k, column=1, value="Como ler").font = Font(name="Arial", size=11, bold=True, color=TITULO)
    notas = [
        "Horas por semana: as horas registradas divididas pelos dias úteis registrados, vezes 5. Horas por mês: horas por semana × 52 ÷ 12.",
        "Pontuação diagnóstico: horas por semana × incômodo. É a mesma conta do mapa rápido do diagnóstico, agora com horas medidas.",
        "Pontuação completa: horas por semana × incômodo × potencial de IA. A linha em destaque é o 1º lugar. Empate: vence o setor com mais horas.",
        "Se os dois setores-alvo forem diferentes: se o setor do diagnóstico tem potencial 1 ou 2, troque pelo da pontuação completa. Se tem potencial 3 ou mais, fique com o do diagnóstico e deixe o outro como próximo da fila.",
        "Horas S e A: o tempo que, pelo palpite de hoje, a IA pode assumir ou acelerar. É a matéria-prima do cálculo de retorno (skill medir-retorno).",
        "Blocos interrompidos: muitos no mesmo setor indicam setor sem fluxo, e isso pesa no incômodo.",
    ]
    for i, n in enumerate(notas):
        rs.cell(row=k + 1 + i, column=1, value=n).font = Font(name="Arial", size=9, color=CINZA_TXT)
    rs.freeze_panes = f"B{T0}"

    # ---------- Por pessoa ----------
    pp = wb.create_sheet("Por pessoa")
    title(pp, "Horas por pessoa e setor", "Para a conversa com a equipe sobre onde o tempo vai. Nunca como cobrança individual.")
    header(pp, 4, ["Pessoa"] + setores + ["Total", "Setor com mais horas"])
    cT = 2 + ns          # coluna do total
    cM = cT + 1          # coluna do setor com mais horas
    lastS = L(1 + ns)
    for i in range(N_PESS):
        r = 5 + i
        pp.cell(row=r, column=1, value=f"=IF('Configuração'!A{P0 + i}=\"\",\"\",'Configuração'!A{P0 + i})").font = bold
        for j in range(ns):
            col = L(2 + j)
            pp.cell(row=r, column=2 + j,
                    value=f'=IF($A{r}="","",ROUND(SUMIFS({RH},{RP},$A{r},{RS},{col}$4)/60,2))')
        pp.cell(row=r, column=cT, value=f'=IF($A{r}="","",SUM(B{r}:{lastS}{r}))')
        pp.cell(row=r, column=cM,
                value=f'=IF(OR($A{r}="",{L(cT)}{r}=0),"",INDEX($B$4:${lastS}$4,MATCH(MAX(B{r}:{lastS}{r}),B{r}:{lastS}{r},0)))')
        for c in range(1, cM + 1):
            x = pp.cell(row=r, column=c); x.border = box
            if c > 1:
                x.font = base; x.alignment = Alignment(horizontal="center")
    pp.column_dimensions["A"].width = 24
    for c in range(2, cT):
        pp.column_dimensions[L(c)].width = 15
    pp.column_dimensions[L(cT)].width = 10
    pp.column_dimensions[L(cM)].width = 30
    pp.conditional_formatting.add(f"B5:{lastS}{4 + N_PESS}", ColorScaleRule(start_type="num", start_value=0,
                                  start_color="FFFFFF", end_type="max", end_color=ESCALA))

    # ---------- Classificação de atividades ----------
    ca = wb.create_sheet("Classificação de atividades")
    title(ca, "Classificação de atividades", "Inventário do setor-alvo (ou de todos): uma linha por atividade. Base do POP do setor.")
    cols = ["Setor", "Atividade (verbo + objeto)", "Horas por semana", "Volume por mês", "Frequência",
            "Regra clara?", "Risco se errar", "Dado sensível?", "Marcação S / A / H",
            "Justificativa em uma linha", "Cuidado obrigatório"]
    header(ca, 4, cols)
    for i, w in enumerate([30, 40, 12, 12, 14, 13, 13, 13, 13, 40, 32], 1):
        ca.column_dimensions[L(i)].width = w
    K0, K1 = 5, 4 + N_CLASS
    for r in range(K0, K1 + 1):
        for c in range(1, 12):
            x = ca.cell(row=r, column=c); x.fill = infill; x.border = box; x.font = base
    dv_list(ca, "=" + SETR, f"A{K0}:A{K1}")
    for rng, opts in [(f"E{K0}:E{K1}", '"Diária,Semanal,Mensal,Eventual"'), (f"F{K0}:F{K1}", '"Sim,Parcial,Não"'),
                      (f"G{K0}:G{K1}", '"Baixo,Médio,Alto"'), (f"H{K0}:H{K1}", '"Sim,Não"'),
                      (f"I{K0}:I{K1}", '"S,A,H"')]:
        dv_list(ca, opts, rng)
    ca.conditional_formatting.add(f"I{K0}:I{K1}", FormulaRule(formula=[f'$I{K0}="S"'], fill=PatternFill("solid", fgColor="D9EEF5")))
    ca.conditional_formatting.add(f"I{K0}:I{K1}", FormulaRule(formula=[f'$I{K0}="A"'], fill=PatternFill("solid", fgColor="E3E8F4")))
    ca.conditional_formatting.add(f"I{K0}:I{K1}", FormulaRule(formula=[f'$I{K0}="H"'], fill=PatternFill("solid", fgColor=DESTAQUE)))
    ca.freeze_panes = "C5"
    ca.cell(row=K1 + 2, column=1, value="Na dúvida entre duas siglas, fique com a mais humana: H antes de A, A antes de S. Atividade com dado sensível ou risco alto nunca vai para S sem revisão.").font = nota

    for w in wb.worksheets:
        w.sheet_view.showGridLines = False
    wb.save(a.saida)
    print(f"Planilha gerada: {a.saida} ({ns} setores, {len(pessoas)} pessoas pré-cadastradas, {N_REG} linhas de registro)")


if __name__ == "__main__":
    main()
