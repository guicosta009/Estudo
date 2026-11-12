---
name: nucleo-de-inovacao
description: >
  Monta o núcleo de cultura e inovação do escritório: missão e escopo, formato por porte,
  os quatro papéis (patrocinador, responsável, embaixadores, guardião), termo de nomeação,
  rituais (semanal de 30 minutos, mensal, trimestral), funil de ideias com ficha e matriz
  impacto × esforço, ata semanal, plano de 90 dias em semanas relativas, orçamento com ponto
  de equilíbrio e checklist de implantação. No solo, monta o bloco fixo semanal. Use quando
  o advogado disser "quem cuida da IA aqui?", "quero um responsável pela inovação", "montar
  o núcleo", "priorizar as ideias da equipe", "plano de 90 dias", "a equipe manda ideia e
  nada anda", "quanto custa manter isso", "eu faço tudo sozinho, como organizo meu tempo".
  Não use para conduzir o piloto com a equipe (use implantar-a-mudanca) nem para rodar as
  revisões mensal e trimestral (use revisao-periodica).
---

# Núcleo de inovação

> Alguém precisa ser dono da mudança. O núcleo é um setor como o financeiro: tem nome, responsável, agenda fixa e entregas. Sem ele, a IA vira assunto de quem tem tempo sobrando, e ninguém tem.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha, setores e escalas: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- O escritório decidiu estruturar a IA e precisa dizer quem conduz, com que tempo e com que autoridade.
- A equipe manda ideias de automação e nada anda, ou tudo anda ao mesmo tempo.
- É preciso um plano de 90 dias para sair do diagnóstico e chegar à primeira automação em uso.
- O titular quer saber quanto o núcleo custa e quantas horas ele precisa devolver para se pagar.
- O advogado solo quer organizar o próprio tempo para a mudança.

**Não use quando:**
- O pedido é rodar o piloto, a reunião de lançamento ou a conversa com quem resiste: use `implantar-a-mudanca`.
- O pedido é fazer a revisão mensal ou trimestral que o núcleo agenda: use `revisao-periodica`.
- O pedido é escrever a política de uso de IA: use `regra-de-uso-de-ia` (o guardião do núcleo cuida dela depois).
- O pedido é calcular o valor da hora e o retorno com detalhe: use `medir-retorno`.

## 2. Antes de começar

1. **Leia o perfil.** Abra `escritorio/perfil.md` (porte, trilha, nota, nível, setor-alvo). Leia o código do escritório e a regra de uso de IA, se existirem, e o diagnóstico mais recente em `escritorio/diagnosticos/`. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão:** o perfil precisa dizer o porte, porque o formato do núcleo depende dele. O ideal é já existir um diagnóstico (nota e setor-alvo). Se não existir, ofereça a `diagnostico` antes, em uma frase: o plano de 90 dias começa pela foto de hoje. Se o advogado quiser seguir, a semana 1 do plano inclui o diagnóstico, e isso fica registrado em "Etapas puladas".
3. **Código e regra de uso:** podem ainda não existir. O plano de 90 dias prevê o código v0 na semana 1 e a política v1 nas semanas 3 e 4.
4. **Descubra o momento.** Pergunte: "Você quer montar o núcleo do zero, priorizar ideias que já chegaram, montar o plano de 90 dias ou fazer a conta do orçamento?" Vá direto ao passo que corresponde.

## 3. Fluxo

### Passo 1. Missão e escopo
Leia para o advogado a missão e o escopo (seção 4) e pergunte: "Tem algo aqui que, no seu escritório, já é de outra pessoa?" Ajuste o "o que fica fora" com o nome da função que cuida hoje.

### Passo 2. Formato pelo porte
Mostre a linha do porte do escritório na tabela da seção 5. Para detalhes de cada faixa, leia `references/papeis-por-porte.md`.

