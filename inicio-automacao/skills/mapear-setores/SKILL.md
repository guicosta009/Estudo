---
name: mapear-setores
description: >
  Mapeia para onde vão as horas do escritório em uma semana de medição: inventário dos 10
  setores com dono, atividades em verbo + objeto, entrevistas com quem executa (ou
  auto-observação no escritório solo), registro de horas com tempo picado, classificação S,
  A ou H, ranking por horas × incômodo × potencial de IA, plano 5W2H do setor-alvo e revisão
  quinzenal. Gera a planilha de registro e calcula o ranking. Use quando o advogado disser
  "mapear os setores", "para onde vão as horas", "qual setor automatizar primeiro",
  "confirmar o setor-alvo", "planilha de horas", "registro de horas da semana", "ranking de
  setores", "entrevistar a equipe sobre o trabalho", "plano 5W2H". Não use para classificar
  passos de um POP já escrito (use classificar-sah) nem para medir horas devolvidas depois
  da automação (use medir-retorno).
---

# Mapear setores

> Troca o palpite do diagnóstico por medição: desce do setor para a atividade, mede uma semana normal e termina com o setor-alvo confirmado, o próximo da fila e um plano 5W2H com dono e data.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, os 10 setores, as escalas de horas, incômodo e potencial e a regra do setor-alvo: `../../docs/glossario.md`. O que muda por porte: `../../docs/trilhas.md`.

"A IA só devolve horas onde existem horas para devolver." Todo advogado acha que sabe para onde vão as horas do escritório e quase sempre erra no mesmo lugar: no tempo picado, naquela mensagem de WhatsApp de dois minutos que acontece quarenta vezes por dia. Escolher o setor errado é gastar a energia numa tarefa de vinte minutos por semana enquanto o setor que sangra continua igual. É enxugar gelo com ferramenta nova.

## 1. Quando usar

**Use quando:**
- O diagnóstico já deu um setor-alvo provisório e o advogado quer confirmar com dado real antes de escrever o POP.
- O escritório não sabe por onde começar a automação e quer decidir com número.
- O setor-alvo caiu do 1º lugar, alguém entrou ou saiu da equipe, abriu uma área nova ou passaram 6 meses: é hora de refazer o mapa.
- O advogado quer a planilha de horas, o ranking a partir de um registro já feito ou o 5W2H do setor-alvo.

**Não use quando:**
- O pedido é marcar S, A ou H nos passos de um processo já descrito: use `classificar-sah` (esta skill chama aquela no passo 5).
- O pedido é escrever o POP do setor-alvo: use `escrever-pop`.
- A automação já roda e a pergunta é quanto tempo ela devolveu: use `medir-retorno`.

## 2. Antes de começar

1. Leia `escritorio/perfil.md` (trilha, porte, pessoas por função, áreas, conta de IA, `setor_alvo`) e, se existirem, o código do escritório e a regra de uso de IA. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão:** o ideal é que o `diagnostico` já tenha rodado, com o setor-alvo provisório (pelo mapa rápido de horas × incômodo) gravado no perfil. Se não rodou, explique em uma frase que o diagnóstico dá o primeiro palpite em 5 minutos e serve de comparação no passo 6, e ofereça o `diagnostico`. Se o advogado quiser seguir sem ele, siga: o passo 6 compara com o 1º lugar de horas × incômodo medido. Registre em "Etapas puladas".
3. **Atalho "só tenho meia hora":** se o advogado não tem a semana de medição agora, o setor-alvo do diagnóstico basta para seguir para o POP. Diga isso com clareza, ofereça o `escrever-pop` e anote no perfil, em "Etapas puladas", que o mapa completo ficou para depois (sugira refazer na primeira revisão quinzenal).
4. **Combine a semana.** O mapeamento completo leva uma semana. Agenda sugerida, em dias do próprio escritório:
   - Dia 1 de manhã: passos 1 e 2. À tarde, avisar a equipe e começar o passo 4.
   - Dias 1 a 5: registro rodando, com uma entrevista por dia (trilha equipe).
   - Dia 6 ou 7: passos 5 e 6 e, se der, o rascunho do 5W2H.
   - Semana 2: passo 7. A partir daí, o passo 8 a cada 15 dias.
