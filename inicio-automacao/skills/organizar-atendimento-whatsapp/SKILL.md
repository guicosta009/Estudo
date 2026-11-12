---
name: organizar-atendimento-whatsapp
description: >
  Organiza o WhatsApp e o atendimento do escritório como um setor: escreve as regras de canal
  (número oficial, horário, urgência, prazos, quem responde, quando vira ligação) e o texto
  para o "Como atendemos" do código, adapta como POPs com S, A e H os quatro fluxos que mais
  consomem o dia (primeiro contato e triagem, dúvida sobre andamento, pedido de documentos,
  agenda e lembretes), monta a régua de atualização proativa e o resumo mensal, escreve a
  biblioteca de mensagens no tom do escritório, as palavras de alerta e os indicadores. Use
  quando o advogado disser "organizar o WhatsApp", "o cliente pergunta toda semana", "cada um
  responde de um jeito", "mensagens-modelo", "resumo mensal", "régua de atualização", "POP do
  WhatsApp", "robô no WhatsApp". Não use para POP de outro setor (use
  escrever-pop) nem para ligar a IA direto no canal (use desenhar-automacao).
---

# Organizar o atendimento pelo WhatsApp

> Trata o WhatsApp como o setor que ele já é: regras de canal no código do escritório, quatro POPs com S, A e H para o que mais chega, uma régua que leva a notícia antes da pergunta, mensagens aprovadas no tom da casa e três números para saber se melhorou.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha, níveis e anatomia do POP: `../../docs/glossario.md`. O que muda entre solo e equipe: `../../docs/trilhas.md`. Pastas e nomes de arquivo: `../../docs/pasta-do-escritorio.md`.

São 22h10 de uma terça. Chega no WhatsApp do escritório: "Doutora, boa noite, alguma novidade do meu processo?". Na manhã seguinte tem mais quatro iguais. Alguém abre o sistema, lê a última movimentação, tenta traduzir "conclusos para despacho" e responde. Depois vem o áudio de três minutos, a foto torta do RG, o pedido de remarcação e o contato novo que quer saber "quanto custa para entrar com o processo".

O WhatsApp tem fila e gente trabalhando nele o dia inteiro. Só falta o POP. Como ele atravessa dois setores do mapa (Atendimento e triagem, enquanto quem escreve é contato novo; Relacionamento com o cliente, quando já é cliente), ninguém se sente dono dele. "Colocar IA num WhatsApp sem regra só faz o caos responder mais rápido."

É a equação da automação aplicada ao canal. **A régua** é a parte "Como atendemos" e "Tom de voz" do código do escritório. **A memória** são as mensagens-modelo, as perguntas frequentes, os critérios de relevância e as listas de documentos. **O roteiro** são os quatro fluxos.

**Regras fixas desta skill** (valem em todo documento que ela escrever):
1. A IA nunca se apresenta como advogado. Mensagem automática diz que é automática.
2. Mensagem com conteúdo do processo nunca sai sem alguém ler.
3. Todo assunto de cliente no número oficial do escritório.
4. Dado sensível no mínimo: só o que a tarefa exige, em conta profissional, anonimizado antes da IA.
5. Notícia ruim, orientação jurídica, cliente aflito e urgência vão sempre para uma pessoa (seção 3 de `references/regras-de-canal.md`).

## 1. Quando usar

**Use quando:**
- O advogado diz que o WhatsApp consome o dia, que o mesmo cliente pergunta toda semana ou que cada pessoa responde de um jeito.
- O setor-alvo do mapa é Atendimento e triagem ou Relacionamento com o cliente e o gargalo está no WhatsApp.
- O escritório quer regras de canal, mensagens-modelo, resumo mensal ou um POP para o que chega pelo WhatsApp.
- Alguém quer "colocar um robô no WhatsApp": esta skill organiza o que precisa existir antes.
- O `/inicio-automacao:pop` indicou esta skill para a etapa 1 de um processo do canal.

**Não use quando:**
- O processo é de outro setor (petição, publicações, cobrança de honorário): use `escrever-pop` ou `organizar-producao-de-pecas`.
- Os POPs do canal já estão testados e o pedido é ligar a IA direto no WhatsApp, com gatilho e fila: use `desenhar-automacao`.
- O pedido é o código do escritório inteiro: use `codigo-do-escritorio`. Esta skill escreve só a parte do canal e sugere o texto.
- O pedido é organizar a base inteira do setor-alvo: use `montar-base`. Esta skill cria os documentos do canal e deixa o resto para ela.

