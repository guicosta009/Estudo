# Ficha do modelo

Vai no topo de cada modelo do banco (`escritorio/04-base/producao-de-pecas/modelos/<area>/modelo-<tipo>-<assunto>.md`) ou, quando o modelo é um .docx, num arquivo `.md` com o mesmo nome ao lado dele. A primeira linha é o cabeçalho padrão da base (o da `montar-base`); o resto é o que só modelo de peça precisa ter.

```
# Modelo: [TIPO DE PEÇA] · [ASSUNTO]
Versão: [X.Y] · Revisado em: AAAA-MM-DD · Dono: [NOME] · Situação: rascunho | em uso | em revisão
Setor: Produção de peças · Área: [ÁREA] · Usado por: [POP-PEC-NN, passo de redigir a minuta] · Acesso: geral | restrito
Aprovado por: [ADVOGADO RESPONSÁVEL PELA ÁREA] · Próxima revisão: [DATA OU "revisão trimestral"]

FICHA DO MODELO
Código: [ÁREA]_[TIPO]_[assunto]          (ex.: PREV_INICIAL_concessao-incapacidade)
Área: [ ] · Tipo de peça: [ ]

QUANDO USAR
[Situação em que este modelo serve]

QUANDO NÃO USAR
[Situações parecidas em que ele não serve, e qual modelo usar no lugar]

TESES QUE O MODELO USA
[Tese] · ficha no caderno de teses: [NOME DA TESE]

CAMPOS VARIÁVEIS
[CLIENTE], [QUALIFICAÇÃO DO CLIENTE], [PARTE CONTRÁRIA], [FATOS], [PEDIDOS], [VALOR DA CAUSA], [OUTROS]

FUNDAMENTAÇÃO DO MODELO
[Citação] · última conferência na fonte oficial: [DATA] · por: [NOME]
(citação sem data é tratada como [CONFERIR] em toda peça que usar o modelo)

O QUE ESTE MODELO SEMPRE PEDE
[Pedidos ou trechos que não podem sair em nenhuma peça feita com ele]

HISTÓRICO
[X.Y] · [DATA] · [o que mudou e por quê: decisão recebida, erro pego na revisão, mudança de entendimento]
```

## Como preencher

- **Código e nome do arquivo.** O código (`[ÁREA]_[TIPO]_[assunto]`) é como a equipe e a IA chamam o modelo na ficha de briefing e no prompt 3. O arquivo segue o padrão da base: minúsculas, sem acento, sem versão no nome (`modelo-inicial-concessao-incapacidade.md`). A versão mora no cabeçalho. Siglas de área sugeridas: PREV, TRAB, FAM, CONS, CIV. Tipos: INICIAL, CONTEST, RECURSO, MANIF, CUMPR.
- **Versão.** Muda o primeiro número quando muda a tese ou a estrutura; o segundo quando muda redação, pedido ou citação.
- **Dono.** Uma pessoa com nome. É ela que aprova mudança e marca a próxima revisão.
- **Próxima revisão.** Pela base, revisão trimestral. O escritório pode marcar outra (por exemplo, a cada seis meses), ou antes se chegar decisão relevante ou a revisão pegar o mesmo erro duas vezes no modelo: [A DEFINIR].
- **Fundamentação datada.** Toda citação com a data da última conferência na fonte. Sem data, `[CONFERIR]`.
- **Campos.** Nenhum dado de cliente no corpo do modelo. Só campos entre colchetes.

## O que é modelo vivo

| Pergunta | Pasta de modelos | Banco vivo |
|---|---|---|
| Qual é a versão certa? | "modelo_FINAL", "modelo_FINAL_v2", "usar_esse" | Uma versão vigente por modelo, com número e data |
| Quem cuida? | Ninguém. Ou quem fez, que já saiu | Cada modelo tem dono com nome |
| Quando usar? | Depende de quem pergunta | A ficha diz quando usar e quando não usar |
| A fundamentação vale? | Ninguém sabe desde quando está lá | Cada citação com a data da última conferência na fonte |
| Tem dado de cliente? | Às vezes, no meio do texto | Só campos: `[CLIENTE]`, `[PARTE CONTRÁRIA]`, `[VALOR 1]` |
| Quando muda? | Quando alguém lembra | Quando chega decisão relevante, quando a revisão pega erro repetido ou na data de revisão marcada |

Erro que a revisão pega duas vezes no mesmo modelo costuma ser defeito do modelo: a correção é feita nele, com nova versão e linha no histórico.
