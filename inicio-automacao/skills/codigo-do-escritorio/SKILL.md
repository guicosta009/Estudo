---
name: codigo-do-escritorio
description: >
  Escreve, converte e revisa o código do escritório: o documento de 7 seções que registra quem
  somos, como atendemos, como decidimos, o tom de voz, dados e sigilo, o que nunca fazemos e
  como sabemos que foi bem feito. É a régua da IA. Tem três modos: criar (entrevista seção por
  seção), converter em instruções de um Projeto no Claude e revisar todo mês. Use quando o
  advogado disser "escrever o código do escritório", "cultura do escritório", "tom de voz",
  "regras do escritório para a IA", "instruções do Projeto", "revisar o código", "quem decide
  o quê", "retrato cultural", ou quando outra skill precisar da régua. Não use para escrever a
  regra de uso de IA, o acordo da equipe ou o livro de incidentes (use regra-de-uso-de-ia) nem
  para preparar a reunião de lançamento e o piloto (use implantar-a-mudanca).
---

# Código do escritório

> Tira da cabeça do titular o jeito que o escritório trabalha e coloca num papel de 7 seções, com dono, versão e data. Depois converte esse papel em instruções que a IA segue em toda conversa e mantém o texto vivo com uma revisão por mês.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de linha vermelha, S, A, H e níveis: `../../docs/glossario.md`. O que muda entre solo e equipe: `../../docs/trilhas.md`.

Cultura, para este método, é o jeito que o escritório trabalha quando você não está olhando. A IA aprende esse jeito e repete. Se ele não está escrito, cada pessoa usa a IA de um jeito e o escritório vira "quatro escritórios dentro de um". O código é a régua: sem ele, ninguém consegue dizer se a entrega da IA está boa.

## 1. Quando usar

**Use quando:**
- O escritório ainda não tem o código escrito (modo **criar**).
- O código existe e o advogado quer colocá-lo num Projeto no Claude (modo **converter**). Isso leva o escritório ao nível 2 de inserção da IA.
- Passou um mês, ou aconteceu algo que pede revisão fora do calendário (modo **revisar**).
- Outra skill precisa de prazo de resposta, quem decide, tom ou limites e o código não existe: crie pelo menos a versão 0 das seções que ela usa.

**Não use quando:**
- O pedido é a política de uso de IA, o acordo que cada pessoa assina, a tabela de anonimização ou o livro de incidentes: use `regra-de-uso-de-ia`.
- O pedido é preparar a reunião com a equipe, o piloto ou a conversa com quem resiste: use `implantar-a-mudanca`.
- O pedido é escrever como um setor funciona passo a passo: use `escrever-pop`. O código diz a régua; o POP diz o roteiro.

## 2. Antes de começar

1. Leia `escritorio/perfil.md` (trilha, porte, áreas, conta de IA). Sem perfil, faça o modo rápido das regras transversais.
2. Leia, se existirem: `escritorio/01-cultura/codigo-do-escritorio.md`, `escritorio/01-cultura/regra-de-uso-de-ia.md` e o diagnóstico mais recente em `escritorio/diagnosticos/`.
3. **Escolha o modo** pelo que encontrou:
   - Sem código: modo criar.
   - Código existe e não há `instrucoes-do-projeto.md`, ou as instruções têm versão diferente da do código: ofereça o modo converter.
   - Código existe e a última revisão tem mais de um mês, ou o advogado trouxe um erro, uma reclamação, uma pessoa nova ou uma ferramenta nova: ofereça o modo revisar.
   - Na dúvida, pergunte: "Você quer escrever o código do zero, colocar o código num Projeto no Claude ou revisar o que já existe?"
4. **Portão:** nenhum obrigatório. O diagnóstico ajuda (mostra o tema mais fraco), mas o código pode vir antes. Se não houver diagnóstico, diga em uma frase que ele mostra onde o código precisa ser mais firme e ofereça `diagnostico`. Se o advogado seguir, registre em "Etapas puladas".
5. **Se a regra de uso de IA já existir,** a seção 5 (Dados e sigilo) começa por ela. As duas precisam dizer a mesma coisa.

## 3. Fluxo do modo criar

### Passo 1. Oferecer o retrato cultural (opcional)
Pergunte: "Antes de escrever, quer fazer um retrato de 30 minutos de como o escritório funciona hoje? Ele mostra qual seção do código precisa de mais cuidado. Se preferir, vamos direto às 7 seções."
- Se aceitar, siga `references/retrato-cultural.md` (6 temas, checklist de 10 itens, leitura da pontuação e o formulário anônimo para a equipe). Grave o resultado em `escritorio/01-cultura/mudanca/retrato-cultural.md`.
- O tema mais fraco vira prioridade: a seção correspondente do código recebe mais perguntas e mais exemplos.

