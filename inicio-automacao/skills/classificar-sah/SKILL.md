---
name: classificar-sah
description: >
  Classifica cada passo ou atividade do escritório em S (Substituição, a IA faz no lugar),
  A (Auxílio, a IA prepara e a pessoa decide) ou H (continua Humano), indica o nível de
  inserção da IA (1 a 5) e o cuidado obrigatório de cada passo. Use quando o advogado disser
  "classificar S A H", "o que a IA pode fazer nesse processo", "onde a IA entra", "marcar os
  passos do POP", "esse passo pode ser automatizado?", "o que continua humano", "nível de
  automação de cada passo", ou quando outra skill do plugin (mapear-setores, escrever-pop,
  desenhar-automacao) precisar da classificação. Não use para escrever o POP inteiro (use
  escrever-pop) nem para auditar riscos de um fluxo pronto (use auditar-riscos).
---

# Classificar S, A ou H

> Decide, passo a passo, o que a IA faz no lugar, o que ela prepara para uma pessoa decidir e o que continua humano. É a régua que todas as outras skills do plugin usam quando falam de "onde a IA entra".

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de S, A, H, linha vermelha e níveis: `../../docs/glossario.md`.

## 1. Quando usar

**Use quando:**
- O advogado tem uma lista de atividades de um setor (vinda do `mapear-setores`) e quer saber o que cabe em S, A ou H.
- Há um POP, ou um passo a passo de como o setor funciona hoje, e é preciso marcar cada passo.
- Outra skill chamou esta para classificar passos (nesse caso, rode direto o passo 3 em diante e devolva a tabela).
- O escritório mudou de estágio (passou a ter conta profissional, regra escrita ou base) e quer rever as siglas.

**Não use quando:**
- Ainda não existe nenhum passo a passo. Primeiro é preciso o retrato de como o trabalho acontece hoje: ofereça o `escrever-pop` (modo "do zero") ou o `mapear-setores`.
- O pedido é avaliar os riscos de um fluxo já desenhado para automatizar: use `auditar-riscos`.

## 2. Antes de começar

1. Leia `escritorio/perfil.md` (trilha, porte, áreas e tipo de conta de IA) e, se existir, o código do escritório e a regra de uso de IA. Sem perfil, faça o modo rápido descrito nas regras transversais.
2. **Portão:** precisa existir uma lista de passos ou atividades. Pode vir colada na conversa, de um arquivo em `escritorio/02-mapa/` ou `escritorio/03-pops/`, ou de um áudio transcrito.
3. **Descubra o estágio do escritório,** porque ele trava algumas siglas (seção 5). Se não estiver no perfil, pergunte, uma de cada vez:
   - A IA roda em conta profissional ou de equipe, com o tratamento de dados conferido?
   - Existe regra de uso de IA escrita?
   - Os modelos, critérios e checklists que esse processo usa estão organizados num lugar que a IA consulta?

## 3. Fluxo

### Passo 1. Organizar a lista
- Reescreva cada item como **verbo + objeto** ("Ler publicações do dia", e não "publicações").
- Se um item for grande demais (mais de duas horas ou várias decisões dentro), proponha quebrar. Exemplo: "Fazer a petição inicial" vira ler documentos, montar a linha do tempo, redigir a minuta, revisar.
- Se aparecer dado de cliente, avise e troque pela versão anonimizada.
- Mostre a lista organizada e peça ok antes de classificar.

### Passo 2. Levantar o que falta para decidir
Para cada passo você precisa saber, pelo menos: com que frequência acontece, se existe regra escrita, o tamanho do estrago se der errado e se envolve dado sensível ou fala direta com o cliente. Pergunte só o que não dá para inferir, uma pergunta por vez. O que ficar sem resposta vira `[A CONFIRMAR]` e puxa a sigla para a mais humana.

### Passo 3. Aplicar a árvore de decisão
Para cada passo, nesta ordem. A primeira resposta que leva a uma sigla encerra a análise:

1. **O passo toca a linha vermelha?** Escolha de tese ou estratégia, notícia ruim ao cliente, assinatura ou responsabilidade técnica, aconselhamento de cliente vulnerável, envio de peça ou mensagem jurídica sem revisão. Sim: **H**.
2. **Exige decisão estratégica, julgamento ético ou conversa delicada?** Sim: **H**.
3. **A regra cabe num papel, de modo que duas pessoas seguindo o papel chegariam ao mesmo resultado?** Não: **A**.
4. **Se a IA errar, o estrago é pequeno e alguém percebe antes do cliente, do tribunal ou do público?** Não: **A** (a pessoa revisa tudo).
5. **O resultado sai do escritório, ou mexe com dado sensível sem conferência depois?** Sim: **A**. Não: **S** (conferência por amostra).

### Passo 4. Conferir com os seis critérios
Use a tabela para confirmar a sigla e escrever a justificativa:

| Critério | Puxa para S | Puxa para A | Puxa para H |
|---|---|---|---|
| Regra clara | Cabe num papel, sem "depende" | Existe regra, com exceções frequentes | Cada caso pede julgamento |
| Volume | Alto e repetitivo, toda semana | Médio, com variação | Baixo, pontual e importante |
| Risco do erro | Barato, percebido no passo seguinte | Relevante, uma conferência pega | Grave ou irreversível (prazo, cliente ofendido, peça assinada) |
| Dado sensível | Sem dado pessoal, ou já anonimizado | Dado pessoal em conta profissional, com conferência | Saúde, criança ou adolescente, violência |
| Relação com o cliente | Mensagem informativa de modelo aprovado | Mensagem personalizada revisada | Conversa difícil, notícia ruim, negociação, reclamação |
| Responsabilidade | Ninguém assina | Alguém valida | Alguém assina e responde profissionalmente |

**Grade rápida** para casos de dúvida:
- Regra clara e erro barato: **S** (renomear arquivo, vincular publicação, lembrete de vencimento).
- Regra clara e erro caro: **A** (sugerir data-limite de prazo, gerar contrato da proposta aprovada).
- Sem regra e erro barato: **A** (pauta, primeira versão de mensagem, roteiro de perguntas).
- Sem regra e erro caro: **H** (tese, honorário, conversa depois de notícia ruim).

### Passo 5. Aplicar a trava por estágio
Veja a seção 5. Ajuste as siglas e explique cada ajuste.

### Passo 6. Indicar o nível de inserção
Para cada passo S ou A, indique o nível de hoje e o nível possível no próximo ciclo (1 a 5, definições no glossário). Passo H não tem nível: a IA só prepara material em volta. Para subir um nível, diga o que falta (no código, no POP, na base ou na governança).

### Passo 7. Entregar
Mostre a tabela, os totais e os destaques (seção 6). Peça ao advogado que valide. A classificação é sempre uma proposta: quem decide é ele.

## 4. Exemplos resolvidos

**Data-limite de prazo processual.** Existe regra, mas há feriado local, suspensão e prazo em dobro. O erro é gravíssimo e quem responde é o advogado. Sigla **A**: a IA sugere a data e mostra a conta, uma pessoa confere. Continua A mesmo depois de meses acertando.

**Renomear e arquivar documento recebido.** Regra clara (padrão de nomes), volume alto, erro barato e percebido logo. Sigla **S**, desde que em conta profissional.

**Atualização de andamento para o cliente** (exemplo de escritório previdenciário com 5 pessoas):

| Passo | Volume/mês | Regra | Risco | Sensível | Sigla |
|---|---|---|---|---|---|
| Conferir movimentações do dia | 400 | Sim | Baixo | Às vezes | S |
| Escrever a atualização ao cliente | 60 | Parcial | Médio | Às vezes (perícia) | A |
| Responder dúvida no WhatsApp | 240 | Parcial | Médio | Às vezes | A |
| Montar o resumo mensal ao cliente | 120 | Sim | Baixo | Não | A (vai para o cliente: pela árvore, o que sai do escritório é A; a conferência pode ser por amostra) |
| Pedir documento pendente | 30 | Sim | Baixo | Não | S |
| Dar notícia desfavorável | 4 | Não | Alto | Às vezes | H |

