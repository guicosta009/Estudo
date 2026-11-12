---
name: implantar-a-mudanca
description: >
  Conduz a entrada da IA no dia a dia do escritório pela equipe: papel da liderança, adoção
  em etapas (0 a 4) com critérios de avanço e recuo, ficha do piloto, registro de usos e de
  prompts, reunião de lançamento de 50 minutos, conversa individual com quem resiste (com
  treino em que a IA faz o papel da pessoa), rituais e painel semanal da cultura. No solo,
  monta o piloto consigo mesmo. Use quando o advogado disser "como apresento a IA para a
  equipe", "quero começar um piloto", "minha equipe resiste", "reunião de lançamento",
  "a assistente não quer usar", "como faço a equipe adotar", "ficha do piloto", "o piloto
  deu certo, e agora?", "painel da semana". Não use para escrever o código ou a regra de uso
  (use codigo-do-escritorio ou regra-de-uso-de-ia) nem para nomear quem cuida da mudança
  (use nucleo-de-inovacao).
---

# Implantar a mudança

> A IA entra pela equipe. Esta skill organiza o primeiro uso de verdade: uma pessoa, um processo, duas semanas, medição e revisão, e só depois o setor inteiro.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha, níveis e escalas: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- O código do escritório e a regra de uso de IA já existem e o escritório quer começar a usar a IA em tarefa real, do mesmo jeito para todo mundo.
- O titular precisa preparar a reunião de lançamento com a equipe.
- Alguém da equipe está resistindo e o titular quer preparar e treinar a conversa individual.
- Um piloto terminou e é preciso decidir: avançar, ajustar ou parar.
- Chegou a hora do painel semanal da cultura ou de registrar um prompt validado.

**Não use quando:**
- Falta o código do escritório ou a regra de uso de IA: use `codigo-do-escritorio` ou `regra-de-uso-de-ia` antes.
- O pedido é definir quem é dono da mudança, montar a reunião semanal do núcleo ou o plano de 90 dias: use `nucleo-de-inovacao`.
- O pedido é escrever o POP completo do processo: use `escrever-pop` (esta skill só gera o rascunho na etapa 2 e entrega para lá).
- O pedido é calcular o retorno em reais: use `medir-retorno`.

## 2. Antes de começar

1. **Leia o perfil.** Abra `escritorio/perfil.md` (porte, trilha, setor-alvo, conta de IA). Leia também `escritorio/01-cultura/codigo-do-escritorio.md`, `escritorio/01-cultura/regra-de-uso-de-ia.md` e, se existir, o retrato cultural em `escritorio/01-cultura/mudanca/`: o tema mais fraco do retrato vira foco da reunião de lançamento. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão de entrada:** o código do escritório e a regra de uso de IA precisam existir. Sem régua escrita, ninguém consegue dizer se a entrega da IA está boa, e cada pessoa usa de um jeito ("quatro escritórios dentro de um"). Se faltar, explique isso em uma frase e ofereça `codigo-do-escritorio` ou `regra-de-uso-de-ia`. Se o advogado quiser seguir, siga e registre em "Etapas puladas" no `perfil.md`.
3. **Portão do piloto:** "Sem acordo assinado, ninguém começa." Antes do primeiro uso com tarefa real, confira em `escritorio/01-cultura/acordos/` o acordo assinado de cada pessoa que vai usar a IA (inclusive o titular). No solo, vale o autocompromisso. Este portão não se pula: sem acordo, a skill prepara tudo (ficha, reunião, conversas), mas o piloto só começa depois da assinatura.
4. **Conta de IA.** Se o perfil diz conta pessoal gratuita, o piloto roda só com dado fictício até a conta profissional estar conferida. Diga isso antes de montar a ficha.
5. **Descubra o momento.** Pergunte: "Em que ponto você está: vai começar agora, vai fazer a reunião com a equipe, tem alguém resistindo, está no meio do piloto ou vai fechar a semana?" Vá direto ao bloco do fluxo que corresponde.

## 3. Fluxo