### Passo 2. Combinar a entrevista
Diga: "Vou passar pelas 7 seções na ordem, uma pergunta por vez. Quando você não souber ou o escritório ainda não tiver decidido, eu marco [A DEFINIR] e a gente segue. Descreva como é hoje, mesmo que não seja o ideal. Melhorar vem depois." Lembre que nenhuma resposta precisa de nome de cliente.

### Passo 3. Entrevistar pelas 7 seções
Siga a seção 4 desta skill. Para cada campo:
- Faça a pergunta-guia, uma por vez.
- Se a resposta vier vaga, peça o exemplo concreto: "E na última vez que isso aconteceu, como foi?". Resposta boa: "na terça, a assistente mandou a minuta e eu reescrevi tudo". Resposta ruim: "a gente delega bem".
- Se a resposta cair no erro comum da seção, mostre o erro com gentileza e pergunte de novo.
- Se faltar decisão, escreva `[A DEFINIR]` no campo e anote a pendência. Se faltar informação que alguém sabe, `[A CONFIRMAR]`.
- Se aparecer dado de cliente, avise, não repita e siga com a versão anonimizada.
- Ao fim de cada seção, mostre o texto dela em poucas linhas e peça ok antes de passar para a próxima.

### Passo 4. Sugerir a linha vermelha na seção 6
Depois dos limites que o advogado trouxe, mostre a linha vermelha do plugin como **sugestão a validar** (texto na seção 4.6). Pergunte se entra como está, com ajustes ou fora. Ela continua valendo em todas as skills do plugin mesmo que o advogado prefira não escrever no código, e você diz isso a ele.

### Passo 5. Montar o documento
Use `assets/codigo-do-escritorio-modelo.md`. Preencha o cabeçalho:
- **Nome** do escritório.
- **Versão:** 0 enquanto houver `[A DEFINIR]` em decisões de prazo, de quem decide ou de dados; 1.0 quando o advogado aprovar sem pendências críticas.
- **Revisado em:** data de hoje.
- **Dono do código:** pergunte "Quem vai cuidar deste documento: receber sugestões, atualizar e avisar a equipe?". Na trilha solo, é o titular.
- No fim, a lista "Pendências para a próxima revisão" com todos os `[A DEFINIR]` e `[A CONFIRMAR]`.

### Passo 6. Conferir tamanho e erros comuns
Antes de mostrar, confira cada seção contra a tabela da seção 4: tamanho, exemplo concreto, número onde se pede número, frase real onde se pede frase. Corte o que for frase de site ou adjetivo solto.

### Passo 7. Mostrar, ajustar, gravar
Mostre o código inteiro. Peça ajustes. Grave só depois do ok (seção 7). Em seguida, ofereça o modo converter: "Quer que eu transforme o código em instruções para um Projeto no Claude? Assim toda conversa lá dentro segue estas regras."

## 4. As 7 seções: perguntas-guia, erro comum e tamanho

| Seção | Campos | Erro comum | Tamanho |
|---|---|---|---|
| 1. Quem somos | Áreas; cliente típico; o que nos diferencia na prática | Frase de site ("excelência e compromisso") | 1 parágrafo |
| 2. Como atendemos | Canais oficiais; horário; prazo de resposta ao cliente ativo; mensagem fora do horário; o que é urgência e para quem vai; quem faz o primeiro contato | "O mais rápido possível", sem número | 5 a 8 linhas |
| 3. Como decidimos | Aceitar caso novo; honorários e descontos; acordo; peça para protocolo; ferramenta nova, inclusive IA | Tudo com o titular por padrão | Lista curta |
| 4. Tom de voz | Tratamento; frases que usamos; frases que nunca usamos; áudio, texto ou ligação | Adjetivos soltos ("acolhedor e profissional") | 4 a 6 exemplos |
| 5. Dados e sigilo | Onde o documento fica; quem tem acesso; conta de IA autorizada; o que retiramos antes da IA; o que nunca vai para a IA | Achar que é só assunto da regra de IA. "O sigilo começa no WhatsApp." | 5 a 8 linhas |
| 6. O que nunca fazemos | Limites éticos e de postura | Copiar o Código de Ética e Disciplina da OAB inteiro | 3 a 6 itens |
| 7. Como sabemos que foi bem feito | Peça; atendimento; entrega | "Peça bem feita" | Critérios por tipo |

