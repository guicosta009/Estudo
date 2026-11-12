---
name: auditar-riscos
description: >
  Revisa os riscos de um POP ou de um fluxo com IA antes de publicar ou automatizar, como o
  sócio responsável pela ética, pelo sigilo e pela proteção de dados: linha vermelha e como
  redesenhar cada passo que a toca, sigilo e dados, pontos de erro, revisão humana, plano para
  erro, publicidade (Provimento 205/2021) quando o fluxo toca marketing, e nota de risco de 1 a 5
  do fluxo como está e redesenhado. Entrega um relatório e propostas marcadas [ALTERADO], sem
  aplicar sozinha. Use quando o advogado disser "auditar o POP", "revisar riscos", "isso pode dar
  problema com a OAB?", "está seguro automatizar?", "checar sigilo e LGPD do fluxo", "linha
  vermelha do processo", "antes de publicar o POP". Não use para escrever ou corrigir o POP
  (use escrever-pop) nem para montar a automação (use desenhar-automacao).
---

# Auditar os riscos de um POP

> Lê o POP ou o fluxo como o sócio que responde pela ética, pelo sigilo e pelos dados, aponta onde ele pode machucar o cliente, o processo ou o escritório, e propõe como redesenhar. Quem decide o que muda é o advogado.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Linha vermelha, S, A, H, níveis e definição de incidente: `../../docs/glossario.md`. Diferenças entre solo e equipe: `../../docs/trilhas.md`.

## 1. Quando usar

**Use quando:**
- Um POP com S, A e H ficou pronto no `escrever-pop` e vai ser publicado para a equipe ou levado ao Projeto do escritório.
- O escritório quer subir um fluxo para o nível 4 (automação de fluxo) ou 5 (agentes) e precisa saber se é seguro.
- Houve um erro ou quase incidente e o advogado quer revisar o fluxo inteiro, não só o passo que falhou.
- O fluxo envolve conteúdo público (redes, site, anúncio) e precisa da leitura de publicidade.

**Não use quando:**
- Ainda não existe POP nem fluxo escrito: use `escrever-pop`.
- O pedido é só marcar S, A ou H numa lista: use `classificar-sah`.
- O pedido é escrever a automação, as instruções por passo ou o plano para erro definitivo: use `desenhar-automacao` (ela reaproveita o rascunho do plano para erro feito aqui).

## 2. Antes de começar

1. **Leia o perfil.** Abra `escritorio/perfil.md` (trilha, porte, áreas, conta de IA, nível) e, se existirem, `escritorio/01-cultura/codigo-do-escritorio.md` (o que nunca fazemos, quem decide, dados e sigilo) e `escritorio/01-cultura/regra-de-uso-de-ia.md`. Sem perfil, ofereça `/inicio-automacao:comecar` ou faça o modo rápido das regras transversais.
2. **Portão.** Precisa haver um POP com siglas ou um fluxo descrito em texto. Procure em `escritorio/03-pops/<setor>/pop-<sigla>-<nn>-<processo>.md` ou peça que o advogado cole. Se o fluxo não tiver siglas, avise que a auditoria fica mais fraca, ofereça o `classificar-sah` e, se ele quiser seguir, trate todo passo sem sigla como S para fins de risco (o pior caso).
3. **Dados primeiro.** Se o fluxo colado tiver nome, CPF, número de processo ou dado de saúde, avise, não repita o dado e trabalhe sobre a versão anonimizada.
4. **Contexto que falta.** Pergunte só o que não está no perfil nem no POP, uma pergunta por vez:
   - "Em que conta de IA esse fluxo roda: pessoal gratuita, pessoal paga, profissional ou de equipe? O tratamento de dados foi conferido?"
   - "Até onde você quer levar esse fluxo: copiloto à mão (nível 3), automação do gatilho à entrega (nível 4) ou agente (nível 5)?"
   - "Alguma parte do fluxo vira conteúdo público, anúncio ou resposta em rede social?"
   - Equipe: "Quem confere cada ponto de revisão, com nome?" · Solo: "Quando você está em audiência, de férias ou doente, o que acontece com esse fluxo?"

