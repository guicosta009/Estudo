# Regras de classificação do inventário

Leia esta referência quando o advogado perguntar "por que esse arquivo foi para esse setor?", quando for ajustar uma sugestão do script ou quando fizer o inventário à mão, sem acesso à pasta (veja `references/sem-acesso-a-pasta.md`). As listas abaixo são as mesmas que o `scripts/inventariar_pasta.py` usa. Se mudar uma, mude a outra.

Tudo é feito sobre o nome do arquivo e o nome das pastas, sem acento e em minúsculas. O asterisco no fim de um termo casa qualquer final: `contestac*` casa contestação, contestações. O conteúdo dos documentos nunca é aberto.

## 1. Marcas de versão e famílias

**Marcas que o inventário reconhece no nome:**

| Marca | Exemplos no nome |
|---|---|
| (N) | `(1)`, `(2)`: cópia automática do sistema |
| cópia | "cópia de", "copia", "copy" |
| final | "final", "final2", "versão final" |
| vN | "v3", "v2.1", "versão 4" |
| revisado | "revisado", "revisada2", "rev", "rev3" |
| novo | "novo", "nova", "novo2" |
| antigo | "antigo", "velho", "obsoleto" |
| não usar | "não usar", "não use", "não utilizar" |
| usar este | "usar este", "usar esse" |
| atualizado | "atualizado", "atual" |
| definitivo | "definitivo", "último", "agora vai", "corrigido", "editado", "bkp", "backup", "ok" |
| data | "2024", "2024-03-07", "07-03-2024", "20240307" |

**Família de versões:** arquivos que ficam com o mesmo nome depois de tirar as marcas ("Modelo Inicial Aposentadoria Especial FINAL", "FINAL2" e "v3 revisado" viram "modelo inicial aposentadoria especial"), com pelo menos dois conteúdos diferentes. A família vale mesmo com extensões diferentes (o .docx e o .pdf do mesmo modelo).

**Duplicado exato:** mesmo conteúdo, pelo hash (a impressão digital do arquivo), qualquer que seja o nome. No grupo, fica como representante o arquivo com menos marcas no nome e, no empate, o mais recente. As outras cópias não precisam ir para lugar nenhum.

**Qual versão vale:** a proposta aponta a mais recente de cada família como ponto de partida, nunca como escolha. A vigente é a que o advogado assinaria hoje sem mexer. É decisão humana (H).

## 2. Alertas de dado sensível

| Nível | Quando |
|---|---|
| Alto | Número de processo (padrão CNJ), número que parece CPF ou número longo de documento ou benefício no nome |
| Alto | Nome que parece de pessoa (primeiro nome seguido de sobrenome ou de outra palavra que não é vocabulário de escritório), principalmente seguido de processo, autos, caso, ação, "x", "contra" ou número |
| Alto | A palavra cliente no nome junto com número ou palavra de dado do caso ("extrato cliente 0231") |
| Alto | Senha ou credencial no nome (senha, gov.br, certificado digital, token, login) |
| Médio | Palavra de dado sensível ou de caso: cpf, rg, cnh, laudo, atestado, cid, exame, prontuário, receita médica, holerite, contracheque, extrato, cnis, ctps, certidão, comprovante, irpf, imposto de renda, boletim de ocorrência, medida protetiva, violência, criança, menor, adolescente, segredo de justiça, sigilo, dados bancários, conta bancária, cartão de crédito, assinado |
| Médio | Primeiro nome solto, sem sobrenome ao lado |
| Médio | Peça sem a palavra modelo, minuta ou padrão no nome (réplica, recurso, contestação, contrato, procuração): costuma ser a peça de um caso, com dado do cliente no texto |
| Médio | Área com pasta restrita (Família e Criminal) |

Exceções conhecidas: "Maria da Penha" não conta como nome de pessoa; nomes de mês não contam como primeiro nome ("holerite_marco" fala do mês). Mesmo assim, o alerta é uma pergunta ao advogado, nunca uma conclusão.

**Pasta de cliente** (o inventário não entra nela e não lista o que tem dentro):
- o nome começa com clientes, cliente, casos, processos, autos, dossiês ou "pasta de clientes";
- tem a palavra cliente no nome;
- tem número de processo, CPF ou número longo no nome;
- tem nome de pessoa (primeiro nome com sobrenome, como em "[NOME] [NOME] x Banco").

Se o advogado confirmar que uma pasta marcada não é de cliente (por exemplo, "Processos de trabalho do escritório"), rode de novo com `--liberar-pasta "<nome>"`. A decisão fica registrada na conversa.