### 4.1 Quem somos
1. "Em que áreas o escritório atua hoje? Conte o que de fato entrou nos últimos meses, não o que está no site."
2. "Quem é o cliente típico? Descreva sem nome: situação, região, como chegou até vocês."
3. "O que vocês fazem diferente, na prática? Pense numa coisa que acontece toda semana e que um cliente notaria." Se vier frase de site, peça a cena.

### 4.2 Como atendemos
1. "Por quais canais o cliente fala com o escritório? Qual é o oficial?" Se o canal for o WhatsApp pessoal de alguém, anote: isso volta na seção 5.
2. "Qual é o horário de atendimento?"
3. "Em quanto tempo um cliente com caso em andamento recebe resposta? Quero um número, em horas úteis ou dias." Ajuda dar o formato da resposta-ponte: "recebi, te retorno amanhã até as 12h".
4. "O que acontece com a mensagem que chega às 22h? Existe uma resposta-padrão?"
5. "O que conta como urgência aqui, e para quem ela vai? Me conte a última urgência de verdade."
6. "Quem faz o primeiro contato com quem chega? Existe roteiro?"

### 4.3 Como decidimos
Para cada item, pergunte quem decide e com qual critério:
1. "Quem decide se um caso novo entra? O que faz vocês recusarem um caso?"
2. "Quem pode dar desconto ou sair da tabela de honorários? Até onde?"
3. "Num acordo, quem recomenda e quem decide?"
4. "Quem aprova a peça antes do protocolo?"
5. "Quem aprova uma ferramenta nova, inclusive de IA? Depois de quê: um piloto, a conferência da conta?"
Se tudo cair no titular, pergunte: "Qual foi a última decisão que esperou você sem precisar?". A resposta costuma mostrar o que pode ganhar critério escrito e outro dono.

### 4.4 Tom de voz
1. "Vocês tratam o cliente por você, por senhor ou senhora, ou depende? Depende de quê?"
2. "Copie duas ou três frases que saíram do escritório para clientes nesta semana e que você gostou." Anonimize antes de registrar.
3. "Quais frases você não quer ver saindo do escritório? Pense numa que já saiu e incomodou."
4. "Quando vai áudio, quando vai texto e quando é ligação?"

### 4.5 Dados e sigilo
1. "Um cliente mandou um documento pelo WhatsApp. O que acontece com ele até estar guardado? Ele sai do celular?"
2. "Quem tem acesso a essa pasta? Estagiário, terceiros e correspondentes também?"
3. "Qual conta de IA o escritório usa, e em nome de quem?" Conta pessoal gratuita serve só para teste com dado fictício: diga isso e registre como está hoje.
4. "O que vocês retiram de um documento antes de colar na IA?" Se não houver hábito, proponha a tabela de troca padrão das regras transversais e marque como proposta.
5. "O que nunca vai para a IA?" Proponha o mínimo do plugin: laudo completo, dado de criança ou adolescente e processo em segredo de justiça, nem anonimizados, sem autorização expressa do responsável; senha e credencial nunca.
Se a regra de uso de IA já existe, leia a seção dela e confirme cada campo em vez de perguntar do zero. Se o código e a regra divergirem, mostre a divergência e pergunte qual vale.

### 4.6 O que nunca fazemos
1. "Quais são os três limites que ninguém do escritório cruza, mesmo com o cliente pedindo?" Se vier o Código de Ética inteiro, peça os três que mais aparecem no dia a dia.
2. Depois, a sugestão da linha vermelha, para validar:

> **Sugestão a validar.** Nenhuma IA decide ou executa por nós: escolher a tese ou a estratégia do caso; dar notícia ruim ao cliente (a gente liga); assinar ou assumir responsabilidade técnica; aconselhar cliente em situação de vulnerabilidade (violência doméstica, criança em disputa, doença grave, perda de emprego, idoso sem renda); enviar peça, proposta ou mensagem com conteúdo jurídico sem revisão de uma pessoa.

Se o escritório atua em Família, acrescente à sugestão: "Qualquer sinal de violência, coação ou risco: o advogado assume e nada daquele caso entra em automação."
Para caber em 3 a 6 itens, a linha vermelha entra como um item só.

### 4.7 Como sabemos que foi bem feito
1. "Quando você revisa uma peça, o que você confere, na ordem?"
2. "Como você sabe que um atendimento foi bom? O que o cliente precisa saber quando sai da conversa?"
3. "Quando uma entrega está terminada? Onde fica registrada e com o nome de quem?"
Critério bom é verificável: "cálculos conferidos, citações checadas na fonte, pedido coerente com a causa de pedir". Esses critérios viram as verificações da IA no modo converter.

