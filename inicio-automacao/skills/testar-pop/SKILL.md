---
name: testar-pop
description: >
  Leva o POP do rascunho (0.1) até "aprovado para uso" (1.0) por uma esteira de qualidade: checklist de
  13 itens (quatro eliminatórios) com correção sugerida para cada falha, teste de mesa por quem
  não escreveu, teste com a IA em três casos (fácil, comum, difícil) com uma ficha por passo e
  caso, revisão por par e do titular, piloto de duas semanas com registro por execução e
  comparação com a linha de base. Revê as siglas S e A, sobe a versão (0.2, 0.3...) e registra cada
  teste. Use quando o advogado disser "meu POP está pronto?", "testar o POP", "teste de mesa",
  "testar o POP com a IA", "essa sigla aguenta?", "piloto do POP", "aprovar o POP", "o POP
  trava no caso real", "ninguém consegue seguir o POP". Não use para escrever ou reescrever o
  POP (use escrever-pop), para auditar riscos (use auditar-riscos) nem para testar a automação
  já desenhada (use desenhar-automacao).
---

# Testar o POP

> Põe o POP para funcionar antes de entregar à equipe e à automação: audita o texto, faz alguém que não escreveu executar, faz a IA executar os passos S e A em três casos, colhe dois olhares e roda duas semanas com casos reais. Sai com número na mão e com o POP aprovado, ou com a lista exata do que falta.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). S, A, H, linha vermelha, anatomia do POP e medição: `../../docs/glossario.md`. Solo e equipe: `../../docs/trilhas.md`. Pasta e nomes: `../../docs/pasta-do-escritorio.md`.

**A régua desta skill:** um POP funciona quando alguém que não escreveu consegue executar do gatilho à saída sem perguntar nada a quem escreveu. Uma pessoa trava e pergunta. A IA não trava: ela preenche o buraco do POP com um palpite e entrega com toda a segurança. Se o POP tiver buraco, a automação executa o buraco, rápido e todo dia.

## 1. Quando usar

**Use quando:**
- O `escrever-pop` gravou um POP na versão 0.1, status Rascunho, com S, A e H, e o próximo passo é saber se ele aguenta um caso real.
- O advogado pergunta "meu POP está pronto?" (modo rápido: só o checklist).
- A equipe recebeu o POP e continua perguntando no WhatsApp como faz.
- O escritório quer saber se a sigla de um passo aguenta (S continua S? A precisa virar H?).
- Um POP vigente está em revisão (rascunho da versão nova em `03-pops/<setor>/_em-construcao/`) e a mudança precisa passar pela esteira antes de virar a vigente.

**Não use quando:**
- Não existe POP escrito: use `escrever-pop`. Se o POP existe mas os passos não têm sigla: `classificar-sah`.
- O pedido é a leitura de risco (linha vermelha, sigilo, LGPD, publicidade, nota de risco): use `auditar-riscos`. As duas se complementam: esta pergunta "dá para executar?", aquela pergunta "é seguro executar assim?".
- O pedido é testar as instruções escritas para cada passo de uma automação contra os casos de teste da base: use `desenhar-automacao` (passos 6 e 7). Esta skill testa o POP como documento e a sigla de cada passo. A `desenhar-automacao` testa a automação.
- O pedido é publicar o POP, numerar, aposentar versão ou atualizar o mapa de POPs: use `gerir-pops`.

## 2. Antes de começar

1. **Leia o perfil** (`escritorio/perfil.md`): trilha, porte, áreas, conta de IA, setor-alvo. Leia também `escritorio/01-cultura/codigo-do-escritorio.md` e `regra-de-uso-de-ia.md`, se existirem: o código é a régua do critério "padrão do escritório" no teste com a IA. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão: precisa existir o POP com S, A e H** em `escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md`. Na revisão de um POP vigente, o arquivo testado é o rascunho em `escritorio/03-pops/<setor>/_em-construcao/`, e a vigente continua valendo até a `gerir-pops` publicar a nova. Sem POP: "Não há o que testar ainda. O teste mostra onde o texto falha, e o texto precisa existir." Ofereça o `escrever-pop`.
3. **Onde o POP está na esteira.** Abra `escritorio/03-pops/<setor>/testes/` e o "Registro de revisão e aprovação" no fim do POP. Se já houver checklist, teste ou piloto, diga o que foi feito e retome da etapa seguinte.
4. **Conta de IA.** Teste com a IA e piloto com caso real anonimizado só em conta profissional ou de equipe, com o tratamento de dados conferido. Conta pessoal: os testes usam só caso fictício, e todo passo que toca dado de cliente fica A até a conta profissional estar ativa. Diga isso antes do passo 4.
5. **Linha de base antes do piloto.** Procure `escritorio/06-medicao/linha-de-base-<setor>.md`. Se não existir, avise já no começo: o setor precisa de cinco dias úteis registrados do jeito antigo antes do piloto começar, senão o "antes" se perde. Ofereça a `medir-retorno` para isso, em paralelo às etapas 1 a 4.
6. **Dados.** Os testes usam caso real anonimizado ou caso fictício, e nada do que a IA produzir em teste vai para cliente ou tribunal. Se o advogado colar um caso com nome, CPF, número de processo, benefício ou dado de saúde, avise, não repita e siga com a versão anonimizada (tabela de troca das regras transversais). Laudo completo, dado de criança ou adolescente e processo em segredo de justiça não viram caso de teste.
7. **Modo rápido.** "Meu POP está pronto?": rode só o passo 2 e devolva o veredito em uma tela, com os itens que falham e a correção de cada um. Ofereça a esteira completa no fim.

