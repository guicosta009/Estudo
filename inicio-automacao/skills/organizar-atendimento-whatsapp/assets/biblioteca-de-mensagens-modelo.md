# Biblioteca de mensagens do WhatsApp
Versão: 0.1 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Relacionamento com o cliente (e Atendimento e triagem) · Área: todas · Usado por: POP-ATD-[NN] primeiro contato (passos 2 e 6), POP-REL-[NN] dúvida de andamento (passos 2 e 4), POP-REL-[NN] documentos (passos 2, 6 e 8), POP-REL-[NN] agenda e lembretes (passos 3, 4 e 8), POP de atualização de andamento (aviso e resumo mensal) · Acesso: geral
Aprovado por: [FUNÇÃO OU NOME] · Próxima revisão: revisão trimestral, ou antes, se o mesmo ajuste aparecer duas vezes na revisão

> Nove mensagens que cobrem a maior parte do WhatsApp de um escritório, mais as que a rotina costuma pedir. A IA parte daqui para rascunhar. Modelo aprovado é o que permite à IA executar um passo como S; por isso a biblioteca entra na base de conhecimento, dentro do Projeto no Claude, e qualquer mudança passa por quem aprovou. Os textos abaixo estão num tom de exemplo ("você", sem juridiquês, termo técnico explicado) e precisam ser reescritos no tom do código do escritório antes de valer.

## Regras para todas as mensagens

- Tom, tratamento e frases que usamos ou nunca usamos: seguir o código do escritório.
- Mensagem curta: o cliente lê no celular. Uma ideia por parágrafo.
- Estrutura das mensagens de andamento: **o que aconteceu, o que significa para o cliente, qual é o próximo passo e se ele precisa fazer algo.**
- Nenhuma mensagem promete resultado, prazo de decisão ou valor.
- Nenhuma mensagem dá orientação jurídica a quem ainda não é cliente.
- Mensagem automática diz que é automática e quando uma pessoa responde. Nunca usa nome de advogado como se fosse ele digitando.
- A IA nunca se apresenta como advogado.
- **Mensagem com conteúdo do processo nunca sai sem alguém ler.**
- **Notícia muito ruim nunca vai por mensagem.** O advogado liga; a mensagem vem depois, para registrar (modelo 8).
- Tudo sai pelo número oficial do escritório.
- Dado sensível no mínimo: dado de saúde só no trecho que a mensagem exige; nada de CPF, número de benefício ou senha em mensagem.
- Campos variáveis entre colchetes. Quem preenche é a pessoa (ou a IA, a partir da ficha), e quem envia confere os campos.

## Os nove modelos

### Modelo 1 · Boas-vindas ao cliente
- **Quando usar:** no dia da contratação. Combina as regras do canal e a régua de atualização.
- **POP e passo:** régua de atualização (contratação).
- **Quem revisa antes de enviar:** [FUNÇÃO], conferindo os campos preenchidos.
- **Sigla:** S depois de aprovado (não traz conteúdo do processo).
- **Texto-modelo:**
  ```
  Oi, [NOME DO CLIENTE]! Aqui é [SEU NOME], do [NOME DO ESCRITÓRIO]. Seja bem-vindo(a).

  A partir de agora este é o número oficial do escritório para falar sobre o seu caso. Algumas combinações para você saber como a gente trabalha:

  * Atendemos de [DIAS], das [HORÁRIO]. Mensagem fora desse horário é respondida no próximo dia útil.
  * Todo mês, até o dia [DIA], você recebe um resumo do seu processo, mesmo quando não houver novidade.
  * Quando acontecer algo importante, a gente te avisa antes de você precisar perguntar.
  * Assunto que pede conversa, a gente liga.

  Quem cuida do seu caso é [NOME DO ADVOGADO OU ADVOGADA]. Qualquer dúvida, é só escrever aqui.
  ```
- **Nunca usar quando:** o contato ainda não é cliente (contratação não assinada).