### Passo 3. Nomear os papéis
Pergunte, uma por vez, sempre pela função:
1. "Quem é o patrocinador: a pessoa que decide orçamento e prioridade e protege a agenda do responsável?"
2. "Quem vai ser o responsável pela inovação?" Confira o perfil (seção 6). Se o titular de um escritório de 2 a 5 pessoas quiser acumular, avise do risco de virar gargalo e sugira repassar a condução a alguém organizado, ficando como patrocinador.
3. "Quem são os embaixadores?" Pelo porte: a equipe toda, um por setor principal, ou um por setor e por área.
4. "Quem é o guardião de governança e dados?" Precisa ter autoridade para dizer não e tempo para responder rápido.
5. "Quantas horas por semana o responsável terá reservadas, em que dia e horário?" Esse tempo só se remarca por prazo fatal ou audiência.

Papel e pessoa são coisas diferentes: a mesma pessoa pode ocupar dois papéis, desde que o termo diga quais.

### Passo 4. Termo de nomeação
Preencha `assets/termo-de-nomeacao.md` com as respostas. Mostre, ajuste e grave. Combine o momento de apresentar o núcleo à equipe: o termo é lido em voz alta e assinado pelo patrocinador e pelo nomeado. O escopo escrito é a proteção contra o risco mais comum: o núcleo virar "o setor do computador".

### Passo 5. Rituais na agenda
Pergunte o dia e o horário da reunião semanal de 30 minutos, a data da primeira mensal (primeira semana útil do mês) e a data da primeira trimestral (semanas 12 e 13 do plano). Explique a pauta (seção 7). As revisões mensal e trimestral são conduzidas pela `revisao-periodica`.

### Passo 6. Plano de 90 dias
Siga a seção 9. Pergunte só o que não está no perfil e no diagnóstico, uma pergunta por vez:
1. Áreas de atuação.
2. Número de pessoas e funções.
3. Nota e nível do diagnóstico, e as dimensões com nota mais baixa.
4. Setor-alvo.
5. Ferramentas de IA em uso hoje e tipo de conta.
6. Horas por semana que o escritório pode reservar para o núcleo.
7. Quem pode ser o responsável pela inovação (se ainda não foi nomeado).

Depois entregue: quem ocupa cada papel, considerando o porte; o plano semana a semana (ou por quinzena) com tarefas, responsável e entrega de cada período; dia e horário da reunião semanal com a pauta de 30 minutos; os riscos de o plano não andar neste escritório e o que fazer em cada um. Seja realista com as horas informadas. Não invente número de mercado. Marque como estimativa qualquer número sugerido. Use `assets/plano-90-dias.md`.

### Passo 7. Abrir o funil de ideias
Combine o canal único onde as fichas chegam (uma pasta, um formulário, um canal interno). Ideia dita de passagem no corredor não conta. Distribua `assets/ficha-de-ideia.md`. Siga a seção 8.

### Passo 8. Orçamento
Siga a seção 10. Se não houver valor da hora, ofereça a `medir-retorno` ou peça uma estimativa marcada como estimativa.

### Passo 9. Checklist de implantação
Mostre a seção 11 com o que já está feito marcado. Se o escritório só puder fazer uma coisa agora: escolher o responsável, reservar o horário fixo na agenda e marcar a primeira reunião de 30 minutos.

## 4. Missão e escopo

**Missão:** fazer o escritório trabalhar um pouco melhor toda semana, com a IA dentro dos processos e dentro da régua da cultura.

**O que o núcleo cuida:** adoção da IA pela equipe; POPs com S, A e H e com versão; base de conhecimento e Projeto do escritório no Claude; funil de ideias; política de uso de IA e incidentes, junto com o guardião; indicadores.

**O que o núcleo não faz:**
- Não define tese nem estratégia de caso (é do advogado responsável).
- Não reescreve sozinho o POP de outro setor (propõe; vale depois da aprovação do setor dono e do patrocinador).
- Não contrata ferramenta (recomenda, com números, e o patrocinador decide).
- Não cuida de gestão de pessoas.
- Não é suporte técnico de computador e impressora (fica com [QUEM CUIDA HOJE]).