**Petição inicial previdenciária** (sigla e nível possível): conferir documentação contra o checklist, S, nível 3 a 4 · montar a linha do tempo de vínculos e contribuições, A, nível 3 · escolher tese e pedido, H · rascunhar a minuta, A, nível 2 a 3 · conferir citações, jurisprudência e cálculos, A, nível 3 (a conferência na fonte é da pessoa) · revisão final e assinatura, H · registrar o protocolo, S, nível 4.

## 5. Trava por estágio

A sigla depende do estágio do escritório. Um passo que seria S num escritório organizado pode precisar ser A hoje.

| Situação do escritório | Efeito na sigla |
|---|---|
| Sem conta profissional ou sem regra de uso de IA escrita | Nenhum passo com dado de cliente fica S. Sobe para A até a regra existir e a conta estar conferida. |
| Sem os critérios escritos que o passo usa (ex.: lista do que é movimentação relevante) | O passo que dependeria desses critérios fica A. Anote o critério que falta: ele vai para a base de conhecimento. |
| Sem base de conhecimento do setor | Passos de redação ficam A, nunca S, e o nível máximo é 2. |
| Dado sensível no passo | Pode ser S ou A, mas exige conta profissional, anonimização quando couber e revisão humana. Anote ao lado da sigla, porque vira regra no POP. |

**Regra de ouro:** na dúvida entre duas siglas, fique com a mais humana. H antes de A, A antes de S. Descer de sigla se decide com o tempo, olhando o indicador e os erros que a revisão pegou. Subir depois de um erro com cliente custa mais caro.

## 6. O que entrega

**Tabela principal:**

| Passo (verbo + objeto) | Sigla | Justificativa (uma linha) | Cuidado obrigatório | Nível hoje | Nível possível | O que falta para subir |
|---|---|---|---|---|---|---|

**Depois da tabela:**
- Total de passos e de horas por semana (quando houver horas) em S, em A e em H.
- **Potencial de IA do setor** (1 a 5), pela parte das horas em S ou A: 1 menos de 20%, 2 de 20% a 40%, 3 de 40% a 60%, 4 de 60% a 80%, 5 mais de 80%.
- Os dois ou três passos com mais horas economizáveis e menor risco: os melhores candidatos para começar.
- A lista do que a IA vai precisar consultar (critérios, modelos, checklists). Ela alimenta a `montar-base`.
- As perguntas que ficaram como `[A CONFIRMAR]`.

**Onde grava:** a classificação entra no arquivo que originou a lista. Se veio do mapeamento, em `escritorio/02-mapa/atividades-<setor>.md`. Se veio de um POP, no próprio POP em `escritorio/03-pops/<setor>/`. Mostre antes de gravar.

## 7. Trilha solo e trilha equipe

- **Solo:** a mesma pessoa executa, confere e decide. Isso empurra para S, porque revisar tudo sozinho cansa. Não ceda: mantenha a sigla pelo critério e proponha conferência em outro momento do dia, um checklist curto de revisão e a IA como segundo olhar. A sigla não muda por falta de gente.
- **Equipe:** indique, para cada passo, quem executa e quem confere (por função). Se o mesmo nome aparecer em todos os passos, aponte: ali está o gargalo do setor.

## 8. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Quase tudo S | A equipe para de olhar e o erro aparece no cliente | Árvore de decisão e sigla mais humana na dúvida |
| Volume alto vira desculpa | Passo da linha vermelha automatizado | "Volume alto não tira o passo da linha vermelha" |
| Revisão-carimbo | Aprova sem ler por causa da fila | Cada passo A diz o que a pessoa confere |
| Sigla sem estágio | S num escritório sem conta profissional | Trava por estágio |

## 9. Próximo passo

- Se a lista veio do mapeamento: volte ao `mapear-setores` para fechar o ranking com o potencial de IA.
- Se veio de um POP: siga no `escrever-pop` para completar os campos e o fluxograma.
- Se o objetivo é automatizar: `desenhar-automacao`, que começa pelo checklist de prontidão.