5. Pergunte: "Que semana dá para registrar? Precisa ser normal: sem feriado, sem mutirão, sem metade da equipe de férias."

## 3. O método em 8 passos

Os tempos valem para escritório pequeno ou médio. No solo, quase tudo cai pela metade.

| Passo | O que faz | Tempo | Quem | Entregável |
|---|---|---|---|---|
| 1 Inventário de setores | Confere os 10 setores e adapta | 30 min | Titular e sócios | Lista de setores, cada um com dono |
| 2 Inventário de atividades | Quebra cada setor em verbo + objeto | 1 a 2 h | Titular e dono de cada setor | 1ª lista de atividades |
| 3 Entrevistas | Conversa com quem executa e corrige a lista | 30 a 40 min por pessoa | Quem executa | Lista revisada, com exceções e travas |
| 4 Registro de horas | Todos anotam por 5 dias úteis | 5 min por dia | Toda a equipe, inclusive o titular | Horas por setor e por atividade |
| 5 Classificação | Volume, frequência, regra, risco, dado sensível: S, A ou H | 1 h | Titular e dono do setor | Atividades classificadas |
| 6 Priorização | Horas × incômodo × potencial | 20 min | Titular e sócios | Ranking e setor-alvo confirmado |
| 7 5W2H | Plano do setor-alvo | 45 min | Titular e responsável | Plano com datas |
| 8 Acompanhamento | Revisão a cada 15 dias | 15 a 20 min | Titular e responsável | Antes e depois |

### Passo 1. Inventário de setores
Mostre os 10 setores do glossário e pergunte, um de cada vez quando precisar:
1. "Algum destes não existe no escritório?" Risque o que não existe ("não temos").
2. "Quem é o dono de cada setor? Um nome por setor, mesmo que seja você em seis." Setor sem dono é setor que ninguém mede e ninguém melhora. Grave por função, e o nome só se o advogado quiser.
3. "Tem setor que a mesma pessoa faz junto com outro, no mesmo fluxo, sem pausa?" **Fundir** quando a mesma pessoa faz os dois setores no mesmo fluxo (caso clássico: Atendimento e triagem com Comercial). Mesmo fundidos, tente anotar as horas separadas.
4. "Tem setor com dois fluxos tão diferentes que não cabem num POP só?" **Separar** mantendo o nome oficial e acrescentando a área: "Produção de peças · Previdenciário". Anote cada decisão de fundir ou separar.
5. "Além do dono, quem mais toca cada setor?" Essa lista define os entrevistados do passo 3 e quem anota horas no passo 4.
6. **Setor terceirizado** (contador, agência, correspondente, cobrança) continua no mapa: contam as horas de coordenação (conferir, responder, cobrar entrega).

### Passo 2. Inventário de atividades
Para cada setor que ficou, pergunte: "O que acontece nesse setor numa semana normal? Me fala como se estivesse contando para quem chegou ontem." Reescreva cada resposta em **verbo + objeto**, com tamanho entre 5 minutos e 2 horas. Atividade maior esconde outras: quebre. Use a tabela "como costuma aparecer → como escrever" e as atividades de exemplo por setor, com palpite S, A ou H, em `references/atividades-por-setor.md`. O palpite é provisório. Mostre a lista e peça ok.

### Passo 3. Entrevistas (equipe) ou auto-observação (solo)
Leia `references/entrevistas.md`.
- **Trilha equipe:** pergunte "Prefere conduzir você mesmo com o roteiro de 15 perguntas, ou que a pessoa responda direto ao Claude?". No primeiro caso, entregue o roteiro. No segundo, siga o modo B (a pessoa responde aqui, uma pergunta por vez, ou cola o texto pronto no Projeto do escritório). Entreviste quem executa, titular e assistente separados.
- **Trilha solo:** pule as entrevistas e rode a auto-observação (modo C) no segundo ou terceiro dia do registro. A pergunta deixa de ser "quem faz" e vira "**em que hora do dia você faz e o que fica para trás quando faz**".
- Em qualquer modo: retrato, sem propor melhoria. Atualize `atividades-<setor>.md` com as atividades novas, as exceções, as travas e os modelos pessoais citados.

