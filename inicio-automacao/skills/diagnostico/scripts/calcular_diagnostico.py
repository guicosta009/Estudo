#!/usr/bin/env python3
"""Calcula o diagnóstico de prontidão para automação do escritório.

Uso:
    python3 calcular_diagnostico.py respostas.json
        [--questionario ../references/questionario.json]
        [--anterior escritorio/diagnosticos/AAAA-MM-DD.md]
        [--perfil escritorio/perfil.md]
        [--formato ambos|json|md]
        [--saida-md caminho/do/arquivo.md]
        [--permitir-incompleto]

Só biblioteca padrão. Tudo roda no computador: nada é enviado para fora.
O formato do arquivo de respostas está descrito no SKILL.md (seção 8).
"""

import argparse
import json
import math
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
QUESTIONARIO_PADRAO = os.path.join(AQUI, "..", "references", "questionario.json")
MARCA_DADOS = "versao_questionario"


class ErroResposta(Exception):
    pass


# ---------- utilidades ----------

def normalizar(texto):
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = texto.replace("“", "").replace("”", "").replace('"', "")
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip(" .")


def arred(x):
    """Arredondamento igual ao Math.round do material (metade para cima)."""
    return int(math.floor(round(x, 9) + 0.5))


def fmt1(x):
    v = math.floor(round(x * 10, 9) + 0.5) / 10
    if v == int(v):
        return str(int(v))
    return ("%.1f" % v).replace(".", ",")


def fmt_pts(x):
    v = float(x)
    if v == int(v):
        return str(int(v))
    return ("%g" % v).replace(".", ",")


def resolver_opcao(pergunta, valor):
    """Devolve o índice da opção. Aceita índice (int), rótulo ou valor."""
    opcoes = pergunta["opcoes"]
    if isinstance(valor, bool):
        raise ErroResposta("%s: resposta inválida (%r)" % (pergunta["id"], valor))
    if isinstance(valor, int):
        if 0 <= valor < len(opcoes):
            return valor
        raise ErroResposta("%s: índice %d fora da lista (0 a %d)" % (pergunta["id"], valor, len(opcoes) - 1))
    if isinstance(valor, str) and valor.strip().isdigit():
        return resolver_opcao(pergunta, int(valor.strip()))
    alvo = normalizar(valor)
    if alvo in ("solo", "trabalho sozinho", "trabalho sozinha"):
        for i, o in enumerate(opcoes):
            if o.get("solo"):
                return i
    for i, o in enumerate(opcoes):
        if normalizar(o["rotulo"]) == alvo or ("valor" in o and normalizar(o["valor"]) == alvo):
            return i
    candidatos = [i for i, o in enumerate(opcoes) if normalizar(o["rotulo"]).startswith(alvo)]
    if len(candidatos) == 1:
        return candidatos[0]
    raise ErroResposta("%s: não encontrei a opção %r" % (pergunta["id"], valor))


def resolver_multipla(pergunta, valor):
    if not isinstance(valor, list):
        valor = [valor]
    idx = sorted(set(resolver_opcao(pergunta, v) for v in valor))
    excl = [i for i in idx if pergunta["opcoes"][i].get("exclusiva")]
    if excl and len(idx) > 1:
        raise ErroResposta("%s: a opção %r é exclusiva e foi marcada junto com outras"
                           % (pergunta["id"], pergunta["opcoes"][excl[0]]["rotulo"]))
    return idx


def rotulos(pergunta, idx):
    if isinstance(idx, list):
        return [pergunta["opcoes"][i]["rotulo"] for i in idx]
    return pergunta["opcoes"][idx]["rotulo"]


# ---------- leitura da rodada anterior e do perfil ----------