### Passo 1. Combinar o papel da liderança (sempre, na primeira vez)
Mostre os cinco comportamentos da seção 4 e pergunte, um de cada vez:
- "Você já usou a IA por pelo menos uma semana em tarefa real sua?" Se não, essa é a primeira tarefa: o titular é o primeiro usuário.
- "Qual dia e horário fixo, sem telefone, vai ser o tempo protegido para testar?" Anote dia e hora. Sem horário fixo, a adoção vira "quando sobrar tempo".

### Passo 2. Etapa 0: escolher processo e pessoa e preencher a ficha do piloto
Use o modelo `assets/ficha-do-piloto.md`. Pergunte, uma por vez:
1. "Dentro do setor-alvo ([SETOR DO PERFIL]), que processo se repete toda semana e tem erro barato, que alguém percebe antes do cliente?" Se o escolhido for complexo ou de risco alto, avise: processo complexo demais faz a pessoa largar o piloto na primeira semana.
2. "Quem vai conduzir o piloto?" Peça a função. O critério é curiosidade e respeito da equipe. Não precisa ser a pessoa mais jovem nem a mais técnica.
3. "Quem acompanha?" (titular ou sócio).
4. "Qual é o horário protegido da pessoa do piloto, e quem cobre o telefone nesse horário?"
5. "Que ferramenta e qual conta?" Confira com a regra de uso de IA.
6. "O que a IA vai fazer nesse processo, e o que continua com uma pessoa?" Marque S ou A para o que a IA faz e H para o resto. Se houver dúvida, rode a árvore da `classificar-sah` só nesses passos. Nenhum passo da linha vermelha entra no piloto como S ou A.
7. "Que dados saem antes de ir para a IA?" Puxe da regra de uso de IA.
8. "Quem revisa antes de qualquer coisa sair, e o que essa pessoa confere?" Revisão sem objeto vira carimbo.
9. "Quanto tempo leva hoje, em minutos, cada vez que esse processo acontece?" É estimativa da própria pessoa. Para ter precisão, sugira cronometrar por uma semana antes do piloto (a `medir-retorno` usa esse número como linha de base).
10. "Qual dia, no fim da semana 2, vai ser a conversa de decisão?"

Mostre a ficha preenchida, ajuste e grave.

### Passo 3. Equipe: preparar a reunião de lançamento
Veja a seção 6. Esse passo vem antes do piloto começar.

### Passo 4. Etapa 1: rodar o piloto (2 semanas)
- Crie o registro de usos (seção 5.2) e explique: uma linha a cada uso, cerca de um minuto.
- Ajude a escrever o prompt de partida e a colocá-lo no Projeto do escritório, no Claude, junto com o código.
- A cada uso, a pessoa anota o tempo com IA (incluindo a revisão) e o que a revisão corrigiu.
- Equipe: na troca da semana, a pessoa do piloto conta um uso que funcionou e um que falhou.

### Passo 5. Fechar a etapa e decidir
No dia da conversa de decisão, leia o registro de usos e aplique os critérios de avanço e recuo da seção 5.1. Entregue a decisão proposta (avançar, ajustar ou parar) com os números do registro. Quem decide é o titular.

### Passo 6. Etapa 2: ajustar (1 semana)
Melhore o prompt com o que a revisão corrigiu. Marque S, A e H em cada passo do processo e escreva o rascunho do POP v1 com a IA. Entregue o rascunho para a `escrever-pop` completar os 12 campos. O prompt validado entra no registro de prompts (`assets/registro-de-prompt.md`).

### Passo 7. Etapas 3 e 4: ampliar e padronizar
Na ampliação, o setor todo usa o mesmo prompt e o mesmo POP. A pessoa do piloto ensina em dupla, longe do grupo. O ritual semanal acompanha. No padrão, o POP vai para o arquivo oficial em `escritorio/03-pops/`, quem chega aprende por ele e toda regra nova que apareceu vai para o código na próxima revisão. Depois, volte à etapa 0 com o próximo processo.

### Passo 8. Equipe: conversa individual com quem resiste
Veja a seção 7 e `references/resistencia.md`.

