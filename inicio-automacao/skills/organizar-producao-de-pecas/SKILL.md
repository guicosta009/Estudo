---
name: organizar-producao-de-pecas
description: >
  Organiza o setor de produção de peças com a IA dentro do fluxo, sem redigir a peça: mostra o
  ciclo da peça em onze etapas e onde o fluxo do escritório muda, adapta o POP do tipo de peça
  (petição inicial, contestação, recurso, manifestação, cumprimento de sentença), instala a ficha
  de briefing, organiza o banco de modelos e o caderno de teses, instala o checklist de revisão
  com a regra de citação e prepara o Projeto de peças. Use quando o advogado disser "organizar a
  produção de peças", "POP de contestação", "POP de recurso", "ficha de briefing", "banco de
  modelos", "caderno de teses", "checklist de revisão de peça", "a IA inventou jurisprudência",
  "montar o Projeto de peças", "cada peça sai de um jeito". Não use para redigir a peça de um caso
  concreto (fica fora do plugin) nem para POP de outro setor (use escrever-pop).
---

# Organizar a produção de peças

> Monta o setor de peças para a IA trabalhar a partir do que o advogado decidiu: o ciclo da peça, o POP do tipo de peça que mais toma tempo, a ficha de briefing, o banco de modelos, o caderno de teses, o checklist de revisão e o Projeto de peças. A skill organiza o setor. Ela não escreve a peça de nenhum caso.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). S, A, H, linha vermelha, níveis e anatomia do POP: `../../docs/glossario.md`. Solo e equipe: `../../docs/trilhas.md`. Pastas: `../../docs/pasta-do-escritorio.md`.

Esta skill é o conjunto do setor de peças. Ela usa o formato e os 8 passos de adaptação do `escrever-pop` (entrada B) para o POP, e o cabeçalho, o índice e o critério de entrada da `montar-base` para a base. O que ela acrescenta é o que só peça tem: o ciclo de onze etapas, cinco POPs por tipo de peça, a ficha de briefing, o banco de modelos vivo, o caderno de teses, o checklist de revisão de peça feita com IA e a regra de citação.

## 1. Quando usar

**Use quando:**
- O setor-alvo é Produção de peças, ou peça é onde as horas estão e o advogado quer começar por ela.
- O escritório já usa IA para minuta, mas cada peça sai de um jeito, a revisão virou reescrita ou já apareceu citação que não existia.
- O advogado quer o POP de um tipo de peça (inicial, contestação, recurso, manifestação, cumprimento de sentença).
- A pasta de modelos é a "modelos_FINAL_v3": quatro versões, ninguém sabe qual vale, nome de cliente antigo no terceiro parágrafo.
- É hora de montar o Projeto de peças no Claude.

**Não use quando:**
- O pedido é redigir, revisar ou pesquisar a peça de um caso concreto. Isso fica fora do escopo do plugin: a skill organiza o setor e entrega os prompts, mas não produz a peça.
- O POP é de outro setor: use `escrever-pop`. Para o WhatsApp e o atendimento, use `organizar-atendimento-whatsapp`.
- Só falta marcar S, A ou H numa lista pronta: use `classificar-sah`.
- O POP de peça está pronto e o pedido é revisar riscos antes de automatizar: use `auditar-riscos`.

## 2. Antes de começar