## 3. A esteira

As etapas seguem esta ordem. Cada uma tem um arquivo em `testes/` e cada ajuste aceito sobe a versão do POP (seção 10).

| # | Etapa | Quem faz | Tempo (referência) | O que mostra |
|---|---|---|---|---|
| 1 | Checklist de qualidade | A skill, com o autor | uns 30 min | Onde o texto falha |
| 2 | Teste de mesa | Quem não escreveu, observado pelo autor | menos de 1 hora | Onde o texto trava uma pessoa |
| 3 | Teste com a IA | Quem vai revisar os passos | poucos minutos por ficha | Onde a sigla aguenta |
| 4 | Revisão por par e do titular | Um colega e o titular | uma leitura cada | Se o POP deve funcionar desse jeito; o titular aprova o piloto |
| 5 | Piloto | Dono do POP, executores, titular | duas semanas | Se aguenta a rotina; os números do antes e depois |
| 6 | Fechamento e aprovação | Titular, com a revisão por par de novo | uma conversa | Passo a passo: manter, ajustar ou voltar a sigla. POP aprovado para uso |

Quem está atrasado faz primeiro o checklist e o teste de mesa: eles já entregam a lista do que falta escrever, que é a matéria-prima da `montar-base`. O teste com a IA e o piloto vêm logo depois.

## 4. Fluxo

### Passo 1. Abrir o POP e combinar o caminho
Leia o POP inteiro uma vez, sem corrigir nada. Diga ao advogado, em três linhas: quantos passos, quantos S, A e H, e em que etapa da esteira ele está. Pergunte: "Quer fazer a esteira inteira agora ou só a próxima etapa?" Uma etapa por conversa é normal: entre o teste de mesa e o piloto passam dias.

### Passo 2. Checklist de qualidade
1. **Sinais rápidos.** Confira os oito sinais de POP que ninguém consegue seguir (`assets/checklist-modelo.md`): escrito para quem já sabe, responsável genérico, passo sem verbo, só o caminho feliz, "usar IA" como passo, sem ponto de chegada, comprido demais, sem versão nem dono. Dois ou mais: diga que o checklist vai resolver a maior parte antes de qualquer teste.
2. **Teste dos dois minutos (equipe, opcional).** Sugira entregar o POP a alguém da equipe por dois minutos e fazer quatro perguntas: o que faz esse processo começar? Quem faz o primeiro passo, e o que entrega para o segundo? Como você sabe que o processo terminou? O que nunca sai daqui sem alguém conferir, e quem confere? Erro ou hesitação mostra onde mexer.
3. **Os 13 itens** (seção 5). Para cada um: situação (ok, parcial, falta), o trecho do POP que comprova ou que falha (copiado) e a correção sugerida. Reescreva só o trecho que falha. Depois, as três conferências complementares, a lista dos passos para reescrever e as siglas a rever (proposta, pela árvore da `classificar-sah`; na dúvida, a mais humana). Roteiro detalhado: `references/roteiros.md`, seção 1. Exemplos de "como está e como fica": `references/erros-comuns.md`.
4. **Veredito.** Item (E) parcial ou em falta: VOLTA PARA AJUSTE. Os quatro (E) completos: PRONTO PARA O TESTE DE MESA, mesmo com itens não eliminatórios em `[A DEFINIR]`, desde que se saiba exatamente o que falta. O teste costuma responder essas pendências.
5. **Correções.** Pergunte quais correções o advogado aceita. A skill não decide nenhuma. As aceitas entram no POP marcadas `[ALTERADO]` ou `[NOVO]`, com versão nova. Mostre antes de gravar. Grave `testes/checklist-<sigla>-<nn>-AAAA-MM-DD.md`.

### Passo 3. Teste de mesa
Uma pessoa que não escreveu o POP executa um caso real, no papel, seguindo só o que está escrito. Pergunte, uma de cada vez:
1. "Qual caso que já aconteceu, comum, já executado ou encerrado, pode servir de teste?" Evite o mais fácil da pasta: ele passa em qualquer POP. O caso tem a referência do que foi feito de verdade.
2. "Quem vai executar?" O melhor executor é quem vai rodar o POP no dia a dia. O segundo melhor é alguém que nunca fez esse processo. O autor nunca executa o próprio teste. Solo: veja a seção 12.
3. "O caso já está anonimizado?" Confira com o advogado o que sai (nome vira "Cliente A"; CPF, benefício, processo, endereço, telefone e nome de terceiros saem) e o que fica (tipo de pedido, datas relevantes, documentos que existem e que faltam).

