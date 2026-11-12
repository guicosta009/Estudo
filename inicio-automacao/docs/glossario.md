# Glossário e definições canônicas

Todas as skills usam estes nomes, escalas e regras exatamente como estão aqui. Se precisar de uma definição, copie daqui em vez de reescrever.

## A equação da automação

> **Automação é um POP executado pela IA, consultando a base de conhecimento e dentro da régua da cultura.**

| Peça | Papel | Onde mora na pasta |
|---|---|---|
| Código do escritório | **A régua**: tom, limites, quem decide, o que a IA nunca faz em nome do escritório | `01-cultura/` |
| Setor-alvo e horas | **O endereço**: por onde começar | `02-mapa/` |
| POP com S, A e H | **O roteiro**: o que acontece em cada passo e quem faz | `03-pops/` |
| Base de conhecimento | **A memória**: modelos, teses, checklists, critérios, respostas aprovadas | `04-base/` |
| Linha de base de horas | **A prova**: o antes, para comparar com o depois | `06-medicao/` |

O que acontece quando falta uma peça:
- **Sem cultura:** a IA produz rápido, mas no tom errado, e cada pessoa usa de um jeito ("quatro escritórios dentro de um"). Ninguém sabe dizer se o resultado está bom.
- **Sem POP:** a IA não sabe o próximo passo. O advogado vira o fluxo e continua sendo o gargalo.
- **Sem base:** a IA preenche o vazio com o que acha. Sai tese genérica, modelo que não é do escritório e, no pior caso, informação errada assinada pelo escritório.

"Automatizar o caos continua sendo caos, só que com mais velocidade."

## S, A e H

Todo POP escrito antes da IA está antigo, porque supõe uma pessoa fazendo cada passo do começo ao fim. Com a IA no fluxo, cada passo recebe uma sigla:

| Sigla | Nome | O que significa | Exemplos |
|---|---|---|---|
| **S** | Substituição | A IA faz no lugar. Alguém confere por amostra ou nas exceções. | Classificar publicação, renomear arquivo, preencher planilha, resumo interno |
| **A** | Auxílio | A IA prepara, resume, rascunha ou revisa. A pessoa é dona do passo e decide. | Minuta de petição, mensagem de cobrança, resumo para audiência, resposta a dúvida de cliente |
| **H** | Humano | Continua com a pessoa. A IA pode preparar o terreno, mas não executa o passo. | Escolher tese, dar notícia ruim, negociar honorário, assinar peça |

**Regra de leitura da sigla:** a sigla diz quem é dono do resultado do passo. Se a IA produz e alguém só confere por amostra, é S. Se a IA produz e a pessoa revisa tudo antes de seguir, é A. Também é A quando a pessoa produz e a IA revisa o trabalho dela (por exemplo, conferir uma peça contra o checklist), porque quem decide continua sendo a pessoa. Se a pessoa faz e decide, com a IA no máximo preparando material em volta, é H. A conferência é registrada à parte, no campo "Confere" do passo.

A árvore de decisão, os seis critérios e a trava por estágio estão na skill `classificar-sah`.

## A linha vermelha

Cinco passos que são sempre H, em qualquer nível: escolha de tese ou estratégia; notícia ruim ao cliente; assinatura e responsabilidade técnica; aconselhamento de cliente em situação de vulnerabilidade; envio de peça, proposta ou mensagem jurídica sem revisão humana. "Nenhum passo H some: ele só passa a receber material mais bem preparado."

## Os cinco níveis de inserção da IA

| Nível | Nome | Como é | O que exige |
|---|---|---|---|
| 1 | Uso pontual | Pergunta solta, cada conversa do zero | Regra de uso de IA (o que pode ir, o que nunca vai, com qual conta). Revisão em tudo. |
| 2 | Assistente com contexto | Projeto no Claude com o código do escritório e os modelos mais usados | Código escrito e colocado no Projeto; modelos com nomes claros |
| 3 | Copiloto dentro do POP | Uma instrução definida para cada passo S e A do POP | Código e regra conhecidos por todos; POP com S, A e H; base com o que o POP cita. Revisão sempre nos A, por amostra nos S. |
| 4 | Automação de fluxo | Roda do gatilho à entrega, com revisão humana em pontos fixos | POP estável, já rodado à mão no nível 3; base completa com dono e data; responsável pela automação; plano para erro |
| 5 | Agentes | Executa várias etapas, escolhe o próximo passo dentro de limites escritos e para na fronteira | Vários POPs maduros conectados; limites de autonomia escritos; registro de tudo o que consultou e fez |

Regras de ordem: subir um ou dois níveis por vez; rodar o POP à mão no nível 3 antes de levar ao 4; nível 5 só depois de fluxos estáveis no 4. "Começar pelo agente, sem POP e sem base, é o jeito mais caro de descobrir que faltava organização."

