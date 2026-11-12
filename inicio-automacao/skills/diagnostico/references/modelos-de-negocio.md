# Modelos de negócio do escritório

Referência da skill `diagnostico`. Leia quando o advogado fizer a identificação do modelo (passo 7 do SKILL.md), quando o resultado der empate ou híbrido, ou quando outra skill precisar do perfil do escritório para escolher POPs, base ou cuidados.

As perguntas do teste, as opções e a pontuação estão em `questionario.json` (bloco `quiz_modelo`). Este arquivo traz a leitura de cada perfil.

## 1. Por que o modelo muda a ordem

A equação da automação é a mesma para todo escritório: um POP executado pela IA, consultando a base de conhecimento e dentro da régua da cultura. O que muda é a ordem em que as peças são montadas.

Pense num escritório de contencioso de massa que recebe centenas de publicações por semana. O que tira o sono dessa equipe é a fila de prazos, porque um erro ali se repete em escala. Agora pense numa boutique de societário com doze clientes ativos. Lá quase não existe fila de prazo. O que trava é o sócio, que escreve cada parecer do zero porque as teses antigas estão perdidas numa pasta chamada "modelos_FINAL_v3".

Os dois fazem o mesmo diagnóstico, usam o mesmo mapa de setores e escrevem POP no mesmo formato. Só que o setor-alvo de um tem pouco a ver com o do outro, e a IA entra de jeitos diferentes: no primeiro, muita Substituição com conferência; no segundo, quase tudo Auxílio, com o sócio no comando.

**Exemplo resolvido** (números inventados, só para mostrar a conta). Dois escritórios de cinco pessoas preencheram o mapa de setores. O setor-alvo é o maior resultado de horas por semana × incômodo.

| Setor | Escritório A · volume de Consumidor | Escritório B · boutique de societário |
|---|---|---|
| Prazos e controladoria | 25 h × 5 = 125 | 4 h × 2 = 8 |
| Produção de peças | 20 h × 4 = 80 | 22 h × 4 = 88 |
| Relacionamento com o cliente | 10 h × 3 = 30 | 10 h × 3 = 30 |
| Comercial | 3 h × 2 = 6 | 8 h × 5 = 40 |
| **Setor-alvo** | **Prazos e controladoria** | **Produção de peças** |

## 2. O que muda de um modelo para outro

1. **O setor-alvo provável.** Cada modelo concentra horas e dor em setores diferentes. O perfil dá uma hipótese, e o diagnóstico confirma ou derruba.
2. **A mistura de S, A e H.** Volume e correspondência aceitam mais Substituição. Boutique e consultivo vivem de Auxílio. O peso do Humano acompanha o quanto o cliente paga pelo julgamento do advogado.
3. **O tipo de base de conhecimento.** No volume, a base é feita de modelos e regras de classificação. Na boutique, de teses, critérios e peças padrão ouro. No digital, de roteiros de triagem e respostas.
4. **O risco que mais pesa.** Para quem trabalha sozinho, depender de uma pessoa. No volume, o erro repetido mil vezes. No digital, a publicidade. No consultivo, misturar informação de clientes.

**O modelo orienta, o mapa decide.** Use o perfil como ponto de partida. Se o diagnóstico apontar outro setor-alvo, siga o diagnóstico: ele foi feito com as horas do escritório, e o perfil foi escrito para o escritório típico do modelo. Anote por que o perfil apontou outro setor. Essa anotação ajuda o `mapear-setores` a confirmar o alvo.

## 3. Como ler o teste

- Seis perguntas, uma por vez. Opção que aponta para um modelo só dá 2 pontos a ele. Opção que aponta para vários dá 1 ponto a cada.
- Resultado: o modelo com mais pontos. Se o segundo tiver pontos e ficar até 2 pontos atrás, o escritório tem traços dos dois: leia os dois perfis e a seção 6 (híbridos).
- Desempate pela ordem: full service, boutique, volume, solo, consultivo, digital, correspondência.
- **Ainda em dúvida?** Use os sinais. Normalmente dois ou três batem com força num modelo só.

| Sinal no dia a dia | Aponta para |
|---|---|
| Existe coordenador de área e reunião de alinhamento entre departamentos | Full service |
| O cliente contrata o nome do sócio, e cada caso tem estratégia própria | Boutique |
| Existe planilha ou sistema com centenas de processos e uma pessoa só para publicações | Contencioso de volume |
| Você é quem atende, escreve, protocola e cobra | Advogado solo |
| A receita vem de mensalidade de empresas, e o cliente cobra resposta rápida | Consultivo e partido mensal |
| Você sabe quantos leads chegaram na semana e quanto investiu em anúncio | Digital de nicho |
| Quem te paga é outro advogado, e a pauta muda todo dia | Parcerias e correspondência |

