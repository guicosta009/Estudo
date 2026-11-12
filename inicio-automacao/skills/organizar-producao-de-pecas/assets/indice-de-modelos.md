# Banco de modelos de peça: índice
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Produção de peças · Área: todas · Usado por: POP-PEC-01 a 05 (abrir a tarefa e sugerir o modelo; redigir a minuta) · Acesso: geral
Aprovado por: [FUNÇÃO OU NOME] · Próxima revisão: revisão trimestral

> Grava em `escritorio/04-base/producao-de-pecas/modelos/INDICE.md`. É a lista de modelos vigentes do banco: modelo fora deste índice não existe para a IA. O `04-base/INDICE.md` geral tem uma linha que aponta para este arquivo.

## Pastas

```
04-base/producao-de-pecas/modelos/
  INDICE.md
  previdenciario/
  trabalhista/
  familia/            ← acesso restrito quando houver criança
  consumidor/
  civel/
```

Uma pasta por área, só das áreas que o escritório atende. Dentro dela, um arquivo por modelo: `modelo-<tipo>-<assunto>.md` (ou o .docx com a ficha `.md` ao lado). Versões antigas vão para `04-base/_arquivo/` com a data no nome e saem do Projeto no mesmo dia.

## Modelos vigentes

| Código | Arquivo | Tipo de peça | Versão | Dono | Última revisão | Próxima revisão | Fundamentação conferida em | Situação |
|---|---|---|---|---|---|---|---|---|
| [ÁREA]_[TIPO]_[assunto] | `<area>/modelo-<tipo>-<assunto>.md` | | | | | | | rascunho / em uso |

## Catálogo de peças curtas (POP-PEC-04)

Um modelo por tipo de manifestação. O que ainda não tem modelo fica na lista de candidatos.

| Tipo de manifestação | Mero expediente ou com conteúdo | Código do modelo | Situação |
|---|---|---|---|
| Ciência | Mero expediente | [A DEFINIR] | |
| Juntada de documento | Mero expediente | [A DEFINIR] | |
| Manifestação sobre laudo | Com conteúdo | [A DEFINIR] | |
| Impugnação de cálculo | Com conteúdo | [A DEFINIR] | |
| Réplica | Com conteúdo | [A DEFINIR] | |

## Candidatos a modelo

Peça feita sem modelo, trecho que ficou melhor que o modelo, manifestação que se repete. Quem decide se entra é o dono do modelo (ou o advogado da área).

| Data | Sugestão | De qual peça (código do caso) | Sugerido por | Decisão |
|---|---|---|---|---|
| | | | | |

## Montagem do banco (acompanhamento)

- [ ] Inventário: tudo numa pasta só, listado por área e tipo, duplicados apontados.
- [ ] As cinco peças que o escritório mais faz, escolhidas pelo registro de peças ou pela controladoria do último mês.
- [ ] A melhor versão de cada uma, escolhida pelo advogado (H).
- [ ] Campos marcados e dado de cliente retirado (prompt 5).
- [ ] Fundamentação datada, ou `[CONFERIR]` no próprio modelo.
- [ ] Ficha do modelo preenchida, dono definido, próxima revisão marcada.
- [ ] O resto movido para `_arquivo/`, fora do Projeto.

## Mudanças
- 1.0 · AAAA-MM-DD · índice criado na organizar-producao-de-pecas · aprovado por [FUNÇÃO]
