# Ficha de briefing: exemplo preenchido

Consumidor, petição inicial por cobrança após cancelamento. **Caso fictício**, inventado para mostrar o nível de detalhe. Datas e valores são fictícios. A base legal fica marcada para conferir, de propósito. Use para comparar com a primeira ficha do escritório (passo 4 da skill `organizar-producao-de-pecas`).

Repare que os campos 5, 7, 8, 9 e 12 não aparecem: é uma ficha em andamento. O campo 5 não se aplica a inicial. Os campos 7, 8 e 12 vêm depois da tese (pedidos, valores e citações conferidas). O campo 9 recebe as datas que a controladoria lançou e conferiu, e ficou fora do exemplo só para encurtar.

```
FICHA DE BRIEFING DE PEÇA · EXEMPLO FICTÍCIO
Código do caso: CONS-0412 · Versão da ficha: 2 · Conferida por: advogada responsável

1. IDENTIFICAÇÃO
Tipo de peça: petição inicial · Área: Consumidor · Lado do cliente: autor
Juízo: [CONFERIR] no sistema do tribunal · Modelo: CONS_INICIAL_cobranca-indevida, versão 3.0

2. OBJETIVO
Fazer parar a cobrança de um plano já cancelado e pedir de volta o que foi pago depois do cancelamento.

3. FATOS EM ORDEM
03/03/2026 · [CLIENTE] pede o cancelamento pelo aplicativo · Fonte: DOC 2, p. 1 (print com protocolo)
04/03/2026 · [EMPRESA] confirma o cancelamento por e-mail · Fonte: DOC 3, p. 1
10/04, 10/05 e 10/06/2026 · Faturas cobradas depois do cancelamento · Fonte: DOC 4, p. 1 a 3
15/04/2026 · [CLIENTE] liga para o SAC e ouve que o valor "vai ser estornado" · Fonte: [SÓ RELATO], protocolo da ligação no DOC 5

4. DOCUMENTOS
DOC 1 · contrato_adesao.pdf · prova: a contratação e o valor mensal
DOC 2 · print_cancelamento.jpg · prova: o pedido e o protocolo
DOC 3 · email_confirmacao.pdf · prova: a empresa confirmou o cancelamento
DOC 4 · faturas_abr_mai_jun.pdf · prova: as cobranças posteriores
DOC 5 · protocolos_sac.pdf · prova: as tentativas de resolver
Faltam: comprovantes de pagamento das faturas de maio e junho · Pedido ao cliente em: 02/07/2026

6. TESE ESCOLHIDA
Tese principal: cobrança indevida depois de cancelamento comprovado, com devolução do que foi pago [CONFERIR a base legal e a forma da devolução]
Teses descartadas: negativação indevida (não houve negativação, conferido no DOC 6)
Decidido por: advogada responsável em 01/07/2026

10. O QUE NÃO PODE FALTAR
O protocolo do cancelamento e o e-mail de confirmação logo no primeiro parágrafo dos fatos. As faturas, uma a uma, com data e valor.

11. O QUE NÃO PODE APARECER
Número do cartão de crédito que aparece nas faturas. O motivo pessoal do cancelamento, que o cliente contou na consulta.
```

## O que o exemplo ensina

- **Fato com fonte:** cada linha do campo 3 aponta documento e página. A ligação ao SAC é `[SÓ RELATO]`, mesmo com o protocolo no DOC 5: o protocolo prova que houve ligação, não o que foi dito.
- **Tese descartada com motivo:** "negativação indevida" ficou de fora porque o DOC 6 mostra que não houve negativação. Escrito assim, a IA não "lembra" dessa tese na minuta e o estagiário não acha que o advogado esqueceu.
- **Base legal marcada:** a tese principal leva `[CONFERIR]` na base legal e na forma da devolução. Nada disso entra na peça antes de alguém abrir a fonte oficial.
- **O que não pode aparecer:** o número do cartão estava nas faturas, e o motivo pessoal foi contado em confiança. A IA tende a usar tudo o que recebe, então a ficha diz o que fica de fora.
- **Código do caso sem o nome do cliente:** `CONS-0412`. A tabela que liga o código ao cliente fica na pasta do caso, fora da IA.