## 2. Antes de começar

1. **Leia o perfil.** `escritorio/perfil.md` (trilha, porte, apoio, áreas, conta de IA, setor-alvo). Leia também `escritorio/01-cultura/codigo-do-escritorio.md` (seções 2, 4, 5 e 6) e `escritorio/01-cultura/regra-de-uso-de-ia.md`, se existirem. Sem perfil, faça o modo rápido das regras transversais e grave um `perfil.md` mínimo.
2. **Veja o que já existe, para não duplicar.** Abra `escritorio/03-pops/00-mapa-de-pops.md` e as pastas `03-pops/atendimento-e-triagem/` e `03-pops/relacionamento-com-o-cliente/`. Abra `escritorio/04-base/INDICE.md`. Se já houver POP de triagem e consulta ou de atualização de andamento, os fluxos desta skill se encaixam neles (passo 4); se já houver modelos de mensagem, roteiro ou FAQ, eles são o ponto de partida.
3. **Portão: o código do escritório com "Como atendemos" e "Tom de voz".** Sem ele, explique em duas frases: "As mensagens e as regras do canal seguem o tom e os prazos do código. Sem o código, a IA escreve no tom dela e cada pessoa decide o prazo." Ofereça `codigo-do-escritorio`. Se o advogado quiser seguir, as regras de canal desta skill viram a proposta da seção 2 do código, as perguntas de tom do passo 6 cobrem o mínimo, e você registra em "Etapas puladas": "Canal organizado antes do código do escritório (data)".
4. **Trava por estágio.** Pergunte, se o perfil não disser: "A IA roda em conta profissional ou de equipe, com o tratamento de dados conferido? Existe regra de uso de IA escrita?". Sem as duas, todo passo S que mexe com dado de cliente sobe para A, e o teste da triagem (passo 8) usa mensagens fictícias. Diga isso antes de adaptar os POPs.
5. **Dado de cliente.** Nunca peça mensagem real identificada. Se o advogado colar uma conversa com nome, telefone, CPF ou número de processo, avise, não repita o dado e mostre a versão anonimizada (tabela em `references/regras-de-canal.md`, seção 6) antes de continuar.
6. **Pedido de uma peça só.** Se o advogado quer só a biblioteca, só as regras ou só um POP, vá direto ao passo correspondente. Ao fim, mostre em uma linha o que ficou de fora e para que serve.

## 3. Fluxo

### Passo 1. Ler os sintomas e escolher por onde começar
Mostre a tabela e pergunte: "Quais destas cenas acontecem no seu escritório? Pode marcar mais de uma."

| Sintoma | O que está por trás | Onde resolve |
|---|---|---|
| O mesmo cliente pergunta toda semana | O escritório só fala quando é perguntado | Passo 5, régua de atualização |
| Cada pessoa responde de um jeito | Não existe biblioteca nem tom escrito | Passo 6, biblioteca |
| Conversa de cliente no celular pessoal | Não existe número oficial nem regra de canal | Passo 3, regras de canal |
| Ninguém sabe o que já foi dito ao cliente | O histórico mora na conversa, e a conversa mora num aparelho | Passo 4 (fluxo 2) e passo 3 (registro) |
| O titular responde às 22h05 | Sem horário combinado, todo horário vira horário de atendimento | Passo 3, regras de canal |
| Documento pedido três vezes e ainda faltando | O pedido não explica onde conseguir nem como mandar | Passo 4 (fluxo 3) e modelo 2 |

**Ordem recomendada:** medir o antes (passo 2), regras de canal (3), o fluxo que mais pesa (4), régua (5), biblioteca (6), base do atendimento (7), teste da triagem (8). Comece pelos sintomas marcados, mas não pule o passo 2: "Sem o antes, daqui a um mês você vai ter só a sensação de que melhorou."

### Passo 2. Medir o antes
Três números, anotados nesta semana, antes de qualquer mudança. Pergunte um por vez:
1. "Numa semana, quanto tempo passa entre a mensagem do cliente e a primeira resposta de uma pessoa? A automática não conta. Dá para anotar a hora de 20 conversas e tirar a média." 
2. "Quantas mensagens do tipo 'e aí, como está meu processo?' chegam por semana? Uma marca na planilha a cada uma já resolve."
3. "Quantas mensagens por semana pedem resposta de alguém, e quantos minutos leva cada uma, contando abrir o processo, ler e escrever?"