def ler_dados_anteriores(caminho):
    with open(caminho, encoding="utf-8") as f:
        conteudo = f.read()
    if caminho.lower().endswith(".json"):
        dados = json.loads(conteudo)
        return dados.get("dados_para_proxima_rodada", dados)
    for bloco in re.findall(r"```json\s*\n(.*?)\n```", conteudo, re.S):
        if MARCA_DADOS in bloco:
            return json.loads(bloco)
    raise ErroResposta("não achei o bloco de dados no arquivo anterior: %s" % caminho)


def ler_progresso(caminho):
    itens = []
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            m = re.match(r"\s*-\s*\[( |x|X)\]\s*(.+)", linha)
            if m:
                itens.append((m.group(1).lower() == "x", m.group(2).strip()))
    return itens


# ---------- cálculo ----------

def calcular(q, entrada, permitir_incompleto=False, anterior=None, progresso=None):
    avisos = []
    perfil_in = entrada.get("perfil", {}) or {}
    perfil_q = {p["id"]: p for p in q["perfil"]["perguntas"]}

    # Bloco "Seu escritório"
    perfil = {}
    for pid, p in perfil_q.items():
        if pid not in perfil_in or perfil_in[pid] in (None, ""):
            continue
        v = perfil_in[pid]
        if p["tipo"] == "texto":
            perfil[pid] = str(v)
        elif p["tipo"] == "multipla":
            perfil[pid] = rotulos(p, resolver_multipla(p, v))
        else:
            i = resolver_opcao(p, v)
            perfil[pid] = p["opcoes"][i].get("valor", p["opcoes"][i]["rotulo"])
            perfil[pid + "_rotulo"] = p["opcoes"][i]["rotulo"]
            if pid == "porte":
                perfil["trilha"] = p["opcoes"][i]["trilha"]
    if "porte" not in perfil:
        raise ErroResposta("perfil.porte é obrigatório: ele define a trilha")
    trilha = perfil["trilha"]
    if trilha == "solo" and "apoio" not in perfil:
        perfil["apoio"] = "nenhum"
        perfil["apoio_rotulo"] = "Ninguém, só eu"

    # Dimensões
    respostas_in = entrada.get("respostas", {}) or {}
    faltam = []
    dims = []
    respostas_norm = {}
    detalhe_respostas = []
    for d in q["dimensoes"]:
        notas = []
        det_dim = []
        for p in d["perguntas"]:
            pontua = p.get("pontua", True)
            if p["id"] not in respostas_in or respostas_in[p["id"]] in (None, [], ""):
                if pontua:
                    faltam.append(p["id"])
                continue
            v = respostas_in[p["id"]]
            if p["tipo"] == "multipla":
                idx = resolver_multipla(p, v)
                respostas_norm[p["id"]] = idx
                if not pontua:
                    nota = None
                else:
                    teto = p.get("teto", 1)
                    validas = [i for i in idx if not p["opcoes"][i].get("exclusiva")]
                    nota = min(len(validas), teto) / float(teto)
                    if len(validas) > teto:
                        avisos.append("%s: %d opções marcadas, o teto é %d (conta como %d)."
                                      % (p["id"], len(validas), teto, teto))
            else:
                idx = resolver_opcao(p, v)
                respostas_norm[p["id"]] = idx
                op = p["opcoes"][idx]
                nota = float(op["pontos"]) if pontua else None
                if op.get("solo") and trilha == "equipe":
                    avisos.append("%s: a opção 'Trabalho sozinho(a)' foi marcada, mas a trilha é equipe. "
                                  "Confirme a resposta." % p["id"])
            if nota is not None:
                notas.append(nota)
            det_dim.append({"id": p["id"], "pergunta": p["texto"], "resposta": rotulos(p, idx),
                            "nota": nota})
        pct = (sum(notas) / len(notas)) if notas else 0.0
        dims.append({"id": d["id"], "nome": d["nome"], "peso": d["peso"], "pct": pct,
                     "pontos": pct * d["peso"], "respondidas": len(notas)})
        detalhe_respostas.append({"dimensao": d["nome"], "perguntas": det_dim})
    incompleto = bool(faltam)
    if faltam and not permitir_incompleto:
        raise ErroResposta("faltam respostas obrigatórias: " + ", ".join(faltam))
    if faltam:
        avisos.append("Resultado incompleto. Faltam: " + ", ".join(faltam) + ".")

    total = arred(sum(d["pontos"] for d in dims))
    nivel = [n for n in q["niveis"] if total >= n["min"]][-1]

    prioridades = []
    for pr in nivel["prioridades"]:
        detalhe = pr.get("detalhe_solo") if (trilha == "solo" and pr.get("detalhe_solo")) else pr["detalhe"]
        prioridades.append({"titulo": pr["titulo"], "detalhe": detalhe, "skill": pr["skill"]})

    cobertas = set(nivel["cobertas"])
    lim = q["atencao"]["limite_pct"]
    fracas = [d for d in dims if d["pct"] < lim and d["id"] not in cobertas]
    fracas = sorted(fracas, key=lambda d: d["pct"])[: q["atencao"]["maximo"]]
    dim_q = {d["id"]: d for d in q["dimensoes"]}
    atencao = []
    for d in fracas:
        dq = dim_q[d["id"]]
        rec = dq.get("recomendacao_solo") if (trilha == "solo" and dq.get("recomendacao_solo")) else dq["recomendacao"]
        atencao.append({"id": d["id"], "nome": d["nome"], "pct": arred(d["pct"] * 100),
                        "recomendacao": rec, "skill": dq["skill"]})

    # Setores
    faixas = q["faixas_horas"]
    setores_in = entrada.get("setores", {}) or {}
    setores = []
    for ordem, s in enumerate(q["setores"]):
        si = setores_in.get(s["id"])
        if si is None:
            avisos.append("Setor %s sem resposta: tratado como 'Não temos' [A CONFIRMAR]." % s["nome"])
            si = {"horas": 0}
        h_raw = si.get("horas", 0) if isinstance(si, dict) else si
        faixa_q = {"id": "setor " + s["id"], "opcoes": faixas}
        fi = resolver_opcao(faixa_q, h_raw)
        h = faixas[fi]["valor"]
        inc = si.get("incomodo") if isinstance(si, dict) else None
        if inc is not None:
            inc = int(inc)
            if not 1 <= inc <= 5:
                raise ErroResposta("setor %s: incômodo deve ser de 1 a 5" % s["id"])
        if h > 0 and not inc:
            avisos.append("Setor %s com horas e sem incômodo: a conta usou 1 [A CONFIRMAR]." % s["nome"])
        if h == 0:
            inc = None
        setores.append({"id": s["id"], "nome": s["nome"], "faixa": faixas[fi]["rotulo"], "horas": h,
                        "incomodo": inc, "pontuacao": h * (inc or 1), "ordem": ordem})
    ativos = sorted([s for s in setores if s["horas"] > 0],
                    key=lambda s: (-s["pontuacao"], -s["horas"], s["ordem"]))
    horas_total = sum(s["horas"] for s in setores)
    alvo = ativos[0] if ativos else None
    fila = ativos[1] if len(ativos) > 1 else None
    gargalo = (entrada.get("gargalo") or "").strip()
    lim_g = q["setor_alvo"]["gargalo_max_caracteres"]
    if len(gargalo) > lim_g:
        avisos.append("O gargalo passou de %d caracteres e foi cortado." % lim_g)
        gargalo = gargalo[:lim_g]

    # Alertas de dados e revisão
    alertas = []
    for a in q.get("alertas", []):
        if a["tipo"] == "perfil":
            if perfil.get(a["campo"]) in a["valores"]:
                alertas.append(a["texto"])
        elif respostas_norm.get(a["pergunta"]) in a["opcoes"]:
            if a["texto"] not in alertas:
                alertas.append(a["texto"])

    resultado = {
        "versao_questionario": q["versao"],
        "data": entrada.get("data"),
        "incompleto": incompleto,
        "perfil": perfil,
        "trilha": trilha,
        "nota": total,
        "nivel": {"nome": nivel["nome"], "faixa": "%d a %d" % (nivel["min"], nivel["max"]),
                  "frase": nivel["frase"], "texto": nivel["texto"]},
        "dimensoes": [{"id": d["id"], "nome": d["nome"], "peso": d["peso"],
                       "pct": round(d["pct"], 4), "pontos": round(d["pontos"], 4),
                       "pontos_exibicao": fmt1(d["pontos"]), "pct_exibicao": arred(d["pct"] * 100)}
                      for d in dims],
        "soma_exata": round(sum(d["pontos"] for d in dims), 4),
        "prioridades": prioridades,
        "atencao": atencao,
        "setores": {
            "ranking": [{"posicao": i + 1, "id": s["id"], "nome": s["nome"], "horas": s["horas"],
                         "incomodo": s["incomodo"], "pontuacao": s["pontuacao"]}
                        for i, s in enumerate(ativos[: q["setor_alvo"]["top"]])],
            "todos": [{k: s[k] for k in ("id", "nome", "faixa", "horas", "incomodo", "pontuacao")}
                      for s in setores],
            "horas_total": horas_total,
            "alvo": alvo["nome"] if alvo else None,
            "proximo_da_fila": fila["nome"] if fila else None,
            "gargalo": gargalo,
        },
        "alertas": alertas,
        "avisos": avisos,
        "detalhe_respostas": detalhe_respostas,
    }

    # Modelo de negócio (opcional)
    modelo_in = entrada.get("modelo")
    if modelo_in:
        resultado["modelo"] = calcular_modelo(q["quiz_modelo"], modelo_in, resultado["setores"]["alvo"], avisos)

    # Próximo passo
    resultado["proximo_passo"] = proximo_passo(q["proximo_passo"], trilha, progresso)

    # Comparação com a rodada anterior
    if anterior:
        resultado["comparacao"] = comparar(anterior, resultado)

    # Perfil sugerido para o perfil.md
    modelo_perfil = None
    if resultado.get("modelo"):
        modelo_perfil = "hibrido" if resultado["modelo"]["secundario"] else resultado["modelo"]["principal"]["perfil"]
    resultado["perfil_sugerido"] = {
        "escritorio": perfil.get("escritorio", "[A CONFIRMAR]"),
        "porte": perfil["porte"],
        "trilha": trilha,
        "apoio": perfil.get("apoio") if trilha == "solo" else None,
        "pessoas": perfil.get("pessoas"),
        "areas": perfil.get("areas", []),
        "modelo_de_negocio": modelo_perfil,
        "conta_de_ia": perfil.get("conta_de_ia"),
        "nivel": nivel["nome"],
        "nota": total,
        "setor_alvo": resultado["setores"]["alvo"],
        "proximo_da_fila": resultado["setores"]["proximo_da_fila"],
    }

    resultado["dados_para_proxima_rodada"] = {
        MARCA_DADOS: q["versao"],
        "data": entrada.get("data"),
        "trilha": trilha,
        "porte": perfil["porte"],
        "nota": total,
        "nivel": nivel["nome"],
        "dimensoes": {d["id"]: {"pontos": round(d["pontos"], 4), "pct": round(d["pct"], 4)} for d in dims},
        "setor_alvo": resultado["setores"]["alvo"],
        "horas_total": horas_total,
        "ranking": [s["nome"] for s in ativos[: q["setor_alvo"]["top"]]],
        "modelo": (resultado["modelo"]["principal"]["id"] if resultado.get("modelo") else None),
        "entrada": {"perfil": perfil_in, "respostas": respostas_norm,
                    "setores": {s["id"]: {"horas": s["faixa"], "incomodo": s["incomodo"]} for s in setores},
                    "gargalo": gargalo, "modelo": modelo_in or None},
    }
    return resultado


