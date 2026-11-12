---
name: pop-para-skill
description: >
  Transforma o POP de uma automação já desenhada, com as instruções de cada passo vindas da
  desenhar-automacao, num artefato que roda dentro do Claude: no nível 2, instruções para o
  Projeto; no nível 3, uma skill que conduz o POP passo a passo, consulta a base pelo nome,
  para em cada passo A para revisão humana e nunca executa passo H; no nível 4, a mesma skill
  preparada para um gatilho, com pontos fixos de revisão. Gera o SKILL.md, o checklist antes
  de liberar e o roteiro de instalação. Use quando o advogado disser "transformar o POP em
  skill", "criar a skill do escritório", "instalar a automação no Claude", "deixar o POP
  rodando no Claude", "empacotar a automação", "atualizar a skill do POP". Não use para
  desenhar a automação (use desenhar-automacao) nem para escrever o POP (use escrever-pop).
---

# Do POP para a skill

> Pega o POP de uma automação desenhada e as instruções de cada passo e entrega um arquivo que o Claude segue: ele conduz o processo na ordem, consulta os documentos certos da base, para onde uma pessoa precisa revisar e não toca nos passos que são de gente.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha e níveis: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- A `desenhar-automacao` já gravou a ficha e as instruções de passo em `escritorio/05-automacoes/<nome>/` e o escritório quer que o Claude siga o POP sem colar instrução por instrução.
- A automação vai começar a rodada à mão no nível 3 e uma skill facilita a execução.
- A automação cumpriu os critérios para o nível 4 e precisa ficar pronta para ser disparada por um gatilho.
- O POP, uma instrução ou um documento da base mudou e a skill precisa de nova versão.

**Não use quando:**
- Não existe ficha nem instruções de passo: use `desenhar-automacao` antes.
- Não existe POP: use `escrever-pop`.
- O pedido é um agente que escolhe sozinho o próximo passo entre vários processos (nível 5). Fica fora desta versão (seção 3).

## 2. Antes de começar

1. **Leia o perfil** (`escritorio/perfil.md`): trilha, tipo de conta de IA e ambiente em que o escritório usa o Claude (app, Claude Code, outro). Sem perfil, faça o modo rápido das regras transversais.
2. **Portão:** precisam existir, em `escritorio/05-automacoes/<nome>/`, a `ficha.md` com o nível-meta de cada passo e a pasta `instrucoes/` com uma instrução para cada passo S e A. Se faltar: "A skill é a soma das instruções de passo. Sem elas, eu teria de inventar critério, e é exatamente o que a automação não pode fazer." Ofereça a `desenhar-automacao`. Aqui não há atalho: sem instruções, a skill não é gerada.
3. **Confirme o nível** com o advogado, a partir da ficha: 2, 3 ou 4. Se a ficha diz 3 e o advogado pede 4, confira os critérios da seção 8 da `desenhar-automacao` e diga com franqueza o que falta.
4. **Conta.** Se o perfil diz conta pessoal gratuita, a skill pode ser gerada e testada só com dado fictício. Anote isso na linha de versão da skill.

## 3. O que se gera em cada nível

| Nível | O que se gera | Onde roda | Onde grava |
|---|---|---|---|
| 2 Assistente com contexto | Um bloco de instruções para o Projeto no Claude, com o POP resumido e os documentos da base | No Projeto do escritório | `05-automacoes/<nome>/skill/instrucoes-projeto-<nome>.md` |
| 3 Copiloto dentro do POP | Uma skill (SKILL.md) que conduz o POP passo a passo, consulta a base pelo nome, para em cada passo A e nunca executa passo H | Acionada por uma pessoa, a cada execução | `05-automacoes/<nome>/skill/<nome-da-skill>/SKILL.md` |
| 4 Automação de fluxo | A mesma skill, com a seção de disparo: roda a partir de um gatilho (tarefa agendada ou pedido recorrente), executa os S, prepara os A numa fila e para. Nada sai do escritório sem passar pelos pontos fixos de revisão | Disparada pelo gatilho; revisada por uma pessoa em horário fixo | Mesmo caminho, com a pasta `05-automacoes/<nome>/fila/` |