Depois, entregue o roteiro ao observador, com a ficha `assets/teste-de-mesa-modelo.md`:
- O executor recebe só o POP, o caso e os modelos, listas e critérios que o POP cita. Sem explicação antes. Modelo citado que não existe por escrito já é o primeiro achado.
- O autor observa e anota, calado. Se o executor perguntar, responde para o teste não travar e registra a pergunta. **Cada pergunta é um defeito do POP.**
- Do gatilho à saída, no papel. Nos passos S e A, o executor descreve o que pediria à IA e o que espera receber. Nada é enviado a ninguém.
- Hora de início e fim de cada passo.

Quando o advogado trouxer a ficha preenchida (ou contar como foi), consolide pelo que observar e pelo critério da seção 6, proponha um ajuste para cada achado e mostre o veredito. Ajustes aceitos sobem a versão (0.1 para 0.2). Se mudou muita coisa, repita com outro caso e outro executor antes do teste com a IA. Grave `testes/teste-de-mesa-<sigla>-<nn>-AAAA-MM-DD.md`.

**Ensaio opcional, antes da pessoa:** a skill pode ler o POP como quem acabou de chegar, com um caso fictício (`references/roteiros.md`, seção 2). Mostra lacunas, mas não substitui o teste com uma pessoa, porque a IA completa com bom senso o que a pessoa nova não saberia completar.

### Passo 4. Teste com a IA
A IA executa os passos S e A com três casos de dificuldade diferente e o resultado é comparado com o que uma pessoa fez nesses mesmos casos. Pergunte, uma de cada vez:
1. "Em que ambiente a IA vai rodar quando o POP estiver em uso?" Monte o teste nesse ambiente: um Projeto no Claude (ou equivalente) em conta profissional, com o código do escritório, o POP e os modelos e listas que ele cita, ou a pasta do escritório aberta com o `escritorio/CLAUDE.md`. Testar num chat solto, sem contexto, mede outra coisa. Sem código no ambiente, o critério "padrão do escritório" fica "não medido" e a ficha diz isso.
2. "Quais são os três casos, e o que uma pessoa fez em cada um?" Fácil, comum e difícil (seção 7), anonimizados do mesmo jeito. Faltando caso real ou o caso difícil, gere casos fictícios com gabarito (`references/roteiros.md`, seção 3).
3. "Quem roda os passos: você, numa conversa nova do Projeto, ou eu, aqui?" O melhor é a pessoa rodar no Projeto, porque esta conversa já conhece os casos. Se a skill rodar, ela roda cada passo **antes de ver a referência humana daquele caso**, usa só a instrução do POP e o que ele cita, e declara o que consultou.

Regras do teste:
- Copie a instrução do passo como está no POP. Se foi preciso explicar mais para a IA acertar, anote: a instrução está fraca, e a automação vai ter só o que está no POP.
- Rode cada passo S duas vezes no mesmo caso. Se as saídas divergem em conteúdo (e não só em redação), o passo ainda não está pronto para rodar sem conferência.
- Cronometre execução e revisão separadas, e compare com o tempo da pessoa no caso real. Revisão faz parte do custo do passo.
- Uma ficha por passo e por caso (`assets/teste-com-ia-modelo.md`). Três casos com dois passos S e três passos A dão 15 fichas. Cada uma leva poucos minutos, e é ela que justifica a sigla na revisão do titular.
- Compare pelos critérios da seção 7 (roteiro em `references/roteiros.md`, seção 4). O trabalho humano é a referência, mas pode ter erro: se a IA pegou algo que a pessoa deixou passar, registre. Às vezes isso revela um passo de conferência que faltava no POP.

Feche com o resumo por passo e a decisão proposta pela tabela da seção 7. **Na dúvida, a sigla sobe.** O advogado decide cada uma. Mudança aceita vai para o POP com `[ALTERADO]` ou `[NOVO]` e versão nova: sigla do passo, exceção com o sinal que identifica o caso difícil, item novo em "Nunca sai sem revisão humana", instrução reescrita em "Onde a IA entra". Grave `testes/teste-com-ia-<sigla>-<nn>-AAAA-MM-DD.md`.

### Passo 5. Revisão por par e do titular (antes do piloto)
O teste mostra se o POP funciona. A revisão mostra se ele deve funcionar desse jeito. Pergunte: "Quem lê como par, e quem é o titular que aprova?" Entregue a cada um as perguntas da seção 8 e o checklist. Se existir relatório da `auditar-riscos`, o titular lê junto. Se não existir e o POP toca dado sensível, mensagem ao cliente ou conteúdo público, ofereça rodar a `auditar-riscos` antes do piloto.

Registre no fim do POP o bloco `assets/registro-de-revisao-modelo.md` (testes feitos, revisão por par, revisão do titular). Decisão do titular: APROVADO PARA O PILOTO, APROVADO COM RESSALVAS ou DEVOLVIDO. Devolvido volta à etapa que a revisão apontar.

