---
name: medir-retorno
description: >
  Mede o retorno da IA e da automação no escritório com número em vez de impressão: valor da
  hora (três métodos), custo total, calculadora de horas devolvidas, ROI em 12 meses e
  payback, estimativa de redução a partir do POP, linha de base antes da mudança, medição
  depois de pelo menos 4 semanas, indicadores por setor e painel mensal com decisão de
  manter, ajustar ou pausar. Use quando o advogado disser "quanto vale a minha hora",
  "valeu a pena a IA?", "calcular o ROI", "payback da automação", "quantas horas a IA
  devolveu", "linha de base do setor", "medir antes e depois", "painel do mês", "quanto
  gasto com IA", "para onde foram as horas". Não use para escolher o setor-alvo pelas horas
  da semana (use mapear-setores) nem para revisar o método inteiro no trimestre (use
  revisao-periodica).
---

# Medir o retorno

> Calcula quanto vale a hora do escritório, quanto custa de verdade a mudança e quantas horas ela devolveu, comparando uma semana medida antes com outra medida depois, e fecha o mês com um painel que decide manter, ajustar ou pausar cada automação.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de valor da hora, linha de base, horas devolvidas e incidente: `../../docs/glossario.md`. O que muda por porte: `../../docs/trilhas.md`.

Sem número, o escritório não escolhe direito o que automatizar e não consegue provar que funcionou. A cena é comum: assina uma ferramenta em março, a equipe usa animada por duas semanas e, em junho, alguém pergunta se valeu a pena. A resposta mais honesta é "acho que sim", e "acho que sim" não decide se renova a assinatura. Tem também a armadilha da velocidade: a IA responde em dez segundos, mas se a conferência leva vinte e cinco minutos, a tarefa de trinta passou a levar vinte e cinco. Pela sensação, meia hora economizada. Pelo relógio, cinco minutos.

**Combinado:** esta skill não promete retorno. Todo número de exemplo vem marcado como exemplo. O percentual de redução quem coloca é o escritório, a partir do próprio POP, e quem confirma é a medição. Nenhum percentual de mercado.

## 1. Quando usar

**Use quando:**
- O setor-alvo está definido e é preciso congelar a linha de base **antes** de mudar qualquer coisa nele.
- O advogado quer saber o valor da própria hora, ou o custo-hora de um colaborador.
- Vai decidir se uma automação vale o investimento (projeção com a calculadora).
- A automação já roda há pelo menos 4 semanas e é hora de medir de novo e comparar.
- Fechou o mês e precisa do painel mensal.

**Não use quando:**
- O pedido é descobrir para onde vão as horas do escritório inteiro e escolher o setor-alvo: use `mapear-setores` (a semana registrada lá serve de ponto de partida para a linha de base).
- O pedido é revisar código, POPs, base e automações no ciclo trimestral: use `revisao-periodica`, que lê os painéis gravados aqui.

## 2. Antes de começar

1. Leia `escritorio/perfil.md` (trilha, pessoas por função, `setor_alvo`) e, se existirem, `escritorio/06-medicao/valor-da-hora.md`, as linhas de base e os painéis anteriores. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão:** é preciso um setor-alvo. O ideal é ter também o POP com S, A e H (`escrever-pop`), porque a estimativa de redução sai dele, passo a passo. Sem setor-alvo, ofereça o `mapear-setores` (ou o setor do `diagnostico`). Sem POP, dá para seguir com o passo a passo atual e marcar a estimativa como mais frágil. Registre em "Etapas puladas" o que ficou para trás.
3. **A linha de base vem antes da mudança.** Se a automação já está rodando e não houve linha de base, diga com franqueza: a comparação perdeu o ponto de partida. As saídas são registrar agora uma semana com a automação pausada no setor, se o advogado aceitar, ou usar o registro de horas do `mapear-setores`, se for anterior à mudança, anotando a limitação no arquivo.
4. **Modo rápido:** se o advogado só quer uma projeção para decidir, pule para o passo 7 (calculadora) com os números que ele tiver, e deixe claro no resultado que tudo é estimativa.
5. **Dados financeiros são sensíveis.** Peça só o necessário, em conta profissional, e nunca nome de cliente nem número de processo. Toda conta devolvida é conferida pelo advogado: a assinatura da decisão continua sendo dele.