**Por que o nível 5 fica fora desta versão.** Um agente executa vários processos, escolhe o próximo passo dentro de limites escritos e para na fronteira. Isso exige vários POPs maduros conectados, limites de autonomia escritos e registro de tudo o que a IA consultou e fez. A skill gerada aqui segue um POP só, na ordem do POP, e quem decide o caminho é a pessoa. Quando o escritório tiver mais de um fluxo estável no nível 4 por alguns trimestres, a `revisao-periodica` é o lugar de discutir o passo seguinte. "Começar pelo agente, sem POP e sem base, é o jeito mais caro de descobrir que faltava organização."

## 4. Fluxo

### Passo 1. Ler o que já existe
Leia a ficha, o POP (na versão que a ficha indica), cada instrução de passo, o `04-base/INDICE.md` e o plano para erro. Monte e mostre a lista: passo, sigla, nível-meta, instrução, documentos da base que ela cita. Se uma instrução citar documento que não está "em uso" no índice, pare e ofereça a `montar-base`.

### Passo 2. Dar nome e gatilhos à skill
Pergunte, uma de cada vez:
- "Como a equipe pede esse trabalho hoje? Me diga três ou quatro frases do jeito que vocês falam." (exemplo: "vê o andamento de hoje", "tem movimentação nova?")
- "O que parece com isso, mas não é para esta skill?" (exemplo: dúvida de cliente novo, que é do Atendimento)

Com as respostas, escreva o `name` (minúsculas, hífen, curto, igual ao nome da pasta; se o escritório usa outras skills, acrescente a sigla do escritório para não confundir) e a `description` (o que faz, as frases de quem pede, e "Não use para ..."). A `description` é o que faz o Claude reconhecer o pedido: frases reais da equipe funcionam melhor do que termos técnicos.

### Passo 3. Converter cada passo
Transforme cada passo do POP num bloco da skill, pela regra da sigla (seção 5). Copie da instrução o que recebe, o que consulta, os critérios, o formato da entrega, quando parar e o que nunca faz. Não reescreva critério: o critério da skill é o do POP. O que a instrução deixou `[A DEFINIR]` continua `[A DEFINIR]` e faz a skill parar naquele ponto.

### Passo 4. Escrever as travas
Toda skill gerada leva, antes do fluxo: a linha vermelha, as regras de anonimização (tabela de troca padrão), a regra de conta, o que a skill nunca faz e as exceções do POP como pontos de parada. Use o modelo `assets/modelo-skill-automacao.md`, que já traz esses blocos.

### Passo 5. Ligar a skill à base
Liste na skill cada documento da base que ela consulta, pelo nome, com a versão e o caminho. Escolha com o advogado o modo:
- **Modo pasta** (Claude Code ou outro ambiente que lê a pasta de trabalho): a skill lê os documentos direto de `escritorio/04-base/`. A versão vigente é sempre a do índice.
- **Modo empacotado** (app do Claude, sem pasta aberta): uma cópia dos documentos vai em `references/` dentro da pasta da skill, com a versão no nome da seção. Toda mudança na base obriga a gerar nova versão da skill. Anote no `INDICE.md`, na linha do documento: "empacotado na skill <nome>, versão X".
- Em qualquer modo: se o documento não for encontrado, a skill para e pede o documento. Nunca segue com texto próprio no lugar.

### Passo 6. Só no nível 4: disparo, fila e pontes
Defina com o advogado, uma pergunta por vez:
- **Gatilho:** "O que inicia o processo, e em que horário?" Pode ser uma tarefa agendada (se o ambiente do Claude permitir, conferir na sua versão e na configuração da conta) ou um pedido recorrente que a equipe faz sempre igual ("rodar o andamento do dia").
- **Pontos fixos de revisão:** "Em que horário alguém abre a fila, e quem?" Tudo o que vai ao cliente ou ao processo passa por esse ponto.
- **Pontes:** "De onde vem a entrada e para onde vai a saída?" Veja a seção 6.

### Passo 7. Registro de uso
A skill termina cada execução propondo a linha do `registro-de-uso.md` (data, tarefa sem nome do cliente, passo, sigla, nível, ferramenta e conta, quem revisou, o que foi ajustado, se houve erro, tempo gasto). No modo pasta, grava a linha depois que a pessoa confirma. No modo empacotado, entrega a linha para copiar.