### Passo 9. Fechar a semana: painel semanal da cultura
Na troca de sexta, preencha `assets/painel-semanal.md` (seção 8). Cabe numa mensagem.

## 4. O papel da liderança

**Os cinco comportamentos:**
1. **Seja o primeiro usuário.** Pelo menos uma semana em tarefa real sua antes de pedir para alguém.
2. **Mostre o seu uso toda semana,** inclusive o que deu errado.
3. **Proteja tempo para aprender.** Bloco fixo (por exemplo, quinta à tarde) sem telefone, com outra pessoa cobrindo.
4. **Trate o erro de quem testa como acerto do processo.** Erro pego na revisão conta como mérito. Bronca por erro de teste ensina a esconder o uso.
5. **Decida com clareza:** ferramenta, conta, processo, quem conduz e prazo. "Usem aí" é decisão vaga e recria os quatro escritórios.

**Frases que atrapalham e o que dizer no lugar:**

| Atrapalha | Ajuda |
|---|---|
| "Usem a IA aí para ir mais rápido." | "Nas próximas duas semanas, a assistente vai testar a IA na triagem. Toda sexta a gente olha junto o que funcionou." |
| "Isso foi a IA? Tá errado." | "Que bom que a revisão pegou. O que a gente muda no prompt para não repetir?" |
| "Quem não se adaptar vai ficar para trás." | "Eu também estou aprendendo. Olha o que eu errei essa semana." |
| "Depois a gente vê o sigilo." | "Antes de qualquer teste, a gente fecha o acordo de uso." |
| "Quando sobrar tempo, vocês aprendem." | "Quinta, das 15h às 16h, é horário de teste. O telefone fica com outra pessoa." |

## 5. Adoção em etapas

| Etapa | Duração | O que acontece | Entregável |
|---|---|---|---|
| 0 Escolha | Reunião de 30 min | Processo do setor-alvo, repetitivo e de baixo risco. Pessoa curiosa e respeitada. | Ficha do piloto |
| 1 Piloto | 2 semanas | Uma pessoa, um processo, prompt de partida no Projeto. Anota o tempo comparado com antes e o que a revisão corrigiu. | Registro de usos |
| 2 Ajuste | 1 semana | Melhora o prompt, marca S, A e H em cada passo, rascunha o POP v1 com a IA. | Prompt validado no registro e rascunho do POP |
| 3 Ampliação | 2 a 4 semanas | O setor todo usa o mesmo prompt e o mesmo POP. A pessoa do piloto ensina em dupla. Ritual semanal acompanha. | Setor usando do mesmo jeito |
| 4 Padrão | A partir do segundo mês | POP no arquivo oficial, quem chega aprende por ele, regra nova vai para o código. Volta à etapa 0 com o próximo processo. | POP oficial e próximo processo escolhido |

Uma pessoa e um processo por vez. Três pilotos ao mesmo tempo é receita para nenhum terminar.

### 5.1 Critérios de avanço e de recuo

| Etapa | Avança quando | Recua quando | Para onde recua |
|---|---|---|---|
| Piloto | A pessoa usou em pelo menos metade das ocorrências e anotou o tempo | Parou na primeira semana (quase sempre o processo era complexo demais) | Etapa 0, com processo mais simples |
| Ajuste | O resultado é aproveitável na maioria das vezes e a revisão ficou mais curta do que fazer do zero | Revisar leva mais tempo do que fazer à mão | Rever o prompt ou trocar o processo |
| Ampliação | Pessoas diferentes chegam a resultados parecidos | Cada um adaptou o prompt do seu jeito | Etapa 2, para unificar o prompt |
| Padrão | O POP está escrito, aprovado e alguém novo segue sem perguntar | Só funciona com a pessoa do piloto presente | Etapa 3, com o POP reescrito |

Regra fixa ligada ao medo do retrabalho: se, por duas semanas seguidas, revisar levar mais tempo do que fazer à mão, o processo volta para a etapa de ajuste.