## 3. Fluxo

### Passo 1. Ler o fluxo inteiro
Monte para você uma lista com cada passo: sigla, quem executa, quem confere, o que confere, e para onde vai o resultado (fica no escritório, vai ao cliente, ao tribunal ou ao público). Leia também gatilho, exceções, saída, "nunca sai sem revisão humana", dados e indicador. Não corrija nada ainda.

### Passo 2. Linha vermelha
Procure qualquer passo em que a IA estaria escolhendo tese ou estratégia, dando notícia ruim ao cliente, assinando ou assumindo responsabilidade técnica, aconselhando cliente em situação de vulnerabilidade, ou enviando peça, proposta ou mensagem com conteúdo jurídico sem revisão humana. Para cada um, proponha o redesenho que devolve a decisão para a pessoa (seção 4.1). "Volume alto não tira o passo da linha vermelha."

### Passo 3. Siglas e revisão
- Passos marcados S que deveriam ser A, porque o erro é caro ou o resultado sai do escritório.
- Passos com dado de cliente marcados S num escritório sem conta profissional ou sem regra de uso escrita (trava por estágio do `classificar-sah`).
- Passos A em que não está escrito o que a pessoa confere: a revisão corre o risco de virar carimbo.
- Mensagens que chegam ao cliente, ao tribunal ou ao público sem revisão humana.

### Passo 4. Sigilo e dados
Para cada passo: que dado pessoal ou sensível entra, se ele precisa estar ali, o que anonimizar e em que ferramenta e tipo de conta o passo deveria rodar (seção 4.2).

### Passo 5. Pontos de erro
Para cada passo S e A: o que a IA pode errar, o estrago, quem perceberia e em quanto tempo (seção 4.3). Erro que só o cliente, o juiz ou o público perceberiam, e tarde, é sempre gravidade alta.

### Passo 6. Exceções, donos e indicador
- Decisões do fluxo sem o caminho do "e se não?".
- Decisões sem dono (ninguém escrito como quem decide).
- Indicador ausente ou impossível de medir. "Sem indicador, você não sabe se a IA ajudou ou só mudou o trabalho de lugar."

### Passo 7. Publicidade (só se o fluxo tocar marketing ou conteúdo público)
Aplique os alertas da seção 4.6. Procure também, em qualquer fluxo, frase que soe como promessa de resultado ou captação de clientela (mensagem de primeiro contato, proposta, resposta em rede social).

### Passo 8. Plano para erro
Rascunhe os 7 itens da seção 4.7 para este fluxo: o que fazer se a IA errar e o erro chegar ao cliente ou ao processo. Na trilha solo, inclua a ausência do titular.

### Passo 9. Nota de risco
Dê a nota de 1 a 5 do fluxo como está e do fluxo redesenhado (com todas as propostas aceitas), pela escala da seção 4.5, e explique a diferença em poucas linhas.

### Passo 10. Entregar, decidir e gravar
1. Mostre o relatório no modelo `assets/relatorio-auditoria.md`: resumo, achados por bloco, a tabela de achados (passo, risco encontrado, gravidade, ajuste sugerido) e a versão corrigida **só dos passos que mudaram**, cada um marcado `[ALTERADO]` (passo existente) ou `[NOVO]` (passo, exceção ou ponto de revisão acrescentado).
2. **Não aplique nada sozinha.** Pergunte, proposta por proposta: aceita, recusa ou deixa para depois? Registre a resposta no relatório.
3. Grave o relatório (seção 5).
4. Só se o advogado pedir, aplique no POP as propostas aceitas: suba a versão, mantenha as marcações `[ALTERADO]` e `[NOVO]` nesta versão e registre a mudança no controle de versões do POP. Se a mudança for grande (passos novos, fluxograma refeito), devolva ao `escrever-pop`.

## 4. Critérios

### 4.1 Linha vermelha: como redesenhar

