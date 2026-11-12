---
name: revisao-periodica
description: >
  Junta num lugar só os rituais que mantêm a estrutura viva: revisão semanal (solo no bloco
  fixo; equipe na troca da semana e na ata), quinzenal do setor-alvo, mensal (código,
  painel do núcleo, incidentes) e trimestral (novo diagnóstico, revisão das siglas de cada
  POP, código, política, ferramentas, embaixadores e plano dos próximos 90 dias). Aplica um
  critério conservador para mudar sigla com dados e diz quando refazer o mapa inteiro,
  inclusive quando o solo contrata a primeira pessoa. Use quando o advogado disser "revisão
  da semana", "revisão do mês", "fechar o trimestre", "esse passo já pode ser S?", "a IA
  errou com o cliente, e agora?", "atualizar o código", "contratei alguém", "o que eu reviso
  hoje?". Não use para medir as horas e o retorno em reais (use medir-retorno) nem para
  montar o núcleo (use nucleo-de-inovacao).
---

# Revisão periódica

> O método só se sustenta se alguém olha para ele com hora marcada. Esta skill reúne a semanal, a quinzenal, a mensal e a trimestral, diz o que revisar em cada uma e como decidir, com dados, quando um passo muda de sigla.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha, incidente e medição: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- Chegou o dia de um ritual: semanal, quinzenal, mensal ou trimestral.
- O escritório quer montar o calendário de revisões.
- Alguém pergunta se um passo já pode mudar de sigla (descer de A para S, ou de H para A).
- Um erro chegou ao cliente ou ao processo e é preciso decidir o que muda no POP e na sigla.
- Aconteceu algo que pode exigir refazer o mapa: alguém entrou ou saiu, o solo vai contratar, abriu uma área nova.

**Não use quando:**
- O pedido é calcular horas devolvidas, valor da hora, ROI ou montar o painel financeiro: use `medir-retorno` (esta skill lê o painel dela).
- O pedido é nomear papéis ou montar o plano de 90 dias pela primeira vez: use `nucleo-de-inovacao`.
- O pedido é escrever o código do zero: use `codigo-do-escritorio`.
- O pedido é refazer o diagnóstico em si: use `diagnostico` (esta skill chama a de lá na trimestral).

## 2. Antes de começar

1. **Leia o perfil.** Abra `escritorio/perfil.md` (trilha, porte, setor-alvo). Leia o código do escritório, a regra de uso de IA e o calendário em `escritorio/06-medicao/revisoes/calendario-de-rituais.md`, se existir. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão:** precisa existir o que vai ser revisado. Para a semanal, pelo menos um uso de IA registrado ou uma ficha no funil. Para a quinzenal, o setor-alvo e o plano dele (o 5W2H do `mapear-setores`, em `escritorio/02-mapa/`) ou o POP. Para a mensal, o código do escritório. Para a trimestral, pelo menos um diagnóstico anterior e um POP. Se faltar, diga o que falta em uma frase e ofereça a skill que resolve.
3. **Sem calendário:** comece pelo passo 1 do fluxo (montar o calendário).
4. **Descubra qual revisão.** Pergunte: "Qual revisão a gente faz hoje: a da semana, a quinzenal do setor-alvo, a do mês ou a do trimestre?" Se o advogado não souber, olhe o calendário e diga qual está na vez.

## 3. Fluxo

### Passo 1. Montar o calendário (uma vez)
Pergunte, uma por vez:
1. "Qual dia e horário da semana para a revisão semanal?" Solo: os primeiros 20 minutos do bloco fixo. Equipe: a troca da semana (sexta, 15 minutos) e a reunião semanal do núcleo (30 minutos).
2. "Qual dia da semana para a quinzenal do setor-alvo, e quem participa?" (você e o responsável pelo setor).
3. "A mensal fica na primeira semana útil do mês. Qual dia?"
4. "Quando vai ser a primeira trimestral?" (semanas 12 e 13 do plano de 90 dias, fora da rotina).

Grave em `calendario-de-rituais.md` (modelo em `assets/calendario-de-rituais.md`). O calendário tem também o registro de rituais cumpridos: o primeiro ritual cancelado mostra a prioridade real do escritório.

### Passo 2. Rodar a revisão do dia
Siga a seção da cadência (4 a 7). Pergunte uma coisa por vez. Leia antes os arquivos que já têm a resposta (registros, atas, painéis) e só pergunte o que falta.

