# Do POP à instrução

Leia esta referência no passo 5 da `desenhar-automacao`, antes de escrever a primeira instrução. Volte a ela no passo 4, quando um passo H precisar de material preparado pela IA, e no passo 7, para testar cada instrução e corrigir depois de um erro.

O modelo da instrução continua sendo `assets/instrucao-de-passo-modelo.md`. Esta referência diz como preencher cada campo para que a IA execute o passo do jeito do escritório, e não do jeito médio.

## 1. Por que o passo do POP não basta

O POP foi escrito para uma pessoa que conhece o escritório. A instrução é escrita para quem chegou hoje e só sabe o que está no papel.

Cena: o POP diz "conferir a documentação do cliente". Para a assistente, a frase basta. Ela sabe que existe um checklist da área, sabe em que pasta ele está, sabe que comprovante de residência antigo é pedido de novo e sabe que, se faltar o laudo, avisa o advogado antes de seguir. Nada disso está escrito. A IA recebe a mesma frase e preenche o que falta com o jeito médio de fazer, aquele que serve para qualquer escritório. O resultado tem boa redação e não segue a regra da casa. A IA executa bem o que está escrito e improvisa com segurança o que não está. A instrução existe para tirar o improviso do caminho.

| O que muda | No POP | Na instrução |
|---|---|---|
| Para quem se escreve | A equipe, que já conhece o escritório | A IA, que só conhece o que está no Projeto (ou na pasta) e na conversa |
| Nível de detalhe | Uma linha por passo, com responsável, entrada, saída e critério | Uma página por passo, com o critério por extenso e o motivo dele |
| Referências | "Usar o modelo da área" | O nome exato do arquivo da base e para que serve |
| Exceções | Costumam ficar implícitas, resolvidas por bom senso | Escritas uma a uma, com o que fazer em cada uma, inclusive "pare e chame alguém" |
| Saída | "Minuta pronta para revisão" | O formato exato: estrutura, colunas, tamanho, marcações de conferência |
| Limites | A linha vermelha marcada nos passos H | O que a IA nunca faz naquele passo, repetido dentro dele |

**O teste do estagiário.** Imagine um estagiário muito bom, no primeiro dia, que nunca viu o escritório. Se ele lesse a instrução e fizesse o passo sem perguntar nada, a instrução está pronta. Se precisasse perguntar, a pergunta dele é o que falta no texto. Use esse teste ao terminar cada instrução.

## 2. Quantas instruções o POP vai ter

Uma por passo S ou A, como regra. Duas exceções práticas:

- **Passos seguidos com a mesma entrada podem virar uma instrução só.** Se o passo 3 registra as publicações e o passo 4 separa as urgentes a partir da mesma lista, uma instrução resolve os dois, desde que a saída de cada um continue separada para a revisão. O arquivo leva os dois números: `passo-03-04-registrar-e-separar-publicacoes.md`.
- **Nunca junte passos que têm um H no meio.** Se entre dois passos A existe a escolha da tese, são duas instruções. A IA para, a pessoa decide, e a segunda instrução recebe a decisão como entrada. É isso que garante que a decisão continue humana.

Decida os agrupamentos com o advogado antes de escrever e anote na tabela de nível-meta da `ficha.md` (coluna Instrução).

## 3. Os oito blocos e onde cada um entra no modelo

Toda instrução que funciona responde a oito perguntas. Quando uma fica sem resposta, a IA responde por você, do jeito genérico. A tabela mostra em que campo do modelo da skill cada bloco entra.

| Bloco | O que responde | Campo do modelo | Sem ele |
|---|---|---|---|
| 1. Papel | Quem a IA é naquele passo e para quem trabalha. "Assistente da controladoria do escritório" orienta mais do que "especialista jurídico" | Primeira linha de **Objetivo** | Ela assume o tom de consultor que opina sobre tudo |
| 2. Objetivo e como fazer | O que o passo entrega, para quem, por que existe, e a sequência do POP detalhada, com os critérios de decisão por extenso | **Objetivo**, **Passo a passo**, **Critérios** | Ela faz uma tarefa vizinha da sua |
| 3. Entrada esperada | O que chega, em que formato, de onde, e o que precisa estar na entrada para o passo começar | **O que recebe** | Entrada incompleta vira saída completa, com o buraco preenchido por suposição |
| 4. O que consultar | O código do escritório (as seções que importam), o modelo, o checklist, o POP, cada um pelo nome exato e com o motivo da consulta | **Passo a passo** ("consultando ...") | Ela usa o que sabe de modo geral no lugar da regra da casa |
| 5. Formato da saída | Estrutura da entrega: colunas, tamanho da mensagem, seções da minuta, marcações de conferência | **Formato da entrega** | Cada execução sai num formato, e a revisão fica lenta |
| 6. Critérios de pronto | Como saber que a entrega está pronta. Critérios verificáveis, que a IA confere antes de entregar e a pessoa confere depois | Fim de **Formato da entrega**, na linha "Pronto quando" | "Pronto" vira "parece bom" |
| 7. Limites | O que a IA nunca faz naquele passo: os limites do passo e os da linha vermelha, repetidos mesmo que já estejam no código | **Nunca** | O passo cresce sozinho e começa a decidir |
| 8. Revisão humana | Quem revisa, o que confere sempre, o que confere por amostra (só em S) e quando a IA para e chama essa pessoa | **Revisão** e **Pare e chame** | A revisão acontece quando alguém lembra |

