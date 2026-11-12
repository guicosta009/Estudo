# Prompts do canal

Cinco prompts para usar dentro do Projeto do escritório no Claude, onde o código do escritório já está. Os prompts 1 e 4 são a base das entrevistas dos passos 5 e 6 desta skill: aqui ficam para o advogado repetir sozinho quando entrar uma área nova. Os prompts 2, 3 e 5 são de uso diário, enquanto a IA entra no WhatsApp pela porta da frente (alguém cola a mensagem anonimizada e decide o que fazer com a resposta). Eles são o rascunho das instruções de passo que a `desenhar-automacao` vai escrever depois.

Antes de colar: troque o que está entre colchetes, anonimize toda mensagem de cliente (tabela em `regras-de-canal.md`, seção 6) e use conta profissional. Prompt validado vai para o registro de prompts do escritório (`escritorio/01-cultura/mudanca/registro-de-prompts.md`), com quem validou e quando.

## 1. Escrever a biblioteca de mensagens no tom do escritório

```
Quero montar a biblioteca de mensagens de WhatsApp do meu escritório de advocacia, no nosso tom de voz.

Use como régua o código do escritório que está neste projeto, principalmente as partes "Como atendemos", "Tom de voz" e "O que nunca fazemos". Se alguma dessas partes não estiver no projeto, me pergunte antes de começar.

Meu escritório:
- Áreas: [ÁREAS]
- Perfil do cliente: [EX.: SEGURADOS DO INSS, MUITOS IDOSOS; FAMÍLIAS EM DIVÓRCIO]
- Como tratamos o cliente: [VOCÊ / SENHOR E SENHORA / PELO NOME]
- Três mensagens reais que mandamos e de que gostamos (anonimizadas): [COLE AQUI]

Modelos de partida:
[COLE OS MODELOS DA BIBLIOTECA QUE VOCÊ QUER ADAPTAR]

Como quero que você trabalhe:
1. Reescreva cada modelo no nosso tom, mantendo os campos entre colchetes.
2. Mensagem curta: o cliente lê no celular. Uma ideia por parágrafo.
3. Sem juridiquês. Termo técnico que ficar, explique na primeira vez.
4. Nenhuma mensagem promete resultado, prazo de decisão ou valor.
5. Nenhuma mensagem dá orientação jurídica a quem ainda não é cliente.
6. Mensagem automática diz que é automática.
7. Depois dos modelos, sugira outras mensagens que a minha rotina provavelmente pede e que não estão na lista, e me pergunte se quero que você escreva.

Não invente regra, prazo ou número de lei. Onde faltar informação, escreva [A DEFINIR].
```

## 2. Classificar mensagens recebidas

```
Você vai fazer a triagem das mensagens de WhatsApp que meu escritório de advocacia recebeu. As mensagens estão anonimizadas: cada remetente tem um código.

Use o código do escritório e as regras de canal deste projeto para saber o que conta como urgência e quem responde cada tipo de assunto.

Para cada mensagem, me devolva uma tabela com:
- Código do remetente
- Contato novo ou cliente ativo (pela lista abaixo)
- Tipo: andamento, documento, agenda, financeiro, orientação jurídica nova, reclamação ou outro
- Urgência: alta, normal ou baixa, com o motivo em uma linha
- Sinal de alerta, se houver: aflição, insatisfação, vontade de desistir, prazo correndo, violência, saúde
- Fluxo: 1 (primeiro contato), 2 (andamento), 3 (documento), 4 (agenda) ou "advogado assume"
- Quem responde, pela regra do código
- Prazo de resposta, pela regra do código

Depois da tabela, liste em ordem o que precisa ser respondido primeiro.

Regras:
- Na dúvida entre normal e alta, marque alta e explique.
- Qualquer sinal de alerta leva a mensagem para "advogado assume" ou para a atendente, nunca para resposta automática.
- Não escreva resposta para nenhuma mensagem. Só classifique.

Clientes ativos (códigos): [LISTA DE CÓDIGOS]
Palavras de alerta da minha área: [LISTA]

Mensagens:
[COLE AS MENSAGENS ANONIMIZADAS, UMA POR LINHA, COM CÓDIGO, DATA E HORA]
```

## 3. Rascunhar a resposta de andamento a partir da movimentação