| Se o passo... | Redesenho |
|---|---|
| Faz a IA escolher tese, pedido ou estratégia | A IA levanta hipóteses com documento e página de origem; o advogado escolhe e registra (H). |
| Manda ao cliente resultado desfavorável por mensagem automática | A classificação marca "notícia desfavorável" e para o fluxo; o advogado liga antes; a mensagem escrita, se houver, vem depois e revisada. |
| Faz a IA protocolar, assinar ou "aprovar" | Passo H com o advogado; a IA só prepara pasta, anexos e checklist. Credencial e certificado nunca passam pela IA. |
| Deixa a IA responder cliente em violência doméstica, criança em disputa, doença grave, perda de emprego ou idoso sem renda | Sinais de parada escritos no POP tiram o caso do fluxo e uma pessoa assume. Em Família, nada daquele caso entra em automação. |
| Envia peça, proposta ou mensagem com conteúdo jurídico sem revisão | Fila de aprovação: a IA rascunha, uma pessoa com nome revisa com objeto e só então sai. Mensagem informativa de modelo aprovado (lembrete, confirmação) pode seguir como S. |

### 4.2 Sigilo e dados

- **Conta:** dado de cliente só em conta profissional ou de equipe, com o tratamento de dados conferido ("conferir na configuração da conta"). Conta pessoal gratuita serve só para teste com dado fictício.
- **Anonimizar** sempre que o dado não precisar estar ali, com a tabela de troca das regras transversais. Terceiros (colegas, testemunhas, empregados que não são clientes) também.
- **Nunca entra:** senha e credencial (gov.br, certificado digital, Meu INSS). Sem autorização expressa do responsável: laudo completo, dado de criança ou adolescente, processo em segredo de justiça.
- **Dado sensível** (saúde, origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, vida sexual, dado genético ou biométrico): pode ser S ou A, mas exige conta profissional, anonimização quando couber e revisão humana.
- **Guarda e acesso:** pasta restrita para saúde, criança e criminal; planilha de lote com acesso restrito; documento no celular pessoal transferido ao canal oficial e apagado; descarte só com autorização do advogado.
- **Cliente informado** de que a IA participa do trabalho, do jeito que o código do escritório definir. Gravação ou transcrição só com consentimento.

Na dúvida sobre uma regra da LGPD (Lei 13.709/2018), do Estatuto da Advocacia (Lei 8.906/1994) ou do Código de Ética e Disciplina da OAB, descreva a preocupação e marque `[CONFERIR]`. Nunca cite artigo, inciso ou decisão.

### 4.3 Pontos de erro

Tabela: `Passo | O que a IA pode errar | Estrago | Quem percebe | Em quanto tempo | Como pegar antes`.

Erros que aparecem muito: jurisprudência inventada ou mal resumida; data trocada; conta de prazo errada (feriado local, suspensão, prazo em dobro); movimentação relevante classificada como rotina; publicação vinculada ao processo errado; dado de um cliente na mensagem de outro; valor diferente entre proposta e contrato; anexo citado e não juntado; tom errado com cliente fragilizado.

"Em quanto tempo" usa estas faixas: no próprio passo · no fechamento do dia · na revisão semanal · só quando o cliente, o juiz ou o público aponta.

**Gravidade:**
- **Alta:** o erro chega ao cliente, ao tribunal ou ao público; ou toca a linha vermelha; ou expõe dado sensível; ou é percebido só tarde, por quem está fora do escritório.
- **Média:** a revisão pega, mas tarde, ou o erro gera retrabalho relevante, atraso interno ou custo.
- **Baixa:** fica dentro do escritório e é percebido no passo seguinte.

### 4.4 Revisão humana

Para cada ponto de revisão: onde fica (antes de quê), quem faz (função e nome) e o que confere. Objetos de conferência: citações e jurisprudência abertas na fonte oficial; cálculos refeitos; datas e prazos com a conta à mostra; nomes, números e valores contra o documento; tom e ausência de orientação jurídica ou promessa; anexos contra a peça. "Revisão que ninguém sabe que é sua acaba não acontecendo."

### 4.5 Nota de risco (1 a 5)

Critério prático e ajustável. A nota é a do **pior achado**, não a média.