### Passo 8. Testar a skill gerada
Instale numa conta de teste ou na do responsável (veja `references/instalacao.md`) e rode cada caso de `04-base/casos-de-teste/<nome>/`. A skill precisa: parar em todo passo A; não executar nenhum passo H; parar no caso que deve parar; pedir o que falta no caso incompleto. Registre o resultado em cada caso. Falha em parada bloqueia a liberação.

### Passo 9. Conferir o checklist antes de liberar
Seção 7. Mostre o checklist preenchido e só libere com todos os itens marcados.

### Passo 10. Instalar
Siga `references/instalacao.md`, na trilha do escritório. Atualize a ficha: versão da skill, data, onde foi instalada e por quem.

## 5. Como cada sigla vira um bloco da skill

| Sigla | O que a skill faz | O que a skill diz |
|---|---|---|
| **S** | Executa o passo seguindo a instrução, mostra o resultado e segue. A conferência por amostra fica com a pessoa indicada no POP | "Passo N feito. Conferência por amostra: [FUNÇÃO]." |
| **A** | Prepara o rascunho, marca como rascunho e **para**. Só segue depois de "aprovado" ou de ajustes da pessoa. Anota quem aprovou | "RASCUNHO PARA REVISÃO. Quem revisa: [FUNÇÃO]. Confira: [objeto da revisão]. Responda 'aprovado' ou diga o que ajustar." |
| **H** | **Nunca executa.** Diz de quem é o passo e, se o POP prevê, entrega o material de apoio (um resumo interno, por exemplo). Só segue quando a pessoa disser que fez | "Este passo é de [FUNÇÃO] e não é feito pela IA. [Material de apoio, se houver.] Me avise quando estiver feito para seguir." |

Palavras de comando que toda skill gerada reconhece: **aprovado** (segue), **ajustar: ...** (refaz o rascunho com o pedido), **parar** (encerra, registra o motivo e não segue), **pular** (só em passo que o POP permite pular; nunca em passo de revisão).

Exemplo de saída num passo A, no formato que a skill usa:

```
Passo 4 · Escrever a mensagem do relevante · RASCUNHO PARA REVISÃO
Quem revisa: assistente de relacionamento. Confira: data da perícia, local, tom, próximo passo.

Olá, [CLIENTE]. ...

Responda "aprovado" ou diga o que ajustar.
```

## 6. Pontes documentadas (integrações)

A skill não escolhe ferramenta. Quando a entrada vem de outro sistema ou a saída vai para outro canal (agenda, e-mail, WhatsApp, software jurídico, ferramentas de automação como n8n, Zapier ou Make), a skill traz uma **ponte documentada**: descreve o que entra e o que sai, e o escritório decide como ligar.

```
Ponte: [NOME, ex.: entrada das movimentações do dia]
Entra: [o quê], em [formato], vindo de [onde]. Quem coloca: [pessoa ou ferramenta, A DEFINIR pelo escritório]
Sai: [o quê], em [formato], para [onde], só com a marca "aprovado por [FUNÇÃO]"
A ponte nunca: envia item sem marca de aprovação; leva senha ou credencial; leva dado além do necessário.
Sem ponte: a pessoa cola a entrada e copia a saída.
```

Até a ponte existir e ser testada, a skill funciona com a pessoa colando e copiando. A ferramenta escolhida passa pela regra de uso de IA (conta, tratamento de dados, quem acessa) antes de ligar. O que depende da ferramenta fica marcado "conferir na configuração da conta".

## 7. Checklist antes de liberar

| Item | Nível 3 | Nível 4 |
|---|---|---|
| Testada com os casos de teste, sem nenhum "não parou" | obrigatório | obrigatório, todos os casos acertando |
| Plano para erro escrito (`plano-para-erro.md`) | rascunho | completo, com a ausência do responsável |
| Responsável pela automação definido | obrigatório | obrigatório, com os pontos fixos de revisão com nome |
| Registro de uso aberto (`registro-de-uso.md`) | obrigatório | obrigatório, com a rodada à mão registrada |
| Linha de base medida (`06-medicao/linha-de-base-<setor>.md`) | obrigatório | obrigatório |
| Conta profissional com tratamento de dados conferido | obrigatório para dado real | obrigatório |
| Critérios de subida do nível 3 ao 4 (`desenhar-automacao`, seção 8) | não se aplica | obrigatório |
| Equipe: acordo de uso de IA assinado por quem vai usar | obrigatório | obrigatório |