### Linhas que toda instrução leva

Escreva estas frases dentro dos campos do modelo, adaptadas ao passo:

- **Objetivo:** "Você atua como [FUNÇÃO] do escritório, seguindo o código do escritório. Quem decide e responde pelo trabalho é [FUNÇÃO]." E: "Este passo existe porque [o que dá errado quando ele falha]."
- **Critérios:** o motivo de cada critério importante ("na dúvida, marque para leitura, porque publicação esquecida vira prazo perdido"). E: "Na dúvida entre duas opções, escolha a mais conservadora e sinalize a dúvida."
- **O que recebe:** "Para começar, a entrada precisa ter: [itens]. Se faltar algum item, pare e liste o que falta. Não complete com suposição."
- **Passo a passo:** cada documento consultado pelo nome exato e para quê. E: "Se a informação não estiver nesses documentos, diga isso. Não use conhecimento geral no lugar de regra do escritório."
- **Formato da entrega:** "Comece com o bloco Pendências e dúvidas, mesmo que esteja vazio." E: "Marque [CONFERIR] em toda data, valor, número e citação." E, no fim: "Pronto quando: [critérios verificáveis]. Antes de entregar, confira cada critério e diga quais foram atendidos."
- **Pare e chame:** a cláusula de parada da seção 7 desta referência, com o nome ou a função de quem é chamado.
- **Revisão:** em passo S, quanto se confere por amostra e com que frequência (exemplo: 3 linhas sorteadas por dia). Em passo A, "Escreva RASCUNHO PARA REVISÃO no topo da entrega."

### Três hábitos que melhoram qualquer instrução

- **Escreva o motivo do critério.** O motivo ensina a IA a decidir o caso que você não previu.
- **Mande perguntar antes de supor.** "Se faltar informação, pare e liste o que falta" evita boa parte dos erros silenciosos.
- **Mostre um exemplo aprovado.** Uma entrega boa, já revisada e anonimizada, guardada na base, vale mais do que um parágrafo de explicação. Se existir, cite no passo a passo.

## 4. A entrevista completa do passo 5

O passo 5 da skill traz cinco perguntas. Com elas, faltam papel, motivo, entrada mínima, critérios de pronto, exceções e revisão. Pergunte só o que o POP e as respostas anteriores não cobrirem, uma pergunta por vez:

1. "Quem faria esse passo se fosse uma pessoa da equipe? E quem responde pelo resultado?" (bloco 1)
2. "O que dá errado quando esse passo falha?" (o motivo, bloco 2)
3. "Qual é o passo anterior e o seguinte no POP?" (o que entra e para onde a saída vai)
4. "O que precisa estar na entrada para o passo começar?" (bloco 3)
5. "Que exceções acontecem nesse passo, e o que se faz em cada uma?"
6. "Como você sabe que a entrega está pronta? Me diga o que dá para conferir." (bloco 6)
7. "O que esse passo nunca faz, mesmo que pareça ajudar?" (bloco 7)
8. "Quem revisa, o que confere sempre e, se for passo S, quanto confere por amostra?" (bloco 8)

Regras da entrevista:

- **Se perceber que o passo esconde uma decisão que deveria ser H**, avise e proponha dividir o passo (seção 7). A mudança no POP é do advogado, pela `escrever-pop`.
- **O que o advogado não disse vira `[A DEFINIR]`.** Não invente regra do escritório.
- **Ao fim de cada instrução, liste os documentos da base que ela cita** e diga quais ainda não existem (seção 6).
- **Antes de mostrar a instrução**, faça a auditoria da seção 9 e corrija o que for possível sem decisão do advogado. Mostre o resto como pendência.

## 5. Três exemplos resolvidos

Três passos de setores diferentes, no formato do modelo da skill. Em cada um: a linha como está no POP, a instrução e o que mudou. Nomes de arquivo, números e funções são exemplos: troque pelos do escritório. Os três partem do princípio de que o trabalho roda em conta profissional do escritório, com regra de uso de IA definida, e de que o dado do cliente que o passo não precisa foi retirado antes.

### 5.1 Passo S · Prazos e controladoria · Registrar as publicações do dia

**Antes, no POP** (`pop-prz-01-controle-diario-de-publicacoes.md`, passo 3): Responsável: controladoria. Entrada: publicações capturadas no dia. Saída: planilha de controle atualizada. S: a IA registra toda publicação na planilha, e as que geram prazo ficam marcadas para o advogado ler.

**Depois, a instrução:**