Serve ao fluxo 2 e ao aviso proativo de movimentação.

```
Preciso responder um cliente do meu escritório sobre o andamento do processo dele, por WhatsApp.

Dados (anonimizados):
- Área e tipo de ação: [EX.: PREVIDENCIÁRIO, CONCESSÃO DE BENEFÍCIO POR INCAPACIDADE]
- Etapa atual do processo: [ETAPA]
- Movimentações recentes, copiadas do sistema: [COLE AQUI, COM DATAS]
- O que já dissemos ao cliente na última conversa: [RESUMO OU "nada"]
- A pergunta do cliente, do jeito que ele escreveu: [COLE AQUI]

Faça assim:
1. Primeiro, me explique em duas ou três linhas, só para mim, o que as movimentações significam e se alguma delas exige atenção do advogado.
2. Diga se esta resposta pode sair pela assistente ou se precisa de revisão do advogado (decisão, valor, estimativa de prazo ou chance de êxito sempre precisam).
3. Escreva a mensagem para o cliente, no tom do código do escritório deste projeto, seguindo o modelo: o que aconteceu, o que isso quer dizer, o que vem agora e se ele precisa fazer algo.
4. Se nada mudou, explique o que está sendo esperado e de quem depende, sem prometer data.
5. Se a pergunta do cliente mostrar ansiedade, insatisfação ou vontade de desistir, não escreva a mensagem: recomende uma ligação e diga por quê.

Não invente movimentação, data, prazo ou valor. Se faltar informação, me pergunte.
```

## 4. Montar a régua de atualização proativa

```
Quero montar a régua de atualização proativa do meu escritório de advocacia: o cliente recebe notícia do processo antes de precisar perguntar.

Meu escritório:
- Áreas e tipos de ação mais comuns: [LISTA]
- Número aproximado de processos ativos: [NÚMERO]
- Quem vai executar e quanto tempo por semana tem para isso: [PESSOA E HORAS]
- Ferramentas: [SOFTWARE JURÍDICO, PLANILHA, CRM, FERRAMENTA DE IA E TIPO DE CONTA]
- Como fazemos hoje: [EX.: SÓ RESPONDEMOS QUANDO O CLIENTE PERGUNTA]

Use o código do escritório deste projeto como régua de tom e de prazos.

Me entregue:
1. A cadência: o que o cliente recebe e quando (contratação, movimentação relevante, resumo mensal, compromissos, encerramento). Prazo que eu não informei fica [A DEFINIR].
2. Para cada área, uma tabela de movimentações típicas com três colunas: só registra para o resumo mensal, avisa por mensagem, ou o advogado liga antes. Marque S, A ou H em cada linha.
3. Um modelo de mensagem para cada tipo de aviso, curto e em linguagem simples.
4. A lista do que nunca vai por mensagem no meu escritório.
5. Uma estimativa de quanto tempo por semana a régua consome com a IA rascunhando e uma pessoa aprovando, mostrando a conta. Marque como estimativa.

Antes de começar, me faça até 5 perguntas, uma por vez. Não invente regra, número de lei ou de provimento.
```

## 5. Resumir o histórico antes de ligar para o cliente

Para a conversa difícil ou quando o caso troca de mão. A ligação continua sendo do advogado.

```
Vou ligar para um cliente do meu escritório e preciso chegar na ligação sabendo de tudo que já foi conversado. A conversa abaixo está anonimizada.

Motivo da ligação: [EX.: SENTENÇA DESFAVORÁVEL, RECLAMAÇÃO SOBRE DEMORA, PROPOSTA DE ACORDO]

Histórico da conversa no WhatsApp e anotações do caso:
[COLE AQUI]

Me entregue, em uma página:
1. O que o cliente já sabe e o que ainda não sabe.
2. Tudo o que o escritório prometeu ou combinou com ele, com data, e se foi cumprido.
3. Pendências dos dois lados.
4. Sinais do estado emocional e das preocupações dele, com o trecho que mostra isso.
5. Perguntas que ele provavelmente vai fazer.
6. Pontos de atenção para a ligação: o que evitar dizer e o que deixar claro.

Não escreva o roteiro da notícia nem dê opinião sobre o mérito do caso. Se algo no histórico estiver ambíguo, aponte em vez de interpretar.
```

A pessoa confere o resumo com a conversa original antes de usar.