### Modelo 2 · Pedido de documento
- **Quando usar:** fluxo de documentos. Um bloco por documento: o que é, onde conseguir, como mandar.
- **POP e passo:** POP-REL-[NN] documentos, passo 2.
- **Quem revisa antes de enviar:** assistente (nome de cada documento, onde conseguir, data).
- **Sigla:** A.
- **Texto-modelo:**
  ```
  Oi, [NOME], tudo bem? Para dar o próximo passo no seu caso, preciso destes documentos:

  1. [NOME DO DOCUMENTO]: [O QUE É, EM UMA FRASE]. Você consegue em [ONDE CONSEGUIR].
  2. [NOME DO DOCUMENTO]: [O QUE É]. Você consegue em [ONDE CONSEGUIR].

  Como mandar: pode ser por aqui mesmo. Se for foto, tire com boa luz, com a folha inteira aparecendo e sem dobra. Se tiver em PDF, melhor ainda.

  Consegue me enviar até [DATA]? Se tiver dificuldade com algum, me fala que a gente resolve junto.
  ```
- **Nunca usar quando:** o documento é senha, credencial ou acesso a sistema (gov.br, Meu INSS, banco); laudo ou documento de criança sem a orientação de mandar só pelo número oficial.

### Modelo 3 · Atualização de andamento
- **Quando usar:** movimentação relevante, pelo critério de relevância da área. A IA rascunha a partir da movimentação.
- **POP e passo:** POP de atualização de andamento (aviso) e POP-REL-[NN] dúvida de andamento, passo 4.
- **Quem revisa antes de enviar:** assistente; advogado quando houver decisão, valor ou estimativa de prazo.
- **Sigla:** A.
- **Texto-modelo:**
  ```
  Oi, [NOME], tudo bem? Tenho uma novidade no seu processo.

  O que aconteceu: [FATO EM UMA FRASE, SEM TERMO TÉCNICO].
  O que isso quer dizer: [SIGNIFICADO PRÁTICO PARA O CLIENTE].
  O que vem agora: [PRÓXIMO PASSO E, SE HOUVER, DATA].

  [ESCOLHA UMA: "Você não precisa fazer nada agora." OU "Preciso de você para: ..."]

  Se quiser que eu explique melhor por ligação, é só me dizer um horário.
  ```
- **Nunca usar quando:** a notícia é desfavorável relevante (ligação primeiro, modelo 8); decisão favorável ainda pode mudar (explicar o que ainda pode acontecer, sem comemorar antes da hora).

### Modelo 4 · Resposta a "alguma novidade?" quando nada mudou
- **Quando usar:** fluxo de dúvida de andamento. Explica a espera em vez de dizer só "sem novidades".
- **POP e passo:** POP-REL-[NN] dúvida de andamento, passo 4.
- **Quem revisa antes de enviar:** assistente (etapa, data da última movimentação, de quem depende).
- **Sigla:** A.
- **Texto-modelo:**
  ```
  Oi, [NOME]! Acabei de olhar o seu processo.

  Hoje ele está nesta etapa: [ETAPA EM LINGUAGEM SIMPLES, EX.: "aguardando o juiz marcar a perícia"]. A última movimentação foi em [DATA] e foi [O QUE FOI].

  O que está sendo esperado agora é [O QUE FALTA ACONTECER]. Esse tempo depende de [DE QUEM DEPENDE: vara, INSS, outra parte], então não consigo te dar uma data exata, e prefiro não chutar.

  Por enquanto você não precisa fazer nada. Assim que andar, eu te aviso. E no dia [DIA] você recebe o resumo do mês, como combinado.
  ```
- **Nunca usar quando:** a pergunta carrega reclamação, ansiedade forte ou vontade de desistir (ligação).

