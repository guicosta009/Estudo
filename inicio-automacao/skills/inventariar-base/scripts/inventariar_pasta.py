#!/usr/bin/env python3
"""Inventário da pasta de modelos do escritório, sem mexer em nada.

Modo 1, inventário (só lê nomes, extensões, datas, tamanhos e hash):
    python3 inventariar_pasta.py <pasta-de-modelos> --saida <pasta-de-saida>
        [--pops <pasta>/escritorio/03-pops]
        [--setor-alvo <setor>]
        [--estrutura escritorio|drive]
        [--excluir NOME] [--liberar-pasta NOME]
        [--anos-parado 2] [--sem-hash] [--limite-md 300]

    Grava em <pasta-de-saida>: inventario.md, inventario.tsv,
    plano-de-reorganizacao.tsv e INDICE-rascunho.md.

Modo 2, aplicar o plano depois do ok do advogado (só copia):
    python3 inventariar_pasta.py --aplicar plano-de-reorganizacao.tsv
        --origem <pasta-de-modelos> --destino <pasta>/escritorio/04-base
        [--simular] [--registro <arquivo.md>]

    Copia com shutil.copy2 só as linhas com ok_do_advogado = sim. Cria as
    pastas, nunca sobrescreve, nunca move nem apaga o original, nunca copia
    pasta de cliente e exige anonimizacao_conferida = sim nas linhas com alerta.

Só biblioteca padrão. Não abre o conteúdo dos documentos e não acessa a internet.
"""

import argparse
import csv
import datetime as dt
import hashlib
import os
import re
import shutil
import sys
import unicodedata

HOJE = dt.date.today()

# ---------------------------------------------------------------- setores

SETORES = [
    ("atendimento-e-triagem", "Atendimento e triagem", "ATD"),
    ("comercial", "Comercial", "COM"),
    ("producao-de-pecas", "Produção de peças", "PEC"),
    ("prazos-e-controladoria", "Prazos e controladoria", "PRZ"),
    ("audiencias-e-diligencias", "Audiências e diligências", "AUD"),
    ("financeiro-e-cobranca", "Financeiro e cobrança", "FIN"),
    ("relacionamento-com-o-cliente", "Relacionamento com o cliente", "REL"),
    ("marketing-e-conteudo", "Marketing e conteúdo", "MKT"),
    ("gestao-de-equipe", "Gestão de equipe", "EQP"),
    ("administrativo", "Administrativo", "ADM"),
]
NOME_SETOR = {s: n for s, n, _ in SETORES}
NOME_SETOR["comum"] = "Comum (todos os setores)"
SIGLA_SETOR = {s: g for s, _, g in SETORES}

# Palavras-chave por setor. "*" no fim casa qualquer final (contestac* casa contestacao).
# Termo com mais de uma palavra vale 2 pontos; termo de uma palavra vale 1.
KW_SETOR = {
    "atendimento-e-triagem": [
        "triagem", "primeiro contato", "atendimento*", "consulta inicial", "boas vindas",
        "ficha de triagem", "pre atendimento", "qualificac*",
    ],
    "comercial": [
        "proposta*", "honorario*", "contrato de honorarios", "contrato*", "procurac*",
        "hipossuficiencia", "desconto*", "orcamento*",
    ],
    "producao-de-pecas": [
        "peticao", "peticoes", "inicial", "iniciais", "contestac*", "recurso*", "apelac*",
        "replica*", "manifestac*", "embargo*", "agravo*", "parecer*", "memoria*", "quesito*",
        "impugnac*", "calculo*", "tese", "teses", "cumprimento de sentenca", "peca", "pecas",
        "minuta*", "requerimento*", "reclamatoria*", "inominado", "contrarrazo*",
    ],
    "prazos-e-controladoria": [
        "prazo*", "publicac*", "intimac*", "controladoria", "agenda*", "feriado*",
        "distribuic*", "diario oficial",
    ],
    "audiencias-e-diligencias": [
        "audiencia*", "diligencia*", "preposto*", "preposic*", "substabelecimento*",
        "correspondente*", "ata de audiencia", "testemunha*",
    ],
    "financeiro-e-cobranca": [
        "cobranca*", "boleto*", "inadimplen*", "regua*", "repasse*", "financeiro*", "recibo*",
        "renegociac*", "nota fiscal", "fluxo de caixa",
    ],
    "relacionamento-com-o-cliente": [
        "mensage*", "whatsapp", "andamento*", "faq", "perguntas frequentes", "resumo mensal",
        "relevancia", "movimentac*", "respostas prontas",
    ],
    "marketing-e-conteudo": [
        "post", "posts", "instagram", "conteudo*", "marketing", "publicidade", "carrossel",
        "reels", "video*", "linkedin", "newsletter", "site", "blog", "provimento 205",
    ],
    "gestao-de-equipe": [
        "onboarding", "novo colaborador", "colaborador*", "treinamento*", "estagiari*",
        "reuniao*", "ata de reuniao", "acessos", "ferias", "confidencialidade", "equipe",
    ],
    "administrativo": [
        "padrao de nomes", "padrao nomes", "pastas", "arquivo morto", "protocolo*",
        "digitalizac*", "descarte", "politica de dados", "recebimento de documentos",
    ],
}

AREAS = [
    ("previdenciario", ["previdenciari*", "prev", "inss", "aposentadoria*", "auxilio*", "bpc", "loas",
                        "beneficio*", "pensao por morte", "cnis", "ppp", "ltcat", "salario maternidade",
                        "rural", "segurado*"]),
    ("trabalhista", ["trabalhist*", "trab", "reclamatoria*", "reclamacao trabalhista", "rescisao",
                     "rescisori*", "horas extras", "trct", "fgts", "justa causa", "vinculo*"]),
    ("familia", ["familia", "fam", "divorcio*", "alimentos", "pensao alimenticia", "guarda",
                 "uniao estavel", "partilha", "visitas"]),
    ("consumidor", ["consumidor*", "cdc", "negativac*", "procon", "fatura*", "plano de saude"]),
    ("civel", ["civel", "civil", "despejo", "usucapiao", "execucao de titulo"]),
    ("criminal", ["criminal", "penal", "habeas", "denuncia", "inquerito", "resposta a acusacao"]),
]
AREAS_RESTRITAS = {"familia", "criminal"}
NOME_AREA = {"previdenciario": "Previdenciário", "trabalhista": "Trabalhista", "familia": "Família",
             "consumidor": "Consumidor", "civel": "Cível", "criminal": "Criminal"}
PALAVRAS_DE_AREA = {"previdenciario", "previdenciaria", "prev", "trabalhista", "trab", "familia", "fam",
                    "consumidor", "civel", "civil", "criminal", "penal"}

# ---------------------------------------------------------------- tipos e esqueletos

TIPOS = ["modelo", "checklist", "critério", "tabela", "roteiro", "política", "resposta aprovada",
         "caso de teste", "outro"]
PREFIXO_TIPO = {
    "modelo": "modelo", "checklist": "checklist", "critério": "criterios", "tabela": "tabela",
    "roteiro": "roteiro", "política": "politica", "resposta aprovada": "respostas-aprovadas",
    "caso de teste": "caso", "outro": "",
}
# esqueleto da montar-base: (setor, tipo)
ESQUELETOS = {
    "criterios-relevancia-movimentacao": ("relacionamento-com-o-cliente", "critério"),
    "modelos-mensagem-por-categoria": ("relacionamento-com-o-cliente", "modelo"),
    "faq-clientes": ("relacionamento-com-o-cliente", "resposta aprovada"),
    "roteiro-triagem-por-area": ("atendimento-e-triagem", "roteiro"),
    "checklist-documentos-por-tipo-de-caso": ("atendimento-e-triagem", "checklist"),
    "checklist-revisao-peca": ("producao-de-pecas", "checklist"),
    "tabela-interna-honorarios": ("comercial", "tabela"),
    "regua-de-cobranca": ("financeiro-e-cobranca", "política"),
    "padrao-nomes-e-pastas": ("comum", "critério"),
    "checklist-etico-publicidade": ("marketing-e-conteudo", "checklist"),
}
PALAVRAS_DE_TIPO = {"modelo", "modelos", "minuta", "minutas", "template", "templates", "checklist",
                    "checklists", "check", "list", "lista", "tabela", "tabelas", "planilha", "roteiro",
                    "criterio", "criterios", "politica", "padrao", "padroes", "respostas", "resposta",
                    "faq", "arquivo", "documento", "doc"}
PECAS = ["peticao", "inicial", "contestac*", "recurso*", "apelac*", "replica*", "manifestac*",
         "embargo*", "agravo*", "parecer*", "memoria*", "quesito*", "impugnac*", "contrarrazo*",
         "requerimento*", "reclamatoria*", "procurac*", "contrato*", "proposta*", "declarac*",
         "notificac*", "acordo*"]

# ---------------------------------------------------------------- dado sensível

SENSIVEL_CASO = ["cpf", "rg", "cnh", "laudo*", "atestado*", "cid", "exame*", "prontuario*", "receita medica",
                 "holerite*", "contracheque*", "extrato*", "cnis", "ctps", "certidao*", "comprovante*",
                 "irpf", "imposto de renda", "boletim de ocorrencia", "medida protetiva", "protetiva*",
                 "violencia", "crianca*", "menor", "menores", "adolescente*", "segredo de justica",
                 "sigilo*", "dados bancarios", "conta bancaria", "cartao de credito", "assinad*"]
CREDENCIAL = ["senha*", "gov br", "govbr", "certificado digital", "token", "login*"]
LIGA_PROCESSO = ["processo*", "proc", "autos", "cliente*", "acao", "x", "vs", "contra", "caso"]

