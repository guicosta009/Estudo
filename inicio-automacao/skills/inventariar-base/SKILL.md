---
name: inventariar-base
description: >
  Faz o inventário da pasta onde o escritório guarda modelos, petições antigas, checklists e
  documentos de trabalho, sem mexer em nada: conta arquivos, tipos, tamanhos e datas, acha
  duplicados e famílias de versões (final, final2, v3, cópia, não usar), alerta dado sensível
  pelo nome, deixa pasta de cliente de fora, sugere setor e tipo, propõe a triagem (usar,
  atualizar, descartar, criar), cruza com o que os POPs pedem e monta o plano de reorganização
  em 04-base e o rascunho do índice. Só copia depois do ok, nunca move nem apaga. Use quando o
  advogado disser "minha pasta de modelos é uma bagunça", "faz o inventário da pasta", "acha os
  duplicados", "qual versão é a certa?", "organiza a modelos_FINAL_v3", "o que eu já tenho para a
  base?", "o que o POP pede e eu não tenho". Não use para criar os documentos que faltam nem
  para montar o Projeto no Claude (use montar-base).
---

# Inventariar a base

> Olha a pasta "modelos_FINAL_v3" como ela está hoje, conta a bagunça, separa o que é dado de cliente e propõe para onde cada arquivo vai na base. Nada sai do lugar sem o ok do advogado, e o original nunca é tocado.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Setores, S, A, H e a equação da automação: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`. Estrutura da pasta e a versão no Drive ou no OneDrive: `../../docs/pasta-do-escritorio.md`.

Esta skill é o passo 2 da `montar-base` ("Fazer o inventário do que já existe") feito de verdade, sobre a pasta real do escritório. Ela usa os mesmos nomes, tipos, critério de entrada, cabeçalho, índice e estrutura de `escritorio/04-base/` da montar-base (`../montar-base/SKILL.md`, seções 4 a 6, e `../montar-base/assets/`). O que ela acrescenta é a varredura: em vez de perguntar documento por documento "onde fica, quantas versões tem", ela olha a pasta inteira e traz o retrato pronto para o advogado conferir.

A cena que esta skill resolve: a pasta compartilhada tem "Modelo Inicial FINAL", "FINAL2", "v3 revisado" e "v3 revisado (1)", a contestação "NÃO USAR" ao lado da "novo", a réplica de um caso com o nome do cliente no arquivo e uma pasta "Clientes" no meio dos modelos. Se tudo isso for para o Projeto no Claude do jeito que está, a IA copia com perfeição o modelo errado.

## 1. Quando usar

**Use quando:**
- A `montar-base` chegou ao passo 2 e o escritório tem uma pasta (ou várias) onde guarda modelos e documentos de trabalho.
- O advogado quer saber o que já existe antes de criar qualquer documento novo para a base.
- Os modelos moram em vários lugares ("cada um tem os seus") e é preciso ver as versões lado a lado.
- A `organizar-producao-de-pecas` chegou ao inventário do banco de modelos (passo 5 dela: listar por área e tipo e apontar os duplicados).
- A `desenhar-automacao` apontou "base organizada, sem versões duplicadas" como item de prontidão em aberto.

**Não use quando:**
- A pasta indicada é de caso de cliente. Pasta de cliente não é base: esta skill não abre e não copia. A organização dos documentos de cliente é assunto do padrão de nomes e pastas (esqueleto `../montar-base/assets/esqueletos/padrao-nomes-e-pastas.md`) e do POP do Administrativo.
- O pedido é criar o que falta, escrever critério, separar casos de teste ou montar o Projeto no Claude: use `montar-base` (passo 3 em diante).
- O pedido é organizar, numerar ou publicar POPs: use `gerir-pops`. POP achado na pasta de modelos vai para lá.

## 2. Antes de começar

1. **Leia o perfil.** `escritorio/perfil.md` diz a trilha, as áreas, o tipo de conta de IA e o setor-alvo. Leia também `escritorio/01-cultura/regra-de-uso-de-ia.md`, se existir. Sem perfil, faça o modo rápido das regras transversais (três perguntas, uma por vez) e grave um `perfil.md` mínimo.
2. **Portão: o POP do setor-alvo,** em `escritorio/03-pops/<setor>/`, com a tabela "O que a IA vai precisar consultar" ou o campo "Entradas" preenchido. É com ele que o inventário separa o que entra na primeira rodada.
   - **Se faltar:** explique em duas frases. "O inventário mostra o que existe. Sem o POP, a gente não sabe o que a IA vai precisar, e corre o risco de organizar documento que ninguém usa." Ofereça o `escrever-pop`.
   - **Se o advogado quiser seguir:** rode no **modo inventário**, igual ao da montar-base. A primeira rodada passa a ser o setor-alvo, cada item fica `[A CONFIRMAR]` com a nota "conferir no POP", e registre no `perfil.md`, em "Etapas puladas": "Inventário da base feito antes do POP do setor-alvo (data)".
3. **Sem setor-alvo:** pergunte qual setor o escritório quer automatizar primeiro. Se ninguém souber, o inventário roda mesmo assim, mas tudo fica com rodada `[A CONFIRMAR]`. Ofereça o `diagnostico` ou o `mapear-setores`.
4. **Ambiente.**
   - **Cowork ou Claude Code** (pasta de trabalho aberta, com Python 3): a skill roda `scripts/inventariar_pasta.py` na pasta que o advogado indicar.
   - **Claude no navegador ou sem Python:** não há acesso a pastas. A skill pede a lista de arquivos (colada, ou o print da pasta descrito em texto) e faz o mesmo raciocínio à mão. Siga `references/sem-acesso-a-pasta.md`.
5. **Conta de IA.** O inventário lê só nomes, datas, tamanhos e hash, e roda em qualquer conta. Abrir um arquivo para conferir ou anonimizar é outra coisa: só em conta profissional ou de equipe, com o tratamento de dados conferido. Em conta pessoal gratuita, quem abre e anonimiza é o advogado, fora da IA.

## 3. Regras fixas

1. **Pasta de cliente nunca é aberta nem copiada para a base.** O script não entra em pasta que parece de cliente e não lista o que tem dentro. Só libera (`--liberar-pasta`) se o advogado disser que aquela pasta não é de cliente.
2. **O original nunca é movido, renomeado ou apagado.** O script só copia (`shutil.copy2`, que guarda a data original), cria as pastas que faltam e nunca sobrescreve. Nada é gravado dentro da pasta original. "Descartar" quer dizer: uma cópia vai para `_arquivo/` e o original continua onde estava, até o advogado decidir o que fazer com ele.
3. **Tudo o que entra na base passa pelo critério de entrada da montar-base** (seção 6 dela). A cópia chega como "rascunho", com o cabeçalho padrão. Só vira "em uso" depois do critério.
4. **Dado sensível vira alerta e decisão do advogado.** Nenhuma linha com alerta é copiada sem `anonimizacao_conferida = sim`. Na conversa, use sempre o nome mascarado (`[NOME]`, `[DOC]`, `[PROCESSO]`, `[NÚMERO]`). Nunca repita o nome de cliente que aparecer num arquivo.
5. **A IA propõe, o advogado decide.** Qual versão de uma família é a vigente é decisão humana: é a que o advogado assinaria hoje sem mexer.

## 4. Fluxo

### Passo 1. Achar a pasta
Pergunte, uma por vez:
- "Onde fica a pasta em que o escritório guarda modelos, petições antigas e checklists? Pode ser no computador, no Drive ou no OneDrive."
- "Tem modelo guardado em mais algum lugar? Por exemplo, no computador de outra pessoa, no e-mail de quem saiu, num pendrive."
- "Dentro dessa pasta tem alguma pasta de cliente ou de processo? Se tiver, me diga só o nome dela, para eu deixar de fora."

Cada lugar a mais é uma rodada do inventário (uma pasta de saída para cada). Pasta que o advogado mandar pular entra em `--excluir`.

**Drive ou OneDrive:** rode sobre a pasta sincronizada no computador. Se os arquivos ficam "só na nuvem" (arquivos sob demanda), use `--sem-hash`: ler o conteúdo para o hash baixaria tudo. Documentos nativos do Google (.gdoc, .gsheet) são atalhos: entram na lista, sem hash.

### Passo 2. Rodar o inventário
Na pasta desta skill:

```
python3 scripts/inventariar_pasta.py "<pasta de modelos>" \
  --saida "<pasta>/escritorio/04-base/_inventario/AAAA-MM-DD" \
  --pops "<pasta>/escritorio/03-pops" \
  --setor-alvo "<setor do perfil>"
