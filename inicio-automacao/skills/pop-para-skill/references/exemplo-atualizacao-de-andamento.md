# Exemplo completo: atualização de andamento processual

Exemplo de ponta a ponta da `pop-para-skill`, gerado a partir do POP de referência "Atualização de andamento processual" (setor Relacionamento com o cliente). Se a biblioteca da `escrever-pop` estiver instalada, a versão de referência do POP fica em `../../escrever-pop/references/biblioteca/setor-07-relacionamento-cliente.md`. Escritório, números, horários e versões são **exemplo**.

## 1. De onde a skill saiu

**Escritório (exemplo):** previdenciário, 5 pessoas, trilha equipe, conta de equipe com tratamento de dados conferido. Setor-alvo: Relacionamento com o cliente.

**POP:** `escritorio/03-pops/relacionamento-com-o-cliente/pop-rel-01-atualizacao-de-andamento.md`, versão 1.2.
- Objetivo: manter o cliente informado sem que ele precise cobrar pelo WhatsApp.
- Gatilho: movimentação relevante (decisão, perícia, audiência, sentença), pergunta do cliente ou fim do mês (resumo mensal).
- Responsáveis: assistente de relacionamento executa; advogado responsável valida mensagens sobre decisões e assume conversas delicadas.
- Entradas: movimentações do dia (vindas da controladoria), ficha do cliente com canal preferido, critérios de relevância por área, modelos por categoria, FAQ.
- Prazo (exemplo): até 24 horas depois da movimentação relevante; resumo mensal até o 5º dia útil.
- Indicador: mensagens "alguma novidade?" por semana; tempo da movimentação ao aviso.

**Ficha da automação** (`escritorio/05-automacoes/atualizacao-de-andamento/ficha.md`, resumo):

| Passo | Sigla | Nível-meta | Instrução |
|---|---|---|---|
| 1 Ler as movimentações do dia e entregar a lista | S | 3 | `passo-01-ler-movimentacoes.md` v1.0 |
| 2 Classificar em rotina ou relevante pelos critérios escritos | S | 3 | `passo-02-classificar-movimentacoes.md` v1.0 |
| 3 Registrar a rotina no histórico | S | 3 | `passo-03-registrar-rotina.md` v1.0 |
| 4 Escrever a mensagem do relevante | A | 3 | `passo-04-escrever-mensagem.md` v1.1 |
| 5 Revisar decisão de mérito ou notícia desfavorável | A | 3 | `passo-05-resumo-para-advogado.md` v1.0 |
| 6 Ligar quando a notícia é muito ruim | H | sem nível | |
| 7 Enviar pelo canal preferido e registrar, após aprovação | S | 3 | `passo-07-lista-de-envio.md` v1.0 |
| 8 Responder a dúvida do cliente | A | 3 | `passo-08-responder-duvida.md` v1.0 |
| 9 Assumir a conversa que pede advogado | H | sem nível | |
| 10 Montar o resumo mensal | A | 3 | `passo-10-resumo-mensal.md` v1.0 |
| 11 Registrar todo contato no histórico | S | 3 | `passo-11-registrar-contato.md` v1.0 |

Prontidão: 10 de 11 depois da rodada à mão (faltava só o fluxograma atualizado). Casos de teste: 5, todos acertando, e o caso de notícia desfavorável parou e indicou ligação. Responsável pela automação: assistente de relacionamento. Ponto fixo de revisão das decisões: advogado responsável.

**Nome e gatilhos.** A equipe pede esse trabalho com frases como "vê o andamento de hoje", "tem movimentação nova?", "responde esse cliente que perguntou do processo", "monta os resumos do mês". O que parece e não é: contato de quem ainda não é cliente (é do Atendimento) e prazo processual (é da controladoria).

## 2. A skill gerada (nível 3)

Caminho: `escritorio/05-automacoes/atualizacao-de-andamento/skill/atualizacao-de-andamento/SKILL.md`

~~~markdown
---
name: atualizacao-de-andamento
description: >
  Conduz o POP "Atualização de andamento processual" do escritório: lê as movimentações do
  dia, separa rotina de relevante pelos critérios escritos, rascunha as mensagens aos
  clientes no tom do escritório, sugere respostas a dúvidas e monta o resumo mensal. Para
  em cada passo de revisão humana e não executa os passos que são do advogado. Use quando
  alguém da equipe disser "vê o andamento de hoje", "tem movimentação nova?", "responde esse
  cliente que perguntou do processo", "monta os resumos do mês". Não use para contato de
  quem ainda não é cliente (é do Atendimento) nem para calcular ou lançar prazo (é da
  controladoria).
---

# Atualização de andamento processual

