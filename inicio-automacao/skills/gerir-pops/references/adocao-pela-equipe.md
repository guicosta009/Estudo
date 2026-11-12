# Adoção do POP pela equipe

Leia na rotina 7, quando uma versão 1.0 ou uma mudança de inteiro vai entrar em uso, ou quando alguém continua no jeito antigo. O roteiro para preencher está em `assets/implantacao-modelo.md`. A entrada da IA no escritório como um todo (piloto, reunião de lançamento, os cinco medos) é da `implantar-a-mudanca`; aqui fica a implantação de um POP específico.

## 1. Preparar o treino

Pergunte ao dono, uma por vez:
1. "Quem vai ser treinado? Funções e quanto cada um já usa IA."
2. "Quanto tempo vocês têm? O roteiro pede 15 minutos de apresentação e 30 a 45 de treino."
3. "Qual vai ser a data de virada, a partir da qual o jeito antigo deixa de valer?"
4. "O que muda em relação ao jeito de hoje? No máximo três pontos."

Leia o POP vigente (sem dado de cliente) e entregue:
1. **Roteiro da apresentação de 15 minutos,** em tópicos, começando pelo problema que o POP resolve.
2. **Um caso fictício completo para o treino,** realista para a área do escritório, sem nenhum dado real, com o resultado esperado em cada passo. Se o caso depender de requisito legal, marque `[CONFERIR]`. Se houver caso de teste guardado pelo `testar-pop`, use-o como base.
3. **Para cada passo S e A:** o que a pessoa confere no que a IA entregou e qual erro da IA é mais provável ali.
4. **Cinco perguntas de checagem** para o fim do treino, com a resposta certa.
5. **Rascunho das perguntas frequentes** com as dúvidas previsíveis.
6. **A mensagem para o grupo da equipe** anunciando a data de virada, no tom do código do escritório, sem tom de bronca.

Linguagem simples, sem jargão de tecnologia. Em algum ponto do treino, reforce três coisas: conta profissional, anonimização antes de colar documento e revisão humana antes de qualquer coisa sair do escritório. Não invente regra jurídica.

## 2. Mensagens prontas (adaptar ao tom do código)

**Data de virada (mudança de inteiro ou primeira versão):**
```
Pessoal, a partir de [DIA] o [PROCESSO] segue o POP-[SIGLA]-[NN] versão [X.Y].
O que muda: [até 3 pontos].
Onde está: [pasta] e o Projeto "[NOME]" no Claude. Abram uma conversa nova no Projeto a partir de [DIA].
O jeito antigo e o modelo antigo saem da pasta no mesmo dia.
Dúvida, falem com [DONO]. Toda dúvida vai para as perguntas frequentes.
```

**Ajuste pequeno (decimal):**
```
Ajuste no POP-[SIGLA]-[NN], agora versão [X.Y]: [o que mudou, em uma frase]. Vale a partir de hoje.
Se estiverem com uma conversa aberta no Projeto, comecem uma nova.
```

**Depois de um erro (sem apontar ninguém):**
```
Mudamos o passo [N] do POP-[SIGLA]-[NN] (versão [X.Y]): [o que mudou].
Motivo: um caso mostrou que [descrição do furo no processo, sem nomes].
A partir de [DIA], [o que cada um faz diferente].
```

## 3. Quem continua no jeito antigo

Vai acontecer, e quase sempre com alguém competente. Antes de cobrar, descubra o motivo. Pergunte ao titular ou ao dono, sem nome da pessoa: "O que ela faz no lugar do POP, e em que situação isso aconteceu?"

| Motivo | Como reconhecer | O que fazer |
|---|---|---|
| 1. O POP não cobre o caso dela | Ela encontrou uma exceção e resolveu do jeito que sabia | Agradecer. Registrar nas anotações de uso. Se fizer sentido, a exceção entra na próxima versão |
| 2. Ela não aprendeu direito | Faltou o treino ou a execução acompanhada | Refazer com ela, sozinha, num caso fictício. Sem plateia, a pessoa pergunta o que não perguntou na frente do grupo |
| 3. Ela acha o jeito antigo melhor | Ela explica por que, com argumento | Medir os dois jeitos lado a lado em dois ou três casos, contando tempo e erros. Se o antigo ganhar, o POP muda. Se o novo ganhar, a conversa fica mais fácil com o número na mesa |
| 4. É hábito | A mão vai sozinha para o modelo de sempre | Tirar o caminho antigo do alcance: modelo velho fora da pasta, POP como primeiro arquivo do Projeto do setor |

**Quando a conversa não resolve:** depois do motivo entendido e tratado, se a pessoa continua no jeito antigo, a conversa sobe para o titular, em particular, com o combinado escrito e uma data. Os medos por trás da resistência (perder o emprego, parecer incompetente, mais retrabalho, sigilo, falta de tempo) e o que dizer em cada um estão em `../../implantar-a-mudanca/references/resistencia.md`. O exemplo do titular também conta: se ele mesmo pula o POP, a equipe entende que o POP é opcional.

**O que nunca fazer:** expor no grupo quem não segue o POP; dar bronca por exceção que o POP não previa; cobrar antes de saber o motivo.

## 4. Por porte

| Porte | Quem conduz | Como fica a implantação |
|---|---|---|
| 2 a 5 pessoas | O dono do POP, com o titular presente na apresentação | Apresentação e treino no mesmo encontro; acompanhamento na reunião semanal com todos |
| 6 a 20 pessoas | O dono do POP, com o embaixador do setor | Treino por setor; o embaixador acompanha a primeira execução de quem ele não alcança |
| Mais de 20 | O dono do POP, com o responsável pela inovação | Turnos de treino por setor e área; perguntas frequentes centralizadas pelo dono |

## 5. Versão solo

A implantação é no próprio titular, e o adversário é a sexta-feira apertada.
1. **POP aberto na tela nas primeiras dez execuções,** marcando cada passo. O que não fez sentido vai para as anotações de uso.
2. **Data de virada própria:** no dia combinado, o modelo antigo sai da pasta e o prompt antigo é apagado. Se ele continua disponível, a mão volta para ele no primeiro dia de prazo fatal.
3. **Com secretária ou estagiário:** a pessoa executa uma vez só com o POP na mão e anota cada dúvida. É o treino dela e a revisão do POP ao mesmo tempo.
4. **Acompanhamento:** nas duas semanas seguintes, os primeiros minutos do bloco fixo semanal respondem às três perguntas (pulei passo? voltei ao jeito antigo? que dúvida apareceu?).
