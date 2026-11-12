---
name: desenhar-automacao
description: >
  Desenha a primeira automação do setor-alvo a partir do POP com S, A e H: escolhe um
  processo, aplica o checklist de prontidão de 11 itens, define o nível-meta de cada passo,
  escreve a instrução de cada passo S e A, combina a rodada à mão no nível 3, testa com os
  casos anonimizados contra o gabarito e fecha plano para erro, registro de uso e
  responsável. Use quando o advogado disser "quero automatizar esse processo", "estou pronto
  para automatizar?", "montar a automação do setor", "escrever as instruções da IA para o
  POP", "subir para o nível 4", "fazer o plano para erro", "testar a automação", "o que falta
  para automatizar". Não use para escrever o POP (use escrever-pop), para transformar a
  automação numa skill instalável (use pop-para-skill) nem para medir horas (use
  medir-retorno).
---

# Desenhar a automação

> Pega um processo do setor-alvo, confere se ele está pronto, decide até que nível a IA vai em cada passo e escreve as instruções que ela segue, com teste, plano para erro e um responsável. "Automação é um POP executado pela IA, consultando a base de conhecimento e dentro da régua da cultura."

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha e dos cinco níveis: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- O setor-alvo tem POP com S, A e H e o advogado quer que a IA passe a executar os passos S e A.
- O advogado quer saber se está pronto para automatizar e até que nível dá para ir.
- Uma automação já roda no nível 3 e o escritório quer avaliar se sobe para o 4.
- Uma automação deu erro e é preciso rever instruções, teste ou plano para erro.

**Não use quando:**
- Não existe POP do processo: use `escrever-pop` (e `classificar-sah` para as siglas).
- O pedido é empacotar a automação já desenhada numa skill para instalar no Claude: use `pop-para-skill`.
- O pedido é medir horas devolvidas ou montar o painel: use `medir-retorno`.
- O pedido é auditar riscos de um fluxo em detalhe: use `auditar-riscos` (esta skill chama a auditoria quando encontra problema).

## 2. Antes de começar

1. **Leia o perfil** (`escritorio/perfil.md`): trilha, porte, áreas, tipo de conta de IA, setor-alvo. Sem perfil, faça o modo rápido das regras transversais.
2. **Portão forte.** Três coisas precisam existir. Confira na pasta e pergunte só o que não der para ver:
   - **POP do processo com S, A e H**, em `escritorio/03-pops/<setor>/`. Se faltar: "A IA não sabe o próximo passo sem o roteiro. Sem POP, você vira o fluxo e continua sendo o gargalo." Ofereça o `escrever-pop`.
   - **Código do escritório no Projeto** (ou na pasta aberta): `escritorio/01-cultura/instrucoes-do-projeto.md` existe e o advogado confirma que está no Projeto que vai rodar a automação. Se faltar: "Sem a régua, a IA produz rápido no tom errado e ninguém sabe dizer se o resultado está bom." Ofereça o `codigo-do-escritorio`.
   - **Regra de uso de IA** em `escritorio/01-cultura/regra-de-uso-de-ia.md`. Se faltar: "Sem regra escrita, nenhum passo com dado de cliente pode ficar S, e não dá para saber em que conta a automação roda." Ofereça a `regra-de-uso-de-ia`.
   - Se o advogado quiser seguir sem algum dos três, siga só até o passo 4 (nível-meta), com o nível máximo travado em 2, e registre em "Etapas puladas" no `perfil.md`. Instrução de passo sem POP, sem código ou sem regra não é escrita.
3. **Veja o que mais existe**, sem bloquear: base em `escritorio/04-base/INDICE.md`, casos de teste em `escritorio/04-base/casos-de-teste/`, linha de base em `escritorio/06-medicao/linha-de-base-<setor>.md`. Tudo isso entra no checklist de prontidão.

## 3. Fluxo

### Passo 1. Escolher um processo
Uma automação por vez, de um processo só. Liste os POPs do setor-alvo e pergunte:
- "Qual desses processos toma mais horas da equipe por semana?" (use o mapa em `02-mapa/` se existir)
- "Em qual deles a regra está mais clara, de modo que duas pessoas seguindo o papel chegariam ao mesmo resultado?"