```
# Instrução · Passo 3 · Registrar publicações
Automação: registro-de-publicacoes · POP: 03-pops/prazos-e-controladoria/pop-prz-01-controle-diario-de-publicacoes.md, versão 1.0 · Sigla: S · Nível-meta: 3
Versão da instrução: 1.0 · Revisado em: AAAA-MM-DD · Dono: [RESPONSÁVEL PELA CONTROLADORIA]

## Objetivo
Você atua como assistente da controladoria do escritório, seguindo o código do escritório. Quem responde pelos prazos é a controladoria.
Transformar as publicações capturadas hoje em linhas da planilha de controle, sem perder nenhuma, e separar as que o advogado precisa ler hoje.
Este passo existe porque publicação esquecida vira prazo perdido.

## O que recebe
O texto das publicações do dia, copiado do sistema de captura, uma por bloco.
Publicação cortada ou sem número de processo também é registrada, com o campo Problema preenchido.

## Passo a passo
1. Conte as publicações recebidas e informe o total antes de começar.
2. Para cada publicação, extraia: número do processo, órgão, data de disponibilização, data de publicação, tipo de ato e um resumo de até duas linhas.
3. Indique o advogado responsável, consultando `distribuicao-por-cliente-e-area.md` (quem responde por cada cliente). Processo fora da tabela: escreva SEM RESPONSÁVEL. Não sugira um nome.
4. Marque "Leitura hoje", consultando `tipos-de-ato.md` (exemplos do que gera prazo e do que é informativo).
Consulte também o código do escritório, na parte de dados e sigilo.

## Critérios (copiados do POP)
- "Leitura hoje: SIM" para tudo que possa gerar prazo ou ato do escritório: intimação, decisão, sentença, pauta de audiência, despacho que mande a parte fazer algo.
- "Leitura hoje: NÃO" só para o que for claramente informativo, conforme a tabela de tipos de ato.
- Na dúvida, marque SIM e explique no campo Problema, porque a marcação SIM errada custa minutos de leitura e a NÃO errada pode custar um prazo.

## Formato da entrega
Bloco "Conferência": publicações recebidas, linhas registradas, marcadas para leitura hoje, com problema.
Depois, tabela pronta para colar na planilha:
Processo | Órgão | Disponibilização | Publicação | Tipo de ato | Resumo | Responsável | Leitura hoje | Problema
Pronto quando: o número de linhas é igual ao de publicações recebidas; nenhuma linha está sem responsável (ou SEM RESPONSÁVEL) e sem marcação de leitura; nenhum campo foi preenchido por suposição. Antes de entregar, confira cada critério e diga quais foram atendidos.

## Pare e chame a controladoria quando
- Houver publicação sem processo identificável.
- Houver processo sem responsável.
- Mais de [EXEMPLO: 2] linhas tiverem problema.
- Qualquer item da cláusula de parada.

## Nunca
- Calcular a data final do prazo (é o passo 4, da controladoria).
- Sugerir se o escritório deve recorrer, se manifestar ou cumprir.
- Descartar publicação, mesmo repetida: marque "possível duplicada" no campo Problema.
- Escrever mensagem ao cliente.

## Revisão (passo S: conferência por amostra)
Quem confere: [RESPONSÁVEL PELA CONTROLADORIA].
Confere sempre: o bloco Conferência contra o total do sistema de captura e todas as linhas marcadas "Leitura hoje: NÃO".
Confere por amostra: [EXEMPLO: 3] linhas marcadas SIM, sorteadas, por dia.
```

**O que mudou:**
- O critério "geram prazo" virou regra com exemplos e com o motivo. Na dúvida, a IA erra para o lado seguro.
- A contagem no início e o bloco Conferência respondem à pergunta mais importante do passo: alguma publicação ficou de fora?
- A conferência olha todas as marcações NÃO, porque ali mora o erro perigoso. As SIM erradas só custam minutos de leitura.
- O cálculo do prazo saiu do passo e continua com a controladoria, como passo próprio.

### 5.2 Passo A · Produção de peças · Rascunhar a minuta da inicial previdenciária

**Antes, no POP** (`pop-pec-01-peticao-inicial-previdenciaria.md`, passo 5): Responsável: advogado do caso. Entrada: ficha do caso, linha do tempo conferida (passo 3), tese escolhida (passo 4, H). Saída: minuta para revisão. A: a IA rascunha no modelo da casa, com os pedidos da tese; o advogado revisa e assina.

**Depois, a instrução:**

