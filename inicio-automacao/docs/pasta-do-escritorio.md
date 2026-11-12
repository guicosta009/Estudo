# A pasta do escritório

O plugin guarda tudo o que o escritório constrói numa pasta chamada `escritorio/`, dentro da pasta de trabalho que o advogado abriu (no Claude Code, no Cowork ou no app desktop). Ela é a memória do método: cada skill lê o que as anteriores gravaram e grava o que produz.

A pasta é criada pelo `/inicio-automacao:comecar`. Se uma skill precisar gravar e a pasta não existir, ela cria só o que precisa e avisa.

## Estrutura

```
escritorio/
  CLAUDE.md                       ← instruções fixas: o Claude lê antes de qualquer tarefa nesta pasta
  perfil.md                       ← porte, trilha, áreas, nível, setor-alvo, progresso
  diagnosticos/
    AAAA-MM-DD.md                 ← um arquivo por rodada do diagnóstico
    em-andamento.json             ← respostas de uma rodada ainda não terminada (apagado ao final)
  01-cultura/
    codigo-do-escritorio.md
    instrucoes-do-projeto.md      ← o código convertido em instruções para um Projeto no Claude
    regra-de-uso-de-ia.md
    acordos/                      ← acordo de uso de IA (um por pessoa, ou o autocompromisso do solo)
      assinaturas.md              ← quem assinou, versão e data
    mudanca/                      ← retrato cultural, ficha do piloto, roteiro da reunião de lançamento
      registro-de-prompts.md      ← os prompts validados, com quem validou e quando
      paineis-semanais.md
    nucleo/                       ← termo de nomeação, plano de 90 dias, fichas de ideia
      atas.md
  02-mapa/
    registro-de-horas.xlsx        ← ou registro-de-horas.tsv, quando não houver openpyxl
    atividades-<setor>.md
    ranking-de-setores.md
    plano-5w2h-<setor>.md
  03-pops/
    00-mapa-de-pops.md            ← todos os POPs do escritório, um por linha: código, dono, versão, status, degrau (gerir-pops)
    00-mapa-de-pops.tsv           ← a mesma tabela para colar numa planilha (opcional)
    <setor>/
      pop-<sigla>-<nn>-<processo>.md        ← POP com S, A e H, o fluxograma (Mermaid, texto e raias) e, em anexo, o retrato de como era
      fluxograma-<processo>.md               ← só quando o desenho vem antes do POP (desenhar-fluxograma)
      auditoria-<processo>-AAAA-MM-DD.md     ← relatório do auditar-riscos
      testes/                                ← checklist de qualidade, teste de mesa, teste com a IA e piloto (testar-pop)
      revisoes-<sigla>-<nn>.md               ← registro das revisões de cada POP (gerir-pops)
      implantacao-<sigla>-<nn>.md            ← roteiro de implantação na equipe e perguntas frequentes (gerir-pops)
      _em-construcao/                        ← rascunho da versão nova enquanto a vigente continua valendo
      _arquivo/                              ← versões substituídas: pop-<sigla>-<nn>-<processo>-v<X-Y>.md
  04-base/
    INDICE.md                     ← o que existe na base, com dono e data
    comum/                        ← o que vale para todos os setores
    <setor>/<area>/               ← modelos, checklists, critérios, respostas aprovadas
    producao-de-pecas/            ← ficha-de-briefing.md, checklist-revisao-peca.md, modelos/ (com INDICE.md) e teses/caderno-de-teses.md (organizar-producao-de-pecas)
    relacionamento-com-o-cliente/ ← biblioteca-de-mensagens.md (organizar-atendimento-whatsapp)
    casos-de-teste/<automacao>/   ← casos reais anonimizados, com o gabarito, para testar cada automação
    _inventario/AAAA-MM-DD/       ← inventário da pasta de modelos e plano de reorganização (inventariar-base), fora do Projeto no Claude
    _arquivo/                     ← versões substituídas (fora do Projeto no Claude)
  05-automacoes/
    <nome-da-automacao>/
      ficha.md                    ← nível-meta, prontidão, responsável
      instrucoes/                 ← uma instrução por passo S ou A
      plano-para-erro.md
      registro-de-uso.md
      fila/                       ← rascunhos gerados pela automação, esperando revisão humana
      skill/                      ← a skill gerada pelo pop-para-skill, pronta para instalar
  06-medicao/
    valor-da-hora.md
    linha-de-base-<setor>.md
    painel-AAAA-MM.md
    incidentes.md                 ← livro de incidentes e quase incidentes
    registro-de-pecas.md          ← peças produzidas com IA: rodadas de revisão e erros pegos (organizar-producao-de-pecas)
    revisoes/                     ← calendário de rituais e registro das revisões quinzenais, mensais e trimestrais
```

Nomes de arquivo: minúsculas, sem acento, palavras separadas por hífen. Cada documento traz no topo nome, versão, data e dono.

