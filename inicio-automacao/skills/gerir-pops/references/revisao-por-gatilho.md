# Revisão por gatilho: como preparar cada uma

Leia na rotina 4, depois de saber o que disparou a revisão. Cada gatilho tem uma preparação; a pauta de 20 minutos (`assets/revisoes-modelo.md`) é a mesma para todos. Nada aqui pede dado de cliente. Se o advogado colar POP, ata ou descrição de erro que cite caso real, avise, não repita o dado e siga com a versão anonimizada.

## 1. Revisão depois de um erro

A análise é do processo, sem procurar culpado. Pergunte, uma por vez:

1. "O que saiu errado, em que passo foi percebido e quem percebeu?" (sem nome de cliente: `[CLIENTE]`, `[PROCESSO]`, `[DOC]`)
2. "Chegou ao cliente, ao processo ou para fora do escritório?"
3. "Já aconteceu antes? Quantas vezes?"
4. "Algum passo com IA estava envolvido? Qual?" (se não souber, siga e marque `[A CONFIRMAR]`)

Não presuma fato que o advogado não contou. Se faltar informação para achar a causa, pergunte antes de propor.

**Localize a causa** em uma ou mais destas sete:

| Causa | Como reconhecer | Mudança típica no POP |
|---|---|---|
| Passo que não existe | O erro passou por um ponto onde ninguém olhava | Passo novo (sobe o inteiro) |
| Passo ambíguo | Duas pessoas leriam o passo de jeitos diferentes | Reescrever o passo com verbo e objeto claros |
| Passo S que deveria ser A | A IA produziu e ninguém conferiu antes de seguir | S sobe para A na hora (regra da `revisao-periodica`) |
| Passo A sem critério de conferência | A pessoa "revisou", mas não sabia o que conferir | Escrever o objeto da conferência no "Confere" |
| Exceção não prevista | O caso caiu fora do caminho principal | Exceção nova, "situação: o que fazer" |
| Entrada errada ou desatualizada | Modelo, documento da base ou prompt velho | Atualizar a entrada (`montar-base`) e conferir a troca no Projeto |
| Passo que a equipe pula | O passo existe, mas não é seguido | Descobrir o motivo (rotina 7) antes de mexer no texto |

**Depois, entregue para o advogado decidir:**
1. A menor mudança no POP que resolve a causa, mostrando só os passos alterados, no formato antes e depois, com a sigla de cada um.
2. Se a mudança sobe o decimal (basta avisar) ou o inteiro (precisa treinar de novo), e qual fica a versão nova.
3. A linha do controle de versões: versão, data, o que mudou, por quê.
4. A mensagem curta para a equipe explicando a mudança, sem apontar quem errou.
5. Se o erro expôs dado de cliente, perdeu ou arriscou prazo ou levou informação errada ao cliente: o aviso de que o caso vai ao guardião e ao livro de incidentes (`regra-de-uso-de-ia`), além da mudança no POP.

Todo erro termina com o POP alterado. Erro corrigido na hora com o POP igual é o erro que volta.

## 2. Revisão porque mudou a ferramenta ou a IA

Pergunte, uma por vez:
1. "O que mudou: plano, ferramenta, Projeto novo, a IA passou a responder diferente, ou um recurso novo que vocês querem usar?"
2. "Onde está o caso de teste guardado deste POP e o resultado que vocês consideram bom?" (na pasta `testes/` do setor ou em `04-base/casos-de-teste/`). Sem caso guardado, ofereça o `testar-pop` para montar um antes de continuar.
3. "Pode rodar o mesmo caso com a configuração nova e colar o que a IA entregou?"

**Entregue:**
1. A comparação entre o resultado esperado e o novo: o que melhorou, o que piorou, o que sumiu.
2. Os passos do POP que ficaram desatualizados, em especial os que descrevem a ferramenta em vez do resultado.
3. A reescrita desses passos pelo resultado esperado e pelo critério de conferência, sem nome de botão ou de tela.
4. Se alguma sigla deve mudar, com o motivo. Subir é imediato; descer fica como proposta para a trimestral.
5. Decimal ou inteiro, e a versão nova.
6. A linha do controle de versões.

Não afirme nada sobre recurso de ferramenta que você não tem certeza que existe. Quando depender da configuração, escreva "conferir na configuração da conta". Antes de usar com cliente, o caso de teste precisa voltar a dar o resultado esperado.

## 3. Revisão porque mudou a lei ou a regra

1. "O que mudou? Lei, entendimento, regra de tribunal ou de órgão, sistema de peticionamento?" Descreva pelo nome e marque `[CONFERIR]`: a skill não confirma norma de memória.
2. Liste os passos, exceções e prazos do POP afetados, e os documentos da base que o POP cita e que também mudam (modelos, checklists, tabela de prazos).
3. A revisão do POP e a da base andam juntas: ofereça a `montar-base` para os documentos. A versão nova do POP só é publicada quando os modelos que ela cita estão atualizados.
4. Mudança por lei ou regra sobe o inteiro.

## 4. Revisão porque chegou gente nova

1. Peça que a pessoa execute o POP só com o papel na mão, num caso fictício ou no primeiro caso real acompanhado, e anote cada dúvida.
2. Leia as dúvidas com o dono. Cada dúvida é um furo do POP, e a culpa nunca é de quem chegou.
3. Dúvida que se responde com uma linha vira explicação no passo (decimal). Dúvida que revela um passo faltando vira passo novo (inteiro).
4. Na equipe, confira também se a pessoa nova assinou o acordo de uso de IA antes de usar qualquer passo com IA (`regra-de-uso-de-ia`).

## 5. Revisão porque a equipe está pulando passo

Descubra o motivo antes de mexer no texto (rotina 7 da skill e `references/adocao-pela-equipe.md`). Só os motivos "o POP não cobre o caso" e "o jeito antigo é melhor, e a medição mostrou isso" mudam o POP. "Não aprendeu" pede treino. "Hábito" pede tirar o caminho antigo do alcance.

## 6. Revisão de calendário (data marcada)

Nenhum gatilho disparou. Rode a mesma pauta, com atenção ao bloco 1 (anotações de uso que se acumularam) e ao caso de teste rodado de novo: a IA pode ter mudado sem ninguém avisar. Se nada mudou, a decisão é manter a versão e marcar a próxima revisão. Isso também é resultado.

## 7. Solo: a IA como leitora crítica

Ninguém discute o POP do titular, e é aí que ele envelhece. Uma vez por revisão, peça à IA a leitura que um colega faria. Diga ao advogado que você vai ler o POP como se fosse a pessoa que chegou ontem e entregue:
1. Os passos em que essa pessoa precisaria perguntar algo ao titular.
2. As decisões do fluxo sem o caminho do "não".
3. Os passos com IA descritos pela ferramenta em vez do resultado.
4. Os "Confere" sem objeto (revisão que vira carimbo).
5. O que mudou na rotina do titular nos últimos meses e não aparece no POP (pergunte: "o que você faz hoje diferente do que está escrito?").

A leitura é proposta. O titular decide, depois de uma pausa de 24 horas quando a mudança sobe o inteiro.