**Departamento jurídico de empresa:** nenhum dos sete perfis foi escrito para ele. O mais próximo é o consultivo (o cliente interno manda demanda o tempo todo, por todo canal). Use esse perfil como hipótese e deixe o mapa decidir. [A CONFIRMAR]

## 4. Vale para os sete modelos

Dado de cliente só entra na IA anonimizado, em conta profissional e com a regra de uso do escritório escrita. Tudo o que sai do escritório passa por revisão humana, com conferência de citação, jurisprudência e número. O que varia de um modelo para outro é o tamanho do estrago quando alguém esquece.

Publicidade (Provimento 205/2021 do CFOAB e Código de Ética e Disciplina da OAB), para todos:
- Caráter informativo, discreto e sóbrio. Conteúdo jurídico informativo é bem-vindo.
- Nada de promessa de resultado, nem disfarçada de "garanta o seu direito".
- Nada de captação de clientela ou mercantilização, nem por intermediário.
- Valor de honorário, desconto e gratuidade fora da publicidade.
- Cliente e caso identificável só com autorização e sem quebrar sigilo. Na dúvida, não publique.
- Conteúdo escrito pela IA passa por revisão humana antes de publicar.
- Atendimento automatizado se apresenta como automatizado e não dá orientação jurídica.
- Follow-up só para quem procurou o escritório, nunca para lista comprada.

A tabela "onde costuma escorregar" de cada perfil é um guia de atenção. A leitura do texto atual das normas continua sendo do advogado, e a seccional interpreta. Antes de lançar campanha, anúncio ou robô de atendimento, confira na fonte. [CONFERIR]

## 5. Os sete perfis

Cada perfil segue a mesma estrutura: como funciona, setores críticos, gargalos típicos, setor-alvo provável, POPs para escrever primeiro (skill `escrever-pop`), onde a IA entra primeiro com S, A e H (confirmar com a `classificar-sah`), riscos, indicadores (skill `medir-retorno`), formato do núcleo (skill `nucleo-de-inovacao`), onde costuma escorregar na publicidade, o que separar antes de automatizar e um plano em três etapas.

O plano usa marcos relativos e é um ritmo sugerido: **etapa 1** nas primeiras 2 semanas (o retrato), **etapa 2** até a semana 4 (a base), **etapa 3** até a semana 8 (o primeiro fluxo rodando com conferência). Ajuste ao tempo que o escritório consegue dedicar. [A DEFINIR]

Tudo o que for separado antes de automatizar vai anonimizado, conforme a tabela de troca das regras do plugin.

---

### 5.1 Full service

**Várias áreas, equipe maior, departamentos.**

**Como funciona.** Atende várias áreas do direito sob o mesmo teto, com a equipe dividida em departamentos ou núcleos, cada um com o seu coordenador. É comum o mesmo cliente aparecer em mais de uma área: a empresa que tem trabalhista, contratos e tributário, ou a família que começa no inventário e termina no imobiliário. Já existe alguma estrutura de apoio, como financeiro, controladoria e às vezes um gestor.

**Setores críticos:** Prazos e controladoria · Atendimento e triagem · Gestão de equipe · Relacionamento com o cliente.

**Gargalos típicos:**
- Cada departamento faz a mesma coisa de um jeito: dois controles de prazo, três modelos de procuração.
- A informação do cliente fica espalhada, e o trabalhista não sabe que o cível tem um contrato parado.
- O caso novo vai para a área de quem atendeu o telefone.
- Quem chega demora a aprender, porque cada área ensina do seu jeito.

**Setor-alvo provável: Prazos e controladoria.** É o setor que todas as áreas usam. Um padrão único aqui rende no escritório inteiro e ainda força as áreas a conversarem. Se a triagem entre áreas for o caos maior, Atendimento e triagem passa na frente.

**POPs para escrever primeiro:**
- Prazos e controladoria: recebimento e distribuição de publicações.
- Atendimento e triagem: encaminhamento para a área certa.
- Gestão de equipe: integração de quem chega.
- Um POP de produção para cada área principal, escrito pelo coordenador dela, todos no mesmo formato.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Ler publicações e classificar por área e tipo de ato | S | Pela regra escrita no POP. A controladoria confere a lista do dia. |
| Distribuir a tarefa para o responsável | S | Só depois que a regra de distribuição estiver no papel. Sem regra, a IA chuta. |
| Resumir o relato do caso novo e sugerir a área | A | Quem faz a triagem confirma a área e o responsável. |
| Resumo da carteira de um cliente com casos em várias áreas | A | O sócio do cliente lê antes da reunião ou do envio. |
| Aceitar caso com possível conflito de interesses | H | A IA ajuda a cruzar nomes. A decisão é de sócio. |