## 5. Formato por porte

| Porte | Quem participa | Horas por semana | Como funciona | Entregas em 90 dias |
|---|---|---|---|---|
| Solo | Titular nos quatro papéis; secretária ou estagiário como embaixador, se houver | 3 a 4 h em bloco fixo "tratado como audiência" | A semanal vira os primeiros 20 min do bloco, por escrito | Código, POP do setor-alvo com IA, base no Projeto, 1 automação em uso, política de 1 página |
| 2 a 5 | Titular como patrocinador e guardião; responsável pode ser o titular ou a pessoa mais organizada; equipe toda como embaixadora | 2 a 4 h do responsável, mais 30 min semanais com todos | Semanal com todos | Tudo do solo, mais 2 setores com POP, funil ativo e painel mensal |
| 6 a 20 | Sócio patrocinador, responsável, um embaixador por setor principal, guardião (sócio ou administrativo) | 4 a 8 h do responsável, cerca de 1 h por embaixador | Semanal de 30 min só do núcleo | Setor-alvo automatizado, segundo setor em piloto, POPs principais com S, A e H, política assinada por todos, indicadores mensais |
| Mais de 20 | Comitê, responsável com dedicação parcial ou integral, embaixador por área e por setor, guardião formal ligado ao encarregado de dados | De um turno a dedicação integral do responsável; 1 a 2 h por embaixador | Semanal do núcleo e mensal com os sócios | Portfólio por área, POPs de todos os setores versionados, trilha de treino, relatório trimestral |

## 6. Os quatro papéis

| Papel | O que faz | Perfil | Sinal de alerta |
|---|---|---|---|
| Patrocinador | Assina o termo e apresenta o núcleo; protege a agenda do responsável; decide orçamento e prioridades; participa das revisões mensal e trimestral; dá o exemplo | Quem tem a palavra final sobre dinheiro e agenda | Cancelar a revisão mensal duas vezes seguidas |
| Responsável pela inovação | Conduz a semanal e escreve a ata; cuida das fichas e da matriz; mantém POPs e base; treina; preenche o painel | Organizado, curioso, respeitado, paciente para escrever processo | Foi escolhido por ser o mais novo "porque mexe no celular" (costuma dar errado); ou é o titular acumulando tudo num escritório de 2 a 5 |
| Embaixadores | Mandam fichas, testam pilotos, cuidam do POP do setor, avisam quando a IA erra ou alguém volta ao jeito antigo | Quem mais reclama de retrabalho; quem executa a tarefa, não quem só supervisiona | Embaixador que só supervisiona e nunca executa a tarefa |
| Guardião de governança e dados | Cuida da política e das assinaturas; avalia as ideias de risco alto; cuida dos incidentes; confere a conta e a anonimização | Advogado detalhista, com autoridade para dizer não e tempo para responder rápido | Sem tempo para responder: as fichas travadas acumulam e ele vira gargalo |

Quem ocupa cada papel em cada porte: `references/papeis-por-porte.md`.

**Quando acontece um incidente** (o dado saiu ou o erro chegou ao cliente), o guardião conduz cinco passos: conter (apagar a conversa, corrigir a mensagem); ser avisado no mesmo dia, pelo canal combinado, e quem avisa nunca é punido; registrar no livro, com fatos e sem caça a culpado (data, o que houve, dado, ferramenta, o que já foi feito), em `escritorio/06-medicao/incidentes.md`; avaliar com o patrocinador se é preciso comunicar o cliente ou outra parte `[CONFERIR]` com a orientação jurídica que o caso pedir; mudar o POP, porque todo incidente termina com um passo novo ou alterado. Quase incidente (a revisão pegou antes) também se registra. Meta "zero incidente" deixa todo mundo cego: número subindo no começo é bom sinal, o que preocupa é o incidente repetido.

## 7. Rituais do núcleo

