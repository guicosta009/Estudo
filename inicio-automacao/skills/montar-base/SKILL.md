---
name: montar-base
description: >
  Monta a base de conhecimento do setor-alvo, a memória que a IA consulta: lista o que os POPs
  citam no campo Entradas, faz o inventário do que já existe, separa o que usar, atualizar,
  descartar ou criar, organiza tudo em escritorio/04-base com nomes claros, versão, dono e
  índice, separa os casos de teste anonimizados e orienta a montagem do Projeto no Claude.
  Use quando o advogado disser "montar a base de conhecimento", "organizar meus modelos", "o
  que a IA precisa consultar", "minha pasta de modelos é uma bagunça", "separar casos de
  teste", "o que eu coloco no Projeto do Claude", "criar o checklist de documentos", "escrever
  os critérios de relevância", ou quando a desenhar-automacao apontar documento faltando.
  Não use para escrever o POP (use escrever-pop) nem para desenhar a automação (use
  desenhar-automacao).
---

# Montar a base

> Junta, limpa e organiza o que a IA precisa consultar para seguir o POP do setor-alvo: modelos, checklists, critérios, tabelas e respostas aprovadas. Sem base, a IA preenche o vazio com o que acha.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, níveis, setores e a equação da automação: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`. Estrutura da pasta: `../../docs/pasta-do-escritorio.md`.

## 1. Quando usar

**Use quando:**
- O POP do setor-alvo está escrito com S, A e H e o próximo passo é dar à IA o material que ele cita.
- O advogado quer organizar modelos e checklists espalhados ("cada um tem os seus", a pasta "modelos_FINAL_v3" na área de trabalho de uma pessoa só).
- A `desenhar-automacao` ou a `pop-para-skill` encontrou uma instrução que aponta para um documento que não existe.
- É hora de separar os casos de teste anonimizados de uma automação.
- Um erro repetido, uma mudança de POP ou a revisão trimestral pediu para atualizar a base.

**Não use quando:**
- Ainda não existe POP do setor-alvo. A base nasce do campo "Entradas" do POP: ofereça o `escrever-pop` (veja o portão abaixo).
- O pedido é escrever a instrução de cada passo da automação: use `desenhar-automacao`.
- O pedido é pesquisar jurisprudência ou escrever uma peça. Esta skill organiza o material do escritório, ela não produz tese nova.

## 2. Antes de começar

1. **Leia o perfil.** `escritorio/perfil.md` diz a trilha, as áreas, o modelo de negócio, o tipo de conta de IA e o setor-alvo. Leia também `escritorio/01-cultura/codigo-do-escritorio.md` e `escritorio/01-cultura/regra-de-uso-de-ia.md`, se existirem. Sem perfil, faça o modo rápido das regras transversais (três perguntas, uma por vez) e grave um `perfil.md` mínimo.
2. **Portão: precisa existir o POP do setor-alvo,** em `escritorio/03-pops/<setor>/`, com o campo "Entradas" preenchido.
   - **Se faltar:** explique em duas frases. "A base é feita do que o POP diz que a IA vai consultar. Sem o POP, a gente organiza documentos que talvez ninguém use e esquece o critério que o fluxo precisa." Ofereça o `escrever-pop`.
   - **Se o advogado quiser seguir mesmo assim:** rode no **modo inventário**. Use a lista de artefatos típicos do setor-alvo em `references/artefatos-por-setor.md` no lugar das Entradas do POP, marque cada item como `[A CONFIRMAR]` (com a nota "conferir no POP") e registre no `perfil.md`, em "Etapas puladas": "Base montada antes do POP do setor-alvo (data)".
3. **Sem setor-alvo no perfil:** pergunte qual setor o escritório quer automatizar primeiro. Se ninguém souber, ofereça o `diagnostico` (rápido) ou o `mapear-setores` (completo). Não monte a base do escritório inteiro.
4. **Conta de IA.** Os documentos da base descrevem o trabalho e não levam dado de cliente, mas os casos de teste nascem de casos reais. Se o perfil diz conta pessoal gratuita, avise: os casos de teste só podem usar dado fictício até a conta profissional estar conferida.

## 3. O princípio: a base nasce dos POPs

**A base é feita do que os POPs citam no campo "Entradas", mais o que o código do escritório exige.** Nada além disso entra na primeira rodada.

- **Entradas do POP:** "critérios de relevância por área", "modelos por categoria", "FAQ", "roteiro de triagem por área". Cada item citado vira um documento da base, com nome, dono e data.
- **Passos que pressupõem um documento:** "classificar pelos critérios escritos", "a partir de modelo aprovado", "pela matriz de distribuição". Se o passo diz que existe uma regra escrita, a regra precisa estar na base.
- **O que o código exige:** quando o código do escritório fala em "critérios de aceite", "política de desconto" ou "frases que nunca usamos" e remete a um documento separado, esse documento também entra.
- **Começa pelo setor-alvo.** Um setor bem servido antes de dois pela metade. A base do escritório inteiro, de uma vez, costuma virar a mesma pasta "modelos_FINAL_v3", só que maior.

### Tipo de base por modelo de negócio

O modelo de negócio (campo `modelo_de_negocio` do perfil) muda o que pesa mais na base. Use como orientação. Quem decide é o POP do setor-alvo.

| Modelo | O que pesa mais na base | O que costuma servir de caso de teste |
|---|---|---|
| Contencioso de volume | Modelos com campos variáveis marcados e regras de classificação (de publicação, de enquadramento de lote) | Cerca de 20 publicações de um mesmo tipo, anonimizadas |
| Boutique | Teses, critérios e peças padrão ouro; o roteiro de como o sócio pensa o caso | 3 a 5 peças padrão ouro e os casos que deram origem a elas |
| Digital de nicho | Roteiros de triagem, perguntas de qualificação, respostas aprovadas, lista de documentos | Conversas reais de primeiro contato, anonimizadas |
| Advogado solo | Respostas às perguntas frequentes, lista de documentos e roteiro de consulta por tipo de caso, modelos de peça mais usados | As 10 perguntas mais frequentes com as respostas atuais |
| Consultivo ou partido | Checklist de revisão de contrato, posições da casa, respostas aprovadas **separadas por cliente** | As demandas de um mês de um cliente, anonimizadas |
| Full service | Os mesmos documentos com variação por área, regra de distribuição escrita | Uma semana de publicações e o POP com as variações por área |
| Correspondência | Checklist do que a solicitação precisa ter, modelo de relatório pós-audiência | 3 solicitações recebidas e os relatórios entregues |
| Híbrido | A base do fluxo de receita que mais se repete | O mesmo do modelo daquele fluxo |

## 4. Fluxo

### Passo 1. Listar o que o POP cita
Leia o POP do setor-alvo inteiro. Monte a lista de tudo o que ele cita no campo "Entradas" e de tudo o que os passos pressupõem. Leia o código e acrescente o que ele remete a documento separado.

| Documento citado | Onde aparece (POP e passo) | Tipo | Precisa existir para |
|---|---|---|---|
| Critérios de relevância de movimentação | pop-atualizacao-de-andamento, Entradas e passo 2 | Critério | Passo S rodar no nível 3 |

Tipos possíveis: modelo, checklist, critério, tabela, roteiro, respostas aprovadas (FAQ), política. Separe à parte o que é **dado do caso** (CNIS, holerite, ficha do cliente): isso fica na pasta do cliente, nunca na base. Mostre a lista e peça ok.

### Passo 2. Fazer o inventário do que já existe
Se o escritório tem uma pasta de modelos e documentos de trabalho (no computador, no Drive ou no OneDrive), ofereça antes a `inventariar-base`: ela lê a pasta real sem mexer em nada, acha duplicados, famílias de versão e alertas de dado de cliente, e já devolve a triagem proposta e o plano de reorganização. Com o inventário pronto, as perguntas abaixo ficam só para o que a pasta não mostra (quem usa, o que está na cabeça de alguém).

Para cada documento da lista, pergunte, um por vez:
- "Onde fica hoje o [documento]? Pode ser pasta, drive, sistema, caderno ou a cabeça de alguém."
- "Quem usa e quem mexe nele?"
- "Quantas versões existem? Tem uma 'final', uma 'final 2', uma no computador de outra pessoa?"
- "Quando foi a última vez que alguém atualizou?"
- "Tem nome, CPF, número de processo ou dado de saúde de algum cliente dentro?"

Se a resposta for "está na minha cabeça", anote como "não escrito" e siga. Se o advogado colar um documento, leia e, se houver dado de cliente, avise, não repita o dado e mostre a versão anonimizada.

| Documento | Onde está | Quem tem | Versões | Última atualização | Dado de cliente? |
|---|---|---|---|---|---|

### Passo 3. Triagem: usar, atualizar, descartar ou criar

| Decisão | Quando | O que fazer |
|---|---|---|
| **Usar** | Existe, uma versão só, em uso, sem dado de cliente | Renomear no padrão, pôr o cabeçalho, registrar no índice |
| **Atualizar** | Existe mas está velho, tem várias versões ou tem dado de cliente que dá para tirar | Juntar as versões numa só (a equipe escolhe a vigente), anonimizar, revisar com o dono |
| **Descartar** | Ninguém usa, é duplicado ou não serve a nenhum POP | Sai da base. Se tiver dado de cliente, volta para a pasta do caso. Descarte de original só com autorização do advogado |
| **Criar** | O POP cita e não existe, ou existe só na cabeça de alguém | Escrever a partir do esqueleto (passo 5) |

Mostre a triagem e peça ok antes de mexer em qualquer arquivo.

### Passo 4. Organizar a pasta
Monte `escritorio/04-base/` conforme a seção 5: uma pasta por setor (e por área dentro do setor, quando o conteúdo muda de uma área para outra), nomes no padrão, cabeçalho em cada documento e o `INDICE.md`. Grave só depois do ok.

### Passo 5. Criar o que falta a partir dos esqueletos
Os esqueletos dos artefatos mais citados estão em `assets/esqueletos/` (lista na seção 5). Para cada documento a criar:
1. Abra o esqueleto e mostre a estrutura.
2. Entreviste o advogado (ou o dono do documento), uma pergunta por vez, para preencher. Primeiro o retrato: como o escritório decide isso hoje, mesmo que de cabeça. Peça um exemplo concreto ("qual foi a última movimentação que você achou importante avisar?").
3. O que o advogado não souber ou não decidir fica `[A DEFINIR]`. Norma, prazo, valor e regra técnica ficam `[CONFERIR]`.
4. Os itens de exemplo do esqueleto só ficam se o advogado confirmar um por um. Não acrescente regra que ele não disse.

### Passo 6. Aplicar o critério de entrada
Antes de cada documento ganhar a situação "em uso", confira os itens da seção 6 (o que pode entrar, quem aprova, anonimização, peças padrão ouro). O que não passar fica como "rascunho" no índice.

### Passo 7. Separar os casos de teste
Para cada automação que o escritório pretende desenhar, separe de 3 a 5 casos reais anonimizados, com o gabarito do que a equipe entregaria. Veja a seção 7.

### Passo 8. Montar o Projeto no Claude
Oriente a montagem do Projeto com as instruções vindas do código e os documentos da base do setor-alvo. Veja a seção 8 e, para o passo a passo completo, `references/projeto-no-claude.md`.

### Passo 9. Combinar a manutenção
Defina com o advogado quando cada documento é revisto e o que acontece com as versões antigas (seção 9). Anote no `INDICE.md`.

## 5. Organização: pastas, nomes, cabeçalho e índice

**Estrutura sugerida** (só cria a pasta do setor-alvo e o que ele usa):

```
escritorio/04-base/
  INDICE.md
  comum/                              ← vale para todos os setores (padrão de nomes, FAQ geral)
  relacionamento-com-o-cliente/
    criterios-relevancia-movimentacao-previdenciario.md
    modelos-mensagem-por-categoria.md
  producao-de-pecas/
    previdenciario/                   ← área dentro do setor, quando o conteúdo muda por área
      modelo-peticao-inicial-aposentadoria.md
      checklist-revisao-peca.md
    familia/                          ← restrita: veja controle de acesso na trilha equipe
  casos-de-teste/
    <nome-da-automacao>/
      caso-01.md
  _arquivo/                           ← versões substituídas, fora do Projeto