### 5.2 Registro de usos do piloto
Uma linha por uso, com ponto e vírgula, para abrir em planilha:

```
Data;Pessoa (função);Processo;Prompt usado;Minutos antes;Minutos com IA;Minutos devolvidos;Erro pego na revisão (sim/não);Qual erro;Para onde foi o tempo
```

- "Minutos antes" é a estimativa da ficha (ou o número cronometrado).
- "Minutos com IA" inclui o tempo de revisão. Sem isso, a conta mente.
- "Para onde foi o tempo" é obrigatório. Hora devolvida sem destino evapora.
- Nada de nome de cliente nem número de processo. Descreva a tarefa ("atualização de andamento, cliente de aposentadoria").

### 5.3 Registro de prompt
Todo prompt validado na etapa 2 entra numa biblioteca única, com os campos de `assets/registro-de-prompt.md`: nome curto, setor, processo, tipo (S ou A), para que serve, o que anonimizar antes, o prompt, o que sempre conferir na revisão, quem validou e quando, versão. Prompt guardado no computador de uma pessoa só é aprendizado que não circula.

## 6. Reunião de lançamento (equipe)

Roteiro completo, pauta e convite: `assets/reuniao-de-lancamento.md` e `assets/convite-reuniao.md`.

**Antes da reunião (confira cada item com o titular):**
1. O titular já usou a IA por pelo menos uma semana.
2. Existem o rascunho do acordo de uso e a ficha do piloto.
3. A demonstração está pronta, com dado fictício ou anonimizado e o prompt já no Projeto.
4. O titular conversou antes, em particular, com a pessoa do piloto.
5. O convite saiu com 2 a 3 dias de antecedência.

**Pauta de 50 minutos:**

| Minutos | Bloco | Conteúdo | Quem conduz |
|---|---|---|---|
| 0 a 5 | Por que agora | Uma cena real da semana passada | Titular |
| 5 a 12 | O que muda e o que fica | S, A e H; o que continua humano | Titular |
| 12 a 22 | Demonstração ao vivo | Tarefa real com dado anonimizado e pelo menos um erro pego pela revisão | Titular |
| 22 a 32 | Rodada de preocupações | Cada pessoa traz uma; anotar em lugar que todos vejam | Titular anota, todos falam |
| 32 a 40 | Acordo de uso | Leitura item a item, ajustes na hora, data de assinatura | Titular ou dono do código |
| 40 a 47 | O piloto | Processo, quem conduz, duração, medição, quando a equipe vê o resultado | Pessoa do piloto |
| 47 a 50 | Próximos passos | Data do primeiro ritual, prazo de assinatura, quem conversa com quem | Titular |

**Fluxo para preparar a reunião** (pergunte uma coisa por vez; o que já está no perfil ou na ficha, só confirme):
1. Áreas e número de pessoas, por função, sem nomes (do perfil).
2. "Como a equipe usa IA hoje: ninguém usa, cada um do seu jeito, ou alguns usam?"
3. Processo do piloto, função de quem conduz e duração (da ficha).
4. "Me conte um problema real da semana passada que mostra por que vocês precisam mudar." Sem dado de cliente.
5. "Qual é o seu maior receio sobre a reação da equipe?"

Se faltar alguma informação, pergunte antes de escrever. Não invente dado, número ou fato sobre o escritório. Use o código do escritório como régua de tom. Depois entregue:
1. O roteiro falado de cada bloco da pauta, em frases curtas que o titular consiga dizer com naturalidade, sem tom de palestra motivacional.
2. Uma demonstração de 10 minutos com uma tarefa real do processo do piloto, usando dados fictícios, com um ponto em que a revisão humana encontra um erro.
3. As cinco preocupações mais prováveis desta equipe e uma resposta honesta para cada, sem prometer nada que o titular não tenha dito.
4. Três perguntas para o fim da reunião, que mostram se todo mundo entendeu o que acontece a partir de segunda.

**Depois da reunião:** conversa individual de 15 minutos com cada pessoa em até uma semana; acordos assinados no prazo combinado; primeiro ritual na agenda.