Se houver audiência e perícia, acrescente: "Quantas faltas em consulta, audiência e perícia no último mês?". O que o advogado não souber vira `[A CONFIRMAR]` com a forma de medir na semana. Grave conforme a seção 7 e ofereça a `medir-retorno` para o valor da hora e o painel.

### Passo 3. Escrever as regras de canal
Leia `references/regras-de-canal.md`. Faça as perguntas da tabela das treze regras, uma por vez, na ordem: número oficial, horário, urgência fora do horário, primeira resposta, resposta completa, quem responde (com substituto), áudio, quando vira ligação, quando vira reunião, o que não se trata por WhatsApp, grupos, registro, mensagem automática.
- Peça número em todo prazo. "O mais rápido possível" vira `[A DEFINIR]`.
- Se o código já tem a seção 2, leia e confirme cada campo em vez de perguntar do zero. Se o que o advogado diz agora diverge do código, mostre a divergência e pergunte qual vale.

Depois, mais duas partes:
- **O que sempre vai para uma pessoa.** Mostre a lista da seção 3 da referência e pergunte: "Tem algum caso aqui que vocês tratam diferente? E algum que falta?". A lista mínima não sai: notícia ruim por ligação, orientação jurídica só com advogado ou na consulta, cliente aflito, urgência, vulnerabilidade.
- **Palavras de alerta.** "Pense nas últimas mensagens que precisavam de você na hora. Que palavras elas tinham?" Peça por área. Os exemplos da seção 4 da referência só entram se o advogado confirmar um por um.

Monte o documento a partir de `assets/regras-de-canal-modelo.md`. Mostre, em seguida, o anexo com a sugestão para o código (seções 2, 4 e 6), cada linha marcada `[NOVO]` ou `[ALTERADO]`. Pergunte: "Quer que eu aplique este texto no código do escritório?". Só com o ok: aplique, suba a versão do código uma casa, atualize a data e lembre de gerar de novo as instruções do Projeto (`codigo-do-escritorio`, modo converter). Sem o ok, a sugestão fica no anexo do documento da base.

### Passo 4. Adaptar os fluxos como POPs
Mostre a tabela da seção 4 desta skill e pergunte: "Qual destes fluxos mais pesa no seu dia hoje?". Um fluxo por vez; o primeiro é o que mais pesa. Abra só a referência escolhida (`references/fluxo-1-primeiro-contato.md` a `fluxo-4-agenda-e-lembretes.md`) e siga a adaptação:

1. **Retrato antes.** "Me conte a última vez que isso aconteceu: quem viu a mensagem, o que fez, quanto tempo levou." Escreva como é hoje, sem melhorar, e peça ok.
2. **Lado a lado.** Compare o retrato com o POP de referência: passos que só um lado tem, passos iguais com nomes diferentes.
3. **Funções por pessoas.** Troque atendente, assistente e advogado pelas funções do escritório (e depois pelos nomes). Se o mesmo nome aparece em todos os passos, aponte: ali está o gargalo.
4. **Prazos e exceções do código.** Os prazos da referência são exemplo e nunca entram como regra sem o advogado dizer que valem. O que não foi decidido fica `[A DEFINIR]`. Para cada decisão, pergunte "e se não?".
5. **Siglas pelo estágio.** Refaça a sigla de cada passo pela árvore da `classificar-sah` e pela trava do item 4 da seção 2. Justifique cada mudança em uma linha. Nenhum passo com conteúdo do processo vira S no envio.
6. **Lista do que a IA consulta.** Monte a tabela do que o POP cita e ainda não existe por escrito (glossário de termos processuais, roteiro, listas de documentos, modelos). Ela vai para a `montar-base` e para os passos 6 e 7.
7. **Código e versão.** Sigla ATD (Atendimento e triagem) ou REL (Relacionamento com o cliente); o próximo número livre do setor sai do `00-mapa-de-pops.md` e nunca é reaproveitado. Sem mapa, use o próximo número depois dos POPs da pasta e avise que a `gerir-pops` vai registrá-lo. O POP nasce na versão 0.1, status Rascunho. A versão 1.0 vem depois do teste.