### Passo 3. Propor, mostrar e gravar
Toda mudança proposta em código, POP, sigla ou plano é proposta: marque `[NOVO]` ou `[ALTERADO]`, mostre ao advogado e só aplique depois do ok. A IA não aprova nada sozinha.

### Passo 4. Registrar no calendário
Uma linha no registro de rituais cumpridos: data, ritual, feito ou cancelado, motivo do cancelamento.

## 4. Revisão semanal

**Solo (20 minutos, no começo do bloco fixo, por escrito):**
1. Placar: o que a IA fez nos POPs, horas estimadas, incidente ou quase incidente.
2. O que travou.
3. Funil: o que entrou no arquivo "o que eu repeti esta semana" e o que virou ficha.
4. Combinados para a próxima semana.
5. Painel de três linhas: horas devolvidas e destino, erro mais importante, uma coisa a mudar.

**Equipe:**
1. **Troca da semana** (sexta, 15 minutos, condução em revezamento): cada pessoa traz um uso que funcionou e um que falhou, inclusive o titular. O que funcionou vai para o registro de prompts. Ao fim, preencha o painel semanal da cultura (modelo em `implantar-a-mudanca`).
2. **Reunião semanal do núcleo** (30 minutos): placar 5, o que travou 10, funil 10, combinados 5, com a ata (modelo em `nucleo-de-inovacao`). Com 2 a 5 pessoas, todos participam e a troca pode acontecer logo antes, no mesmo encontro. Regra dos 30 minutos: assunto que passa do tempo vira conversa separada.

**Na última semana do mês (equipe):** a celebração do mês, 10 minutos na última troca, conduzida pelo titular: reconhece quem devolveu mais horas e quem pegou erro. As duas coisas contam como mérito.

## 5. Revisão quinzenal do setor-alvo (15 a 20 minutos)

Você e o responsável pelo setor. Quatro blocos:
1. **Números:** horas da última semana no setor-alvo e incômodo de hoje (1 a 5), dado por quem executa.
2. **Plano:** o que andou no plano do setor (5W2H), o que atrasou e por quê.
3. **Erros da IA:** cada erro repetido vira ajuste no POP, na base ou na instrução do passo. Anote qual.
4. **Próximos 15 dias:** uma ou duas ações, cada uma com dono e data.

**Indicadores da quinzenal:**

| Indicador | Como medir | Quando |
|---|---|---|
| Horas por semana do setor-alvo | Registro de horas, só de quem toca o setor | Uma semana por mês |
| Incômodo | 1 a 5, dado por quem executa | Toda quinzenal |
| Ações do plano no prazo | Concluídas ÷ previstas | Toda quinzenal |
| Retrabalho da IA | Quantas vezes a saída foi refeita, e em que passo | Anotado na semana, somado na quinzenal |
| Indicador do setor (escolher um) | Ex.: relacionamento, tempo até a primeira resposta; prazos, tarefas concluídas antes do vencimento; peças, ajustes pedidos na revisão | Toda quinzenal |

Modelo: `assets/quinzenal.md`. Se o retrabalho da IA aparece no mesmo passo em duas quinzenais seguidas, leve o passo para a regra de sigla (seção 9).

## 6. Revisão mensal (primeira semana útil do mês)

Três partes. Modelo completo, com o painel do núcleo: `assets/mensal.md`.

### 6.1 Revisão leve do código (30 minutos, dono do código)
Leia o código atual (com a versão) e junte o que aconteceu no mês. Pergunte só o que não estiver nos arquivos:
1. Painéis semanais do mês (em `escritorio/01-cultura/mudanca/paineis-semanais.md`).
2. Erros pegos na revisão e o que causou cada um.
3. Reclamações ou elogios de cliente, resumidos e sem nomes.
4. Situações novas que a equipe não sabia como tratar.
5. Sugestões da equipe.

Entregue:
1. Quais regras do código foram quebradas mais de uma vez no mês, com uma hipótese para cada (a regra está confusa, desatualizada ou falta treinamento).
2. Quais situações novas precisam de regra, com uma sugestão de redação curta.
3. Quais trechos ficaram desatualizados.
4. A proposta de versão nova, com `[NOVO]` e `[ALTERADO]` em cada mudança.
5. Uma mensagem curta para a equipe explicando o que mudou e por quê.