## 8. Versão e manutenção

- A skill gerada mostra a linha de versão no começo de cada execução: versão da skill, versão do POP, data e responsável. Quem revisa sabe com que regra a IA trabalhou.
- Gera-se nova versão quando muda o POP, uma instrução de passo ou um documento da base (no modo empacotado, sempre; no modo pasta, quando muda o nome ou o critério do documento).
- Mudanças vêm marcadas com `[NOVO]` ou `[ALTERADO]` na seção "Mudanças" da skill. A IA propõe, o responsável aprova.
- A fonte única fica em `escritorio/05-automacoes/<nome>/skill/`. O que está instalado é cópia. Versão antiga é desinstalada no mesmo dia em que a nova entra.
- Erro repetido no registro de uso, quase incidente ou incidente: siga o plano para erro e volte à `desenhar-automacao` para ajustar a instrução antes de gerar a nova versão.

## 9. O que entrega e onde grava

| Entrega | Onde grava |
|---|---|
| Nível 2: instruções para o Projeto | `escritorio/05-automacoes/<nome>/skill/instrucoes-projeto-<nome>.md` |
| Nível 3 e 4: a skill | `escritorio/05-automacoes/<nome>/skill/<nome-da-skill>/SKILL.md` |
| Modo empacotado: cópia dos documentos da base | `escritorio/05-automacoes/<nome>/skill/<nome-da-skill>/references/` |
| Nível 4: pasta da fila de revisão | `escritorio/05-automacoes/<nome>/fila/` |
| Checklist antes de liberar e versão instalada | Na `ficha.md`, seções "Liberação" e "Histórico" |

Modelos e exemplos desta skill:
- `assets/modelo-skill-automacao.md`: o modelo de SKILL.md de automação, com todos os blocos fixos. Leia no passo 3.
- `references/exemplo-atualizacao-de-andamento.md`: um exemplo completo, gerado a partir do POP de atualização de andamento processual. Leia antes da primeira geração e mostre ao advogado se ele quiser ver como fica.
- `references/instalacao.md`: como instalar, testar e distribuir. Leia no passo 10.

Mostre a skill inteira antes de gravar. Sem acesso a arquivos, entregue o SKILL.md em bloco pronto para copiar, com o caminho onde ele deve ficar.

## 10. Trilha solo e trilha equipe

- **Solo:** instalação na conta do titular. A fonte continua na pasta `escritorio/`, e o titular reinstala a cada nova versão. Como a mesma pessoa executa e revisa, a skill marca os passos A para revisão **em outro momento** quando o POP pedir (por exemplo, rascunhos da manhã revisados no bloco do fim da tarde). No nível 4, a fila respeita o plano para erro: na ausência do titular, nada sai e a fila espera.
- **Equipe:** instalação para a equipe com **o mesmo arquivo para todos e versão controlada.** Só o responsável pela automação gera e publica versão nova. A ficha lista quem instalou e qual versão. Ninguém edita a cópia instalada: ajuste pedido vai para o responsável. Cada ponto de revisão tem dono com nome, e a skill diz esse dono em cada passo A.

## 11. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Skill escrita sem as instruções de passo | A IA inventa critério | Portão: sem ficha e instruções, nada é gerado |
| Passo A que segue sozinho | Mensagem sai sem revisão | Todo A para e espera "aprovado" |
| Passo H executado "para ajudar" | Linha vermelha cruzada | H nunca é executado, só apoiado |
| Documento da base trocado por texto da IA | Modelo que não é do escritório | Documento não encontrado faz a skill parar |
| Integração escolhida antes do fluxo | Ferramenta manda no processo | Ponte documentada; a ferramenta vem depois e passa pela regra de uso |
| Cada pessoa com uma versão | Ninguém sabe que regra valeu | Fonte única, versão na abertura, cópia antiga desinstalada |

## 12. Próximo passo

- Skill liberada: `medir-retorno`, para comparar o registro de uso com a linha de base e montar o primeiro painel.
- Algo falhou no teste ou no uso: `desenhar-automacao`, para ajustar instrução e plano para erro.
- Depois de um trimestre: `revisao-periodica`, para decidir se a automação fica, sobe, desce de nível ou se o próximo processo da fila entra.