### Passo 6. Piloto de duas semanas
O POP roda com casos reais. A automação ainda não entra: a pessoa leva a instrução do POP até a IA, dentro do Projeto, e registra cada execução. Prepare a ficha `assets/piloto-modelo.md` perguntando, uma de cada vez:
1. "Quem executa, quem revisa os passos A e quem decide no fim?"
2. "O que fica fora do piloto e continua no fluxo antigo?" (exemplo: prazo fatal no mesmo dia)
3. "A linha de base do setor está registrada?" Se não, o piloto espera os cinco dias do jeito antigo.
4. Equipe: "Todos que vão participar assinaram o acordo de uso de IA?" Sem acordo, ninguém começa (`regra-de-uso-de-ia`).
5. "Quando começa a semana 1?" Combine em marco relativo ("no próximo dia útil cheio") e grave a data real.

Rotina (detalhes na seção 9): conversa de abertura (dia 0, 30 minutos), registro por execução todo dia, conversa do fim da semana 1 (20 minutos) com a versão nova para a semana 2, semana 2 com a versão ajustada, fechamento. Durante o piloto, a skill ajuda a ler o registro, aponta quando ajustar e quando voltar atrás, e na semana 2 propõe o erro plantado. Grave `testes/piloto-<sigla>-<nn>.md` e atualize o mesmo arquivo a cada semana.

Se o escritório está no piloto da `implantar-a-mudanca` com este mesmo processo, não rode dois pilotos: o registro daqui serve aos dois, e a ficha de lá aponta para este arquivo.

### Passo 7. Fechamento: medir e decidir
1. **Consolide o registro.** Rode `python3 scripts/analisar_piloto.py escritorio/03-pops/<setor>/testes/piloto-<sigla>-<nn>.md --antes <min> --retrabalho-antes <%> --execucoes-mes <n>` (caminho do script relativo à pasta desta skill; ele lê as linhas com tabulação do próprio arquivo do piloto). Sem Python, faça as contas da seção 9 à mão e mostre cada uma. Roteiro da análise: `references/roteiros.md`, seção 5.
2. **Compare a semana 2 com a linha de base**, igual com igual (seção 9). Diga se o tipo de caso mudou entre os períodos.
3. **Procure carimbo** e confira o resultado do erro plantado.
4. **Recomende por passo S e A:** manter, ajustar a instrução, completar a base ou subir a sigla, com o número que sustenta. Responda: os passos S e A estão prontos para seguir à automação? Sim, sim com ressalvas ou não. Erro que chegou ao cliente ou ao tribunal: não, até a causa estar corrigida e testada.
5. **Segunda revisão por par e decisão do titular**, passo a passo. Preencha "Fechamento do piloto" no registro de revisão.

### Passo 8. Aprovar para uso e subir a versão
1. Aplique no POP as mudanças aceitas no fechamento, com `[ALTERADO]` e `[NOVO]`, e mostre o POP inteiro.
2. Defina a versão aprovada pela regra da seção 10 (1.0 na primeira aprovação; 1.x ou 2.0 na revisão de um POP vigente) e acrescente a linha no "Controle de versões" do POP, com as seis colunas: Versão, Data, O que mudou, Por quê, Quem aprovou, Equipe avisada ou treinada em (esta última fica em branco até a `gerir-pops` publicar).
3. Preencha "Aprovação para uso" no registro de revisão, com a próxima revisão em marco relativo ("na revisão trimestral", "depois de 4 semanas de uso").
4. Leve as pendências de base para a tabela "O que a IA vai precisar consultar" do POP (seção 11).
5. Só depois do ok, grave o POP e atualize o `perfil.md`.
6. Avise: "O POP está aprovado para uso, mas ainda não é o vigente. Rode a `gerir-pops` para publicar esta versão, tirar a anterior do Projeto e atualizar o mapa de POPs."

## 5. Checklist de qualidade: os 13 itens

(E) = eliminatório. A coluna da direita mostra o texto que reprova.

| Item | Como verificar | Sinal de reprovado |
|---|---|---|
| 1. Objetivo em uma frase | Lido em voz alta, cabe numa frase e diz o resultado para o cliente ou para o escritório | "Organizar o setor de peças." |
| 2. Gatilho definido | Um acontecimento que dá para observar: mensagem nova, publicação, contrato assinado, data fixa | "Quando necessário." "Sempre que possível." |
| 3. Entradas listadas | Tudo que precisa estar disponível, inclusive o que a IA consulta, com nome e lugar | "Documentos do cliente." "Modelo padrão." |
| 4. (E) Cada passo com verbo e responsável | Todo passo começa com verbo de ação e diz quem executa e quem confere, por nome ou função | "Petição." "Equipe revisa." |
| 5. Critério de pronto | Cada passo diz como se sabe que terminou, em especial os passos A | "Revisar a minuta", sem dizer o que se confere |
| 6. (E) S, A ou H justificado | Cada sigla tem uma linha de motivo pelos seis critérios da `classificar-sah`, e todo passo da linha vermelha é H | Sigla sem motivo, ou quase tudo S |
| 7. Exceções cobertas | Cada decisão do fluxograma tem o "e se não?" escrito, e as exceções dos últimos meses aparecem | Nenhuma exceção, ou "casos especiais: falar com a Dra." |
| 8. Prazo | Do gatilho à saída, mais os prazos internos das etapas críticas, coerentes com o código do escritório | "O mais rápido possível." |
| 9. Saída | O que foi entregue, para quem e onde ficou registrado | O POP termina no último passo, sem dizer o que existe no final |
| 10. (E) Onde a IA entra | Para cada passo S e A: o que a IA faz, o que consulta, em que ambiente roda e o que se anonimiza antes | "Usar IA para ajudar." |
| 11. (E) Nunca sai sem revisão humana | Lista curta e específica, com quem revisa e o que confere em cada item | "Revisar tudo." Ou o campo em branco |
| 12. Indicador | Um ou dois números com fórmula e fonte, e a linha de base registrada ou com marco para medir | "Melhorar a eficiência." |
| 13. Dono e versão | Nome do dono, versão, data e data da próxima revisão | Arquivo "POP_final_agora_vai" sem data |