**Código do POP.** Todo POP tem um código com a sigla do setor e um número de dois dígitos, que nunca é reaproveitado: `POP-PEC-01`. No cabeçalho e nas conversas, o POP aparece como "POP-PEC-01 Petição inicial v1.0"; o arquivo fica `03-pops/producao-de-pecas/pop-pec-01-peticao-inicial.md`, com a versão só no cabeçalho. A versão vigente é uma só: a anterior vai para `_arquivo/` e sai do Projeto no Claude. Siglas: ATD atendimento e triagem, COM comercial, PEC produção de peças, PRZ prazos e controladoria, AUD audiências e diligências, FIN financeiro e cobrança, REL relacionamento com o cliente, MKT marketing e conteúdo, EQP gestão de equipe, ADM administrativo. O próximo número livre de cada setor sai do `00-mapa-de-pops.md`.

**Quando o escritório guarda tudo no Drive ou no OneDrive.** A mesma organização funciona fora do Claude, com cinco pastas na raiz: `00 Código do escritório` (o que está em `01-cultura/`), `01 POPs` (uma subpasta por sigla, com o mapa de POPs na raiz), `02 Base` (o que está em `04-base/`), `03 Habilidades` (as skills geradas, em `.zip`) e `04 Registros` (horas, painéis, incidentes e revisões). As skills continuam gravando em `escritorio/` e indicam onde cada arquivo fica nessa versão.

Nome das pastas de setor (em `03-pops/` e `04-base/`): `atendimento-e-triagem`, `comercial`, `producao-de-pecas`, `prazos-e-controladoria`, `audiencias-e-diligencias`, `financeiro-e-cobranca`, `relacionamento-com-o-cliente`, `marketing-e-conteudo`, `gestao-de-equipe`, `administrativo`. Nos arquivos de `02-mapa/`, o `<setor>` usa o mesmo nome.

## O `perfil.md`

Formato fixo, para que todas as skills leiam do mesmo jeito:

```markdown
---
escritorio: [NOME]
porte: solo | 2-5 | 6-20 | 20+
trilha: solo | equipe
apoio: nenhum | estagiario | secretaria | estagiario-e-secretaria   # só na trilha solo
pessoas: [FUNÇÕES, SEM NOMES DE CLIENTE]                             # ex.: 2 advogadas, 1 estagiário
areas: [LISTA]
modelo_de_negocio: full-service | boutique | volume | solo | consultivo | digital | correspondencia | hibrido   # se híbrido, dizer quais: ex. hibrido (solo + digital)
conta_de_ia: nenhuma | pessoal-gratuita | pessoal-paga | profissional | equipe | mista
nivel: Zero | Base | Estrutura | Automação
nota: [0 a 100]
setor_alvo: [UM DOS 10 SETORES]
proximo_da_fila: [SETOR]
criado_em: AAAA-MM-DD
atualizado_em: AAAA-MM-DD
---

## Progresso

- [ ] Diagnóstico
- [ ] Código do escritório
- [ ] Regra de uso de IA
- [ ] Mudança e núcleo (equipe) / bloco fixo semanal (solo)
- [ ] Mapa de setores e setor-alvo confirmado
- [ ] POP do setor-alvo com S, A e H
- [ ] Base de conhecimento do setor-alvo
- [ ] Prontidão e primeira automação
- [ ] Linha de base e primeiro painel
- [ ] Primeira revisão trimestral

Uma etapa em andamento pode trazer o estado entre parênteses, por exemplo `- [ ] Código do escritório (v0, pendências: 3)` ou `- [ ] Regra de uso de IA (política aprovada, acordos 2 de 4)`.

## Etapas puladas

(o que o advogado decidiu pular, com data e motivo)

## Histórico

(uma linha por mudança importante: nova nota, novo setor-alvo, nova pessoa na equipe)
```

**Como a trilha é definida:**
- `porte: solo` (inclusive com estagiário ou secretária) leva à `trilha: solo`. A pessoa de apoio vira a embaixadora do método.
- Qualquer outro porte leva à `trilha: equipe`. O porte ajusta a intensidade (veja `docs/trilhas.md`).
- Quando o solo contrata a primeira pessoa, o `perfil.md` muda de trilha e a `revisao-periodica` sugere o que refazer.

## O `CLAUDE.md` da pasta

O `/comecar` grava este arquivo. Ele faz o Claude carregar a régua do escritório sempre que alguém trabalhar nesta pasta.

```markdown
# Escritório [NOME]

Esta pasta guarda a estrutura do escritório: cultura, mapa de setores, POPs, base de conhecimento, automações e medição.

Antes de qualquer tarefa aqui:
1. Leia `perfil.md` para saber o porte, a trilha e o setor-alvo.
2. Siga o `01-cultura/codigo-do-escritorio.md` (tom, prazos, quem decide, o que nunca fazemos) e a `01-cultura/regra-de-uso-de-ia.md`.
3. Quando a tarefa seguir um POP, abra o POP em `03-pops/` e consulte só o que ele cita em `04-base/`. Siga só POP com status Vigente ou Em revisão; ignore `_arquivo/` e `_em-construcao/`.

Regras fixas:
- Nunca invente lei, jurisprudência, número de processo, prazo ou dado. Marque [CONFERIR] o que precisa ser checado na fonte.
- Se aparecer dado de cliente sem anonimização, avise e proponha a versão anonimizada antes de continuar.
- Escolha de tese, notícia ruim ao cliente, assinatura, aconselhamento de cliente vulnerável e envio sem revisão humana são sempre de uma pessoa.
- Tudo o que sai do escritório passa por revisão humana.
```