## 3. Fluxo

### Passo 1. O que vai ser medido
Pergunte, uma de cada vez: "Qual setor e quais tarefas a gente vai medir?" e "Já existe automação rodando nesse setor ou ainda vai começar?". Liste as tarefas, de preferência seguindo os passos do POP.

### Passo 2. Valor da hora
Siga a seção 4. Perguntas, uma por vez, só as que o método precisar:
1. "Quem executa as tarefas que vão ser automatizadas: você, outro advogado, ou secretária, estagiário, assistente?"
2. "Quantas horas por mês você fica no escritório? E quantas delas viram entrega (peça, atendimento, audiência, análise)?" Se não souber, a semana de registro responde. Enquanto isso, estimativa honesta, marcada como estimativa.
3. Método 1: "Qual o faturamento médio mensal dos últimos 6 ou 12 meses?" Método 2: "Quanto você quer retirar por mês e quanto são os custos fixos?" Método 3: "Qual o salário da pessoa e quanto o contador estima de encargos e benefícios?" (sem percentual padrão de encargos).

Mostre a conta, explique em poucas linhas o que a diferença entre os métodos diz sobre o escritório e indique qual valor usar em cada setor. Grave `valor-da-hora.md` (modelo em `assets/valor-da-hora.md`).

### Passo 3. Custo total
Percorra a tabela da seção 5 item por item. Pergunte o que faltar. A assinatura costuma ser a menor parte: o que pesa é o tempo das pessoas.

### Passo 4. Para onde vão as horas
Antes de automatizar, pergunte: "Se o setor devolver horas, para onde elas vão? Mais casos, captação, estratégia ou qualidade de vida?". Registre a resposta na linha de base. Destinos e como medir cada um em `references/medicao-e-indicadores.md`.

### Passo 5. Linha de base
Leia `references/medicao-e-indicadores.md`. Monte a folha única (seção 7) com as tarefas já nas linhas e:
1. Peça uma semana típica registrada por quem trabalha no setor: tarefa, início, fim, minutos, volume, se usou IA, minutos de revisão.
2. Calcule o tempo por unidade (minutos ÷ volume) de cada tarefa.
3. Pergunte: "Quais 1 a 3 números do setor você quer acompanhar?" Ofereça a lista do setor e anote fórmula e fonte de cada um.
4. Pergunte: "A semana foi típica? O que foi diferente?"
5. Congele com data, método do valor da hora e quem preencheu. Grave `linha-de-base-<setor>.md` (modelo em `assets/linha-de-base.md`).

Na trilha equipe, ofereça uma mensagem curta, em tom de conversa, explicando à equipe por que vamos registrar e como preencher sem atrapalhar o dia.

### Passo 6. Estimar a redução a partir do POP
Leia `references/estimar-reducao.md`. Para cada passo: faixa mínima e máxima, com o raciocínio em uma frase. **Passo H fica com redução zero.** Em passos A e S, **a revisão humana que vai continuar existindo entra na conta.** **Sem percentual de mercado nem promessa de fornecedor.** O resultado é a redução do setor em horas por semana e em percentual, nos dois cenários.

### Passo 7. Calculadora (projeção)
Monte o JSON com as variáveis (formato e fórmulas em `references/calculadora.md`) e rode:
```
python3 scripts/calcular_roi.py ENTRADA.json [--valor-hora 40] [--saida ARQUIVO.md]
```
Sem acesso ao terminal, faça a mesma conta na conversa, mostrando cada linha. Mostre os avisos. Se as horas devolvidas são de colaborador, rode uma segunda vez com o custo-hora dele (método 3) e apresente as duas: "a conta mais honesta costuma ficar entre as duas". Aproveitamento conservador. A saída é **projeção** e é anotada assim.