PRIMEIROS_NOMES = set("""
joao jose maria ana antonio francisco carlos paulo pedro lucas luiz luis marcos gabriel rafael daniel
marcelo bruno eduardo felipe rodrigo manoel manuel mateus matheus andre fernando fabio leonardo gustavo
guilherme ricardo sergio jorge roberto claudio adriana juliana marcia fernanda patricia aline sandra
camila amanda bruna jessica leticia julia luciana vanessa mariana gabriela vera beatriz larissa raimunda
rita sonia tereza teresa cristina carla renata simone debora roberta priscila tatiana elaine helena
lucia alice laura sofia valentina isabela heloisa joana sebastiao raimundo edson geraldo benedito
miguel arthur heitor davi bernardo samuel enzo joaquim otavio vitor victor thiago tiago diego alexandre
henrique caio igor renato sandro silvio wagner wellington wesley anderson cleber edilson ivone neide
rosangela rosana silvana elisangela cleide marlene aparecida conceicao fatima regina angela monica
denise carolina natalia bianca livia viviane kelly sueli solange irene celia dalva zilda marco
""".split())
SOBRENOMES = set("""
silva santos oliveira souza sousa rodrigues ferreira alves pereira lima gomes costa ribeiro martins
carvalho almeida lopes soares fernandes vieira barbosa rocha nascimento andrade moreira nunes marques
machado mendes freitas ramos goncalves santana teixeira araujo melo mello correia batista moura
cavalcanti monteiro pinto reis castro azevedo barros cunha farias medeiros prado queiroz siqueira
""".split())
MESES = {"janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro",
         "outubro", "dezembro"}
EXCECOES_NOME = ["maria da penha"]

# ---------------------------------------------------------------- marcas de versão

MARCAS_VERSAO = [
    ("cópia", r"copia de|copia|copy"),
    ("final", r"versao final|final\d*"),
    ("vN", r"v\d+(?: \d+)?|versao \d+"),
    ("revisado", r"revisad[oa]\d*|rev\d*"),
    ("novo", r"nov[oa]\d*"),
    ("antigo", r"antig[oa]s?|velh[oa]s?|obsolet[oa]s?"),
    ("não usar", r"nao usar|nao use|nao utilizar"),
    ("usar este", r"usar (?:este|esse|esta|essa)"),
    ("atualizado", r"atualizad[oa]|atual"),
    ("definitivo", r"definitiv[oa]|ultim[oa]|agora vai|corrigid[oa]|editad[oa]|bkp|backup|ok"),
    ("data", r"\d{4} \d{2} \d{2}|\d{2} \d{2} \d{4}|\d{8}|(?:19|20)\d{2}"),
]
MARCAS_DESCARTE = {"antigo", "não usar"}

STOP = {"de", "da", "do", "das", "dos", "e", "para", "por", "com", "a", "o", "as", "os", "em", "no", "na",
        "nos", "nas", "um", "uma", "ao", "aos", "se", "que", "the", "pra", "pro"}
ABREV = {"prev": "previdenciario", "trab": "trabalhista", "fam": "familia", "doc": "documentos",
         "docs": "documentos", "msg": "mensagem", "msgs": "mensagens", "crit": "criterios"}

LIXO_NOMES = {".ds_store", "thumbs.db", "desktop.ini", "icon\r"}
PASTAS_SISTEMA = {"$recycle.bin", "system volume information", "__macosx", ".git", "__pycache__"}
ATALHOS_NUVEM = {"gdoc", "gsheet", "gslides", "gform", "gdraw", "gmap", "gsite", "url", "webloc", "lnk"}

# ---------------------------------------------------------------- utilidades


def normalizar(texto):
    t = unicodedata.normalize("NFD", str(texto))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return t.lower()


def texto_busca(texto):
    t = re.sub(r"[^a-z0-9]+", " ", normalizar(texto))
    return " " + re.sub(r"\s+", " ", t).strip() + " "


_CACHE = {}


def termo_re(termo):
    if termo not in _CACHE:
        partes = []
        for p in termo.split():
            partes.append(re.escape(p[:-1]) + r"[a-z0-9]*" if p.endswith("*") else re.escape(p))
        _CACHE[termo] = re.compile(r"(?<![a-z0-9])" + " ".join(partes) + r"(?![a-z0-9])")
    return _CACHE[termo]


def tem(t, termo):
    return bool(termo_re(termo).search(t))


def achados(t, termos):
    return [x.replace("*", "") for x in termos if tem(t, x)]


def tamanho_legivel(n):
    if n < 1024:
        return "%d B" % n
    for un in ("KB", "MB", "GB"):
        n /= 1024.0
        if n < 1024 or un == "GB":
            return ("%.1f %s" % (n, un)).replace(".", ",")
    return str(n)


def limpar_celula(v):
    return str(v if v is not None else "").replace("\t", " ").replace("\n", " ").replace("\r", " ")


def md_celula(v):
    return limpar_celula(v).replace("|", "/")


VOCAB = set(STOP) | PALAVRAS_DE_TIPO | PALAVRAS_DE_AREA | set(ABREV)
VOCAB_PREFIXOS = set()
for _lista in list(KW_SETOR.values()) + [a[1] for a in AREAS] + [PECAS, SENSIVEL_CASO, CREDENCIAL, LIGA_PROCESSO]:
    for _termo in _lista:
        for _p in _termo.split():
            if _p.endswith("*"):
                VOCAB_PREFIXOS.add(_p[:-1])
            else:
                VOCAB.add(_p)
VOCAB |= {"inss", "banco", "empresa", "ltda", "me", "sa", "modelo", "geral", "padrao", "ideias", "manual",
          "lista", "documentos", "especial", "aposentadoria", "pericia", "medica", "pericial", "assinada",
          "bancario", "equipe", "inominado", "declaracao", "embargos", "honorarios", "regras"}


def no_vocab(tok):
    if tok in VOCAB:
        return True
    return any(tok.startswith(p) for p in VOCAB_PREFIXOS if len(p) >= 4)


# ---------------------------------------------------------------- números e nomes

RE_CNJ = re.compile(r"(?<!\d)\d{7}-?\d{2}\.?\d{4}\.?\d\.?\d{2}\.?\d{4}(?!\d)")
RE_CPF = re.compile(r"(?<!\d)\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?!\d)")
RE_LONGO = re.compile(r"(?<!\d)\d{9,}(?!\d)")


def numeros_sensiveis(texto):
    achou = []
    if RE_CNJ.search(texto):
        achou.append("número de processo")
        texto = RE_CNJ.sub(" ", texto)
    if RE_CPF.search(texto):
        achou.append("número que parece CPF")
        texto = RE_CPF.sub(" ", texto)
    if RE_LONGO.search(texto):
        achou.append("número longo (documento, benefício ou processo)")
    return achou


def mascarar_numeros(texto):
    texto = RE_CNJ.sub("[PROCESSO]", texto)
    texto = RE_CPF.sub("[DOC]", texto)
    return RE_LONGO.sub("[NÚMERO]", texto)


def detectar_nomes(texto):
    """Devolve (tokens que parecem nome de pessoa, forte?)."""
    n = normalizar(texto)
    for exc in EXCECOES_NOME:
        n = n.replace(exc, " ")
    toks = re.findall(r"[a-z]+", n)
    marcados, forte = set(), False
    for i, tok in enumerate(toks):
        prox = toks[i + 1] if i + 1 < len(toks) else ""
        if tok in PRIMEIROS_NOMES and tok not in MESES:
            marcados.add(tok)
            if prox and (prox in SOBRENOMES or prox in PRIMEIROS_NOMES or
                         (len(prox) >= 3 and not no_vocab(prox) and prox not in MESES)):
                marcados.add(prox)
                forte = True
        elif tok in SOBRENOMES and prox in SOBRENOMES:
            marcados.update([tok, prox])
            forte = True
    return marcados, forte


def mascarar(texto, nomes):
    texto = mascarar_numeros(texto)
    if not nomes:
        return texto
    partes = re.split(r"([A-Za-zÀ-ÿ̀-ͯ]+)", texto)
    saida = []
    for p in partes:
        if p and normalizar(p) in nomes:
            saida.append("[NOME]")
        else:
            saida.append(p)
    return "".join(saida)


def eh_pasta_de_cliente(nome):
    t = texto_busca(nome)
    if re.match(r" (clientes?|casos?|processos?|autos|dossies?|pastas? (?:de |dos |do )?clientes?) ", t):
        return "nome de pasta de caso ou de cliente"
    if tem(t, "cliente*"):
        return "a palavra cliente no nome da pasta"
    if numeros_sensiveis(nome):
        return "número de processo ou documento no nome da pasta"
    nomes, forte = detectar_nomes(nome)
    if forte:
        return "nome de pessoa no nome da pasta"
    return None


# ---------------------------------------------------------------- classificação


def marcas_de_versao(nome_sem_ext):
    bruto = normalizar(nome_sem_ext)
    marcas = []
    if re.search(r"\(\s*\d+\s*\)", bruto):
        marcas.append("(N)")
    t = texto_busca(nome_sem_ext)
    resto = t
    for rotulo, padrao in MARCAS_VERSAO:
        rx = re.compile(r"(?<![a-z0-9])(?:" + padrao + r")(?![a-z0-9])")
        if rx.search(resto):
            marcas.append(rotulo)
            resto = rx.sub(" ", resto)
    resto = re.sub(r"(?<![a-z0-9])\d+(?![a-z0-9])", " ", resto) if "(N)" in marcas else resto
    toks = [w for w in resto.split() if w]
    while toks and toks[0] in STOP:
        toks.pop(0)
    while toks and toks[-1] in STOP:
        toks.pop()
    return marcas, " ".join(toks)


def pontuar_setor(t_nome, t_pasta):
    pontos = {}
    porque = {}
    for setor, termos in KW_SETOR.items():
        p = 0.0
        hits = []
        for termo in termos:
            peso = 2.0 if " " in termo else 1.0
            if tem(t_nome, termo):
                p += peso
                hits.append(termo.replace("*", ""))
            elif tem(t_pasta, termo):
                p += peso * 0.5
                hits.append(termo.replace("*", "") + " (pasta)")
        if p:
            pontos[setor] = p
            porque[setor] = hits
    return pontos, porque