### Passo 4. Registro de horas
1. Pergunte: "Prefere a planilha pronta (.xlsx) ou um modelo simples para colar em qualquer planilha?"
   - **.xlsx:** rode `scripts/gerar_planilha_horas.py` (seção 4) e grave em `escritorio/02-mapa/registro-de-horas.xlsx`.
   - **Sem openpyxl ou sem planilha:** o script avisa e explica a instalação. A alternativa é `assets/registro-de-horas.tsv`, com as mesmas colunas da aba Registro (colado numa planilha, cada coluna cai no lugar). Para incômodo e potencial, `assets/incomodo-potencial.csv`.
2. Regras do registro, para passar à equipe:
   - Semana normal. Se sair atípica no meio, anotar o motivo e repetir depois.
   - Todo mundo anota, inclusive o titular, cada um na sua aba ou na sua coluna Pessoa.
   - Anotar no momento em que o bloco termina. No fim do dia a memória já apagou metade das interrupções.
   - Uma linha por bloco, em verbo + objeto, com o setor ao lado. Bloco abaixo de 5 minutos vai para a rajada.
   - Sem nome de cliente. "Responder dúvida de andamento" basta. A planilha vai passar pela IA e precisa nascer limpa.
   - Fechar somando por setor (minutos ÷ 60), ou pelo ranking do passo 6.
3. **Tempo picado** (é o que mais se subestima e onde a IA costuma devolver mais horas):
   - **WhatsApp por rajada:** um risquinho num papel a cada mensagem respondida. No fim do dia, risquinhos × tempo médio, numa linha só. Exemplo de linha: "Responder mensagens curtas (rajada) | 48 | WhatsApp | Sim | 12 mensagens x 4 min".
   - **Tempo médio:** no primeiro dia, cronometrar 10 respostas com o relógio do celular. Exemplo: 10 respostas somaram 38 minutos, a média fica perto de 4 minutos.
   - **Ligações:** pelo histórico do celular, somar as do trabalho no fim do dia e lançar por setor, mais uns minutos por ligação para o que vem depois (anotar, avisar alguém, procurar documento).
   - **Interrupções:** "Sim" na coluna "Interrompida?" sempre que o bloco foi cortado no meio. Muitas no mesmo setor indicam setor sem fluxo e pesam no incômodo.
4. **Trilha equipe:** combine antes: "ninguém está batendo ponto". O número que interessa é o do setor. Olhar por pessoa só serve para decidir quem entrevistar de novo. Ofereça um texto curto de aviso, em tom de conversa.

### Passo 5. Classificação S, A ou H
Chame a skill `classificar-sah` com a lista de atividades do setor-alvo (e dos setores que o advogado quiser), passando o volume por mês e a frequência tirados do registro. Os cinco critérios do mapeamento: volume (vezes por mês), frequência (diária, semanal, mensal ou eventual; atividade eventual raramente é a primeira a automatizar), regra clara (sim, parcial ou não), risco se errar (baixo, médio ou alto) e dado sensível (sim ou não). S só com volume alto, regra clara e risco baixo, as três juntas. Na dúvida, a sigla mais humana. A classificação devolve o **potencial de IA do setor** (1 a 5), que entra no passo 6. Grave em `atividades-<setor>.md`.

### Passo 6. Priorização
1. Peça o incômodo de cada setor (escala 1 a 5 do glossário), dado por quem executa. Na trilha equipe, pergunte a quem toca o setor, não só ao titular.
2. Rode `scripts/ranking_setores.py` com o registro e o arquivo de incômodo e potencial (seção 4). Sem arquivos, faça a mesma conta na conversa, com as mesmas regras.
3. **Confirme as linhas suspeitas antes de corrigir** (setor em branco, atividade vaga, mais de 10 horas no mesmo dia para a mesma pessoa, possível dado de cliente). Nunca invente horas que não estão no registro: o que faltar vira `[A CONFIRMAR]`.
4. Aplique a regra da seção 5 e mostre a leitura e o "ranking em texto".
5. Pergunte: "Confirma o setor-alvo e o próximo da fila?" Só depois atualize o perfil.

