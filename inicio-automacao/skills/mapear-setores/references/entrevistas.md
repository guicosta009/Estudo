# Entrevistas do mapeamento (passo 3)

Leia no passo 3 do `mapear-setores`. Há três modos:

- **A. Roteiro de 15 perguntas** (trilha equipe): o advogado ou o responsável conversa com quem executa, 30 a 40 minutos por pessoa.
- **B. O colaborador responde direto ao Claude** (trilha equipe): a pessoa senta na frente do computador e o Claude conduz a conversa, uma pergunta por vez.
- **C. Auto-observação** (trilha solo): o titular responde sobre o próprio trabalho, com o registro de horas aberto ao lado.

Nos três, a regra é a mesma: **agora é retrato.** Ninguém propõe melhoria nem automação durante a entrevista.

## Antes de qualquer entrevista (modos A e B)

- Entreviste quem executa. Titular e assistente, separadamente. "O sócio descreve o setor como ele deveria ser. Quem executa conta como ele é."
- Explique o objetivo: ninguém está sendo avaliado.
- Marque horário. Entrevista no corredor vira conversa e some.
- Peça autorização se for gravar.

Durante:
- Peça para a pessoa mostrar na tela.
- Se a resposta vier genérica, peça o último exemplo real ("e na terça, como foi?").
- Anote as exceções, porque é nelas que o POP quebra.
- Não corrija na hora.

O que costuma aparecer: a planilha paralela, a ligação de toda sexta, o arquivo "modelos_FINAL_v3" na área de trabalho de uma pessoa só.

## A. Roteiro de entrevista (15 perguntas em 4 partes)

```
ROTEIRO DE ENTREVISTA · MAPEAMENTO DO SETOR [SETOR]
Pessoa: [FUNÇÃO]     Data: [DATA]     Duração: 30 a 40 minutos

ABERTURA (2 minutos)
"A gente está mapeando como o trabalho acontece de verdade, para decidir onde a IA vai
ajudar primeiro. Não tem resposta certa. Quanto mais real, melhor."

PARTE 1 · A ROTINA
1. Me conta como foi o seu dia ontem, do momento em que você abriu o computador.
2. Que tarefas você faz toda semana, sem falta?
3. E o que aparece só de vez em quando, mas toma muito tempo quando aparece?

PARTE 2 · CADA ATIVIDADE (repita para as principais)
4. O que faz essa tarefa começar? Quem pede ou o que avisa?
5. Me mostra na tela como você faz, do começo ao fim.
6. Quantas vezes por semana ela acontece? Quanto tempo leva cada vez?
7. De onde vem a informação e onde fica registrado o resultado?
8. Que modelo, planilha ou anotação você usa? É só seu ou o escritório inteiro usa?
9. O que acontece quando dá errado ou quando o caso foge do normal?

PARTE 3 · ONDE DÓI
10. Em que ponto você fica esperando alguém ou alguma coisa?
11. O que mais te interrompe durante o dia?
12. Que tarefa você faz que ninguém no escritório sabe que você faz?
13. Se você faltasse uma semana, o que pararia primeiro?

PARTE 4 · OLHANDO PARA A IA
14. Que tarefa você tiraria das suas costas amanhã, se pudesse?
15. Que tarefa você acha que precisa continuar com uma pessoa? Por quê?

FECHAMENTO (2 minutos)
"Obrigado. Vou organizar o que você contou e te mostrar a lista, para você corrigir o
que eu entendi errado."

ANOTAÇÕES
Atividades novas que apareceram:
Exceções:
Pontos de trava:
Modelos e planilhas citados:
```

Depois da conversa, o Claude pode organizar as anotações no formato de `atividades-<setor>.md` (veja `atividades-por-setor.md`) e o entrevistador mostra a lista à pessoa para corrigir.

## B. O colaborador responde direto ao Claude

Duas formas:

1. **Nesta conversa:** o advogado passa o teclado para a pessoa. Antes, o Claude confirma três dados (áreas de atuação, quantas pessoas, setor e função de quem responde) e então segue as regras abaixo, uma pergunta por vez.
2. **Em outra conversa:** o Claude entrega o texto abaixo, já preenchido, para a pessoa colar no Projeto do escritório no Claude (conta profissional ou de equipe). A pessoa devolve a tabela final, que entra em `atividades-<setor>.md`.