| Nota | Leitura |
|---|---|
| 1 | Nenhum passo toca a linha vermelha sem pessoa; dado em conta profissional e anonimizado onde cabe; toda saída para fora com revisão com objeto e dono; exceções e plano para erro escritos. |
| 2 | Lacunas pequenas e internas: uma revisão sem objeto escrito, uma exceção faltando, indicador vago. Nada chega ao cliente sem conferência. |
| 3 | Algum S que deveria ser A, dado pessoal sem anonimização onde não precisava, decisão sem dono ou indicador ausente. O erro seria pego, mas tarde. |
| 4 | Mensagem, peça ou prazo pode sair sem revisão humana; dado sensível em conta pessoal; sem plano para erro num fluxo que vai ao nível 4. |
| 5 | A IA decide ou executa um item da linha vermelha, ou credencial, dado de criança ou processo em segredo de justiça entra na IA, ou o erro chegaria ao cliente, ao processo ou ao público sem ninguém perceber. |

Fluxo com nota 4 ou 5 não sobe de nível até ser redesenhado. Fluxo com nota 3 pode rodar no nível 3, à mão, enquanto os ajustes são feitos.

### 4.6 Publicidade (Provimento 205/2021 do Conselho Federal da OAB)

Quando o fluxo toca marketing, conteúdo, anúncio ou rede social. Leia o texto do provimento ao montar o checklist ético do escritório `[CONFERIR]`. Procure:
- Promessa ou estimativa de resultado.
- Captação de clientela.
- Tom mercantil.
- Exposição de caso ou de cliente. Caso de cliente só com autorização expressa e revisão do sócio; na dúvida, não publica.
- Sensacionalismo. Tema sensível (crime, família com crianças, repercussão) exige o sócio.
- Anúncio pago fora da revisão ética: passa pela mesma revisão.
- Resposta em comentário público que pareça consultoria: pergunta sobre caso concreto vai para o Atendimento.
- Dúvida de cliente usada como pauta sem anonimização.
- Lei ou decisão mencionada sem conferência na fonte.
- Publicação sem a revisão ética do advogado. Nada é publicado sem ela.

### 4.7 Plano para erro (os 7 itens)

1. Como a gente percebe o erro.
2. Quem pausa a automação e como.
3. Se chegou ao cliente ou ao processo: quem avisa e por qual canal (por exemplo, o advogado responsável, por ligação).
4. Como corrigir o que já saiu.
5. O que muda para não repetir (POP, base, instrução ou ponto de revisão).
6. Onde fica registrado (o livro de incidentes em `escritorio/06-medicao/incidentes.md`, com incidente e quase incidente; quem avisa nunca é punido por avisar).
7. Quando volta a rodar e quem autoriza.

### 4.8 Alertas que valem por setor

| Setor | O que conferir |
|---|---|
| Atendimento e triagem | A IA nunca se apresenta como advogado nem dá orientação jurídica; conflito de interesse checado; urgência e aflição vão a uma pessoa; prescrição conferida pelo advogado no primeiro contato. |
| Comercial | Nenhuma promessa de resultado na proposta; valor final e cláusulas com o advogado; tabela da seccional da OAB como referência. |
| Produção de peças | Nenhuma citação sem abrir na fonte oficial; peça inteira lida por quem assina; em massa, cada petição revisada e com os fatos do próprio cliente. |
| Prazos e controladoria | A IA mostra a conta; na dúvida, "gera prazo"; data do prazo fatal sempre conferida por pessoa. |
| Audiências e diligências | Testemunha recebe orientação sobre o ato, nunca sobre o conteúdo do depoimento; limites de acordo combinados com o cliente. |
| Financeiro e cobrança | Cobrança não expõe nem constrange; medida final dentro das regras éticas; valores recebidos em nome do cliente seguem repasse e prestação de contas próprios. |
| Relacionamento com o cliente | Notícia muito ruim nunca por mensagem; decisão de mérito revisada pelo advogado. |
| Marketing e conteúdo | Seção 4.6. |
| Gestão de equipe | Acesso a dado de cliente só depois do termo de confidencialidade e do treino de IA. |
| Administrativo | Pasta restrita; documento no celular pessoal transferido e apagado; suspeita de adulteração para tudo; descarte só com autorização. |