def detectar_area(t):
    melhor, pts = None, 0
    for area, termos in AREAS:
        p = sum(2 if " " in x else 1 for x in termos if tem(t, x))
        if p > pts:
            melhor, pts = area, p
    return melhor


def detectar_esqueleto(t):
    if tem(t, "relevancia") and (tem(t, "criterio*") or tem(t, "moviment*")):
        return "criterios-relevancia-movimentacao"
    if tem(t, "faq") or tem(t, "perguntas frequentes"):
        return "faq-clientes"
    if tem(t, "triagem") and (tem(t, "roteiro*") or tem(t, "script*") or tem(t, "pergunta*")):
        return "roteiro-triagem-por-area"
    if (tem(t, "checklist*") or tem(t, "check list") or tem(t, "lista*")) and tem(t, "document*"):
        return "checklist-documentos-por-tipo-de-caso"
    if (tem(t, "checklist*") or tem(t, "check list")) and (tem(t, "revis*") or tem(t, "peca*") or tem(t, "peticao")):
        return "checklist-revisao-peca"
    if tem(t, "honorario*") and (tem(t, "tabela*") or tem(t, "valores") or tem(t, "planilha*")):
        return "tabela-interna-honorarios"
    if tem(t, "regua*") or (tem(t, "cobranca*") and tem(t, "politica*")):
        return "regua-de-cobranca"
    if tem(t, "padrao*") and (tem(t, "nome*") or tem(t, "pasta*")):
        return "padrao-nomes-e-pastas"
    if (tem(t, "etic*") or tem(t, "provimento")) and (tem(t, "checklist*") or tem(t, "publicidade") or tem(t, "lista*")):
        return "checklist-etico-publicidade"
    if tem(t, "mensage*") and (tem(t, "modelo*") or tem(t, "pronta*") or tem(t, "padrao*") or
                               tem(t, "whatsapp") or tem(t, "categoria*")):
        return "modelos-mensagem-por-categoria"
    return None


def detectar_tipo(t, ext, setor):
    """Devolve (tipo, é POP?, peça sem a palavra modelo?)."""
    if tem(t, "pop") or tem(t, "procedimento operacional"):
        return "outro", True, False
    if tem(t, "caso de teste") or tem(t, "casos de teste") or tem(t, "gabarito*"):
        return "caso de teste", False, False
    esq = detectar_esqueleto(t)
    if esq:
        return ESQUELETOS[esq][1], False, False
    if tem(t, "checklist*") or tem(t, "check list") or tem(t, "lista de conferencia"):
        return "checklist", False, False
    if tem(t, "criterio*"):
        return "critério", False, False
    if tem(t, "tabela*") or tem(t, "planilha*") or ext in ("xlsx", "xls", "csv", "ods"):
        return "tabela", False, False
    if tem(t, "roteiro*") or tem(t, "script*") or tem(t, "passo a passo") or tem(t, "manual*"):
        return "roteiro", False, False
    if tem(t, "politica*") or tem(t, "termo de*") or tem(t, "regra de uso"):
        return "política", False, False
    if tem(t, "respostas*") or tem(t, "resposta padrao"):
        return "resposta aprovada", False, False
    if tem(t, "modelo*") or tem(t, "minuta*") or tem(t, "template*") or tem(t, "padrao") or tem(t, "mensage*"):
        return "modelo", False, False
    if any(tem(t, p) for p in PECAS) and setor in ("producao-de-pecas", "comercial", None):
        return "modelo", False, True
    return "outro", False, False


def assunto(item, remover_area):
    toks = []
    for w in item["chave"].split():
        w = ABREV.get(w, w) if w in ("doc", "docs", "msg", "msgs") else w
        if w in STOP or w in PALAVRAS_DE_TIPO or w in item["nomes"] or w.isdigit():
            continue
        if w in ("cliente", "clientes", "x", "vs", "processo", "processos", "proc", "autos", "caso", "acao", "contra"):
            continue
        if remover_area and w in PALAVRAS_DE_AREA:
            continue
        if w not in toks:
            toks.append(w)
    return toks[:6]


def nome_novo(item, area_na_pasta):
    esq, tipo, area = item["esqueleto"], item["tipo"], item["area"]
    sufixo_area = [area] if (area and not area_na_pasta) else []
    toks = assunto(item, remover_area=True)
    if esq == "checklist-documentos-por-tipo-de-caso":
        resto = [w for w in toks if w not in ("documentos", "documento", "checklist", "lista")]
        partes = ["checklist", "documentos"] + (resto or ([area] if area else ["por", "tipo", "de", "caso"]))
    elif esq == "roteiro-triagem-por-area":
        resto = [w for w in toks if w not in ("roteiro", "triagem", "script")]
        partes = ["roteiro", "triagem"] + ([area] if area else (resto or ["por", "area"]))
    elif esq in ("regua-de-cobranca", "padrao-nomes-e-pastas", "checklist-etico-publicidade"):
        partes = esq.split("-")
    elif esq:
        partes = esq.split("-") + sufixo_area
    elif tem(item["texto"], "manual*") and (tem(item["texto"], "estagiari*") or tem(item["texto"], "colaborador*")
                                            or tem(item["texto"], "integrac*")):
        partes = ["trilha", "de", "leitura"]
    else:
        prefixo = PREFIXO_TIPO.get(tipo, "")
        corpo = [w for w in toks if w != prefixo]
        partes = ([prefixo] if prefixo else []) + (corpo or ["documento"]) + \
            [a for a in sufixo_area if a not in corpo]
    nome = "-".join(p for p in partes if p)
    nome = re.sub(r"-+", "-", nome).strip("-")
    return nome or "documento"


# ---------------------------------------------------------------- varredura


def varrer(raiz, excluir, liberar, com_hash, saida_abs):
    itens, clientes, ignorados = [], [], {"sistema": 0, "atalhos": 0, "links": 0, "excluidas": []}
    excluir_n = {texto_busca(e).strip() for e in excluir}
    liberar_n = {texto_busca(e).strip() for e in liberar}
    for atual, pastas, arquivos in os.walk(raiz, topdown=True, followlinks=False):
        manter = []
        for p in sorted(pastas):
            caminho = os.path.join(atual, p)
            pn = texto_busca(p).strip()
            if p.startswith(".") or p.lower() in PASTAS_SISTEMA:
                continue
            if saida_abs and os.path.abspath(caminho) == saida_abs:
                continue
            if os.path.islink(caminho):
                ignorados["links"] += 1
                continue
            if pn in excluir_n:
                ignorados["excluidas"].append(os.path.relpath(caminho, raiz))
                continue
            motivo = None if pn in liberar_n else eh_pasta_de_cliente(p)
            if motivo:
                rel = os.path.relpath(caminho, raiz)
                nomes, _ = detectar_nomes(rel)
                clientes.append({"rel": rel, "motivo": motivo, "exibicao": mascarar(rel, nomes)})
                continue
            manter.append(p)
        pastas[:] = manter
        for a in sorted(arquivos):
            caminho = os.path.join(atual, a)
            al = a.lower()
            if al in LIXO_NOMES or a.startswith("~$") or a.startswith(".~lock") or a.startswith(".") \
                    or al.endswith(".tmp"):
                ignorados["sistema"] += 1
                continue
            if os.path.islink(caminho):
                ignorados["links"] += 1
                continue
            rel = os.path.relpath(caminho, raiz)
            stem, ext = os.path.splitext(a)
            ext = ext[1:].lower()
            st = os.stat(caminho)
            sha = ""
            if com_hash and ext not in ATALHOS_NUVEM:
                h = hashlib.sha256()
                with open(caminho, "rb") as f:
                    for bloco in iter(lambda: f.read(1024 * 1024), b""):
                        h.update(bloco)
                sha = h.hexdigest()
            if ext in ATALHOS_NUVEM:
                ignorados["atalhos"] += 1
            pasta_rel = os.path.dirname(rel)
            itens.append({
                "rel": rel, "nome": a, "stem": stem, "ext": ext, "tamanho": st.st_size,
                "mtime": dt.date.fromtimestamp(st.st_mtime), "sha": sha, "pasta": pasta_rel,
                "texto": texto_busca(stem), "texto_pasta": texto_busca(pasta_rel),
            })
    itens.sort(key=lambda x: normalizar(x["rel"]))
    for i, it in enumerate(itens, 1):
        it["id"] = i
    return itens, clientes, ignorados