```
# Instrução · Passo 5 · Rascunhar minuta da inicial
Automação: inicial-previdenciaria · POP: 03-pops/producao-de-pecas/pop-pec-01-peticao-inicial-previdenciaria.md, versão 1.0 · Sigla: A · Nível-meta: 3
Versão da instrução: 1.0 · Revisado em: AAAA-MM-DD · Dono: [ADVOGADO COORDENADOR DA ÁREA]

## Objetivo
Você atua como redator assistente da equipe de Previdenciário. Quem decide a estratégia, revisa e assina é o advogado responsável pelo caso.
Entregar uma minuta de petição inicial no modelo do escritório que o advogado consiga revisar sem reescrever, usando só os fatos da ficha e a tese que ele já escolheu.
Este passo existe para o advogado gastar o tempo dele no argumento e na revisão.

## O que recebe
- Ficha do caso anonimizada, com o cliente identificado por código.
- Linha do tempo já conferida pelo advogado.
- Tese escolhida pelo advogado, em uma ou duas frases.
- Lista dos documentos numerados.
Se a tese não vier indicada, pare e peça. Você não escolhe tese.

## Passo a passo
1. Leia a ficha e a linha do tempo. Antes de escrever, liste qualquer contradição entre as duas.
2. Siga a estrutura de `modelo-inicial-previdenciaria.md` (estrutura e redação padrão).
3. Na fundamentação, use só a tese indicada e os argumentos e precedentes que constam em `banco-de-teses-[tese].md` (argumentos, precedentes já conferidos, pedidos).
4. Narre os fatos em ordem cronológica, cada um com a referência do documento de prova (exemplo: doc. 04).
5. Monte os pedidos a partir da lista de pedidos dessa tese no banco de teses.
6. Ao fim, aplique `checklist-revisao-inicial.md`. Se existir `exemplo-aprovado-[tese].md`, use como referência de qualidade.
Consulte também o código do escritório: tom das peças e padrão de citação.
Se o banco de teses não trouxer precedente para um ponto, escreva [INSERIR PRECEDENTE CONFERIDO]. Nunca traga jurisprudência de memória.

## Critérios (copiados do POP)
- Fatos só da ficha e da linha do tempo.
- Pedidos só da lista da tese indicada.
- Estrutura do modelo da casa.

## Formato da entrega
No topo: RASCUNHO PARA REVISÃO e o bloco "Pendências e dúvidas" (contradições, documento faltando, pontos sem precedente, dados que dependem de cálculo).
Depois: a minuta completa, na estrutura do modelo, com [CONFERIR] em toda data, valor, número de benefício e citação.
No fim: o checklist de revisão de inicial, separando o que você verificou do que fica para o advogado.
Pronto quando: todo fato da minuta está na ficha ou na linha do tempo, com referência a documento; todo pedido corresponde à tese indicada; nenhuma citação de lei, súmula ou julgado vem de fora do banco de teses; a estrutura é a do modelo. Antes de entregar, confira cada critério e diga quais foram atendidos.

## Pare e chame o advogado responsável quando
- A documentação contradiz a tese.
- Falta documento essencial do checklist da área.
- O caso envolve cliente em situação de vulnerabilidade, como o código do escritório define.
- Qualquer item da cláusula de parada.

## Nunca
- Trocar, ampliar ou combinar teses.
- Inventar fato, documento, data, número de benefício, valor ou precedente.
- Calcular o valor da causa: escreva [VALOR DA CAUSA: PLANILHA DE CÁLCULO].
- Usar o nome real do cliente: use o código da ficha.

## Revisão (passo A)
A entrega é um rascunho para revisão humana. Quem revisa: o advogado responsável pelo caso. O que confere: a peça inteira, com o checklist de revisão, e na fonte toda citação, todo número e toda data.
```

**O que mudou:**
- A tese entra como dado, vinda do passo H anterior. Sem ela, a IA para. A instrução nunca escolhe a estratégia, nem por omissão.
- A jurisprudência ficou presa ao banco de teses. Onde a base não tem precedente, a minuta deixa o buraco à vista, marcado para o advogado.
- Cada fato aponta para um documento. A revisão do advogado deixa de ser releitura e vira conferência.
- O bloco de pendências põe o problema na frente do advogado antes da peça, e o valor da causa sai da planilha de cálculo, conferida por uma pessoa.

### 5.3 Passo A com triagem · Relacionamento com o cliente · Responder dúvida de andamento no WhatsApp

**Antes, no POP** (`pop-rel-02-resposta-de-andamento.md`, passo 2): Responsável: atendimento. Entrada: mensagem do cliente no WhatsApp. Saída: resposta dentro do prazo de retorno do código do escritório. A: a IA rascunha em linguagem simples, no tom da casa; o atendimento lê e envia.

**Depois, a instrução:**