**Riscos e cuidados.** Conflito de interesses entre áreas exige checagem humana. Nem todo mundo precisa ver tudo: quando o sigilo pedir, separe Projetos no Claude por área ou por cliente. Cuidado com cada departamento criando a sua própria automação, com conta pessoal e regra nenhuma: a regra de uso de IA precisa ser uma só para o escritório. E repare no coordenador que "sabe tudo" da área: se ele sai, o POP que não foi escrito vai junto.

**Indicadores:** prazos tratados no último dia, por área · tempo entre a publicação e a distribuição da tarefa · quantos modelos diferentes existem para o mesmo documento · tempo até quem chega trabalhar sem supervisão.

**Núcleo de inovação:** comitê pequeno com um representante por área e alguém da controladoria ou do administrativo, mais um sócio patrocinador que destrava decisão. Encontro quinzenal curto, com pauta fixa.

**Onde costuma escorregar na publicidade:** cada área posta do seu jeito, e ninguém revisa o conjunto. O que fazer: um POP de Marketing e conteúdo para o escritório todo, com um revisor ético definido.

**O que separar antes de automatizar:** o POP do setor-alvo com as variações de cada área já anotadas, o código do escritório aprovado pelos sócios e uma semana de publicações anonimizadas para testar a classificação.

**Plano:** etapa 1, passo a passo atual da controladoria, com as diferenças entre áreas anotadas · etapa 2, modelos únicos de documentos comuns às áreas, numa base só · etapa 3, classificação e distribuição de publicações rodando com conferência.

---

### 5.2 Boutique

**Nicho e alta especialização, ticket alto, poucos casos.**

**Como funciona.** Atua num nicho estreito, como societário, direito médico, propriedade intelectual ou tributário de um setor específico. São poucos casos, cada um com estratégia própria e honorário alto. O cliente contrata o nome do sócio e espera o sócio por perto. A equipe é enxuta e muito técnica, e o conhecimento da casa costuma morar na cabeça de uma ou duas pessoas.

**Setores críticos:** Produção de peças · Comercial · Relacionamento com o cliente.

**Gargalos típicos:**
- A pesquisa de cada caso recomeça do zero, porque as teses antigas estão em pastas soltas.
- A proposta de honorários sob medida leva dias para sair.
- O relatório caprichado para o cliente quem escreve é o sócio, à noite.
- O associado não consegue assumir porque falta o "jeito da casa" por escrito.

**Setor-alvo provável: Produção de peças.** Começando pela pesquisa e pela primeira minuta, que é onde o sócio perde mais horas com trabalho que alguém poderia preparar. Se o que trava é fechar contrato, Comercial vira o alvo, com a proposta de honorários sob medida.

**POPs para escrever primeiro:**
- Produção de peças: pesquisa, minuta e revisão em camadas.
- Comercial: proposta e contrato de honorários.
- Relacionamento com o cliente: relatório periódico.
- O POP da especialidade, adaptado aos critérios da casa.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Organizar teses, pareceres e peças antigas na base de conhecimento | S | Resumir, etiquetar e indexar material já anonimizado. O sócio escolhe o que entra. |
| Pesquisa inicial e mapa de argumentos do caso novo | A | Toda fonte citada é conferida na origem antes de ir para a peça. |
| Primeira minuta no estilo da casa | A | A partir das peças padrão ouro. O sócio reescreve o que for estratégia. |
| Relatório ao cliente a partir das notas do sócio | A | O sócio lê e assina antes do envio. |
| Escolha da tese e conversa sobre risco com o cliente | H | É exatamente o que o cliente está pagando. |

**Riscos e cuidados.** O sigilo pesa mais aqui, porque os casos envolvem informação estratégica de empresa ou de pessoa conhecida. Anonimize com rigor e use conta profissional. Jurisprudência que a IA inventa é o pior erro possível numa boutique: confira cada citação na fonte. Se o jeito de pensar do sócio não for para a base, a IA só replica o gargalo. E como o cliente paga pelo julgamento, combine com ele, com transparência, onde a IA participa.

**Indicadores:** horas do sócio por caso · tempo até a primeira minuta · rodadas de revisão por peça · tempo para montar uma proposta de honorários.

**Núcleo de inovação:** uma dupla. O sócio, que define o que é qualidade, e um associado que testa, documenta e alimenta a base. O sócio não precisa operar a ferramenta, mas precisa revisar a base.

**Onde costuma escorregar na publicidade:** citar o caso famoso ou o cliente importante para mostrar autoridade. O que fazer: autoridade por conteúdo técnico, artigo e palestra. Caso e cliente só com autorização expressa, e mesmo assim com cuidado.