def classificar(itens, anos_parado):
    for it in itens:
        it["marcas"], it["chave"] = marcas_de_versao(it["stem"])
        nomes, forte = detectar_nomes(it["stem"])
        nomes_pasta, _ = detectar_nomes(it["pasta"])
        it["nomes"] = nomes | nomes_pasta
        it["exibicao"] = mascarar(it["rel"], it["nomes"])
        t = it["texto"]
        pontos, porque = pontuar_setor(t, it["texto_pasta"])
        ordem = sorted(pontos.items(), key=lambda kv: -kv[1])
        setor = ordem[0][0] if ordem else None
        alternativo = ""
        if len(ordem) > 1 and ordem[1][1] >= ordem[0][1] * 0.8:
            alternativo = ordem[1][0]
        it["area"] = detectar_area(t) or detectar_area(it["texto_pasta"])
        tipo, eh_pop, peca_de_caso = detectar_tipo(t, it["ext"], setor)
        esq = None if eh_pop or tipo == "caso de teste" else detectar_esqueleto(t)
        if esq:
            setor_esq = ESQUELETOS[esq][0]
            if setor_esq != setor:
                alternativo = setor if setor and setor_esq != "comum" else alternativo
                setor = setor_esq
        it["setor"], it["setor_alt"], it["tipo"], it["esqueleto"] = setor, alternativo, tipo, esq
        it["eh_pop"] = eh_pop
        it["porque"] = ", ".join(porque.get(setor, [])) if setor else ""
        if esq and not it["porque"]:
            it["porque"] = "pelo esqueleto %s" % esq
        # alertas
        alertas = []
        nivel = ""
        for n in numeros_sensiveis(it["stem"]):
            alertas.append(n)
            nivel = "alto"
        cred = achados(t, CREDENCIAL)
        if cred:
            alertas.append("senha ou credencial no nome (%s)" % ", ".join(cred))
            nivel = "alto"
        if nomes:
            liga = achados(t, LIGA_PROCESSO) or (["número"] if numeros_sensiveis(it["stem"]) else [])
            if forte and liga:
                alertas.append("nome de pessoa seguido de processo ou caso")
                nivel = "alto"
            elif forte:
                alertas.append("nome que parece de pessoa")
                nivel = "alto"
            else:
                alertas.append("possível nome de pessoa")
                nivel = nivel or "médio"
        if nomes_pasta:
            alertas.append("nome que parece de pessoa na pasta")
            nivel = "alto"
        sens = achados(t, SENSIVEL_CASO)
        if tem(t, "cliente*") and (sens or re.search(r"\d", it["stem"])):
            alertas.append("a palavra cliente no nome, com número ou dado de caso")
            nivel = "alto"
        if sens:
            alertas.append("palavra de dado sensível ou de caso (%s)" % ", ".join(sens))
            nivel = nivel or "médio"
        if peca_de_caso:
            alertas.append("parece peça usada num caso: pode ter dado de cliente no texto")
            nivel = nivel or "médio"
        if it["area"] in AREAS_RESTRITAS:
            alertas.append("área com pasta restrita (%s)" % it["area"])
            nivel = nivel or "médio"
        it["alertas"], it["nivel"], it["sens"], it["peca_de_caso"] = alertas, nivel, sens, peca_de_caso
        it["parado"] = (HOJE - it["mtime"]).days > anos_parado * 365


def agrupar(itens):
    por_hash = {}
    for it in itens:
        it["duplicado_de"] = None
        it["familia"] = ""
        if it["sha"]:
            por_hash.setdefault(it["sha"], []).append(it)
    grupos_dup = []
    for grupo in por_hash.values():
        if len(grupo) < 2:
            continue
        rep = min(grupo, key=lambda x: (len(x["marcas"]), -x["mtime"].toordinal(), len(x["nome"]), x["id"]))
        for it in grupo:
            if it is not rep:
                it["duplicado_de"] = rep["id"]
        grupos_dup.append([rep] + [g for g in grupo if g is not rep])
    grupos_dup.sort(key=lambda g: g[0]["id"])
    por_chave = {}
    for it in itens:
        if it["chave"]:
            por_chave.setdefault(it["chave"], []).append(it)
    familias = []
    for chave, grupo in sorted(por_chave.items(), key=lambda kv: min(x["id"] for x in kv[1])):
        reps = [g for g in grupo if g["duplicado_de"] is None]
        if len(reps) < 2:
            continue
        rotulo = "F%d" % (len(familias) + 1)
        for g in grupo:
            g["familia"] = rotulo
        familias.append((rotulo, chave, grupo))
    return grupos_dup, familias


def triar(itens, familias):
    candidata = {}
    for rotulo, _, grupo in familias:
        reps = [g for g in grupo if g["duplicado_de"] is None and not (set(g["marcas"]) & MARCAS_DESCARTE)]
        if not reps:
            reps = [g for g in grupo if g["duplicado_de"] is None]
        if reps:
            candidata[rotulo] = max(reps, key=lambda x: (x["mtime"], x["id"]))["id"]
    for it in itens:
        decisao, motivo = "usar", "uma versão só, sem alerta no nome"
        caso = bool(it["sens"]) and it["tipo"] == "outro"
        if it["eh_pop"]:
            decisao, motivo = "fora da base", "é POP: leve à gerir-pops (código e nome padrão POP-SIGLA-NN, em 03-pops)"
        elif caso or (it["nivel"] == "alto" and it["tipo"] == "outro"):
            decisao, motivo = "fora da base", "dado do caso: volta para a pasta do cliente, nunca entra na base"
        elif it["duplicado_de"]:
            decisao, motivo = "descartar", "duplicado exato do #%d (mesmo conteúdo): não precisa de cópia" % it["duplicado_de"]
        elif set(it["marcas"]) & MARCAS_DESCARTE:
            decisao, motivo = "descartar", "o nome diz que não vale mais (%s)" % ", ".join(
                m for m in it["marcas"] if m in MARCAS_DESCARTE)
        elif it["familia"] and candidata.get(it["familia"]) != it["id"]:
            decisao, motivo = "descartar", "versão mais antiga da família %s: vai para o arquivo" % it["familia"]
        elif it["familia"]:
            n = sum(1 for x in itens if x["familia"] == it["familia"])
            decisao, motivo = "atualizar", ("família %s com %d arquivos: a mais recente é só o ponto de partida, "
                                            "o advogado escolhe a vigente e junta numa só" % (it["familia"], n))
        elif it["alertas"]:
            decisao, motivo = "atualizar", "alerta no nome: abrir, conferir e anonimizar antes de entrar"
        elif it["tipo"] == "outro":
            decisao, motivo = "descartar", ("não parece documento de base (modelo, checklist, critério, tabela, "
                                            "roteiro, política, resposta aprovada): [A CONFIRMAR] se algum POP usa")
        elif it["parado"]:
            decisao, motivo = "atualizar", "sem alteração há muito tempo: conferir se ainda vale"
        elif it["marcas"]:
            decisao, motivo = "usar", "uma versão só; o nome novo tira a marca de versão (%s)" % ", ".join(it["marcas"])
        if it["alertas"] and decisao == "atualizar" and "alerta" not in motivo:
            motivo += "; alerta no nome: conferir e anonimizar"
        it["decisao"], it["motivo"] = decisao, motivo


# ---------------------------------------------------------------- POPs


def ler_pops(pasta):
    pops = []
    if not pasta or not os.path.isdir(pasta):
        return pops
    for atual, dirs, arqs in os.walk(pasta):
        dirs[:] = [d for d in dirs if not d.startswith("_") and d != "testes" and not d.startswith(".")]
        for a in sorted(arqs):
            if not (a.startswith("pop-") and a.endswith(".md")):
                continue
            caminho = os.path.join(atual, a)
            with open(caminho, encoding="utf-8", errors="replace") as f:
                linhas = f.read().splitlines()
            codigo, nome, status = a[:-3], "", ""
            for ln in linhas[:8]:
                m = re.match(r"#\s*(POP-[A-Z]{3}-\d{2})\s*(.*)", ln.strip())
                if m:
                    codigo, nome = m.group(1), m.group(2).strip()
                m2 = re.search(r"Status:\s*([A-Za-zçãéí ]+)", ln)
                if m2:
                    status = m2.group(1).strip().split("·")[0].strip()
            if normalizar(status).startswith("aposentado"):
                continue
            setor = os.path.basename(os.path.dirname(caminho))
            itens, dentro = [], False
            for ln in linhas:
                if ln.startswith("#"):
                    dentro = "precisar consultar" in normalizar(ln)
                    continue
                if not dentro or not ln.strip().startswith("|"):
                    continue
                cel = [c.strip() for c in ln.strip().strip("|").split("|")]
                if not cel or not cel[0] or set(cel[0]) <= set("-: ") or normalizar(cel[0]).startswith("item"):
                    continue
                cel += [""] * 5
                itens.append({"item": cel[0], "passo": cel[1], "existe": cel[2], "onde": cel[3], "dono": cel[4]})
            pops.append({"codigo": codigo, "nome": nome, "status": status, "setor": setor,
                         "arquivo": os.path.relpath(caminho, pasta), "itens": itens})
    return pops


def toks_sig(t):
    out = []
    for w in t.split():
        w = ABREV.get(w, w)
        if len(w) >= 3 and w not in STOP:
            out.append(w)
    return out


def casa(a, b):
    if len(a) >= 5 and len(b) >= 5:
        return a[:5] == b[:5]
    return a == b


def cruzar_pops(pops, itens):
    pedidos = []
    candidatos = [x for x in itens if x["decisao"] in ("usar", "atualizar")]
    for pop in pops:
        for ped in pop["itens"]:
            alvo = toks_sig(texto_busca(ped["item"]))
            melhor, melhor_p = None, 0.0
            for it in candidatos:
                base = toks_sig(it["texto"] + " " + it["texto_pasta"] + " " + it["nome_novo"].replace("-", " "))
                acertos = sum(1 for a in alvo if any(casa(a, b) for b in base))
                p = acertos / float(len(alvo)) if alvo else 0
                if p >= 0.6 and acertos >= min(2, len(alvo)) and (p > melhor_p or
                                                                   (p == melhor_p and melhor and it["mtime"] > melhor["mtime"])):
                    melhor, melhor_p = it, p
            ped = dict(ped, pop=pop["codigo"], pop_nome=pop["nome"], setor=pop["setor"],
                       achado=melhor["id"] if melhor else None)
            if melhor:
                melhor.setdefault("usado_por", []).append("%s passo %s" % (pop["codigo"], ped["passo"] or "?"))
            pedidos.append(ped)
    return pedidos


# ---------------------------------------------------------------- plano


def preparar_nomes(itens):
    """Dá o nome novo de cada arquivo e devolve a função que garante destino único."""
    usados = set()

    def unico(caminho):
        base, ext = os.path.splitext(caminho)
        cand, n = caminho, 2
        while cand.lower() in usados:
            cand = "%s-%d%s" % (base, n, ext)
            n += 1
        usados.add(cand.lower())
        return cand

    casos = 0
    for it in itens:
        area_na_pasta = it["setor"] == "producao-de-pecas" and bool(it["area"])
        ext = ("." + it["ext"]) if it["ext"] else ""
        if it["tipo"] == "caso de teste":
            casos += 1
            it["nome_novo"] = "caso-%02d%s" % (casos, ext)
        else:
            it["nome_novo"] = nome_novo(it, area_na_pasta) + ext
        it.setdefault("usado_por", [])
    return unico