### Passo 8. Medição depois
Só depois de **pelo menos 4 semanas** de uso regular. Pergunte: "Já são quatro semanas usando no dia a dia?" Se não, combine a data. Repita a mesma folha, numa semana parecida com a da linha de base, agora com os minutos de revisão. Compare **tempo por unidade**, não o total. Confronte com a estimativa do passo 6 e rode a calculadora de novo com o número medido. As primeiras semanas mais lentas vão para o custo de aprendizado. Grave a medição como nova seção em `linha-de-base-<setor>.md`.

### Passo 9. Painel mensal
No fim de cada mês, preencha os 6 blocos (seção 8, modelo em `assets/painel-mensal.md`). Depois, faça a leitura do painel:
1. O retorno líquido do mês é confiável? Aponte hora contada duas vezes, revisão esquecida, implantação de fora ou valor da hora inadequado para quem executa.
2. Quanto das horas devolvidas virou trabalho e quanto "não sabemos dizer". Se o segundo for relevante, sugira como recuperar essas horas.
3. Onde reinvestir no próximo mês, em ordem, olhando os indicadores que pioraram ou não mexeram.
4. Para cada automação, uma decisão objetiva: manter, ajustar ou pausar, com o motivo.
5. A pergunta mais importante para levar à reunião (equipe) ou ao bloco fixo (solo).

Diferencie medido de estimado. Não arredonde para cima. Se faltar dado para uma conclusão, diga qual. Grave `painel-AAAA-MM.md`.

### Passo 10. Passar a conta pela lista de erros
Antes de apresentar a sócio ou equipe, confira a conta contra os 8 erros da seção 11. Corrija o que aparecer e diga o que mudou.

## 4. Valor da hora

**Base: horas produtivas,** as que viram entrega. Quem fica 8 horas por dia em 22 dias úteis soma 176 horas no escritório, mas boa parte não vira trabalho para cliente (reunião interna, deslocamento, o WhatsApp que interrompe a peça, a procura pelo "modelo_contestacao_FINAL_v3"). Exemplo: 176 h no escritório, cerca de 120 h produtivas. Usar as 176 deixa a hora artificialmente baixa e a conta de retorno pequena demais.

| Método | Fórmula | Exemplo | Quando usar |
|---|---|---|---|
| 1 · Faturamento ("quanto a hora vale hoje") | faturamento médio mensal (6 ou 12 meses) ÷ horas produtivas (somar todos que faturam) | 18.000 ÷ 120 = R$ 150 | A tarefa automatizada é do advogado (peça, análise, estratégia) |
| 2 · Retirada desejada ("quanto a hora precisa valer") | (retirada desejada + custos fixos) ÷ horas produtivas | (15.000 + 9.000) ÷ 120 = R$ 200 | Faturamento baixo ou muito irregular (muito êxito, pouco mensal) |
| 3 · Custo do colaborador ("quanto custa a hora de quem executa") | (salário + encargos e benefícios informados pelo contador) ÷ horas produtivas da pessoa | (3.000 + 1.800) ÷ 120 = R$ 40 | Tarefa de secretária, estagiário ou assistente. Sem percentual padrão de encargos |

Escritório com vários advogados: método 1 por pessoa ou uma média, anotada no painel. Usar a hora do sócio para a triagem que a secretária faz infla o retorno.

**Regra de ouro:** escolha o método, anote qual foi e não troque no meio do caminho. Se num mês mediu com o método 1 e no outro com o 2, a comparação perde o sentido.

## 5. Custo total

| Item | O que entra | Como calcular | Frequência |
|---|---|---|---|
| Assinaturas de IA | Plano de cada pessoa que usa | Preço do plano × número de usuários | Mensal |
| Outras ferramentas | Software jurídico, CRM, automação de mensagens, armazenamento: só a parte nova ou o upgrade que veio por causa da IA | Conta de agora − conta de antes | Mensal |
| Implantação | Escrever o POP, montar o Projeto no Claude, organizar a base, testar e ajustar | Horas × valor da hora de quem fez | Uma vez, com ajustes depois |
| Aprendizado | As semanas em que a equipe faz a tarefa mais devagar porque ainda está pegando o jeito | Horas a mais em relação à linha de base × valor da hora | Concentrado no início |
| Treinamento | Cursos, mentorias, formações e as horas da equipe em treinamento | Valor pago + horas em treinamento × valor da hora | Uma vez ou anual |
| Consultoria, se houver | Quem ajuda a implantar ou configura alguma integração | Valor do contrato | Uma vez ou mensal |
| Revisão humana | As horas novas de conferência do que a IA produziu. Elas não somem nunca, e não devem sumir | Horas por semana × 4,33 × valor da hora | Mensal, contínuo |
| Custo de oportunidade | O que deixou de ser feito nas horas de implantação | Já está nas horas de implantação × valor da hora. Não some de novo | Cuidado com dupla contagem |