**O que separar antes de automatizar:** de três a cinco peças ou pareceres de referência, anonimizados (os padrão ouro), um roteiro curto de como o sócio pensa um caso novo e o POP de Produção de peças com as linhas de Auxílio marcadas.

**Plano:** etapa 1, passo a passo de como um caso novo vira peça, do jeito que o sócio faz · etapa 2, peças padrão ouro e teses anonimizadas organizadas na base · etapa 3, pesquisa e primeira minuta no estilo da casa, como Auxílio.

---

### 5.3 Contencioso de volume

**Muitos processos, petição padronizada, controladoria pesada.**

**Como funciona.** Centenas ou milhares de processos parecidos, seja do lado réu, com uma carteira de poucos clientes grandes como banco, varejo, telefonia ou seguradora, seja do lado autor, em ações repetitivas. Petição padronizada, prazo apertado, controladoria pesada e muita gente em início de carreira. A margem por processo é pequena, então cada minuto economizado se multiplica.

**Setores críticos:** Prazos e controladoria · Produção de peças · Audiências e diligências · Financeiro e cobrança.

**Gargalos típicos:**
- Publicação lida uma por uma, por gente cansada.
- Peça padrão adaptada à mão, com o risco de esquecer de trocar o nome da parte.
- Audiências espalhadas, com correspondente contratado no improviso.
- Relatório para o cliente-carteira montado em planilha no último dia do mês.
- Rotatividade alta, e quem chega precisa produzir na primeira semana.

**Setor-alvo provável: Prazos e controladoria.** No volume, o erro custa caro e o ganho de escala aparece primeiro aqui. Logo atrás vem Produção de peças, com a montagem da peça padronizada.

**POPs para escrever primeiro:**
- Prazos e controladoria: triagem de publicações, cálculo e conferência de prazo.
- Produção de peças: montagem a partir de modelo, com checagem de campos.
- Audiências e diligências: contratação e retorno do correspondente.
- POPs por área em Consumidor e Trabalhista, onde as teses repetitivas costumam se concentrar.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Ler publicações e classificar por tipo de ato | S | Com conferência por amostragem todo dia. A regra de classificação fica escrita no POP. |
| Extrair dados de documentos para a planilha ou o software jurídico | S | Campos definidos, checagem dos campos vazios. |
| Sugerir o prazo e lançar na agenda | A | A pessoa confirma cada prazo. Prazo nunca vai para a agenda sem conferência humana. |
| Montar a peça padronizada a partir do modelo e dos dados do processo | A | Checklist de campos variáveis e leitura do advogado antes de protocolar. |
| Relatório periódico ao cliente-carteira | A | A IA consolida, o coordenador revisa os números. |
| Decidir recorrer, propor acordo ou mudar a tese em lote | H | Decisão estratégica, com o cliente. |

**Riscos e cuidados.** Um modelo errado vira mil peças erradas. Teste toda automação com uma amostra pequena antes de soltar na carteira inteira. Dado em massa faz a LGPD pesar mais, e o contrato com o cliente-carteira pode ter regra sobre ferramentas e fornecedores: leia antes de colocar qualquer coisa na IA. Peça padronizada que ignora a particularidade do caso o juiz percebe. E se a regra de prazo só existe na cabeça do controller, o escritório depende dele para respirar. Do lado autor, a captação em massa tem limite ético claro (veja abaixo).

**Indicadores:** tempo entre a publicação e o lançamento do prazo · prazos tratados no último dia · peças devolvidas na revisão por erro de campo · processos por pessoa da equipe · tempo para fechar o relatório do cliente-carteira.

**Núcleo de inovação:** liderado pela controladoria, com a pessoa mais técnica da equipe e um advogado que responde pela qualidade das peças. Reunião semanal curta, olhando número.

**Onde costuma escorregar na publicidade:** do lado autor, anúncio de "você pode ter direito a receber", mensagem em massa e parceria com quem capta cliente. O que fazer: conteúdo que explica o direito, sem chamar para a ação de forma mercantil. Nenhuma parceria de captação.

**O que separar antes de automatizar:** uma amostra anonimizada de publicações de um tipo frequente (umas 20 bastam), o modelo de peça correspondente com os campos variáveis marcados e o POP de controladoria com a regra de classificação escrita.

**Plano:** etapa 1, regra de classificação de publicações escrita, com exemplos de cada tipo · etapa 2, modelos de peça com os campos variáveis marcados · etapa 3, triagem de publicações testada com amostra antes de escalar.

---

### 5.4 Advogado solo ou autônomo

**Uma pessoa faz tudo.**

