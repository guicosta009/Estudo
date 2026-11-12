---
name: regra-de-uso-de-ia
description: >
  Escreve a regra de uso de IA do escritório em três peças: a Política de uso de IA (uma
  página, no máximo uma e meia), o Acordo de uso de IA com 8 compromissos (uma via por pessoa,
  ou o autocompromisso do advogado solo) e a tabela de anonimização com exemplo. Propõe o texto
  de transparência com o cliente, confere a conta de IA e abre o livro de incidentes. Use quando
  o advogado disser "regra de uso de IA", "política de IA", "o que pode ir para a IA",
  "acordo de uso", "termo para a equipe assinar", "como anonimizar", "posso colocar documento
  de cliente na IA?", "a conta de IA é segura?", "contar ao cliente que uso IA", "vazou um dado",
  "registrar incidente" ou "quem é o guardião de dados". Não use para escrever o código do
  escritório inteiro (use codigo-do-escritorio) nem para auditar os riscos de um fluxo (use
  auditar-riscos).
---

# Regra de uso de IA

> Diz, em uma página, o que pode ir para a IA, em qual conta, o que nunca vai, como anonimizar, quem revisa, o que o cliente fica sabendo e o que fazer quando algo dá errado. Depois transforma a regra em compromisso: cada pessoa assina o seu acordo antes de começar.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Definições de linha vermelha, incidente e quase incidente: `../../docs/glossario.md`. Papéis por porte: `../../docs/trilhas.md`.

A regra de uso é o mínimo do nível 1 de inserção da IA. Sem ela, nenhum passo com dado de cliente pode ser S (trava por estágio da `classificar-sah`). "Na dúvida, o dado não entra."

## 1. Quando usar

**Use quando:**
- O escritório não tem regra escrita do que pode ir para a IA (modo **criar**).
- A regra existe e chegou a revisão trimestral, ou mudou a ferramenta, a conta, a equipe ou a seção "Dados e sigilo" do código (modo **revisar**).
- Aconteceu um incidente ou um quase incidente e é preciso conter, registrar e mudar o POP (modo **incidente**).
- Uma pessoa nova entrou e precisa assinar o acordo.

**Não use quando:**
- O pedido é o código do escritório inteiro (tom, prazos, quem decide): use `codigo-do-escritorio`. Esta skill só garante que a seção 5 do código e a política digam o mesmo.
- O pedido é avaliar os riscos de um fluxo ou de uma automação já desenhada: use `auditar-riscos`.
- O pedido é o plano para erro de uma automação específica: use `desenhar-automacao`.

## 2. Antes de começar

1. Leia `escritorio/perfil.md` (trilha, porte, áreas, `conta_de_ia`). Sem perfil, faça o modo rápido das regras transversais.
2. Leia, se existirem: `escritorio/01-cultura/codigo-do-escritorio.md` (seções 5 e 6), `escritorio/01-cultura/regra-de-uso-de-ia.md`, `escritorio/01-cultura/acordos/` e `escritorio/06-medicao/incidentes.md`.
3. **Escolha o modo:** sem regra, criar. Com regra, pergunte se é revisão ou incidente. Se o advogado chegou dizendo que algo vazou ou que a revisão pegou um erro sério, vá direto ao modo incidente (seção 7).
4. **Portão:** o ideal é ter o código do escritório antes, porque a seção 5 dele (Dados e sigilo) e a política precisam bater. Se o código não existir, diga isso em uma frase, ofereça `codigo-do-escritorio` e, se o advogado preferir seguir, siga. Registre em "Etapas puladas" do `perfil.md`: "Regra de uso escrita antes do código: sincronizar a seção 5 quando o código for escrito."
5. **Modo curto.** Se o advogado quiser só o essencial agora, monte a política com o mínimo do plugin (seção 4 das regras transversais), marque `[A DEFINIR]` no resto e entregue o autocompromisso ou os acordos. Volte aos campos pendentes na próxima conversa.

## 3. Fluxo do modo criar

Uma pergunta por vez. Peça exemplo concreto quando a resposta vier vaga. O que ficar sem decisão vira `[A DEFINIR]`.