Na calculadora, aprendizado e treinamento entram como custo único (horas de implantação e outros custos únicos), e a revisão humana é descontada das horas devolvidas. No painel, entram no mês em que aconteceram.

## 6. A calculadora em uma tela

SEM = 52 ÷ 12 (cerca de 4,33). Horas devolvidas por mês = max(0, soma de horas por semana × redução % − revisão por semana) × SEM. Valor por mês = horas por mês × valor da hora × aproveitamento %. Investimento inicial = horas de implantação × valor da hora de implantação + custos únicos. Líquido mensal = valor − ferramentas por mês. ROI em 12 meses = (12 × valor − (12 × custo mensal + inicial)) ÷ (12 × custo mensal + inicial) × 100. Payback = inicial ÷ líquido mensal ("não se paga" se o líquido for zero ou negativo; "imediato" se não houver investimento inicial). Fórmulas completas, avisos e exemplo resolvido em `references/calculadora.md`.

**Exemplo (números fictícios, 2 advogados e 1 secretária):** 14,4 h por semana brutas, 49,4 h por mês líquidas, valor da hora R$ 120, R$ 3.557 por mês, investimento inicial R$ 6.300, líquido R$ 2.957 por mês, ROI de 216% em 12 meses, payback de 2,1 meses. É o arquivo `scripts/exemplos/roi-exemplo.json`.

## 7. Uma folha só e um registro de horas devolvidas

O método tinha três formatos de registro que se sobrepunham: a folha da semana (tarefa, início, fim, minutos, volume, uso de IA, minutos de revisão), o registro de horas devolvidas por uso (minutos antes, minutos com IA, erro pego, para onde foi o tempo) e o registro de uso da automação. Aqui eles viram dois:

1. **A folha de linha de base**, que é a mesma folha da medição depois. As colunas são as da folha semanal, com a pessoa (por função) em cada linha. Antes e depois são preenchidos igual, e a comparação é por tempo por unidade. Fica nas Partes 1 e 2 de `linha-de-base-<setor>.md`.
2. **O registro de horas devolvidas**, uma linha por uso, que junta o registro por uso com o que importa do registro de uso: tarefa (passo do POP), S ou A, minutos antes (o tempo por unidade da linha de base, e não a memória), minutos com IA já com revisão, minutos devolvidos, erro pego na revisão e para onde foi o tempo. Fica na Parte 3 de `linha-de-base-<setor>.md` enquanto não houver automação. Quando a automação existir, as duas colunas "minutos antes" e "para onde foi o tempo" passam para o `registro-de-uso.md` dela, para não haver dois registros do mesmo uso.

O painel do mês soma o registro de horas devolvidas (blocos 2 e 3). A medição depois confirma ou corrige essa soma.

## 8. Painel mensal (6 blocos)

1. **Investimento do mês e acumulado:** ferramentas, horas de implantação e ajuste × valor da hora, treinamento ou consultoria.
2. **Horas devolvidas por setor:** linha de base × este mês × revisão nova, cada linha marcada como medida ou estimada. Horas devolvidas líquidas = (diferença − revisão) × 4,33.
3. **Para onde as horas foram:** casos, captação, estratégia, qualidade de vida (fora dos reais) e "não sabemos dizer". Aproveitamento = horas com destino conhecido ÷ horas devolvidas.
4. **Indicadores do setor-alvo:** linha de base e mês. Na trilha equipe, também a adoção.
5. **Ganhos que não são hora:** quase-erros, tempo até a primeira resposta ao lead, peças devolvidas, retorno dos clientes.
6. **Resultado e decisão:** valor aproveitado = horas com destino × valor da hora; líquido do mês e acumulado; o que funcionou e o que travou; manter, ajustar ou pausar cada automação; próximo setor, responsável e prazo.