def calcular_modelo(qm, respostas, alvo_diag, avisos):
    ordem = [m["id"] for m in qm["modelos"]]
    info = {m["id"]: m for m in qm["modelos"]}
    pontos = {k: 0 for k in ordem}
    respondidas = 0
    for p in qm["perguntas"]:
        if p["id"] not in respostas or respostas[p["id"]] in (None, ""):
            continue
        i = resolver_opcao(p, respostas[p["id"]])
        respondidas += 1
        alvos = p["opcoes"][i]["modelos"]
        ganho = 2 if len(alvos) == 1 else 1
        for m in alvos:
            pontos[m] += ganho
    if respondidas < len(qm["perguntas"]):
        avisos.append("Modelo de negócio: resultado parcial, %d de %d perguntas."
                      % (respondidas, len(qm["perguntas"])))
    rank = sorted(ordem, key=lambda k: (-pontos[k], ordem.index(k)))
    top, sec = rank[0], rank[1]
    secundario = None
    if pontos[sec] > 0 and pontos[top] - pontos[sec] <= qm["diferenca_hibrido"]:
        secundario = sec
    combinacao = None
    if secundario:
        par = {top, secundario}
        for c in qm["combinacoes"]:
            if set(c["modelos"]) == par:
                combinacao = c["por_onde_comecar"]
    principal = dict(info[top])
    if alvo_diag is None:
        leitura = "Sem setor-alvo no diagnóstico: use o setor do perfil como hipótese e confirme no mapear-setores."
    elif principal["setor_alvo"] == alvo_diag:
        leitura = "O perfil e o diagnóstico apontam o mesmo setor: %s." % alvo_diag
    else:
        leitura = ("O modelo orienta, o mapa decide. O perfil sugere %s, mas o diagnóstico, feito com as horas "
                   "do seu escritório, aponta %s. Siga o diagnóstico e anote por que o perfil apontou outro."
                   % (principal["setor_alvo"], alvo_diag))
    return {
        "pontos": {info[k]["nome"]: pontos[k] for k in rank if pontos[k] > 0},
        "principal": principal,
        "secundario": dict(info[secundario]) if secundario else None,
        "combinacao": combinacao,
        "leitura_setor": leitura,
        "respondidas": respondidas,
    }