### Passo 1. Definir o guardião
Mostre a tabela da seção 4 e pergunte: "Pelo porte do escritório, o guardião de governança e dados seria [SUGESTÃO]. Quem vai ser?". Na trilha solo, confirme que é o titular. O guardião escreve a política; o patrocinador (em geral o titular ou o sócio) aprova.

### Passo 2. Levantar ferramentas e contas
1. "Quais ferramentas de IA alguém do escritório usa hoje, inclusive por conta própria?"
2. Para cada uma: "Em que tipo de conta ela roda: pessoal gratuita, pessoal paga, profissional ou de equipe? Em nome de quem?"
3. "Quais dessas o escritório quer autorizar?"
Regra fixa: dado de cliente só em conta profissional ou de equipe, com o tratamento de dados conferido. Conta pessoal gratuita serve só para teste com dado fictício. Se o `perfil.md` disser outra coisa, atualize o campo `conta_de_ia` com o ok do advogado.

### Passo 3. Conferir a conta
Para cada conta que vai receber dado de cliente, siga `references/checklist-conta-de-ia.md` (retenção, uso para treino, compartilhamento, quem tem acesso). Você não sabe o que cada ferramenta oferece: cada item é "conferir na configuração da conta" e o advogado diz o que encontrou. O que ele não souber fica `[A CONFIRMAR]`. Responsável configura, guardião confere.

### Passo 4. Tipos de dado
"Que tipos de dado circulam no escritório? Por exemplo: saúde, finanças, dados de crianças, processos em segredo de justiça, dados de empregados que não são clientes." Anote quais são dado sensível no sentido da LGPD (Lei 13.709/2018).

### Passo 5. Para que a IA pode ser usada
"Para que a IA já é usada, ou vai ser usada, em cada setor? Me dê um exemplo real de cada." Use os nomes dos 10 setores do glossário. Separe os usos sem dado de cliente (conteúdo, modelo em branco, estudo) dos usos com dado de cliente.

### Passo 6. O que nunca vai para a IA
Proponha o mínimo do plugin e pergunte o que acrescentar:
- Nem anonimizado, sem autorização expressa de [GUARDIÃO OU RESPONSÁVEL]: laudo completo, dado de criança ou adolescente, processo em segredo de justiça.
- Nunca, em nenhuma hipótese: senha e credencial (gov.br, certificado digital, Meu INSS).
Pergunte: "Quem autoriza uma exceção, e como essa autorização fica registrada?"

### Passo 7. Anonimização
Mostre a tabela de troca padrão e o exemplo de `references/anonimizacao.md`, com os cuidados da área do escritório. Pergunte: "Quem anonimiza antes de colar? Onde fica guardada a correspondência entre o código e o nome real?" (resposta esperada: com quem usa, numa pasta do cliente, nunca dentro da IA).

### Passo 8. Revisão humana
1. "O que nunca sai do escritório sem leitura de advogado?" Proponha: tudo o que sai do escritório.
2. Mostre o que a revisão confere: citações de lei e jurisprudência na fonte, nomes, datas, valores, cálculos, prazos e tom. "Quem assina responde pelo conteúdo."
3. Mostre a linha vermelha (glossário). Se o código já a tem na seção 6, cite a seção em vez de repetir.

### Passo 9. Transparência com o cliente
Apresente as três opções-modelo de `references/transparencia-com-o-cliente.md`: cláusula no contrato de honorários, comunicado no início do atendimento ou informação sob pedido. Pergunte qual o escritório quer usar (pode combinar). Avise: os textos são modelo a revisar, e a orientação da seccional sobre o tema precisa ser conferida `[CONFERIR]`. Se o advogado não quiser decidir agora, o campo fica `[A DEFINIR PELO ESCRITÓRIO]`, como no acordo.

### Passo 10. Incidentes
1. "Por qual canal a pessoa avisa o guardião quando algo dá errado?" (um só canal, combinado).
2. Confirme o prazo: no mesmo dia. Confirme o compromisso: quem avisa nunca é punido por avisar.
3. Explique a diferença entre incidente e quase incidente (seção 6) e diga onde fica o livro.