Por área: Família (violência, coação ou risco param o POP, sem automação); Previdenciário (credenciais sempre operadas por pessoa); Trabalhista (original da conversa intacto e fora da IA; dados de terceiros anonimizados; contato com testemunha por pessoa); alimentos (busca sobre a outra parte só no que é público e lícito).

## 5. O que entrega e onde grava

**Entrega:** o relatório de auditoria no modelo `assets/relatorio-auditoria.md`, com as propostas de alteração marcadas `[ALTERADO]` e `[NOVO]` e a decisão do advogado em cada uma.

**Onde grava:** `escritorio/03-pops/<setor>/auditoria-<processo>-AAAA-MM-DD.md`, junto do POP auditado (mesma pasta de setor e mesmo nome de processo do `pop-<sigla>-<nn>-<processo>.md`). No topo: nome, versão do POP auditado, data e dono. Mostre antes de gravar.

**No `perfil.md`:** acrescente em "Histórico" uma linha com a data, o POP auditado e as duas notas (como está e redesenhado). O rascunho do plano para erro fica no relatório; a `desenhar-automacao` o reaproveita em `escritorio/05-automacoes/<nome>/plano-para-erro.md`.

**Sem acesso a arquivos:** entregue o relatório no chat, em bloco pronto para copiar, com o caminho onde ele deveria ficar.

## 6. Trilha solo e trilha equipe

**Solo:**
- O ponto único de revisão é o próprio titular. A auditoria registra sempre, como achados próprios:
  - **Fadiga de revisão:** revisar tudo sozinho cansa e empurra passos A para S na prática, sem ninguém decidir. Gravidade média ou alta conforme o volume. Ajustes típicos: conferência em outro momento do dia, checklist curto por passo A, teto de itens por bloco de revisão `[A DEFINIR]`, a IA como segundo olhar (sem virar S).
  - **Ausência do titular** (férias, audiência, doença): o que pausa, o que espera, quem avisa o cliente. Sem resposta escrita, gravidade alta para fluxos no nível 4.
- "O sócio aprova" sem sócio: a auditoria pede regra escrita prévia ou pausa de 24 horas.
- A linha vermelha 5 (envio sem revisão) depende só do titular: aponte cada envio que sai sem a leitura dele.

**Equipe:**
- Cada ponto de revisão com nome. Ponto sem dono é achado de gravidade média.
- "Se o mesmo nome aparece em todos os passos, ali está o gargalo": aponte como risco de fila e de revisão-carimbo.
- Substituto escrito para funções críticas (quem confere prazo, quem pausa a automação), nunca "quem estiver livre".
- Acesso por pessoa às pastas restritas e à planilha de lote.

## 7. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Auditar só o caminho feliz | O erro aparece na exceção, às 19h | Passo 6: "e se não?" em cada decisão |
| Confiar na sigla porque a IA "acerta quase sempre" | Passo da linha vermelha automatizado aos poucos | Linha vermelha primeiro, sem exceção por volume |
| Revisão-carimbo | Aprova sem ler por causa da fila | Cada ponto de revisão com dono e objeto |
| Nota pela média | Um risco grave some no meio de achados pequenos | A nota é a do pior achado |
| Corrigir sem perguntar | POP muda sem o dono saber | Propostas `[ALTERADO]` e `[NOVO]`, aplicadas só com ok |
| Citar artigo de memória | Norma errada num documento do escritório | Normas só pelo nome, com `[CONFERIR]` |

## 8. Próximo passo

- Nota 4 ou 5: volte ao `escrever-pop` com as propostas aceitas e audite de novo.
- Nota 3 ou menos: rode o POP à mão no nível 3 e leve a lista do que a IA consulta para a `montar-base`.
- Pronto para automatizar: `desenhar-automacao`, que começa pelo checklist de prontidão e transforma o rascunho do plano para erro em plano definitivo.