def proximo_passo(cfg, trilha, progresso):
    etapas = cfg["etapas"]
    escolhida = etapas[0]
    if progresso:
        pendentes = [txt for feito, txt in progresso if not feito and not normalizar(txt).startswith("diagnostico")]
        if pendentes:
            alvo = normalizar(pendentes[0])
            for e in etapas:
                if alvo.startswith(normalizar(e["item"])):
                    escolhida = e
                    break
    return {"item": escolhida["item"], "skill": escolhida["skill"], "texto": escolhida[trilha],
            "tarefa_paralela": cfg["tarefa_paralela"]}


def comparar(ant, atual):
    linhas = []
    dims_ant = ant.get("dimensoes", {})
    for d in atual["dimensoes"]:
        a = dims_ant.get(d["id"])
        antes = a["pontos"] if a else None
        linhas.append({"id": d["id"], "nome": d["nome"], "antes": antes, "agora": d["pontos"],
                       "diferenca": (d["pontos"] - antes) if antes is not None else None})
    obs = []
    if ant.get("trilha") and ant.get("trilha") != atual["trilha"]:
        obs.append("A trilha mudou (%s para %s). As perguntas com a opção 'Trabalho sozinho(a)' "
                   "(c1, c2, c3, i5, e1) mudam de régua: leia Cultura, Uso de IA e Equipe com cuidado."
                   % (ant.get("trilha"), atual["trilha"]))
    if ant.get(MARCA_DADOS) and ant.get(MARCA_DADOS) != atual["versao_questionario"]:
        obs.append("A versão do questionário mudou (%s para %s)." % (ant.get(MARCA_DADOS), atual["versao_questionario"]))
    if ant.get("setor_alvo") and ant.get("setor_alvo") != atual["setores"]["alvo"]:
        obs.append("O setor-alvo provisório mudou de %s para %s. Confirme no mapear-setores antes de trocar o POP em andamento."
                   % (ant.get("setor_alvo"), atual["setores"]["alvo"]))
    return {
        "data_anterior": ant.get("data"),
        "nota_antes": ant.get("nota"), "nota_agora": atual["nota"],
        "nivel_antes": ant.get("nivel"), "nivel_agora": atual["nivel"]["nome"],
        "setor_alvo_antes": ant.get("setor_alvo"), "setor_alvo_agora": atual["setores"]["alvo"],
        "horas_antes": ant.get("horas_total"), "horas_agora": atual["setores"]["horas_total"],
        "dimensoes": linhas,
        "observacoes": obs,
    }