```

- `--pops` e `--setor-alvo` só se existirem. No Drive ou no OneDrive, acrescente `--estrutura drive` e grave a saída em `02 Base/_inventario/AAAA-MM-DD`.
- A pasta de saída nunca fica dentro da pasta inventariada (o script recusa).
- Se o script disser que a pasta indicada parece de cliente, explique por quê e pergunte. Só use `--liberar-pasta` se o advogado confirmar que não é.

O script grava `inventario.md`, `inventario.tsv`, `plano-de-reorganizacao.tsv` e `INDICE-rascunho.md` e imprime um resumo curto (seção 8 mostra um). Os quatro arquivos ficam em `_inventario/`, fora do Projeto no Claude: o `.tsv` guarda o caminho real, que pode ter nome de cliente.

### Passo 3. Mostrar o retrato, sem propor nada ainda
Mostre a seção 1 do `inventario.md`: quantos arquivos, de que tipos, de quando, os mais antigos, os duplicados exatos e as famílias de versões. Retrato antes de melhoria: nesta hora, nada de "descartar".

Pergunte: "Isso bate com o que você imaginava? Tem alguma pasta que eu deveria ter olhado e ficou de fora?"

### Passo 4. Resolver os alertas de dado sensível
Mostre a seção 2, com os nomes mascarados. Lembre a regra: pasta de caso de cliente não é base, e dado do caso (laudo, holerite, extrato, documento pessoal) volta para a pasta do cliente.

- **Pasta de cliente:** só informe que ficou de fora. Não peça para abrir.
- **Alerta alto,** um por vez: "O arquivo #27 parece a réplica de um caso, com nome e número de processo no nome. Ele fica na pasta do cliente, ou você quer aproveitar a estrutura dele como modelo, depois de anonimizar?"
  - Se for virar modelo: a anonimização segue o critério de entrada da montar-base (tabela de troca padrão, cabeçalho, rodapé e propriedades do arquivo). O advogado faz uma versão anonimizada fora da base, em conta profissional se usar a IA para isso, e o caminho dessa versão substitui a `origem` no plano. Só então a linha ganha `anonimizacao_conferida = sim`.
  - Se for peça padrão ouro: valem os cinco critérios da montar-base (seção 6). A IA pode sugerir a candidata, nunca escolher.
- **Alerta médio:** agrupe por tipo de alerta, um tipo por pergunta. "Estes três arquivos são peças sem a palavra modelo no nome. Costumam ser peças de casos, com dado do cliente no texto. Você sabe se algum deles já foi limpo?"

### Passo 5. Confirmar setor e tipo
Mostre a seção 3. Pergunte só o que ficou em dúvida: setor `[A CONFIRMAR]`, setor com alternativo e tipo "outro". Exemplo: "O #22, 'post instagram ideias', ficou em Marketing e conteúdo, tipo outro. É um documento que a IA vai consultar ou é anotação solta?"

Por que cada arquivo foi para cada setor está na coluna "Palavras que pesaram" e nas regras de `references/regras-de-classificacao.md`.

### Passo 6. Cruzar com os POPs
Mostre a seção 6: o que cada POP pede, o que foi achado na pasta e o que falta.
- **Achado:** a linha do arquivo ganha "Usado por" (POP e passo) e entra na primeira rodada.
- **Falta:** vira uma linha "criar" no plano, com o esqueleto da montar-base indicado. Quem cria é a `montar-base` (passo 5 dela).
- **O POP diz que existe e a pasta não tem:** pergunte onde está ("outra pasta, o drive de alguém, o e-mail?"). Se estiver na cabeça de alguém, anote "não escrito" e vira "criar".

Sem a tabela "O que a IA vai precisar consultar" no POP, leia o campo "Entradas" na conversa e faça o cruzamento à mão. Separe à parte o que é dado do caso (CNIS, holerite, ficha do cliente): isso nunca vira documento da base.

### Passo 7. Triagem linha a linha
Mostre a seção 4 em blocos, pela proposta. As regras estão na seção 5 desta skill.

- **Famílias primeiro,** uma por pergunta: "Família F2: quatro versões do modelo de inicial de aposentadoria especial, a mais recente de 2024. Qual delas você assinaria hoje sem mexer?" Se o advogado escolher outra, troque: a escolhida vira "atualizar", as outras viram "descartar".
- **Depois o resto, um bloco por vez:** "Estes seis ficaram como usar: uma versão só, sem alerta. Algum deles você não usa mais?"
- **Rodada:** a primeira rodada é o que o POP cita (ou, no modo inventário, o setor-alvo e `comum/`). Recomende dar o ok agora só às linhas da primeira rodada e às cópias para `_arquivo/` que vêm junto. O resto fica no plano para a próxima rodada. Se o advogado quiser organizar mais de um setor de uma vez, siga e registre a escolha.

Cada confirmação vira `sim` na coluna `ok_do_advogado` do `plano-de-reorganizacao.tsv`. Dá para fazer de dois jeitos: na conversa (você grava o `sim` depois de cada ok) ou o advogado abre o arquivo numa planilha e preenche. Ajustes de nome, setor ou destino vão nas colunas `setor`, `nome_novo` e `destino`.

### Passo 8. Plano de reorganização e cópia
1. Mostre o plano das linhas aprovadas (seção 5 do `inventario.md`): de onde, para onde, com o nome novo. Mostre a árvore de pastas que vai ser criada.
2. Rode a simulação e mostre o resultado:
   ```
   python3 scripts/inventariar_pasta.py --aplicar "<saida>/plano-de-reorganizacao.tsv" \
     --origem "<pasta de modelos>" --destino "<pasta>/escritorio/04-base" --simular
   ```
3. Pergunte: "Posso copiar estes [N] arquivos para `escritorio/04-base/`? O original continua onde está."
4. Só depois do sim, rode o mesmo comando sem `--simular`. O registro da cópia fica ao lado do plano (`registro-de-copia-AAAA-MM-DD-HHMMSS.md`). Mostre o resumo: copiados, pulados por uma regra, sem ok, e o que fica para a montar-base criar.

Para desfazer, basta apagar as cópias listadas no registro: o original nunca foi tocado.

### Passo 9. Índice e passagem para a montar-base
Mostre o `INDICE-rascunho.md`. Ele já vem no formato do `../montar-base/assets/indice-modelo.md`: levantamento (com "Usado por", versões encontradas e decisão), documentos da base em "rascunho", casos de teste, regras da base e lacunas abertas. Ajuste com o advogado: tire as linhas que não foram copiadas, preencha dono e data quando ele souber.

Grave em `escritorio/04-base/INDICE.md` só depois do ok. Se o índice já existir, não sobrescreva: acrescente as linhas novas marcadas com `[NOVO]` e mostre antes.

## 5. Como o script decide

Tudo pelo nome do arquivo e o nome das pastas. O conteúdo nunca é aberto. As listas completas estão em `references/regras-de-classificacao.md`.

**Retrato.** Arquivos, pastas, tamanho total, por extensão, por ano da última alteração, os cinco mais antigos, quantos têm marca de versão no nome e quantos estão parados há mais de 2 anos (ajustável). Arquivos de sistema e temporários (`~$`, Thumbs.db, .DS_Store) são contados e ignorados.

**Duplicado exato e família.** Duplicado exato é o mesmo conteúdo pelo hash, qualquer que seja o nome. Família é o mesmo nome depois de tirar as marcas de versão (final, final2, v3, revisado, cópia, "(1)", novo, antigo, "não usar", datas), com pelo menos dois conteúdos diferentes.

**Alertas.**

| Nível | O que dispara |
|---|---|
| Alto | Número de processo, CPF ou número longo no nome; nome que parece de pessoa, principalmente seguido de processo, caso, "x" ou número; "cliente" com número ou dado de caso; senha ou credencial |
| Médio | Palavra de dado sensível ou de caso (cpf, rg, laudo, atestado, cid, exame, holerite, extrato, criança, violência, assinado e outras); primeiro nome solto; peça sem a palavra modelo no nome; área com pasta restrita (Família, Criminal) |
| Pasta de cliente | Nome começa com clientes, casos, processos ou autos; tem "cliente", número de processo ou nome de pessoa. Não é aberta |

**Triagem proposta** (a primeira regra que casa decide):

| Situação | Proposta | Para onde |
|---|---|---|
| É POP | fora da base | `gerir-pops` |
| Dado do caso (laudo, holerite, extrato, documento pessoal) | fora da base | volta para a pasta do cliente; não copia |
| Duplicado exato | descartar | não copia |
| "Antigo" ou "não usar" no nome | descartar | `_arquivo/` |
| Versão mais antiga de uma família | descartar | `_arquivo/` |
| A mais recente de uma família | atualizar | o advogado escolhe a vigente e junta numa só |
| Tem alerta | atualizar | abrir, conferir e anonimizar antes |
| Tipo "outro" | descartar | `_arquivo/`, com `[A CONFIRMAR]` se algum POP usa |
| Parado há mais de 2 anos | atualizar | conferir se ainda vale |
| O resto | usar | o destino do setor |
| O POP pede e não existe | criar | `montar-base`, a partir do esqueleto |

"Fora da base" é o caso do "descartar" da montar-base em que o arquivo vai para outro lugar (pasta do cliente ou `03-pops/`), nunca para `_arquivo/`.

**Nome novo e destino** (padrão da montar-base, seção 5):
- `<tipo>-<assunto>[-<area>]`, minúsculas, sem acento, hífen entre as palavras, sem versão no nome. Sai nome de pessoa, número, "processo", "cliente" e as palavras de tipo repetidas.
- Quando o arquivo casa um esqueleto, usa o nome dele: `criterios-relevancia-movimentacao-previdenciario`, `checklist-documentos-auxilio-doenca`, `roteiro-triagem-familia`, `tabela-interna-honorarios`, `regua-de-cobranca`, `padrao-nomes-e-pastas` (em `comum/`).
- Modelo de peça vai para `producao-de-pecas/modelos/<area>/`, como na `organizar-producao-de-pecas`. Os outros setores vão para `<setor>/`, com a área no fim do nome.
- Caso de teste vai para `casos-de-teste/<nome-da-automacao>/caso-NN`, e o nome da automação é preenchido pelo advogado antes da cópia.
- Descartar vai para `_arquivo/<nome-novo>_ate-AAAA-MM-DD.<ext>`, com a data da última alteração, no mesmo padrão de versões substituídas da montar-base.
- A extensão não muda. Arquivo que não é .md (.docx, .pdf, .xlsx, .txt) ganha uma ficha `.md` com o mesmo nome ao lado, com o cabeçalho da montar-base em "rascunho" e a lista do critério de entrada. Arquivo .md ganha o cabeçalho no topo da cópia.

## 6. O script

`scripts/inventariar_pasta.py`, Python 3, só biblioteca padrão. Não abre o conteúdo dos documentos (não depende de leitor de .docx ou .pdf) e não acessa a internet.

| Opção | Para que serve |
|---|---|
| `<pasta>` `--saida <pasta>` | Pasta a inventariar e onde gravar o resultado (fora dela) |
| `--pops <pasta>` | `escritorio/03-pops`, para cruzar com a tabela "O que a IA vai precisar consultar". Ignora `_arquivo/`, `_em-construcao/`, `testes/` e POP aposentado |
| `--setor-alvo <setor>` | Um dos 10 setores, pelo nome ou pelo nome da pasta |
| `--estrutura drive` | Mostra os destinos em `02 Base/` em vez de `escritorio/04-base/` |
| `--excluir <nome>` | Pula uma pasta (repetível) |
| `--liberar-pasta <nome>` | Entra numa pasta que parecia de cliente, depois da confirmação do advogado (repetível) |
| `--anos-parado <n>` | A partir de quantos anos sem alteração a proposta vira "atualizar" (padrão 2) |
| `--sem-hash` | Não lê o conteúdo para o hash (nuvem sob demanda); sem duplicados exatos |
| `--aplicar <plano.tsv>` `--origem` `--destino` | Copia as linhas aprovadas |
| `--simular` | Mostra o que seria copiado, sem copiar |
| `--registro <arquivo>` | Onde gravar o registro da cópia (padrão: ao lado do plano) |

**Colunas do `plano-de-reorganizacao.tsv`:** id, origem (caminho real, relativo à pasta), nome_exibicao (mascarado), setor, area, tipo, esqueleto, alerta, familia, decisao, motivo, nome_novo, destino (relativo à raiz da base), rodada, usado_por, **ok_do_advogado**, **anonimizacao_conferida**, observacao. As duas em negrito são as que o advogado preenche. Linhas `P1`, `P2` são pastas de cliente; linhas `C1`, `C2` são o que o POP pede e falta criar.

**O que o `--aplicar` nunca faz:** copiar linha sem `ok_do_advogado = sim`; copiar pasta de cliente ou linha "fora da base"; copiar linha com alerta sem `anonimizacao_conferida = sim`; copiar para destino com `[A CONFIRMAR]`, `a-definir`, `..` ou caminho absoluto; sobrescrever arquivo que já existe; gravar dentro da pasta original; mover ou apagar o original. Depois de cada cópia, confere o hash da cópia com o do original e desfaz se não bater.

**`inventario.tsv`:** uma linha por arquivo, com caminho, nome mascarado, extensão, tamanho, data, hash, duplicado de, família, marcas de versão, setor e setor alternativo, área, tipo, esqueleto, alertas e as palavras que pesaram. Serve para filtrar numa planilha quando a pasta é grande (o `inventario.md` mostra até 300 linhas por tabela; `--limite-md` muda).

## 7. Sem acesso à pasta

No Claude do navegador, sem pasta aberta e sem Python, o raciocínio é o mesmo e quem aplica é o advogado:
1. Peça a lista de arquivos, colada ou com o print da pasta descrito em texto, e o nome das pastas de cliente (sem o conteúdo).
2. Aplique as regras de `references/regras-de-classificacao.md` e entregue as mesmas seções do `inventario.md` em tabelas no chat. Sem hash, duplicado é "possível duplicado" (mesmo nome sem marcas e mesmo tamanho), a confirmar abrindo os dois.
3. Depois do ok linha a linha, entregue as pastas a criar, a tabela de cópia (de onde, para onde, nome novo, o que fazer antes) e as regras da cópia: copiar, nunca mover; renomear só a cópia; não substituir arquivo que já existe.

Roteiro completo, com as perguntas e os atalhos para gerar a lista: `references/sem-acesso-a-pasta.md`.

## 8. Exemplo resolvido

Pasta fictícia criada pelo `scripts/criar_pasta_exemplo.py`: 35 arquivos pequenos de texto com nomes e extensões de escritório (.docx, .pdf, .xlsx, .txt, .md) e datas antigas simuladas, mais um POP fictício em `03-pops/` com a tabela "O que a IA vai precisar consultar" (cinco itens). Todos os nomes e números são inventados. Duas pastas de cliente fictícias e dois arquivos de sistema estão lá de propósito. A pasta não viaja dentro do plugin, porque os nomes bagunçados (espaço, acento, "(1)", arquivo temporário do Word) são justamente o que se quer mostrar e não passam na instalação: o script monta a pasta na hora, onde o advogado indicar.

```
python3 scripts/criar_pasta_exemplo.py <pasta-de-teste>
python3 scripts/inventariar_pasta.py <pasta-de-teste>/pasta-baguncada --saida <pasta-de-teste>/saida \
  --pops <pasta-de-teste>/03-pops --setor-alvo "Relacionamento com o cliente"