### Modelo 5 · Aviso de audiência ou perícia
- **Quando usar:** fluxo de agenda, assim que o ato é designado. Faça uma variação por tipo de compromisso e por área (perícia médica, audiência presencial, audiência por vídeo).
- **POP e passo:** POP-REL-[NN] agenda e lembretes, passo 3.
- **Quem revisa antes de enviar:** advogado responsável, sempre.
- **Sigla:** A.
- **Texto-modelo:**
  ```
  Oi, [NOME]! Foi marcada a [AUDIÊNCIA / PERÍCIA] do seu processo.

  Quando: [DIA DA SEMANA, DATA], às [HORA]. Chegue com [ANTECEDÊNCIA] de antecedência.
  Onde: [ENDEREÇO OU "por vídeo, no link que vou te mandar na véspera"].
  O que levar: [DOCUMENTO COM FOTO, EXAMES, LAUDOS, OUTROS].
  Como funciona: [EXPLICAÇÃO CURTA DO QUE VAI ACONTECER, APROVADA PELO ADVOGADO].

  [NOME DO ADVOGADO OU ADVOGADA] vai estar com você. Pode me confirmar que recebeu e que consegue ir?

  Vou te lembrar de novo [QUANDO].
  ```
- **Nunca usar quando:** a orientação diria ao cliente o que falar ao perito (a orientação explica como funciona e o que levar, nada além); orientação de testemunha (conversa do advogado).

### Modelo 6 · Fora do horário
- **Quando usar:** resposta automática, se a ferramenta tiver, ou enviada pela IA.
- **POP e passo:** POP-ATD-[NN] primeiro contato, passo 2; vale também para cliente ativo.
- **Quem revisa antes de enviar:** ninguém a cada envio; o texto é aprovado uma vez e conferido por amostra.
- **Sigla:** S.
- **Texto-modelo:**
  ```
  Oi! Esta é uma mensagem automática do [NOME DO ESCRITÓRIO].

  Nosso atendimento é de [DIAS], das [HORÁRIO]. Sua mensagem ficou registrada e uma pessoa da equipe te responde [QUANDO, EX.: "amanhã a partir das 9h"].

  Se for urgente, como [EXEMPLOS DE URGÊNCIA DO SEU CÓDIGO], [O QUE FAZER: "escreva URGENTE no começo da mensagem" OU "ligue para ..."].
  ```
- **Nunca usar quando:** a mensagem que chegou tem palavra de alerta e o caminho de urgência do código manda acionar alguém (a automática pode sair, mas a pessoa é acionada do mesmo jeito).

### Modelo 7 · Cobrança gentil
- **Quando usar:** documento ou retorno pendente. Lembra sem cobrar culpa.
- **POP e passo:** POP-REL-[NN] documentos, passo 6.
- **Quem revisa antes de enviar:** ninguém a cada envio quando não há prazo correndo; com prazo correndo, assistente e advogado.
- **Sigla:** S (A quando há prazo correndo).
- **Texto-modelo:**
  ```
  Oi, [NOME], tudo bem? Passando para lembrar do [DOCUMENTO OU RETORNO] que combinamos no dia [DATA].

  Ele é importante porque [POR QUE O CASO PRECISA, EM UMA FRASE].

  Se estiver difícil de conseguir, me conta o que está acontecendo que eu te ajudo a achar outro caminho. Se já mandou e eu não vi, me desculpa e me avisa por aqui.
  ```
- **Nunca usar quando:** o cliente já disse que o documento não existe (conversa com o advogado); cliente idoso ou com pouca familiaridade com o celular que não respondeu à primeira (ligação).

### Modelo 8 · Convite para ligação e registro depois dela
- **Quando usar:** notícia que pede conversa. A notícia em si nunca vai na primeira mensagem.
- **POP e passo:** régua de atualização (notícia difícil) e qualquer POP em que o advogado assume.
- **Quem revisa antes de enviar:** o próprio advogado escreve ou aprova as duas partes.
- **Sigla:** a ligação é H; as duas mensagens são A.
- **Texto-modelo:**
  ```
  ANTES DA LIGAÇÃO
  Oi, [NOME], tudo bem? Aqui é [NOME DO ADVOGADO]. Teve um andamento no seu processo e eu prefiro conversar com você por telefone para explicar com calma. Você consegue falar hoje [HORÁRIO] ou amanhã [HORÁRIO]?

  DEPOIS DA LIGAÇÃO
  [NOME], obrigado pela conversa. Deixo aqui por escrito o que combinamos, para você poder reler:
  * O que aconteceu: [RESUMO]
  * O que vamos fazer: [PRÓXIMO PASSO]
  * O que preciso de você: [AÇÃO E PRAZO, OU "nada por enquanto"]
  Qualquer dúvida que surgir depois, me escreve aqui.
  ```