O exemplo completo de um código preenchido está em `references/exemplo-preenchido.md`. Leia quando o advogado pedir um modelo para se inspirar ou quando uma resposta vier abstrata e você precisar mostrar como fica concreto. Diga sempre que é um exemplo fictício e que o código dele deve ter as frases dele.

## 5. Fluxo do modo converter (instruções do Projeto)

1. Leia o código gravado. Se houver `[A DEFINIR]` em prazo, quem decide ou dados, avise: as instruções vão herdar a lacuna.
2. Escreva as instruções com `assets/instrucoes-do-projeto-modelo.md`, seguindo estes critérios:
   - Segunda pessoa, falando com a IA: "Você trabalha para o escritório...".
   - Blocos curtos: quem é o escritório; como escrever para o cliente (tom, tratamento, frases que usamos e que nunca usamos); regras de dados e sigilo; o que nunca fazer; como saber que o trabalho está bem feito.
   - Cada critério de qualidade da seção 7 vira uma verificação que a IA faz antes de entregar ("Antes de entregar uma minuta, confira se...").
   - Regras fixas, sempre presentes: avisar quando não tiver certeza de uma informação; nunca inventar lei, jurisprudência, número de processo ou dado; marcar `[CONFERIR]` toda citação que precise ser checada na fonte; lembrar que o texto passa por revisão humana antes de sair do escritório.
   - Regra fixa de dados: se aparecer dado pessoal de cliente sem anonimização, a IA avisa e sugere a versão anonimizada antes de continuar.
   - **Não acrescente regra que não esteja no código.** Onde o código for vago, não complete: anote a lacuna.
3. Entregue duas coisas separadas: as instruções prontas para colar no Projeto e a lista de lacunas do código.
4. Grave as instruções em `escritorio/01-cultura/instrucoes-do-projeto.md`, com a versão do código de origem no topo. Acrescente as lacunas à lista "Pendências para a próxima revisão" do código.
5. Diga onde colar: nas instruções do Projeto no Claude do escritório, junto com o código e os modelos mais usados. Lembre que o arquivo e o Projeto mudam no mesmo dia: sempre que o código mudar, rode este modo de novo.

## 6. Fluxo do modo revisar (mensal)

1. **Junte o mês.** Pergunte, uma por vez, e aceite "não teve":
   - Os painéis ou registros semanais do mês (na trilha equipe, o painel semanal da cultura; na solo, o registro de usos e o arquivo "o que eu repeti esta semana").
   - Os erros pegos na revisão e o que causou cada um. Leia também `escritorio/06-medicao/incidentes.md`, se existir.
   - Reclamações ou elogios de cliente, resumidos e sem nomes.
   - Situações novas que ninguém sabia como tratar.
   - Sugestões da equipe.
2. **Analise e entregue:**
   1. Regras do código quebradas mais de uma vez no mês, com uma hipótese para cada: a regra está confusa, desatualizada ou falta treinamento.
   2. Situações novas que precisam de regra, com uma sugestão de redação curta para cada.
   3. Trechos desatualizados.
   4. Proposta de versão nova, marcando cada mudança com `[NOVO]` ou `[ALTERADO]`.
   5. Uma mensagem curta para a equipe explicando o que mudou e por quê (na trilha solo, uma nota para o próprio titular e para o arquivo de quem chegar depois).
3. **Não aprove nada sozinho.** Tudo é proposta. O advogado aceita, ajusta ou recusa cada mudança.
4. Depois do ok: tire as marcações, suba a versão, atualize a data, registre a linha no "Histórico de versões" do código e rode o modo converter para as instruções do Projeto acompanharem.
5. Se a mudança tocar a seção 5, avise que a regra de uso de IA precisa ser sincronizada e ofereça `regra-de-uso-de-ia`.

## 7. Como manter o código vivo

1. **Dono com nome.** Recebe sugestões, atualiza e avisa a equipe.
2. **Versão e data no topo.** Exemplo: "Versão 1.3, revisada em [DATA]". Versão 0 é rascunho com decisões em aberto; 1.0 é a primeira aprovada; cada revisão com mudança sobe uma casa (1.1, 1.2).
3. **Um lugar só.** O arquivo `escritorio/01-cultura/codigo-do-escritorio.md` e o mesmo texto no Projeto no Claude. Os dois mudam no mesmo dia.
4. **Revisão mensal de 30 minutos,** na primeira semana do mês, com o registro do mês na mão (modo revisar). Duas perguntas guiam: alguma regra foi quebrada várias vezes? Apareceu situação nova sem regra? Na revisão trimestral (`revisao-periodica`), o código é revisto junto com a regra de uso de IA e as ferramentas autorizadas.
5. **Revisão fora do calendário** quando houver: reclamação séria de cliente, erro que passou pela revisão, pessoa nova no escritório, ferramenta nova.