### Passo 11. Revisão da política
Proponha: revisão a cada trimestre (pelo núcleo, na `revisao-periodica`; no solo, pelo titular no bloco fixo) e fora do calendário quando houver ferramenta nova, conta nova, incidente, pessoa nova ou mudança na seção 5 do código.

### Passo 12. Montar e medir a política
Use `assets/politica-de-uso-de-ia-modelo.md`. **Tamanho: uma página, no máximo uma e meia** (na prática, até umas 700 palavras no corpo, sem contar anexos e assinaturas; estimativa). Se passar, corte exemplo antes de cortar regra. Linguagem para quem chegou ontem. Normas só pelo nome. Nada de recurso de ferramenta que você não conferiu.

### Passo 13. Sincronizar com o código
Se o código existe, compare a seção 5 dele com as partes 2, 3 e 4 da política. Mostre cada divergência numa lista ("o código diz X, a política diz Y") e pergunte qual vale. Com o ok, ajuste o lado que perdeu: na política, direto; no código, marque `[ALTERADO]` na seção 5, suba a versão, registre no histórico e lembre de gerar de novo as instruções do Projeto (`codigo-do-escritorio`, modo converter). Se o código não existe, deixe a nota de sincronizar no `perfil.md`.

### Passo 14. Acordos
- **Equipe:** gere um acordo por pessoa com `assets/acordo-de-uso-de-ia-modelo.md`, preenchendo a lista de ferramentas, o [RESPONSÁVEL] (o guardião) e o item 7 (cliente) com a opção escolhida. Prazo de assinatura: até uma semana. "Sem acordo assinado, ninguém começa." O acordo é lido item a item com a equipe na reunião de lançamento (`implantar-a-mudanca`), e os ajustes feitos ali voltam para todas as vias.
- **Solo:** gere o autocompromisso com `assets/autocompromisso-solo-modelo.md`. Se houver secretária ou estagiário que use IA, essa pessoa assina o acordo da equipe, com o titular como [RESPONSÁVEL].
- Abra `acordos/assinaturas.md`, uma tabela com: pessoa, função, versão do acordo, entregue em, assinado em, observação. Quem não assinou em uma semana aparece para o guardião, e essa pessoa não usa IA com dado de cliente até assinar.

### Passo 15. Abrir o livro de incidentes
Se `escritorio/06-medicao/incidentes.md` não existir, crie a partir de `assets/livro-de-incidentes-modelo.md`. Se existir, não mexa no conteúdo.

### Passo 16. Mostrar e gravar
Mostre a política, um acordo (ou o autocompromisso) e a tabela de anonimização. Peça ajustes. Grave só depois do ok (seção 9).

## 4. Papéis: quem é o guardião

| Porte | Patrocinador (aprova) | Guardião de governança e dados (escreve e cuida) |
|---|---|---|
| Solo | Titular | Titular |
| 2 a 5 pessoas | Titular | Titular |
| 6 a 20 pessoas | Sócio | Sócio ou responsável pelo administrativo |
| Mais de 20 | Sócio ou comitê | Pessoa formal ligada ao encarregado de dados |

**O guardião cuida de:** política e assinaturas; ideias e automações de risco alto; incidentes; conferência da conta e da anonimização.
**Perfil:** advogado detalhista, com autoridade para dizer não e tempo para responder rápido. Guardião que demora vira gargalo e a equipe passa a contornar a regra.
**Divisão do trabalho:** quem usa anonimiza, com o checklist no POP; o responsável pela inovação configura a conta; o guardião confere; o advogado responsável faz a revisão humana; todos guardam o sigilo.

## 5. Os três documentos

| Documento | Para quê | Tamanho | Quem assina |
|---|---|---|---|
| Política de uso de IA | A regra do escritório, em 8 partes | Uma página, no máximo uma e meia | Guardião escreve, patrocinador aprova, cada pessoa assina a ciência |
| Acordo de uso de IA (ou autocompromisso) | Transforma a regra em compromisso pessoal, em 8 itens | Uma página | Cada pessoa, a sua via, em até uma semana |
| Tabela de anonimização com exemplo | O "como fazer" da troca de dados | Anexo da política | Não se assina; se segue |