1. **Leia o perfil.** `escritorio/perfil.md` (trilha, porte, áreas, conta de IA, setor-alvo). Leia também `escritorio/01-cultura/codigo-do-escritorio.md` (tom, prazos internos, quem decide) e `escritorio/01-cultura/regra-de-uso-de-ia.md`, se existirem. Sem perfil, ofereça `/inicio-automacao:comecar` ou faça o modo rápido das regras transversais.
2. **Portão.** O setor de peças precisa ser o setor-alvo ou uma escolha consciente do advogado. Se o `setor_alvo` for outro, diga em uma frase que a ordem recomendada é começar pelo setor-alvo, e siga se ele quiser, registrando em "Etapas puladas". Sem código do escritório, os prazos internos e o tom ficam `[A DEFINIR]`: ofereça o `codigo-do-escritorio` e siga.
3. **Conta de IA.** Se o perfil diz conta pessoal gratuita ou não há regra de uso escrita, avise logo: documento de cliente só entra no Projeto de peças em conta profissional, com a regra escrita. Até lá, nenhum passo com dado de cliente fica S, e os testes usam caso fictício.
4. **Veja o que já existe.** Procure `escritorio/03-pops/producao-de-pecas/` e `escritorio/04-base/producao-de-pecas/`. Se houver POP de peça (por exemplo, o da biblioteca adaptado pelo `escrever-pop`) ou checklist criado pela `montar-base`, esta rodada é uma revisão: suba a versão e marque cada mudança com `[NOVO]` ou `[ALTERADO]`.
5. **Escopo da rodada.** Pergunte: "Quer organizar o setor inteiro (POP, ficha, banco, teses, checklist e Projeto) ou só uma parte agora?" Rodada inteira costuma levar mais de uma conversa. A ordem dos passos abaixo é a recomendada, e cada passo grava o que produziu.

## 3. O que nunca muda no setor de peças

Vale para todo POP, ficha, modelo e prompt que esta skill produz, em qualquer nível de automação:

1. **Tese, pedidos e assinatura são H.** A IA pode listar caminhos a partir do caderno de teses. Quem escolhe a tese, decide os pedidos e assina é o advogado, com nome e OAB.
2. **Nenhuma citação entra sem conferência na fonte oficial.** Jurisprudência, súmula, artigo de lei e doutrina sugeridos pela IA ficam `[CONFERIR]` até uma pessoa abrir a fonte oficial e registrar link, data e nome na tabela de citações. Peça antiga e modelo não são fonte.
3. **A IA não calcula prazo de peça.** Prazo fatal é o que a controladoria lançou e conferiu. A ficha e o POP só registram a data que alguém já conferiu.
4. **A tese vem antes da minuta.** Pedir a peça e decidir a tese em cima do texto pronto é deixar a máquina escolher.
5. **A peça inteira é lida por quem assina,** do começo ao fim, por curta que seja.

Os quatro jeitos de acelerar o caos que estas regras evitam: **minuta sem modelo** (cada peça sai diferente e a revisão vira reescrita); **tese escolhida pela máquina** (a IA tende ao argumento mais comum, e o advogado assina uma estratégia que não escolheu); **fatos que ninguém conferiu** (onde falta informação, a IA preenche com o plausível: uma data, um valor arredondado, um documento que ninguém juntou); **citação sem fonte** (julgado que não existe, súmula com número trocado, artigo na redação antiga, trecho entre aspas que o tribunal nunca escreveu). "Automatizar o caos continua sendo caos, só que com mais velocidade."

## 4. Fluxo

### Passo 1. Entender o escritório e as peças

Retrato antes de melhoria. Pergunte uma de cada vez, só o que não está no perfil (no máximo 8):

1. "Quais peças o escritório mais faz, e quantas de cada por mês, mais ou menos?"
2. "Qual delas mais toma tempo, ou mais volta para correção?"
3. "Quem mexe com peça hoje: quem monta, quem revisa, quem assina e quem protocola?" No solo, troque por: "Em que hora do dia você monta peça, e em que hora revisa?"
4. "Onde estão os modelos hoje? Pasta compartilhada, software jurídico, e-mail, o computador de alguém?"
5. "Vocês têm teses escritas em algum lugar, ou cada um lembra das suas?"
6. "Como a IA entra na peça hoje, e em que tipo de conta?"
7. "Me conte a última peça desse tipo, do pedido ao protocolo, na ordem em que aconteceu."
8. "Onde ela travou, atrasou ou voltou?"

Resposta vaga vira pedido de exemplo ("e a última contestação, como foi?"). Dado de cliente na conversa: avise, não repita e siga com a versão anonimizada. Devolva o retrato em poucas linhas (passos, quem faz, onde trava) e peça ok.

### Passo 2. Mostrar o ciclo e onde o fluxo dele difere

Apresente o ciclo em onze etapas e quatro grupos (detalhe, fluxograma e raias em `references/ciclo-da-peca.md`):

