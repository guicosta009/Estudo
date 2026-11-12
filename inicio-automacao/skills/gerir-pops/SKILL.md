---
name: gerir-pops
description: >
  Organiza, documenta e guarda os POPs do escritório: monta e mantém o mapa de POPs, dá
  código e nome padrão (POP-PEC-01 Petição inicial v1.0), define o dono, publica a versão
  vigente e arquiva a anterior, troca o arquivo no Projeto no Claude, conduz a revisão de 20
  minutos quando um gatilho dispara, aposenta POP com motivo, mostra em que degrau cada POP
  está e prepara a implantação com a equipe. Use quando o advogado disser "mapa de POPs",
  "qual versão está valendo?", "numerar os POPs", "quem é o dono desse POP", "publicar o
  POP", "subir a versão", "trocar o POP no Projeto", "revisar o POP depois do erro", "mudou a
  ferramenta, e o POP?", "aposentar esse POP", "a equipe não segue o POP", "treinar a equipe
  no POP". Não use para escrever o POP (use escrever-pop), para testá-lo (use testar-pop) nem
  para os rituais do escritório inteiro (use revisao-periodica).
---

# Gerir os POPs

> Cuida da vida de cada POP e do conjunto de POPs: um código, um dono, uma versão vigente, um lugar. Escrever o POP é o começo. O que faz ele continuar valendo é o sistema em volta.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Código, versão, status, dono, mapa de POPs e os seis degraus: `../../docs/glossario.md`. Pasta, nomes de arquivo e siglas de setor: `../../docs/pasta-do-escritorio.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

A cena que esta skill evita: o passo a passo da petição inicial foi escrito com cuidado, salvo como "POP_peticao_inicial_FINAL_revisado2.docx" numa pasta que ninguém abre. Seis meses depois, a estagiária nova aprende com a colega do lado, o modelo mudou duas vezes e o documento continua lá, desatualizado. Com a IA no fluxo, o problema cresce: os passos S e A dependem do prompt e da ferramenta, que mudam muito mais rápido do que a lei. POP com IA envelhece mais rápido do que POP sem IA.

## 1. Quando usar

**Use quando:**
- O escritório tem POPs (ou checklists e passo a passo soltos) e ninguém sabe dizer quais existem, qual versão vale e de quem é cada um: montar o mapa.
- Um POP acabou de sair do `escrever-pop` ou do `testar-pop` e precisa de código, nome padrão, dono, aprovação e publicação.
- Uma versão nova foi aprovada e é preciso arquivar a anterior e trocar o arquivo no Projeto no Claude.
- Um gatilho disparou: erro, ferramenta nova, lei nova, gente nova, equipe pulando passo, data de revisão vencida.
- Um POP deixou de servir e precisa ser aposentado.
- O advogado quer saber em que degrau cada POP está (pasta, Projeto, skill, automação) e qual o próximo.
- A equipe não segue o POP, ou vai começar a seguir uma versão nova.

**Não use quando:**
- O POP ainda não existe ou precisa ser reescrito por inteiro: use `escrever-pop`. Desenhar o fluxo antes de escrever: `desenhar-fluxograma`.
- O pedido é testar o POP (checklist de qualidade, teste de mesa, teste com a IA, piloto): use `testar-pop`.
- O pedido é a revisão semanal, mensal ou trimestral do escritório inteiro, o calendário de rituais ou a regra para mudar uma sigla com dados: use `revisao-periodica`. Ela chama esta skill para cada POP que precisa mudar.
- O pedido é organizar os modelos e checklists que o POP cita: use `montar-base`.

## 2. Antes de começar

1. **Leia o perfil.** `escritorio/perfil.md` diz a trilha, o porte, as áreas, o tipo de conta de IA e o setor-alvo. Leia também, se existirem, o código do escritório e a regra de uso de IA em `escritorio/01-cultura/`. Sem perfil, ofereça `/inicio-automacao:comecar` ou faça o modo rápido das regras transversais (três perguntas, uma por vez).
2. **Leia o que já existe:** `escritorio/03-pops/00-mapa-de-pops.md`, todos os `pop-*.md` em `escritorio/03-pops/<setor>/`, os arquivos `revisoes-*.md`, a pasta `testes/` de cada setor, `escritorio/02-mapa/ranking-de-setores.md`, `escritorio/04-base/INDICE.md` e as fichas em `escritorio/05-automacoes/*/ficha.md`. Pergunte só o que não estiver nos arquivos.
3. **Portão:** precisa existir pelo menos um POP escrito ou uma lista de processos que o escritório faz. Se não houver nada, explique em uma frase ("o mapa organiza POPs; sem nenhum, a gente começa escrevendo o do setor-alvo") e ofereça o `escrever-pop`. Se o advogado quiser só a lista de processos, monte o mapa com todas as linhas em Rascunho ou sem POP e registre em "Etapas puladas".
4. **Escolha a rotina.** Pergunte: "O que a gente faz hoje: (1) montar o mapa de POPs, (2) padronizar um POP (código, nome, cabeçalho), (3) publicar uma versão, (4) revisar um POP porque algo mudou, (5) aposentar um POP, (6) olhar o conjunto e a escada, ou (7) preparar a equipe para usar um POP?" Se o advogado não souber, comece pela 6: ela mostra o que está vencido e sugere a rotina.

## 3. Fluxo

### Rotina 1. Montar o mapa de POPs (primeira vez)

1. **Junte o que existe.** Liste o que está na pasta. Depois pergunte, uma por vez:
   - "Além do que está aqui, que POPs, checklists ou passo a passo existem em outro lugar? Drive, sistema, papel, mensagem fixada no grupo. Pode colar só os nomes dos arquivos."
   - "E quais processos a equipe faz de cabeça, sem nada escrito?"
2. **Agrupe por setor** (os 10 setores do glossário) e aponte o que parece ser o mesmo processo em arquivos diferentes. Para cada grupo duplicado, pergunte: "Destes arquivos, qual é o que a equipe segue hoje?" Nome de arquivo ambíguo: pergunte, não deduza.
3. **Proponha código e nome** de cada POP pelo padrão da seção 5. Numere na ordem em que os POPs aparecem no setor, começando em 01.
4. **Proponha o status** de cada um com uma linha de justificativa (seção 4). Se não der para saber, escreva `[A CONFIRMAR]`.
5. **Pergunte o dono, POP por POP:** "Quem é o dono do POP-[SIGLA]-[NN]? Uma pessoa só." Nunca invente nome. No solo, confirme uma vez que o titular é dono de todos.
6. **Marque a próxima revisão.** Sugestão de ponto de partida: 90 dias depois da vigência para POP com passo S ou A, 6 meses para POP só com H. Rascunho e Em teste: "após o teste". Confirme com o advogado; o que ele não decidir fica `[A DEFINIR]`.
7. **Descubra o degrau** de cada POP (seção 9). Leia as fichas de automação e pergunte o que não estiver nelas: "Esse POP está como arquivo num Projeto no Claude? Virou skill? Roda a partir de um gatilho?"
8. **Mostre as lacunas:** setores do ranking sem nenhum POP e processos feitos de cabeça. Termine com a ordem sugerida para escrever ou revisar, começando pelo setor-alvo.
9. **Mostre o mapa** (modelo em `assets/mapa-de-pops-modelo.md`; exemplo preenchido em `references/exemplo-mapa.md`), peça ajustes e grave depois do ok. Pergunte: "Quer também a versão para colar numa planilha?" Se sim, grave o `.tsv`.
10. **Arquivos fora do padrão:** se houver POP com nome antigo (`pop-<processo>.md`, "FINAL", "v3"), siga para a rotina 2.

### Rotina 2. Padronizar um POP

1. **Código.** O próximo número livre do setor sai do mapa. Número nunca é reaproveitado, nem de POP aposentado.
2. **Nome do arquivo.** `escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md`, sem versão e sem "final" no nome. Antes de renomear, procure o nome antigo dentro de `escritorio/` (índice da base, fichas de automação, linha de base, auditorias) e mostre a lista do que será atualizado junto. Renomeie e atualize só depois do ok.
3. **Cabeçalho.** Confira a linha de cabeçalho do modelo do `escrever-pop` (código, nome, setor, área, versão, atualizado em, dono, status, próxima revisão) e acrescente a segunda linha de `assets/cabecalho-e-registro.md`: aprovado por, vigente desde, substitui, passos com IA, onde está a vigente e o aviso "Se você está lendo uma versão diferente desta em outro lugar, ela está desatualizada."
4. **Registro de mudanças.** A seção "Controle de versões" do POP ganha as colunas "Por quê" e "Equipe avisada ou treinada em", e logo abaixo as "Anotações de uso". Se o POP não tinha histórico, a primeira linha é a versão atual, com o que se souber e `[A CONFIRMAR]` no resto.
5. **Passos com IA.** Liste os números dos passos S e dos passos A ("S: 2, 4 · A: 3, 5, 6"). O mesmo texto vai ao mapa.
6. **Passo de IA escrito pelo resultado.** Procure passos que descrevem a ferramenta ("clicar no botão", "colar o prompt 7", "abrir a aba"). Proponha reescrever pelo resultado e pelo critério de conferência (seção 8). O texto do prompt vai para a instrução do passo, se houver automação (`escritorio/05-automacoes/<nome>/instrucoes/`), ou para um anexo no fim do POP, com a mesma versão.
7. **Tamanho.** Mais de 12 passos, ou um POP que ninguém consegue seguir com o cliente esperando no telefone: sugira separar em dois e ofereça o `escrever-pop`.
8. **Mostre o POP padronizado,** com cada mudança marcada `[ALTERADO]` ou `[NOVO]`, e grave depois do ok. Padronizar não muda a versão quando só o cabeçalho e o nome mudaram; anote no registro como "padronização, sem mudança de conteúdo".

### Rotina 3. Publicar a versão vigente

**Portão:** a versão precisa ter passado pelo `testar-pop` (resultado em `escritorio/03-pops/<setor>/testes/`). Se não passou, explique: "Publicar sem teste é colocar a equipe e a IA para seguir um roteiro que ninguém rodou." Ofereça o `testar-pop`. Se o advogado quiser publicar mesmo assim, siga, escreva "publicado sem teste" na Observação do mapa e registre em "Etapas puladas" do perfil.

1. **Aprovação.** Pergunte: "Quem aprova esta versão?" Na equipe, o titular ou o sócio responsável pelo setor. Se o POP tem dado sensível (saúde, criança ou adolescente, dado financeiro), o guardião de dados também lê antes. No solo, o titular aprova depois de uma pausa de 24 horas, por escrito. A IA nunca preenche "Aprovado por" sozinha: ela pergunta o nome e confirma.
2. **Número da versão.** Primeira versão aprovada é sempre 1.0. Nas seguintes, aplique a tabela da seção 5 e diga ao advogado por que sobe o decimal ou o inteiro.
3. **Arquivar a anterior.** Copie a vigente atual para `escritorio/03-pops/<setor>/_arquivo/pop-<sigla>-<nn>-<processo>-v<X-Y>.md` (ponto vira hífen: v1.2 vira `-v1-2`) e escreva no topo da cópia: "VERSÃO SUBSTITUÍDA pela v[NOVA] em [DATA]. Não usar." Só depois grave a nova no caminho principal, com status Vigente, vigente desde, substitui e próxima revisão. Em `escritorio/03-pops/<setor>/` existe um arquivo por código, nunca dois.
4. **Modelos e anexos.** Liste os documentos da base que o POP cita (no `INDICE.md`, coluna "Usado por"). Se a versão nova manda usar um modelo novo, o antigo sai do caminho no mesmo dia (manutenção da `montar-base`). Atualizar o POP e esquecer o modelo é o erro mais comum: metade da equipe abre o antigo.
5. **Projeto no Claude.** Entregue ao advogado o roteiro de troca da seção 7, preenchido com os nomes dos arquivos.
6. **Skill e automação.** Se o POP está no degrau 4 ou acima, a skill precisa de versão nova pelo `pop-para-skill`, e a ficha da automação passa a apontar a versão nova do POP. A skill antiga é desinstalada no mesmo dia.
7. **Implantação.** Primeira versão ou mudança de inteiro: rotina 7 (treino e data de virada). Mudança de decimal: entregue a mensagem curta para a equipe (o que mudou, a partir de quando, abrir conversa nova no Projeto).
8. **Registros.** Linha nova no registro de mudanças do POP, linha atualizada no mapa (versão, vigente desde, próxima revisão, status, degrau) e, se for o POP do setor-alvo, uma linha em "Histórico" do `perfil.md`.

### Rotina 4. Revisar um POP (20 minutos)

1. Pergunte: "O que disparou a revisão: ferramenta ou IA mudou, lei ou regra mudou, um erro, gente nova no setor, equipe pulando passo, ou a data chegou?" Prepare a revisão pelo gatilho (seção 8). O passo a passo da revisão pós-erro e da revisão por mudança de ferramenta está em `references/revisao-por-gatilho.md`.
2. **Marque o POP como Em revisão** no mapa e no cabeçalho. A versão vigente continua valendo até a nova ser aprovada: o setor nunca fica sem POP "porque está sendo atualizado".
3. **Conduza a pauta** de `assets/revisoes-modelo.md`, um bloco por vez, lendo antes as anotações de uso e as perguntas frequentes:
   - O que aconteceu desde a última revisão (3 min).
   - O que mudou em volta: ferramenta, lei, equipe, resultado do caso de teste rodado de novo (5 min).
   - Onde o POP falhou: erros e quase erros, passos pulados, exceções sem escrita (5 min).
   - As siglas ainda valem? (4 min). Subir de sigla (S para A, A para H) é imediato. Descer só na revisão trimestral, pela regra da `revisao-periodica` (seção 9 dela). Aqui se registra a proposta, sem decidir a descida.
   - Decisão (3 min): mantém e atualiza a data; ajuste pequeno (decimal, aviso); mudança de execução (inteiro, novo treino); aposenta (rotina 5).
4. **Passou de 20 minutos?** Encerre, mantenha Em revisão e combine uma sessão de trabalho separada com quem executa (`escrever-pop`, entrada "reescrever um POP antigo").
5. **Rascunho da versão nova.** Enquanto a vigente vale, o rascunho fica em `escritorio/03-pops/<setor>/_em-construcao/pop-<sigla>-<nn>-<processo>-v<X-Y>.md`, nunca no caminho principal. Mudança de inteiro que mexe em passo S ou A roda o caso de teste guardado (`testar-pop`) antes de publicar. Depois, rotina 3.
6. **Grave a ata** em `escritorio/03-pops/<setor>/revisoes-<sigla>-<nn>.md` (a mais recente no topo), com quem faz a alteração, até quando e a próxima revisão.
7. **Erro grave:** se o erro expôs dado de cliente, perdeu ou arriscou prazo ou levou informação errada ao cliente, ele vai também ao guardião e ao livro de incidentes (`escritorio/06-medicao/incidentes.md`, pela `regra-de-uso-de-ia`). Todo erro termina com o POP alterado.

### Rotina 5. Aposentar um POP

1. Pergunte: "Por que esse POP sai? A tarefa deixou de existir, foi absorvida por outro POP (qual?), foi trocada por uma automação com POP próprio, ou outro motivo?"
2. **Confira o que depende dele:** automação ou skill que segue o POP (`05-automacoes/`), documentos da base usados só por ele (`INDICE.md`), Projeto no Claude. Mostre a lista. Documento da base que perde o uso vai para a triagem da `montar-base`.
3. **Mova o arquivo** para `_arquivo/pop-<sigla>-<nn>-<processo>-v<X-Y>.md`, com status Aposentado e o motivo no topo. Nenhum lugar ativo fica com a versão antiga.
4. **Tire do Projeto e da conta:** o arquivo sai do Projeto no Claude e a skill, se houver, é desinstalada (`pop-para-skill`).
5. **Mapa:** a linha continua, com status Aposentado e, na Observação, o motivo e o código que substitui. É isso que impede alguém de recriar a mesma coisa daqui a um ano. O número não volta a ser usado.
6. **Registro e aviso:** uma entrada no `revisoes-<sigla>-<nn>.md` e a mensagem curta para a equipe, com o modelo antigo fora do alcance no mesmo dia.

### Rotina 6. Olhar o conjunto e a escada

1. Leia o mapa e os arquivos e confira, nesta ordem:
   - Revisão vencida ou sem data.
   - POP sem dono, ou dono que saiu do escritório, mudou de setor ou está em férias longas.
   - Pessoa dona de mais de quatro ou cinco POPs vigentes (costuma deixar algum para trás).
   - Mapa e arquivo discordando (o mapa diz v1.2 e o cabeçalho diz v1.1) ou dois arquivos com o mesmo código fora do `_arquivo/`.
   - Em revisão parado ou rascunho parado há mais de [sugestão: 30 dias] `[A DEFINIR]`.
   - POP vigente que não está no Projeto do setor, ou Projeto com versão antiga (pergunte).
   - Setor do ranking sem nenhuma linha no mapa.
2. Para cada achado, diga qual causa de "POP que morre na gaveta" ele mostra (seção 6) e qual rotina resolve.
3. **Mostre a escada:** cada POP vigente com o degrau atual e o próximo passo (seção 9).
4. Recomende no máximo duas ações, com a rotina ou a skill de cada uma. Não altere nada nesta rotina sem passar pela rotina correspondente.

### Rotina 7. Colocar a equipe para usar (plano de adoção)

Mandar o POP no grupo e escrever "a partir de agora é assim" tem o mesmo efeito de não mandar. O roteiro cabe em uma semana. Modelo para preencher em `assets/implantacao-modelo.md`; detalhe, mensagens prontas e a versão solo em `references/adocao-pela-equipe.md`.

1. **Apresentação (15 minutos):** o problema que o POP resolve, com exemplo anonimizado; no máximo três mudanças em relação a hoje; os passos S e A e o que a pessoa confere em cada um; os passos H e por quê; onde está a vigente.
2. **Treino (30 a 45 minutos):** cada pessoa executa o POP inteiro num caso fictício, inclusive os passos com IA, na conta profissional do escritório. O dono anota onde travaram. Nunca caso de cliente real no treino.
3. **Primeira execução acompanhada:** no primeiro caso real de cada pessoa, o dono senta junto ou confere logo depois. Atenção dobrada aos passos de revisão humana.
4. **Perguntas frequentes:** toda dúvida do treino e da primeira semana vira uma linha. A pergunta que aparece três vezes entra no POP na próxima versão.
5. **Data de virada:** o dia a partir do qual o jeito antigo deixa de valer. No mesmo dia, modelo antigo e prompt antigo saem do alcance e a versão antiga sai do Projeto.
6. **Duas semanas de acompanhamento:** na reunião semanal do núcleo, três perguntas (alguém pulou passo? alguém voltou ao jeito antigo? que dúvida apareceu?). As respostas vão para as anotações de uso.

**Quem continua no jeito antigo.** Antes de cobrar, descubra o motivo, porque cada um pede uma resposta diferente: (1) o POP não cobre o caso dela: agradeça e registre a exceção; (2) ela não aprendeu direito: refaça o treino com ela, sozinha, num caso fictício; (3) ela acha o jeito antigo melhor: meça os dois lado a lado em dois ou três casos, contando tempo e erros, e o POP muda se o antigo ganhar; (4) é hábito: tire o caminho antigo do alcance. Se nada resolver, a conversa sobe para o titular, em particular, com combinado escrito. Os medos por trás da resistência estão na `implantar-a-mudanca`. Se o titular pula o POP, a equipe entende que o POP é opcional.

## 4. Ciclo de vida e os cinco status

Todo POP passa por sete etapas: **rascunho** (v0.x, escrito pelo dono com quem executa, a partir do fluxograma), **teste** (`testar-pop`, ainda v0.x), **aprovação** (vira 1.0, com nome e data), **implantação** (treino e data de virada), **uso** (o dono anota os sinais), **revisão** (por gatilho ou data; vira 1.1 ou 2.0) e **aposentadoria**.

| Status | Etapas | Pode usar com cliente? | Onde fica o arquivo | No Projeto no Claude |
|---|---|---|---|---|
| Rascunho | Rascunho | Não | Primeira versão: caminho principal, com o status no cabeçalho. Versão nova de POP vigente: `_em-construcao/` | Não |
| Em teste | Teste | Só nos casos do teste, com revisão humana de tudo | Igual ao Rascunho; resultados em `testes/` | Não. Teste com a IA, só em Projeto de teste separado, com nome que deixe isso claro |
| Vigente | Aprovação, implantação e uso | Sim, seguindo o POP | Caminho principal | Sim, só esta versão |
| Em revisão | Revisão | Sim: a vigente vale até a nova ser aprovada | Vigente no caminho principal; rascunho da nova em `_em-construcao/` | A vigente, até a troca |
| Aposentado | Aposentadoria | Não | `_arquivo/` | Não |

Na pasta aberta (Claude Code ou ambiente que lê `escritorio/`), o Claude segue só POP com status Vigente ou Em revisão e ignora `_arquivo/` e `_em-construcao/`. Na primeira vez que montar o mapa, proponha acrescentar essa frase às regras fixas do `escritorio/CLAUDE.md` e grave só com o ok.

## 5. Código, nome e versão

**Padrão:** `POP` + sigla do setor + número de dois dígitos + nome curto + versão. Exibição: **POP-PEC-01 Petição inicial v1.0**. Arquivo: `pop-pec-01-peticao-inicial.md`, com a versão só no cabeçalho e no registro.

| Setor | Sigla | Pasta | Exemplo |
|---|---|---|---|
| Atendimento e triagem | ATD | `atendimento-e-triagem` | POP-ATD-01 Triagem no WhatsApp v1.0 |
| Comercial | COM | `comercial` | POP-COM-01 Proposta de honorários v1.0 |
| Produção de peças | PEC | `producao-de-pecas` | POP-PEC-01 Petição inicial v1.2 |
| Prazos e controladoria | PRZ | `prazos-e-controladoria` | POP-PRZ-01 Leitura de publicações v2.0 |
| Audiências e diligências | AUD | `audiencias-e-diligencias` | POP-AUD-01 Preparação de audiência v1.0 |
| Financeiro e cobrança | FIN | `financeiro-e-cobranca` | POP-FIN-01 Cobrança de honorários v1.1 |
| Relacionamento com o cliente | REL | `relacionamento-com-o-cliente` | POP-REL-01 Andamento no WhatsApp v1.0 |
| Marketing e conteúdo | MKT | `marketing-e-conteudo` | POP-MKT-01 Post semanal v1.0 |
| Gestão de equipe | EQP | `gestao-de-equipe` | POP-EQP-01 Integração de novo membro v1.0 |
| Administrativo | ADM | `administrativo` | POP-ADM-01 Arquivo digital do cliente v1.0 |

POPs por área dentro do mesmo setor: a área entra no nome curto e a sigla do setor fica (POP-PEC-02 Inicial previdenciária v1.0; arquivo `pop-pec-02-inicial-previdenciaria.md`).

**O que muda a versão.** Regra prática: se a equipe precisa ser treinada de novo, sobe o inteiro; se basta avisar, sobe o decimal. Rascunho e teste usam 0.1, 0.2; a primeira aprovada é sempre 1.0.

| Tipo de mudança | Exemplo | De 1.2 vai para |
|---|---|---|
| Texto, link ou exemplo | Redação confusa corrigida, link do modelo trocado, nome de pasta atualizado | 1.3 |
| Prompt ajustado sem mudar a saída | A instrução do passo A ganhou "não repetir a qualificação das partes"; o resultado esperado é o mesmo | 1.3 |
| Prazo interno ajustado | Prazo de resposta revisto, sem mudar quem faz o quê | 1.3 (2.0 se a equipe precisar ser treinada) |
| Exceção nova | Entrou "cliente menor de idade", com o que fazer | 1.3, ou 2.0 se mudar o fluxo |
| Passo novo ou removido | Entrou a conferência de citações na fonte oficial antes do protocolo | 2.0 |
| Troca de sigla | Um A virou S, ou um S voltou para A depois de um erro | 2.0 |
| Troca de responsável ou de gatilho | A conferência do prazo passou da estagiária para a controladoria | 2.0 |
| Troca de ferramenta ou de ambiente de IA | O rascunho saiu de uma conta pessoal e foi para o Projeto da conta profissional | 2.0 |
| Lei, regra de tribunal ou sistema de peticionamento | Mudou um requisito da peça | 2.0 |

## 6. O dono do POP

Cada POP tem um dono, e só um. Muita gente executa e opina; uma pessoa com nome responde por ele estar escrito, certo, treinado e atualizado.

**O que o dono faz:** escreve ou conduz a escrita com quem executa; leva para aprovação e registra quem aprovou; treina na implantação e acompanha a primeira execução; responde às dúvidas e mantém as perguntas frequentes; anota os sinais de uso; conduz a revisão; troca o arquivo na pasta e no Projeto; avisa quem mantém o mapa.

**O que o dono não precisa fazer:** executar a tarefa todo dia (pode ser quem supervisiona); decidir sozinho (a aprovação é do titular ou do sócio do setor); saber mexer em ferramenta (o responsável pela inovação ajuda); ser dono de tudo.

| Papel | Responde por | Onde aparece |
|---|---|---|
| Dono do setor | O setor inteiro: horas, incômodo, pessoas, resultado | Mapa de setores (`mapear-setores`) |
| Dono do POP | Um processo do setor escrito, certo, treinado e atualizado | Cabeçalho do POP e mapa de POPs |
| Responsável pela inovação | O sistema: mapa em dia, revisões acontecendo, Projeto organizado | Núcleo (`nucleo-de-inovacao`) |

**Como escolher:** quem conhece a tarefa de perto (quem só "sabe como deveria ser" escreve o POP do mundo ideal); quem tem cuidado com detalhe; quem a equipe escuta; com tempo reservado (sugestão de ponto de partida: uma hora por mês por POP vigente, mais a implantação quando a versão muda). Combinado falado não vale: o nome vai no cabeçalho e no mapa.

**Por que um POP morre na gaveta** (é a lista que a rotina 6 usa): ninguém é dono; ninguém sabe qual versão vale; ele mora longe do trabalho; a equipe nunca foi treinada; nunca foi revisado depois de um erro; é longo demais para seguir com o cliente esperando.

## 7. O POP dentro do Projeto no Claude

No Projeto, o POP é lido toda vez que a IA trabalha naquele setor. Versão errada ali faz estrago rápido: duas versões no mesmo Projeto fazem a IA misturar passos. A montagem do Projeto está na `montar-base` (seção 8 dela); aqui fica a troca de versão. A instrução do Projeto cita o código (POP-PEC-01) sem o número da versão, para não precisar ser reescrita a cada 1.x.

**A troca, nesta ordem e no mesmo dia** (a skill entrega a lista preenchida; quem mexe no Projeto é a pessoa):
1. Aprovar a versão nova antes de mexer no Projeto. Rascunho em teste nunca entra no Projeto da equipe.
2. Trocar na pasta: nova no caminho principal, antiga em `_arquivo/`. Conferir que existe um arquivo só por código.
3. Remover a versão antiga do Projeto e subir a nova, no mesmo momento. As duas nunca convivem, nem por um dia.
4. Conferir as instruções do Projeto e os outros arquivos: alguma instrução descreve um passo que mudou? Algum modelo citado mudou?
5. Abrir uma conversa nova e rodar o caso de teste. Perguntar: "Qual versão do POP-[SIGLA]-[NN] você está seguindo?" Se a resposta for a antiga, algo ficou para trás.
6. Avisar a equipe: o que mudou, a partir de quando, e o pedido para abrir conversa nova no Projeto.
7. Atualizar o mapa e o registro de mudanças, com a data em que a equipe foi avisada.

Os recursos do Projeto variam conforme o plano: conferir na configuração da conta. O POP e os modelos do Projeto não levam nome, documento, número de processo ou dado de saúde de cliente; exemplos são fictícios ou anonimizados.

## 8. Gatilhos de revisão

| Gatilho | Como aparece | O que fazer | Quando |
|---|---|---|---|
| Mudou a ferramenta ou a IA | Troca de plano ou de ferramenta, IA respondendo diferente, recurso novo que se quer usar | Rodar o caso de teste guardado com a configuração nova e comparar; revisar os passos S e A | Antes de usar com cliente |
| Mudou a lei ou a regra | Lei nova, entendimento que muda a peça, regra de tribunal ou de órgão, sistema de peticionamento | Revisar passos e modelos afetados; atualizar a base junto (`montar-base`) | Antes da próxima peça afetada |
| Erro recorrente | O mesmo erro duas vezes em pouco tempo, ou um erro grave uma vez (prazo, dado exposto, informação errada ao cliente) | Revisão pós-erro, sem caça a culpado; todo erro termina com o POP alterado | Na mesma semana |
| Gente nova | Chegou estagiário, colaborador ou advogado no setor | A pessoa executa só com o POP na mão e anota cada dúvida. Cada dúvida é um furo do POP, e a culpa nunca é dela | Na primeira semana dela |
| Desvio da equipe | Gente pulando passo ou voltando ao jeito antigo | Descobrir o motivo (rotina 7); se o problema for o POP, revisar | Na reunião semanal |
| Data marcada | Nenhum gatilho desde a última revisão | Mesma pauta de 20 minutos | Sugestão: 90 dias para POP com S ou A; 6 meses para POP só com H |

**Escreva o passo de IA pelo resultado.** "Clicar no botão tal e colar o prompt 7" quebra na primeira atualização da ferramenta. "A IA entrega o resumo dos fatos em tópicos, com datas, no formato da ficha padrão, e quem executa confere as datas com os documentos" sobrevive a qualquer troca. Quando a ferramenta muda, ajusta-se o anexo ou a instrução e roda-se o caso de teste: se a saída continua igual, sobe só o decimal.

**O caso de teste guardado.** Um ou dois casos fictícios ou anonimizados, com o resultado que o escritório considera bom, guardados pelo `testar-pop` (ou em `04-base/casos-de-teste/`, quando há automação). A cada mudança de ferramenta ou de prompt, roda-se o mesmo caso e compara-se. É o jeito mais barato de saber se a IA nova piorou alguma coisa antes que o cliente perceba.

## 9. A escada: do POP à IA

Cada POP vigente está num degrau (definições no glossário). A coluna Degrau do mapa guarda o número; a rotina 6 mostra o próximo passo.

| Degrau | Como saber que o POP está nele | Próximo passo | Skill |
|---|---|---|---|
| 1. Prompt solto | O processo não tem POP vigente (sem POP, rascunho ou em teste) | Escrever o POP ou terminar o teste | `escrever-pop`, `testar-pop` |
| 2. POP escrito e guardado | Vigente na pasta, com código, versão e dono | Colocar no Projeto do setor, com o código do escritório e a base que ele cita | `montar-base` (Projeto e base), `codigo-do-escritorio` (instruções) |
| 3. Projeto no Claude | A vigente é arquivo de conhecimento do Projeto do setor | Desenhar a automação (prontidão e instrução por passo) e gerar a skill no nível 3 | `desenhar-automacao`, depois `pop-para-skill` |
| 4. Habilidade do POP | Skill gerada a partir do POP e instalada | Rodar à mão, medir e, cumpridos os critérios do nível 4, preparar o disparo | `medir-retorno`, `desenhar-automacao`, `pop-para-skill` |
| 5. Plugin do escritório | Duas ou mais skills do escritório distribuídas juntas, na mesma versão, para todos | Manter versão única para a equipe (conferir na configuração da conta) | `pop-para-skill` (instalação e distribuição) |
| 6. Automação | Roda a partir do gatilho, com fila e revisão humana nos pontos fixos | Medir e manter as revisões | `medir-retorno`, `revisao-periodica` |

- O degrau 5 é do conjunto: um POP sozinho pode ir do 4 ao 6 quando cumprir os critérios do nível 4 da `desenhar-automacao`.
- Correspondência com os níveis de inserção: degrau 1 e 2, nível 1; degrau 3, nível 2; degrau 4, nível 3; degrau 6, nível 4.
- Só sobe de degrau POP Vigente. Habilidade feita sobre POP que ninguém testou espalha o erro com mais velocidade.
- Por que o POP deixa a IA melhor: sem POP, cada pessoa reexplica o processo a cada conversa, a IA inventa o critério que faltou e ninguém sabe com que regra a resposta foi feita. Com o POP virando habilidade, o roteiro já está pronto, o critério está escrito (onde não está, ela para e pergunta), todos usam a mesma versão, ela para em cada passo A, não toca nos H e mostra a versão do POP em cada uso.

## 10. O que entrega e onde grava

| Entrega | Onde grava |
|---|---|
| Mapa de POPs | `escritorio/03-pops/00-mapa-de-pops.md` |
| Mapa para planilha (opcional) | `escritorio/03-pops/00-mapa-de-pops.tsv` |
| POP vigente, padronizado | `escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md` |
| Rascunho da versão nova de um POP vigente | `escritorio/03-pops/<setor>/_em-construcao/pop-<sigla>-<nn>-<processo>-v<X-Y>.md` |
| Versões substituídas e POPs aposentados | `escritorio/03-pops/<setor>/_arquivo/pop-<sigla>-<nn>-<processo>-v<X-Y>.md` |
| Atas de revisão e registro de aposentadoria | `escritorio/03-pops/<setor>/revisoes-<sigla>-<nn>.md` |
| Roteiro de implantação e perguntas frequentes | `escritorio/03-pops/<setor>/implantacao-<sigla>-<nn>.md` |
| Roteiro de troca no Projeto e mensagens à equipe | No chat, prontos para copiar |
| Progresso | `perfil.md`: linha em "Histórico" a cada publicação ou aposentadoria do POP do setor-alvo |

Colunas do mapa: Setor, Código, POP, Dono, Versão, Vigente desde, Próxima revisão, Status, Passos com IA (S/A), Degrau, Onde está a vigente, Observação. Uma linha por POP, inclusive os aposentados. Datas no formato AAAA-MM-DD.

Mostre cada documento antes de gravar. Sem acesso a arquivos, entregue cada um em bloco pronto para copiar, com o caminho. Se o escritório guarda tudo no Drive ou no OneDrive, diga o equivalente: o mapa na raiz de `01 POPs`, uma subpasta por sigla, e dentro dela a vigente, `_arquivo` e `_em-construcao`. POP nunca fica na conta pessoal de alguém: quando a pessoa sai, o POP sai junto.

## 11. Trilha solo e trilha equipe

**Solo:**
- O titular é dono de todos os POPs. Ninguém vai discutir o POP dele, e é aí que ele envelhece em silêncio. Duas defesas: a data de revisão de cada POP na agenda, tratada como prazo; e a IA como revisora crítica, com a leitura pós-erro de `references/revisao-por-gatilho.md`.
- Se houver secretária ou estagiário, peça que executem uma vez só com o POP na mão e anotem cada dúvida. Cada dúvida é um furo.
- Aprovação: o titular aprova depois de uma pausa de 24 horas, por escrito. Guardião é o próprio titular.
- Implantação em si mesmo: o POP aberto na tela nas primeiras dez execuções, marcando cada passo, e a própria data de virada, apagando o modelo antigo. Se ele continua disponível, a mão volta para ele no primeiro dia de prazo fatal.
- Contratar a primeira pessoa: o POP do setor que ela vai assumir é escrito antes, e ela vira a primeira dona de POP (sequência completa na `revisao-periodica`).

**Equipe:**
- Distribua os POPs, e não só as tarefas: triagem no WhatsApp com quem atende, prazos com a controladoria, peças com o advogado que mais produz. O titular aprova e cobra a data. Quando a equipe é dona do POP, ela defende o POP.
- Quem mantém o mapa é o responsável pela inovação; o dono avisa a cada mudança. Na reunião semanal do núcleo, filtrar "Revisão vencida" e "Sem data".
- Aprovação pelo titular ou sócio do setor; guardião junto quando há dado sensível.
- Saída, troca de função ou férias longas: todo POP da pessoa ganha dono novo antes. Item fixo do desligamento.
- Plano de adoção completo (rotina 7) a cada versão nova de inteiro.

## 12. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| "FINAL_v3_agora_vai" | Ninguém sabe qual vale | Um código, versão no cabeçalho, um arquivo por código |
| Duas versões no Projeto | A IA mistura passos | Troca no mesmo dia, nessa ordem, com a pergunta "qual versão você segue?" |
| POP sem dono | Envelhece sem ninguém notar | Nome no cabeçalho e no mapa, dono novo antes de qualquer saída |
| Implantação "enviada no grupo" | Cada um segue o seu jeito | Apresentação, treino, primeira execução acompanhada e data de virada |
| Erro corrigido na hora e POP igual | O erro volta | Todo erro termina com o POP alterado e a ata gravada |
| Setor sem POP "porque está sendo atualizado" | Cada um improvisa | Status Em revisão: a vigente vale até a nova |
| POP novo, modelo velho | Metade da equipe abre o antigo | Conferência dos documentos que o POP cita a cada versão |
| Aposentado apagado do mapa | Alguém recria a mesma coisa | A linha fica, com motivo e substituto |
| Passo de IA descrito por botão | Quebra na primeira atualização | Passo escrito pelo resultado; prompt em anexo ou instrução |
| Skill sobre POP não testado | O erro se espalha mais rápido | Só sobe de degrau POP Vigente |

## 13. Próximo passo

- POP em Rascunho: `testar-pop`, antes de qualquer publicação.
- POP Vigente no degrau 2 ou 3: `desenhar-automacao`, que começa pelo checklist de prontidão, e depois `pop-para-skill`.
- POP Vigente que já virou skill: `pop-para-skill` para cada versão nova, e `medir-retorno` para o painel.
- Revisão que mostrou que o POP precisa ser reescrito: `escrever-pop`.
- Vários POPs com a mesma sigla para mudar, ou dúvida se um passo pode descer de sigla: `revisao-periodica`.

## Referências desta skill

- `assets/mapa-de-pops-modelo.md`: mapa em branco, versão para planilha e fórmula de alerta. Use na rotina 1.
- `assets/cabecalho-e-registro.md`: segunda linha do cabeçalho, registro de mudanças e anotações de uso. Use na rotina 2.
- `assets/revisoes-modelo.md`: ata da revisão de 20 minutos e registro de aposentadoria. Use nas rotinas 4 e 5.
- `assets/implantacao-modelo.md`: roteiro de implantação e perguntas frequentes. Use na rotina 7.
- `references/exemplo-mapa.md`: mapa preenchido de um escritório fictício, com a leitura dos alertas e da escada. Mostre na rotina 1 se o advogado quiser ver como fica.
- `references/revisao-por-gatilho.md`: revisão pós-erro (sete causas), revisão por mudança de ferramenta e leitura crítica do solo. Leia na rotina 4.
- `references/adocao-pela-equipe.md`: preparação do treino, mensagens prontas, os quatro motivos de quem não segue e a versão solo. Leia na rotina 7.