**Como funciona.** Uma pessoa atende, vende, escreve, protocola, cobra e ainda tenta postar no Instagram. Às vezes tem um estagiário ou uma secretária meio período. Pode ser generalista ou ter uma ou duas áreas. A agenda é de quem chegou primeiro, e o WhatsApp do cliente às 22h faz parte da rotina. O escritório inteiro cabe na sua cabeça, e é exatamente esse o problema.

**Setores críticos:** Relacionamento com o cliente · Atendimento e triagem · Produção de peças · Financeiro e cobrança.

**Gargalos típicos:**
- Interrupção o dia inteiro: você nunca termina uma peça de uma vez.
- Tudo depende de você lembrar.
- A cobrança fica para depois, e depois vira nunca.
- Não sobra tempo para pensar o escritório, só o processo do dia.

**Setor-alvo provável: Relacionamento com o cliente.** É o setor que mais picota o seu dia. Organizar a atualização de andamento e as respostas frequentes devolve blocos inteiros de concentração. Se o problema é que entra pouca gente, Atendimento e triagem passa na frente.

**POPs para escrever primeiro:**
- Relacionamento com o cliente: atualização de andamento.
- Atendimento e triagem: primeiro contato e lista de documentos.
- Financeiro e cobrança: lembrete e cobrança amigável.
- O POP da sua área principal.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Lista de documentos e roteiro da consulta por tipo de caso | S | Gerada a partir da sua base. Você revisa uma vez, e ela vira padrão. |
| Resumo do processo antes de falar com o cliente | S | Uso interno, com dado anonimizado e conta profissional. |
| Resposta a dúvida frequente do cliente | A | A partir das respostas-modelo e do código do escritório. Você lê antes de enviar. |
| Rascunho de peça a partir do seu modelo | A | Conferência de citação e de dado do cliente, sempre. |
| Mensagem de cobrança no tom do escritório | A | Você escolhe quando e para quem mandar. |
| Aceitar caso, definir preço, dar notícia ruim | H | Continua com você. Notícia ruim é ligação, nunca mensagem automática. |

**Riscos e cuidados.** Dependência total de uma pessoa: se você adoece ou tira férias, o escritório para. O POP escrito funciona como seguro. Cuidado com a tentação da conta gratuita e pessoal para resolver rápido com dado de cliente. E ninguém revisa o que a IA fez além de você. Essa revisão não pode ser pulada no dia corrido, que é justamente o dia em que dá vontade de pular.

**Indicadores:** horas por semana no WhatsApp · tempo de resposta ao cliente · honorários em atraso · horas em trabalho jurídico contra horas em administrativo.

**Núcleo de inovação:** você mesmo, com hora marcada: um bloco fixo por semana na agenda para melhorar o escritório e um arquivo "o que eu repeti esta semana". Se tiver estagiário ou secretária, essa pessoa vira sua parceira de teste.

**Onde costuma escorregar na publicidade:** perfil pessoal e profissional misturados, e post feito pela IA publicado sem leitura. O que fazer: separar o tom profissional e ler tudo antes de publicar, inclusive a legenda.

**O que separar antes de automatizar:** o código do escritório, as dez perguntas que os clientes mais fazem com as suas respostas de hoje e o POP de Relacionamento com o cliente.

**Plano:** etapa 1, passo a passo da atualização de andamento e das respostas no WhatsApp · etapa 2, dez perguntas frequentes com respostas-modelo e o código do escritório · etapa 3, respostas e atualizações rascunhadas pela IA, com a sua aprovação.

---

### 5.5 Consultivo e empresarial · partido mensal

**Contratos recorrentes, empresas clientes.**

**Como funciona.** Os clientes são empresas com contrato recorrente, por partido mensal ou pacote de horas. A demanda é contínua e picada: revisar contrato, responder consulta do RH, parecer rápido, acompanhar assembleia, orientar uma demissão. A receita é previsível, mas a pressão vem por dois lados: responder rápido e mostrar valor todo mês, para o partido não ser cortado na próxima revisão de custos do cliente.

**Setores críticos:** Relacionamento com o cliente · Produção de peças · Comercial · Financeiro e cobrança.

**Gargalos típicos:**
- A demanda chega por e-mail, WhatsApp e ligação, sem fila única.
- O cliente acha que paga muito porque não enxerga o que foi feito.
- Contrato revisado do zero, sem checklist da casa.
- A mesma dúvida de RH respondida pela décima vez.

**Setor-alvo provável: Relacionamento com o cliente.** Organizando a entrada das demandas e a prestação de contas mensal. Logo atrás vem Produção de peças, com a revisão de contratos contra as posições padrão do escritório.