| Grupo | Etapas | Sigla |
|---|---|---|
| Antes da minuta | 1 Gatilho · 2 Briefing do caso · 3 Triagem de documentos · 4 Escolha da tese | S · A · S e A · **H** |
| Produção | 5 Pesquisa · 6 Minuta | A · A |
| Portões | 7 Revisão técnica · 8 Revisão de forma e citações · 9 Aprovação e assinatura | H e A · A · **H** |
| Saída | 10 Protocolo · 11 Registro e prazo | S e A · S |

Compare com o retrato do passo 1 e marque as diferenças: etapa que o escritório pula (o mais comum: tese depois da minuta, pesquisa sem tabela, revisão sem critério), etapa feita por quem não deveria, etapa que não existe no ciclo. Depois pergunte: "Alguma destas situações é comum no escritório?"

- **Solo:** os passos continuam, só mudam de momento. Revisão técnica em outro horário, de preferência no dia seguinte.
- **Peça urgente:** briefing de dez linhas, pesquisa restrita ao que já está conferido no caderno de teses. Tese, citação conferida, leitura integral e assinatura não saem.
- **Peça de massa:** enquadramento na tese antes do briefing. POP completo em `../escrever-pop/references/biblioteca/area-civel-massa.md`.
- **Peça que volta do cliente:** documento novo volta à ficha primeiro; só depois se mexe na minuta.

O que o advogado marcar vira exceção no POP do passo 3. Não proponha mudança antes do ok no retrato.

### Passo 3. Escolher o tipo de peça e adaptar o POP

Mostre os cinco POPs de referência e sugira começar pela peça que mais toma tempo (pergunta 2 do passo 1). Um POP por rodada.

| POP | Arquivo | Quando usar | S | A | H | O portão que mais pesa |
|---|---|---|---|---|---|---|
| POP-PEC-01 Petição inicial a partir de modelo | `references/pop-pec-01-peticao-inicial.md` | Caso novo, contrato assinado, documentos completos | 3 | 7 | 2 | Tese escolhida antes da minuta |
| POP-PEC-02 Contestação ou defesa | `references/pop-pec-02-contestacao.md` | Citação ou intimação para defesa registrada | 3 | 6 | 3 | Nenhum pedido da inicial sem resposta |
| POP-PEC-03 Recurso | `references/pop-pec-03-recurso.md` | Decisão desfavorável publicada, ou contrarrazões | 3 | 7 | 2 | Decidir com o cliente se recorre |
| POP-PEC-04 Manifestação e impugnação | `references/pop-pec-04-manifestacao.md` | Intimação para se manifestar; peças curtas e recorrentes | 3 | 5 | 2 | Posição decidida e registrada |
| POP-PEC-05 Cumprimento de sentença | `references/pop-pec-05-cumprimento-de-sentenca.md` | Decisão que permite cobrar o que foi concedido | 3 | 5 | 3 | Cálculo batendo com o título |

Abra só o arquivo escolhido e adapte pelos 8 passos da entrada B do `escrever-pop` (`../escrever-pop/SKILL.md`, seção 3), com o retrato do passo 1 no lugar do "passo a passo atual". Regras próprias de peça na adaptação:

1. **Troque funções por pessoas.** Se a mesma pessoa monta e assina, mantenha os dois passos e escreva quando acontece a revisão (outro momento, de preferência outro dia).
2. **Revise a sigla de cada passo para o estágio do escritório,** pela árvore do `classificar-sah`, com uma linha de justificativa. Sem conta profissional ou sem regra de uso escrita, nenhum passo com dado de cliente fica S.
3. **Não mexa nos portões:** escolha de tese e pedidos, revisão final com leitura integral e assinatura continuam H em qualquer cenário; o passo de pesquisa com tabela de citações e conferência na fonte oficial continua existindo.
4. **Prazos:** prazo interno vem do código do escritório ou fica `[A DEFINIR]`, com o exemplo do POP ao lado. Prazo processual é sempre "o que a controladoria lançou e conferiu na fonte" `[CONFERIR]`. Nenhum passo pede à IA que calcule prazo.
5. **Exceções:** inclua as situações marcadas no passo 2 e, se o escritório atua em Família, a exceção obrigatória de violência, coação ou risco.
6. **Exemplo por área:** mantenha só o das áreas do escritório. Se houver POP de área na biblioteca do `escrever-pop` (reclamatória, defesa da empresa, alimentos, indenizatória, massa), ofereça juntar os dois e cortar o que sobra.
7. **Lista do que a IA consulta:** no fim do POP, a tabela "O que a IA vai precisar consultar". Em peças ela quase sempre tem: modelo do banco, ficha de briefing, caderno de teses, checklist de revisão, tabela de citações e, conforme a peça, quadro da inicial, checklist de requisitos do recurso, catálogo de peças curtas, premissas de cálculo.