# ---------- markdown ----------

def sinal(x):
    if x is None:
        return "sem dado"
    v = math.floor(round(x * 10, 9) + 0.5) / 10
    if v > 0:
        return "+" + fmt1(v)
    if v < 0:
        return "-" + fmt1(-v)
    return "0"


def json_compacto(dados):
    """Um nível de indentação: cada chave de topo numa linha, valores compactos."""
    partes = []
    for k, v in dados.items():
        if isinstance(v, dict) and k == "entrada":
            sub = ",\n".join("    %s: %s" % (json.dumps(k2, ensure_ascii=False), json.dumps(v2, ensure_ascii=False))
                             for k2, v2 in v.items())
            partes.append("  %s: {\n%s\n  }" % (json.dumps(k, ensure_ascii=False), sub))
        else:
            partes.append("  %s: %s" % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)))
    return "{\n" + ",\n".join(partes) + "\n}"


def markdown(r):
    p = r["perfil"]
    L = []
    L.append("# Diagnóstico de prontidão para automação")
    L.append("")
    L.append("- Escritório: %s" % p.get("escritorio", "[A CONFIRMAR]"))
    L.append("- Rodada: %s · questionário versão %s" % (r.get("data") or "[A CONFIRMAR]", r["versao_questionario"]))
    L.append("- Respondido por: %s" % p.get("papel", "[A CONFIRMAR]"))
    L.append("- Dono deste documento: [A DEFINIR]")
    trilha_txt = "solo" if r["trilha"] == "solo" else "equipe"
    extra = (" · apoio: %s" % p.get("apoio_rotulo", p.get("apoio"))) if r["trilha"] == "solo" else ""
    L.append("- Porte: %s · trilha %s%s" % (p.get("porte_rotulo", p["porte"]), trilha_txt, extra))
    if p.get("areas"):
        L.append("- Áreas: %s" % ", ".join(p["areas"]))
    if p.get("volume"):
        L.append("- Processos ativos: %s" % p["volume"])
    if p.get("conta_de_ia"):
        L.append("- Conta de IA: %s" % p.get("conta_de_ia_rotulo", p["conta_de_ia"]))
    L.append("")
    L.append("> A nota é uma foto de hoje, feita por quem respondeu. Ela não julga o trabalho do escritório. "
             "O valor está na comparação entre uma rodada e a próxima. O cálculo foi feito no computador, sem envio para fora.")
    if r["incompleto"]:
        L.append("")
        L.append("> Resultado incompleto: faltaram respostas. Veja os avisos no fim.")
    L.append("")
    L.append("## Resultado")
    L.append("")
    L.append("**Nota %d de 100 · nível %s (%s)**" % (r["nota"], r["nivel"]["nome"], r["nivel"]["faixa"]))
    L.append("")
    L.append("%s %s" % (r["nivel"]["frase"], r["nivel"]["texto"]))
    L.append("")
    L.append("## As 9 dimensões")
    L.append("")
    L.append("| Dimensão | Pontos | Peso | % |")
    L.append("|---|---|---|---|")
    for d in r["dimensoes"]:
        L.append("| %s | %s | %d | %d%% |" % (d["nome"], d["pontos_exibicao"], d["peso"], d["pct_exibicao"]))
    L.append("| **Total** | **%d** | 100 | |" % r["nota"])
    L.append("")
    L.append("A nota é a soma exata dos pontos (%s), arredondada. Por isso a soma da coluna, já arredondada, pode diferir por pouco."
             % ("%.2f" % r["soma_exata"]).replace(".", ","))
    L.append("")
    L.append("## Prioridades para o nível %s" % r["nivel"]["nome"])
    L.append("")
    for i, pr in enumerate(r["prioridades"], 1):
        L.append("%d. **%s** %s (skill `%s`)" % (i, pr["titulo"], pr["detalhe"], pr["skill"]))
    L.append("")
    if r["atencao"]:
        L.append("## Também merece atenção")
        L.append("")
        for a in r["atencao"]:
            L.append("- **%s (%d%%).** %s (skill `%s`)" % (a["nome"], a["pct"], a["recomendacao"], a["skill"]))
        L.append("")
    if r["alertas"]:
        L.append("## Cuidados com dados e revisão")
        L.append("")
        for a in r["alertas"]:
            L.append("- %s" % a)
        L.append("")
    s = r["setores"]
    L.append("## Setor-alvo provisório")
    L.append("")
    if s["ranking"]:
        a = s["ranking"][0]
        L.append("**%s**: %d h por semana, incômodo %d de 5 (pontuação %d)."
                 % (a["nome"], a["horas"], a["incomodo"] or 1, a["pontuacao"]))
        L.append("")
        L.append("| # | Setor | Horas por semana | Incômodo | Horas × incômodo |")
        L.append("|---|---|---|---|---|")
        for x in s["ranking"]:
            L.append("| %d | %s | %d | %s | %d |" % (x["posicao"], x["nome"], x["horas"],
                                                    x["incomodo"] if x["incomodo"] else "1 [A CONFIRMAR]",
                                                    x["pontuacao"]))
        L.append("")
    else:
        L.append("Nenhum setor com horas marcadas. [A CONFIRMAR]")
        L.append("")
    L.append("Total mapeado: %d h por semana. Próximo da fila: %s." % (s["horas_total"], s["proximo_da_fila"] or "nenhum"))
    L.append("")
    L.append("O setor-alvo é provisório: ele vem de faixas de horas estimadas. A confirmação vem no `mapear-setores`, "
             "com as horas registradas e o potencial de IA de cada setor.")
    if s["gargalo"]:
        L.append("")
        L.append("Maior gargalo, nas palavras de quem respondeu: \"%s\"" % s["gargalo"])
    L.append("")
    m = r.get("modelo")
    if m:
        pr = m["principal"]
        L.append("## Modelo de negócio")
        L.append("")
        L.append("**%s** (%s)." % (pr["nome"], ", ".join("%s %d" % (k, v) for k, v in m["pontos"].items())))
        if m["secundario"]:
            L.append("Também tem traços de **%s**: leia os dois perfis e a parte de híbridos em `references/modelos-de-negocio.md`."
                     % m["secundario"]["nome"])
            if m["combinacao"]:
                L.append("Combinação conhecida: %s" % m["combinacao"])
        L.append("")
        L.append("- Setor-alvo provável do perfil: %s (alternativo: %s)." % (pr["setor_alvo"], pr["alternativo"]))
        L.append("- Mistura de S, A e H: %s" % pr["mistura_sah"])
        L.append("- Tipo de base de conhecimento: %s" % pr["tipo_de_base"])
        L.append("- Risco que mais pesa: %s" % pr["risco_principal"])
        L.append("- Primeiro passo típico: %s" % pr["primeiro_passo"])
        L.append("")
        L.append(m["leitura_setor"])
        L.append("")
    c = r.get("comparacao")
    if c:
        L.append("## Evolução desde a rodada de %s" % (c["data_anterior"] or "antes"))
        L.append("")
        L.append("Nota: %s para %d (%s). Nível: %s para %s. Setor-alvo: %s para %s. Horas mapeadas: %s para %d."
                 % (c["nota_antes"], c["nota_agora"],
                    sinal(c["nota_agora"] - c["nota_antes"]) if c["nota_antes"] is not None else "sem dado",
                    c["nivel_antes"], c["nivel_agora"], c["setor_alvo_antes"], c["setor_alvo_agora"],
                    c["horas_antes"], c["horas_agora"]))
        L.append("")
        L.append("| Dimensão | Antes | Agora | Diferença |")
        L.append("|---|---|---|---|")
        for d in c["dimensoes"]:
            L.append("| %s | %s | %s | %s |" % (d["nome"], fmt1(d["antes"]) if d["antes"] is not None else "sem dado",
                                                fmt1(d["agora"]), sinal(d["diferenca"])))
        L.append("")
        for o in c["observacoes"]:
            L.append("- %s" % o)
        if c["observacoes"]:
            L.append("")
    pp = r["proximo_passo"]
    L.append("## Próximo passo")
    L.append("")
    L.append("- **%s**, com a skill `%s`. %s" % (pp["item"], pp["skill"], pp["texto"]))
    L.append("- %s" % pp["tarefa_paralela"])
    L.append("")
    L.append("## Respostas")
    L.append("")
    for bloco in r["detalhe_respostas"]:
        L.append("**%s**" % bloco["dimensao"])
        L.append("")
        for x in bloco["perguntas"]:
            resp = x["resposta"] if isinstance(x["resposta"], str) else "; ".join(x["resposta"])
            nota = "não pontua" if x["nota"] is None else fmt_pts(round(x["nota"], 4))
            L.append("- %s %s → %s (%s)" % (x["id"], x["pergunta"], resp, nota))
        L.append("")
    if r["avisos"]:
        L.append("## Avisos do cálculo")
        L.append("")
        for a in r["avisos"]:
            L.append("- %s" % a)
        L.append("")
    L.append("## Dados para a próxima rodada")
    L.append("")
    L.append("Não edite este bloco: a próxima rodada do diagnóstico lê daqui para comparar.")
    L.append("")
    L.append("```json")
    L.append(json_compacto(r["dados_para_proxima_rodada"]))
    L.append("```")
    L.append("")
    return "\n".join(L)