Versão da skill: 1.0 · POP: pop-rel-01-atualizacao-de-andamento.md, versão 1.2 · Instruções: passo 4 na 1.1, demais na 1.0 · Nível: 3 · Gerada em: AAAA-MM-DD · Responsável: assistente de relacionamento · Modo: pasta · Conta: equipe

> Mantém o cliente informado sem que ele precise cobrar. A skill prepara e organiza. Quem revisa as mensagens, decide sobre notícia ruim e conversa com o cliente nos momentos difíceis é uma pessoa do escritório.

## 1. Antes de começar

1. Mostre a linha de versão acima.
2. Leia `escritorio/CLAUDE.md`, o código do escritório e a regra de uso de IA. Use os documentos da seção 4 a partir de `escritorio/04-base/`. Se um deles não for encontrado, diga qual é e pare.
3. Pergunte uma vez por sessão: "Estamos na conta de equipe do escritório?" Se não, siga só com dado fictício.
4. Pergunte qual é o trabalho de agora:
   - **A. Movimentações do dia** (passos 1 a 7 e 11)
   - **B. Dúvida de um cliente** (passos 8, 9 e 11)
   - **C. Resumo mensal** (passos 10 e 11)
5. Confira a entrada (seção 3).

## 2. Linha vermelha e travas

Em nenhum passo esta skill escolhe tese ou estratégia, dá notícia ruim ao cliente, assina, aconselha cliente em situação de vulnerabilidade ou envia mensagem com conteúdo jurídico sem revisão humana. Notícia muito ruim é ligação do advogado, nunca mensagem. Também nunca inventa movimentação, data, prazo ou dado, nem promete resultado ou prazo de decisão, nem dá orientação jurídica nova por mensagem. Processo marcado como restrito (criança, violência, saúde grave): pare e passe ao advogado.

## 3. Anonimização

Se a entrada trouxer nome, CPF, NIT, número de processo ou de benefício, endereço ou contato, avise, não repita e mostre a versão com `[CLIENTE]`, `[DOC]`, `[PROCESSO]` (ou o código interno), `[BENEFÍCIO]`, `[ENDEREÇO]`, `[CONTATO]` antes de seguir. Dado de saúde (perícia, CID) fica só no trecho que a mensagem exige. Laudo completo não entra. As mensagens saem com `[CLIENTE]`; quem envia troca pelo nome no canal oficial.

## 4. Base que esta skill consulta

| Documento | Versão | Usado no passo | Caminho |
|---|---|---|---|
| Critérios de relevância de movimentação · Previdenciário | 1.1 | 2, 5 | `escritorio/04-base/relacionamento-com-o-cliente/criterios-relevancia-movimentacao-previdenciario.md` |
| Modelos de mensagem por categoria | 1.0 | 4, 5, 10 | `escritorio/04-base/relacionamento-com-o-cliente/modelos-mensagem-por-categoria.md` |
| FAQ de clientes | 1.0 | 8 | `escritorio/04-base/relacionamento-com-o-cliente/faq-clientes.md` |

## 5. Fluxo

### Como cada passo funciona aqui
- **[S]** A IA faz, mostra e segue. Conferência por amostra: assistente de relacionamento.
- **[A]** A IA prepara um rascunho, escreve "RASCUNHO PARA REVISÃO", diz quem revisa e o que conferir, e para. Só segue com "aprovado" ou com os ajustes pedidos.
- **[H]** A IA não executa. Diz de quem é o passo, entrega o material de apoio e espera.
- Comandos: **aprovado** · **ajustar: ...** · **parar**.

### Trabalho A. Movimentações do dia

#### Passo 1 · [S] · Ler as movimentações do dia e entregar a lista
- Recebe: a lista de movimentações do dia vinda da controladoria, colada como texto ou em arquivo, com o código interno de cada processo.
- Faz: uma linha por movimentação, sem duplicidade.
- Entrega: tabela `Processo (código) | Data | Movimentação (resumo de uma linha)`.
- Pare e chame a assistente quando: a lista vier vazia num dia útil (a captura pode ter falhado) ou aparecer movimentação de processo sem código (avisar a controladoria).

#### Passo 2 · [S] · Classificar em rotina ou relevante pelos critérios escritos
- Faz: classifica cada linha pelo documento "Critérios de relevância de movimentação · Previdenciário". Na dúvida, **relevante**. Marca "exige advogado" nos itens que o documento manda.
- Entrega: a tabela do passo 1 com as colunas `Classificação | Motivo (uma linha) | Exige advogado?`.
- Conferência: a assistente confere todas as marcadas como relevantes.
- Nunca: criar critério que o documento não tem. Movimentação que não se encaixa em nenhum item vira relevante, com o motivo "fora dos critérios", e a skill sugere atualizar o documento.

#### Passo 3 · [S] · Registrar a rotina no histórico
- Faz: junta as movimentações de rotina num bloco por processo, para o resumo mensal.
- Entrega: bloco "Para o histórico", pronto para colar no histórico de cada processo.