Escolha **o de mais horas e regra mais clara**. Se os dois critérios apontarem processos diferentes, fique com o de regra mais clara e deixe o outro anotado como próximo. Dê um nome curto à automação, em minúsculas e com hífen (exemplo: `atualizacao-de-andamento`). Esse nome vira a pasta `escritorio/05-automacoes/<nome>/`.

### Passo 2. Revisar o POP com a IA dentro do fluxo
Leia o POP e confira, sem reescrever:
- Todo passo da linha vermelha está marcado H.
- Todo passo A diz o que a pessoa confere (citações, nomes, datas, valores, prazos, tom). Revisão sem objeto vira carimbo.
- Gatilho, exceções e saída estão escritos.
- As siglas respeitam o estágio do escritório (trava por estágio da `classificar-sah`).

Se encontrar problema, mostre a lista e ofereça voltar ao `escrever-pop` ou rodar a `auditar-riscos`. Não mude sigla sozinho: a IA propõe, o advogado decide.

### Passo 3. Aplicar o checklist de prontidão
Confira os 11 itens da seção 4. Marque o que dá para ver nos arquivos e pergunte o resto, uma pergunta por vez. Depois pergunte: "Até que nível você quer levar esse processo agora?"

Dê a leitura pela soma:
- **10 a 11:** pronto para o nível 4, depois de rodar à mão no nível 3.
- **6 a 9:** nível 3, perto do 4. Fechar POP e base primeiro.
- **Até 5:** ainda no nível 2. Focar em POP e código. A meta realista é o copiloto do nível 3.

**Se o nível pedido for alto demais, diga com franqueza.** Exemplo: "Você quer o nível 4, e hoje são 7 de 11. Faltam a base com dono e data, os casos de teste e o plano para erro. Dá para rodar no nível 3 já nesta semana e voltar a olhar o 4 quando esses três estiverem prontos." Se pedirem o nível 5, explique que ele exige vários POPs maduros conectados, limites de autonomia escritos e registro de tudo o que a IA consultou e fez, e que fica fora desta versão do método.

Para cada item faltando, diga o que fazer e qual skill resolve (seção 4). Se faltar a linha de base, recomende rodar a `medir-retorno` **antes** do passo 6: a rodada à mão já muda o trabalho e o "antes" se perde.

### Passo 4. Definir o nível-meta de cada passo
Para cada passo do POP, monte a tabela:

| Passo | S, A ou H | Nível hoje | Nível-meta | O que falta para chegar |
|---|---|---|---|---|

Regras:
- Passo H não tem nível. Anote só o material que a IA pode preparar em volta.
- Qualquer passo que envolva escolha de tese, notícia ruim, assinatura, cliente vulnerável ou envio sem revisão humana é H, sem exceção.
- O nível-meta não passa do que a prontidão permite (até 5: nível 2; 6 a 9: nível 3; 10 a 11: nível 4).
- Subir um ou dois níveis por vez. Nível 4 só para passos que já rodaram à mão no nível 3.
- Depois da tabela, aponte os passos com mais horas economizáveis e menor risco: são os primeiros a ganhar instrução.

A referência `references/mapa-setor-nivel.md` mostra, para cada setor, como cada nível costuma aparecer na prática e o que cada nível exige. Use para explicar o degrau ao advogado.

### Passo 5. Escrever a instrução de cada passo S e A
Antes da primeira instrução, leia `references/do-pop-a-instrucao.md`: quando juntar dois passos numa instrução, os oito blocos e em que campo do modelo cada um entra, as perguntas que completam a entrevista abaixo, a cláusula de parada, três exemplos resolvidos (Prazos, Peças, Relacionamento) e a auditoria da instrução antes de mostrar. Volte a ela no passo 7, para testar cada instrução e corrigir depois de um erro.

Uma instrução por passo, um passo por vez. Para cada um, pergunte só o que faltar:
1. "O que exatamente chega nesse passo, e em que formato?" (uma lista colada, um PDF, a mensagem do cliente)
2. "Que documentos da base esse passo consulta?" Confira os nomes no `INDICE.md`.
3. "Que critério decide o resultado?" Copie do POP. Se o POP não tem, fica `[A DEFINIR]`.
4. "Como deve sair a entrega?" (tabela, mensagem pronta para revisar, lista)
5. "Em que situação a IA deve parar e chamar alguém?"