**Conferências complementares** (vêm da lista "o POP está pronto?" e não eliminam sozinhas): o fluxograma existe e bate com o texto; as exceções cobrem no mínimo falta de documento, urgência e notícia ruim; o campo "Dados pessoais e sensíveis" diz em que passo e como anonimizar. O último item daquela lista ("quem executa leu e conseguiu seguir sem perguntar") é o teste de mesa.

## 6. Teste de mesa: o que observar e quando aprova

| O que observar | O que costuma ser | Ajuste típico |
|---|---|---|
| Onde parou, releu ou voltou | Verbo vago ou falta de critério de pronto | Reescrever o passo com verbo, objeto e "pronto quando" |
| Onde interpretou diferente | O texto permite duas leituras, e a IA vai escolher uma sem avisar | Reescrever com uma leitura só |
| Informação buscada fora do POP | Arquivo aberto, critério perguntado, lista procurada | Vira entrada do POP com nome e lugar, e pendência para a `montar-base` |
| Passo pulado ou fora de ordem | Inverteu e deu certo: a ordem do POP pode estar errada. Pulou e deu errado: o passo precisa ficar visível | Reordenar ou destacar o passo |
| Exceção sem resposta | Situação do caso que o POP não cobre | Exceção escrita, com o que fazer e quem decide |
| Tempo por passo | O passo que consome metade do teste | Dividir o passo, ou candidato à ajuda da IA |

**Critério de aprovação:** o executor chegou à saída certa sem perguntar o que fazer. Pergunta sobre um dado que sumiu na anonimização não conta. Pergunta sobre como fazer, quem decide ou qual modelo usar conta sempre. Exemplo resolvido em `references/exemplos-resolvidos.md`, seção 1.

## 7. Teste com a IA: casos, comparação e decisão

**Os três casos:**

| Dificuldade | O que é | O que mostra | Exemplo em peças | Exemplo em WhatsApp |
|---|---|---|---|---|
| Fácil | O caso de manual: documentos completos, sem exceção, cliente sem pressa | Se a IA acerta o básico e o padrão do escritório | Aposentadoria por idade urbana com CNIS completo e documentação na pasta | Cliente pergunta do andamento e a última movimentação é despacho de mero expediente |
| Comum | O que mais aparece, com uma ou duas variações | Se a IA funciona no volume real | Benefício por incapacidade com laudos de médicos diferentes | Juntada de laudo pericial, e o cliente quer saber se é bom ou ruim |
| Difícil | Informação faltando, documento conflitante ou notícia ruim | Se a IA sabe parar e passar para uma pessoa | CNIS com vínculo em aberto e um documento faltando | Sentença de improcedência publicada, e o cliente perguntando às 22h |

**O que comparar:**

| Critério | Pergunta | Exemplo de falha |
|---|---|---|
| Correção | Fatos, datas, valores e nomes conferem com o material do caso? | Data do requerimento trocada pela data da perícia |
| Completude | Falta algo que a pessoa incluiu no trabalho de referência? | Pedido subsidiário que o escritório sempre faz ficou de fora |
| Padrão do escritório | Segue o modelo, a estrutura e o tom do código do escritório? | "Prezado Senhor" num escritório que trata o cliente por você |
| Invenção | Trouxe fato, norma ou jurisprudência que não estava no material? | Ementa citada que ninguém encontra. Qualquer invenção reprova o passo como S |
| Saber parar | No caso difícil, a IA sinalizou que precisava de uma pessoa? | Escreveu a notícia da improcedência como se fosse rotina |
| Tempo | IA mais revisão levou menos que a pessoa sozinha? | Revisão de 50 minutos numa peça que a advogada fazia em 60 |

**Do resultado à decisão:**