**Máscara na exibição:** número de processo vira `[PROCESSO]`, CPF vira `[DOC]`, número longo vira `[NÚMERO]`, nome de pessoa vira `[NOME]`. É a tabela de troca padrão das regras transversais aplicada ao nome do arquivo. O caminho real fica só no `inventario.tsv` e no `plano-de-reorganizacao.tsv`, que ficam no computador do escritório.

## 3. Setor

O setor com mais pontos vence. Termo de uma palavra vale 1 ponto; termo de mais de uma palavra vale 2; termo achado só no nome da pasta vale metade. Se o segundo colocado chega a 80% do primeiro, ele aparece como alternativo e o advogado escolhe. Sem nenhum termo, o setor fica `[A CONFIRMAR]`.

| Setor | Termos |
|---|---|
| Atendimento e triagem | triagem, primeiro contato, atendimento*, consulta inicial, boas vindas, ficha de triagem, pré-atendimento, qualificac* |
| Comercial | proposta*, honorario*, contrato de honorários, contrato*, procurac*, hipossuficiência, desconto*, orcamento* |
| Produção de peças | petição, petições, inicial, iniciais, contestac*, recurso*, apelac*, replica*, manifestac*, embargo*, agravo*, parecer*, memoria*, quesito*, impugnac*, calculo*, tese, teses, cumprimento de sentença, peça, peças, minuta*, requerimento*, reclamatoria*, inominado, contrarrazo* |
| Prazos e controladoria | prazo*, publicac*, intimac*, controladoria, agenda*, feriado*, distribuic*, diário oficial |
| Audiências e diligências | audiencia*, diligencia*, preposto*, preposic*, substabelecimento*, correspondente*, ata de audiência, testemunha* |
| Financeiro e cobrança | cobranca*, boleto*, inadimplen*, regua*, repasse*, financeiro*, recibo*, renegociac*, nota fiscal, fluxo de caixa |
| Relacionamento com o cliente | mensage*, whatsapp, andamento*, faq, perguntas frequentes, resumo mensal, relevância, movimentac*, respostas prontas |
| Marketing e conteúdo | post, posts, instagram, conteudo*, marketing, publicidade, carrossel, reels, video*, linkedin, newsletter, site, blog, provimento 205 |
| Gestão de equipe | onboarding, novo colaborador, colaborador*, treinamento*, estagiari*, reuniao*, ata de reunião, acessos, férias, confidencialidade, equipe |
| Administrativo | padrão de nomes, padrão nomes, pastas, arquivo morto, protocolo*, digitalizac*, descarte, política de dados, recebimento de documentos |

Quando o nome casa um esqueleto da `montar-base` (seção 5), o setor do esqueleto manda: o padrão de nomes vai para `comum/`, o checklist de documentos vai para Atendimento e triagem, e assim por diante.

## 4. Área

| Área | Termos |
|---|---|
| Previdenciário | previdenciari*, prev, inss, aposentadoria*, auxilio*, bpc, loas, beneficio*, pensão por morte, cnis, ppp, ltcat, salário-maternidade, rural, segurado* |
| Trabalhista | trabalhist*, trab, reclamatoria*, reclamação trabalhista, rescisão, rescisori*, horas extras, trct, fgts, justa causa, vinculo* |
| Família | família, fam, divorcio*, alimentos, pensão alimentícia, guarda, união estável, partilha, visitas |
| Consumidor | consumidor*, cdc, negativac*, procon, fatura*, plano de saúde |
| Cível | cível, civil, despejo, usucapião, execução de título |
| Criminal | criminal, penal, habeas, denúncia, inquérito, resposta à acusação |

## 5. Tipo e esqueleto

A primeira regra que casa decide:

| Ordem | Tipo | Quando |
|---|---|---|
| 1 | POP | "pop" ou "procedimento operacional" no nome. Vai para a `gerir-pops`, fora da base |
| 2 | caso de teste | "caso de teste", "casos de teste", "gabarito" |
| 3 | o tipo do esqueleto | o nome casa um esqueleto da montar-base (tabela abaixo) |
| 4 | checklist | checklist, check list, lista de conferência |
| 5 | critério | critério, critérios |
| 6 | tabela | tabela, planilha, ou arquivo .xlsx, .xls, .csv, .ods |
| 7 | roteiro | roteiro, script, passo a passo, manual |
| 8 | política | política, "termo de", regra de uso |
| 9 | resposta aprovada | respostas, resposta padrão |
| 10 | modelo | modelo, minuta, template, padrão, mensagem |
| 11 | modelo (com alerta) | nome de peça sem a palavra modelo, em Produção de peças ou Comercial |
| 12 | outro | nenhuma das anteriores |