Escreva no modelo da seção 5. Em passo A, a instrução diz que a entrega é rascunho para revisão humana. Use o tom do código e não invente regra. Se a instrução citar um documento que a base não tem, marque `[A DEFINIR]` com a nota "falta na base: nome do documento" e anote para a `montar-base`. Grave em `instrucoes/passo-NN-<verbo-objeto>.md` depois do ok.

### Passo 6. Rodar à mão no nível 3, por uma a duas semanas
Antes de qualquer gatilho automático, o POP roda à mão: a pessoa abre o Projeto, aciona a instrução em cada passo S e A, revisa e segue. Combine com o advogado:
- Quem roda e em que horário (de preferência no horário em que o processo já acontece).
- Toda execução vai para o registro de uso (passo 9).
- **Toda exceção que aparecer vira ajuste no POP**, com nova versão, e as instruções afetadas são revistas.
- Ao fim da primeira semana, olhar o registro: quantos ajustes, em que passo, que erro a revisão pegou.

Ofereça a `pop-para-skill` em nível 3 para facilitar a rodada à mão: a skill conduz o POP passo a passo e para em cada A.

### Passo 7. Testar com os casos anonimizados
Rode cada caso de teste de `escritorio/04-base/casos-de-teste/<nome>/` com as instruções atuais e compare com o gabarito. Se não houver casos, ofereça a `montar-base` (seção de casos de teste). Para cada caso, um resultado:

| Resultado | Leitura | O que fazer |
|---|---|---|
| Acertou | Igual ao gabarito no que importa | Nada |
| Acertou com ajuste | Certo, mas pediu correção de tom ou forma | Ajustar instrução ou modelo da base |
| Errou | Classificação, dado, data ou próximo passo diferente do gabarito | Ajustar instrução ou base e rodar **todos** os casos de novo |
| Parou certo | Era o caso que deve parar, e parou | Nada |
| Não parou | Devia ter parado e seguiu | **Bloqueia a subida de nível.** Rever "quando parar" e "o que nunca faz" |

Registre o resultado em cada caso e o resumo na `ficha.md`. Instrução alterada ganha nova versão.

### Passo 8. Escrever o plano para erro
Uma página por automação, com os 7 itens da seção 6, preenchida com o advogado, uma pergunta por item. Na trilha solo, inclua a versão que prevê a ausência do titular. Grave em `plano-para-erro.md`.

### Passo 9. Abrir o registro de uso
Crie `registro-de-uso.md` com as colunas da seção 7. Combine quem preenche (quem revisou) e quando (a cada execução no nível 3, a cada lote no nível 4).

### Passo 10. Definir o responsável e os pontos fixos de revisão
- **Responsável pela automação:** um nome. Cuida das instruções, pausa quando der erro, autoriza a volta e lê o registro toda semana.
- **Pontos fixos de revisão:** para cada passo A e para tudo o que sai do escritório, quem revisa e o que confere.

### Passo 11. Medir contra a linha de base e decidir o próximo degrau
Depois da rodada à mão, compare o tempo do registro de uso com a linha de base do setor (`06-medicao/linha-de-base-<setor>.md`). A conta das horas devolvidas é da `medir-retorno`. Para subir ao nível 4, confira os critérios da seção 8. Se passar, siga para a `pop-para-skill` em nível 4.

## 4. Checklist de prontidão (11 itens)

| # | Item | Se faltar, quem resolve |
|---|---|---|
| 1 | POP com S, A e H, com gatilho, responsável, prazo, exceções e saída | `escrever-pop`, `classificar-sah` |
| 2 | Fluxograma desenhado, com decisões e pontos de revisão visíveis | `escrever-pop` |
| 3 | Linha vermelha marcada e escrita no código | `codigo-do-escritorio` |
| 4 | Código no Projeto (tom, dados e sigilo, o que nunca fazemos) | `codigo-do-escritorio` |
| 5 | Base organizada (nomes claros, sem versões duplicadas) | `montar-base` |
| 6 | Linha de base medida | `medir-retorno` |
| 7 | Responsável pela automação | esta skill, passo 10 |
| 8 | Regra de uso de IA conhecida pela equipe (no solo, o autocompromisso) | `regra-de-uso-de-ia`, `implantar-a-mudanca` |
| 9 | Conta profissional com o tratamento de dados conferido | `regra-de-uso-de-ia` |
| 10 | 3 a 5 casos de teste anonimizados | `montar-base` |
| 11 | Plano para erro rascunhado | esta skill, passo 8 |