As 8 partes da política: 1) para que a IA pode ser usada, com exemplos dos setores; 2) ferramentas e contas autorizadas, dado de cliente só em conta profissional; 3) o que nunca vai para a IA, nem anonimizado; 4) como anonimizar; 5) revisão humana obrigatória; 6) transparência com o cliente; 7) registro de incidentes; 8) revisão da política a cada trimestre.

Se o escritório preferir uma assinatura só por pessoa, a assinatura do acordo pode substituir a lista de ciência da política, porque o acordo cita a política. Essa escolha é do advogado `[A DEFINIR]`.

## 6. Incidente e quase incidente

- **Incidente:** o dado saiu, ou o erro chegou ao cliente ou ao processo. Exemplo: uma petição inteira, com dados e laudo, colada numa conta gratuita.
- **Quase incidente:** a revisão pegou antes. Exemplo: um julgado inexistente encontrado na conferência da citação.
- Os dois são registrados. Meta de "zero incidente" deixa todo mundo cego: o número subir no começo é bom sinal, porque mostra que as pessoas estão contando. O que preocupa é o incidente repetido.
- Quem avisa nunca é punido por avisar.

**Os 5 passos quando acontece:**
1. **Conter:** apagar a conversa ou corrigir a mensagem.
2. **Avisar o guardião** no mesmo dia, pelo canal combinado.
3. **Registrar no livro,** com fatos e sem caça a culpado: data, o que houve, tipo de dado, ferramenta e conta, o que já foi feito.
4. **Avaliar se é preciso comunicar** o cliente ou outra parte. Quem decide é o advogado responsável (com o patrocinador, na equipe). A skill não decide e não redige comunicação sem esse pedido. Possíveis obrigações legais (por exemplo, o que a LGPD prevê para incidente de segurança com dado pessoal, e o dever de sigilo do Estatuto da Advocacia) precisam ser conferidas na fonte e com a orientação jurídica que o caso pedir `[CONFERIR]`.
5. **Mudar o POP:** todo incidente termina com um passo novo ou alterado. Nos exemplos: o POP ganha um checklist de anonimização e a conta profissional vira atalho fixo no navegador; o julgado inexistente vira passo H explícito com o campo "conferido por".

## 7. Fluxo do modo incidente

1. Pergunte o que aconteceu, em fatos. **Não peça o dado** que vazou: peça o tipo ("dado de saúde de um cliente", "nome e CPF"). Se o dado aparecer na conversa, avise e não repita.
2. Pergunte se já foi contido. Se não, oriente o passo 1 antes de qualquer outra coisa.
3. Classifique: incidente ou quase incidente. Na dúvida, registre como incidente.
4. Preencha a entrada no livro (`escritorio/06-medicao/incidentes.md`) e mostre antes de gravar.
5. Leve a pergunta da comunicação ao advogado, com o `[CONFERIR]` do passo 4 da seção 6. Registre a decisão e quem decidiu.
6. Proponha a mudança no POP afetado e ofereça `escrever-pop` para aplicá-la. Se o incidente mostrou uma regra que falta, proponha a mudança na política com `[NOVO]` ou `[ALTERADO]` e, se tocar dados e sigilo, no código.

## 8. Fluxo do modo revisar (trimestral)

1. Leia a política atual, o livro de incidentes do período e a seção 5 do código.
2. Pergunte, uma por vez: entrou ferramenta ou conta nova? Saiu alguém ou entrou alguém? Algum uso novo apareceu sem regra? Alguma regra foi contornada?
3. Proponha a versão nova com `[NOVO]` e `[ALTERADO]`. Não aprove nada sozinho.
4. Refaça o checklist da conta para cada conta autorizada.
5. Se mudou algum dos 8 compromissos do acordo, gere as vias novas para assinar. O acordo é revisado sempre que o código ou a política mudarem nesses pontos.
6. Sincronize com o código (passo 13 do modo criar).

## 9. O que entrega e onde grava

| Documento | Caminho |
|---|---|
| Política de uso de IA, com anexos (tabela de anonimização, registro da conferência da conta, texto de transparência escolhido) | `escritorio/01-cultura/regra-de-uso-de-ia.md` |
| Acordo de cada pessoa | `escritorio/01-cultura/acordos/acordo-<nome-ou-funcao>.md` |
| Autocompromisso do titular (solo) | `escritorio/01-cultura/acordos/autocompromisso-titular.md` |
| Controle de assinaturas | `escritorio/01-cultura/acordos/assinaturas.md` |
| Livro de incidentes (cria se não existir) | `escritorio/06-medicao/incidentes.md` |

