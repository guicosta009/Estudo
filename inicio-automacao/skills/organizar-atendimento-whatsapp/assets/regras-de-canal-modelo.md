# Regras de canal do WhatsApp
Versão: 0.1 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: comum (Atendimento e triagem, Relacionamento com o cliente) · Área: todas · Usado por: classificação de toda mensagem; POP-ATD-[NN] primeiro contato (passos 1, 2 e 4); POP-REL-[NN] dúvida de andamento (passos 5 e 6); POP-REL-[NN] documentos; POP-REL-[NN] agenda e lembretes · Acesso: geral
Aprovado por: [FUNÇÃO OU NOME] · Próxima revisão: revisão trimestral, ou quando entrar pessoa nova, mudar o horário ou a ferramenta

> As regras que dizem como o escritório atende pelo WhatsApp. O resumo está na seção 2 do código do escritório ("Como atendemos"); aqui fica a versão completa, que a IA consulta para classificar e encaminhar cada mensagem. Prazos e horários são do escritório: o que ainda não foi decidido fica `[A DEFINIR]`.

## 1. Regras

- **Número oficial:** [NÚMERO]. Nenhum assunto de cliente no celular pessoal da equipe. Documento recebido no celular pessoal vai para o número oficial e é apagado do aparelho.
- **Horário:** [DIAS], das [HORA] às [HORA]. Fora disso, mensagem automática com o próximo horário de atendimento (modelo 6).
- **Urgência fora do horário:** [O QUE CONTA COMO URGÊNCIA] vai para [QUEM], por [CANAL].
- **Primeira resposta de uma pessoa:** cliente ativo em até [PRAZO]; contato novo em até [PRAZO]. A automática não conta.
- **Resposta completa:** até [PRAZO]. Se depender do advogado, até [PRAZO], avisando o cliente quando ela vem. Resposta-ponte: "[FRASE]".
- **Áudio:** [REGRA]. Notícia importante vai por escrito, para poder reler.
- **Vira ligação:** notícia muito ruim, cliente aflito ou insatisfeito, decisão que o cliente precisa tomar, assunto que passou de [N] mensagens sem resolver.
- **Vira reunião:** [CASOS, EX.: PROPOSTA DE ACORDO, MUDANÇA DE ESTRATÉGIA, PRESTAÇÃO DE CONTAS NO FIM DO CASO].
- **Não tratamos pelo WhatsApp:** [LISTA, EX.: CONSULTA JURÍDICA PARA QUEM AINDA NÃO É CLIENTE, NEGOCIAÇÃO DE HONORÁRIO FORA DA TABELA, ASSUNTO DE UM CLIENTE COM OUTRA PESSOA SEM AUTORIZAÇÃO DELE].
- **Grupos:** [REGRA, EX.: SEM GRUPO COM CLIENTE; SE A FAMÍLIA QUER ACOMPANHAR, O CLIENTE INDICA QUEM RECEBE].
- **Registro:** todo contato relevante entra no histórico do cliente em [ONDE: CRM, PLANILHA, SOFTWARE JURÍDICO].
- **Atualização proativa:** resumo mensal até [DIA]; movimentação relevante avisada em até [PRAZO]. Detalhe na régua de atualização (`04-base/relacionamento-com-o-cliente/regua-de-atualizacao.md`).
- **Mensagem automática:** sempre diz que é automática e quando uma pessoa responde. Nunca usa nome de advogado como se fosse ele digitando.
- **A IA no canal:** nunca se apresenta como advogado; mensagem com conteúdo do processo nunca sai sem alguém ler.

## 2. Quem responde

| Quem escreve | Quem responde | Substituto | Quando chama o advogado |
|---|---|---|---|
| Contato novo | [FUNÇÃO OU NOME] | [FUNÇÃO OU NOME] | Pergunta jurídica, urgência, aflição, parte contrária |
| Cliente ativo | [FUNÇÃO OU NOME] | [FUNÇÃO OU NOME] | Decisão, valor, estimativa de prazo, reclamação, desistência |
| Assunto que pede advogado | [ADVOGADO RESPONSÁVEL] | [FUNÇÃO OU NOME] | Sempre |

Em escritório pequeno a mesma pessoa acumula funções, e tudo bem, mas cada papel fica escrito.

## 3. O que sempre vai para uma pessoa

Nenhum destes casos recebe resposta automática, nem com modelo aprovado:

- Notícia ruim: o advogado liga antes de qualquer mensagem; depois, mensagem curta que registra a conversa.
- Pergunta jurídica de quem ainda não é cliente: convite para a consulta, revisado por uma pessoa.
- Orientação nova para cliente, decisão que ele precisa tomar, estimativa de valor, de data de pagamento, de prazo de decisão ou de chance de êxito: advogado.
- Cliente aflito, insatisfeito, com reclamação ou vontade de desistir: advogado, por ligação.
- Urgência: [LISTA DO ESCRITÓRIO]: advogado, pelo caminho de urgência.
- Cliente em situação de vulnerabilidade (violência, criança em disputa, doença grave, perda de emprego, idoso sem renda, luto): a pessoa assume e aciona o advogado. Em Família, sinal de violência, coação ou risco tira o caso da automação.
- Pedido de remarcação de audiência ou perícia: advogado.
- Parte contrária de cliente atual: advogado.
- [A DEFINIR: outros casos do escritório]

## 4. Palavras de alerta

A IA sinaliza a mensagem que contém qualquer destas palavras ou frases; a pessoa decide o que fazer. Na dúvida entre urgência normal e alta, vale alta.

| Área | Palavras e frases | Confirmado por | Em |
|---|---|---|---|
| Todas | [A DEFINIR] | | |
| [ÁREA] | [A DEFINIR] | | |

## 5. Caminho de cada mensagem

1. A IA registra e classifica: tipo, urgência, contato novo ou cliente ativo.
2. Urgente ou pessoa aflita: a pessoa avisa o advogado na hora e o advogado liga.
3. Contato novo: POP-ATD-[NN] primeiro contato e triagem.
4. Cliente ativo que pede orientação nova, reclama ou fala em desistir: a IA resume o histórico, a pessoa confere e o advogado assume por ligação ou reunião.
5. Cliente ativo com pedido operacional: andamento (POP-REL-[NN]), documento (POP-REL-[NN]), agenda e lembrete (POP-REL-[NN]) ou outro assunto (a pessoa decide o caminho).
6. A IA rascunha a resposta pelo modelo; a pessoa responsável aprova, ajusta ou passa ao advogado.
7. A IA envia e registra no histórico, dentro do prazo deste documento.

## 6. Dado de cliente no canal

- Antes de colar qualquer mensagem na IA: nome pelo código do cliente ou `[CLIENTE]`; CPF, RG e número de benefício saem; processo por `[PROCESSO]`; endereço e telefone saem; saúde, criança e violência viram descrição genérica e só entram quando a tarefa precisar.
- Conta de IA autorizada para dado de cliente: [CONTA PROFISSIONAL OU DE EQUIPE, CONFERIDA EM AAAA-MM-DD].
- Senha e credencial nunca são pedidas por mensagem nem entram na IA. Laudo completo, dado de criança ou adolescente e processo em segredo de justiça não entram sem autorização expressa do responsável.

## Mudanças
- 0.1 · AAAA-MM-DD · rascunho criado na organizar-atendimento-whatsapp

---

## Anexo: sugestão de texto para o código do escritório

Não faz parte do documento da base. A skill mostra este bloco ao advogado, com `[NOVO]` ou `[ALTERADO]` em cada linha que muda o código, e só aplica com o ok dele.

**Seção 2. Como atendemos**
```
- Canais oficiais: WhatsApp no número [NÚMERO]. Nenhum assunto de cliente no celular pessoal da equipe.
- Horário: [DIAS], das [HORA] às [HORA].
- Prazo de resposta: cliente ativo em até [PRAZO]; contato novo em até [PRAZO]. Resposta completa até [PRAZO]. Resposta-ponte: "[FRASE]".
- Mensagem fora do horário: automática, diz que é automática e quando uma pessoa responde.
- Urgência: [LISTA CURTA] → [FUNÇÃO E CANAL].
- Quem faz o primeiro contato: [FUNÇÃO], com o roteiro de triagem da área.
- Atualização proativa: resumo mensal até [DIA]; movimentação relevante avisada em até [PRAZO].
- Regras completas do canal: 04-base/comum/regras-de-canal.md.
```

**Seção 4. Tom de voz** (campo "Áudio, texto ou ligação")
```
- Áudio: [REGRA]. Notícia importante vai por escrito. Vira ligação: notícia muito ruim, cliente aflito ou insatisfeito, decisão que o cliente precisa tomar, assunto que passou de [N] mensagens. Vira reunião: [CASOS].
```

**Seção 6. O que nunca fazemos** (só os itens que ainda não estiverem lá)
```
- Dar notícia muito ruim por mensagem.
- Prometer resultado ou prazo de decisão.
- Orientar por mensagem quem ainda não é cliente.
- Deixar a IA se apresentar como advogado ou mandar mensagem com conteúdo do processo sem alguém ler.
```