| Ritual | Duração | Quem | Pauta |
|---|---|---|---|
| Semanal | 30 min | Equipe toda (2 a 5) ou só o núcleo (6 ou mais) | Placar 5 min · O que travou 10 min · Funil 10 min · Combinados 5 min |
| Mensal | 60 min, primeira semana útil | Núcleo e patrocinador | Painel; incidentes e o que mudou no POP; matriz; custo contra horas; decisão do patrocinador |
| Trimestral | 2 h, fora da rotina e de preferência fora do escritório | Núcleo e sócios | Refazer o diagnóstico; para cada POP, "o S ainda é S? algum A virou S? algum volta a H?"; revisar código, política e ferramentas autorizadas; rodízio de embaixadores; plano dos próximos 90 dias |

**Pauta da semanal em detalhe** (registrada em `assets/ata-semanal.md`):
1. **Placar (5 min):** o que a IA fez nos POPs na semana; horas estimadas; incidente ou quase incidente.
2. **O que travou (10 min):** até dois problemas, cada um com encaminhamento.
3. **Funil (10 min):** fichas novas; fichas pontuadas, com quadrante; fichas mandadas ao guardião; ideia em piloto e status.
4. **Combinados (5 min):** o quê, quem, até quando.

**Regra dos 30 minutos:** assunto que passa do tempo vira conversa separada, com duas ou três pessoas. A semanal não estica.

As revisões mensal e trimestral, e o registro de cada ritual feito ou cancelado, ficam com a `revisao-periodica`.

## 8. Funil de ideias

### Os sete passos
1. **Capturar:** ficha (`assets/ficha-de-ideia.md`) num canal único. Ideia dita de passagem não conta.
2. **Triar na semanal:** juntar repetidas, devolver o que está fora do escopo, mandar ao guardião o que tem dado sensível ou decisão humana.
3. **Pontuar:** quatro critérios de 1 a 5, cerca de 2 minutos por ideia.
4. **Posicionar na matriz.**
5. **Decidir:** o patrocinador escolhe uma ideia "Faça agora" por vez.
6. **Pilotar com POP:** o passo é marcado S, A ou H (pela `classificar-sah`), o embaixador testa por 2 semanas, com revisão humana em tudo. O piloto segue a `implantar-a-mudanca`.
7. **Medir e padronizar:** se deu certo, vai para o POP vigente, para o treino e para o painel. Se não deu, o aprendizado vai para a base e a ficha é arquivada com o motivo.

### Os quatro critérios (nota de 1 a 5)

| Critério | 1 | 5 |
|---|---|---|
| H · Horas por semana, somando quem faz | Menos de 1 h | Mais de 8 h |
| I · Incômodo (mesma escala do glossário) | Ninguém liga | Todo mundo reclama e o cliente percebe |
| R · Risco se a IA errar (dado sensível, prazo, fala com cliente?) | Erro interno, fácil de corrigir | Dano ao cliente, prazo perdido ou dado exposto |
| F · Facilidade (o quanto já está pronto) | Tudo do zero | POP escrito, modelo pronto, ferramenta em uso |

### A conta
- **Impacto = H + I** (vai de 2 a 10).
- **Esforço = (6 − F) + R** (vai de 2 a 10).
- **6 ou mais é alto.** Abaixo de 6 é baixo.
- **Risco 5 trava a ficha:** ela não entra na matriz e vai para o guardião, que sugere como redesenhar para baixar o risco (anonimização, conta profissional, revisão humana, trocar Substituição por Auxílio).

### A matriz

| | Esforço baixo (até 5) | Esforço alto (6 ou mais) |
|---|---|---|
| **Impacto alto (6 ou mais)** | **Faça agora:** uma por vez, piloto de 2 semanas | **Projeto do trimestre:** quebrar em partes menores |
| **Impacto baixo (até 5)** | **Encaixe quando sobrar:** bom para treinar | **Arquivo:** registrar o motivo e reavaliar no trimestre |

Mais o estado **Travada no guardião** (risco 5), fora da matriz.

### Exemplo resolvido