## Os 10 setores

Use sempre estes nomes:

| Setor | O que entra nele |
|---|---|
| Atendimento e triagem | Primeiro contato, consulta inicial, coleta de documentos para análise |
| Comercial | Proposta de honorários, contrato, negociação e fechamento |
| Produção de peças | Petições, recursos, pareceres, cálculos que acompanham a peça |
| Prazos e controladoria | Publicações, intimações, agenda e distribuição de tarefas |
| Audiências e diligências | Preparo, deslocamento, atas e retorno ao cliente |
| Financeiro e cobrança | Honorários, boletos, repasses e inadimplência |
| Relacionamento com o cliente | Atualização de andamento, dúvidas, WhatsApp do dia a dia |
| Marketing e conteúdo | Redes sociais, site, anúncios e materiais |
| Gestão de equipe | Contratação, treinamento, rotina e reuniões |
| Administrativo | Documentos, protocolos, arquivo e organização geral |

Setor terceirizado (contador, agência, correspondente) continua no mapa: contam as horas de coordenação.

## Escalas

**Horas por semana** (faixas do diagnóstico e valor usado na conta): Não temos = 0 · 1 a 3 h = 2 · 4 a 8 h = 6 · 9 a 15 h = 12 · 16 a 25 h = 20 · 26 h ou mais = 30. Somar o tempo de todo mundo que toca o setor e contar o tempo picado (WhatsApp, ligação rápida, procurar documento). Na dúvida entre duas faixas, a maior.

**Incômodo (1 a 5):**
1. Quase não lembro que existe.
2. Dá trabalho, mas anda sozinho.
3. Incomoda toda semana, alguém sempre reclama.
4. Gera retrabalho, atraso ou hora extra com frequência.
5. Cliente reclama, prazo fica em risco ou tira o seu sono.

**Potencial de IA do setor (1 a 5),** pela parte das horas do setor que cabe em S ou A: 1 menos de 20% · 2 de 20% a 40% · 3 de 40% a 60% · 4 de 60% a 80% · 5 mais de 80%. As faixas são um critério prático e ajustável.

## Setor-alvo

- **Pelo diagnóstico (rápido):** horas × incômodo. O maior vira o setor-alvo provisório. Empate: vence o setor com mais horas.
- **Pelo mapeamento (completo):** horas medidas × incômodo × potencial de IA.
- **Quando as duas contas discordam:** se o setor do diagnóstico tem potencial 1 ou 2, troque pelo da conta completa. Se tem potencial 3 ou mais, fique com o do diagnóstico e deixe o outro como "próximo da fila".
- "O modelo de negócio orienta, o mapa decide."

## Níveis do diagnóstico

| Nota | Nível | Leitura |
|---|---|---|
| 0 a 25 | Zero | O escritório roda na cabeça das pessoas. Automatizar agora seria acelerar a bagunça, mas é aqui que cada passo dá mais retorno. |
| 26 a 50 | Base | Existe organização, mas ela não está escrita. O trabalho é tirar da cabeça e colocar no papel, onde a IA consegue ler. |
| 51 a 75 | Estrutura | Processos escritos em parte e IA em uso pontual. Falta fechar as lacunas e padronizar o uso. |
| 76 a 100 | Automação | Cultura, processos e base no lugar. Agora é conectar a IA ao fluxo real e medir as horas que ela devolve. |

A nota é uma foto de hoje, feita pelo próprio advogado. Ela não julga o trabalho dele. O valor está na comparação entre uma rodada e a próxima.

## Anatomia do POP (12 campos)

Cabeçalho: `POP-[SIGLA]-[NN] [NOME DO PROCESSO] · Setor · Área (se houver) · Versão · Atualizado em · Dono do POP · Status`. O código e as siglas de setor estão em `docs/pasta-do-escritorio.md`.

1. **Objetivo:** uma frase com o resultado entregue. Se não cabe numa frase, são dois POPs.
2. **Gatilho:** o acontecimento que inicia o processo (uma mensagem, uma publicação, um vencimento, uma data fixa). Sem gatilho, o processo depende de alguém lembrar.
3. **Responsáveis:** Executa, Confere e Decide, escritos primeiro como função e depois com nomes.
4. **Entradas:** documentos, sistemas, modelos, listas e critérios. É daqui que sai a lista do que a base de conhecimento precisa ter.
5. **Passo a passo com S, A e H:** de 7 a 12 passos, cada um começando com verbo, no formato `1. [S/A/H] Verbo + tarefa. Executa: ... Confere: ...`
6. **Prazo:** do gatilho à saída, mais os prazos internos das etapas críticas. Vem do código do escritório.
7. **Exceções:** "Situação: o que fazer". Para cada decisão do fluxo, perguntar "e se não?".
8. **Saída:** o que foi entregue, para quem e onde ficou registrado.
9. **Onde a IA entra:** resumo dos passos S e A, o que a IA consulta e em que ambiente roda.
10. **Nunca sai sem revisão humana:** lista curta do que não avança sem conferência, "nem quando a IA acerta quase sempre".
11. **Dados pessoais e sensíveis:** que dados aparecem, o que anonimizar, o que nunca entra na IA.
12. **Indicador:** um ou dois números acompanhados todo mês. "Sem indicador, você não sabe se a IA ajudou ou só mudou o trabalho de lugar."