- **Nunca usar quando:** a mensagem "antes" for assinada com o nome do advogado sem ser ele quem escreve (quem manda é o advogado, ou a mensagem diz quem está escrevendo).

### Modelo 9 · Resumo mensal
- **Quando usar:** todo cliente, todo mês, inclusive o de processo parado. A IA monta a partir do histórico.
- **POP e passo:** POP de atualização de andamento (resumo mensal).
- **Quem revisa antes de enviar:** assistente lê cada resumo antes de sair (nome, etapa, nenhuma promessa); a conferência a fundo contra o processo é por amostra [A DEFINIR tamanho da amostra].
- **Sigla:** A.
- **Texto-modelo:**
  ```
  Oi, [NOME]! Aqui vai o resumo de [MÊS] do seu processo.

  Em que pé está: [ETAPA ATUAL EM LINGUAGEM SIMPLES].
  O que aconteceu no mês: [MOVIMENTAÇÕES EXPLICADAS, OU "o processo ficou aguardando ..., o que é normal nesta etapa"].
  O que esperamos para os próximos meses: [PRÓXIMA ETAPA, SEM PROMETER DATA].
  Pendências suas: [DOCUMENTO OU AÇÃO, OU "nenhuma"].

  O próximo resumo chega até o dia [DIA] de [MÊS]. Se acontecer algo importante antes, eu te aviso na hora.
  ```
- **Nunca usar quando:** houve no mês notícia desfavorável ainda não comunicada por ligação; o cliente pediu para não receber o resumo (registrar na ficha e respeitar).

## Mensagens que a rotina costuma pedir

Não estão entre as nove. Escreva com o advogado, no tom do código, só as que os POPs do escritório usam. Até lá, o texto fica `[A DEFINIR]`.

| Mensagem | POP e passo | Estrutura sugerida | Sigla |
|---|---|---|---|
| Resposta inicial ao contato novo, dentro do horário | POP-ATD-[NN], passo 2 | Quem está falando (o atendimento do escritório), quando uma pessoa continua a conversa, como sinalizar urgência | S |
| Convite para a consulta, em resposta a pergunta jurídica | POP-ATD-[NN], passo 6 | Acolhe a dúvida, explica que a resposta depende de olhar o caso na consulta, como funciona a consulta, próximo passo | A |
| Recusa cordial com indicação | POP de triagem e consulta | Agradece, diz que o escritório não vai atender o caso, indica caminho quando houver, sem orientação jurídica | A |
| Confirmação de recebimento com prazo | POP-REL-[NN] andamento, passo 2 | "Recebi, te retorno até [HORA]." Só vale se o prazo for cumprido | S |
| Aviso de documento ilegível ou errado | POP-REL-[NN] documentos, passo 5 | Qual documento, o que veio errado, como refazer | A |
| Lista de documentos completa | POP-REL-[NN] documentos, passo 8 | Agradece, confirma que está tudo certo, diz o próximo passo do caso em termos gerais | S |
| Lembrete de compromisso (7 dias, véspera, dia) | POP-REL-[NN] agenda, passo 4 | Repete só data, hora, local e o que levar, como na orientação aprovada | S |
| Teste de link de videoconferência | POP-REL-[NN] agenda, exceções | Link, horário do teste, o que conferir (câmera, áudio) | A |
| Mensagem de depois do compromisso | POP-REL-[NN] agenda, passo 8 | O que aconteceu, próximo passo, se o cliente precisa fazer algo | A |
| Fechamento do caso | Régua de atualização (encerramento) | O que aconteceu, o que o cliente recebe ou precisa fazer agora, como falar com o escritório no futuro (parte do modelo 3) | A |
| Ausência do responsável | Régua e regras de canal | Quem responde no lugar e quando o responsável volta | S |

## Mudanças
- 0.1 · AAAA-MM-DD · rascunho criado na organizar-atendimento-whatsapp
