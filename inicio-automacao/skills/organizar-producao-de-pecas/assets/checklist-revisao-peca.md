# Checklist de revisão de peça feita com IA
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Produção de peças · Área: todas · Usado por: POP-PEC-01 a 05 (revisar a forma e as citações pelo checklist) e prompt 4 · Acesso: geral
Aprovado por: [FUNÇÃO OU NOME] · Próxima revisão: revisão trimestral, ou antes se a revisão pegar o mesmo erro duas vezes

> O portão de toda peça antes da assinatura. Revisar peça sem critério escrito é enxugar gelo: cada dia a revisão pega uma coisa diferente, dependendo do cansaço. O checklist faz a revisão pegar sempre as mesmas coisas. A IA aponta, a pessoa corrige, e a citação só é conferida por quem abriu a fonte. Se a `montar-base` já criou um `checklist-revisao-peca.md`, esta versão o substitui: suba a versão e marque as mudanças com `[NOVO]` ou `[ALTERADO]`.

## As três revisões

| Revisão | O que olha | Quem faz | Sigla |
|---|---|---|---|
| Técnica | A tese está bem construída, os pedidos decorrem dos fatos, nada contradiz a estratégia, a peça resiste à leitura da outra parte | A IA faz a leitura crítica e lista pontos. O advogado decide | A (leitura crítica) e H (revisão final) |
| De forma | Nomes, números, datas, valores, anexos, endereçamento, português, tom | A IA aponta pelo checklist. Quem montou corrige | A |
| De citações | Cada lei, súmula, precedente e doutrina citada foi aberta na fonte oficial e diz o que a peça diz que ela diz | A IA lista e cruza com a tabela de citações. Uma pessoa abre a fonte | A |

## Uma citação pode entrar na peça?

1. A IA sugeriu uma citação.
2. **Alguém abriu na fonte oficial?** (site do tribunal, legislação oficial, obra consultada). Se não: fica `[CONFERIR]` e a peça não vai para assinatura assim.
3. **O texto diz o que a peça diz que ele diz?** (número, órgão, data e trecho conferidos). Se não: a citação sai ou o argumento é reescrito, por decisão do advogado (H).
4. Se sim: entra na tabela de citações com link, data e nome de quem conferiu. Só então pode ficar na peça.

Peça antiga e modelo do banco não servem de fonte. Citação de modelo sem data de conferência é tratada como `[CONFERIR]` em toda peça que usar o modelo.

## O checklist (colar no Projeto de peças)

```
CHECKLIST DE REVISÃO DE PEÇA FEITA COM IA
Peça: [ ] · Código do caso: [ ] · Revisor: [ ] · Data: [ ]

CITAÇÕES E JURISPRUDÊNCIA
[ ] Toda decisão citada foi aberta na fonte oficial (número, órgão, data e relator conferidos, link na tabela)
[ ] O trecho entre aspas existe na fonte e diz o que a peça diz que ele diz (trecho que não foi achado na íntegra sai)
[ ] Súmula, tema ou enunciado conferido no site oficial, com a redação atual e a situação de vigência
[ ] Artigo de lei conferido na redação vigente, na legislação oficial
[ ] Nenhuma marcação [CONFERIR] sobrando no texto (busca pela marcação antes de mandar para assinatura)

FATOS E DOCUMENTOS
[ ] Cada fato da peça está na ficha de briefing, com documento e página (fato que só está na minuta foi a IA que trouxe: sai ou volta para a ficha)
[ ] Datas, nomes e números iguais aos documentos originais (a ficha também pode ter erro)
[ ] Fato que é só relato do cliente entrou por decisão do advogado, com a prova indicada
[ ] Todo documento citado está anexado, na ordem em que aparece, com o nome do arquivo batendo com a referência

PEDIDOS
[ ] Todo pedido decidido na ficha (campo 7) está na peça, e nenhum pedido a mais
[ ] Cada pedido tem fato e fundamento que o sustenta
[ ] Pedido de urgência, se houver, com o motivo demonstrado e a prova do risco apontada

VALORES E PRAZOS
[ ] Valor da causa coerente com os pedidos e com a memória de cálculo, conferido por quem calculou
[ ] O mesmo valor escrito igual em toda a peça, em número e por extenso, nos fatos, nos pedidos e no valor da causa
[ ] Prazo fatal conferido pela controladoria (nunca só sugerido pela IA), e protocolo planejado antes do prazo interno

TOM
[ ] Tom do código do escritório, sem adjetivo sobrando nem ataque pessoal à outra parte
[ ] Nenhuma frase genérica que serviria para qualquer caso

DADOS DO CLIENTE
[ ] Qualificação trazida do cadastro e nenhum campo [CLIENTE] ou [PARTE CONTRÁRIA] esquecido
[ ] Nenhum dado de outro cliente herdado do modelo (nome, cidade, valor ou data de caso antigo)
[ ] Dado sensível só o que o pedido exige, conforme o campo 11 da ficha
[ ] Arquivo final sem comentários, marcas de revisão ou propriedades de outra peça

REVISÃO FINAL (sempre H)
[ ] Leitura integral por quem assina
[ ] Nas peças de maior risco, também pelo revisor sênior (no solo: em outro dia ou por revisor externo)
[ ] Assinatura e autorização do protocolo pelo advogado
```

## Versão reduzida (manifestações curtas, POP-PEC-04)

Citações e jurisprudência (todos os itens) · Fatos e documentos (os dois primeiros) · Dados do cliente (todos) · Revisão final (leitura integral e assinatura). Peça curta também cita, e citação curta também precisa de fonte.

## Itens próprios deste escritório

[A DEFINIR] (com o advogado, a partir dos erros que o registro de peças mostrar. Exemplo: em demandas de massa, conferir se os fatos são do próprio cliente e não de outro do lote.)

## Revisão que vira carimbo

O passo é A no papel, mas a pessoa aprova sem ler porque a fila está grande. É o jeito mais comum de um checklist morrer. Duas defesas: revisar em outro momento, e não logo depois de escrever; e anotar no registro de peças cada erro que a revisão pegou. Checklist que nunca pega nada ou está perfeito ou não está sendo lido.

## Mudanças
- 1.0 · AAAA-MM-DD · primeira versão, criada na organizar-producao-de-pecas · aprovado por [FUNÇÃO]