Use o modelo `../escrever-pop/assets/pop-modelo.md` para os 12 campos. Mostre o POP, peça ajustes e grave em `escritorio/03-pops/producao-de-pecas/pop-pec-<nn>-<tipo>.md` (`pop-pec-01-peticao-inicial.md`, `pop-pec-02-contestacao.md`, `pop-pec-03-recurso.md`, `pop-pec-04-manifestacao.md`, `pop-pec-05-cumprimento-de-sentenca.md`). O fluxograma pode sair da referência adaptada ou ser refeito com a `desenhar-fluxograma`.

### Passo 4. Instalar a ficha de briefing

A minuta só sai do jeito do escritório quando a IA recebe o caso do jeito do escritório. Colar quarenta páginas de PDF e escrever "faz a contestação" é pedir para a IA decidir sozinha o que importa.

1. Mostre a ficha de 12 campos (`assets/ficha-de-briefing.md`) e os campos que mais se preenche errado: fatos com fonte, teses descartadas, o que não pode faltar, o que não pode aparecer, prazos, citações conferidas.
2. Ajuste ao escritório, uma pergunta por vez: "Quais tipos de peça entram no campo 1?" e "Em alguma área a ficha precisa de um campo a mais?" (por exemplo, Previdenciário: o que o INSS analisou e o que ficou de fora; Família: o campo 11 protege a criança).
3. Mostre o exemplo fictício (`references/exemplo-ficha-de-briefing.md`) para dar o nível de detalhe.
4. Combine o teste: o advogado preenche uma ficha de um caso real, anonimizado, no Projeto de peças e em conta profissional, com o prompt 1, e confere campo por campo. Aqui na conversa não entra documento de cliente. Se ele trouxer a ficha já anonimizada, revise com ele o que faltou.

Grava o modelo em branco em `escritorio/04-base/producao-de-pecas/ficha-de-briefing.md`. A ficha preenchida de cada caso fica na pasta do caso, nunca na base.

### Passo 5. Organizar o banco de modelos

A pasta "modelos_FINAL_v3" é o gargalo invisível da produção de peças. Com IA ela piora, porque a IA copia com perfeição o modelo errado.

**Montar o banco em uma semana** (com o índice `assets/indice-de-modelos.md` acompanhando):
1. **Inventário:** juntar tudo numa pasta só, de todos os lugares, e rodar a `inventariar-base`: ela lista os arquivos por área e tipo, aponta duplicados e famílias de versão e separa o que é pasta de cliente, sem mexer em nada.
2. **Escolher as cinco peças que o escritório mais faz,** pelo registro de peças ou pela controladoria do último mês. O resto entra depois.
3. **Escolher a melhor versão de cada uma:** a que o advogado assinaria hoje sem mexer. Esta escolha é H: quem sabe qual peça foi boa é quem viveu o caso. A IA pode sugerir candidatas, nunca escolher.
4. **Limpar e marcar os campos:** tirar todo dado de cliente e trocar por campos, separando o fixo do variável (prompt 5, em conta profissional).
5. **Datar a fundamentação:** toda citação do modelo vai para conferência na fonte e ganha a data. O que não der para conferir agora fica `[CONFERIR]` no próprio modelo.
6. **Escrever a ficha e dar um dono:** ficha do modelo preenchida (`assets/ficha-do-modelo.md`), dono com nome, próxima revisão marcada.
7. **Mover o resto para o arquivo:** versões antigas vão para `04-base/_arquivo/`, fora do Projeto. Modelo velho dentro da base é a IA escolhendo errado com toda a confiança.