| Ideia | H | I | R | F | Impacto (H + I) | Esforço ((6 − F) + R) | Quadrante |
|---|---|---|---|---|---|---|---|
| Triagem no WhatsApp | 4 | 5 | 2 | 4 | 9 | 2 + 2 = 4 | Faça agora |
| Resumo mensal de andamento | 3 | 4 | 3 | 3 | 7 | 3 + 3 = 6 | Projeto do trimestre |
| Padronizar nome dos PDFs | 1 | 2 | 1 | 5 | 3 | 1 + 1 = 2 | Encaixe quando sobrar |
| Robô no site | 1 | 2 | 4 | 2 | 3 | 4 + 4 = 8 | Arquivo |
| IA analisa o laudo e manda parecer pelo WhatsApp | 3 | 4 | 5 | 3 | 7 | travada | Travada no guardião |

O guardião redesenha a última: laudo anonimizado, conta profissional, a IA faz A (prepara o resumo) e o advogado faz H (o parecer e a conversa com o cliente). O risco cai para 3. Nova conta: Impacto 7, Esforço (6 − 3) + 3 = 6. Vai para Projeto do trimestre.

### Fluxo para priorizar a lista de ideias
Quando o responsável trouxer as fichas ou uma lista (já anonimizada):
1. Para cada ideia, dê as quatro notas. Quando faltar informação para uma nota, pergunte em vez de chutar.
2. Calcule impacto e esforço e mostre a conta.
3. Ideia com risco 5 não entra na matriz: marque "Travada no guardião" e sugira o redesenho.
4. Para cada ideia, diga se o passo da IA seria S, A ou H, e por quê, pela árvore da `classificar-sah`.
5. Entregue a tabela (ideia, as quatro notas, impacto, esforço, quadrante), a ideia que deveria ser pilotada primeiro com justificativa curta, e, para cada Projeto do trimestre, como quebrar em partes menores.
6. A decisão é do patrocinador.

## 9. Plano de 90 dias

Semanas relativas, contadas a partir da semana em que o termo é assinado. O modelo para preencher está em `assets/plano-90-dias.md`.

| Semanas | Foco | Entregas |
|---|---|---|
| 1 | Nomear e tirar a foto | Termo assinado; nota do diagnóstico (`diagnostico`); código v0 (`codigo-do-escritorio`); setor-alvo |
| 2 | POP do setor-alvo | POP v1 com S, A e H (`escrever-pop`); embaixadores nomeados |
| 3 e 4 | Base, política e funil | Projeto no Claude com código, POP e modelos (`montar-base`); política v1 assinada (`regra-de-uso-de-ia`); fichas e matriz |
| 5 | Preparar a primeira automação | Checklist de prontidão (`desenhar-automacao`); 3 a 5 casos de teste anonimizados; conta profissional conferida; linha de base fechada (`medir-retorno`); ideia nº 1 escolhida; quem cobre o escritório no tempo de construção |
| 6 | Construir e ligar a primeira automação | Primeira automação rodando (`desenhar-automacao`, `pop-para-skill`); segunda nota do diagnóstico, para comparar com a semana 1 |
| 7 e 8 | Uso de verdade (aqui muita automação morre) | Automação dentro do POP vigente; setor treinado; revisão obrigatória funcionando; primeiro painel mensal |
| 9 e 10 | Segunda ideia e segundo setor | Segundo piloto; POP v2 |
| 11 | Arrumar a casa | Base limpa; lista de prompts oficiais |
| 12 e 13 | Primeira revisão trimestral | Terceira nota do diagnóstico; plano do próximo trimestre; tamanho do núcleo para o próximo ciclo (`revisao-periodica`) |

Se a base de conhecimento atrasar e não ficar pronta nas semanas 3 e 4, o Projeto é montado na semana 5, junto com a prontidão. O que não se pula é a semana 5: automação sem casos de teste e sem conta conferida é o jeito mais caro de descobrir que faltava organização.

## 10. Orçamento e ponto de equilíbrio

**Custo mensal do núcleo:**