**POPs para escrever primeiro:**
- Relacionamento com o cliente: entrada de demanda com fila única e prazo de resposta combinado.
- Produção de peças: revisão de contrato com checklist.
- Comercial: renovação do partido com o relatório do período na mão.
- POPs por área: Trabalhista pelo lado da empresa e a área consultiva principal.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Registrar e classificar a demanda que chegou | S | Cliente, tipo, urgência e responsável, numa fila única. |
| Revisar contrato contra o checklist e as posições da casa | A | A IA aponta desvios. O advogado decide o que negociar. |
| Responder consulta recorrente | A | A partir de respostas já aprovadas, guardadas na base daquele cliente. |
| Relatório mensal do que foi feito | A | A IA consolida a fila do mês. O sócio lê antes de enviar. |
| Parecer com risco relevante e negociação com a outra parte | H | Julgamento e responsabilidade do advogado. |

**Riscos e cuidados.** Dado de empresa costuma ser sigiloso e às vezes estratégico, como uma reestruturação ou uma demissão coletiva. Separe a base por cliente quando fizer sentido e nunca deixe a informação de um aparecer na resposta de outro. O contrato do cliente pode exigir confidencialidade sobre ferramentas e fornecedores: leia antes. E sem o checklist da casa escrito, a IA revisa contrato com o critério genérico dela.

**Indicadores:** tempo de resposta por tipo de demanda · demandas por cliente por mês · horas consumidas contra o valor do partido, por cliente · quantas respostas reaproveitam a base.

**Núcleo de inovação:** o sócio responsável pela carteira e a pessoa que toca a fila de demandas, testando primeiro com um cliente piloto.

**Onde costuma escorregar na publicidade:** logo de cliente no site, case de empresa na proposta comercial. O que fazer: só com autorização expressa e por escrito. Na proposta, descreva o tipo de trabalho sem identificar o cliente.

**O que separar antes de automatizar:** a lista anonimizada das demandas de um mês de um cliente, o checklist de revisão de contrato da casa (mesmo que incompleto) e um modelo de relatório mensal.

**Plano:** etapa 1, fluxo de entrada de demanda de um cliente piloto · etapa 2, checklist de revisão de contrato e respostas já aprovadas, por cliente · etapa 3, fila única e relatório mensal montado pela IA.

---

### 5.6 Escritório digital de nicho

**Captação online, atendimento remoto, volume de leads.**

**Como funciona.** Um nicho bem definido, como o previdenciário de uma categoria, o direito do passageiro aéreo, o superendividamento ou o servidor público. A captação vem de conteúdo, anúncio e busca. O atendimento é remoto, com cliente em vários estados e assinatura digital. Chega muito lead, e boa parte não vira contrato. Os casos se parecem bastante entre si, o que favorece padronização.

**Setores críticos:** Atendimento e triagem · Comercial · Marketing e conteúdo · Relacionamento com o cliente.

**Gargalos típicos:**
- Lead esperando resposta enquanto a equipe atende outro.
- Triagem gastando tempo com quem não tem o direito.
- Documento chegando pela metade, em foto torta, pelo WhatsApp.
- Follow-up que ninguém faz.
- O conteúdo depende de uma pessoa só.

**Setor-alvo provável: Atendimento e triagem.** É onde o volume de leads vira horas. Uma triagem bem escrita filtra cedo e entrega o caso pronto para o advogado. Logo atrás vem Comercial, com proposta, contrato e follow-up.

**POPs para escrever primeiro:**
- Atendimento e triagem: perguntas de qualificação e lista de documentos por tipo de caso.
- Comercial: proposta, contrato, assinatura e follow-up.
- Marketing e conteúdo: revisão ética antes de publicar.
- O POP da área do nicho.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Primeira resposta e coleta das informações básicas | S | Deixando claro que é atendimento automatizado, sem análise jurídica e sem promessa. Passa para uma pessoa quando o caso pede. |
| Conferir os documentos recebidos contra a lista | S | Aponta o que falta e o que está ilegível. |
| Pré-análise de viabilidade a partir dos documentos | A | O advogado decide se o caso tem viabilidade. |
| Mensagem de follow-up para quem parou de responder | A | A IA prepara no tom do escritório. Uma pessoa decide se e quando enviar. |
| Roteiros e posts a partir das dúvidas reais dos clientes | A | Revisão ética antes de publicar, sempre. |
| Dizer se a pessoa tem o direito e fechar honorários | H | Orientação jurídica e contrato são do advogado. |

**Riscos e cuidados.** Robô de atendimento que promete resultado ou dá parecer é o risco número um. No previdenciário, dado de saúde chega pelo chat o tempo todo, e dado sensível pede cuidado redobrado com a LGPD. Anúncio e conteúdo precisam caber no Provimento 205/2021 do CFOAB. Volume de lead sem filtro esgota a equipe. E depender de uma plataforma de anúncio só deixa o escritório frágil.