**Pastas e nomes.** `escritorio/04-base/producao-de-pecas/modelos/<area>/modelo-<tipo>-<assunto>.md`, no padrão de nomes da `montar-base` (minúsculas, sem acento, sem versão no nome). O código do modelo, que a equipe e a IA usam na ficha e no prompt, segue `[ÁREA]_[TIPO]_[assunto]` (por exemplo, `PREV_INICIAL_concessao-incapacidade`). A versão mora no cabeçalho: muda o primeiro número quando muda a tese ou a estrutura, o segundo quando muda redação, pedido ou citação.

**Modelo vivo** tem dono, tem data, aprende com o uso (erro que a revisão pega duas vezes no mesmo modelo é corrigido no modelo) e tem fundamentação datada. O índice `modelos/INDICE.md` traz também o catálogo de peças curtas do POP-PEC-04 (um modelo por tipo de manifestação) e a lista de candidatos a modelo.

Antes de qualquer peça real virar modelo, aplique o critério de entrada da `montar-base` (seção 6: anonimização, quem aprova, peças padrão ouro).

### Passo 6. Começar o caderno de teses

Modelo diz como a peça é montada. Tese diz o que o escritório defende e em que condições. Separar os dois evita o modelo inchado, com cinco teses alternativas que ninguém sabe quando usar.

1. Pergunte: "Quais são as duas teses que o escritório mais usa?" Comece por elas.
2. Para cada uma, preencha a ficha de tese (`assets/caderno-de-teses.md`) por entrevista, uma pergunta por vez: quando usar (fatos que precisam estar no caso), quando não usar (fatos que derrubam a tese), o argumento em cinco linhas, os contra-argumentos que já apareceram e como o escritório responde.
3. **Fundamentos:** só com link da fonte oficial, data e nome de quem conferiu. O que o advogado citar de memória fica `[CONFERIR]`. Não sugira fundamento.
4. Situação de cada tese: em uso, em teste ou abandonada (com o motivo).

A IA não acrescenta tese ao caderno. Ela propõe a partir de um argumento que funcionou (passo 12 do POP-PEC-03) e quem aprova é o advogado responsável. Grava em `escritorio/04-base/producao-de-pecas/teses/caderno-de-teses.md`.

### Passo 7. Instalar o checklist de revisão e a regra de citação

Mostre as três revisões (técnica, de forma, de citações) e a regra "uma citação pode entrar na peça?":

1. A IA sugeriu uma citação.
2. Alguém abriu na fonte oficial (site do tribunal, legislação oficial, obra consultada)? Se não: fica `[CONFERIR]` e não vai para assinatura assim.
3. O texto diz o que a peça diz que ele diz (número, órgão, data e trecho conferidos)? Se não: sai, ou o argumento é reescrito por decisão do advogado.
4. Se sim: entra na tabela de citações (`assets/tabela-de-citacoes.md`) com link, data e nome.

Depois instale o checklist (`assets/checklist-revisao-peca.md`), com os seis blocos: citações e jurisprudência, fatos e documentos, pedidos, valores e prazos, tom, dados do cliente, e a revisão final. Pergunte: "Que erro a revisão de vocês mais pega hoje?" e acrescente em "Itens próprios deste escritório" só o que o advogado disser. Se a `montar-base` já gravou um checklist de peça, este o substitui com versão nova e mudanças marcadas.

Avise sobre a **revisão que vira carimbo**: o passo é A no papel, mas a pessoa aprova sem ler porque a fila está grande. As defesas são revisar em outro momento e anotar no registro de peças cada erro pego. "Checklist que nunca pega nada ou está perfeito ou não está sendo lido."

Grava em `escritorio/04-base/producao-de-pecas/checklist-revisao-peca.md`.

### Passo 8. Preparar o Projeto de peças

Monte, no chat, a lista exata do que subir. Os recursos de Projeto variam conforme o plano: conferir na configuração da conta. O passo a passo geral está em `../montar-base/references/projeto-no-claude.md`.