## 7. Conversa individual com quem resiste (equipe)

Leia `references/resistencia.md` quando o titular trouxer um caso concreto. Lá estão os cinco medos, o que dizer em cada um, a regra escrita que responde a cada medo, o que nunca fazer e o fluxo completo de preparação e treino.

Resumo do fluxo:
1. Pergunte, uma por vez e sem nome: função e tempo de casa; o que a pessoa faz muito bem; o que ela disse ou fez, do jeito que aconteceu; o medo que o titular acha que está por trás (perder o emprego, parecer incompetente, retrabalho, sigilo, falta de tempo, não sei); o que o titular pode garantir de verdade; o que ele ainda não decidiu.
2. **Parte 1, preparar:** entregue uma abertura que não soe como bronca nem como discurso; três perguntas abertas para entender o medo real antes de falar; como responder a cada medo provável sem prometer o que não pode garantir; uma regra concreta para pôr no papel; um combinado pequeno com data.
3. **Parte 2, treinar:** quando o titular disser "vamos treinar", faça o papel da pessoa. Reaja como alguém desconfiado reagiria, sem facilitar. Depois de cinco trocas, saia do personagem e diga o que o titular fez bem e o que deveria mudar na conversa real.
4. Grave só a regra escrita adotada e o combinado, sem nome e sem o conteúdo da conversa.

## 8. Rituais e painel semanal da cultura

| Ritual | Quando | Duração | Quem | O que sai |
|---|---|---|---|---|
| Troca da semana | Sexta | 15 min | Revezamento na condução | Um uso que funcionou e um que falhou; o que funcionou vai para o registro de prompts |
| Registro de prompts | A cada prompt validado | 5 min | Quem validou | Biblioteca única atualizada |
| Horas devolvidas | A cada uso | 1 min | Quem usou | Linha no registro de usos, lida na troca |
| Celebração do mês | Última troca do mês | 10 min | Titular | Reconhece quem devolveu mais horas e quem pegou erro (as duas coisas contam como mérito) |
| Revisão do código | Primeira semana do mês | 30 min | Dono do código | Conduzida pela `revisao-periodica` |
| Integração de quem chega | Primeira semana da pessoa | 1 h | Pessoa de referência | Lê o código, assina o acordo, aprende os prompts do setor |

**Painel semanal da cultura** (`assets/painel-semanal.md`), preenchido na troca de sexta:
- Período.
- Pessoas usando IA em tarefa real: [N] de [TOTAL].
- Processos com prompt validado.
- Horas devolvidas e para onde foram.
- Erros pegos e o mais importante.
- Prompt novo no registro (ou "nenhum").
- Uma coisa a mudar na próxima semana.

**Como ler os indicadores da cultura:**
- Semanais: pessoas usando (quem parou de usar?); horas devolvidas (minutos ÷ 60, sempre olhando o destino); erros pegos (alto no começo é bom sinal, deve cair depois).
- Mensais: processos com IA (se parou no piloto, a ampliação travou); prompts no registro (se só uma pessoa registra, o aprendizado não circula); rituais cumpridos (o primeiro ritual cancelado mostra a prioridade real).
- Exemplo ilustrativo de um painel: 4 de 5 pessoas usando, 2 processos com prompt validado, 9 h devolvidas na semana, 6 erros pegos. Números de exemplo, sem valor de referência.

## 9. O que entrega e onde grava

Tudo em `escritorio/01-cultura/mudanca/`, com nome, versão, data e dono no topo:

| Arquivo | Conteúdo |
|---|---|
| `ficha-do-piloto-<processo>.md` | Ficha preenchida, com a etapa atual (0 a 4) e a decisão de cada fechamento |
| `registro-de-usos-<processo>.md` | O registro de usos em formato de tabela com ponto e vírgula |
| `registro-de-prompts.md` | A biblioteca única de prompts validados |
| `reuniao-de-lancamento.md` | Roteiro falado, demonstração, preocupações e respostas, perguntas finais e convite |
| `regras-da-mudanca.md` | As regras escritas adotadas para os medos da equipe, com data |
| `paineis-semanais.md` | Um painel por semana, o mais recente no topo |