#### Passo 4 · [A] · Escrever a mensagem do relevante
- Vale para os relevantes sem "exige advogado". Os outros vão para o passo 5.
- Faz: escolhe a categoria em "Modelos de mensagem por categoria" e rascunha no tom do código, com a estrutura: o que aconteceu, o que significa para o cliente, qual é o próximo passo.
- Entrega, uma por processo:
  ```
  Passo 4 · [código do processo] · [categoria] · RASCUNHO PARA REVISÃO
  Quem revisa: assistente de relacionamento. Confira: data, local, o que o cliente precisa fazer, tom.
  [texto com [CLIENTE]]
  ```
- Pare e chame a assistente quando: a categoria não existir nos modelos.
- Nunca: prometer resultado ou prazo de decisão; dar orientação jurídica nova.

#### Passo 5 · [A] · Preparar a revisão do advogado (decisão de mérito ou notícia desfavorável)
- Vale para os itens com "exige advogado".
- Faz: um resumo interno de até cinco linhas (o que foi decidido, o que muda para o cliente, o que o escritório pode fazer, marcado como sugestão). Se a decisão **não** for desfavorável, também o rascunho da mensagem, como no passo 4.
- Entrega: "RESUMO PARA O ADVOGADO · RASCUNHO PARA REVISÃO. Quem revisa: advogado responsável. Confira: leitura da decisão na íntegra, próximo passo, tom."
- Se a decisão for desfavorável: nenhum rascunho de mensagem ao cliente. Pergunte ao advogado se a notícia é muito ruim; se for, siga para o passo 6.

#### Passo 6 · [H] · Ligar quando a notícia é muito ruim
Este passo é do advogado responsável, por ligação, e não é feito pela IA. Material de apoio: o resumo do passo 5. Nenhuma mensagem é preparada antes da ligação. Me avise quando a ligação estiver feita, para registrar o contato no passo 11.

#### Passo 7 · [S] · Montar a lista de envio e registrar a data
- Faz: junta só as mensagens com "aprovado" e monta a lista de envio.
- Entrega: tabela `Processo (código) | Categoria | Aprovado por | Texto final`.
- No nível 3 não há ponte: **quem envia é a pessoa**, pelo canal preferido da ficha, trocando `[CLIENTE]` pelo nome. Quando ela disser "enviado", a skill registra a data para o passo 11.
- Sem WhatsApp: e-mail ou ligação, conforme a ficha.
- Nunca: incluir na lista mensagem sem "aprovado".

### Trabalho B. Dúvida de um cliente

#### Passo 8 · [A] · Responder a dúvida do cliente
- Recebe: a dúvida (anonimizada) e a última movimentação do processo.
- Faz: procura a pergunta no "FAQ de clientes" e rascunha a resposta com a movimentação real. Sem pergunta parecida no FAQ, rascunha no tom do código e marca "fora do FAQ".
- Entrega: "Passo 8 · RASCUNHO PARA REVISÃO. Quem revisa: assistente de relacionamento. Confira: se a resposta bate com o processo, se não promete prazo, tom." Prazo de resposta (exemplo): até 1 dia útil.
- Pare e vá para o passo 9 quando: a dúvida pedir orientação nova, for reclamação, insatisfação ou pedido de desistência, ou o cliente estiver em situação de vulnerabilidade.

#### Passo 9 · [H] · Assumir a conversa que pede advogado
Este passo é do advogado responsável, por ligação, e não é feito pela IA. Material de apoio: resumo da conversa em três linhas, sem opinião sobre o caso. Me avise quando estiver feito, para registrar o contato.

### Trabalho C. Resumo mensal

#### Passo 10 · [A] · Montar o resumo mensal de cada cliente
- Recebe: o histórico do mês de cada processo (rotina registrada no passo 3 e mensagens enviadas).
- Faz: um resumo por cliente no modelo "resumo mensal", inclusive de processo parado ("este mês não houve movimentação; o próximo passo esperado é ...").
- Antes de começar, pergunte: "Algum cliente desta lista pediu para não receber o resumo?" Quem pediu fica de fora, com registro.
- Entrega: o lote de resumos, cada um marcado "RASCUNHO PARA REVISÃO", e para uma vez, com o lote inteiro. Quem revisa: assistente de relacionamento. O POP prevê conferência por amostra neste passo `[A CONFIRMAR]` com o advogado se a amostra basta, porque o resumo vai ao cliente.
- Prazo (exemplo): até o 5º dia útil do mês.

### Para todos os trabalhos

#### Passo 11 · [S] · Registrar todo contato no histórico
- Faz: uma linha por contato: data, canal, assunto (sem conteúdo jurídico detalhado).
- Entrega: bloco "Para o histórico", pronto para colar.