**Encaixe com os POPs da biblioteca e com os que o escritório já tem:**
- **Fluxo 1** termina na ficha com o advogado e na consulta agendada. A consulta (briefing, condução, ata) é do POP de triagem e consulta (`../escrever-pop/references/biblioteca/setor-01-atendimento-triagem.md`). Se o escritório já tem esse POP, o fluxo 1 vira o POP da parte que acontece no WhatsApp e aponta para ele no passo 7. Se o primeiro contato é quase todo pelo WhatsApp e o advogado prefere um POP só, junte os dois e corte o que sobra, mantendo de 7 a 12 passos.
- **Fluxo 2** responde a pergunta que chega. O aviso que o escritório manda quando o processo se mexe é do POP de atualização de andamento (`../escrever-pop/references/biblioteca/setor-07-relacionamento-cliente.md`). Se ele já existe, sugira que o passo dele de "responder a dúvida" aponte para o POP do fluxo 2, marcado `[ALTERADO]`, e só mude com o ok.
- **Fluxo 3** cuida da conversa. O arquivo que chega segue o POP de documentos do Administrativo (`setor-10-administrativo.md` da mesma biblioteca).
- **Fluxo 4** fica em Relacionamento com o cliente quando cobre audiência e perícia; em Atendimento e triagem, se cobrir só a consulta inicial. Um código só.

Mostre o POP nos 12 campos, com o fluxograma em Mermaid e em texto, a lista do que a IA consulta e os pontos em aberto. Pergunte se quer seguir para o próximo fluxo agora ou depois.

### Passo 5. Montar a régua de atualização proativa e o resumo mensal
Explique em duas frases: "Hoje o escritório fala quando é perguntado, então o cliente aprende que precisa perguntar. Quando o escritório avisa em data combinada, e avisa de novo sempre que algo relevante acontece, a pergunta perde o motivo."

Faça até cinco perguntas, uma por vez:
1. "Quais são as áreas e os tipos de ação mais comuns?"
2. "Quantos processos ativos, mais ou menos?"
3. "Quem vai cuidar da régua, e quanto tempo por semana essa pessoa tem?"
4. "Que ferramentas vocês usam: software jurídico, planilha, CRM, que IA e em que tipo de conta?"
5. "Como é hoje: vocês só respondem quando o cliente pergunta, ou já avisam alguma coisa?"

Depois, preencha `assets/regua-de-atualizacao-modelo.md`, nesta ordem:
- **Cadência:** contratação, movimentação relevante, resumo mensal, compromisso, notícia difícil, encerramento. Para cada prazo: "Até quando vocês conseguem cumprir isso todo mês, inclusive na semana cheia?". Prazo não dito fica `[A DEFINIR]`.
- **Movimentação por movimentação:** para cada área, pergunte "Qual foi a última movimentação que você achou importante avisar? E uma que não precisava?". Monte a tabela com três destinos (só registra para o resumo, avisa por mensagem, advogado liga antes) e a sigla. A versão de cada área vai para o critério de relevância, no esqueleto da `montar-base` (`../montar-base/assets/esqueletos/criterios-relevancia-movimentacao.md`). Na dúvida entre rotina e relevante, é relevante.
- **O que nunca vai por mensagem:** a lista mínima da régua e o que o advogado acrescentar.
- **Resumo mensal:** todo cliente, inclusive o de processo parado; cada resumo lido por alguém antes de sair; conferência a fundo contra o processo por amostra; quem pediu para não receber fica registrado e respeitado; quem passou do limite de perguntas de andamento entra com prioridade.
- **Custo da régua por semana:** a conta à mostra, marcada como estimativa.

Se o escritório ainda não tem o POP de atualização de andamento, a régua fica gravada na base e você oferece adaptar o POP pela `escrever-pop` (entrada B, setor 07). A régua dá a ele as decisões que a biblioteca deixou em aberto.

### Passo 6. Escrever a biblioteca de mensagens no tom do escritório
Abra `assets/biblioteca-de-mensagens-modelo.md`. Se o código tem "Tom de voz", leia e confirme. Depois, uma pergunta por vez:
1. "Como é o cliente típico? Por exemplo: segurados do INSS, muitos idosos; famílias em divórcio."
2. "Vocês tratam por você, por senhor e senhora, ou pelo nome?"
3. "Cole duas ou três mensagens que vocês mandaram e de que gostaram." Anonimize antes de usar.
4. "Tem alguma frase que você não quer ver saindo do escritório?"