Guarde todos os meses. O valor do painel aparece no terceiro ou quarto mês, quando dá para ver a tendência e não só a foto.

## 9. O que entrega e onde grava

Tudo em `escritorio/06-medicao/`, com nome, versão, data da revisão e dono no topo. Mostre antes de gravar.

| Arquivo | Conteúdo |
|---|---|
| `valor-da-hora.md` | Método escolhido, horas produtivas, cálculo, custo-hora por função, valor usado em cada setor, histórico |
| `linha-de-base-<setor>.md` | Parte 1, linha de base congelada · Parte 2, medições depois · Parte 3, registro de horas devolvidas |
| `painel-AAAA-MM.md` | O painel do mês, com a leitura e as decisões |

A saída da calculadora entra no painel do mês (bloco 6, como projeção) ou na linha de base (como estimativa de partida). No `perfil.md`, depois do primeiro painel, marque "Linha de base e primeiro painel" no Progresso e registre no Histórico a primeira medição ("AAAA-MM-DD: primeira medição do setor [SETOR]: [H] h devolvidas por mês, medido").

## 10. Trilha solo e trilha equipe

**Solo:**
- Valor da hora pelo método 1 (faturamento) ou 2 (retirada desejada). Se houver estagiário ou secretária e a tarefa for dela, método 3 para aquela tarefa.
- O registro e a medição são feitos pelo titular. A memória exagera as tarefas chatas e encurta as que a gente gosta: só a folha afirma resultado.
- O painel é lido no bloco fixo semanal, na primeira semana do mês, por escrito.
- Indicador de adoção não se aplica.

**Equipe:**
- Método 3 para tarefas da equipe. Nunca usar a hora do sócio para tarefa de colaborador. Vários advogados: valor por pessoa ou média, anotada.
- Cada pessoa do setor preenche a própria folha. Combinar antes que ninguém está batendo ponto: o número que interessa é o tempo por unidade da tarefa.
- O painel é preenchido por quem cuida da inovação e lido na reunião do núcleo (`nucleo-de-inovacao`).
- Adoção = pessoas usando ÷ equipe.

## 11. Erros de conta que a skill evita (os 8 erros comuns)

| Erro | O que acontece | Como a skill evita |
|---|---|---|
| Contar hora que virou ociosidade | 40 horas "voltaram" e ninguém sabe onde estão | Destino decidido antes, aproveitamento na calculadora e "não sabemos dizer" no painel |
| Ignorar a revisão humana | Retorno inflado e decepção no segundo mês | Revisão descontada das horas e incluída na estimativa por passo |
| Esquecer a implantação | ROI que não fecha com o caixa | Horas de implantação × valor da hora no investimento inicial e payback |
| Usar o valor da hora errado | Hora do sócio na tarefa da secretária multiplica o retorno | Método 3 para colaborador e calculadora rodada duas vezes |
| Medir na fase de aprendizado | A primeira semana mostra piora e o escritório desiste | Pelo menos 4 semanas de uso, e as horas a mais vão para custo de aprendizado |
| Dupla contagem | Retrabalho evitado somado às horas devolvidas; custo de oportunidade somado à implantação | Cada ganho num lugar só |
| Estimar de memória | "Acho que a gente gastava umas dez horas nisso" | Folha de registro antes e depois; estimativa só para escolher |
| Converter tudo em dinheiro | O prazo evitado vira o valor da causa no ROI | Ganho de risco e de satisfação em quantidade e tendência, fora dos reais |

## 12. Próximo passo

- Depois da linha de base congelada: seguir com a automação (`desenhar-automacao`), que já nasce com régua para ser medida.
- Depois do primeiro painel: levar as decisões de manter, ajustar ou pausar para a `revisao-periodica`.
- Se o setor-alvo caiu do 1º lugar ou o painel mostrou que ele já devolveu o que podia: `mapear-setores` para escolher o próximo da fila.
