# Regras de canal: guia para a entrevista

Leia no passo 3 do fluxo. Sem regra de canal, todo horário vira horário de atendimento e todo assunto cabe no WhatsApp. As regras moram em dois lugares: o resumo na seção 2 do código do escritório ("Como atendemos"), que é a régua que a IA e a equipe seguem, e o documento completo em `escritorio/04-base/comum/regras-de-canal.md` (modelo em `../assets/regras-de-canal-modelo.md`), que a IA consulta para classificar e encaminhar.

## 1. As treze regras

Os exemplos são de um escritório fictício e servem só de ponto de partida. O que o escritório ainda não decidiu fica `[A DEFINIR]` até a equipe combinar.

| Regra | Pergunta para o advogado | Exemplo para ajustar | Por que importa |
|---|---|---|---|
| Número oficial | "Qual é o número oficial do escritório? Alguém da equipe atende cliente no celular pessoal?" | Todo assunto de cliente no número do escritório. Nada no celular pessoal da equipe. | Sigilo e continuidade: o histórico fica no escritório quando alguém sai de férias ou vai embora. |
| Horário | "Qual é o horário de atendimento pelo WhatsApp?" | Dias úteis, das 9h às 18h. Fora disso, resposta automática com o próximo horário. | Combina expectativa. Quem responde às 22h ensina o cliente a escrever às 22h. |
| Urgência fora do horário | "O que é urgente de verdade para o escritório fora do horário, e para quem vai? Me conte a última vez que aconteceu." | Audiência no dia seguinte, prisão, violência doméstica: vai para o celular do advogado responsável. | O cliente sabe o que é urgente para o escritório e tem um caminho para isso. |
| Primeira resposta | "Em quanto tempo uma pessoa responde, em horas úteis? Para cliente ativo e para contato novo." | Cliente ativo em até 4 horas úteis. Contato novo em até 2 horas úteis. | Sem número, "o mais rápido possível" vira o que der. |
| Resposta completa | "E a resposta que de fato informa, sai em quanto tempo? E se depender do advogado?" | No mesmo dia útil. Se depender do advogado, até o dia útil seguinte, avisando o cliente. | Separa o "recebi" da resposta que informa. |
| Quem responde | "Quem responde contato novo? Quem responde cliente ativo? Quem cobre quando essa pessoa falta?" | Atendente para contato novo, assistente para cliente ativo, advogado para o que pede advogado. Cada função com um substituto. | Em escritório pequeno a mesma pessoa acumula, e tudo bem, mas o papel precisa estar escrito. |
| Áudio | "Vocês mandam áudio? Quando?" | Áudio só quando o cliente pede. Notícia importante vai por escrito, para poder reler. | Áudio some no histórico e a IA trabalha melhor com texto. |
| Quando vira ligação | "Em que situação vocês param de escrever e ligam?" | Notícia muito ruim, cliente aflito ou insatisfeito, decisão que o cliente precisa tomar, assunto que passou de 5 mensagens sem resolver. | Algumas conversas pedem voz, e insistir no texto piora a relação. |
| Quando vira reunião | "E quando vira reunião?" | Proposta de acordo, mudança de estratégia, prestação de contas no fim do caso. | Decisão importante com registro em ata. |
| O que não se trata por WhatsApp | "O que vocês não tratam por mensagem de jeito nenhum?" | Consulta jurídica para quem ainda não é cliente, negociação de honorário fora da tabela, assunto de um cliente com outra pessoa sem autorização dele. | Orientação jurídica acontece na consulta, e o sigilo é do cliente. |
| Grupos | "Existe grupo com cliente ou com a família do cliente?" | Sem grupo com cliente. Se a família inteira quer acompanhar, o cliente indica quem recebe. | Em grupo, ninguém controla quem lê o quê. |
| Registro | "Onde fica registrado o que foi dito ao cliente?" | Todo contato relevante entra no histórico do cliente, no CRM ou na planilha. | Qualquer pessoa da equipe sabe o que já foi dito, e a IA também. |
| Mensagem automática | "Existe resposta automática hoje? O que ela diz?" | Sempre diz que é automática e quando uma pessoa responde. | Transparência com o cliente (seção 4). |