| Entra no Projeto de peças | Fica fora |
|---|---|
| Instruções do Projeto (`01-cultura/instrucoes-do-projeto.md`, vindas do código) | Documentos de cliente: entram na conversa de cada caso, anonimizados |
| POP de peça adaptado | A tabela que diz quem é `[CLIENTE]` |
| Modelos vigentes, só a versão em uso, com a ficha, e o `modelos/INDICE.md` | Versões antigas de modelos |
| Caderno de teses | Peça antiga com dado de cliente sem limpar |
| Checklist de revisão de peça | Fichas e tabelas de citações preenchidas de casos |
| Ficha de briefing em branco e os prompts do ciclo (`references/prompts-do-ciclo.md`) | Senhas, certificados e credenciais de qualquer sistema |

Acrescente às instruções do Projeto, com o ok do advogado: "Use só os modelos e as citações deste Projeto e da tabela de citações do caso. Qualquer outra citação vai marcada [CONFERIR]. Não calcule prazo: use a data que a controladoria conferiu. Não escolha tese nem pedido: pergunte."

**Um Projeto ou vários?** Comece com um Projeto de peças. Se o banco crescer e a IA começar a misturar modelo de uma área com outra, separe um Projeto por área. Área com acesso restrito (Família com criança, saúde, criminal) pode pedir Projeto próprio desde o começo.

### Passo 9. Combinar o indicador

Todo POP de peça sai com indicador. Ofereça o registro de peças (`assets/registro-de-pecas.md`): uma linha por peça, com tempo do gatilho ao protocolo, rodadas de revisão, erros pegos por tipo, modelo usado e prazo interno cumprido. Comece antes de mudar o fluxo, para ter o número de antes. A `medir-retorno` usa o registro para a linha de base do setor.

## 5. O que entrega e onde grava

| Entrega | Onde grava |
|---|---|
| POP do tipo de peça, com S, A, H, fluxograma e lista do que a IA consulta | `escritorio/03-pops/producao-de-pecas/pop-pec-<nn>-<tipo>.md` |
| Ficha de briefing em branco, ajustada ao escritório | `escritorio/04-base/producao-de-pecas/ficha-de-briefing.md` |
| Checklist de revisão de peça feita com IA | `escritorio/04-base/producao-de-pecas/checklist-revisao-peca.md` |
| Índice do banco de modelos, com catálogo de peças curtas e candidatos | `escritorio/04-base/producao-de-pecas/modelos/INDICE.md` |
| Modelos limpos, com ficha | `escritorio/04-base/producao-de-pecas/modelos/<area>/modelo-<tipo>-<assunto>.md` |
| Caderno de teses | `escritorio/04-base/producao-de-pecas/teses/caderno-de-teses.md` |
| Registro de peças | `escritorio/06-medicao/registro-de-pecas.md` |
| Lista do que sobe no Projeto de peças e o texto a acrescentar às instruções | Bloco no chat |

Todo documento da base leva o cabeçalho da `montar-base` (`../montar-base/assets/cabecalho-documento.md`) e uma linha no `escritorio/04-base/INDICE.md`: a ficha, o checklist e o caderno com uma linha cada; o banco de modelos com uma linha que aponta para `modelos/INDICE.md`. Se o índice geral não existir, crie-o a partir de `../montar-base/assets/indice-modelo.md`.

**No `perfil.md`:** se peças é o setor-alvo, marque `- [x] POP do setor-alvo com S, A e H` quando o POP for gravado e acrescente o estado da base entre parênteses (por exemplo, `- [ ] Base de conhecimento do setor-alvo (ficha e checklist prontos, banco 2 de 5 modelos)`). Uma linha em "Histórico" por rodada. O que ficou para depois vai para "Etapas puladas".

Mostre cada documento antes de gravar. **Sem acesso a arquivos:** entregue cada um em bloco pronto para copiar, com o nome do arquivo e o caminho.

## 6. Trilha solo e trilha equipe

**Solo:**
- Quem monta, revisa e assina é a mesma pessoa. Os passos de revisão continuam, só mudam de momento: leitura crítica e revisão final em outro horário, de preferência no dia seguinte, com o checklist na mão. "Logo depois de escrever, você lê o que quis dizer. No dia seguinte, lê o que está escrito."
- Sem revisor sênior: nas peças de maior risco, revisão em outro dia ou por revisor externo.
- A IA confere o próprio rascunho contra o checklist como segundo olhar, sem que o passo vire S por isso.
- O banco começa menor: as três peças mais frequentes, com o titular como dono de todos os modelos. No fim de cada semana, 15 minutos para capturar o trecho que funcionou.
- Se houver estagiário ou secretária, essa pessoa cuida da pasta, dos nomes e do índice; o titular aprova o conteúdo.