**Indicadores:** tempo de primeira resposta ao lead · leads qualificados por semana · consultas que viram contrato, comparando o escritório com ele mesmo · documentação completa na primeira tentativa · custo por contrato fechado, se há investimento em anúncio.

**Núcleo de inovação:** quem cuida do comercial e quem cuida do marketing, olhando o funil juntos toda semana, com um advogado responsável pela revisão ética.

**Onde costuma escorregar na publicidade:** anúncio com promessa, consulta gratuita usada como isca, robô que responde "você tem direito". O que fazer: revisão ética de cada anúncio e de cada roteiro do robô antes de ir ao ar (a `auditar-riscos` ajuda a revisar o fluxo do robô).

**O que separar antes de automatizar:** o roteiro atual de triagem, as perguntas que separam quem tem o direito de quem não tem, a lista de documentos por tipo de caso e umas dez conversas reais de atendimento, anonimizadas.

**Plano:** etapa 1, roteiro de triagem atual, do primeiro contato ao contrato · etapa 2, perguntas de qualificação, lista de documentos e respostas a objeções · etapa 3, primeira resposta e conferência de documentos rodando, com revisão ética.

---

### 5.7 Parcerias e correspondência

**Diligências e audiências para outros escritórios.**

**Como funciona.** O cliente é outro advogado ou um departamento jurídico. O escritório faz audiência, diligência, protocolo, cópia de processo e despacho. São muitas demandas pequenas, com prazo curto e pagamento por ato. Às vezes é uma rede de correspondentes coordenada por um escritório. A pauta muda todo dia, e a qualidade do relatório decide se o contratante volta.

**Setores críticos:** Audiências e diligências · Administrativo · Financeiro e cobrança · Relacionamento com o cliente.

**Gargalos típicos:**
- Demanda chegando em cima da hora e com informação pela metade.
- Ata e relatório para o contratante escritos à noite.
- Cobrança de muitos atos pequenos, de vários contratantes.
- Cada contratante quer o relatório num formato.

**Setor-alvo provável: Audiências e diligências.** Do recebimento da demanda até o relatório entregue ao contratante. Se a cobrança estiver acumulando, Financeiro e cobrança passa na frente.

**POPs para escrever primeiro:**
- Audiências e diligências: recebimento com checklist mínimo, preparo, ata e retorno.
- Financeiro e cobrança: fechamento por contratante.
- Administrativo: agenda e deslocamento.
- POPs por área das áreas com mais audiência, para entender o que o contratante espera.

**Onde a IA entra primeiro:**

| Passo | Sigla | Como e com que cuidado |
|---|---|---|
| Ler a solicitação e conferir se tem o mínimo para cumprir | S | Contra um checklist: processo, horário, alçada para acordo, documentos. |
| Fechamento mensal por contratante | S | A partir da agenda e dos atos registrados. |
| Resumo do processo para a audiência | A | Você lê os pontos-chave antes de entrar na sala. |
| Relatório pós-audiência no formato do contratante | A | A partir do seu áudio logo depois da audiência. Você confere se está fiel ao que aconteceu. |
| O que fazer dentro da audiência | H | Acordo dentro da alçada, requerimento, postura. É você na sala. |

**Riscos e cuidados.** Você recebe dado do cliente de outro escritório, então o sigilo vale em dobro: use só o que precisa e não guarde o que não precisa guardar. Respeite os limites do substabelecimento e da alçada combinada. O relatório pós-audiência precisa ser fiel, e a IA não pode "melhorar" o que aconteceu. E se dois contratantes respondem pela maior parte da receita, o escritório depende deles.

**Indicadores:** tempo entre a audiência e o relatório entregue · demandas devolvidas por falta de informação · atos realizados por semana · valores em atraso por contratante.

**Núcleo de inovação:** o coordenador da pauta e um correspondente de campo. Se for rede, uma pessoa responsável por padronizar o relatório para todos.

**Onde costuma escorregar na publicidade:** tabela de preço por ato divulgada como anúncio aberto. O que fazer: preço e condições tratados direto com o colega contratante, numa proposta.

**O que separar antes de automatizar:** três solicitações reais anonimizadas, o modelo de relatório mais usado e o POP de Audiências e diligências.

**Plano:** etapa 1, fluxo do recebimento da demanda até o relatório entregue · etapa 2, checklist mínimo de solicitação e modelos de relatório por contratante · etapa 3, relatório pós-audiência a partir do seu áudio.

---

## 6. Comparativo