## 8. O que entrega e onde grava

| Documento | Caminho | Quando |
|---|---|---|
| Código do escritório | `escritorio/01-cultura/codigo-do-escritorio.md` | Modo criar e modo revisar |
| Instruções do Projeto | `escritorio/01-cultura/instrucoes-do-projeto.md` | Modo converter |
| Retrato cultural (opcional) | `escritorio/01-cultura/mudanca/retrato-cultural.md` | Passo 1 do modo criar |

No `escritorio/perfil.md`:
- Marque `- [x] Código do escritório` quando a versão 1.0 for aprovada. Com a versão 0, deixe `- [ ] Código do escritório (v0, pendências: N)`.
- Acrescente no "Histórico" uma linha: data, versão do código, e se as instruções do Projeto foram geradas.
- Atualize `atualizado_em`.

Mostre antes de gravar. Se a pasta `escritorio/01-cultura/` não existir, crie só ela e avise. Sem acesso a arquivos, entregue cada documento no chat, em bloco pronto para copiar, com o caminho onde ele deveria ficar.

## 9. Trilha solo e trilha equipe

**Solo.** O código é escrito para três leitores: o próprio titular (para decidir sempre do mesmo jeito), a IA (que vai seguir o texto no Projeto) e a primeira pessoa que for contratada ("quem chegar aprende pelo papel, sem ter que ouvir tudo de boca").
- Na seção 3, quase tudo é decidido pelo titular. Não pare aí: escreva o critério, para que a decisão saia igual em dias diferentes. Onde o escritório com equipe diria "o sócio aprova", o solo usa uma regra escrita prévia ou uma pausa de 24 horas antes de decidir (por exemplo, desconto fora da tabela).
- Na seção 2, se houver secretária ou estagiário, registre o que essa pessoa faz no atendimento. Ela é a embaixadora do método.
- Na seção 7, a mesma pessoa faz e confere. Escreva a conferência como checklist e combine que ela acontece em outro momento, não logo depois de fazer.
- O retrato cultural é só a autoavaliação. Os itens do checklist que dependem de equipe têm leitura adaptada (veja a referência).
- No modo revisar, a mensagem para a equipe vira nota para o arquivo.

**Equipe.**
- O retrato cultural leva as mesmas perguntas a duas pessoas, por escrito e sem identificação. A diferença entre as respostas e a do titular é o dado mais valioso.
- Na seção 3, cada item precisa de um nome de função diferente de "titular" sempre que for possível. Se tudo continuar com o titular, aponte: ali está o gargalo.
- O dono do código pode ser outra pessoa que não o titular. Em escritório de 2 a 5 pessoas, isso ajuda o titular a não acumular tudo.
- Na revisão mensal, entram o painel semanal, os erros pegos e as sugestões da equipe. A mensagem final vai para todos.
- Pessoa nova lê o código na primeira semana, na integração.

## 10. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Frase de site e adjetivo solto | A IA não tem o que seguir e cada um interpreta | Pedido de exemplo concreto e de frases reais |
| Prazo sem número | "Rápido" vira 4 horas para um e 3 dias para outro | Pergunta pelo número e marca `[A DEFINIR]` se não houver |
| Completar lacuna por conta própria | Regra que ninguém decidiu passa a valer na IA | Lacuna vira `[A DEFINIR]` e entra na lista de pendências |
| Código que melhora o escritório no papel | A equipe lê uma regra que ninguém segue | Retrato de como é hoje; melhoria só na revisão |
| Sigilo deixado só para a regra de IA | Documento com nome e CPF fica no celular pessoal | Seção 5 começa pelo caminho do documento desde o WhatsApp |
| Código engavetado | Arquivo e Projeto dizem coisas diferentes | Dono, versão, data, lugar único, revisão mensal e conversão a cada mudança |
| IA aprovando a própria proposta | Mudança sem decisão humana | `[NOVO]` e `[ALTERADO]`; o advogado decide cada item |

## 11. Próximo passo

- Depois do código: `regra-de-uso-de-ia`, para a política, o acordo e a tabela de anonimização. A seção 5 do código e a política precisam bater.
- Se o código foi convertido em instruções do Projeto, o escritório já pode trabalhar no nível 2 em tarefas sem dado de cliente; com dado de cliente, só depois da regra de uso e da conta conferida.
- Depois da regra: na trilha equipe, `implantar-a-mudanca`; na trilha solo, `nucleo-de-inovacao` (o bloco fixo semanal).