### Passo 7. Plano 5W2H do setor-alvo
Leia `references/plano-5w2h.md`. Faça até cinco perguntas, uma por vez, sobre o que faltar (responsável, ferramentas, conta de IA, prazo realista, meta). Monte o 5W2H com os sete campos, um responsável só, passos com S, A ou H, a linha fixa de cuidado com dado de cliente e `[A DEFINIR]` onde faltar número. Termine sugerindo os três indicadores da revisão quinzenal.

### Passo 8. Acompanhamento quinzenal
Proponha um dia fixo da semana, a cada 15 dias, de 15 a 20 minutos:
- **Números:** horas da última semana medida e incômodo de hoje, dado por quem executa.
- **Plano:** o que andou no 5W2H, o que atrasou e por quê.
- **Erros da IA:** onde a saída precisou ser refeita. Cada erro repetido vira ajuste no POP ou na base.
- **Próximos 15 dias:** uma ou duas ações, cada uma com dono e data.

O que medir:

| Indicador | Como medir | Quando |
|---|---|---|
| Horas por semana do setor-alvo | O mesmo registro do passo 4, só para quem toca o setor-alvo | Uma semana por mês |
| Incômodo | Nota de 1 a 5 dada por quem executa, na mesma escala do diagnóstico | Toda revisão |
| Ações do 5W2H no prazo | Concluídas no prazo ÷ previstas para o período | Toda revisão |
| Retrabalho da IA | Quantas vezes a saída da IA foi refeita, e em que passo | Anotado na semana, somado na revisão |
| Indicador do próprio setor (escolher 1) | Relacionamento: tempo até a primeira resposta ao cliente · Prazos: tarefas concluídas antes do vencimento · Peças: ajustes pedidos na revisão (outros setores: lista em `medir-retorno`) | Toda revisão |

Marcos sugeridos: primeira revisão 15 dias depois do POP escrito · novo diagnóstico na revisão trimestral (`revisao-periodica`) · primeira medição depois de pelo menos 4 semanas de uso da automação (`medir-retorno`, uma semana só do setor-alvo).

## 4. Os scripts

Rode a partir da pasta desta skill. Mostre o comando ao advogado antes de rodar.

**Planilha de registro (.xlsx, requer openpyxl):**
```
python3 scripts/gerar_planilha_horas.py escritorio/02-mapa/registro-de-horas.xlsx \
  --escritorio "[NOME]" --pessoas "Advogada titular; Assistente; Estagiário" \
  [--inicio AAAA-MM-DD] [--dias 5] [--valor-hora 120] \
  [--setor-extra "Produção de peças · Previdenciário"] [--solo]
```
Abas: Comece aqui (instruções, tempo picado, siglas, sigilo), Configuração (escritório, início, dias úteis, valor da hora opcional, pessoas por função, incômodo, potencial e dono por setor, com validação de 1 a 5), Registro (500 linhas, listas de pessoa, setor, canal, Sim/Não e S/A/H; minutos e horas por fórmula), Resumo por setor (horas, horas por semana e por mês, as duas pontuações, ranking, horas S, A e H, valor das horas, setor-alvo pelas duas contas), Por pessoa e Classificação de atividades. Amarelo claro é para preencher, cinza é fórmula. Se o openpyxl faltar, o script explica a instalação (`python3 -m pip install openpyxl`) e indica `assets/registro-de-horas.tsv`.

**Ranking (biblioteca padrão):**
```
python3 scripts/ranking_setores.py REGISTRO.csv INCOMODO.csv --dias 5 \
  --escritorio "[NOME]" --dono "[FUNÇÃO]" --alvo-diagnostico "[SETOR DO PERFIL]" \
  --saida escritorio/02-mapa/ranking-de-setores.md
```
Lê o registro em CSV ou TSV (as colunas do material, ou a aba Registro exportada) e o incômodo e potencial por setor em CSV (`Setor, Incômodo, Potencial, Dono`) ou JSON. Entrega: horas por setor e por pessoa (`--sem-pessoas` para omitir), as 10 atividades que mais consumiram horas, as linhas suspeitas, a pontuação do diagnóstico e a completa, o ranking com desempate, a regra de discordância, `setor_alvo` e `proximo_da_fila`, e o ranking em texto. Quando o registro tem a coluna S/A/H, o script também mostra o potencial que as marcações sugerem, para comparar com o informado. Exemplo para testar: `scripts/exemplos/registro-exemplo.csv` com `scripts/exemplos/setores-exemplo.csv`.