| Resultado | Decisão |
|---|---|
| Passou nos três casos, só com ajuste de forma | Mantém a sigla. Registra na ficha e segue para a revisão |
| Passou no fácil e no comum, falhou no difícil | Mantém a sigla para os casos comuns e cria uma exceção: caso com aquela característica sobe para A ou H. Escreve o sinal que identifica o caso difícil |
| Falhou no caso comum | Reescreve a instrução do passo ou completa o que a IA consulta, e testa de novo. Falhou outra vez: a sigla sobe (S para A, A para H) |
| Inventou fato, norma ou jurisprudência | O passo sai de S. Fica A com conferência obrigatória daquele ponto, que entra em "Nunca sai sem revisão humana" |
| Duas rodadas, duas respostas diferentes | Fica A até a instrução ficar fechada o bastante para as rodadas coincidirem |
| Revisão demorou quase o mesmo que fazer do zero | O passo não ganhou nada. Divide em dois passos menores ou deixa como H por enquanto |

Passo da linha vermelha não entra no teste como S ou A: é H, e a IA no máximo prepara o material em volta. Exemplo resolvido: `references/exemplos-resolvidos.md`, seção 2.

## 8. Revisão por par e do titular

São duas leituras, por pessoas diferentes, em dois momentos: depois dos testes (antes do piloto) e no fechamento do piloto.

**Par.** Um colega do mesmo nível, ou alguém do setor que entrega trabalho para este ou recebe dele. Olha clareza, ordem dos passos, encaixe com os setores vizinhos e se as fichas sustentam as siglas:
- Eu executaria isso numa segunda-feira cheia, sem perguntar?
- O que este POP recebe do setor anterior bate com o que aquele setor entrega?
- Algum passo depende de uma pessoa específica que pode faltar?
- As fichas mostram teste com caso difícil?
- Tem passo que a gente faz e o POP não mostra?

**Titular.** O sócio ou o advogado responsável pela área, quem assina e responde pelo trabalho. Olha risco e responsabilidade, decide se o POP vai para o piloto e, no fim, se os passos S e A seguem para a automação:
- Os passos H são mesmo todos os que exigem decisão, julgamento ético, conversa delicada ou assinatura?
- A lista do que nunca sai sem revisão cobre prazo, notícia de decisão, valor e citação?
- O caminho do dado de cliente respeita o sigilo profissional e a LGPD (Lei 13.709/2018)?
- O tom das mensagens segue o código do escritório? Se algo é público, respeita o Provimento 205/2021 do CFOAB `[CONFERIR]`?
- Eu assinaria o que sair deste POP sem ter visto cada execução? (resposta por escrito)

## 9. Piloto: rotina, o que medir e medição antes e depois

**Participantes:** o dono do POP, que conduz e consolida; uma ou duas pessoas que executam; o titular, que revisa os passos A e decide no fim. **Escopo:** um POP, um setor, só os casos que entrarem no período, com o que fica fora combinado antes. **Regra de mudança:** ajustes entram no fim de cada semana, com versão nova (por exemplo, 0.4 para a semana 2). Mudar o POP todo dia impede saber o que funcionou. Erro crítico corrige na hora. **Registro:** uma linha por execução, preenchida na hora, em até dois minutos. Registro feito na sexta, de memória, sai bonito e inútil.

**Rotina:**
- **Dia 0, conversa de abertura (30 min):** apresentar o POP, mostrar o registro, combinar o que fica fora. Dizer que o piloto mede o POP e ninguém está sendo avaliado. Se alguém achar que está sendo vigiado, o registro sai maquiado.
- **Todo dia:** quem executa preenche a linha; quem revisa anota o que corrigiu, com o tipo do erro.
- **Fim da semana 1 (20 min):** o que travou, o que se repetiu, o que alguém fez diferente do POP e por quê. Sai a versão nova para a semana 2.
- **Semana 2:** roda a versão ajustada. É a semana que vale para a comparação, porque a curva de aprendizado ficou na semana 1.
- **Fechamento:** passo 7.

**O que medir:**

| Indicador | Como medir | Para que serve |
|---|---|---|
| Tempo por execução | Minutos de execução mais minutos de revisão, por caso | É o número que se compara com a linha de base |
| Retrabalho | Execuções que voltaram depois de dadas como prontas ÷ total de execuções | Ganho de tempo que volta como retrabalho é ganho falso |
| Erros pegos na revisão | Quantidade e tipo: fato, data ou prazo, valor, tom, invenção, dado sensível | Mostra a revisão funcionando e qual instrução precisa melhorar |
| Erros que passaram | Erros que chegaram ao cliente ou ao tribunal | Meta zero. Um só já é motivo para voltar atrás no passo |
| Desvios do POP | Vezes em que alguém fez diferente do escrito, e o motivo | Desvio repetido costuma mostrar um jeito melhor que o POP ainda não tem |
| Peso da revisão | Minutos de revisão ÷ tempo total da execução | Perto de zero por muitos dias, sem nenhuma correção, é sinal de carimbo |

**Ajustar no fim da semana, sem parar o piloto:** a mesma pergunta ou o mesmo erro apareceu duas vezes; alguém criou um atalho por fora do POP; a revisão pega sempre o mesmo erro no mesmo passo; a instrução precisou de explicação extra; um caso trouxe exceção que o POP não previa.