| Modelo | Em uma linha | Setor-alvo provável | Primeira entrada da IA | Peso do H | Cuidado maior |
|---|---|---|---|---|---|
| Full service | Várias áreas, departamentos, cliente compartilhado | Prazos e controladoria | S: classificar e distribuir publicações | Médio | Conflito de interesses e regra de IA única |
| Boutique | Nicho, poucos casos, ticket alto | Produção de peças | A: pesquisa e primeira minuta | Alto | Sigilo estratégico e citação inventada |
| Contencioso de volume | Centenas de processos parecidos | Prazos e controladoria | S: ler e classificar publicações | Baixo nos passos, alto na estratégia | Erro replicado em escala |
| Advogado solo | Uma pessoa faz tudo | Relacionamento com o cliente | A: respostas frequentes ao cliente | Alto | Dependência de uma pessoa e conta pessoal |
| Consultivo e partido | Empresas com contrato recorrente | Relacionamento com o cliente | S: fila única de demandas | Médio | Misturar informação de clientes |
| Digital de nicho | Captação online, atendimento remoto | Atendimento e triagem | S: primeira resposta e coleta | Médio | Publicidade e promessa de resultado |
| Correspondência | Atos para outros escritórios | Audiências e diligências | S: conferir a solicitação recebida | Médio | Sigilo de cliente de terceiro |

"Peso do H" é uma leitura qualitativa de quanto do trabalho depende do julgamento do advogado. Serve para orientar a conversa e não tem medição por trás.

## 7. Híbridos e transição

Quase nenhum escritório é um modelo puro. O advogado previdenciarista que capta pelo Instagram e ainda faz audiência como correspondente tem três modelos rodando ao mesmo tempo. O caminho é separar os fluxos e decidir qual organizar primeiro:

1. **Separe o escritório por fluxo de receita.** Cada tipo de cliente que paga de um jeito diferente é um fluxo. Liste os fluxos e quanto do tempo vai para cada um.
2. **Leia o perfil de cada fluxo.** Os gargalos e os riscos de cada um continuam valendo, mesmo dentro do mesmo escritório.
3. **Deixe o mapa de setores decidir o setor-alvo.** O modelo ajuda a interpretar e a escolher os POPs. Quem aponta onde estão as horas é o diagnóstico.
4. **Comece pela parte que mais se repete.** É ela que paga mais rápido o esforço de escrever o POP e montar a base.

**Combinações comuns:**

| Combinação | Como aparece | Por onde começar |
|---|---|---|
| Boutique + consultivo | Boutique de societário que também tem partido com algumas empresas | Checklist de revisão de contrato: as posições da casa servem aos dois |
| Solo + digital | Advogado sozinho que capta pelo Instagram | Atendimento e triagem, antes que o lead engula a agenda |
| Volume + digital | Causas repetitivas do lado autor, com captação online | Triagem e controladoria, com cuidado ético dobrado na publicidade |
| Full service com célula de volume | Escritório de várias áreas que pegou uma carteira de massa | Tratar a célula como um escritório dentro do escritório, com POP e indicador próprios |
| Solo + correspondência | Carteira própria pequena e audiências para colegas | Separar agenda e financeiro por tipo de cliente antes de qualquer automação |

**Boutique que quer ganhar escala.** É a transição mais pedida e a mais perigosa, porque o que faz a boutique valer o preço é justamente o que não escala. O caminho é escalar o entorno e proteger o núcleo:
1. Separe o sob medida do repetível: nos últimos casos, marque o que foi igual em todos (documentos pedidos, checklist inicial, estrutura do relatório, cláusulas que sempre aparecem).
2. Escreva primeiro o POP da parte repetível: entrada do cliente, checklist documental, relatório periódico. É onde a IA entra com S e A sem tocar na estratégia.
3. Leve o jeito de pensar do sócio para a base: teses, critérios de decisão, peças padrão ouro. Sem isso, nenhum associado assume e a escala vira queda de qualidade.
4. Defina por escrito o que continua H do sócio, coloque no código do escritório e conte ao cliente.
5. Meça as horas do sócio por caso, antes e depois (skill `medir-retorno`). Se elas não caírem, a escala só aumentou o volume de revisão.

**Solo que vai contratar.** Escreva o POP do setor-alvo antes da primeira contratação. A pessoa chega e aprende pelo papel, e a IA já está no fluxo como Auxílio. Você contrata para o que a IA não faz, e o perfil da vaga muda. Depois, troque a trilha no `perfil.md` (veja `docs/trilhas.md`).

**Volume que quer subir o ticket.** Crie uma trilha separada para os casos que fogem do padrão, com POP próprio e mais H. Misturar os dois fluxos num só derruba a eficiência do volume e a qualidade do caso especial.

**Digital que quer depender menos de anúncio.** Invista no Relacionamento com o cliente de quem já fechou: atualização de andamento bem feita gera indicação. A IA ajuda a manter esse contato sem tomar o dia da equipe.