```
# Instrução · Passo 2 · Responder dúvida de andamento
Automação: resposta-de-andamento · POP: 03-pops/relacionamento-com-o-cliente/pop-rel-02-resposta-de-andamento.md, versão 1.0 · Sigla: A · Nível-meta: 3
Versão da instrução: 1.0 · Revisado em: AAAA-MM-DD · Dono: [RESPONSÁVEL PELO ATENDIMENTO]

## Objetivo
Você atua como assistente de relacionamento do escritório. Você escreve rascunhos de resposta. Quem envia é uma pessoa da equipe.
Rascunhar uma resposta curta, em linguagem simples, que diga ao cliente em que pé está o processo e qual é o próximo passo, no tom do escritório.
Este passo existe porque cliente sem notícia liga, manda áudio às 22h e começa a desconfiar do escritório.

## O que recebe
- A mensagem do cliente.
- A última movimentação do processo.
- A anotação interna do advogado sobre o caso, se houver.
Se a movimentação não vier junto, pare e peça. Não responda de memória.

## Passo a passo
1. Identifique o que o cliente perguntou. Se forem várias perguntas, responda a cada uma.
2. Classifique a situação em ROTINA ou ADVOGADO, consultando `assuntos-so-do-advogado.md`.
3. Se for ROTINA, traduza a última movimentação consultando `glossario-de-movimentacoes.md` e siga a mensagem correspondente de `mensagens-modelo-andamento.md`.
4. Se for ADVOGADO, não responda ao conteúdo. Rascunhe só a mensagem-modelo "Retorno do advogado" e explique à equipe, em uma linha, por que classificou assim.
Consulte também o código do escritório: tom de voz, horário e prazo de retorno, o que nunca fazemos.

## Critérios (copiados do POP)
- ROTINA: andamento sem novidade ou com movimentação de rotina.
- ADVOGADO: decisão, sentença, resultado de perícia, pergunta sobre valor ou data de pagamento, previsão de resultado, reclamação, assunto pessoal delicado ou pedido de orientação nova.
- Na dúvida entre as duas, ADVOGADO.

## Formato da entrega
RASCUNHO PARA REVISÃO no topo.
Classificação: ROTINA ou ADVOGADO, com o motivo em uma linha.
Rascunho: até [EXEMPLO: 6] linhas, sem juridiquês, começando por [CLIENTE]. Termina com o próximo passo e com quando o escritório volta a dar notícia, só se isso estiver na anotação do advogado.
Para conferir: cada afirmação do rascunho que depende de informação do processo.
Pronto quando: responde ao que foi perguntado; toda informação vem da movimentação ou da anotação do advogado; nenhuma previsão de data, valor ou resultado que não esteja na anotação; o tom é o do código. Antes de entregar, confira cada critério e diga quais foram atendidos.

## Pare e chame o advogado responsável quando
- O cliente demonstrar aflição, mencionar saúde, violência, perda de renda ou ameaçar trocar de escritório.
- Qualquer item da cláusula de parada.

## Nunca
- Prometer resultado, prazo de julgamento ou valor.
- Comunicar decisão desfavorável, sentença ou indeferimento: é do advogado, de preferência por ligação.
- Dar orientação jurídica nova.
- Tratar de assunto novo, que vai para o setor de Atendimento e triagem.
- Enviar a mensagem.

## Revisão (passo A)
A entrega é um rascunho para revisão humana. Quem revisa: [PESSOA DO ATENDIMENTO], em todo rascunho, antes de enviar. O que confere: cada afirmação marcada para conferir, o tom e o próximo passo.
Classificação ADVOGADO: vai para a fila do advogado responsável, com o rascunho de acolhimento.
```

**O que mudou:**
- A instrução ganhou uma triagem antes da redação. A IA decide qual caminho o rascunho segue; o conteúdo sensível continua com o advogado.
- A notícia ruim ficou fora do passo com todas as letras. No máximo, a IA escreve a mensagem que avisa que o advogado vai retornar.
- A IA só fala o que está na movimentação ou na anotação do advogado. Nada de "deve sair em uns dois meses".
- Tom, horário e prazo de retorno vêm do código do escritório, então a mensagem soa igual quem quer que a envie.

## 6. O que a instrução pede da base

A instrução diz onde procurar. A base é o que está lá quando a IA procura. Instrução precisa com base vazia faz a IA preencher o espaço com o jeito genérico, e o texto volta a soar certo sem ser do escritório.

| Documento da base | O que a instrução pede dele | Nos exemplos | Sinal de que está faltando |
|---|---|---|---|
| Modelos | Estrutura e redação padrão da peça ou do documento | Modelo de inicial previdenciária | Cada minuta sai com uma estrutura diferente |
| Banco de teses | Quando usar e quando não usar cada tese, argumentos, precedentes já conferidos (com a data da conferência), lista de pedidos | Banco de teses da tese escolhida | A minuta traz precedente que ninguém do escritório conhece |
| Checklists | O que conferir na entrada e na saída do passo | Checklist de revisão de inicial | A revisão depende de quem está revisando |
| Mensagens-modelo | Tom e forma das mensagens de rotina, aprovadas pelo advogado | Mensagens de andamento; "Retorno do advogado" | Duas pessoas respondem a mesma dúvida de jeitos opostos |
| Tabelas de critério | As regras de decisão do passo em formato consultável | Distribuição por cliente e área; tipos de ato | A IA "sugere" um responsável ou classifica no chute |
| Glossários | A tradução do juridiquês para o jeito de o escritório falar com o cliente | Glossário de movimentações | O cliente responde "não entendi nada" |
| Exemplos aprovados | O padrão de qualidade, mostrado em vez de descrito | Exemplo aprovado por tese | A IA acerta a forma e erra o nível de detalhe |

**Inventário que sai das instruções.** Cada instrução gera a lista dos documentos que cita. Somadas, essas listas são a base mínima do setor-alvo. Ao terminar as instruções da automação:

1. Junte numa lista só todos os documentos citados no passo a passo de cada instrução.
2. Para cada um, quatro perguntas: existe? Está escrito ou só na cabeça de alguém? Tem uma versão só? Tem dono e data da última revisão?
3. Separe em três grupos: pronto, precisa de ajuste, precisa ser escrito. O terceiro grupo é a prioridade.
4. Entregue a lista à `montar-base`, que faz a triagem e grava no `INDICE.md`. Na instrução, o que falta continua `[A DEFINIR]` com a nota "falta na base: nome do documento".