Reescreva os modelos no tom da casa, mantendo os campos entre colchetes. Comece pelos que os POPs adaptados usam; o mínimo é boas-vindas (1), andamento (3), "nada mudou" (4) e fora do horário (6). Regras da reescrita: mensagem curta, uma ideia por parágrafo; sem juridiquês e termo técnico explicado na primeira vez; nenhuma promessa de resultado, prazo de decisão ou valor; nenhuma orientação jurídica a quem ainda não é cliente; mensagem automática diz que é automática; a IA nunca fala como advogado. Para cada modelo, confirme quem revisa antes de enviar e a sigla.

Depois dos nove, mostre a lista "Mensagens que a rotina costuma pedir" e pergunte quais o escritório quer escrever agora. As outras ficam `[A DEFINIR]`. Sem inventar regra, prazo ou número de lei.

### Passo 7. Montar a base do atendimento
Os POPs do canal citam três documentos que moram em Atendimento e triagem. Para cada um, use o esqueleto da `montar-base` e entreviste, uma pergunta por vez:
- **Roteiro de triagem por área** (`../montar-base/assets/esqueletos/roteiro-triagem-por-area.md`): "Quais perguntas vocês fazem a quem chega com um caso de [ÁREA]? Em que ordem?". Pergunta que pede documento sensível antes da consulta sai do roteiro. Urgências da área vêm das palavras de alerta.
- **Perguntas frequentes** (`../montar-base/assets/esqueletos/faq-clientes.md`): horário, endereço, como funciona a consulta, documentos por tipo de caso e as perguntas de andamento que mais chegam. "Separe as dez perguntas que mais chegaram na última semana, do jeito que o cliente escreve." Para cada uma: a resposta aprovada e quando ela não serve e a conversa vai para o advogado.
- **Lista de documentos por tipo de caso** (`../montar-base/assets/esqueletos/checklist-documentos-por-tipo-de-caso.md`): um arquivo por tipo de caso, com onde o cliente consegue cada documento, que é o que o modelo 2 precisa. Requisito técnico de documento fica `[CONFERIR]` na fonte.

Os exemplos dos esqueletos só ficam se o advogado confirmar um por um. O glossário de termos processuais em linguagem simples (fluxo 2) e as orientações por tipo de audiência e perícia (fluxo 4) entram na lista para a `montar-base`.

### Passo 8. Testar a triagem com uma semana de mensagens
Leia `references/triagem-de-mensagens.md`. Peça: "Separe as mensagens de uma semana, anonimizadas, cada remetente com um código, com data e hora." Com conta pessoal gratuita, use mensagens fictícias parecidas com as reais.
- Classifique cada mensagem pelo caminho de cada mensagem e pelas regras de canal, preenchendo a ficha do teste. Não escreva resposta para nenhuma mensagem: só classifique.
- Mostre: quantas por fluxo, quantas em "outro assunto", quantas com sinal de alerta.
- Duas leituras: se alguma mensagem com sinal de alerta caiu numa resposta pronta, a regra ou a lista de palavras está falhando e volta ao passo 3; se muita coisa caiu em "outro assunto", existe um quinto fluxo (financeiro e cobrança costuma ser o candidato: `escrever-pop`, entrada B, setor 06).

O teste de cada POP, um a um, é da `testar-pop`.

### Passo 9. Mostrar, ajustar e gravar
Mostre cada documento inteiro, peça ajustes e grave só depois do ok, nos caminhos da seção 7. Registre cada documento da base no `04-base/INDICE.md` (se não existir, crie a partir de `../montar-base/assets/indice-modelo.md` e avise). Feche com a lista de pontos em aberto, cada um com a pergunta que resolve, e o próximo passo.

## 4. Os quatro fluxos lado a lado