```

Resumo que o script imprime:

```
Inventário de pasta-baguncada
  30 arquivos (3,6 KB), 2 pastas de cliente não abertas, 2 arquivos de sistema ignorados
  duplicados exatos: 2 grupos (2 cópias a mais) · famílias de versões: 3 (8 arquivos)
  alertas de dado sensível: 3 alto, 5 médio
  setor não identificado: 3 · triagem proposta: usar 7, atualizar 10, descartar 9, fora da base 6, criar 2
  POPs lidos: 1 · itens pedidos: 5 · achados na pasta: 3 · faltando: 2
```

O que aparece (saída completa em `scripts/exemplos/saida/inventario.md`):
- "Modelo Inicial Aposentadoria Especial" em FINAL, FINAL2, v3 revisado e "v3 revisado (1)": uma família de quatro, com um duplicado exato. A proposta parte da v3 (`producao-de-pecas/modelos/previdenciario/modelo-inicial-aposentadoria-especial.docx`) e manda FINAL e FINAL2 para `_arquivo/`. Qual vale, quem diz é o advogado.
- "Clientes" e "[NOME] [NOME] x Banco Ficticio" ficam de fora sem ser abertos. Laudo, holerite e extrato viram "fora da base". A réplica com nome e número de processo no arquivo vira "atualizar", com alerta alto, e só é copiada depois de anonimizada.
- Os critérios de relevância, as mensagens prontas e o checklist de documentos casam com os passos 2, 3 e 6 do POP-REL-01 e entram na primeira rodada. O glossário de termos processuais e as perguntas frequentes não existem: viram "criar", com o esqueleto `faq-clientes.md` da montar-base.
- O "POP peticao inicial FINAL_revisado2" vai para a `gerir-pops`.

A cópia foi testada com `scripts/exemplos/saida/plano-aprovado-exemplo.tsv`, em que algumas linhas receberam `sim` de propósito, inclusive linhas que o script deve recusar. O resultado está em `scripts/exemplos/saida/registro-de-copia-exemplo.md`: 8 copiados (com fichas e cabeçalhos de rascunho); recusados a pasta de cliente, o laudo, o extrato, a réplica sem anonimização conferida, um destino fora da base e um destino com `[A CONFIRMAR]`. Rodado de novo, não copiou nada: tudo "já existe, não sobrescrevo". Os originais continuaram idênticos.

## 9. O que entrega e onde grava

| Entrega | Onde grava |
|---|---|
| Inventário (retrato, alertas, setor e tipo, triagem, plano, cruzamento com os POPs) | `escritorio/04-base/_inventario/AAAA-MM-DD/inventario.md` |
| Lista completa para planilha | `escritorio/04-base/_inventario/AAAA-MM-DD/inventario.tsv` |
| Plano de reorganização, com as colunas de ok | `escritorio/04-base/_inventario/AAAA-MM-DD/plano-de-reorganizacao.tsv` |
| Registro da cópia | `escritorio/04-base/_inventario/AAAA-MM-DD/registro-de-copia-AAAA-MM-DD-HHMMSS.md` |
| Cópias aprovadas, com ficha ou cabeçalho em "rascunho" | `escritorio/04-base/<setor>/`, `<setor>/<area>/`, `producao-de-pecas/modelos/<area>/`, `comum/`, `_arquivo/` |
| Índice | rascunho em `_inventario/AAAA-MM-DD/INDICE-rascunho.md`; depois do ok, `escritorio/04-base/INDICE.md` |
| Etapa pulada (modo inventário) | `escritorio/perfil.md`, em "Etapas puladas" |

No Drive ou no OneDrive, os mesmos caminhos ficam dentro de `02 Base/`. A pasta `_inventario/`, como a `_arquivo/`, fica fora do Projeto no Claude. Sem acesso a arquivos, entregue cada documento em bloco pronto para copiar, com o nome e o caminho.

## 10. Trilha solo e trilha equipe

- **Solo:** o titular dá todos os oks, mas não precisa fazer tudo. Se houver estagiário ou secretária, essa pessoa pode rodar o inventário, conferir setor e nome novo e preencher o plano; o titular decide as famílias, os alertas e o ok final, de preferência em outro momento do dia. Depois da primeira limpeza, o hábito da montar-base (15 minutos no fim da semana) evita que a pasta volte a crescer.
- **Equipe:** quando "cada um tem os seus", rode uma vez por pasta de pessoa e compare as famílias: o mesmo modelo em quatro versões, uma por mesa, é o retrato dos "quatro escritórios dentro de um". A escolha da vigente é do dono da pasta da base, e do advogado da área quando o conteúdo é jurídico. Os alertas vão também para o guardião de dados. Pastas restritas (Família com criança, saúde, criminal) só são abertas por quem trabalha nesses casos.

## 11. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Despejar a pasta inteira no Projeto | A IA consulta a versão velha e o modelo com nome de cliente | Inventário, triagem e índice antes de qualquer cópia |
| Abrir pasta de cliente para "organizar tudo" | Dado do caso vai parar na base | O script não entra em pasta que parece de cliente |
| Mover ou apagar no meio da limpeza | Some o único exemplar de um modelo | Só cópia, nunca sobrescreve, original intacto |
| A IA escolher a versão "certa" pela data | Fica a versão mais nova e pior | A família vai para o advogado decidir |
| Peça antiga com nome do cliente virar modelo | Sigilo exposto em toda conversa | Alerta, anonimização conferida e critério de entrada |
| Organizar tudo de uma vez | A base vira a mesma "modelos_FINAL_v3", só que maior | Rodada pelo que o POP cita ou pelo setor-alvo |
| Repetir nome de cliente na conversa | Dado espalhado no histórico | Nome mascarado em tudo o que aparece na tela |

## 12. Próximo passo

- Cópia feita e índice gravado: siga na `montar-base`, do passo 3 em diante (triagem final dos documentos copiados, criar o que falta a partir dos esqueletos, critério de entrada, casos de teste e Projeto no Claude).
- Apareceu POP na pasta de modelos: `gerir-pops` (rotina 2, padronizar código e nome).
- Faltou o POP do setor-alvo: `escrever-pop`, e depois rode o inventário de novo com `--pops` para separar a primeira rodada.
- O banco de modelos de peça precisa de ficha, dono e fundamentação datada: `organizar-producao-de-pecas` (passo 5).