```
Você vai me ajudar a mapear as atividades de um setor do meu escritório de advocacia. Quem
vai responder às suas perguntas é a pessoa que executa esse trabalho no dia a dia.

Contexto:
- Escritório de [ÁREAS DE ATUAÇÃO], com [QUANTAS PESSOAS] pessoas.
- Setor que estamos mapeando: [SETOR]
- Quem responde: [FUNÇÃO DA PESSOA]

Regras da conversa:
1. Faça uma pergunta por vez e espere a resposta antes de seguir.
2. Comece pedindo que a pessoa descreva o dia de trabalho de ontem nesse setor, do começo
   ao fim.
3. Para cada tarefa que aparecer, pergunte: o que dispara a tarefa, quantas vezes ela
   acontece por semana, quanto tempo leva cada vez, de onde vem a informação, onde o
   resultado fica registrado, onde costuma travar e que exceções aparecem.
4. Pergunte também pelo tempo picado: mensagens de WhatsApp, ligações, procurar documento,
   interrupções.
5. Se a resposta vier genérica, como "cuido dos clientes", peça um exemplo concreto da
   última semana.
6. O objetivo é entender o trabalho. Mantenha o tom leve e sem julgar a pessoa.
7. Se a pessoa citar nome de cliente, número de processo ou dado de saúde, peça para trocar
   por uma descrição genérica e não repita o dado.

No final, entregue:
- Uma tabela com as atividades no formato verbo + objeto, com as colunas: atividade,
  gatilho, vezes por semana, minutos por vez, horas por semana estimadas, onde fica
  registrado, onde trava.
- A soma das horas por semana do setor, segundo esta pessoa.
- As exceções que apareceram.
- Os modelos, planilhas e anotações pessoais que ela usa.
- As perguntas que ficaram sem resposta, marcadas como [A CONFIRMAR].

Não proponha melhorias nem automações ainda. Agora é só o retrato de como é hoje.
Comece pela primeira pergunta.
```

As horas que a pessoa estima na entrevista servem para montar a lista. Para o ranking valem as horas medidas no registro (passo 4).

## C. Auto-observação: "eu respondo sobre mim" (trilha solo)

No escritório solo não há a quem entrevistar, e a validação de fora some. O risco troca de lado: sai a vigilância, entra o autoengano e o esquecimento. Por isso a auto-observação anda junto com o registro de horas: cada resposta é conferida com o que a planilha mostrou. "A memória costuma exagerar o tempo das tarefas chatas e encurtar o das tarefas de que a gente gosta."

O titular pode responder de uma vez, em 30 a 40 minutos no fim do segundo ou terceiro dia de registro, ou em duas sessões curtas. O Claude conduz, uma pergunta por vez, e para cada tarefa pede o mesmo detalhe do modo B (gatilho, vezes por semana, minutos por vez, de onde vem a informação, onde fica o resultado, onde trava, exceções).

```
AUTO-OBSERVAÇÃO · MAPEAMENTO DO ESCRITÓRIO SOLO
Data: [DATA]     Dias de registro já feitos: [N]     Duração: 30 a 40 minutos

ABERTURA
"Agora é retrato. Vale o que você fez de verdade nesta semana, não o que deveria ter feito.
Se a resposta não bater com o registro, o registro ganha."

PARTE 1 · A ROTINA
1. Como foi o seu dia ontem, do momento em que abriu o computador até fechar? Em que
   horário fez cada coisa?
2. Que tarefas você faz toda semana, sem falta? Em que dia e em que hora do dia elas
   costumam cair?
3. O que aparece só de vez em quando, mas come o seu dia quando aparece?

PARTE 2 · CADA ATIVIDADE (repita para as principais)
4. O que faz essa tarefa começar? Uma mensagem, uma publicação, um vencimento, a sua
   memória?
5. Em que hora do dia você faz? É a hora que você escolheu ou a hora em que a tarefa
   chegou?
6. Quantas vezes por semana ela acontece e quanto tempo leva cada vez? (Confira no
   registro antes de responder.)
7. De onde vem a informação e onde fica registrado o resultado?
8. Que modelo, planilha ou anotação você usa? Está num lugar em que outra pessoa, ou a
   IA, acharia sem você explicar?
9. O que acontece quando o caso foge do normal?

PARTE 3 · ONDE DÓI
10. O que fica para trás quando você faz essa tarefa?
11. O que mais te interrompe, e em que horário isso costuma acontecer?
12. Que tarefa você empurra para a noite ou para o fim de semana?
13. Se você ficasse uma semana fora (férias, doença, audiência em outra cidade), o que
    pararia primeiro e quem perceberia?

PARTE 4 · OLHANDO PARA A IA
14. Que tarefa você tiraria das suas costas amanhã, se pudesse? E se fosse contratar
    alguém, qual passaria primeiro?
15. Que tarefa precisa continuar com você? Por quê?

FECHAMENTO
"Vou organizar o que você contou e cruzar com o registro. Onde os dois discordarem, eu
mostro a diferença e você decide qual número vale."
```

Entrega da auto-observação: a mesma tabela do modo B, com duas colunas a mais, **"Hora do dia"** e **"O que fica para trás"**, e uma lista curta de diferenças entre o que o titular disse e o que o registro mostrou. Se houver estagiário ou secretária, essa pessoa pode responder ao roteiro A ou ao modo B sobre o trabalho dela: ela é a embaixadora do método.