Se a resposta vier vaga ("a gente responde rápido"), peça o número e o exemplo: "E na terça passada, a mensagem das 22h foi respondida quando?". Se o canal oficial for o celular pessoal de alguém, registre como está hoje e marque a regra como `[A DEFINIR]`: o código vai voltar a isso na seção 5 (Dados e sigilo).

## 2. Onde cada regra entra no código do escritório

O código tem limite de tamanho por seção (a seção 2 tem de 5 a 8 linhas). Por isso o código recebe o resumo e aponta para o documento completo da base.

| Regra de canal | Seção do código | Como entra |
|---|---|---|
| Número oficial, horário, mensagem fora do horário, primeira resposta, urgência e para quem vai, quem faz o primeiro contato | 2. Como atendemos | Uma linha cada, com número |
| Resposta completa e resposta-ponte ("recebi, te retorno até as 16h") | 2. Como atendemos | No campo do prazo de resposta ao cliente ativo |
| Áudio, texto ou ligação; quando vira ligação; quando vira reunião | 4. Tom de voz | No campo "Áudio, texto ou ligação" |
| Número oficial e documento recebido no celular pessoal | 5. Dados e sigilo | No caminho do documento desde o WhatsApp |
| Nada de notícia muito ruim por mensagem, nada de promessa de resultado ou prazo de decisão, nada de orientação a quem ainda não é cliente, IA nunca se apresenta como advogado | 6. O que nunca fazemos | Um item cada, se ainda não estiverem lá |
| Atualização proativa (resumo mensal, prazo do aviso de movimentação) | 2. Como atendemos | Uma linha, apontando para a régua na base |
| Grupos, registro, quem responde com substituto, palavras de alerta | Documento da base | O código diz: "Regras completas do canal em 04-base/comum/regras-de-canal.md" |

**Regra de edição:** a skill mostra o texto sugerido com `[NOVO]` e `[ALTERADO]` em cada linha que muda e pergunta se pode aplicar. Sem o ok, não mexe no código. Com o ok, aplica, sobe a versão do código uma casa (1.2 para 1.3), atualiza a data e lembra que as instruções do Projeto precisam ser geradas de novo (`codigo-do-escritorio`, modo converter). Se o código e a regra de uso de IA disserem coisas diferentes sobre dado e conta, mostre a divergência e pergunte qual vale.

## 3. O que sempre vai para uma pessoa

Nenhum destes casos recebe resposta automática, nem com modelo aprovado. A IA pode sinalizar e preparar material; a conversa é de gente.

| Situação | Para quem vai | Como |
|---|---|---|
| Notícia ruim: decisão desfavorável relevante, benefício negado, sentença contrária, acordo que não saiu, qualquer problema causado pelo próprio escritório | Advogado responsável | Ligação antes de qualquer mensagem. Depois, mensagem curta que registra o que foi conversado (modelo 8). |
| Orientação jurídica: "eu tenho direito?", "quanto vou receber?", "dá para ganhar?", orientação nova sobre o caso | Contato novo: convite para a consulta, revisado. Cliente: advogado | Nada de orientação por mensagem automática. |
| Cliente aflito, insatisfeito, com reclamação ou vontade de desistir | Advogado responsável | Ligação. A IA pode resumir o histórico antes (prompt 5). |
| Urgência: prisão, violência doméstica, audiência ou perícia no dia seguinte, prazo correndo, benefício cortado | Advogado responsável, pelo caminho de urgência do código | Na hora, inclusive fora do horário. |
| Cliente em situação de vulnerabilidade: violência, criança em disputa, doença grave, perda de emprego, idoso sem renda, luto | Atendente assume e aciona o advogado | Em Família, sinal de violência, coação ou risco tira o caso inteiro da automação. |
| Decisão que o cliente precisa tomar: aceitar acordo, recorrer, desistir | Advogado | Ligação ou reunião, com registro. |
| Estimativa de valor, de data de pagamento, de prazo de decisão ou de chance de êxito | Advogado | Nenhuma estimativa sai por mensagem sem ele. |
| Pedido de remarcação de audiência ou perícia | Advogado | Decisão dele; a IA só remarca consulta e reunião do escritório. |
| Parte contrária de um cliente atual escrevendo | Advogado | A triagem para. |
| Documento que o cliente diz não existir; pendência que trava o caso | Advogado | Conversa, não cobrança. |
| Assunto que passou do número de mensagens combinado sem resolver | Pessoa da equipe e, se preciso, advogado | Ligação. |

