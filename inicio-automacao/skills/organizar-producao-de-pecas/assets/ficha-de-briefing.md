# Ficha de briefing de peça
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Produção de peças · Área: todas · Usado por: POP-PEC-01 a 05 (montar a ficha de briefing; a minuta só usa o que está nela) · Acesso: geral
Aprovado por: [FUNÇÃO OU NOME] · Próxima revisão: revisão trimestral

> A entrada da IA em toda peça. Em uma ou duas páginas, diz o que aconteceu, com a prova de cada fato, e o que o advogado já decidiu sobre a peça. Este arquivo é o modelo em branco e fica na base e no Projeto de peças. **A ficha preenchida de cada caso fica na pasta do caso, nunca na base.**

## Regras de uso

- **Quem preenche:** a IA preenche fatos, documentos e lacunas a partir dos documentos anonimizados (prompt 1). Quem monta a minuta confere cada fato contra o documento. Os campos 6 (tese) e 7 (pedidos) ficam em branco até o advogado decidir.
- **Quando está pronta:** quando nenhum fato está sem fonte e a tese está assinada com nome e data. Antes disso, nada de minuta.
- **Fonte da verdade:** documento novo depois da minuta pronta volta para a ficha primeiro. Só depois se mexe no texto.
- **Antes de colar qualquer documento na IA:** troque nomes por códigos (`[CLIENTE]`, `[PARTE CONTRÁRIA]`, `[EMPRESA]`, `[FILHO 1]`, `[TESTEMUNHA 1]`). Tire CPF, RG, NIT, endereço, telefone, e-mail e dados bancários. O número do processo vira `[PROCESSO]`. Dado de saúde só se a peça precisa dele. Use a conta profissional do escritório. A tabela que diz quem é quem fica na pasta do caso, fora da IA.

## Os campos que mais se preenche errado

| Campo | O cuidado |
|---|---|
| 3. Fatos com fonte | Cada fato aponta documento e página. O que o cliente contou e nenhum documento mostra entra como `[SÓ RELATO]`, e só vai para a peça se o advogado decidir, já pensando em como provar. |
| 6. Teses descartadas | Escrever o que ficou de fora, e por quê, impede a IA de "lembrar" daquela tese na minuta. E impede o estagiário de achar que o advogado esqueceu. |
| 10. O que não pode faltar | O pedido que o escritório sempre faz nesse tipo de caso, ou o detalhe que o cliente repetiu três vezes na consulta. É o campo que mais evita retrabalho. |
| 11. O que não pode aparecer | O motivo pessoal que o cliente contou em confiança, o diagnóstico que não interessa ao pedido. A IA tende a usar tudo o que recebe, então diga o que fica de fora. |
| 9. Prazos | O prazo fatal vem da controladoria, conferido. A IA não calcula prazo de peça. A ficha só registra a data que alguém já conferiu. |
| 12. Citações conferidas | Começa vazio e vai sendo preenchido na pesquisa. É desta lista, e só dela, que a minuta pode tirar citação. |

## A ficha (copiar para a pasta do caso)

```
FICHA DE BRIEFING DE PEÇA
Código do caso: [CÓDIGO INTERNO, SEM O NOME DO CLIENTE] · Versão da ficha: [1] · Data: [DATA]
Preenchida por: [NOME] · Conferida por: [NOME]

1. IDENTIFICAÇÃO
Tipo de peça: [INICIAL / CONTESTAÇÃO / RECURSO / MANIFESTAÇÃO / CUMPRIMENTO DE SENTENÇA]
Área: [ÁREA] · Lado do cliente: [AUTOR / RÉU / RECORRENTE / RECORRIDO]
Juízo ou instância: [CONFERIR] no sistema do tribunal
Modelo do banco: [CÓDIGO DO MODELO E VERSÃO]

2. OBJETIVO DA PEÇA (uma frase)
[O que esta peça precisa conseguir]

3. FATOS EM ORDEM (um por linha, sempre com a fonte)
[DATA] · [FATO] · Fonte: [DOC N, p. X] ou [SÓ RELATO]

4. DOCUMENTOS
DOC 1 · [NOME DO ARQUIVO] · prova: [O QUE ESTE DOCUMENTO PROVA]
DOC 2 · ...
Faltam: [LISTA] · Pedido ao cliente em: [DATA]

5. O QUE A OUTRA PARTE DISSE (contestação, recurso, manifestação)
[Resumo pedido a pedido ou fundamento a fundamento, com a página]

6. TESE ESCOLHIDA (preenchida pelo advogado)
Tese principal: [A DEFINIR]
Tese subsidiária: [A DEFINIR]
Teses descartadas e por quê: [A DEFINIR]
Decidido por: [NOME] em [DATA]

7. PEDIDOS DECIDIDOS
[Pedido] · fato que sustenta: [ ] · valor, se houver: [ ] · fonte do valor: [ ]
Pedido de urgência: [SIM / NÃO] · motivo: [ ]

8. VALORES
Valor da causa: [VALOR] · Memória de cálculo: [ARQUIVO] · Conferido por: [NOME]

9. PRAZOS
Prazo fatal: [DATA LANÇADA E CONFERIDA PELA CONTROLADORIA]
Prazo interno: [DATA]
Minuta pronta até: [DATA] · Revisão final até: [DATA]

10. O QUE NÃO PODE FALTAR
[Pedido, documento, argumento ou detalhe que este caso exige]

11. O QUE NÃO PODE APARECER
[Dado sensível desnecessário, fato que o cliente não autorizou expor, informação de terceiros]

12. CITAÇÕES CONFERIDAS
[Referência] · sustenta: [ ] · fonte oficial aberta em: [DATA] · por: [NOME]

Lembrete: na conversa com a IA, só códigos ([CLIENTE], [PARTE CONTRÁRIA], [EMPRESA], [FILHO 1]). A correspondência entre código e pessoa fica na pasta do caso, fora da IA.
```

## Ajustes deste escritório

- Tipos de peça que o escritório usa no campo 1: [A DEFINIR]
- Áreas: [A DEFINIR]
- Campo extra por área (por exemplo, Previdenciário: o que o INSS analisou e o que ficou de fora; Trabalhista: a matriz de prova como campo 3; Família: o campo 11 protege a criança): [A DEFINIR]

## Mudanças
- 1.0 · AAAA-MM-DD · primeira versão, criada na organizar-producao-de-pecas · aprovado por [FUNÇÃO]
