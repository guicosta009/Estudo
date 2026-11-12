# Retrato cultural (diagnóstico opcional antes do código)

Leia quando o advogado aceitar fazer o retrato no passo 1 do modo criar, ou quando pedir "como está a cultura do escritório". O retrato descreve como o escritório funciona hoje. Ele não julga ninguém e não propõe melhoria: a melhoria entra no código depois.

## Como conduzir

- Tempo: 30 minutos, sem celular, pensando na última semana normal (sem feriado, sem audiência fora do comum).
- Para cada tema, pergunte em qual coluna o escritório está hoje. Vale marcar o sinal de alerta "sem drama": é para isso que o retrato existe.
- Depois, faça a pergunta do tema e peça um exemplo real. Exemplo bom: "na terça, a assistente mandou a minuta e eu reescrevi tudo". Exemplo ruim: "a gente delega bem".
- Um tema por vez. Não dê nota durante a conversa; a leitura vem no fim.
- Nenhum nome de cliente. Pessoas da equipe pela função.

## Os 6 temas

| Tema | Sinal saudável | Sinal de alerta | Pergunta |
|---|---|---|---|
| Decisão | Dono conhecido e critério escrito para preço, aceite e acordo | Tudo espera o titular | "Qual foi a última decisão que esperou você sem precisar?" |
| Delegação | Quem recebe sabe o resultado, o prazo e onde está o modelo | Você refaz e, na próxima, faz você mesmo | "Quantas tarefas você refez na última semana, e por quê?" |
| Comunicação | Canal por assunto, a mesma resposta vem de qualquer pessoa | Tudo no WhatsApp pessoal | "Se você sumisse por uma semana, a equipe saberia o que cada cliente ouviu?" |
| Erro | Contado cedo, causa discutida, vira ajuste | Aparece quando o cliente reclama; a equipe esconde | "Qual foi o último erro que alguém te contou antes de você descobrir?" |
| Aprendizado | O jeito novo vira padrão | "modelos_FINAL_v3" e prompt guardado no próprio computador | "Qual foi a última coisa que alguém ensinou para a equipe?" |
| Dados e sigilo | Todos sabem o que vai para a IA, em qual conta e o que anonimizar | Cada um usa a conta que quer; documento vai com nome e CPF | "Você sabe em qual conta cada pessoa usa IA?" |

**Ponte para o código:**

| Tema fraco | Seção do código que recebe mais cuidado |
|---|---|
| Decisão | 3. Como decidimos |
| Delegação | 7. Como sabemos que foi bem feito (critério de entrega) e 3 |
| Comunicação | 2. Como atendemos e 4. Tom de voz |
| Erro | 7, e o livro de incidentes da `regra-de-uso-de-ia` |
| Aprendizado | Seção "Como manter o código vivo" (dono, lugar único) e a base (`montar-base`) |
| Dados e sigilo | 5. Dados e sigilo, e a `regra-de-uso-de-ia` logo depois |

## Checklist cultural (10 itens)

Marque o que é verdade hoje:

1. Quem decide o quê está escrito (preço, aceite, acordo, protocolo).
2. O prazo de resposta ao cliente está combinado e todos conhecem.
3. O tom está descrito com exemplos.
4. A tarefa delegada volta pronta na maioria das vezes.
5. Alguém contou um erro antes de você descobrir, nas últimas 4 semanas.
6. Os modelos estão num lugar só, com versão clara.
7. Existe uma reunião curta e fixa (mesmo que de 15 minutos por semana).
8. A equipe sabe o que pode ir para a IA.
9. Você usa IA toda semana em tarefa real.
10. Quem chega aprende sem depender só de você.

**Leitura:**
- 0 a 3 marcados: **Cultura na cabeça.**
- 4 a 7 marcados: **Cultura em construção.**
- 8 a 10 marcados: **Terreno pronto.**

Anote o tema mais fraco. Ele vira prioridade no código e, na trilha equipe, também na reunião de lançamento (`implantar-a-mudanca`).

### Leitura adaptada para a trilha solo

Adaptação do plugin para quem trabalha sem equipe. Use estas perguntas no lugar dos itens que dependem de outra pessoa:

| Item | Versão solo |
|---|---|
| 4 | Se há secretária ou estagiário: a tarefa delegada volta pronta? Se não há ninguém: você termina a tarefa na primeira vez, sem refazer no dia seguinte? |
| 5 | Nas últimas 4 semanas, você anotou um erro seu antes de o cliente ou o processo mostrar? |
| 7 | Existe um bloco fixo na semana para olhar o próprio trabalho (mesmo que de 20 minutos)? |
| 8 | Você tem escrito para você mesmo o que pode ir para a IA e em qual conta? |
| 10 | Se você contratasse alguém amanhã, essa pessoa conseguiria começar lendo o que está escrito? |

A leitura da pontuação continua a mesma.

## Trilha equipe: as mesmas perguntas a duas pessoas

1. Escolha duas pessoas de funções diferentes (por exemplo, uma da produção e uma do atendimento).
2. Entregue os 6 temas e o checklist por escrito, sem campo de nome. Elas devolvem sem identificação (envelope, caixa, formulário sem login). Combine que a resposta não entra em avaliação nenhuma.
3. Em escritório de 2 a 5 pessoas, o anonimato é frágil: diga isso a elas e peça respostas sobre o escritório, não sobre colegas.
4. Compare as três versões (titular e as duas pessoas) tema a tema. **A diferença entre as respostas é o dado mais valioso.** Onde o titular marcou saudável e a equipe marcou alerta, o código precisa de mais exemplo e mais regra escrita.
5. Não tente descobrir quem respondeu o quê. Se alguém se identificar por conta própria, não registre o nome.

A skill também pode receber as respostas coladas pelo titular e montar a comparação.

## Como gravar

Arquivo `escritorio/01-cultura/mudanca/retrato-cultural.md`:

```markdown
# Retrato cultural · [ESCRITÓRIO]
Versão: 1 · Data: AAAA-MM-DD · Dono: [FUNÇÃO]

| Tema | Titular | Pessoa A | Pessoa B | Exemplo real (sem nome de cliente) |
|---|---|---|---|---|
| Decisão | saudável / alerta | | | |
...

Checklist: [N] de 10 · Leitura: [Cultura na cabeça / em construção / Terreno pronto]
Tema mais fraco: [TEMA] → seção [N] do código
Maiores diferenças entre as respostas: [LISTA]
```

Na trilha solo, as colunas Pessoa A e Pessoa B saem.