## 4. Palavras de alerta

São as palavras que fazem uma mensagem pular a fila no caminho de cada mensagem (veja `triagem-de-mensagens.md`) e nunca receber resposta automática. A lista é do escritório, por área, e vai para o documento de regras de canal na base. Pergunte: "Pense nas últimas mensagens que precisavam de você na hora. Que palavras elas tinham?". Peça exemplos reais, anonimizados.

Exemplos de partida, todos a confirmar um por um com o advogado da área:

| Área | Exemplos de palavras e frases de alerta |
|---|---|
| Família | "medida protetiva", "não me deixa ver meu filho", "ameaça", "agressão", "polícia" |
| Previdenciário | "benefício cortado", "perícia amanhã", "não tenho como pagar", "internado" |
| Todas | "preso", "prisão", "audiência amanhã", "prazo", "urgente", "vou desistir", "outro advogado", "reclamação", "faleceu" |

A IA marca a palavra de alerta; quem decide o que fazer é a pessoa. Na dúvida entre urgência normal e alta, a IA marca alta e explica.

## 5. Mensagem automática e robô de atendimento

Robô que responde sozinho no WhatsApp é a primeira coisa que muita gente quer quando ouve "IA no atendimento". Faz sentido para resposta inicial, fora do horário, perguntas frequentes sobre o escritório e lembretes. Dois cuidados antes de ligar qualquer coisa automática:

- **Publicidade e ética.** Mensagem automática também é comunicação do escritório. O Provimento 205/2021 do CFOAB e o Código de Ética e Disciplina da OAB valem para o que o robô escreve tanto quanto para as redes sociais. Na prática: nada de promessa de resultado, nada de tom de oferta, nada de orientação jurídica para quem ainda não é cliente e nada de se apresentar como advogado. Na dúvida, o advogado lê o provimento inteiro antes de publicar o texto do robô `[CONFERIR]`.
- **Transparência.** Se a resposta é automática, o cliente precisa saber. A mensagem diz que é automática, diz quando uma pessoa assume e nunca usa nome de advogado como se fosse ele digitando. Quem está aflito e descobre depois que conversou com um robô perde a confiança no escritório inteiro.

**A porta da frente vem antes.** No começo, a IA entra no WhatsApp pela porta da frente: alguém copia a mensagem anonimizada para o Projeto do escritório no Claude, recebe a classificação ou o rascunho e decide. Ligar a IA direto no canal é um passo de automação: ele só faz sentido com o POP testado, a biblioteca aprovada e as regras de canal escritas, e é desenhado na `desenhar-automacao`. Recursos de resposta automática, etiqueta e transcrição variam conforme a ferramenta: conferir na configuração da conta.

## 6. Dado de cliente: o que sai antes de colar na IA

Para classificar ou rascunhar, a IA quase nunca precisa saber quem é o cliente. Anonimize antes e use conta profissional. Nada volta para o cliente sem revisão humana.

| Dado na mensagem | Troque por | Observação |
|---|---|---|
| Nome do cliente e de terceiros | Código do cliente ("Cliente 0231"), "Ex-cônjuge", "Empresa A", ou `[CLIENTE]` | O código permite voltar ao caso sem expor o nome. |
| CPF, RG, número de benefício | Retire | Para classificar ou rascunhar, a IA dispensa esses números. |
| Número do processo | "Processo do Cliente 0231" ou `[PROCESSO]` | O vínculo fica na planilha ou no software jurídico. |
| Endereço e telefone | Retire | Só volta no envio, pela pessoa. |
| Dado de saúde, de criança, de violência | Descrição genérica: "laudo médico", "filho menor" | Dado pessoal sensível pela LGPD (Lei 13.709/2018). Só entra quando a tarefa precisar, e só em conta profissional. |

Senha e credencial (gov.br, Meu INSS, banco) nunca são pedidas por mensagem e nunca entram na IA. Laudo completo, dado de criança ou adolescente e processo em segredo de justiça não entram, nem anonimizados, sem autorização expressa do responsável.