| Item | Como estimar |
|---|---|
| Horas da equipe | Horas por semana × 4 × valor da hora |
| Assinaturas | Preço atual do plano × número de contas `[CONFERIR]` na configuração da conta |
| Treinamento | Valor total ÷ 12 (no orçamento mensal do núcleo o treinamento é diluído em 12 meses; no cálculo de retorno da `medir-retorno` ele entra como custo único. O total do ano é o mesmo.) |
| Reserva | Só com aprovação na revisão mensal |

**Ponto de equilíbrio** = custo mensal do núcleo ÷ valor da hora = horas devolvidas por mês de que o núcleo precisa para se pagar.

Duas regras: as horas da equipe entram no custo (no solo, as horas do titular no bloco fixo também); e o destino das horas devolvidas é decidido antes, porque hora devolvida sem destino evapora. O valor da hora precisa ser o mesmo número em todas as contas, pelo método anotado na `medir-retorno`.

**Exemplo (números ilustrativos):** escritório de 5 pessoas, valor da hora de R$ 120. Horas do núcleo: 6,5 h por semana × 4, cerca de 26 h, R$ 3.120. Assinaturas: R$ 600. Treinamento: R$ 300 por mês. Total: R$ 4.020. Ponto de equilíbrio: 4.020 ÷ 120, cerca de 34 h por mês (8 por semana). Se a triagem devolver 21 h e o resumo de andamento 16 h, são cerca de 37 h: com as duas, o núcleo se paga.

## 11. Checklist de implantação (18 itens)

1. Diagnóstico feito.
2. Papéis com nome.
3. Termo de nomeação assinado.
4. Núcleo apresentado à equipe.
5. Reunião semanal na agenda, com arquivo de ata.
6. Código v0.
7. Setor-alvo definido.
8. POP do setor-alvo com S, A e H.
9. Política v1 assinada.
10. Conta profissional conferida.
11. Livro de incidentes e canal de aviso.
12. Funil de ideias aberto.
13. Base de conhecimento montada.
14. Prontidão da primeira automação: casos de teste e plano para erro.
15. Medição do "antes" (uma semana).
16. Primeira automação em uso.
17. Primeiro painel mensal (por volta da semana 8).
18. Revisão trimestral marcada (semanas 12 e 13).

Se fizer uma coisa só: escolha o responsável, reserve o horário fixo na agenda e marque a primeira reunião de 30 minutos.

## 12. Indicadores do núcleo (5 + 1)

| Indicador | Como medir | Fonte | Frequência |
|---|---|---|---|
| Horas devolvidas | (antes − depois) × ocorrências no mês, com o "antes" medido uma semana antes do piloto | Cronômetro, software ou planilha | Mensal |
| POPs revisados com IA | POPs com S, A e H revistos nos últimos 90 dias | Pasta `03-pops/` versionada | Mensal |
| Adoção % | Pessoas que usaram IA dentro de um POP ÷ total da equipe (pergunta de sim ou não) | Pergunta na semanal | Mensal (não se aplica ao solo) |
| Incidentes de dados | Incidentes e quase incidentes, separados | Livro do guardião | Mensal |
| Nota do diagnóstico | Mesma pessoa, mesma sinceridade | `diagnostico` | Trimestral |
| Funil (apoio) | Fichas recebidas, pontuadas e em uso | Fichas e matriz | Mensal |

Não há meta padrão. A meta é definida na primeira revisão mensal, a partir do que foi medido no primeiro mês. O painel mensal é montado pela `revisao-periodica`.

## 13. O que entrega e onde grava

Tudo em `escritorio/01-cultura/nucleo/`, com nome, versão, data e dono no topo:

| Arquivo | Conteúdo |
|---|---|
| `termo-de-nomeacao.md` | Termo preenchido e assinado |
| `plano-90-dias.md` | Plano semana a semana, com responsáveis e riscos |
| `fichas/ideia-NNN-<nome-curto>.md` | Uma ficha por ideia, numerada pelo responsável |
| `matriz-de-ideias.md` | Tabela de todas as fichas com notas, conta e quadrante |
| `atas.md` | Atas das semanais, a mais recente no topo (um arquivo só, para mostrar a evolução) |
| `orcamento.md` | Custo mensal e ponto de equilíbrio |
| `o-que-eu-repeti.md` | Só no solo (seção 14) |

Mostre antes de gravar. Quando o termo estiver assinado e a semanal na agenda (ou o bloco fixo, no solo), marque no `perfil.md` o item "Mudança e núcleo / bloco fixo semanal".

## 14. Trilha solo e trilha equipe

**Solo: o bloco fixo.** O titular ocupa os quatro papéis. Se houver secretária ou estagiário, essa pessoa é a embaixadora. O núcleo vira um bloco fixo de 3 a 4 horas por semana, **tratado como audiência**: só se remarca por prazo fatal ou audiência de verdade. Exemplo: sexta, das 14h às 17h.

| Parte do bloco | O que fazer |
|---|---|
| Primeiros 20 min | A reunião semanal, por escrito, com a mesma pauta (placar, o que travou, funil, combinados), no mesmo arquivo de ata. É esse histórico que mostra a evolução na revisão trimestral |
| Primeira hora | Revisar o que a IA fez na semana e anotar os erros |
| Segunda hora | Trabalhar um item do funil |
| Terceira hora | Atualizar a base de conhecimento e o painel |

**O arquivo "o que eu repeti esta semana"** (`o-que-eu-repeti.md`) é o funil do solo. Durante a semana, cada vez que o titular faz uma tarefa pela segunda ou terceira vez, anota uma linha:

| Data | Tarefa (verbo + objeto, sem dado de cliente) | Quantas vezes na semana | Minutos cada vez | Setor | A IA poderia resumir, rascunhar, organizar, conferir ou responder? | Vira ficha? |
|---|---|---|---|---|---|---|

No bloco fixo, o que aparece em três semanas seguidas vira ficha de ideia e entra na matriz, com a mesma conta. A sugestão de três semanas é um critério prático, ajustável pelo titular.

No solo, o indicador de adoção não se aplica. Horas devolvidas, POPs revisados, incidentes e nota do diagnóstico valem igual. As horas do titular no bloco entram no custo do orçamento.

**Equipe.** Papéis com nome conforme o porte (seção 5 e `references/papeis-por-porte.md`), semanal de 30 minutos, mensal com o patrocinador, trimestral fora da rotina. Com 2 a 5 pessoas, todos participam da semanal. Com 6 a 20, só o núcleo. Com mais de 20, semanal do núcleo e mensal com os sócios. Quando o escritório muda de faixa de porte, os papéis e o guardião são revistos na revisão trimestral.

## 15. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Núcleo sem escopo escrito | Vira "o setor do computador" | O que fica fora está no termo e é lido na apresentação |
| Responsável escolhido por ser o mais novo | Ninguém escreve processo nem segura a agenda | Perfil do papel e sinal de alerta |
| Titular acumulando tudo em equipe pequena | O núcleo para quando o titular está em audiência | Sugestão de repassar a condução e ficar como patrocinador |
| Três pilotos ao mesmo tempo | Nenhum termina | Uma ideia "Faça agora" por vez |
| Ideia de risco alto direto no piloto | Laudo numa conta gratuita | Risco 5 trava no guardião |
| Semanal que estica | A reunião morre na terceira semana | Regra dos 30 minutos |
| Plano amarrado a datas externas | O plano envelhece no primeiro atraso | Semanas relativas, de 1 a 13 |
| Horas devolvidas sem destino | O ganho some e ninguém percebe | Destino decidido antes, no orçamento |

## 16. Próximo passo

- Com os papéis nomeados e o piloto ainda por começar: `implantar-a-mudanca`.
- Se o setor-alvo ainda é provisório: `mapear-setores`.
- Para manter a semanal, montar o painel mensal e fazer a trimestral: `revisao-periodica`.