**Equipe:**
- Cada passo com nome: quem monta, quem calcula, quem pesquisa, quem revisa, quem assina, quem protocola. "Se o mesmo nome aparece em todos os passos, ali está o gargalo." Proponha repassar os passos A para quem monta, deixando o titular com tese, revisão final e assinatura.
- Um dono por modelo e um dono do caderno de teses (o advogado responsável pela área, ou o sócio na boutique).
- Regra de entrada no banco: qualquer pessoa sugere candidato; o dono do modelo aprova.
- Pasta e Projeto restritos para Família com criança, saúde e criminal.

## 7. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Pedir a peça antes de decidir a tese | A IA escolhe a estratégia e o advogado assina o que não escolheu | Tese na etapa 4, campo 6 da ficha assinado antes da minuta |
| Citação sem fonte | Julgado inexistente ou trecho inventado na peça assinada | Tabela de citações, regra "uma citação pode entrar?", `[CONFERIR]` até abrir a fonte |
| Minuta direto dos PDFs | Fato plausível que ninguém disse | Ficha de briefing com fonte de cada fato; `[SÓ RELATO]` só entra por decisão |
| IA calculando prazo | Prazo perdido com cara de certo | Prazo sempre da controladoria, conferido |
| Modelo velho no Projeto | A IA copia com perfeição o modelo errado | Banco vivo, índice com versão vigente, `_arquivo/` fora do Projeto |
| Modelo com cinco teses dentro | Ninguém sabe quando usar qual | Caderno de teses separado do modelo |
| Peça curta inteira com a IA | Frase que concorda com o laudo que se queria impugnar | POP-PEC-04 com posição decidida e leitura integral |
| Revisão-carimbo | Checklist marcado sem ler | Revisão em outro momento e erros anotados no registro |
| Skill virando redatora | Peça de caso concreto sem POP nem base | Escopo: organiza o setor, não redige a peça |

## 8. Próximo passo

- **Fluxograma do POP:** `desenhar-fluxograma`, partindo do fluxograma da referência ou do ciclo em `references/ciclo-da-peca.md`.
- **Testar o POP:** `testar-pop`, com 3 a 5 casos reais anonimizados (típico, com exceção, que deve parar, com dado sensível) antes de publicar.
- **Completar a base:** `montar-base`, para premissas de cálculo, matriz de prova, checklist de requisitos do recurso, critérios de enquadramento de lote e os casos de teste.
- **Virar habilidade:** `pop-para-skill`, quando o POP estiver estável depois de uma a duas semanas rodando à mão no nível 3.
- Antes de automatizar, `auditar-riscos` no POP. Para manter os POPs de peça vivos na equipe, `gerir-pops`.

## Referências desta skill

- `references/ciclo-da-peca.md`: as onze etapas, os grupos, a ordem, o fluxograma do ciclo, onde o fluxo muda e o ciclo em raias. Leia no passo 2.
- `references/pop-pec-01-peticao-inicial.md` a `references/pop-pec-05-cumprimento-de-sentenca.md`: os cinco POPs de referência nos 12 campos, com exemplos por área, trilha solo e fluxograma. Abra só o escolhido no passo 3.
- `references/exemplo-ficha-de-briefing.md`: ficha preenchida de um caso fictício. Use no passo 4.
- `references/prompts-do-ciclo.md`: os cinco prompts do ciclo (briefing, pesquisa, minuta, revisão técnica, peça boa em modelo). Sobem no Projeto no passo 8.
- `assets/ficha-de-briefing.md`, `assets/checklist-revisao-peca.md`, `assets/ficha-do-modelo.md`, `assets/indice-de-modelos.md`, `assets/caderno-de-teses.md`, `assets/tabela-de-citacoes.md`, `assets/registro-de-pecas.md`: modelos prontos para preencher e gravar.