| Esqueleto da montar-base | O nome casa quando tem | Setor | Tipo |
|---|---|---|---|
| `criterios-relevancia-movimentacao` | relevância, com critério ou movimentação | Relacionamento com o cliente | critério |
| `faq-clientes` | faq ou perguntas frequentes | Relacionamento com o cliente | resposta aprovada |
| `roteiro-triagem-por-area` | triagem, com roteiro, script ou perguntas | Atendimento e triagem | roteiro |
| `checklist-documentos-por-tipo-de-caso` | checklist ou lista, com documento | Atendimento e triagem | checklist |
| `checklist-revisao-peca` | checklist, com revisão, peça ou petição | Produção de peças | checklist |
| `tabela-interna-honorarios` | honorários, com tabela, valores ou planilha | Comercial | tabela |
| `regua-de-cobranca` | régua, ou cobrança com política | Financeiro e cobrança | política |
| `padrao-nomes-e-pastas` | padrão, com nome ou pasta | comum | critério |
| `checklist-etico-publicidade` | ético ou provimento, com checklist, lista ou publicidade | Marketing e conteúdo | checklist |
| `modelos-mensagem-por-categoria` | mensagem, com modelo, pronta, padrão, whatsapp ou categoria | Relacionamento com o cliente | modelo |

Os tipos são os da montar-base (modelo, checklist, critério, tabela, roteiro, política, resposta aprovada) mais caso de teste e outro.

## 6. Triagem proposta

A primeira regra que casa decide:

| Ordem | Situação | Proposta |
|---|---|---|
| 1 | É POP | fora da base (gerir-pops) |
| 2 | Tipo outro com palavra de dado do caso ou com alerta alto (laudo, holerite, extrato, documento pessoal) | fora da base (volta para a pasta do cliente) |
| 3 | Duplicado exato de outro arquivo | descartar, sem cópia |
| 4 | O nome diz "antigo" ou "não usar" | descartar, cópia em `_arquivo/` |
| 5 | Versão mais antiga de uma família | descartar, cópia em `_arquivo/` |
| 6 | A mais recente de uma família | atualizar (o advogado escolhe a vigente e junta numa só) |
| 7 | Tem alerta | atualizar (abrir, conferir, anonimizar) |
| 8 | Tipo outro | descartar, `[A CONFIRMAR]` se algum POP usa |
| 9 | Sem alteração há mais de 2 anos (ajustável com `--anos-parado`) | atualizar (conferir se vale) |
| 10 | O resto | usar |

"Criar" não sai de um arquivo: sai de um item que o POP pede e a pasta não tem.

**Rodada.** Com POP lido: primeira rodada é o que algum POP cita; o resto fica para a próxima. Sem POP, com setor-alvo: primeira rodada é o setor-alvo e `comum/`. Sem nenhum dos dois: `[A CONFIRMAR]`. É o princípio da montar-base: a base nasce do que o POP cita, um setor bem servido antes de dois pela metade.

## 7. Nome novo e destino

Padrão da montar-base: `<tipo>-<assunto>[-<area>]`, minúsculas, sem acento, hífen entre palavras, sem versão no nome.

- O assunto sai do nome antigo sem as marcas de versão, sem as palavras de tipo (modelo, checklist, tabela, padrão), sem nome de pessoa, sem número e sem "processo", "cliente", "autos". No máximo seis palavras.
- Quando o nome casa um esqueleto, usa o nome do esqueleto: `criterios-relevancia-movimentacao-previdenciario`, `checklist-documentos-auxilio-doenca`, `roteiro-triagem-familia`, `tabela-interna-honorarios`, `regua-de-cobranca`, `padrao-nomes-e-pastas`.
- Manual de quem chega vira `trilha-de-leitura` em Gestão de equipe (artefatos por setor da montar-base).
- A extensão continua a mesma. Modelo em .docx continua .docx, com a ficha .md ao lado.

| Caso | Destino dentro de `04-base/` (ou `02 Base/`) |
|---|---|
| Modelo de peça | `producao-de-pecas/modelos/<area>/` (padrão da `organizar-producao-de-pecas`); sem área, `producao-de-pecas/modelos/` com a área `[A CONFIRMAR]` |
| Checklist de revisão de peça | `producao-de-pecas/` |
| Outro documento de peças com área | `producao-de-pecas/<area>/` |
| Padrão de nomes e pastas | `comum/` |
| Caso de teste | `casos-de-teste/<nome-da-automacao>/caso-NN` (o nome da automação é preenchido pelo advogado) |
| Os outros setores | `<setor>/`, com a área no fim do nome |
| Setor não identificado | `[A CONFIRMAR setor]/`: a cópia só acontece depois que o advogado preencher |
| Descartar | `_arquivo/<nome-novo>_ate-AAAA-MM-DD.<ext>`, com a data da última alteração do arquivo |
| Duplicado exato, dado do caso, POP, pasta de cliente | não copia |