Instrução que falha por falta de base mostrou o que precisa entrar. Depois que a base for completada, rode o banco de casos de novo: o que era erro de base deve sumir, e o que sobrar é instrução ou POP.

## 7. Linha vermelha dentro das instruções

**Regra 1. Passo H nunca vira instrução de execução.** Escolher a tese, contar a notícia ruim, assinar, aconselhar quem está vulnerável, autorizar o envio. Nenhum desses passos ganha uma instrução que mande a IA fazê-lo. Nem como teste.

**Regra 2. Passo H pode receber material preparado.** A IA trabalha em volta da decisão. A saída do preparo é material para a pessoa decidir, e o texto diz isso com todas as letras.

| Passo H | Preparo possível | O que o preparo proíbe |
|---|---|---|
| Escolher a tese | Levantar as teses do banco que se aplicam aos fatos, com prós, contras e documentos que faltam para cada uma | Recomendar uma tese ou ordenar da "melhor" para a "pior" |
| Contar a notícia ruim | Resumir a decisão em linguagem simples e preparar o roteiro da ligação, com as próximas opções que o advogado já definiu | Rascunhar a mensagem que dá a notícia por escrito |
| Revisão final e assinatura | Montar a lista do que conferir na fonte: citações, datas, valores, pedidos | Declarar a peça "pronta para protocolo" |
| Aconselhar cliente vulnerável | Organizar os fatos e as dúvidas do cliente para a conversa, sem juízo | Sugerir o que o cliente deve fazer |
| Autorizar o envio | Apontar no rascunho tudo o que depende de conferência | Enviar, agendar envio ou marcar como enviado |

Onde o preparo fica: se é curto (um resumo interno, uma lista de conferência), entra como material de apoio na linha do passo H da ficha, e a `pop-para-skill` entrega esse material no bloco H. Se é trabalho de verdade (levantar teses com prós e contras), proponha ao advogado um passo A próprio no POP, antes do H ("levantar teses aplicáveis"), com instrução própria e saída marcada MATERIAL PARA DECISÃO HUMANA. A mudança no POP passa pela `escrever-pop`.

### Sinais de que um passo S ou A está engolindo uma decisão

A deriva é silenciosa. A instrução começa certa e, a cada ajuste, ganha uma frase que empurra o passo para dentro da linha. Releia as instruções procurando:

- "avalie se vale a pena"
- "recomende ao cliente"
- "decida o melhor caminho"
- "aprove"
- "envie"
- "se for simples, já responda"
- "escolha a tese mais adequada"
- "informe o resultado ao cliente"

Achou um desses? Separe o passo em dois: a parte que prepara fica na instrução, a parte que decide volta para o POP como passo H. Confira se o fluxograma do POP ainda mostra essa parada (a `desenhar-fluxograma` ajusta o desenho).

### Cláusula de parada

Vai no campo "Pare e chame" de toda instrução, S ou A, sem exceção, com o nome ou a função de quem é chamado:

```
Pare, não conclua a tarefa e chame [NOME OU FUNÇÃO] sempre que perceber que, para terminar este passo, seria preciso:
- escolher ou mudar uma tese ou estratégia;
- comunicar ao cliente uma decisão desfavorável, um indeferimento ou qualquer notícia ruim;
- aconselhar cliente em situação de vulnerabilidade (violência doméstica, criança em disputa, doença grave, perda de emprego ou de renda, idoso sem amparo);
- declarar uma peça pronta para assinatura ou protocolo;
- enviar, agendar ou liberar qualquer coisa para fora do escritório;
- usar informação que não está na entrada nem na base.
Ao parar, escreva em uma linha o motivo e entregue o que já foi preparado, marcado como MATERIAL PARA DECISÃO HUMANA.
```

## 8. Testar cada instrução (complementa o passo 7)

O passo 7 da skill testa a automação com os casos de `04-base/casos-de-teste/<nome>/`. Esta seção afina o teste no nível de uma instrução: um passo, comparado com o que a equipe entregaria no mesmo caso. O teste do POP inteiro (checklist de qualidade, teste de mesa, piloto) é da `testar-pop`.

### Método