| Fluxo | Referência | Setor do mapa | Passos | S | A | H | Indicador principal |
|---|---|---|---|---|---|---|---|
| 1 · Primeiro contato e triagem | `fluxo-1-primeiro-contato.md` | Atendimento e triagem | 8 | 4 | 3 | 1 | Tempo até a primeira resposta de uma pessoa |
| 2 · Dúvida sobre andamento | `fluxo-2-duvida-de-andamento.md` | Relacionamento com o cliente | 8 | 5 | 2 | 1 | Perguntas de andamento por semana |
| 3 · Pedido e cobrança de documentos | `fluxo-3-documentos.md` | Relacionamento com o cliente | 8 | 4 | 3 | 1 | Dias até a lista completa |
| 4 · Agendamento, orientação e lembretes | `fluxo-4-agenda-e-lembretes.md` | Relacionamento (ou Atendimento) | 8 | 4 | 2 | 2 | Faltas por mês |

As siglas valem para um escritório com conta profissional de IA e regra de uso escrita. Sem isso, todo passo S que mexe com dado de cliente sobe para A. Nos quatro, o que sai para o cliente com conteúdo do processo passa pela leitura de alguém, e a conversa difícil continua humana.

## 5. Onde a IA entra no canal

No WhatsApp, a IA rende muito na parte que ninguém vê. Na parte que o cliente vê, ela entra com modelo aprovado e com uma pessoa por perto.

| Sigla | Tarefa | Por quê |
|---|---|---|
| S | Classificar a mensagem recebida: tipo (contato novo, andamento, documento, agenda, financeiro, reclamação), urgência e fluxo | Regra que cabe num papel, volume alto e erro percebido no passo seguinte. É o primeiro lugar para colocar a IA. |
| A | Rascunhar a resposta a partir da movimentação, do histórico e da biblioteca, no tom do código | A pessoa lê, ajusta e envia. Mensagem com conteúdo do processo nunca sai sem alguém ler. |
| A | Resumir o histórico antes de ligar ou quando o caso troca de mão: o que já foi dito, o que foi prometido, o que está pendente, como o cliente está se sentindo | A pessoa confere com a conversa original antes de usar. |
| H | A conversa que pede gente: notícia ruim, cliente aflito, reclamação, decisão sobre acordo, vontade de desistir | A IA pode preparar a ligação. A conversa é do advogado responsável. |

**Robô de atendimento.** Faz sentido para resposta inicial, fora do horário, perguntas frequentes sobre o escritório e lembretes, com dois cuidados: publicidade e ética (Provimento 205/2021 do CFOAB e Código de Ética e Disciplina da OAB valem para o que o robô escreve) e transparência (a mensagem diz que é automática e quando uma pessoa assume). Detalhe em `references/regras-de-canal.md`, seção 5.

**Porta da frente primeiro.** No começo, alguém copia a mensagem anonimizada para o Projeto do escritório no Claude, recebe a classificação ou o rascunho e decide (prompts 2, 3 e 5 de `references/prompts-do-canal.md`). Ligar a IA direto no canal é automação: só com o POP testado, a biblioteca aprovada e as regras de canal escritas, pela `desenhar-automacao`.

## 6. Indicadores do canal

No WhatsApp, medir é mais fácil do que em outros setores, porque tudo tem data e hora. Três números bastam; o quarto entra quando houver audiência e perícia.

| Indicador | Como medir | Onde anotar | Frequência | Quem anota |
|---|---|---|---|---|
| Tempo de primeira resposta de uma pessoa | Hora da mensagem e hora da resposta de 20 conversas; média | Planilha | Uma semana por mês, como amostra | Atendente |
| "E aí, como está meu processo?" por semana | Uma marca a cada pergunta, ou a etiqueta da ferramenta, se ela tiver | Planilha ou ferramenta | Toda semana | Assistente, ou a IA no passo 8 do fluxo 2 |
| Horas por semana no WhatsApp | Mensagens por semana × minutos por mensagem, antes e depois | Conta abaixo | Antes de começar e uma vez por mês | Dono dos POPs do canal |
| Faltas em compromissos | Agenda | Planilha | Todo mês | Atendente |

**Conta das horas (números de exemplo):** antes, 100 mensagens por semana × 6 minutos = 600 minutos = 10 horas por semana. Depois de um mês de régua, 60 mensagens × 4,5 minutos (com a classificação e o rascunho da IA, já contando a leitura de quem aprova) = 270 minutos = 4,5 horas por semana. Diferença: 5,5 horas por semana, 22 horas a menos num mês de 4 semanas. As horas devolvidas só valem com o campo "para onde foram as horas" (`medir-retorno`).