## 5. Pontuação e regra de decisão

- **Pontuação do diagnóstico** = horas por semana × incômodo.
- **Pontuação completa** = horas por semana × incômodo × potencial de IA. Empate: vence o setor com mais horas.
- Horas por semana = horas registradas ÷ dias úteis registrados × 5. Horas por mês = horas por semana × 52 ÷ 12.

**Quando as duas contas discordam** (o setor do diagnóstico, provisório, e o 1º da pontuação completa):
- Mesmo 1º lugar: está decidido.
- O setor do diagnóstico tem potencial 1 ou 2: troque pelo da pontuação completa.
- O setor do diagnóstico tem potencial 3 ou mais: fique com o do diagnóstico e deixe o outro como "próximo da fila".

Quando as contas concordam, o próximo da fila é o 2º lugar da pontuação completa. "O modelo de negócio orienta, o mapa decide", e o ranking existe para proteger o advogado do setor de estimação.

**Exemplo resolvido** (números fictícios, escritório de Previdenciário com 5 pessoas; horas, incômodo, potencial):

| Posição | Setor | Conta | Pontuação |
|---|---|---|---|
| 1 | Relacionamento com o cliente | 18 × 5 × 4 | 360 |
| 2 | Produção de peças | 25 × 3 × 4 | 300 |
| 3 | Atendimento e triagem | 12 × 4 × 4 | 192 |
| 4 | Prazos e controladoria | 8 × 4 × 4 | 128 |
| 5 | Administrativo | 6 × 3 × 3 | 54 |
| 6 | Financeiro e cobrança | 4 × 3 × 4 | 48 |
| 7 | Comercial | 5 × 3 × 3 | 45 |
| 8 | Audiências e diligências | 6 × 2 × 2 | 24 |
| 9 | Marketing e conteúdo | 3 × 2 × 4 | 24 |
| 10 | Gestão de equipe | 4 × 2 × 2 | 16 |

Relacionamento fica em 1º pelas duas contas (horas × incômodo = 90, também o maior): setor-alvo confirmado, Produção de peças como próximo da fila. Audiências e Marketing empatam em 24, e Audiências vem antes por ter mais horas.

**Ranking em texto** (para colar no Projeto do escritório no Claude): uma linha por setor no formato `1. Setor: 18 h × 5 × 4 = 360 (horas × incômodo = 90)`, seguida do setor-alvo pelas duas contas, do decidido, do próximo da fila e das horas por semana mapeadas. O script já entrega nesse formato.

## 6. O que entrega e onde grava

Tudo em `escritorio/02-mapa/`, com nome, versão, data da revisão e dono no topo. Mostre cada documento antes de gravar.

| Arquivo | Conteúdo |
|---|---|
| `registro-de-horas.xlsx` | A planilha da semana (ou o TSV equivalente, salvo como `registro-de-horas.tsv`) |
| `atividades-<setor>.md` | Atividades em verbo + objeto, quem toca o setor, decisões de fundir e separar, exceções, travas, modelos pessoais e, depois do passo 5, a classificação S, A ou H |
| `ranking-de-setores.md` | A saída do passo 6: horas por setor e por pessoa, top 10, linhas suspeitas resolvidas, pontuações, leitura e ranking em texto |
| `plano-5w2h-<setor>.md` | O plano do setor-alvo, com o dia da revisão quinzenal |

Nome do setor no arquivo: minúsculas, sem acento, hífen no lugar do espaço (`relacionamento-com-o-cliente`).

**No `perfil.md`,** depois do ok: atualize `setor_alvo` e `proximo_da_fila`, `atualizado_em`, marque "Mapa de setores e setor-alvo confirmado" no Progresso e acrescente uma linha no Histórico ("AAAA-MM-DD: setor-alvo confirmado pelo mapeamento: [SETOR]; próximo da fila: [SETOR]"). Se o setor-alvo mudou em relação ao diagnóstico, diga isso na linha.

## 7. Trilha solo e trilha equipe