Mostre cada documento antes de gravar. Ao fechar a etapa 4 do primeiro processo, marque no `perfil.md` o item "Mudança e núcleo" do progresso, se o núcleo também estiver de pé.

## 10. Trilha solo e trilha equipe

**Solo (versão curta).** Não há reunião de lançamento nem conversa de resistência. O que fica:
1. **Piloto consigo mesmo.** A ficha tem os mesmos campos, com "quem conduz" e "quem acompanha" iguais ao titular. Para compensar a falta de um segundo olhar: a conferência acontece em outro momento do dia (não logo depois de fazer), com um checklist curto do que conferir. A IA pode ser segundo olhar, sem transformar o passo em S por isso.
2. **Registro de usos.** O mesmo formato. No solo é o registro que mostra a verdade, porque não há outra pessoa para notar que a revisão está ficando maior que o ganho.
3. **Revisão no bloco fixo.** A decisão de avançar, ajustar ou parar acontece nos primeiros 20 minutos do bloco fixo semanal (veja `nucleo-de-inovacao`), por escrito. O painel semanal vira três linhas: horas devolvidas e destino, erro mais importante da semana, uma coisa a mudar.
4. **Autocompromisso.** O portão do piloto é o autocompromisso assinado pelo próprio titular.
5. **Pessoa de apoio** (estagiário ou secretária), se houver: é a embaixadora do método. Se ela for usar a IA, assina o acordo antes. Em vez da reunião, uma conversa curta de 15 minutos explicando o piloto e o que ela confere.
6. **Pensando na primeira contratação.** O registro de prompts e o POP que saem do piloto são o que permite contratar depois sem ter que explicar tudo de boca.

**Equipe (completa), ajustada por porte:**
- **2 a 5 pessoas:** todos participam da reunião de lançamento e da troca da semana. Cuidado com o titular conduzindo tudo e virando gargalo: a condução do piloto e da troca pode passar para a pessoa mais organizada, com o titular como patrocinador.
- **6 a 20 pessoas:** a reunião de lançamento é com todos, porque o acordo vale para todos. O piloto e a ampliação acontecem no setor-alvo, com o embaixador do setor. A troca da semana pode ser por setor, e o painel semanal junta os setores.
- **Mais de 20 pessoas:** sugestão a validar pelo escritório: um lançamento geral curto feito pelo patrocinador e reuniões de 50 minutos por área ou setor, conduzidas pelo comitê do núcleo e pelos embaixadores. O formato exato fica `[A DEFINIR]` pelo escritório.

## 11. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| "Usem aí" | Cada um usa de um jeito e ninguém mede | Ficha do piloto com processo, pessoa, prazo e medição |
| Começar sem acordo | Dado de cliente em conta errada | Portão do piloto: sem acordo assinado, ninguém começa |
| Processo complexo no piloto | A pessoa larga na primeira semana | Critério repetitivo e de baixo risco na etapa 0 |
| Vários pilotos ao mesmo tempo | Nenhum termina | Uma pessoa e um processo por vez |
| Bronca pelo erro de teste | A equipe esconde o uso | Erro pego na revisão conta como mérito |
| Expor quem resiste no grupo | A resistência vira oposição | Conversa individual preparada e treinada |
| Minutos com IA sem a revisão | Ganho que não existe | Revisão dentro do tempo com IA |
| Ampliar sem unificar o prompt | Volta a haver quatro escritórios | Critério de recuo da ampliação |

## 12. Próximo passo

- Se ninguém é dono da mudança ainda, ou o titular está acumulando tudo: `nucleo-de-inovacao`.
- Com o piloto fechado na etapa 2: `escrever-pop` para completar o POP v1 que saiu do ajuste.
- Se o setor-alvo ainda é provisório (veio só do diagnóstico): `mapear-setores` para confirmar.
- Para manter a troca da semana, o painel e a revisão do código acontecendo: `revisao-periodica`.