```

Os nomes das pastas de setor seguem os 10 setores do glossário, em minúsculas e com hífen.

**Convenção de nomes:** `<tipo>-<assunto>[-<area>].md`, em minúsculas, sem acento, palavras separadas por hífen. Exemplos: `checklist-documentos-auxilio-doenca.md`, `modelo-mensagem-pericia-marcada.md`, `roteiro-triagem-trabalhista.md`.
- **Sem versão no nome do arquivo.** Nada de "final", "v3", "novo", "revisado". A versão mora no cabeçalho. Isso acaba com a "modelos_FINAL_v3".
- **Um documento, um assunto.** Se o nome precisa de "e" para caber, provavelmente são dois documentos.
- Modelos de peça podem continuar no formato que o escritório usa (.docx, por exemplo). O nome segue o padrão e o cabeçalho vai no próprio arquivo ou numa ficha `.md` com o mesmo nome.

**Cabeçalho de cada documento** (modelo em `assets/cabecalho-documento.md`):

```
# [NOME DO DOCUMENTO]
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho | em uso | em revisão
Setor: [SETOR] · Área: [ÁREA OU "todas"] · Usado por: [POP E PASSO] · Acesso: geral | restrito
```

**Índice** (`escritorio/04-base/INDICE.md`, modelo em `assets/indice-modelo.md`): uma linha por documento, com pasta, versão, data, dono, POPs que usam, situação e acesso. O índice é o que a IA e a equipe consultam para saber qual é a versão vigente. Documento fora do índice é documento que não existe para a IA.

**Esqueletos disponíveis** em `assets/esqueletos/`:

| Esqueleto | Setor onde mais aparece |
|---|---|
| `criterios-relevancia-movimentacao.md` | Relacionamento com o cliente |
| `modelos-mensagem-por-categoria.md` | Relacionamento com o cliente |
| `faq-clientes.md` | Relacionamento com o cliente, Atendimento e triagem |
| `roteiro-triagem-por-area.md` | Atendimento e triagem |
| `checklist-documentos-por-tipo-de-caso.md` | Atendimento e triagem, Administrativo |
| `checklist-revisao-peca.md` | Produção de peças |
| `tabela-interna-honorarios.md` | Comercial |
| `regua-de-cobranca.md` | Financeiro e cobrança |
| `padrao-nomes-e-pastas.md` | Administrativo (vai para `comum/`) |
| `checklist-etico-publicidade.md` | Marketing e conteúdo |

Para os outros artefatos que os POPs citam (tabela de prazos, calendário de feriados, matriz de distribuição, política de renegociação, checklist por tipo de audiência, política de dados e descarte, termo de confidencialidade, matriz de prova, premissas de cálculo, critérios de enquadramento de lote, critérios de aceite), veja a estrutura sugerida em `references/artefatos-por-setor.md` e monte o documento na mesma lógica dos esqueletos.

## 6. Critério de entrada

**O que pode entrar:**
- Documento que algum POP cita ou que o código exige.
- Escrito, com uma versão só, com dono e data.
- Sem dado que identifique cliente. Modelos usam `[CLIENTE]`, `[PROCESSO]`, `[DOC]` e as outras trocas da tabela padrão das regras transversais.
- Norma citada pelo nome e jurisprudência só depois de aberta na fonte oficial, com a marca `[CONFERIR]` para quem for reutilizar.

**O que nunca entra:** dado de cliente identificável; laudo completo, dado de criança ou adolescente e processo em segredo de justiça (nem anonimizados, sem autorização expressa do responsável); senha e credencial de qualquer sistema; conversa real de cliente sem anonimização; jurisprudência que ninguém abriu na fonte; versão antiga "para garantir".

**Quem aprova:**
- Documento com conteúdo jurídico (tese, modelo de peça, resposta com orientação, critério de aceite): o advogado responsável pela área.
- Documento operacional (padrão de nomes, régua, roteiro de triagem): o dono do setor.
- Solo: o titular aprova, de preferência em outro momento do dia, e não logo depois de escrever.
- A IA propõe, nunca aprova. Mudanças em documento já em uso vêm marcadas com `[NOVO]` ou `[ALTERADO]`.

**Anonimização obrigatória.** Antes de qualquer documento real virar modelo: trocar nomes, documentos, número de processo e de benefício, endereço e contato pela tabela padrão; tirar datas e valores que permitam identificar o caso, quando não forem necessários ao modelo; conferir cabeçalho, rodapé e propriedades do arquivo, que costumam guardar o nome do cliente. Quem anonimiza é quem inclui. Quem aprova confere.

**Peças padrão ouro.** Peça que o escritório usaria de novo como referência de estrutura, argumentação e estilo. Critérios para entrar:
1. Escolhida pelo advogado responsável (na boutique, pelo sócio). A IA pode sugerir candidatas, nunca escolher.
2. Anonimizada por inteiro, inclusive nos documentos citados.
3. Acompanhada de uma nota curta: por que é padrão ouro, para que tipo de caso serve e o que não reaproveitar.
4. Jurisprudência e normas marcadas `[CONFERIR]`, com a data em que foram conferidas. O que valia na peça pode ter mudado.
5. O resultado do processo não é o critério. A peça entra pela qualidade do trabalho.

## 7. Casos de teste

Cada automação é testada com **3 a 5 casos reais anonimizados**, cada um com o **gabarito**: o que a equipe entregaria naquele caso. É com eles que a `desenhar-automacao` compara a saída da IA antes de subir de nível.

**Como escolher os casos** (para a mesma automação):
1. **Típico:** o caso que mais se repete.
2. **Com exceção:** um caso que cai numa exceção do POP.
3. **Que deve parar:** um caso que toca a linha vermelha (notícia muito ruim, cliente vulnerável, decisão de mérito). O acerto é a IA parar e chamar uma pessoa.
4. **Com dado sensível:** saúde, por exemplo. O acerto é tratar o dado como o POP manda.
5. **Incompleto (opcional):** falta informação. O acerto é pedir o que falta em vez de inventar.

**Como montar cada caso** (modelo em `assets/caso-de-teste-modelo.md`), em `escritorio/04-base/casos-de-teste/<nome-da-automacao>/caso-NN.md`:
- Entrada anonimizada, exatamente como a IA vai recebê-la.
- Gabarito: o que a equipe entregaria, escrito por quem executa o processo hoje.
- O que a IA não pode fazer neste caso.
- Critério de acerto (o que precisa estar igual ao gabarito e o que pode variar).

**Cuidados:** casos de teste vêm de casos reais, por isso a anonimização é a mais rigorosa da base. Laudo completo, dado de criança e segredo de justiça não viram caso de teste. Se a conta de IA for pessoal gratuita, monte os casos com dado fictício parecido com o real.

## 8. O Projeto no Claude

Um Projeto no Claude guarda instruções fixas e documentos que valem para toda conversa dentro dele. É o nível 2 de inserção da IA. Os recursos variam conforme o plano e a versão: conferir na configuração da conta.

- **Instruções do Projeto:** o texto de `escritorio/01-cultura/instrucoes-do-projeto.md`, que a `codigo-do-escritorio` gerou a partir do código. Se não existir, ofereça a `codigo-do-escritorio` antes.
- **Conhecimento do Projeto:** os documentos da base do setor-alvo com situação "em uso", na versão vigente do índice, mais o próprio `INDICE.md` e o POP do setor-alvo.
- **O que não colocar:** versões antigas, documentos em rascunho, pastas inteiras despejadas sem triagem, documentos de outro setor que o POP não cita, casos de teste (ficam fora para não contaminar o teste), dado de cliente, senhas.
- **Quando separar em mais de um Projeto:** consultivo com base por cliente (um Projeto por cliente, para nunca misturar informação), full service com bases muito diferentes por área, ou quando o volume de documentos começar a atrapalhar a consulta.
- **Sem Projeto, com a pasta aberta** (Claude Code ou outro ambiente que lê a pasta de trabalho): o `escritorio/CLAUDE.md` já manda o Claude abrir o POP e consultar só o que ele cita em `04-base/`. O índice cumpre o papel do conhecimento do Projeto.

Passo a passo, teste de consulta e manutenção do Projeto: `references/projeto-no-claude.md`.

## 9. Manutenção

A base envelhece. Três gatilhos fazem um documento ser revisto:
1. **Erro repetido.** O mesmo ajuste apareceu duas vezes no registro de uso, ou um quase incidente apontou um critério faltando: o documento que a IA consultou é revisto na mesma semana.
2. **O POP mudou.** Toda nova versão de POP faz conferir os documentos que ele cita: os que ele deixou de citar saem, os novos entram.
3. **Revisão trimestral** (`revisao-periodica`): cada documento do índice com data de revisão mais antiga que um trimestre é aberto pelo dono, que confirma, atualiza ou descarta.

**Descarte de versões:** quando um documento muda, a versão nova substitui a antiga no mesmo arquivo, com a versão e a data atualizadas no cabeçalho. A antiga vai para `04-base/_arquivo/` com a data no nome (`modelo-mensagem-pericia-marcada_ate-AAAA-MM-DD.md`) e sai do Projeto no mesmo dia. Uma versão viva por documento.

## 10. O que entrega e onde grava

| Entrega | Onde grava |
|---|---|
| Lista do que o POP cita e inventário com a triagem | No topo do `escritorio/04-base/INDICE.md`, seção "Levantamento" |
| Documentos da base, com cabeçalho | `escritorio/04-base/<setor>/` ou `<setor>/<area>/`; os comuns em `comum/` |
| Índice | `escritorio/04-base/INDICE.md` |
| Casos de teste com gabarito | `escritorio/04-base/casos-de-teste/<nome-da-automacao>/caso-NN.md` |
| Roteiro de montagem do Projeto | Bloco no chat, com a lista exata do que subir |
| Progresso | Marcar "Base de conhecimento do setor-alvo" no `perfil.md` |

Mostre cada documento antes de gravar. Sem acesso a arquivos, entregue cada documento em bloco pronto para copiar, com o nome do arquivo e o caminho.

## 11. Trilha solo e trilha equipe

- **Solo:** o titular organiza a base e é o dono de todas as pastas. O que mais ajuda é o hábito: **no fim de cada semana, 15 minutos para capturar o que funcionou** (a resposta que o cliente entendeu de primeira, o parágrafo que vai servir de novo) e incluir na base, anonimizado. Se houver estagiário ou secretária, essa pessoa pode cuidar dos nomes e do índice, e o titular aprova o conteúdo. A aprovação acontece em outro momento do dia, nunca logo depois de escrever.
- **Equipe:** **um dono por pasta** da base, escrito no índice. **Regra de entrada** escrita: quem pode incluir (qualquer pessoa sugere), quem aprova (dono da pasta e, se houver conteúdo jurídico, o advogado da área). **Controle de acesso** para pastas restritas (Família com criança, saúde, criminal): só quem trabalha naquele caso, e o Projeto daquela área também restrito. Se o mesmo nome for dono de todas as pastas, ali está o gargalo.

## 12. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Base do escritório inteiro de uma vez | Meses organizando, nada sendo usado | Começa pelo setor-alvo e pelo que o POP cita |
| Despejar a pasta toda no Projeto | A IA consulta versão velha e modelo de outra pessoa | Triagem antes, índice com versão vigente |
| "modelos_FINAL_v3" | Ninguém sabe qual é a certa | Versão no cabeçalho, uma versão viva, arquivo à parte |
| Modelo com dado de cliente | Sigilo exposto em toda conversa | Critério de entrada com anonimização conferida |
| Critério que só existe na cabeça | A IA chuta o que é relevante | Esqueleto preenchido por entrevista, lacunas em `[A DEFINIR]` |
| Testar com o caso que deu certo | Automação aprovada sem ver exceção | 3 a 5 casos, incluindo o que deve parar |
| Base sem dono | Envelhece em silêncio | Dono e data em cada documento e três gatilhos de revisão |

## 13. Próximo passo

- Base do setor-alvo pronta e casos de teste separados: siga para a `desenhar-automacao`, que começa pelo checklist de prontidão.
- Faltou o POP ou ele mudou durante o levantamento: volte ao `escrever-pop`.
- Faltou a linha de base de horas do setor: rode a `medir-retorno` antes de mexer no fluxo, para ter o "antes" medido.