**Solo:**
- O titular é o dono de todos os setores. A pergunta deixa de ser "quem faz" e vira "em que hora do dia você faz e o que fica para trás quando faz".
- Sem entrevistas: auto-observação (modo C de `references/entrevistas.md`). O registro de horas é reforçado, "porque no solo é ele que mostra a verdade". Ofereça a coluna Observação para "o que ficou para trás".
- Tempos do método caem pela metade. Gestão de equipe pode ser riscado (se houver estagiário ou secretária, fica, e essa pessoa é a embaixadora do método e anota as próprias horas).
- Quase tudo se funde no inventário. Mesmo assim, anote as horas separadas por setor.
- Terceirizados pesam proporcionalmente mais: conte com cuidado as horas de coordenação.
- No 5W2H, o responsável é o titular. Gatilho especial para refazer o mapa: contratar a primeira pessoa (e aí o mapeamento volta com entrevistas).

**Equipe:**
- Entrevistas com quem executa: roteiro de 15 perguntas ou o colaborador respondendo direto ao Claude.
- Aba "Por pessoa" na planilha e tabela por pessoa no ranking, para a conversa com a equipe, nunca como cobrança individual.
- Combinar antes que ninguém está batendo ponto, mostrar só o total por setor e pedir o incômodo a quem executa.
- Entrada ou saída de pessoa refaz o mapa.

## 8. Erros que a skill evita (os 10 erros comuns)

| Erro | O que acontece | Como a skill evita |
|---|---|---|
| Mapear o organograma | Lista cargos em vez de trabalho | O mapa mostra o que acontece; quem faz entra como coluna |
| Ouvir só o titular | O sócio descreve o setor como deveria ser, e o POP nasce torto | Entrevista quem executa, separado do titular |
| Esquecer o tempo picado | Só os blocos grandes contam e o ranking distorce | Rajada, tempo médio cronometrado, histórico de ligações |
| Atividade sem verbo | "Clientes", "financeiro", "prazos" não se medem nem viram passo de POP | Verbo + objeto e alerta do script |
| Escolher o setor de estimação | Mexe no setor de que gosta, não no que dói | Ranking pelas duas contas e regra de discordância |
| Querer o setor inteiro de uma vez | O plano vira lista de desejos | Começa pelas atividades S e A de maior volume |
| Registro que parece vigilância | Os números saem arrumados e inúteis | Combinado prévio e só o total por setor |
| Dado de cliente na planilha | Nome, processo ou diagnóstico médico vão para a IA | Regra de sigilo na planilha e alerta de número longo no script |
| Escolher a ferramenta antes do mapa | Contrata software e depois procura onde usar | O mapa vem primeiro, a ferramenta segue o mapa |
| Mapear e engavetar | O mapa morre na pasta | 5W2H com dono e data e revisão em 15 dias |

## 9. Checklist

Os itens com * são o mínimo para seguir para o POP.
- [ ] Setores conferidos e com dono *
- [ ] Atividades em verbo + objeto *
- [ ] Equipe avisada (trilha equipe)
- [ ] Entrevistas feitas (equipe) ou auto-observação (solo)
- [ ] 5 dias de registro
- [ ] Planilha sem dado de cliente
- [ ] Classificação S, A ou H *
- [ ] Potencial de IA definido por setor
- [ ] Ranking e setor-alvo confirmado *
- [ ] Ranking em texto salvo no Projeto do escritório
- [ ] 5W2H preenchido
- [ ] Revisão quinzenal agendada

**Quando refazer o mapa inteiro:** o setor-alvo caiu do 1º lugar (sinal de que funcionou); alguém entrou ou saiu da equipe; o escritório abriu uma área nova ou mudou o modelo de negócio; no mínimo a cada 6 meses, mesmo que nada pareça ter mudado.

## 10. Próximo passo

- Setor-alvo confirmado: `escrever-pop`, para transformar as atividades do setor em POP com S, A e H. As atividades e os tempos medidos entram direto no passo a passo.
- Ao mesmo tempo, a semana registrada já serve de ponto de partida para a linha de base: ofereça o `medir-retorno` para calcular o valor da hora e congelar a linha de base do setor-alvo antes de qualquer mudança.
- Se a classificação mostrou que falta critério escrito ou modelo, anote para a `montar-base`.