# ---------- principal ----------

def main(argv=None):
    ap = argparse.ArgumentParser(description="Calcula o diagnóstico do escritório (cálculo local).")
    ap.add_argument("respostas")
    ap.add_argument("--questionario", default=QUESTIONARIO_PADRAO)
    ap.add_argument("--anterior")
    ap.add_argument("--perfil")
    ap.add_argument("--formato", choices=["ambos", "json", "md"], default="ambos")
    ap.add_argument("--saida-md")
    ap.add_argument("--permitir-incompleto", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.questionario, encoding="utf-8") as f:
            q = json.load(f)
        with open(a.respostas, encoding="utf-8") as f:
            entrada = json.load(f)
        anterior = ler_dados_anteriores(a.anterior) if a.anterior else None
        progresso = ler_progresso(a.perfil) if a.perfil and os.path.exists(a.perfil) else None
        r = calcular(q, entrada, a.permitir_incompleto, anterior, progresso)
    except ErroResposta as e:
        print("ERRO: %s" % e, file=sys.stderr)
        return 2
    md = markdown(r)
    if a.saida_md:
        with open(a.saida_md, "w", encoding="utf-8") as f:
            f.write(md)
    if a.formato in ("ambos", "json"):
        print(json.dumps(r, ensure_ascii=False, indent=2))
    if a.formato == "ambos":
        print("\n===== RESUMO EM MARKDOWN =====\n")
    if a.formato in ("ambos", "md"):
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