## A vida do POP

- **Código:** sigla do setor e número, como `POP-PEC-01`. O número nunca é reaproveitado, nem quando o POP é aposentado.
- **Versão:** rascunho e teste são `0.x` (0.1 quando o POP é escrito, 0.2, 0.3 a cada rodada de ajustes do teste). A primeira publicação como vigente é `1.0`. Depois disso, ajuste de redação, prazo ou exceção sobe o decimal (1.1); mudança de sigla, de responsável, de passo, de ordem ou de gatilho sobe o inteiro (2.0). Regra prática: se a equipe precisa ser treinada de novo, sobe o inteiro; se basta avisar, sobe o decimal.
- **Status:** Rascunho (sendo escrito) · Em teste (teste de mesa, teste com a IA ou piloto) · Vigente (a única versão em uso) · Em revisão (vigente, com mudança em andamento) · Aposentado (fora de uso, com o motivo registrado).
- **Dono do POP:** a pessoa que responde por ele estar escrito, certo, treinado e atualizado. Não precisa ser quem executa.
- **Mapa de POPs:** a tabela com todos os POPs do escritório, um por linha, inclusive os aposentados.

## Do POP à IA: os seis degraus

| Degrau | O que existe | O que a IA faz |
|---|---|---|
| 1. Prompt solto | Cada pessoa pede de um jeito | Responde de um jeito diferente a cada vez |
| 2. POP escrito e guardado | O processo no papel, com código, versão e dono | Nada sozinha, mas a equipe já tem a fonte única |
| 3. Projeto no Claude | O código do escritório, os POPs e a base como conhecimento do Projeto | Trabalha com o contexto do escritório em toda conversa |
| 4. Habilidade do POP | O POP convertido em skill: instruções de cada passo (`desenhar-automacao`) e depois a skill (`pop-para-skill`) | Carrega o roteiro quando o trabalho aparece, segue a ordem, consulta os documentos certos, para em cada passo A e nunca executa um passo H |
| 5. Plugin do escritório | Várias habilidades reunidas num pacote | A equipe inteira usa o mesmo padrão, na mesma versão |
| 6. Automação | Disparo por gatilho, fila de revisão e registro de uso (`desenhar-automacao`) | Roda a partir do acontecimento e espera a revisão humana nos pontos fixos |

Cada degrau depende do anterior. Habilidade feita sobre POP que ninguém testou espalha o erro com mais velocidade.

## Termos de desenho e de ferramenta

- **Fluxograma:** o desenho do caminho do trabalho, do gatilho à saída, com as decisões e as exceções. Mostra por onde o trabalho anda; o POP explica como fazer cada passo.
- **Raia:** uma coluna do fluxograma para cada executor (IA, Equipe, Advogado). Mostra quem faz cada passo e, na mesma linha de um passo A, quem revisa.
- **Mermaid:** código de texto que vira diagrama. O Claude escreve o fluxograma em Mermaid e o desenha na conversa; o mesmo código pode ser colado em editores que leem Mermaid.
- **Projeto no Claude:** área de trabalho com instruções fixas e arquivos de conhecimento que valem para todas as conversas dentro dela.
- **Habilidade (skill):** pasta com um arquivo `SKILL.md` e materiais de apoio que ensina o Claude a fazer um trabalho do jeito do escritório. Fica instalada na conta e é carregada só quando o pedido combina com ela.
- **Plugin:** pacote que reúne várias habilidades e comandos, instalado de uma vez.

## Medição

- **Valor da hora:** três métodos (faturamento, retirada desejada, custo do colaborador). Escolher um, anotar qual e não trocar no meio do caminho.
- **Linha de base:** uma semana típica registrada antes da mudança, com o tempo por unidade (minutos ÷ volume).
- **Horas devolvidas:** tempo antes menos tempo com IA, descontada a revisão humana. Sempre com o campo "para onde foram as horas". "Hora devolvida sem destino evapora."
- **Incidente:** o dado saiu ou o erro chegou ao cliente ou ao processo. **Quase incidente:** a revisão pegou antes. Os dois são registrados. Quem avisa nunca é punido por avisar.