Nada é aprovado pela IA. Depois do ok, grave a nova versão do código (versão e data no topo) e avise que as instruções do Projeto no Claude mudam no mesmo dia: ofereça a `codigo-do-escritorio` para regenerar `instrucoes-do-projeto.md`.

### 6.2 Painel mensal do núcleo (60 minutos com o patrocinador; solo, no bloco fixo)
Monte o painel com os indicadores do núcleo, lendo o painel financeiro do mês da `medir-retorno` (`escritorio/06-medicao/painel-AAAA-MM.md`) para horas devolvidas, custo e valor. Não recalcule o que a `medir-retorno` já calculou. Depois leia o painel e as atas do mês e entregue:
1. O mês em até 8 linhas, em linguagem de conversa com o sócio.
2. O indicador que mais melhorou e o que mais preocupa, com o motivo provável tirado das atas.
3. O custo do núcleo contra o valor das horas devolvidas: acima ou abaixo do ponto de equilíbrio.
4. Os incidentes e quase incidentes, e se o POP correspondente foi alterado. Se não foi, sinalize.
5. No máximo duas decisões para o patrocinador tomar.

Não invente número que não esteja no painel. Se faltar dado, diga qual. Antes de fechar, passe o painel pelos oito erros comuns de conta (referência; o detalhe está na `medir-retorno`): contar hora que virou ociosidade; ignorar a revisão humana; esquecer a implantação; usar o valor da hora errado (hora do sócio na tarefa da secretária); medir na fase de aprendizado; contar duas vezes; estimar de memória; converter tudo em dinheiro.

Na primeira mensal, defina as metas de cada indicador a partir do que foi medido no primeiro mês. Não há meta padrão. A meta de incidentes é "registrar todos".

### 6.3 Incidentes e POP
Abra `escritorio/06-medicao/incidentes.md`. Para cada incidente ou quase incidente do mês: o que houve, em que passo de que POP, e o que mudou no POP. Todo incidente termina com um passo novo ou alterado. Incidente sem mudança no POP é sinalizado no painel. Se o incidente aconteceu num passo S ou A, aplique a regra de subida da seção 9 (ela vale na hora, sem esperar a mensal; aqui só se confere que foi aplicada).

**Alerta do patrocinador:** se a mensal foi cancelada duas vezes seguidas, registre isso no calendário e leve para a trimestral.

## 7. Revisão trimestral (2 horas, fora da rotina)

Núcleo e sócios (solo: um bloco fixo inteiro, fora da agenda normal). Modelo: `assets/trimestral.md`. Ordem:
1. **Refazer o diagnóstico** pela skill `diagnostico`, com a mesma pessoa e a mesma sinceridade. Compare com a rodada anterior: o valor está na comparação.
2. **Rever as siglas de cada POP.** Para cada POP em `escritorio/03-pops/`, passo a passo: o S ainda é S? Algum A virou S? Algum volta a H? Responda com os dados do trimestre (registro de uso, erros pegos, incidentes, indicador), pela regra da seção 9. As mudanças aprovadas entram no POP com `[ALTERADO]` e versão nova.
3. **Revisão completa do código** (seção 8): as sete seções, uma por uma.
4. **Política de uso de IA e ferramentas autorizadas:** a política ainda descreve o que se faz? Alguma ferramenta entrou ou saiu? A configuração da conta foi conferida de novo? Mudanças vão para a `regra-de-uso-de-ia`, e quem já assinou assina a versão nova.
5. **Rodízio de embaixadores:** quem continua, quem passa o papel, quem entra. Se o escritório mudou de faixa de porte, reveja os papéis e o guardião (`nucleo-de-inovacao`).
6. **Conferir os gatilhos do mapa** (seção 10).
7. **Plano dos próximos 90 dias**, com semanas relativas de 1 a 13, pelo modelo da `nucleo-de-inovacao`. Inclui o tamanho do núcleo para o próximo ciclo.

## 8. Código do escritório: leve todo mês, completa todo trimestre

Os dois ritmos convivem:

| Revisão | Quando | Duração | O que olha | Resultado |
|---|---|---|---|---|
| Leve | Mensal, primeira semana útil | 30 min | Só o que o mês mostrou: regras quebradas, situações novas, trechos desatualizados | Mudanças pontuais, versão menor (1.2 para 1.3) |
| Completa | Trimestral | Parte das 2 h | As sete seções, uma a uma, mais os `[A DEFINIR]` que ficaram para trás | Versão nova (1.x para 2.0 quando muda algo de fundo) |
| Fora do calendário | Na hora | O necessário | Reclamação séria de cliente, erro que passou pela revisão, pessoa nova, ferramenta nova | Ajuste imediato e registro na próxima mensal |

