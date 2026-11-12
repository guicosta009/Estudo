---
name: desenhar-fluxograma
description: >
  Desenha o fluxograma de um processo do escritório, antes ou depois do POP, a partir do
  retrato de como funciona hoje ou do POP pronto, em três formatos: Mermaid (flowchart TD),
  texto numerado com "vá para" e versão em raias (IA, Equipe, Advogado), com sigla S, A ou
  H em cada ação e a revisão de cada passo A marcada. Confere se texto e desenho batem e
  devolve as decisões e exceções que o desenho revelou. Traz 10 fluxogramas de referência,
  um por setor. Use quando o advogado disser "desenhar o fluxograma", "fazer o fluxograma
  do processo", "desenhar em raias", "quem faz o quê no setor", "gerar o Mermaid",
  "conferir se o fluxograma bate com o POP", "onde esse processo trava", "atualizar o
  desenho do POP". Não use para escrever os 12 campos do POP (use escrever-pop) nem para
  testar o POP com casos reais (use testar-pop).
---

# Desenhar o fluxograma

> Mostra por onde o trabalho anda, onde ele se divide, o que acontece quando a resposta é "não" e em quais caixas a IA entra sem que ninguém perca o controle. O POP explica como fazer cada passo; o fluxograma mostra o caminho inteiro numa olhada.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha e anatomia do POP: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`. Esta skill aprofunda a seção 6 do `escrever-pop` (`../escrever-pop/SKILL.md`) e segue as mesmas convenções de desenho.

Pergunte a três pessoas do escritório como uma petição sai daí de dentro e você ouve três versões: uma começa na intimação, outra no e-mail do cliente, a terceira na pasta "modelos_FINAL_v3". Cada uma enxerga o pedaço que passa pelas próprias mãos. O fluxograma é o primeiro lugar em que o processo aparece inteiro, do gatilho à entrega.

## 1. Quando usar

**Use quando:**
- Existe o retrato de um processo (o passo a passo de hoje) e o advogado quer enxergar decisões, exceções e onde a IA entra **antes** de escrever o POP.
- Existe o POP e falta o fluxograma, ou o desenho ficou velho depois de uma revisão do POP.
- O advogado quer a versão em raias para ver quem carrega o setor e onde o trabalho troca de mãos.
- É preciso conferir se o fluxograma e o texto do POP dizem a mesma coisa.
- Outra skill pediu o desenho (o `escrever-pop` no fechamento, o `testar-pop` ou o `gerir-pops` numa revisão de versão).

**Não use quando:**
- O pedido é escrever o POP inteiro nos 12 campos: use `escrever-pop` (ele já sai com um fluxograma simples; esta skill entra quando o desenho precisa de mais cuidado).
- Só falta marcar S, A ou H numa lista: use `classificar-sah`.
- O pedido é rodar o POP em casos reais e ver onde quebra: use `testar-pop`.
- O pedido é revisar riscos, sigilo e linha vermelha antes de automatizar: use `auditar-riscos`.

## 2. Antes de começar

1. **Leia o perfil.** Abra `escritorio/perfil.md` (trilha, porte, áreas, conta de IA, setor-alvo) e, se existirem, `escritorio/01-cultura/codigo-do-escritorio.md` e `escritorio/01-cultura/regra-de-uso-de-ia.md`. Sem perfil, ofereça `/inicio-automacao:comecar` ou faça o modo rápido das regras transversais (três perguntas, uma por vez).
2. **Descubra o estágio,** porque ele trava siglas. Se não estiver no perfil, pergunte: "A IA roda em conta profissional ou de equipe, e existe regra de uso de IA escrita?" Sem as duas, todo passo com dado de cliente fica no mínimo A.
3. **Portão.** Precisa haver um processo com algum texto: o retrato, o POP ou, no mínimo, a disposição do advogado para ser entrevistado (entrada C). Sem setor definido, pergunte qual setor e processo ele quer desenhar e avise que o ideal é sair do `mapear-setores`.
4. **Veja o que já existe** em `escritorio/03-pops/<setor>/`:
   - um POP do processo (`pop-<sigla>-<nn>-<processo>.md`, ou `pop-<processo>.md` nos POPs gravados antes da numeração);
   - um fluxograma avulso (`fluxograma-<processo>.md`).
   Se houver POP, esta rodada desenha ou redesenha a seção de fluxograma dele. Se houver só o fluxograma avulso, esta rodada é uma revisão dele: suba a versão.
5. **Escolha a entrada.** Pergunte: "Para esse processo, o que você tem? (a) O passo a passo de como é hoje, escrito ou em áudio. (b) O POP pronto. (c) Nada escrito: prefiro que você me entreviste."

Siglas de setor, usadas no nome do POP: ATD atendimento-e-triagem · COM comercial · PEC producao-de-pecas · PRZ prazos-e-controladoria · AUD audiencias-e-diligencias · FIN financeiro-e-cobranca · REL relacionamento-com-o-cliente · MKT marketing-e-conteudo · EQP gestao-de-equipe · ADM administrativo.

## 3. Fluxo

### Passo 1. Juntar o texto de entrada

- **Entrada A (retrato):** peça o passo a passo do jeito que acontece hoje, com os atalhos e as gambiarras. Aceite texto corrido ou áudio transcrito. Se o retrato for raso, pergunte "e depois?" até chegar ao fim.
- **Entrada B (POP):** leia o POP inteiro. O desenho sai do campo 5 (passos), do 2 (gatilho), do 7 (exceções) e do 8 (saída). As siglas do POP valem: não troque nenhuma no desenho. Se discordar de uma, diga fora do desenho.
- **Entrada C (entrevista):** no máximo 15 perguntas, uma por vez. Comece pelas pontas: "O que faz esse processo começar? Pense na última vez." e "Quando você sabe que terminou, e quem recebe o resultado?". Depois vá passo a passo com "e depois?", "quem faz?" e "e se não der certo?". Resposta genérica vira pedido do último exemplo real, sem dado de cliente ("e na terça, como foi?"). Anote cada decisão e cada exceção que aparecer. No fim, mostre o passo a passo numerado, do jeito que ele descreveu, e peça ok: esse é o retrato.

Em qualquer entrada: dado de cliente na conversa (nome, número de processo, dado de saúde), avise, não repita e siga com a versão anonimizada. O fluxograma descreve o processo, nunca um caso.

### Passo 2. Fechar as duas pontas

Escreva o gatilho (o acontecimento que inicia o processo) e a entrega (o que sai e para quem), uma frase cada. Se aparecerem dois gatilhos muito diferentes, são dois desenhos. Se o desenho começa na intimação e termina na cobrança de honorários, são dois processos: corte onde o gatilho muda e ligue os dois pelo nome.

### Passo 3. Transformar cada linha em ação

Uma caixa por linha, com verbo no infinitivo e um responsável. Junte linhas que são o mesmo passo. Quebre as que fazem duas coisas ("ler e responder"). Caixa com dois donos ("advogado e estagiário revisam") vira duas caixas. Teste a altura de cada caixa: dá para dizer quem faz, o que entrega e se ficou certo? Se sim, a altura está boa.

### Passo 4. Caçar as decisões

Procure no texto as palavras "se", "depende", "quando", "às vezes" e "a não ser que". Cada uma vira um losango com a pergunta escrita. "Depende" é a palavra mais cara do escritório: no desenho ela mostra quem decide e com base em quê.

### Passo 5. Perguntar "e se não?" em cada losango

Para cada decisão, pergunte ao advogado o caminho do "não" e desenhe a resposta. Cada saída termina num fim, numa volta para um passo anterior ou no nome de outro processo. Seta solta é exceção que ainda vai chegar até você às 19h. Exceção sem dono vira `[A DEFINIR]`. Pergunte também onde o processo fica parado (cliente que não manda documento, assinatura pendente, retorno do tribunal) e quanto tempo a espera dura.

### Passo 6. Mostrar o desenho de hoje (entradas A e C)

Diga: "Este é o desenho de como é hoje, sem a IA. Ainda não melhorei nada." Mostre a versão em texto numerado (seção 5), com o responsável de cada caixa e sem siglas. Peça ok. Retrato antes de melhoria: o redesenho só começa depois que o advogado reconhece o próprio processo no papel. Na entrada B, pule este passo: o POP já é o redesenho.

### Passo 7. Pôr a IA dentro

Só depois do ok. Para cada ação:
1. **Sigla** pela árvore do `classificar-sah` (`../classificar-sah/SKILL.md`), a primeira resposta encerra: toca a linha vermelha? H. Exige decisão estratégica, julgamento ético ou conversa delicada? H. A regra não cabe num papel? A. O erro seria caro ou percebido tarde? A. O resultado sai do escritório ou mexe com dado sensível sem conferência depois? A. Se não, S.
2. **Trava por estágio:** sem conta profissional ou sem regra de uso escrita, nenhum passo com dado de cliente fica S. Na dúvida entre duas siglas, a mais humana.
3. **Responsável:** passo S é executado pela IA e tem uma pessoa que confere por amostra. Passo A tem a pessoa dona do passo, e a IA prepara. Passo H fica com a pessoa.
4. **Revisão com objeto:** em todo passo A, escreva o que se confere ("datas e valores", "citações na fonte", "tom da mensagem", "caso certo, data certa, nenhuma promessa de resultado"). Revisão sem objeto vira carimbo.
5. **O que muda no desenho:** passo que só existia por falta de outro jeito pode sumir ou se fundir; podem faltar a conferência do que a IA fez, o registro e o tratamento de exceção. Tudo o que for acréscimo seu entra como sugestão marcada `[NOVO]`, e só fica no desenho depois do ok. Nunca desenhe passo que o advogado não disse que existe: se algo parecer faltar, pergunte.

### Passo 8. Montar as três versões

Monte, nesta ordem, as versões descritas na seção 5: Mermaid, texto numerado e raias. Depois das três, entregue o caminho principal em uma linha, do início ao fim, e a contagem: caixas de ação e de decisão, quantas S, A e H, e quantas caixas há em cada raia.

### Passo 9. Conferir texto e desenho

Rode a conferência da seção 6 e devolva duas listas: as divergências entre texto e desenho, e as decisões e exceções que o desenho revelou e o texto ainda não cobria. Pergunte, uma por vez, o que fazer com cada item que muda o processo.

### Passo 10. Validar com quem executa

Peça ao advogado que percorra o desenho com quem faz o trabalho, usando um caso real recente, anonimizado. A pergunta que destrava é "e na terça, como foi?". Ajuste o que não bater com a prática. No solo, faça o percurso em outro dia, com um caso diferente do que foi usado para desenhar. Se o advogado não puder validar agora, registre como pendência no arquivo.

### Passo 11. Dar nome, versão e gravar

Nome, setor, versão e data no topo (por exemplo, "Fluxograma · Produção de peças · v1 · AAAA-MM-DD"). Mostre tudo, peça ajustes e só grave depois do ok (seção 9).

## 4. Símbolos e regras do desenho

Três símbolos, como no `escrever-pop`:

| Símbolo | Mermaid | O que é |
|---|---|---|
| INÍCIO e FIM | `I1(["1 · INÍCIO: ..."])` e `F9(["9 · FIM: ..."])` | Pílula. O início é o gatilho; o fim é uma entrega com destinatário. Um início por desenho; fins podem ser vários. Quando o caminho segue em outro processo, o fim diz o nome dele: `(["9 · SEGUE: POP de triagem"])`. |
| AÇÃO | `P4["4 · [A · assistente] Verbo + tarefa ..."]` | Retângulo. Verbo no infinitivo, um responsável, sigla no começo. |
| DECISÃO | `D3{"3 · Pergunta de sim ou não?"}` | Losango. Sempre uma pergunta, sem sigla, com as saídas rotuladas. |

**Espera e documento** entram dentro desses três símbolos, para o desenho continuar legível sem legenda: a espera é uma ação com o verbo "aguardar", quanto dura e quem acompanha (`[S · IA] Aguardar a resposta do cliente por 2 dias úteis (exemplo) e avisar quando estourar`); o documento aparece no texto da ação que o produz ou consulta ("conferir o comprovante de protocolo").

**Regras que valem para qualquer desenho:**
1. **Duas pontas fechadas.** Um gatilho no topo e pelo menos uma entrega no fim.
2. **Verbo em toda ação** e **um responsável por caixa.**
3. **Sigla no começo de cada ação:** `[S · IA]`, `[A · função]`, `[H · função]`. Início, fim e decisão ficam sem sigla.
4. **Losango com as duas saídas nomeadas.** "Sim" e "Não", ou as opções reais. Losango com uma seta só é ação disfarçada.
5. **Nenhuma seta solta.** Toda saída termina num fim, numa volta ou no nome de outro processo.
6. **Exceção como desvio.** O caminho normal desce pelo centro; exceções saem para os lados; volta só quando o processo realmente volta (uma correção, um documento que chegou).
7. **No máximo 15 caixas** de ação e de decisão (início e fim não contam). A faixa comum é de 8 a 15. Passou de 15: agrupe passos seguidos do mesmo responsável e da mesma sigla, ou divida em dois desenhos ligados pelo nome. Ficou abaixo de 6: alguma decisão ficou escondida.
8. **Revisão tracejada nos passos A.** Toda caixa A leva `[REVISÃO HUMANA]` no texto e a classe `revisao`, que desenha a borda tracejada. Um passo A sem revisão no desenho virou S sem ninguém ter decidido.
9. **Linha vermelha visível.** Escolher tese, dar notícia ruim, assinar, aconselhar cliente vulnerável e enviar sem revisão aparecem como caixas H, nunca escondidas dentro de outra caixa.
10. **Um processo por desenho** e **sem dado de cliente.** Exemplo, quando precisar, é fictício ("cliente de aposentadoria especial").

**Altura certa.** Alto demais, uma caixa só ("Fazer a petição") esconde a tese, a revisão e a conferência de datas, e não dá para dizer onde a IA entra. Baixo demais ("Abrir o Word", "Clicar em Arquivo") vira tutorial de software, envelhece na próxima atualização e enterra as decisões. Na medida: "Decidir a tese" (H), "Montar a minuta" (A), "Aprovada?", "Assinar e protocolar" (H).

## 5. Os três formatos

### 5.1 Mermaid

Código num único bloco, sempre `flowchart TD`. Convenções:
- Identificadores por tipo e número: `I` início, `P` ação, `D` decisão, `F` fim (`P4`, `D6`). Nunca use `end` como identificador.
- Todo rótulo entre aspas. Parênteses e dois-pontos fora das aspas quebram o desenho.
- Número no formato `4 ·` (alguns renderizadores leem `4.` no começo do rótulo como lista). Não use aspas duplas dentro do rótulo.
- Saída de decisão com rótulo: `D3 -->|Não, é rotina| P4`.
- No fim do bloco, sempre: `classDef revisao stroke-width:3px,stroke-dasharray:4 2` e `class <todas as caixas A> revisao`.
- A ordem das linhas muda a posição das caixas. Se o código estiver certo e o desenho feio, reorganize as linhas: caminho principal primeiro, desvios depois.

Para ver o desenho: dependendo de onde o Claude roda, o diagrama aparece na própria conversa. Se aparecer só o código, cole num editor de Mermaid (por exemplo, o mermaid.live) e salve a imagem. Esses sites ficam fora do escritório e o link de compartilhamento carrega o diagrama inteiro: nada de cliente entra ali. Se aparecer erro de sintaxe, cole a mensagem de erro na conversa e corrija.

### 5.2 Texto numerado

Para quem não renderiza Mermaid e para a leitura em voz alta. Um item por símbolo, com o mesmo número do Mermaid:

```
1. INÍCIO: [gatilho]. Vá para 2.
2. AÇÃO [S · IA] [Verbo + tarefa]. Confere: [função], por amostra [frequência ou A DEFINIR]. Vá para 3.
3. DECISÃO: [pergunta]? Se sim, vá para 4. Se não, vá para 6.
4. AÇÃO [A · função] [Verbo + tarefa], com rascunho da IA [REVISÃO HUMANA]. Confere: [o que é conferido]. Vá para 5.
5. AÇÃO [H · função] [Verbo + tarefa]. Vá para 7.
6. AÇÃO [H · função] [Verbo + tarefa da exceção]. Vá para 8.
7. FIM: [entrega principal].
8. FIM: [entrega da exceção] (ou SEGUE: [nome do outro processo]).
```

O objeto da revisão fica escrito aqui por inteiro; no Mermaid ele pode vir resumido.

### 5.3 Raias

Uma linha por passo, uma coluna por responsável: **IA**, **Equipe** e **Advogado**. Acrescente a coluna **Cliente** quando ele age no processo (manda documento, assina); o cliente não leva sigla, porque S, A e H classificam o trabalho do escritório. Em escritório com várias funções, a coluna Equipe pode se abrir por função (atendente, controladoria, financeiro), até quatro ou cinco colunas no total.

Como preencher:
- **Passo S:** a caixa fica na coluna IA; na coluna de quem confere, "Confere por amostra".
- **Passo A:** ocupa duas colunas **na mesma linha**: a IA prepara numa, a pessoa revisa na outra, com o objeto da revisão ("A · Revisa: datas e valores"). Se um passo A aparece só na coluna da IA, falta a revisão humana.
- **Passo H:** só na coluna da pessoa.
- **Decisão:** na coluna de quem decide, com as saídas: "Aprovou? sim: passo 9 · não: volta para o 7".

Depois da tabela, entregue: quantas caixas ficaram em cada coluna; quais passagens de bastão (quando o trabalho muda de coluna) são as mais arriscadas e por quê; se alguma coluna humana concentra decisões demais. Cada passagem de bastão é candidata a um prazo interno no POP.

No **solo**, as colunas continuam três: IA, **Equipe (você, em outro momento)** e Advogado (você). A coluna Equipe guarda as revisões feitas em outra hora do dia, com olhar descansado, nunca logo depois de fazer.

Se o advogado quiser as raias também em Mermaid, use um `subgraph` por coluna (`subgraph IA ... end`), cada caixa na raia de quem faz, o passo A como duas caixas ligadas com a mesma sigla (a da pessoa com a classe `revisao`) e o cliente numa raia própria. Funciona bem até umas quatro raias; com mais voltas que isso, fique com a tabela.

## 6. Conferir texto e desenho

| # | Pergunta | Se falhar |
|---|---|---|
| 1 | O INÍCIO é o gatilho do texto, e os FINS são a saída? | Ajuste o desenho ou aponte a diferença no texto. |
| 2 | Cada passo do texto tem uma caixa (ou está agrupado, dizendo quais)? | Inclua a caixa ou registre o agrupamento. |
| 3 | Cada caixa tem a mesma sigla e o mesmo responsável do texto? | Vale o texto; a divergência vai para a lista. |
| 4 | Cada decisão do desenho aparece no texto, como passo H ou como exceção? | Vira "decisão que o desenho revelou". |
| 5 | Cada exceção do texto aparece como desvio no desenho? | Desenhe o desvio. |
| 6 | Toda decisão tem as duas saídas rotuladas e com destino? | Pergunte "e se não?". |
| 7 | Todo A tem quem confere e o que confere, e a classe `revisao`? Todo S tem quem confere por amostra? | Complete; dono que falta vira `[A DEFINIR]`. |
| 8 | Apareceu no desenho algum passo que não está no texto? | Apague ou confirme com o advogado, marcando `[NOVO]`. |
| 9 | Alguma sigla ficou mais otimista que a árvore permite? | Volte para a mais humana. |
| 10 | A linha vermelha está visível em caixas H? | Separe o passo H da caixa onde ele estava escondido. |
| 11 | Há espera que o desenho não mostra? | Desenhe a espera com quanto dura e o que acontece quando estoura. |
| 12 | São 15 caixas ou menos, e nenhum dado de cliente? | Agrupe ou divida; anonimize. |

**Revisor chato de propósito.** Antes de entregar, passe o desenho por cinco frentes e devolva uma tabela (problema, onde está, gravidade alta, média ou baixa, sugestão):
1. **Estrutura:** início e fim claros, setas soltas, decisões sem o "não", caixas sem verbo ou com dois responsáveis.
2. **Exceções esquecidas:** para cada decisão e cada passo da IA, o que acontece quando dá errado, quando falta documento, quando o cliente não responde, quando o prazo aperta, quando o responsável falta.
3. **Siglas:** S que deveria ser A por tocar o cliente, um prazo, um valor ou dado sensível; A sem quem confere; H que é só execução repetitiva.
4. **Esperas:** onde o processo fica parado e o desenho não mostra.
5. **Riscos:** onde um erro da IA chegaria ao cliente ou ao tribunal sem passar por uma pessoa.

Termine com as três correções a fazer primeiro.

## 7. Exemplos resolvidos

**Do retrato ao desenho: o WhatsApp do escritório** (exemplo: escritório de Família com 3 pessoas, setor Atendimento e triagem). O retrato, do jeito que o titular escreveu: a secretária olha o WhatsApp quando dá, de manhã e no fim da tarde; se é gente nova, pergunta o que aconteceu e passa para o titular; se é cliente perguntando do processo, pergunta ao titular, que olha no sistema e diz o que responder; se mandam documento, ela salva no computador; à noite o titular responde o que ficou para trás.

| Linha do retrato | O que ela esconde | O que vira no desenho | Sigla |
|---|---|---|---|
| "Olha quando dá" | Gatilho sem regra; a mensagem das 22h espera até o dia seguinte | Resposta imediata com saudação aprovada e identificação do tipo de mensagem | S |
| "Pergunta o que aconteceu" | Triagem sem roteiro, diferente a cada conversa | Roteiro de triagem da área conduzido pela IA, com a atendente acompanhando | A |
| "Ela me pergunta, eu olho no sistema" | O titular é o gargalo de toda resposta de andamento | IA lê os últimos andamentos e rascunha; atendente confere e envia | A |
| "Salva no computador" | Documento fora da pasta do caso, num computador só | Confirmação de recebimento e arquivamento com nome padrão na pasta do caso | S |
| "À noite eu respondo o que ficou" | Exceção sem dono e sem critério de urgência | Decisão "sinal de urgência ou aflição?", com a atendente assumindo na hora e chamando o advogado | H |
| (não aparece no retrato) | Nada fica registrado; ninguém sabe quantas mensagens chegam | Registro de cada atendimento no CRM ou na planilha, sugerido como `[NOVO]` | S |

Cinco linhas de retrato viraram três decisões e sete ações. É normal o desenho ficar maior que o retrato: ele mostra o que estava implícito. O desenho pronto está em `references/biblioteca/atd-mensagem-nova-no-whatsapp.md`.

**Raias: petição inicial a partir do modelo** (Produção de peças, versão de 10 passos):

| Nº | IA | Equipe | Advogado |
|---|---|---|---|
| 1 | S · Conferir documentos pelo checklist do tipo de caso | Confere por amostra | |
| 2 | A · Montar o briefing e a linha do tempo dos fatos | | A · Revisa: os fatos |
| 3 | | | H · Definir a tese e os pedidos |
| 4 | A · Sugerir caminhos de pesquisa, marcados [CONFERIR] | | A · Revisa: cada fonte, na fonte |
| 5 | A · Escrever a minuta no modelo do escritório | | A · Recebe a minuta |
| 6 | | | H · Fazer a revisão técnica com leitura integral |
| 7 | A · Conferir forma: nomes, datas, valores, pedidos contra fatos | A · Corrige os apontamentos | |
| 8 | | | H · Assinar |
| 9 | S · Registrar número e prazos a partir do comprovante | Protocola | |
| 10 | A · Rascunhar o aviso ao cliente no tom do escritório | A · Revisa e envia | |

Leitura: dez passos, dois S, cinco A e três H. A IA participa de sete, e nenhuma decisão ou assinatura sai da coluna do advogado. As passagens de bastão do 2 para o 3 e do 8 para o 9 pedem prazo interno no POP. No solo, as colunas Equipe e Advogado são a mesma pessoa, e as revisões da coluna Equipe acontecem em outro momento do dia.

## 8. A biblioteca de 10 fluxogramas

Dez desenhos de referência, um por setor, com a IA dentro e a sigla em cada ação, em Mermaid e em texto. Cada um mostra um segundo fluxo que costuma travar o setor, complementar ao POP do mesmo setor na biblioteca do `escrever-pop`. Leia `references/biblioteca/INDICE.md` quando o advogado quiser um gabarito e abra só o arquivo do setor dele.

Use o desenho da biblioteca para **conferir** o do escritório, nunca para **substituir** o retrato: o valor do exercício está em descobrir onde o escritório é diferente. Prazos e intervalos da biblioteca são exemplos e só entram como regra se o advogado disser que valem.

## 9. O que entrega e onde grava

**Entrega,** nesta ordem, para o advogado validar:
1. O fluxograma em Mermaid.
2. A versão em texto numerado.
3. A versão em raias, com a contagem por coluna e as passagens de bastão.
4. O caminho principal em uma linha e a contagem de caixas (S, A, H, decisões).
5. A conferência texto e desenho: divergências e o que o desenho revelou.
6. Os pontos em aberto: `[A DEFINIR]`, `[A CONFIRMAR]` e `[CONFERIR]`, cada um com a pergunta que resolve.

Mostre tudo, peça ajustes e só grave depois do ok.

**Quando o POP ainda não existe:** grave `escritorio/03-pops/<setor>/fluxograma-<processo>.md`, a partir do modelo `assets/fluxograma-modelo.md` (nome, setor, versão, data, dono no topo; anexo com o retrato que originou o desenho). Nome do processo em poucas palavras, minúsculas, sem acento e com hífen (`fluxograma-mensagem-nova-no-whatsapp.md`).

**Quando o POP existe:** atualize a seção "Fluxograma" dentro do próprio POP (`escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md`):
- Troque o Mermaid e o texto, acrescente a subseção "Em raias" e atualize o caminho principal e os pontos ambíguos.
- Suba a versão do POP (1.0 vira 1.1; se o desenho mudou passo, sigla ou responsável, a mudança é do `escrever-pop` e a versão sobe lá) e acrescente uma linha no "Controle de versões": data, "fluxograma redesenhado", quem aprovou.
- Exceção que o desenho revelou e o advogado aprovou entra no campo 7 marcada `[NOVO]`. Passo novo, sigla trocada ou responsável diferente não são alterados aqui: liste e leve ao `escrever-pop`.
- Se existia um `fluxograma-<processo>.md` avulso, escreva no topo dele "Substituído pela seção Fluxograma do POP, versão X" em vez de apagá-lo.

**No `perfil.md`:** atualize `atualizado_em` e acrescente em "Histórico" uma linha com a data, o fluxograma gravado e o caminho. Validação com quem executa ainda não feita vai para "Etapas puladas".

**No Projeto do escritório no Claude:** oriente guardar o código Mermaid ao lado do POP do setor, com nome e versão, e a imagem onde a equipe consulta o POP. Quando sair versão nova, a antiga sai do Projeto.

**Sem acesso a arquivos:** entregue o fluxograma no chat, em bloco pronto para copiar, com o caminho onde ele deveria ficar.

## 10. Trilha solo e trilha equipe

**Solo** (inclusive com estagiário ou secretária):
- As raias continuam valendo: IA, Equipe (você, em outro momento) e Advogado (você), mais o Cliente quando ele age. O ganho é ver o que sai das suas mãos. Muita gente que trabalha sozinha descobre, desenhando, que está na raia de tudo, inclusive de passos que a IA faria com uma conferência rápida no fim do dia.
- Revisar tudo sozinho empurra para S. A sigla não muda por falta de gente: mantenha o A e escreva a compensação na caixa (conferência em outro momento, checklist curto, a IA como segundo olhar).
- "O sócio aprova" vira decisão do titular com regra escrita prévia ou pausa de 24 horas. "A atendente assume" vira "o advogado assume".
- Valide percorrendo o desenho em outro dia, com um caso diferente; se houver estagiário ou secretária, percorra com essa pessoa.

**Equipe:**
- Uma coluna por função que aparece no processo. Conte as caixas de cada coluna: "se o mesmo nome aparece em todas as linhas, ali está o gargalo". Proponha repassar os passos A para quem executa e deixar o titular com decisões, assinaturas e conversas difíceis.
- Cada passagem de bastão vira candidata a prazo interno, e cada ponto de revisão tem dono com nome.
- Valide com quem executa, nunca só com o titular: quem faz o trabalho conhece outro caminho.

## 11. Erros que esta skill evita

| Erro | O que acontece | Como a skill evita |
|---|---|---|
| Desenhar o processo ideal | A equipe olha e não se reconhece | Desenho de hoje primeiro, ok, redesenho depois |
| Caixa sem verbo | Ninguém sabe o que se espera ali | Verbo no infinitivo em toda ação |
| Decisão sem o "não" | A exceção continua existindo, fora do papel | "E se não?" em cada losango |
| Seta solta | O caso some e alguém pergunta, um mês depois, "e aquele?" | Toda saída termina num fim, numa volta ou em outro processo |
| Caixa com dois donos | Cada um acha que o outro revisou | Uma caixa por responsável; passo A em duas colunas |
| Detalhe de clique | Tutorial de software que envelhece e esconde as decisões | Teste de altura de cada caixa |
| Dois processos num desenho | Ninguém mantém e a IA se perde ao ler | Corte onde o gatilho muda; limite de 15 caixas |
| IA sem raia e sem sigla | "Usar o Claude" no meio do fluxo, sem dizer o que faz nem quem confere | Coluna IA e sigla em toda ação |
| Espera invisível | Rápido no papel, semanas na vida real | Espera desenhada com duração |
| Desenhar sozinho | O titular desenha o que acha que acontece | Validação com quem executa, com caso real anonimizado |
| IA inventando passo ou sigla otimista | Desenho que ninguém disse que existe | Acréscimo só como `[NOVO]` com ok; sigla mais humana |
| Dado de cliente no desenho | Nome ou número de processo num site de diagramas | Exemplo fictício e anonimização antes de colar |

## 12. Próximo passo

- **Se o desenho veio antes do POP:** `escrever-pop`. Leve o arquivo `fluxograma-<processo>.md`: o início vira o gatilho (campo 2), cada ação vira um passo com a mesma sigla e o "Executa / Confere" das raias (campo 5), cada saída lateral vira uma exceção (campo 7), os fins viram a saída (campo 8), as caixas S e A alimentam "Onde a IA entra" (campo 9) e as revisões alimentam "Nunca sai sem revisão humana" (campo 10).
- **Se o POP já existia:** `testar-pop`, para rodar o POP com o desenho novo em casos reais anonimizados e ver onde ele quebra.
- Para cada caixa S ou A, a pergunta que fica é: o que a IA precisa ler para fazer isso do jeito do escritório? A resposta vai para a `montar-base`.

## Referências desta skill

- `assets/fluxograma-modelo.md`: o arquivo avulso em branco, para quando o POP ainda não existe.
- `references/biblioteca/INDICE.md`: os 10 fluxogramas de referência, com setor, gatilho e contagem S, A e H. Leia quando o advogado quiser um gabarito.
- `references/biblioteca/*.md`: cada fluxograma completo, em Mermaid e em texto. Abra só o do setor escolhido.