## 6. Exceções do POP

| Situação | O que a skill faz |
|---|---|
| Cliente sem WhatsApp | Lista de envio indica e-mail ou ligação, conforme a ficha |
| Notícia muito ruim | Para no passo 5 e vai ao passo 6 (ligação do advogado) |
| Cliente pediu para não receber o resumo mensal | Fica fora do lote do passo 10, com registro |
| Processo restrito (criança, violência, saúde grave) | Para e passa ao advogado, sem rascunho |
| Movimentação fora dos critérios | Classifica como relevante e sugere atualizar o documento de critérios |

## 7. Registro de uso

Ao fim de cada trabalho, proponha a linha e grave em `escritorio/05-automacoes/atualizacao-de-andamento/registro-de-uso.md` depois da confirmação:
`AAAA-MM-DD | Andamento do dia, 12 processos | Passos 1 a 7 | S e A | 3 | Projeto do escritório, conta de equipe | Assistente de relacionamento | Ajustou o tom de 2 mensagens | não | 25 min` (exemplo)

## 10. Se algo der errado

Siga `escritorio/05-automacoes/atualizacao-de-andamento/plano-para-erro.md`. Quem pode pausar: assistente de relacionamento ou advogado responsável. O comando **parar** encerra e registra o motivo. Quem avisa um erro nunca é punido por avisar.

## Mudanças

- 1.0 · AAAA-MM-DD · gerada pela pop-para-skill a partir do POP versão 1.2
~~~

(Na skill de nível 3 as seções 8 e 9 do modelo não entram. A numeração foi mantida para que a versão de nível 4 só acrescente.)

## 3. O que muda para o nível 4

Quando a automação cumprir os critérios de subida, a skill ganha as seções abaixo e sobe para a versão 2.0. A linha de versão passa a dizer "Nível: 4".

~~~markdown
## 8. Disparo e fila

- **Gatilho:** todo dia útil às 11h30 (exemplo), depois que a controladoria fecha o controle do dia. Por tarefa agendada, se o ambiente do Claude permitir (conferir na configuração da conta), ou pelo pedido "rodar o andamento do dia".
- **Quando disparada sem ninguém acompanhando:** executa os passos 1, 2 e 3, prepara os rascunhos dos passos 4 e 5 e grava tudo em `escritorio/05-automacoes/atualizacao-de-andamento/fila/AAAA-MM-DD.md`. Para aí. Nada é dado como aprovado e nada sai do escritório.
- **Topo da fila, "Para o advogado, hoje":** os itens com "exige advogado", com o resumo do passo 5 e sem rascunho de mensagem quando a decisão for desfavorável.
- **Fila do dia anterior sem revisão:** não gera fila nova por cima. Avisa a assistente e o advogado.
- **Pontos fixos de revisão:** às 14h (exemplo), a assistente de relacionamento revisa os rascunhos do passo 4; até as 17h (exemplo), o advogado responsável revisa o topo da fila. Só o item com "aprovado por [FUNÇÃO]" vai para a lista de envio do passo 7.
- **Ausência do responsável:** segue o plano para erro. A fila espera, nada sai.

## 9. Pontes

Ponte: entrada das movimentações do dia
Entra: lista de movimentações, uma por linha, com código interno do processo, data e texto da movimentação, vinda do software jurídico ou do relatório da controladoria. Quem coloca: [A DEFINIR] (pelo escritório)
Sai: nada. É só entrada.
A ponte nunca: traz nome ou documento do cliente; traz a íntegra da decisão.

Ponte: saída das mensagens aprovadas
Entra: a lista de envio do passo 7.
Sai: cada mensagem com "aprovado por [FUNÇÃO]", para o canal preferido do cliente (WhatsApp ou e-mail), com o nome trocado no próprio canal. Ferramenta: [A DEFINIR] (pelo escritório)
A ponte nunca: envia mensagem sem a marca de aprovação; envia mensagem de item do topo da fila sem a aprovação do advogado; leva senha ou credencial.
Sem ponte: a assistente copia e envia, e avisa "enviado" para o registro.
~~~

## 4. O que este exemplo mostra

- O passo 7 é S no POP, mas no nível 3, sem ponte, quem aperta "enviar" é a pessoa. A skill prepara a lista e registra. A sigla não muda: o que muda é quem opera o canal.
- O passo 10 traz uma tensão do próprio POP (passo A com conferência por amostra). A skill não resolve sozinha: marca `[A CONFIRMAR]` e para uma vez com o lote.
- Os passos 6 e 9 aparecem na skill para que ninguém pule. Eles só dizem de quem é o passo e entregam o material de apoio.
- O documento de critérios na versão 1.1 veio da rodada à mão (a perícia remarcada não estava na lista). É assim que a base melhora: erro pego na revisão vira item escrito.
