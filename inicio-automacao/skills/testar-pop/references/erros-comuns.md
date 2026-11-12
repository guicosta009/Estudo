# Erros comuns de POP com IA: como está, como fica e quem pega

Os erros que mais aparecem quando o POP é testado, mostrados no próprio texto do POP. Use ao propor correções no checklist (passo 2) e ao explicar ao advogado por que um teste reprovou um trecho. Os textos "depois" são exemplos: adapte ao código e à base do escritório, e o que não estiver decidido fica `[A DEFINIR]`.

## 1. Passo vago

O executor lê, entende o tema e não sabe o que fazer.

- **Antes:** `3. [A] Revisar a petição.`
- **Depois:** `3. [A] Conferir a minuta gerada pela IA contra o checklist de petição inicial: dados do cliente, datas, pedidos e documentos citados que existem na pasta. Executa: advogada responsável. Pronto quando: todos os itens do checklist estão marcados e as divergências corrigidas.`
- **Quem pega:** o teste de mesa. A primeira pergunta do executor é "revisar o quê?".

## 2. IA sem contexto

A saída sai genérica, correta no geral e fora do jeito do escritório.

- **Antes:** `2. [A] Gerar a minuta com IA.`
- **Depois:** `2. [A] Gerar a minuta no Projeto "Peças Previdenciário" (conta profissional), a partir do modelo "Inicial aposentadoria por idade v3", com o resumo anonimizado do caso e a lista de documentos conferida no passo 1. A IA não acrescenta jurisprudência: trecho de tese sai só do banco de teses do escritório.`
- **Quem pega:** o teste com a IA, no critério "padrão do escritório". E a ficha mostra que foi preciso explicar mais do que o POP dizia.

## 3. Sem critério de pronto

Ninguém sabe quando o passo terminou, e o seguinte começa com pendência.

- **Antes:** `5. [S] Classificar as mensagens do WhatsApp.`
- **Depois:** `5. [S] Classificar cada mensagem nova em uma das categorias da tabela do código do escritório (andamento, documento, agendamento, urgente). Pronto quando: toda mensagem tem categoria e as urgentes foram avisadas à advogada responsável no prazo do código do escritório.`
- **Quem pega:** o piloto, pelo retrabalho e pelas mensagens que ficam sem destino.

## 4. Revisão humana que vira carimbo

O passo é A no papel e S na prática.

- **Antes:** `Nunca sai sem revisão humana: tudo.`
- **Depois:**
  ```
  Nunca sai sem revisão humana:
  1. Mensagem com notícia de decisão: a advogada confere o resultado no sistema do tribunal e o tom.
  2. Qualquer data de prazo ou audiência: a controladoria confere contra o sistema do tribunal.
  3. Valor ao cliente: a advogada refaz a conta.
  ```
- **Quem pega:** o piloto, pelo peso da revisão perto de zero, e o erro plantado (um caso fictício com um defeito discreto, colocado na fila só para ver se a revisão encontra). "Revisar tudo" na prática vira revisar nada.

## 5. Exceção esquecida

O caminho feliz funciona e toda exceção cai na mesa do titular, como antes.

- **Antes:** `Exceções: casos especiais, falar com a Dra.`
- **Depois:**
  ```
  Exceções:
  - Cliente pergunta quanto vai receber: a IA não estima valor; a resposta informa que a advogada retorna no prazo do código do escritório e o caso vai para a fila H.
  - Documento ilegível: a IA marca como pendente e a assistente pede nova foto com o modelo "Documento ilegível".
  - Decisão desfavorável: nenhuma mensagem automática; a advogada liga para o cliente.
  ```
- **Quem pega:** o caso difícil do teste com a IA. Se o teste foi só com caso fácil, a exceção aparece no piloto, com cliente de verdade.

## 6. Dado de cliente sem anonimizar

Documento sob sigilo indo para onde não devia, sem necessidade.

- **Antes:** `1. [S] Colar a conversa do WhatsApp na IA e pedir um resumo.`
- **Depois:** `1. [A] Copiar a conversa para o Projeto do escritório (conta profissional), sem CPF, número de benefício, endereço e dado de saúde que não seja necessário para o resumo, seguindo a lista de anonimização do código do escritório. Executa e confere antes de enviar: assistente.`
- **Quem pega:** o item 10 do checklist e a revisão do titular. No teste de mesa, também aparece quando o executor pergunta "em qual IA eu colo isso?".

## 7. Testar só com o caso fácil

O POP passa no teste e quebra na primeira semana.

- **Antes:** `Testado com 1 caso. Funcionou.`
- **Depois:** `Testado com 3 casos (fácil, comum, difícil), fichas anexas. Passo 4 falhou no difícil: exceção criada para caso com documento faltando, que sobe para A.`
- **Quem pega:** a revisão por par, que pede para ver as fichas.