Leitura: **10 a 11** pronto para o nível 4 · **6 a 9** nível 3, perto do 4 · **até 5** ainda no nível 2.

## 5. A instrução de um passo S ou A

Modelo em `assets/instrucao-de-passo-modelo.md`. Campos:

```
# Instrução · Passo [N] · [VERBO + OBJETO]
Automação: [NOME] · POP: [ARQUIVO], versão [V] · Sigla: S | A · Nível-meta: [N]
Versão da instrução: 1.0 · Revisado em: AAAA-MM-DD · Dono: [RESPONSÁVEL PELA AUTOMAÇÃO]

Objetivo: [uma frase]
O que recebe: [o que entra e em que formato]
Passo a passo:
1. [ação], consultando [NOME DO DOCUMENTO DA BASE]
2. ...
Critérios (copiados do POP): [...]
Formato da entrega: [exato]
Pare e chame [FUNÇÃO] quando: [dúvida, exceção, qualquer item da linha vermelha]
Nunca: [...]
(Só em passo A) A entrega é um rascunho para revisão humana. Quem revisa confere: [objeto da revisão].
```

## 6. Plano para erro (7 itens)

Modelo em `assets/plano-para-erro-modelo.md`.
1. Como a gente percebe o erro.
2. Quem pausa a automação e como.
3. Se o erro chegou ao cliente ou ao processo, quem avisa e por qual canal (de preferência o advogado responsável, por ligação).
4. Como corrigir o que já saiu.
5. O que muda para não repetir (POP, base, instrução ou ponto de revisão).
6. Onde fica registrado (`06-medicao/incidentes.md`, incidente ou quase incidente).
7. Quando volta a rodar e quem autoriza.

Quem avisa um erro nunca é punido por avisar.

## 7. Registro de uso

Modelo em `assets/registro-de-uso-modelo.md`. Colunas:

| Data | Tarefa (sem nome do cliente) | Passo do POP | S ou A | Nível | Ferramenta e conta | Quem revisou | O que foi ajustado | Houve erro? | Tempo gasto |
|---|---|---|---|---|---|---|---|---|---|
| (exemplo) AAAA-MM-DD | Atualização de andamento, processo 014 | Passo 4, escrever mensagem | A | 3 | Projeto do escritório, conta de equipe | Assistente de relacionamento | Ajustou o tom do segundo parágrafo | não | 6 min |

O registro alimenta a `medir-retorno` (tempo gasto) e a `revisao-periodica` (erro repetido vira ajuste no POP ou na base).

## 8. Critérios para subir do nível 3 ao 4

Critério prático e ajustável pelo escritório. Todos juntos:
- Prontidão em 10 ou 11.
- POP rodado à mão no nível 3 por uma a duas semanas, com registro de cada execução.
- Na última semana, nenhuma exceção nova que tenha mudado o POP.
- Todos os casos de teste passaram e nenhum caso "que deve parar" seguiu adiante.
- Nenhum incidente aberto, e os quase incidentes viraram ajuste.
- Responsável e pontos fixos de revisão com nome.

Subir ao nível 4 não tira nenhum ponto de revisão: tudo o que vai ao cliente ou ao processo continua passando por uma pessoa. "Nenhum passo H some: ele só passa a receber material mais bem preparado."

## 9. Exemplo resolvido