Nomes de arquivo em minúsculas, sem acento, com hífen. Todo documento leva nome, versão, data e dono no topo.

No `escritorio/perfil.md`:
- Marque `- [x] Regra de uso de IA` quando a política estiver aprovada e todos os acordos (ou o autocompromisso) assinados. Enquanto faltar assinatura: `- [ ] Regra de uso de IA (política aprovada, acordos N de TOTAL)`.
- Acrescente no "Histórico": data, versão da política, guardião (função), conta autorizada.
- Atualize `conta_de_ia` e `atualizado_em` se mudaram.

Mostre antes de gravar. Sem acesso a arquivos, entregue cada documento no chat, em bloco pronto para copiar, com o caminho onde ele deveria ficar.

## 10. Trilha solo e trilha equipe

**Solo.**
- O titular é o guardião e o patrocinador. A política continua de uma página: ela é a regra escrita que substitui a segunda pessoa que não existe.
- O acordo vira **autocompromisso** de uma página (`assets/autocompromisso-solo-modelo.md`). Onde o acordo da equipe diz "sem autorização de [RESPONSÁVEL]", o autocompromisso pede decisão escrita no Registro de exceções da política, com o motivo, depois de uma pausa de 24 horas. Onde diz "avisar [RESPONSÁVEL]", o titular registra no livro no mesmo dia, mesmo que ninguém mais fique sabendo.
- A revisão humana acontece em outro momento, não logo depois de fazer, com checklist escrito. A IA pode ser um segundo olhar, sem nunca transformar o passo em S por isso.
- Secretária ou estagiário que use IA assina o acordo da equipe.
- **Quando contratar a primeira pessoa:** a trilha muda para equipe no `perfil.md`, a nova pessoa assina o acordo antes de qualquer acesso a dado de cliente e a política é revista.

**Equipe.**
- Guardião definido pelo porte (seção 4). Em escritório de 2 a 5 pessoas, o titular acumula patrocinador e guardião: combine um tempo fixo para responder, senão ele vira gargalo.
- Um acordo por pessoa, assinado em até uma semana. "Sem acordo assinado, ninguém começa."
- Pessoa nova assina o acordo na primeira semana, antes de qualquer acesso a dado de cliente.
- Em escritório com várias áreas, a regra é única para todos. Cada área pode ter cuidados extras na tabela de anonimização, mas a política é uma só.

## 11. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| "Depois a gente vê o sigilo" | Documento com nome e CPF numa conta pessoal | Regra e acordo antes de qualquer teste com dado real |
| Prometer recurso de ferramenta | Política diz que a conta "não guarda nada" e ninguém conferiu | Todo item da conta é "conferir na configuração da conta" |
| Política de quatro páginas | Ninguém lê | Uma página, no máximo uma e meia; anexos à parte |
| Regra que só o titular conhece | Cada um usa de um jeito | Acordo assinado por pessoa, com prazo |
| Punir quem avisa | A equipe passa a esconder erro | Compromisso escrito de que quem avisa não é punido |
| Código e política dizendo coisas diferentes | A IA segue uma, a equipe segue outra | Passo de sincronização com a seção 5 do código |
| Decidir pela comunicação ao cliente | Decisão jurídica tomada pela IA | Decisão do advogado, com `[CONFERIR]` nas obrigações |

## 12. Próximo passo

- Se o código ainda não existe: `codigo-do-escritorio`, começando a seção 5 pela política.
- Trilha equipe: `implantar-a-mudanca`, para ler o acordo item a item na reunião de lançamento e começar o piloto.
- Trilha solo: `nucleo-de-inovacao`, para marcar o bloco fixo semanal, e depois `mapear-setores`.
- Com a regra escrita e a conta conferida, a trava por estágio da `classificar-sah` deixa de impedir que um passo com dado de cliente seja S. Os outros critérios da classificação continuam valendo.