O código e as instruções do Projeto mudam sempre no mesmo dia.

## 9. Quando um passo muda de sigla

O método diz que descer de sigla se decide "com o tempo, olhando o indicador e os erros pegos na revisão", mas não fixa números. A regra abaixo é uma **sugestão conservadora, a validar pelo escritório.** Os números entre colchetes são sugestão e ficam `[A DEFINIR]` até o escritório aprovar. O detalhe, com exemplos e o que conta como erro, está em `references/mudanca-de-sigla.md`.

**Princípios fixos:**
- Os cinco passos da linha vermelha nunca descem de H. Em Família, caso com sinal de violência, coação ou risco não entra em automação.
- A trava por estágio da `classificar-sah` vence qualquer contagem.
- Subir é imediato. Descer só na revisão trimestral.
- Depois de uma subida, a contagem para descer recomeça do zero.

**Descer de A para S (todas as condições):**
1. O resultado do passo fica dentro do escritório. Se sai para cliente, tribunal ou público sem conferência depois, o passo continua A.
2. [Sugestão: 30] execuções seguidas sem erro pego na revisão `[A DEFINIR]`, em pelo menos [sugestão: 8] semanas de uso `[A DEFINIR]`.
3. Indicador do POP estável ou melhor nas duas últimas mensais, e retrabalho da IA zero nesse passo no período.
4. Plano de amostra escrito: quem confere, o que confere e quantas a cada lote ([sugestão: 1 a cada 5] nas primeiras 4 semanas como S, depois [sugestão: 1 a cada 10]) `[A DEFINIR]`.
5. Aprovação do dono do POP e do patrocinador (e do guardião se houver dado de cliente). No solo, a decisão é escrita e confirmada depois de uma pausa de 24 horas.

**Descer de H para A:** só para passo fora da linha vermelha, quando o julgamento que o passo exigia virou critério escrito na base. O passo passa por um piloto de 2 semanas como A, com revisão em tudo, antes de a sigla mudar no POP.

**Subir na hora (qualquer pessoa aciona; o dono do POP confirma no mesmo dia):**
- **Erro que chegou ao cliente ou ao processo, ou dado que saiu:** passo S sobe para A. Passo A sobe para H (a IA para nesse passo) até a causa estar corrigida no POP e a revisão ter objeto claro; a volta para A se decide na mensal seguinte.
- **Erros repetidos na amostra de um passo S:** [sugestão: 2 erros do mesmo tipo em 30 dias, ou 1 erro em prazo, valor ou dado de cliente] `[A DEFINIR]`: sobe para A.
- **Mudança de estágio:** perdeu a conta profissional, a regra de uso ficou desatualizada, o critério ou a base do passo mudou ou ficou sem dono: a trava por estágio volta a valer.
- **Retrabalho:** se, por duas semanas seguidas, revisar levar mais tempo do que fazer à mão, o processo volta para a etapa de ajuste da `implantar-a-mudanca` (a sigla não desce por isso).

Toda mudança de sigla é registrada no POP (`[ALTERADO]`, versão nova, motivo e dados usados) e na revisão em que foi decidida.

## 10. Quando refazer o mapa inteiro

Refaça o mapeamento completo pela `mapear-setores` quando:
- o setor-alvo caiu do primeiro lugar no ranking (sinal de que funcionou);
- alguém entrou ou saiu da equipe;
- o escritório abriu uma área nova ou mudou o modelo de negócio;
- e, no mínimo, a cada 6 meses (uma trimestral sim, outra não).

**Solo que vai contratar a primeira pessoa.** É o gatilho mais importante da trilha solo, porque muda a trilha. Na ordem:
1. **Antes de a pessoa chegar:** escrever o POP do setor que ela vai assumir (`escrever-pop`). A pessoa aprende pelo papel, e o perfil da vaga fica mais claro.
2. **Trocar a trilha no `perfil.md`:** `porte: 2-5`, `trilha: equipe`, com uma linha no "Histórico".
3. **Acordo assinado:** o autocompromisso dá lugar ao acordo de uso de IA assinado pela pessoa nova, antes de ela usar qualquer IA (`regra-de-uso-de-ia`). Sem acordo assinado, ninguém começa.
4. **Integração na primeira semana** (1 hora, com a pessoa de referência): ler o código, assinar o acordo, aprender os prompts do setor.
5. **Mapeamento com entrevistas** (`mapear-setores`), agora com a pessoa nova entrevistada e registrando horas. Sugestão: depois de [4] semanas de casa `[A DEFINIR]`, quando ela já conhece a rotina.
6. **Núcleo:** rever os papéis (`nucleo-de-inovacao`). A pessoa nova pode virar embaixadora.
7. **Diagnóstico:** na trimestral seguinte, as perguntas de delegação e equipe passam a contar inteiras.

