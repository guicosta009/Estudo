# Registro de peças
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME]

> Grava em `escritorio/06-medicao/registro-de-pecas.md` (ou numa planilha com as mesmas colunas). Uma linha por peça. É onde os indicadores dos POPs de peça são anotados e de onde a `medir-retorno` tira o "antes" e o "depois". Comece antes de mudar o fluxo, à mão se precisar: o número de antes é o que mostra o ganho depois. Use só o código do caso, nunca o nome do cliente.

## Colunas

```
Data do gatilho | Código do caso | Tipo de peça | Área | Modelo usado | Ficha conferida em | Minuta v1 em | Rodadas de revisão | Erros pegos (citação / fato / valor / pedido / dado / forma) | Protocolo em | Prazo interno cumprido | Observação
```

Linha de exemplo (fictícia):

```
03/08/2026 | CONS-0412 | Inicial | Consumidor | CONS_INICIAL_cobranca-indevida 3.0 | 04/08/2026 | 05/08/2026 | 2 | citação 1, valor 1 | 07/08/2026 | sim | faltava fatura de maio na ficha
```

## Os cinco números

| Número | O que mostra |
|---|---|
| Tempo do gatilho ao protocolo (dias úteis) | Se o ciclo encurtou de verdade, ou se a peça só ficou parada em outra etapa |
| Rodadas de revisão | Quantas vezes a minuta voltou. Se sobe depois da IA, o problema costuma estar no briefing ou no modelo |
| Erros pegos por tipo | Citação, fato, valor, pedido, dado do cliente, forma. Diz onde o POP precisa de reforço |
| Peças que saíram de modelo do banco | O avanço da base. Peça sem modelo é candidata a virar modelo |
| Prazo interno cumprido | Sim ou não, peça a peça |

## O erro que mais aparece e o que ajustar

| Erro | Onde costuma estar a causa | O que ajustar |
|---|---|---|
| Citação | Pesquisa sem tabela, ou minuta pedindo citação livre para a IA | Reforçar o passo de pesquisa e usar o prompt 3, que só aceita citação da tabela |
| Fato | Ficha sem fonte ou minuta feita direto dos PDFs | Nenhuma minuta sem ficha conferida. Fato sem fonte volta para a ficha |
| Valor | Memória de cálculo fora da ficha ou valor digitado em mais de um lugar | Um valor, uma fonte: o campo 8 da ficha |
| Pedido | Tese e pedidos decididos depois da minuta | Campos 6 e 7 da ficha assinados antes da minuta |
| Dado do cliente | Modelo com dado de caso antigo ou qualificação feita pela IA | Limpar o modelo (prompt 5) e trazer a qualificação sempre do cadastro |

Exemplo: um escritório de 3 pessoas que registra as peças de duas semanas e vê "citação" liderando os erros já sabe qual passo do POP reforçar primeiro. Os números são do escritório, e a decisão sai deles.

## Registro

(uma linha por peça, abaixo)