**Voltar atrás na hora:** erro chegou ao cliente ou ao tribunal; erro de prazo, mesmo pego pela revisão; dado de cliente fora da conta profissional ou sem a anonimização prevista; a IA inventou norma ou jurisprudência e passou da primeira conferência; a revisão virou carimbo. **Quem recua é o passo, o POP continua:** o passo sobe de sigla na hora, a ficha registra motivo e data, e ele só desce de novo depois de um novo teste com os três casos. Incidente e quase incidente vão para `escritorio/06-medicao/incidentes.md`.

**Erro plantado.** Na semana 2, um caso fictício com um defeito discreto (uma data trocada, um pedido faltando) entra na fila de revisão sem o revisor saber. Se passar, a revisão virou carimbo: o passo ganha um critério de pronto explícito para quem revisa. A skill pode gerar o caso (`references/roteiros.md`, seção 3) e entregá-lo a quem vai plantar. Exemplo resolvido: `references/exemplos-resolvidos.md`, seção 3.

**Medição antes e depois:**
1. Converta a linha de base em minutos por execução: total de minutos da tarefa ÷ volume (blocos espalhados do mesmo caso se somam).
2. Some o depois inteiro: execução + revisão + retrabalho. Quem esquece a revisão sempre encontra um ganho que não existe.
3. Compare só a semana 2. A semana 1 entra no relatório, fora da comparação.
4. Compare igual com igual: anote o tipo de caso dos dois períodos. Piloto só com casos fáceis infla o ganho.
5. Olhe qualidade junto com tempo: tempo menor com retrabalho maior é troca ruim. Erro que chegou ao cliente zera qualquer ganho.
6. Calcule: minutos a menos por execução, percentual de redução, horas por mês (minutos a menos × execuções por mês ÷ 60) e pontos de retrabalho. "Não medido" é resposta honesta para erro antes do piloto.

O resultado do piloto vira o número de partida da automação: depois, a `medir-retorno` compara três números (antes da IA, piloto com a IA na mão das pessoas, automação) e decide para onde vão as horas. Hora devolvida sem destino evapora. Exemplo com números: `references/exemplos-resolvidos.md`, seção 4.

## 10. Versões

A regra é a do glossário ("A vida do POP"), a mesma da `gerir-pops`.

- **POP novo.** O `escrever-pop` grava 0.1, status Rascunho. Ao entrar na esteira, o status vira Em teste. Cada rodada de ajustes aceitos sobe o decimal: 0.2 depois do teste de mesa, 0.3 depois do teste com a IA, 0.4 no fim da semana 1 do piloto (números de exemplo; a contagem segue as rodadas que houver). A aprovação para uso gera a 1.0.
- **Revisão de um POP vigente.** O rascunho fica em `03-pops/<setor>/_em-construcao/` e a vigente continua valendo. Na aprovação: mudança de redação, prazo ou exceção sobe o decimal (1.0 para 1.1); mudança de sigla, de responsável, de passo, de ordem ou de gatilho sobe o inteiro (1.x para 2.0). Regra prática: se a equipe precisa ser treinada de novo, sobe o inteiro; se basta avisar, sobe o decimal.
- **Controle de versões.** Cada versão ganha uma linha na tabela do fim do POP, com as seis colunas: Versão, Data, O que mudou, Por quê, Quem aprovou, Equipe avisada ou treinada em.
- **Aprovado para uso ainda não é Vigente.** Quem publica a versão aprovada como Vigente, tira a anterior do Projeto, arquiva e atualiza o mapa de POPs é a `gerir-pops`.

## 11. O que entrega e onde grava

Pasta: `escritorio/03-pops/<setor>/testes/` (cria se não existir). `<setor>` é a pasta do setor (`producao-de-pecas`, `relacionamento-com-o-cliente` etc.). `<sigla>` é a do setor, em minúsculas no nome do arquivo, e `<nn>` é o número do POP.

| Sigla | Setor | Sigla | Setor |
|---|---|---|---|
| ATD | Atendimento e triagem | FIN | Financeiro e cobrança |
| COM | Comercial | REL | Relacionamento com o cliente |
| PEC | Produção de peças | MKT | Marketing e conteúdo |
| PRZ | Prazos e controladoria | EQP | Gestão de equipe |
| AUD | Audiências e diligências | ADM | Administrativo |

| Entrega | Arquivo | Modelo |
|---|---|---|
| Checklist de qualidade | `testes/checklist-<sigla>-<nn>-AAAA-MM-DD.md` | `assets/checklist-modelo.md` |
| Teste de mesa | `testes/teste-de-mesa-<sigla>-<nn>-AAAA-MM-DD.md` | `assets/teste-de-mesa-modelo.md` |
| Teste com a IA (todas as fichas e o resumo) | `testes/teste-com-ia-<sigla>-<nn>-AAAA-MM-DD.md` | `assets/teste-com-ia-modelo.md` |
| Piloto (combinados, registro, conversas, fechamento) | `testes/piloto-<sigla>-<nn>.md` | `assets/piloto-modelo.md` |
| Registro de revisão e aprovação | Fim do POP, depois de "Controle de versões" | `assets/registro-de-revisao-modelo.md` |
| POP aprovado, com a versão nova | `escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md` | o do `escrever-pop` |