**Equipe:** entrada ou saída de pessoa refaz o mapa. Quem sai deixa o POP do setor atualizado antes de sair, sempre que possível. Equipe que cresce de faixa revê os papéis do núcleo e o guardião na trimestral.

## 11. O que entrega e onde grava

| Revisão | Onde grava |
|---|---|
| Calendário e registro de rituais cumpridos | `escritorio/06-medicao/revisoes/calendario-de-rituais.md` |
| Semanal (ata) | `escritorio/01-cultura/nucleo/atas.md`, a mais recente no topo |
| Semanal (painel da cultura) | `escritorio/01-cultura/mudanca/paineis-semanais.md` |
| Quinzenal | `escritorio/06-medicao/revisoes/quinzenal-AAAA-MM-DD.md` |
| Mensal (código leve, painel do núcleo, incidentes) | `escritorio/06-medicao/revisoes/mensal-AAAA-MM.md` |
| Trimestral | `escritorio/06-medicao/revisoes/trimestral-AAAA-MM-DD.md` |

Mudanças aprovadas vão para o documento dono: o código em `escritorio/01-cultura/codigo-do-escritorio.md`, as siglas no POP em `escritorio/03-pops/`, a trilha e o histórico no `perfil.md`. Mostre cada documento antes de gravar. Na primeira trimestral, marque no `perfil.md` o item "Primeira revisão trimestral".

## 12. Trilha solo e trilha equipe

**Solo:**
- Semanal: 20 minutos no começo do bloco fixo, por escrito, no mesmo arquivo de ata.
- Quinzenal: o titular sozinho, com o registro de horas como fonte principal. No solo é o registro que mostra a verdade.
- Mensal: código e painel no bloco fixo da primeira semana. O indicador de adoção não se aplica.
- Trimestral: um bloco fixo inteiro, fora da rotina. Sem rodízio de embaixadores (a não ser que haja pessoa de apoio).
- A descida de sigla exige pausa de 24 horas entre a proposta e a decisão escrita, porque não há segunda pessoa para aprovar.
- Gatilho especial: contratar a primeira pessoa (seção 10).

**Equipe:**
- Troca da semana (15 minutos) e ata semanal do núcleo (30 minutos).
- Mensal com o patrocinador; trimestral com os sócios.
- Com 6 ou mais pessoas, a quinzenal é por setor-alvo, com o embaixador do setor.
- Entrada ou saída de pessoa refaz o mapa.

## 13. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Mapear e engavetar | O mapa envelhece e o setor-alvo errado continua sendo atacado | Gatilhos de refazer o mapa e prazo de 6 meses |
| Descer de sigla porque "está acertando" | O erro aparece no cliente | Contagem mínima, indicador estável e descida só na trimestral |
| Incidente sem mudança no POP | O mesmo erro volta | Todo incidente termina com passo novo ou alterado, conferido na mensal |
| Código e Projeto desalinhados | A IA segue a regra antiga | Os dois mudam no mesmo dia |
| Meta "zero incidente" | Ninguém registra | Meta é registrar todos |
| Painel com número inventado | Decisão errada do patrocinador | Só número do painel; o que falta é dito |
| Ritual cancelado sem registro | A prioridade real some de vista | Registro de rituais cumpridos |
| Solo contrata e segue na trilha solo | Pessoa nova sem acordo e sem POP | Sequência da primeira contratação |

## 14. Próximo passo

- Depois da trimestral: o plano dos próximos 90 dias (`nucleo-de-inovacao`) e, se o setor-alvo mudou, `mapear-setores` e `escrever-pop` para o novo setor.
- Se a mensal mostrou horas sem destino ou conta inconsistente: `medir-retorno`.
- Se uma sigla mudou: `desenhar-automacao` para ajustar a instrução do passo e o plano para erro, e `pop-para-skill` para atualizar a skill instalada.