## 7. O que entrega e onde grava

| Entrega | Caminho |
|---|---|
| POP do fluxo 1 | `escritorio/03-pops/atendimento-e-triagem/pop-atd-<nn>-primeiro-contato-whatsapp.md` |
| POP do fluxo 2 | `escritorio/03-pops/relacionamento-com-o-cliente/pop-rel-<nn>-duvida-de-andamento.md` |
| POP do fluxo 3 | `escritorio/03-pops/relacionamento-com-o-cliente/pop-rel-<nn>-pedido-de-documentos.md` |
| POP do fluxo 4 | `escritorio/03-pops/relacionamento-com-o-cliente/pop-rel-<nn>-agenda-e-lembretes.md` (ou `atendimento-e-triagem/pop-atd-<nn>-agenda-e-lembretes.md`) |
| Regras de canal, o que sempre vai para pessoa, palavras de alerta, caminho de cada mensagem | `escritorio/04-base/comum/regras-de-canal.md` |
| Biblioteca de mensagens | `escritorio/04-base/relacionamento-com-o-cliente/biblioteca-de-mensagens.md` |
| Régua de atualização e resumo mensal | `escritorio/04-base/relacionamento-com-o-cliente/regua-de-atualizacao.md` |
| Critério de relevância por área | `escritorio/04-base/relacionamento-com-o-cliente/criterios-relevancia-movimentacao-<area>.md` |
| Roteiro de triagem por área | `escritorio/04-base/atendimento-e-triagem/roteiro-triagem-<area>.md` |
| Perguntas frequentes | `escritorio/04-base/atendimento-e-triagem/faq-clientes.md` |
| Lista de documentos por tipo de caso | `escritorio/04-base/atendimento-e-triagem/checklist-documentos-<tipo-de-caso>.md` |
| Sugestão de texto para o código | Anexo de `regras-de-canal.md`; no código só com o ok do advogado |
| Os três números do antes | Seção "Canal WhatsApp" de `escritorio/06-medicao/linha-de-base-relacionamento-com-o-cliente.md` (se o arquivo não existir, crie com o cabeçalho e avise que a `medir-retorno` completa) |

- Todo documento da base leva o cabeçalho da `montar-base` (`../montar-base/assets/cabecalho-documento.md`) e entra no `04-base/INDICE.md` como "rascunho" até o dono aprovar. Só "em uso" vai para o Projeto no Claude.
- POP nasce em 0.1, status Rascunho, com o fluxograma em Mermaid e em texto. Se existir o `00-mapa-de-pops.md`, acrescente a linha do POP com código, dono, versão, status e degrau; se não existir, avise que a `gerir-pops` cria o mapa.
- No `perfil.md`: se o setor-alvo é Atendimento e triagem ou Relacionamento com o cliente, marque o POP do setor-alvo como em andamento (por exemplo, `- [ ] POP do setor-alvo com S, A e H (POP-REL-01 v0.1, teste pendente)`). Acrescente no "Histórico" uma linha por entrega, com data e caminho, e atualize `atualizado_em`. O que foi pulado vai para "Etapas puladas".
- Nomes de arquivo: minúsculas, sem acento, hífen entre palavras, sem versão no nome.
- Sem acesso a arquivos: entregue cada documento no chat, em bloco pronto para copiar, com o caminho onde ele deveria ficar.

## 8. Trilha solo e trilha equipe

**Solo** (inclusive com secretária ou estagiário):
- "A atendente assume" vira "o advogado assume": urgência, aflição e reclamação vão direto para o titular.
- As regras de canal protegem o horário do titular. Horário escrito, mensagem automática fora dele e um caminho de urgência que não seja "qualquer mensagem no meu celular a qualquer hora". Pergunte: "O que acontece com a mensagem das 22h quando você está de férias ou em audiência?". A resposta vira a regra de ausência: quem responde, o que espera, que mensagem sai.
- Se houver secretária ou estagiário, essa pessoa é a atendente dos POPs e a embaixadora do canal. O titular fica com o que é H e revisa os A.
- O titular revisa todas as mensagens A. A pressão para virar S aumenta: mantenha A, revise num horário fixo do dia, nunca logo depois de a IA rascunhar, com o checklist de tom.
- Número oficial vale também para o solo: o WhatsApp do escritório separado do pessoal, para o histórico não morar num aparelho só.