def destino_de(it, unico):
    setor, area, tipo, esq = it["setor"], it["area"], it["tipo"], it["esqueleto"]
    ext = ("." + it["ext"]) if it.get("ext") else ""
    stem = it["nome_novo"][: -len(ext)] if ext and it["nome_novo"].endswith(ext) else it["nome_novo"]
    if it["decisao"] == "fora da base" or (it["decisao"] == "descartar" and it.get("duplicado_de")):
        return ""
    if it["decisao"] == "descartar":
        stem = nome_novo(it, False) if "chave" in it and it["tipo"] != "caso de teste" else stem
        return unico("_arquivo/%s_ate-%s%s" % (stem, it["mtime"].isoformat(), ext))
    if tipo == "caso de teste":
        pasta = "casos-de-teste/a-definir"
    elif not setor:
        pasta = "[A CONFIRMAR setor]"
    elif setor == "comum":
        pasta = "comum"
    elif setor == "producao-de-pecas":
        if tipo == "modelo":
            pasta = "producao-de-pecas/modelos" + ("/" + area if area else "")
        elif esq == "checklist-revisao-peca" or not area:
            pasta = "producao-de-pecas"
        else:
            pasta = "producao-de-pecas/" + area
    else:
        pasta = setor
    return unico(pasta + "/" + it["nome_novo"])


def rodada_de(it, setor_alvo, tem_pops):
    if it["decisao"] in ("fora da base", "descartar"):
        return "não se aplica"
    if tem_pops:
        return "primeira" if it.get("usado_por") else "próxima (nenhum POP cita)"
    if setor_alvo:
        return "primeira" if it["setor"] in (setor_alvo, "comum") else "próxima (fora do setor-alvo)"
    return "[A CONFIRMAR] (sem POP e sem setor-alvo)"


COLUNAS_PLANO = ["id", "origem", "nome_exibicao", "setor", "area", "tipo", "esqueleto", "alerta", "familia",
                 "decisao", "motivo", "nome_novo", "destino", "rodada", "usado_por", "ok_do_advogado",
                 "anonimizacao_conferida", "observacao"]
COLUNAS_INV = ["id", "caminho", "nome_exibicao", "extensao", "tamanho_bytes", "tamanho", "modificado_em",
               "sha256", "duplicado_de", "familia", "marcas_de_versao", "setor_sugerido", "setor_alternativo",
               "area", "tipo_sugerido", "esqueleto", "nivel_alerta", "alertas", "palavras_que_pesaram"]


def caminho_esqueleto(esq):
    if esq:
        return "../montar-base/assets/esqueletos/%s.md" % esq
    return "../montar-base/references/artefatos-por-setor.md"


# ---------------------------------------------------------------- escrita