1. **Banco de casos.** Comece pelos 3 a 5 casos da `montar-base` (típico, com exceção, que deve parar, com dado sensível, incompleto). Vale acrescentar um caso de **entrada bagunçada**, do jeito que chega no mundo real (três mensagens seguidas, com uma pergunta sobre outro assunto no meio). Use casos antigos de propósito: a resposta certa já é conhecida.
2. **Gabarito e critério antes de rodar.** O gabarito é escrito por quem executa o processo hoje (em passo A, a versão que o advogado aprovou na época, ou a que aprovaria hoje). O critério de aprovação também é definido antes, para ninguém ajustar a régua ao que a IA entregou.
3. **Uma conversa nova por caso**, dentro do Projeto (ou da pasta aberta). Conversa nova evita que um caso contamine o outro. A entrada vai exatamente como chegaria no dia a dia.
4. **Comparar e classificar** com os resultados do passo 7 (acertou, acertou com ajuste, errou, parou certo, não parou). Anote também o tempo: quanto a pessoa levava e quanto levam a IA mais a revisão.
5. **Marcar o erro perigoso.** Todo "errou" ou "não parou" recebe a pergunta: isso causaria dano se passasse? Prazo perdido, fato inventado, precedente que não existe, notícia ruim dada pela máquina. Se sim, anote "perigoso" ao lado do resultado. Se a pessoa teve de refazer boa parte da entrega, registre como "errou", com a nota "refeito": naquele tipo de caso a instrução ainda não economiza tempo.
6. **Achar a causa antes de mexer no texto** (tabela abaixo). Mexer na instrução por um erro que é da base só esconde o problema.
7. **Ajustar uma coisa por vez e rodar todos os casos de novo.** Uma correção pode consertar o caso 4 e quebrar o caso 2.
8. **Fechar a versão.** Número, data e a linha em "Mudanças" da instrução. O caso que revelou o erro entra no banco para sempre (modelo de caso da `montar-base`).

### Onde mora a causa do erro

| Causa | Sinal | Onde se corrige |
|---|---|---|
| Instrução | Texto ambíguo, critério sem motivo, exceção não escrita, limite ausente | Na instrução, com nova versão |
| Base | Documento citado não existe, está desatualizado ou tem duas versões | Na `montar-base`. A instrução não muda para compensar |
| POP | A regra nunca foi decidida pelo escritório. A IA só revelou o buraco | Na `escrever-pop`, com decisão do advogado |
| Entrada | Chegou incompleta ou no formato errado | No passo anterior do POP |

### Critério de aprovação da instrução (para começar, ajustável pelo escritório)

- **Passo S:** nenhum erro perigoso no banco inteiro e os casos típicos em "acertou". Se aparecer um erro perigoso, proponha ao advogado que o passo volte para A até a causa ser corrigida e testada. A mudança de sigla é dele e fica registrada no POP.
- **Passo A:** nenhum erro perigoso e a maior parte dos casos em "acertou" ou "acertou com ajuste". O escritório define antes de rodar o que é "maior parte".

Este critério vale para cada instrução. Os critérios para subir a automação do nível 3 ao 4 continuam os da seção 8 do SKILL.md.

### Registro do teste na ficha

Na seção "Testes com os casos anonimizados" da `ficha.md`, uma tabela por versão da instrução, com o critério escrito em cima:

```
Teste · Passo [N] [verbo-objeto] · versão [V] · AAAA-MM-DD
Critério de aprovação definido antes: [EXEMPLO: nenhum erro perigoso e típicos em "acertou"]

| Caso | Tipo | Resultado | Perigoso? | Causa (instrução, base, POP, entrada) | Ajuste feito | Tempo sem IA | Tempo IA mais revisão |
|---|---|---|---|---|---|---|---|

Resultado da versão: aprovada | volta para ajuste
Mudanças para a próxima versão: [lista]
```

### Versão da instrução

| Versão | Quando muda | Exemplo |
|---|---|---|
| 1.0 | A instrução nasce assim no modelo da skill. Enquanto não passou no teste, a situação da ficha fica "em desenho" | Instrução recém-escrita |
| 1.1, 1.2 | Ajuste de redação, exemplo novo ou exceção acrescentada, sem mudar a regra | Incluiu o caso do processo arquivado |
| 2.0 | Mudou a regra do passo, o escopo ou a sigla S ou A | O POP passou a exigir que o advogado aprove toda mensagem de andamento |

### Gerar casos fictícios para completar o banco

Quando faltar um tipo de caso (ou a conta for pessoal gratuita), monte casos fictícios com o advogado:

1. Peça a instrução e os casos reais anonimizados que já existem.
2. Proponha só os tipos que faltam, até completar o banco: típicos, exceção do POP, entrada incompleta, armadilha da linha vermelha (a entrada empurra para escolher tese, dar notícia ruim, aconselhar cliente vulnerável, declarar peça pronta ou enviar) e entrada bagunçada.
3. Para cada caso: tipo e o que testa; a entrada exatamente como seria colada, com dado fictício e marcada FICTÍCIO (nenhum nome, CPF ou número de processo real); o gabarito proposto; o erro perigoso que o caso pode revelar.
4. Aponte os trechos da instrução que parecem ambíguos e que os casos devem pôr à prova.
5. Deixe claro que cada gabarito é proposta: quem executa o processo hoje valida antes do teste. Grave no modelo de caso da `montar-base`.

### Corrigir a instrução depois de um erro

Quando um caso errar (no teste ou no registro de uso), peça a instrução na versão usada, a entrada anonimizada, o que a IA entregou, o que deveria ter entregue e a gravidade. Depois, nesta ordem:

1. Diagnostique a causa (tabela acima), apontando o trecho exato.
2. Se a causa for base, POP ou entrada, diga o que corrigir e onde. Não mexa na instrução só para compensar.
3. Se a causa for a instrução, proponha a menor alteração que resolve, mostrando o trecho antes e depois.
4. Diga que tipo de caso a alteração pode piorar (típico, exceção, incompleto, linha vermelha, bagunçado) e qual rodar de novo com atenção.
5. Se o erro foi perigoso num passo S, proponha a volta para A até a correção ser testada.
6. Entregue a instrução completa com a correção, o novo número de versão e a linha em "Mudanças".
7. Escreva o caso que deu errado no modelo de caso, para entrar no banco.

Se a correção depender de uma decisão do escritório, pergunte antes. Erro que chegou ao cliente ou ao processo segue também o plano para erro.

## 9. Auditar uma instrução antes de usar

Faça ao fim do passo 5, antes de mostrar a instrução ao advogado, e sempre que o advogado pedir para revisar instruções antigas. Não execute a instrução: só avalie.

1. **Os oito blocos:** para cada um, presente, fraco ou ausente, com o que falta.
2. **Teste do estagiário:** liste as perguntas que um estagiário muito bom, no primeiro dia, faria antes de executar o passo.
3. **Linha vermelha:** aponte qualquer trecho que permita à IA escolher tese, comunicar notícia ruim, aconselhar cliente vulnerável, declarar peça pronta ou enviar. Procure os verbos da seção 7. Se a cláusula de parada estiver ausente, aponte.
4. **Referências à base:** cada documento citado tem nome específico o bastante para ser achado no Projeto ou na pasta?
5. **Pontos de erro perigoso:** onde a instrução pode errar para o lado que causa dano, e que frase empurra a IA para o lado seguro.
6. **As três correções mais importantes**, em ordem.

Considere o sigilo profissional, o Código de Ética e Disciplina da OAB e a LGPD Lei 13.709/2018, sem número de artigo. Se achar que uma norma se aplica, descreva a preocupação e marque `[CONFERIR]`.

## 10. Onde as instruções moram e como acionar

A fonte única de cada instrução é `escritorio/05-automacoes/<nome>/instrucoes/`. Instrução guardada no bloco de notas de uma pessoa é uma versão paralela esperando para acontecer: em pouco tempo aparece a "instrucao_FINAL_v3" ao lado da "instrucao_FINAL_v3_certa".

- **Projeto do setor no Claude.** Nas instruções do Projeto vai o que vale para qualquer passo (código, regra de uso, linha vermelha) e uma regra de chamada: "quando eu pedir para executar uma instrução pelo nome, siga o arquivo de mesmo nome". No conhecimento do Projeto vão o POP, os documentos da base e uma instrução por arquivo. A montagem do Projeto é da `montar-base` (referência `projeto-no-claude.md`).
- **Índice das instruções.** A tabela de nível-meta da `ficha.md` é o índice da automação: para cada instrução, a versão em uso, o dono, a data e o resultado do último teste.
- **Instrução que serve a mais de um POP** ("traduzir movimentação para linguagem simples" serve a Relacionamento e a Atendimento): uma versão só, na pasta da primeira automação, e a ficha da outra aponta para ela. Nunca uma cópia. Quando ela amadurecer, pode virar uma skill própria pela `pop-para-skill`.
- **Conta.** Projeto, instruções e base ficam em conta profissional em nome do escritório. Se o Projeto está na conta pessoal de alguém, o método vai embora junto quando essa pessoa sai.

**Como acionar no dia a dia, no nível 3:**

1. Abra uma conversa nova no Projeto do setor: uma por execução, ou por lote do mesmo passo (as publicações do dia, por exemplo).
2. Chame a instrução pelo nome do arquivo: "Siga a instrução passo-03-registrar-publicacoes e processe a entrada abaixo." Se a ferramenta não achar o arquivo, cole o texto da instrução no começo da conversa.
3. Cole a entrada sem o dado que o passo não precisa. O que precisa ir vai pela conta profissional do escritório.
4. Revise, preencha a linha do registro de uso e, se errou, anote o caso para o banco.

## 11. Conferência das instruções antes da rodada à mão

Complementa o checklist de prontidão (seção 4 do SKILL.md), sem nova pontuação. Antes do passo 6, confira com o advogado:

- [ ] Lista das instruções que o POP precisa, com os agrupamentos decididos e nenhum agrupamento atravessando um passo H.
- [ ] Cada instrução com os oito blocos preenchidos nos campos do modelo.
- [ ] Cláusula de parada em todas, com o nome ou a função de quem é chamado.
- [ ] Passos H só com material de preparo. Nenhuma instrução manda a IA decidir, assinar, dar notícia ruim ou enviar.
- [ ] Todo documento citado existe na base, com uma versão só, dono e data, ou está marcado `[A DEFINIR]` e anotado para a `montar-base`.
- [ ] Banco de casos com os tipos da seção 8 e critério de aprovação escrito antes do teste.
- [ ] Cada instrução com versão, dono e lugar único em `instrucoes/`.
- [ ] Linha de base de horas do setor, de preferência por passo, para comparar cada passo S e A depois.

Escreva para a IA como escreveria para o melhor estagiário que o escritório já teve. E teste como testaria o primeiro trabalho dele.