Escritório previdenciário com 5 pessoas (exemplo). Setor-alvo Relacionamento com o cliente. Processo escolhido: atualização de andamento processual (o de mais horas e com critério de relevância já escrito).
- **Prontidão: 7 de 11.** Faltavam linha de base, casos de teste, plano para erro e o fluxograma. Pediram nível 4. Leitura: nível 3 agora, 4 depois de fechar o que falta.
- **Nível-meta:** ler movimentações (S, 3), classificar rotina ou relevante (S, 3), registrar rotina (S, 3), escrever a mensagem do relevante (A, 3), revisar decisão de mérito (A, 3, advogado), ligar em notícia muito ruim (H), responder dúvida (A, 3), assumir conversa que pede advogado (H).
- **Rodada à mão:** duas semanas. Na primeira, a perícia remarcada não estava nos critérios. Virou item novo em `criterios-relevancia-movimentacao-previdenciario.md`, versão 1.1.
- **Teste:** 5 casos. O caso da notícia desfavorável parou e indicou ligação. Um caso errou o próximo passo; a instrução do passo 4 ganhou a versão 1.1 e todos os casos rodaram de novo.

O desenho completo e a skill gerada a partir dele estão na referência da `pop-para-skill`.

## 10. O que entrega e onde grava

Tudo em `escritorio/05-automacoes/<nome>/`:

| Arquivo | O que tem | Modelo |
|---|---|---|
| `ficha.md` | Processo, POP de origem e versão, prontidão, nível hoje e nível-meta por passo, responsável, pontos fixos de revisão, base usada, resultado dos testes, rodada à mão, situação | `assets/ficha-modelo.md` |
| `instrucoes/passo-NN-<verbo-objeto>.md` | Uma instrução por passo S ou A | `assets/instrucao-de-passo-modelo.md` |
| `plano-para-erro.md` | Os 7 itens | `assets/plano-para-erro-modelo.md` |
| `registro-de-uso.md` | O registro aberto | `assets/registro-de-uso-modelo.md` |

Também: resultado em cada caso de teste (`04-base/casos-de-teste/<nome>/`) e o item "Prontidão e primeira automação" marcado no `perfil.md`. Mostre cada arquivo antes de gravar.

## 11. Trilha solo e trilha equipe

- **Solo:** o titular é o responsável pela automação, e o plano para erro **prevê a ausência dele** (férias, audiência, doença): quem pausa (a secretária ou o estagiário podem pausar, nunca decidir), o que espera na fila sem sair, quem revisa no lugar `[A DEFINIR]` (advogado parceiro, por exemplo) e o que é urgente e vai por ligação. **Atenção à fadiga de revisão:** revisar tudo sozinho cansa e empurra para S. Combine blocos fixos de revisão no dia e um limite de itens por bloco; se a fila passar do limite, diminui o volume da automação, nunca a revisão.
- **Equipe:** responsável pela automação com nome. **Cada ponto de revisão com dono e critério** escritos na ficha. Se o mesmo nome aparece em todos os pontos, ali está o gargalo. Quem usa a automação assinou o acordo de uso de IA.

## 12. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Automatizar o setor inteiro de uma vez | Nada fica estável | Um processo, o de mais horas e regra mais clara |
| Pular do nível 2 para o 4 | O erro aparece no cliente | Rodada à mão no nível 3 e critérios para subir |
| Instrução genérica ("escreva a mensagem") | Cada execução sai diferente | Modelo de instrução com entrada, critério, formato e parada |
| Testar só o caso que dá certo | Aprova sem ver a exceção | Casos que devem parar bloqueiam a subida |
| Juntar numa instrução dois passos com um H no meio | A IA decide por omissão | Agrupamento nunca atravessa um H; a decisão entra como dado na instrução seguinte |
| Mexer na instrução por um erro que é da base, do POP ou da entrada | O problema volta escondido | Achar a causa antes de mudar o texto e rodar todos os casos de novo |
| Automação sem dono | Erro sem ninguém para pausar | Responsável e plano para erro antes de rodar |
| Começar pelo agente | "O jeito mais caro de descobrir que faltava organização" | Nível 5 fora desta versão |

## 13. Próximo passo

- Automação desenhada: `pop-para-skill`, no nível-meta (3 para a rodada à mão, 4 depois dos critérios da seção 8).
- Faltou base ou casos de teste: `montar-base`.
- Faltou linha de base, ou a rodada à mão terminou: `medir-retorno`.
- Daqui a um trimestre: `revisao-periodica`.