Exemplo: o teste de mesa do POP-PEC-01 feito no dia 2026-03-10 fica em `escritorio/03-pops/producao-de-pecas/testes/teste-de-mesa-pec-01-2026-03-10.md` (data de exemplo).

**Pendências para a base.** Tudo o que o executor ou a IA buscou fora do POP vai para a seção "Pendências" do arquivo do teste e, na aprovação, para a tabela "O que a IA vai precisar consultar" do POP, com "Existe por escrito? não". Essa tabela é o roteiro da `montar-base`. Casos usados no teste com a IA podem virar casos de teste da automação: ofereça-os à `montar-base`, que aplica a anonimização mais rigorosa e monta o gabarito.

**No `perfil.md`:** na linha "POP do setor-alvo com S, A e H", o estado entre parênteses (`(v0.2, em teste: teste de mesa feito)`, depois `(v1.0, aprovado para uso; publicar na gerir-pops)`). Em "Histórico", uma linha por etapa concluída, com data e arquivo. Etapa pulada vai para "Etapas puladas", com data e motivo.

Mostre cada arquivo antes de gravar. Sem acesso a arquivos, entregue cada documento no chat, em bloco pronto para copiar, com o nome e o caminho onde ele deveria ficar.

## 12. Trilha solo e trilha equipe

**Solo:**
- **Teste de mesa:** chame alguém de fora (o estagiário, a secretária, um colega de confiança de outro escritório), com o caso bem anonimizado. Em último caso, o titular executa dois dias depois de escrever, lendo ao pé da letra e proibido de completar com a memória. O ensaio "como quem acabou de chegar" ajuda, como complemento.
- **Revisão por par:** um colega de confiança de outro escritório. Um POP bem escrito não tem dado de cliente, então dá para mandar, sem as fichas. A IA pode fazer o papel de revisora com o roteiro de auditoria, sabendo que ela aponta lacuna e quem decide é o titular.
- **Revisão do titular:** é dele, mas em outro dia, com o checklist na mão e a pergunta final respondida por escrito.
- **Piloto:** o titular acumula os papéis. Vale chamar alguém de fora para a conversa de fechamento. O erro plantado precisa de outra mão: a pessoa de apoio planta, ou a skill gera o caso e só revela o defeito depois da revisão. Atenção à fadiga de revisão: revisar tudo sozinho empurra os passos A para S na prática. A sigla não muda por falta de gente.

**Equipe:**
- O executor do teste de mesa é quem vai rodar o POP no dia a dia. O autor observa calado.
- O par é do mesmo nível ou de um setor vizinho. O titular é quem assina.
- No piloto, cada pessoa assinou o acordo de uso de IA, e a conversa de abertura deixa claro que ninguém está sendo avaliado. O registro por pessoa nunca vira cobrança individual.
- Se o mesmo nome aparece como executor, revisor e decisor em todos os passos, ali está o gargalo: aponte na revisão por par.

## 13. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| POP bonito e não testado | A equipe abre, fecha e pergunta no WhatsApp | Teste de mesa por quem não escreveu, com cada pergunta tratada como defeito |
| Autor testando o próprio POP | Preenche as lacunas sem perceber | O autor observa calado; no solo, outra pessoa ou dois dias de distância |
| Testar só com o caso fácil | Passa no teste e quebra na primeira semana | Três casos, com o difícil obrigatório, e a revisão por par pede as fichas |
| Testar a IA num chat solto | Mede outra coisa | Teste no ambiente real, com código, POP e base |
| Explicar à IA mais do que o POP diz | A automação vai ter só o POP | A ficha registra toda explicação extra como instrução fraca |
| Contar só o tempo da IA | Ganho que não existe | Execução, revisão e retrabalho somados |
| Revisão-carimbo | O erro chega ao cliente | Peso da revisão, sinal de carimbo e erro plantado |
| Comparar semana de aprendizado ou casos diferentes | Número inflado | Só a semana 2, igual com igual |
| Mudar o POP todo dia no piloto | Ninguém sabe o que funcionou | Ajuste no fim da semana, com versão nova |
| Sigla descendo por conveniência | Passo de risco vira S | Na dúvida, a sigla sobe; quem decide é o advogado |

## 14. Próximo passo

- **POP aprovado para uso:** `gerir-pops`, para publicar como vigente, tirar a versão anterior do Projeto e atualizar o mapa de POPs.
- **Depois:** `montar-base`, com as pendências que os testes levantaram e os casos que podem virar caso de teste. Com a base pronta, `desenhar-automacao` (que começa pelo checklist de prontidão e usa a semana 2 do piloto como comparação), que escreve as instruções de cada passo, e depois `pop-para-skill` (para a equipe seguir o POP com o Claude passo a passo).
- **Faltou a linha de base:** `medir-retorno`, antes de começar o piloto.
- **POP devolvido na revisão:** volte ao `escrever-pop` com a lista do que falta, e depois retome a esteira daqui.