**Equipe:**
- Atendente com roteiro de triagem e palavras de alerta; assistente de relacionamento para cliente ativo; advogado para o que pede advogado. Cada função com substituto escrito, "nunca quem estiver livre".
- Mensagem com conteúdo do processo revisada por quem acompanha o caso.
- Todos no número oficial e no mesmo histórico. Ninguém atende cliente no celular pessoal.
- Mostre os POPs e a biblioteca a quem atende antes de fechar: é quem conhece a exceção que falta e as frases que o cliente entende de primeira.
- Se o mesmo nome aparece em todos os passos, aponte e proponha passar os A para quem executa, deixando o titular com as decisões e as ligações difíceis.

## 9. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Responder rápido sem informar | O cliente pergunta de novo na semana seguinte | Modelo 4 e régua: o que aconteceu, o que vem agora, quando chega a próxima notícia |
| IA no WhatsApp sem regra | O caos responde mais rápido | Regras de canal e POPs antes de qualquer automação |
| Robô que se passa por advogado | Confiança perdida e problema ético | Regra fixa 1 e cuidados de publicidade e transparência |
| Mensagem do processo enviada sem leitura | Erro de etapa, data ou promessa chega ao cliente | Regra fixa 2; nenhum envio com conteúdo do processo vira S |
| Notícia ruim por mensagem | Relação abalada no pior momento | Ligação do advogado primeiro, modelo 8 depois |
| Orientação jurídica pelo WhatsApp a quem não é cliente | Consulta de graça e risco ético | Convite para a consulta, revisado |
| Prazo de exemplo virando regra | Promessa que ninguém decidiu | Prazo do código ou `[A DEFINIR]` |
| Conversa no celular pessoal | Sigilo exposto, histórico perdido | Número oficial nas regras e no código |
| Palavra de alerta caindo em resposta pronta | Urgência sem ninguém ver | Teste da triagem com a conta que precisa dar zero |
| POP duplicado com o da biblioteca | Dois roteiros para o mesmo passo | Encaixe com os POPs de triagem, atualização e documentos |
| Medir só depois | Sensação no lugar de número | Passo 2 antes de qualquer mudança |

## 10. Próximo passo

- Para cada POP adaptado: `desenhar-fluxograma` (raias IA, Equipe, Advogado) e `testar-pop` (teste de mesa, teste com a IA em três casos, versão 1.0). Depois, `auditar-riscos` e `gerir-pops` para o código, o dono e a versão vigente no mapa.
- Para a base: `montar-base`, com a lista do que os POPs citam e ainda não existe (glossário de termos processuais, orientações por tipo de audiência e perícia, critério de relevância de cada área) e os casos de teste do canal (o típico, o com exceção, o que deve parar, o com dado sensível).
- Com o POP testado e a base em uso: `pop-para-skill`, para o Claude conduzir o POP passo a passo. Ligar a IA direto no canal fica para a `desenhar-automacao`.
- Para os números: `medir-retorno`, com o antes do passo 2.

## Referências desta skill

- `references/regras-de-canal.md`: as treze regras com as perguntas, onde cada regra entra no código, o que sempre vai para uma pessoa, palavras de alerta, robô e anonimização. Leia no passo 3.
- `references/triagem-de-mensagens.md`: o caminho de cada mensagem (Mermaid e texto) e a ficha do teste da triagem. Leia nos passos 3 e 8.
- `references/fluxo-1-primeiro-contato.md`, `fluxo-2-duvida-de-andamento.md`, `fluxo-3-documentos.md`, `fluxo-4-agenda-e-lembretes.md`: os quatro POPs de referência nos 12 campos, com fluxograma. Abra só o escolhido, no passo 4.
- `references/prompts-do-canal.md`: os cinco prompts para usar no Projeto do escritório. Leia no passo 5 (régua), no 6 (biblioteca) e quando o advogado quiser operar pela porta da frente.
- `assets/regras-de-canal-modelo.md`: o documento de regras de canal, com o anexo de sugestão para o código. Use no passo 3.
- `assets/regua-de-atualizacao-modelo.md`: a régua, a tabela por movimentação e o resumo mensal. Use no passo 5.
- `assets/biblioteca-de-mensagens-modelo.md`: as nove mensagens-modelo e as que a rotina costuma pedir. Use no passo 6.
