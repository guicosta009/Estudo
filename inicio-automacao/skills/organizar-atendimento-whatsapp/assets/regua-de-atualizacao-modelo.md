# Régua de atualização do cliente
Versão: 0.1 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Relacionamento com o cliente · Área: [ÁREA OU "todas"] · Usado por: POP de atualização de andamento (aviso, resumo mensal); POP-REL-[NN] dúvida de andamento (passo 8, quem entra na régua) · Acesso: geral
Aprovado por: [ADVOGADO RESPONSÁVEL] · Próxima revisão: revisão trimestral, ou quando o indicador de perguntas de andamento não cair depois de um mês de régua

> Cada "e aí, alguma novidade?" é um sintoma de silêncio. O cliente que sabe quando vai receber notícia tende a esperar por ela. Esta régua diz o que o cliente recebe, quando, quem aprova e o que nunca vai por mensagem. O critério do que é movimentação relevante fica em documento próprio, por área (`criterios-relevancia-movimentacao-<area>.md`).

## 1. A cadência

Exemplo de cadência para um escritório de contencioso. Os prazos são exemplos e valem só depois que o advogado confirmar.

| Momento | Quando (exemplo) | O que o cliente recebe | Modelo | Quem aprova | Sigla |
|---|---|---|---|---|---|
| Contratação | No mesmo dia | Boas-vindas com as regras do canal: número oficial, horário, quem cuida do caso e, principalmente, como e quando ele vai saber do processo. É aqui que a régua é combinada. | 1 | [FUNÇÃO] confere os campos | S |
| Movimentação relevante | Até 1 dia útil | Aviso do que muda alguma coisa para o cliente. Despacho de rotina fica no resumo do mês. | 3 e a tabela da seção 2 | Assistente; advogado quando é decisão | A |
| Todo mês | Até o 5º dia útil | Resumo mensal. Todo cliente recebe, inclusive o de processo parado, com a explicação do que está sendo esperado. É o resumo do processo parado que mais evita pergunta. | 9 | Assistente lê cada um; conferência a fundo por amostra | A |
| Compromisso | 7 dias antes, véspera e dia | Orientação e lembretes de audiência, perícia, consulta e reunião, pelo POP de agenda e lembretes. | 5 | Advogado aprova a orientação | A (lembrete S) |
| Notícia difícil | Antes de qualquer mensagem | Ligação do advogado. Depois da ligação, uma mensagem curta registra o que foi conversado. | 8 | Advogado | H |
| Encerramento | Quando o caso termina | Fechamento: o que aconteceu, o que o cliente recebe ou precisa fazer agora e como falar com o escritório no futuro. | Escrito a partir do 3 | Advogado | A |

No escritório: [A DEFINIR cada prazo].

## 2. Que mensagem vai para cada tipo de movimentação

Esta tabela é o começo do critério de relevância, que a IA consulta para classificar. Ela muda de área para área: a versão de cada área vai para `criterios-relevancia-movimentacao-<area>.md` (esqueleto da `montar-base`).

| Movimentação (exemplo) | O que o cliente recebe | Quem aprova | Sigla |
|---|---|---|---|
| Despacho de rotina, juntada, conclusão | Nada na hora. Entra no resumo mensal, explicado. | Ninguém, a IA registra | S |
| Citação ou manifestação da outra parte | Aviso curto: o que aconteceu, o que vem agora e se ele precisa fazer algo. | Assistente | A |
| Audiência ou perícia designada | Aviso com data e local, e entrada no POP de agenda e lembretes. | Advogado aprova a orientação | A |
| Exigência de documento | Pedido pelo POP de documentos, com prazo. | Advogado define a lista | A |
| Decisão ou sentença favorável | Mensagem explicando o que foi decidido, o que ainda pode acontecer e o próximo passo, sem comemorar antes da hora. | Advogado | A |
| Pagamento, alvará ou liberação de valor | Aviso com o próximo passo. Valor e data só com o advogado e o financeiro conferindo. | Advogado | A |
| Decisão desfavorável, sentença de improcedência | Ligação do advogado primeiro. Mensagem só depois, para registrar. | Advogado liga | H |
| [A DEFINIR] | | | |

Regra de segurança: na dúvida entre rotina e relevante, a movimentação é relevante.

## 3. O que nunca vai por mensagem

- Notícia muito ruim: decisão desfavorável relevante ou qualquer problema causado pelo próprio escritório.
- Decisão que o cliente precisa tomar, como aceitar acordo ou recorrer.
- Conversa com cliente em luto, em crise ou muito insatisfeito.
- [A DEFINIR: outros casos do escritório]

Nesses casos o advogado liga, e a mensagem vem depois, curta, registrando o que foi conversado. A IA ajuda a preparar a ligação com o resumo do histórico. A ligação continua sendo do advogado.

## 4. O resumo mensal

- **Quem recebe:** todo cliente com processo ativo, inclusive o de processo parado.
- **Quando:** até o dia [DIA] de cada mês.
- **Como é montado:** a IA monta a partir do histórico do processo e do histórico de contatos, no modelo 9.
- **Quem lê antes de sair:** [FUNÇÃO] lê cada resumo (nome certo, etapa certa, nenhuma promessa de data ou resultado). Mensagem com conteúdo do processo nunca sai sem alguém ler.
- **Conferência a fundo:** [A DEFINIR quantos] resumos por mês conferidos contra o processo, escolhidos ao acaso. Erro encontrado na amostra faz conferir todos daquela área no mês.
- **Quem não recebe pela régua:** cliente com notícia desfavorável ainda não comunicada (primeiro a ligação); cliente que pediu para não receber, registrado na ficha. A régua é um compromisso do escritório com ele, e ele pode abrir mão.
- **Quem entra na régua com prioridade:** cliente que passou do limite de perguntas de andamento no mês ([A DEFINIR], exemplo: duas), sinalizado pelo POP de dúvida de andamento.

## 5. Quanto a régua custa por semana

Estimativa, com a conta à mostra. Troque pelos números do escritório.

- Processos ativos: [N] · Movimentações relevantes por semana: [N] × [MIN] minutos de revisão = [MIN].
- Resumos mensais: [N] por mês ÷ 4 semanas × [MIN] minutos de leitura = [MIN] por semana.
- Total estimado: [H] horas por semana, com a IA rascunhando e uma pessoa aprovando. Estimativa a confirmar depois de um mês de régua.

## Mudanças
- 0.1 · AAAA-MM-DD · rascunho criado na organizar-atendimento-whatsapp