def escrever_tsv(caminho, colunas, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(colunas)
        for ln in linhas:
            w.writerow([limpar_celula(ln.get(c, "")) for c in colunas])


def tabela_md(cab, linhas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for ln in linhas:
        out.append("| " + " | ".join(md_celula(c) for c in ln) + " |")
    return out


def gerar(args):
    raiz = os.path.abspath(args.pasta)
    if not os.path.isdir(raiz):
        sys.exit("Pasta não encontrada: %s" % args.pasta)
    saida = os.path.abspath(args.saida)
    if saida == raiz or saida.startswith(raiz + os.sep):
        sys.exit("A pasta de saída fica dentro da pasta inventariada. Escolha outra (o inventário não grava "
                 "nada dentro da pasta original). Sugestão: <pasta>/escritorio/04-base/_inventario/AAAA-MM-DD")
    liberar_n = {texto_busca(e).strip() for e in args.liberar_pasta}
    raiz_motivo = eh_pasta_de_cliente(os.path.basename(raiz))
    if raiz_motivo and texto_busca(os.path.basename(raiz)).strip() not in liberar_n:
        sys.exit("A pasta indicada parece pasta de cliente (%s). Esta skill não abre pasta de cliente. Se o "
                 "advogado confirmar que não é, rode de novo com --liberar-pasta \"%s\"."
                 % (raiz_motivo, os.path.basename(raiz)))
    setor_alvo = None
    if args.setor_alvo:
        alvo = texto_busca(args.setor_alvo).strip()
        for s, n, _ in SETORES:
            if alvo in (texto_busca(s).strip(), texto_busca(n).strip()):
                setor_alvo = s
        if not setor_alvo:
            sys.exit("Setor-alvo não reconhecido: %s. Use um dos 10 setores do glossário." % args.setor_alvo)
    os.makedirs(saida, exist_ok=True)
    itens, clientes, ignorados = varrer(raiz, args.excluir, args.liberar_pasta, not args.sem_hash, saida)
    classificar(itens, args.anos_parado)
    grupos_dup, familias = agrupar(itens)
    triar(itens, familias)
    unico = preparar_nomes(itens)
    pops = ler_pops(args.pops)
    tem_pops = any(p["itens"] for p in pops)
    pedidos = cruzar_pops(pops, itens) if tem_pops else []
    for it in itens:
        it["destino"] = destino_de(it, unico)
        it["rodada"] = rodada_de(it, setor_alvo, tem_pops)
    # linhas criar
    criar = []
    for ped in pedidos:
        if ped["achado"]:
            continue
        t = texto_busca(ped["item"])
        setor = ped["setor"] if ped["setor"] in NOME_SETOR else None
        esq = detectar_esqueleto(t)
        tipo, _, _ = detectar_tipo(t, "md", setor)
        setor = setor or (ESQUELETOS[esq][0] if esq else None)
        fake = {"esqueleto": esq, "tipo": tipo, "area": detectar_area(t), "chave": " ".join(t.split()),
                "nomes": set(), "texto": t, "setor": setor, "ext": "md", "decisao": "usar"}
        fake["nome_novo"] = nome_novo(fake, fake["setor"] == "producao-de-pecas" and bool(fake["area"])) + ".md"
        fake["destino"] = destino_de(fake, unico)
        obs = ""
        if normalizar(ped["existe"]).startswith("sim"):
            obs = "o POP diz que existe por escrito: [A CONFIRMAR] onde está (outra pasta, drive, e-mail?)"
        criar.append(dict(fake, item=ped["item"], pop=ped["pop"], passo=ped["passo"], obs=obs,
                          esq_caminho=caminho_esqueleto(esq)))
    # -------- TSVs
    linhas_inv = []
    for it in itens:
        linhas_inv.append({
            "id": it["id"], "caminho": it["rel"], "nome_exibicao": it["exibicao"], "extensao": it["ext"],
            "tamanho_bytes": it["tamanho"], "tamanho": tamanho_legivel(it["tamanho"]),
            "modificado_em": it["mtime"].isoformat(), "sha256": it["sha"],
            "duplicado_de": it["duplicado_de"] or "", "familia": it["familia"],
            "marcas_de_versao": ", ".join(it["marcas"]), "setor_sugerido": it["setor"] or "[A CONFIRMAR]",
            "setor_alternativo": it["setor_alt"], "area": it["area"] or "", "tipo_sugerido": it["tipo"],
            "esqueleto": it["esqueleto"] or "", "nivel_alerta": it["nivel"], "alertas": "; ".join(it["alertas"]),
            "palavras_que_pesaram": it["porque"],
        })
    escrever_tsv(os.path.join(saida, "inventario.tsv"), COLUNAS_INV, linhas_inv)
    linhas_plano = []
    for it in itens:
        linhas_plano.append({
            "id": it["id"], "origem": it["rel"], "nome_exibicao": it["exibicao"],
            "setor": it["setor"] or "[A CONFIRMAR]", "area": it["area"] or "", "tipo": it["tipo"],
            "esqueleto": it["esqueleto"] or "", "alerta": "; ".join(it["alertas"]), "familia": it["familia"],
            "decisao": it["decisao"], "motivo": it["motivo"], "nome_novo": it["nome_novo"] if it["destino"] else "",
            "destino": it["destino"], "rodada": it["rodada"], "usado_por": "; ".join(it.get("usado_por", [])),
            "ok_do_advogado": "", "anonimizacao_conferida": "", "observacao": "",
        })
    for n, c in enumerate(clientes, 1):
        linhas_plano.append({
            "id": "P%d" % n, "origem": "", "nome_exibicao": c["exibicao"], "setor": "", "area": "", "tipo": "",
            "alerta": "pasta de cliente (%s)" % c["motivo"], "decisao": "fora da base",
            "motivo": "pasta de caso de cliente não é base: não foi aberta e nunca é copiada",
            "rodada": "não se aplica", "observacao": "não aberta pelo inventário",
        })
    for n, c in enumerate(criar, 1):
        linhas_plano.append({
            "id": "C%d" % n, "origem": "", "nome_exibicao": c["item"], "setor": c["setor"] or "[A CONFIRMAR]",
            "area": c["area"] or "", "tipo": c["tipo"], "esqueleto": c["esqueleto"] or "",
            "decisao": "criar", "motivo": "%s pede (passo %s) e não achei na pasta: montar-base cria a partir de %s"
            % (c["pop"], c["passo"] or "?", c["esq_caminho"]), "nome_novo": c["nome_novo"], "destino": c["destino"],
            "rodada": "primeira", "usado_por": "%s passo %s" % (c["pop"], c["passo"] or "?"), "observacao": c["obs"],
        })
    escrever_tsv(os.path.join(saida, "plano-de-reorganizacao.tsv"), COLUNAS_PLANO, linhas_plano)
    # -------- markdown
    raiz_base = "02 Base" if args.estrutura == "drive" else "escritorio/04-base"
    md = escrever_md(args, raiz, itens, clientes, ignorados, grupos_dup, familias, pops, pedidos, criar,
                     setor_alvo, tem_pops, raiz_base)
    with open(os.path.join(saida, "inventario.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    indice = escrever_indice(itens, clientes, criar, pops, tem_pops, setor_alvo, raiz_base)
    with open(os.path.join(saida, "INDICE-rascunho.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(indice) + "\n")
    # -------- resumo no terminal
    cont = contar(itens)
    print("Inventário de %s" % os.path.basename(raiz))
    print("  %d arquivos (%s), %d pastas de cliente não abertas, %d arquivos de sistema ignorados"
          % (len(itens), tamanho_legivel(sum(i["tamanho"] for i in itens)), len(clientes), ignorados["sistema"]))
    print("  duplicados exatos: %d grupos (%d cópias a mais) · famílias de versões: %d (%d arquivos)"
          % (len(grupos_dup), sum(len(g) - 1 for g in grupos_dup), len(familias), sum(len(f[2]) for f in familias)))
    print("  alertas de dado sensível: %d alto, %d médio"
          % (sum(1 for i in itens if i["nivel"] == "alto"), sum(1 for i in itens if i["nivel"] == "médio")))
    print("  setor não identificado: %d · triagem proposta: usar %d, atualizar %d, descartar %d, fora da base %d, criar %d"
          % (sum(1 for i in itens if not i["setor"]), cont["usar"], cont["atualizar"], cont["descartar"],
             cont["fora da base"] + len(clientes), len(criar)))
    if pops:
        print("  POPs lidos: %d · itens pedidos: %d · achados na pasta: %d · faltando: %d"
              % (len(pops), len(pedidos), sum(1 for p in pedidos if p["achado"]), len(criar)))
    print("Gravado em %s: inventario.md, inventario.tsv, plano-de-reorganizacao.tsv, INDICE-rascunho.md" % args.saida)


def contar(itens):
    c = {"usar": 0, "atualizar": 0, "descartar": 0, "fora da base": 0}
    for i in itens:
        c[i["decisao"]] = c.get(i["decisao"], 0) + 1
    return c


def escrever_md(args, raiz, itens, clientes, ignorados, grupos_dup, familias, pops, pedidos, criar,
                setor_alvo, tem_pops, raiz_base):
    nome_raiz = os.path.basename(raiz)
    total = sum(i["tamanho"] for i in itens)
    md = ["# Inventário da pasta \"%s\"" % mascarar(nome_raiz, detectar_nomes(nome_raiz)[0]),
          "Feito em: %s · Ferramenta: inventariar-base · Situação: rascunho para o advogado conferir" % HOJE.isoformat(),
          "",
          "> Nada foi movido, renomeado, aberto ou apagado. O inventário leu só nomes, extensões, datas, tamanhos "
          "e a impressão digital (hash) de cada arquivo. Nomes com possível dado de cliente aparecem mascarados "
          "([NOME], [DOC], [PROCESSO], [NÚMERO]).",
          ""]
    if args.sem_hash:
        md += ["> Rodado sem hash: duplicados exatos não foram procurados.", ""]
    # 1. retrato
    md += ["## 1. O retrato em números", ""]
    anos = {}
    for i in itens:
        anos[i["mtime"].year] = anos.get(i["mtime"].year, 0) + 1
    parados = sum(1 for i in itens if i["parado"])
    com_marca = sum(1 for i in itens if i["marcas"])
    md += ["- **Arquivos:** %d, somando %s, em %d pastas." % (
        len(itens), tamanho_legivel(total), len({i["pasta"] for i in itens})),
        "- **Pastas de cliente encontradas e não abertas:** %d." % len(clientes),
        "- **Ignorados:** %d arquivos de sistema ou temporários, %d atalhos de nuvem sem hash, %d atalhos de "
        "pasta%s." % (ignorados["sistema"], ignorados["atalhos"], ignorados["links"],
                      (", pastas excluídas a pedido: %d" % len(ignorados["excluidas"])) if ignorados["excluidas"] else ""),
        "- **Duplicados exatos** (mesmo conteúdo, nomes diferentes): %d grupos, %d cópias a mais." % (
            len(grupos_dup), sum(len(g) - 1 for g in grupos_dup)),
        "- **Famílias de versões** (o mesmo documento com final, v3, revisado, cópia, novo, antigo): %d famílias, "
        "%d arquivos." % (len(familias), sum(len(f[2]) for f in familias)),
        "- **Arquivos com marca de versão no nome:** %d de %d." % (com_marca, len(itens)),
        "- **Sem alteração há mais de %d anos:** %d." % (args.anos_parado, parados),
        ""]
    md += ["**Por tipo de arquivo**", ""]
    por_ext = {}
    for i in itens:
        e = i["ext"] or "(sem extensão)"
        q, t = por_ext.get(e, (0, 0))
        por_ext[e] = (q + 1, t + i["tamanho"])
    md += tabela_md(["Extensão", "Arquivos", "Tamanho"],
                    [(e, q, tamanho_legivel(t)) for e, (q, t) in sorted(por_ext.items(), key=lambda kv: -kv[1][0])])
    md += ["", "**Última alteração por ano**", ""]
    md += tabela_md(["Ano", "Arquivos"], [(a, anos[a]) for a in sorted(anos)])
    md += ["", "**Os 5 mais antigos**", ""]
    md += tabela_md(["#", "Arquivo", "Última alteração"],
                    [(i["id"], i["exibicao"], i["mtime"].isoformat())
                     for i in sorted(itens, key=lambda x: (x["mtime"], x["id"]))[:5]])
    if grupos_dup:
        md += ["", "**Duplicados exatos**", ""]
        md += tabela_md(["Grupo", "Fica (representante)", "Cópias iguais"],
                        [("D%d" % n, "#%d %s" % (g[0]["id"], g[0]["exibicao"]),
                          "; ".join("#%d %s" % (x["id"], x["exibicao"]) for x in g[1:]))
                         for n, g in enumerate(grupos_dup, 1)])
    if familias:
        md += ["", "**Famílias de versões**", ""]
        linhas = []
        for rotulo, chave, grupo in familias:
            for g in sorted(grupo, key=lambda x: x["mtime"]):
                linhas.append((rotulo, "#%d %s" % (g["id"], g["exibicao"]), ", ".join(g["marcas"]) or "(nenhuma)",
                               g["mtime"].isoformat(), ("igual ao #%d" % g["duplicado_de"]) if g["duplicado_de"] else ""))
        md += tabela_md(["Família", "Arquivo", "Marcas no nome", "Última alteração", "Duplicado"], linhas)
        md += ["", "Qual versão vale é decisão do advogado. A mais recente é só o ponto de partida da conversa."]
    # 2. alertas
    md += ["", "## 2. Alertas de dado sensível", "",
           "Regra: pasta de caso de cliente não é base. O que é dado do caso (laudo, holerite, extrato, documento "
           "pessoal, peça com nome do cliente) fica na pasta do cliente. Cada alerta abaixo é uma decisão do "
           "advogado, e nenhuma linha com alerta é copiada sem `anonimizacao_conferida = sim` no plano.", ""]
    if clientes:
        md += ["**Pastas de cliente (não abertas)**", ""]
        md += tabela_md(["#", "Pasta", "Por que parece de cliente"],
                        [("P%d" % n, c["exibicao"], c["motivo"]) for n, c in enumerate(clientes, 1)])
        md += [""]
    com_alerta = [i for i in itens if i["alertas"]]
    if com_alerta:
        md += ["**Arquivos com alerta no nome ou no caminho**", ""]
        md += tabela_md(["#", "Arquivo", "Nível", "Alerta", "Proposta"],
                        [(i["id"], i["exibicao"], i["nivel"], "; ".join(i["alertas"]), i["decisao"])
                         for i in sorted(com_alerta, key=lambda x: (x["nivel"] != "alto", x["id"]))])
    if not clientes and not com_alerta:
        md += ["Nenhum alerta pelo nome. Isso não garante que o conteúdo esteja limpo: o critério de entrada da "
               "montar-base continua valendo para cada documento."]
    # 3. setor e tipo
    lim = args.limite_md
    md += ["", "## 3. Sugestão de setor e tipo", "",
           "Pelas palavras do nome e da pasta. Setor com alternativo é empate: o advogado escolhe. Sem setor, "
           "fica `[A CONFIRMAR]`.", ""]
    linhas = []
    for i in itens[:lim]:
        setor = NOME_SETOR.get(i["setor"], "[A CONFIRMAR]") if i["setor"] else "[A CONFIRMAR]"
        if i["setor_alt"]:
            setor += " (ou %s)" % NOME_SETOR.get(i["setor_alt"], i["setor_alt"])
        linhas.append((i["id"], i["exibicao"], setor, NOME_AREA.get(i["area"], ""), i["tipo"] + (" (POP)" if i["eh_pop"] else ""),
                       i["esqueleto"] or "", i["porque"]))
    md += tabela_md(["#", "Arquivo", "Setor", "Área", "Tipo", "Esqueleto da montar-base", "Palavras que pesaram"], linhas)
    if len(itens) > lim:
        md += ["", "(%d linhas a mais no `inventario.tsv`.)" % (len(itens) - lim)]
    resumo_setor = {}
    for i in itens:
        resumo_setor[i["setor"]] = resumo_setor.get(i["setor"], 0) + 1
    md += ["", "**Arquivos por setor sugerido**", ""]
    md += tabela_md(["Setor", "Arquivos"], [(NOME_SETOR.get(s, "[A CONFIRMAR]") if s else "[A CONFIRMAR]", q)
                                            for s, q in sorted(resumo_setor.items(), key=lambda kv: -kv[1])])
    # 4. triagem
    cont = contar(itens)
    md += ["", "## 4. Proposta de triagem", "",
           "Usar: existe, uma versão, sem alerta. Atualizar: várias versões, alerta ou parado há muito tempo. "
           "Descartar: duplicado, antigo ou sem uso (vai para `_arquivo/`, o original fica onde está). Criar: o POP "
           "pede e não existe. Fora da base: dado do caso ou POP. Tudo é proposta: o advogado confirma linha a linha.",
           "",
           "- Usar: %d · Atualizar: %d · Descartar: %d · Fora da base: %d (mais %d pastas de cliente) · Criar: %d" % (
               cont["usar"], cont["atualizar"], cont["descartar"], cont["fora da base"], len(clientes), len(criar)),
           ""]
    ordem = {"usar": 0, "atualizar": 1, "descartar": 2, "fora da base": 3}
    md += tabela_md(["#", "Arquivo", "Proposta", "Motivo", "Rodada"],
                    [(i["id"], i["exibicao"], i["decisao"], i["motivo"], i["rodada"])
                     for i in sorted(itens, key=lambda x: (ordem.get(x["decisao"], 9), x["id"]))[:lim]])
    if criar:
        md += [""]
        md += tabela_md(["#", "Documento que falta", "Pedido por", "Esqueleto"],
                        [("C%d" % n, c["item"], "%s passo %s" % (c["pop"], c["passo"] or "?"), c["esq_caminho"])
                         for n, c in enumerate(criar, 1)])
    # 5. plano
    md += ["", "## 5. Plano de reorganização (só depois do ok)", "",
           "Destino dentro de `%s/`. Nada é aplicado sem o ok. O script só copia: o original continua onde está, "
           "e o que for descartado vai para `_arquivo/` com a data no nome." % raiz_base, ""]
    md += tabela_md(["#", "De", "Para", "Decisão"],
                    [(i["id"], i["exibicao"], i["destino"] or "(não copia)", i["decisao"])
                     for i in itens[:lim]])
    md += ["", "**Como aprovar e aplicar**", "",
           "1. Abra `plano-de-reorganizacao.tsv` numa planilha (ou confira linha a linha na conversa).",
           "2. Em cada linha que o advogado aprovar, escreva `sim` na coluna `ok_do_advogado`. Ajuste `setor`, "
           "`nome_novo` e `destino` se quiser outro lugar ou outro nome.",
           "3. Linha com alerta só é copiada com `sim` também em `anonimizacao_conferida`: quer dizer que o advogado "
           "abriu o arquivo e confirmou que não tem dado de cliente, ou trocou a `origem` pelo caminho de uma versão "
           "anonimizada feita por ele.",
           "4. Rode primeiro a simulação e depois a cópia:",
           "",
           "```",
           "python3 scripts/inventariar_pasta.py --aplicar <saida>/plano-de-reorganizacao.tsv --origem \"<pasta original>\" "
           "--destino \"<pasta>/%s\" --simular" % raiz_base,
           "python3 scripts/inventariar_pasta.py --aplicar <saida>/plano-de-reorganizacao.tsv --origem \"<pasta original>\" "
           "--destino \"<pasta>/%s\"" % raiz_base,
           "```",
           "",
           "Tudo que entra na base chega como **rascunho**, com o cabeçalho da montar-base (no próprio arquivo .md ou "
           "numa ficha .md ao lado). Só vira \"em uso\" depois do critério de entrada da montar-base."]
    # 6. pops
    md += ["", "## 6. O que os POPs pedem", ""]
    if not pops:
        md += ["Nenhum POP lido (sem `--pops` ou sem POP em `03-pops/`). Inventário feito no **modo inventário**: "
               "a rodada de cada documento depende do setor-alvo%s, e cada item fica `[A CONFIRMAR]` (conferir no POP)."
               % ((" (%s)" % NOME_SETOR[setor_alvo]) if setor_alvo else ", que não foi informado")]
    else:
        md += ["POPs lidos: " + "; ".join("%s %s (%s)" % (p["codigo"], p["nome"], p["status"] or "status não lido")
                                          for p in pops), ""]
        if not tem_pops:
            md += ["Os POPs lidos não têm a tabela \"O que a IA vai precisar consultar\" preenchida. Leia o campo "
                   "Entradas de cada POP na conversa e monte a lista à mão."]
        else:
            md += tabela_md(["POP", "Passo", "O que o POP pede", "O POP diz que existe?", "Na pasta"],
                            [(p["pop"], p["passo"], p["item"], p["existe"],
                              ("#%d %s" % (p["achado"], next(i["exibicao"] for i in itens if i["id"] == p["achado"])))
                              if p["achado"] else "não achei: criar na montar-base") for p in pedidos])
    md += ["", "## 7. Próximo passo", "",
           "Com a triagem confirmada e a cópia feita, siga na `montar-base` a partir do passo 3 (triagem), "
           "depois criar o que falta a partir dos esqueletos, critério de entrada, casos de teste e Projeto no "
           "Claude. O rascunho do índice está em `INDICE-rascunho.md`, ao lado deste arquivo."]
    return md


def escrever_indice(itens, clientes, criar, pops, tem_pops, setor_alvo, raiz_base):
    pop_ref = "; ".join("`03-pops/%s` (%s)" % (p["arquivo"], p["codigo"]) for p in pops) or \
        "[A CONFIRMAR] sem POP lido (modo inventário)"
    alvo = NOME_SETOR.get(setor_alvo, "[A DEFINIR]") if setor_alvo else "[A DEFINIR]"
    md = ["# Índice da base de conhecimento",
          "Versão: 0.1 · Revisado em: %s · Dono: [A DEFINIR] · Situação: rascunho (saiu do inventário)" % HOJE.isoformat(),
          "",
          "> O que existe na base, qual é a versão que vale e quem cuida. Documento fora deste índice não existe para a "
          "IA. Rascunho gerado pelo inventário: confira com o advogado antes de gravar em `%s/INDICE.md`." % raiz_base,
          "",
          "## Levantamento (setor-alvo: %s)" % alvo,
          "",
          "POP de origem: %s." % pop_ref,
          ""]
    linhas = []
    docs = {}
    for i in itens:
        if i["decisao"] in ("usar", "atualizar"):
            docs[i["id"]] = i
    for i in sorted(docs.values(), key=lambda x: (x["rodada"] != "primeira", x["id"])):
        n_versoes = sum(1 for x in itens if x["familia"] and x["familia"] == i["familia"]) if i["familia"] else \
            1 + sum(1 for x in itens if x["duplicado_de"] == i["id"])
        onde = "; ".join(i.get("usado_por", [])) or "[A CONFIRMAR] conferir no POP"
        linhas.append((i["nome_novo"], onde, i["tipo"], i["exibicao"], n_versoes, i["decisao"]))
    for c in criar:
        linhas.append((c["nome_novo"], "%s passo %s" % (c["pop"], c["passo"] or "?"), c["tipo"],
                       "não existe na pasta", 0, "criar"))
    md += tabela_md(["Documento citado", "Onde aparece (POP e passo)", "Tipo", "Onde estava", "Versões encontradas",
                     "Decisão (usar, atualizar, descartar, criar)"], linhas)
    fora = sum(1 for i in itens if i["decisao"] == "fora da base")
    desc = sum(1 for i in itens if i["decisao"] == "descartar")
    md += ["", "Fora do levantamento: %d arquivos descartados (duplicados, versões antigas, sem uso), %d arquivos "
           "de dado do caso ou POP, %d pastas de cliente não abertas." % (desc, fora, len(clientes)), "",
           "## Documentos da base", ""]
    linhas = []
    for i in sorted(docs.values(), key=lambda x: x["id"]):
        if not i["destino"] or "[A CONFIRMAR" in i["destino"]:
            pasta = "[A CONFIRMAR]"
        else:
            pasta = os.path.dirname(i["destino"]) + "/"
        acesso = "restrito [A CONFIRMAR]" if (i["area"] in AREAS_RESTRITAS or i["alertas"]) else "geral"
        if i["tipo"] == "caso de teste":
            continue
        linhas.append((i["nome_novo"], pasta, "0.1", "[A DEFINIR]", "[A DEFINIR]",
                       "; ".join(i.get("usado_por", [])) or "[A CONFIRMAR]", "rascunho", acesso))
    md += tabela_md(["Documento", "Pasta", "Versão", "Revisado em", "Dono", "Usado por", "Situação", "Acesso"], linhas)
    casos = [i for i in docs.values() if i["tipo"] == "caso de teste"]
    md += ["", "## Casos de teste", ""]
    md += tabela_md(["Automação", "Pasta", "Casos", "Gabarito escrito por", "Situação"],
                    [("[A DEFINIR]", "`casos-de-teste/[nome]/`", len(casos) or "", "[A DEFINIR]",
                      "rascunho" if casos else "")])
    md += ["", "## Regras da base", "",
           "- Quem pode incluir: [A DEFINIR]",
           "- Quem aprova conteúdo jurídico: [A DEFINIR]",
           "- Quem aprova documento operacional: [A DEFINIR]",
           "- Pastas restritas e quem acessa: [A DEFINIR]",
           "- Revisão: erro repetido, mudança de POP e revisão trimestral.",
           "- Versão antiga vai para `_arquivo/` com a data no nome e sai do Projeto no mesmo dia.",
           "- `_inventario/` e `_arquivo/` ficam fora do Projeto no Claude.",
           "", "## Lacunas abertas", ""]
    if criar:
        for c in criar:
            md.append("- %s (pedido por %s passo %s): criar a partir de `%s`. Dono: [A DEFINIR] · Prazo: [A DEFINIR]"
                      % (c["nome_novo"], c["pop"], c["passo"] or "?", c["esq_caminho"]))
    else:
        md.append("- [A CONFIRMAR] sem POP lido, as lacunas saem do campo Entradas do POP do setor-alvo.")
    return md


# ---------------------------------------------------------------- aplicar

SIM = {"sim", "s", "x", "ok", "yes", "aprovado"}
CABECALHO = """# {titulo}
Versão: 0.1 · Revisado em: [A DEFINIR] · Dono: [A DEFINIR] · Situação: rascunho
Setor: {setor} · Área: {area} · Usado por: {usado} · Acesso: {acesso}
Aprovado por: [A DEFINIR] · Próxima revisão: revisão trimestral
"""
CRITERIO = """
## Antes de passar para "em uso" (critério de entrada da montar-base)

- [ ] Algum POP cita este documento, ou o código do escritório exige.
- [ ] Uma versão só: as outras foram para `_arquivo/`.
- [ ] Sem dado que identifique cliente (conferir também cabeçalho, rodapé e propriedades do arquivo).
- [ ] Norma pelo nome; jurisprudência aberta na fonte e marcada [CONFERIR] com a data da conferência.
- [ ] Dono, data e quem aprovou preenchidos.
"""


def seguro(rel):
    if not rel or os.path.isabs(rel) or rel.startswith("~"):
        return False
    partes = rel.replace("\\", "/").split("/")
    return ".." not in partes and "" not in partes


def ficha_texto(ln, arquivo, hoje):
    titulo = os.path.splitext(os.path.basename(arquivo))[0].replace("-", " ")
    titulo = titulo[:1].upper() + titulo[1:]
    setor = NOME_SETOR.get(ln.get("setor", ""), ln.get("setor", "") or "[A CONFIRMAR]")
    area = NOME_AREA.get(ln.get("area", ""), ln.get("area") or "todas")
    acesso = "restrito [A CONFIRMAR]" if (ln.get("area") in AREAS_RESTRITAS or ln.get("alerta")) else "geral"
    cab = CABECALHO.format(titulo=titulo, setor=setor, area=area, acesso=acesso,
                           usado=ln.get("usado_por") or "[A CONFIRMAR] conferir no POP")
    corpo = ["", "Arquivo: `%s` · Veio do inventário em %s (o original continua onde estava: %s)."
             % (os.path.basename(arquivo), hoje, ln.get("nome_exibicao", "")), CRITERIO,
             "## Mudanças", "- 0.1 · %s · copiado pelo inventário (inventariar-base) · decisão: %s"
             % (hoje, ln.get("decisao", ""))]
    return cab + "\n".join(corpo) + "\n"


def aplicar(args):
    plano = os.path.abspath(args.aplicar)
    origem = os.path.abspath(args.origem) if args.origem else None
    destino = os.path.abspath(args.destino) if args.destino else None
    if not (os.path.isfile(plano) and origem and destino):
        sys.exit("Use: --aplicar plano.tsv --origem <pasta original> --destino <pasta da base>")
    if not os.path.isdir(origem):
        sys.exit("Pasta de origem não encontrada: %s" % args.origem)
    if destino == origem or destino.startswith(origem + os.sep):
        sys.exit("O destino fica dentro da pasta original. A cópia não grava nada dentro da pasta original.")
    with open(plano, encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f, delimiter="\t"))
    faltando = [c for c in ("id", "origem", "decisao", "destino", "ok_do_advogado") if c not in (linhas[0] if linhas else {})]
    if faltando:
        sys.exit("O plano não tem as colunas: %s" % ", ".join(faltando))
    hoje = dt.date.today().isoformat()
    feitos, pulados, pendentes = [], [], []
    for ln in linhas:
        ident = ln.get("id", "")
        exib = ln.get("nome_exibicao", "") or ln.get("origem", "")
        decisao = normalizar(ln.get("decisao", "")).strip()
        dest_rel = (ln.get("destino") or "").strip()
        ok = normalizar(ln.get("ok_do_advogado", "")).strip() in SIM
        if decisao == "criar":
            pendentes.append((ident, exib, "fica para a montar-base: criar a partir do esqueleto"))
            continue
        if not ok:
            pulados.append((ident, exib, "sem ok do advogado"))
            continue
        if ident.startswith("P") or "pasta de cliente" in normalizar(ln.get("alerta", "")):
            pulados.append((ident, exib, "pasta de cliente: nunca é copiada"))
            continue
        if decisao == "fora da base":
            pulados.append((ident, exib, "fora da base: não é copiado"))
            continue
        if not dest_rel:
            pulados.append((ident, exib, "sem destino (duplicado exato ou não copia)"))
            continue
        if "[" in dest_rel or "a-definir" in dest_rel or "a confirmar" in normalizar(dest_rel):
            pulados.append((ident, exib, "destino com marcação a preencher: %s" % dest_rel))
            continue
        if not seguro(dest_rel):
            pulados.append((ident, exib, "destino fora da pasta da base: %s" % dest_rel))
            continue
        if (ln.get("alerta") or "").strip() and normalizar(ln.get("anonimizacao_conferida", "")).strip() not in SIM:
            pulados.append((ident, exib, "tem alerta e falta anonimizacao_conferida = sim"))
            continue
        org_rel = (ln.get("origem") or "").strip()
        if os.path.isabs(org_rel):
            org = org_rel
        elif seguro(org_rel):
            org = os.path.join(origem, org_rel)
        else:
            pulados.append((ident, exib, "origem inválida"))
            continue
        if not os.path.isfile(org):
            pulados.append((ident, exib, "arquivo de origem não encontrado"))
            continue
        alvo = os.path.join(destino, dest_rel)
        if os.path.exists(alvo):
            pulados.append((ident, exib, "já existe no destino: não sobrescrevo (%s)" % dest_rel))
            continue
        ficha = None
        eh_arquivo = dest_rel.startswith("_arquivo/")
        if not eh_arquivo and not alvo.lower().endswith(".md"):
            ficha = os.path.splitext(alvo)[0] + ".md"
            if os.path.exists(ficha):
                ficha = None
        if args.simular:
            feitos.append((ident, exib, dest_rel, "copiaria" + (" e criaria a ficha .md" if ficha else "")))
            continue
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        shutil.copy2(org, alvo)
        if hash_arquivo(org) != hash_arquivo(alvo):
            os.remove(alvo)
            pulados.append((ident, exib, "a cópia não conferiu com o original: desfeita"))
            continue
        extra = ""
        if not eh_arquivo and alvo.lower().endswith(".md"):
            with open(alvo, encoding="utf-8", errors="replace") as f:
                conteudo = f.read()
            if "Situação:" not in conteudo[:600]:
                with open(alvo, "w", encoding="utf-8") as f:
                    f.write(ficha_texto(ln, alvo, hoje) + "\n---\n\n" + conteudo)
                extra = " · cabeçalho de rascunho no topo da cópia"
        if ficha:
            with open(ficha, "w", encoding="utf-8") as f:
                f.write(ficha_texto(ln, alvo, hoje))
            extra = " · ficha %s" % os.path.relpath(ficha, destino)
        feitos.append((ident, exib, dest_rel, "copiado" + extra))
    # registro
    titulo = "Simulação da cópia" if args.simular else "Registro da cópia"
    out = ["# %s do inventário" % titulo,
           "Feito em: %s · Plano: `%s` · Destino: `%s`" % (hoje, os.path.basename(plano), args.destino), "",
           "O original não foi movido, renomeado nem apagado. Nada foi sobrescrito.", "",
           "- %s: %d · Pulados: %d · Ficam para a montar-base: %d" % (
               "Copiaria" if args.simular else "Copiados", len(feitos), len(pulados), len(pendentes)), ""]
    if feitos:
        out += ["## %s" % ("O que seria copiado" if args.simular else "Copiados"), ""]
        out += tabela_md(["#", "Origem", "Destino", "Resultado"], feitos)
        out += [""]
    sem_ok = [p[0] for p in pulados if p[2] == "sem ok do advogado"]
    outros = [p for p in pulados if p[2] != "sem ok do advogado"]
    if outros:
        out += ["## Pulados por uma regra", ""]
        out += tabela_md(["#", "Origem", "Por quê"], outros)
        out += [""]
    if sem_ok:
        out += ["## Sem ok do advogado (não copiados)", "", ", ".join("#%s" % i for i in sem_ok), ""]
    if pendentes:
        out += ["## Para a montar-base criar", ""]
        out += tabela_md(["#", "Documento", "O que fazer"], pendentes)
        out += [""]
    if not args.simular:
        out += ["Para desfazer: apague as cópias listadas em \"Copiados\" (e as fichas). O original nunca foi tocado."]
    texto = "\n".join(out) + "\n"
    if args.simular:
        print(texto)
        return
    reg = args.registro or os.path.join(os.path.dirname(plano), "registro-de-copia-%s.md"
                                        % dt.datetime.now().strftime("%Y-%m-%d-%H%M%S"))
    with open(reg, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Copiados: %d · Pulados: %d · Para a montar-base: %d" % (len(feitos), len(pulados), len(pendentes)))
    print("Registro: %s" % reg)


def hash_arquivo(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


# ---------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description="Inventário da pasta de modelos do escritório, sem mexer em nada.")
    ap.add_argument("pasta", nargs="?", help="pasta de modelos a inventariar")
    ap.add_argument("--saida", help="pasta onde gravar o inventário (fora da pasta inventariada)")
    ap.add_argument("--pops", help="pasta escritorio/03-pops, para cruzar com o que os POPs pedem")
    ap.add_argument("--setor-alvo", help="setor-alvo do perfil (um dos 10 setores)")
    ap.add_argument("--estrutura", choices=["escritorio", "drive"], default="escritorio")
    ap.add_argument("--excluir", action="append", default=[], help="nome de pasta para pular (repetível)")
    ap.add_argument("--liberar-pasta", action="append", default=[],
                    help="pasta que parece de cliente e o advogado confirmou que não é (repetível)")
    ap.add_argument("--anos-parado", type=int, default=2)
    ap.add_argument("--sem-hash", action="store_true", help="não ler o conteúdo para o hash (nuvem sob demanda)")
    ap.add_argument("--limite-md", type=int, default=300)
    ap.add_argument("--aplicar", help="plano-de-reorganizacao.tsv aprovado")
    ap.add_argument("--origem", help="pasta original (modo --aplicar)")
    ap.add_argument("--destino", help="pasta da base: escritorio/04-base ou 02 Base (modo --aplicar)")
    ap.add_argument("--simular", action="store_true", help="mostra o que seria copiado, sem copiar")
    ap.add_argument("--registro", help="arquivo do registro da cópia (padrão: ao lado do plano)")
    args = ap.parse_args()
    if args.aplicar:
        aplicar(args)
    elif args.pasta and args.saida:
        gerar(args)
    else:
        ap.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
