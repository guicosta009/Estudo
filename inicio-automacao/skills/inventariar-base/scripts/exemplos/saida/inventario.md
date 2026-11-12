# Inventário da pasta "pasta-baguncada"
Feito em: 2026-11-09 · Ferramenta: inventariar-base · Situação: rascunho para o advogado conferir

> Nada foi movido, renomeado, aberto ou apagado. O inventário leu só nomes, extensões, datas, tamanhos e a impressão digital (hash) de cada arquivo. Nomes com possível dado de cliente aparecem mascarados ([NOME], [DOC], [PROCESSO], [NÚMERO]).

## 1. O retrato em números

- **Arquivos:** 30, somando 3,6 KB, em 2 pastas.
- **Pastas de cliente encontradas e não abertas:** 2.
- **Ignorados:** 2 arquivos de sistema ou temporários, 0 atalhos de nuvem sem hash, 0 atalhos de pasta.
- **Duplicados exatos** (mesmo conteúdo, nomes diferentes): 2 grupos, 2 cópias a mais.
- **Famílias de versões** (o mesmo documento com final, v3, revisado, cópia, novo, antigo): 3 famílias, 8 arquivos.
- **Arquivos com marca de versão no nome:** 14 de 30.
- **Sem alteração há mais de 2 anos:** 17.

**Por tipo de arquivo**

| Extensão | Arquivos | Tamanho |
|---|---|---|
| docx | 17 | 2,0 KB |
| txt | 6 | 742 B |
| pdf | 3 | 350 B |
| md | 2 | 245 B |
| xlsx | 2 | 254 B |

**Última alteração por ano**

| Ano | Arquivos |
|---|---|
| 2019 | 2 |
| 2020 | 1 |
| 2021 | 2 |
| 2022 | 3 |
| 2023 | 3 |
| 2024 | 6 |
| 2025 | 9 |
| 2026 | 4 |

**Os 5 mais antigos**

| # | Arquivo | Última alteração |
|---|---|---|
| 6 | contrato honorarios antigo.docx | 2019-05-03 |
| 20 | Peticoes antigas/replica INSS 2019.docx | 2019-08-19 |
| 4 | Contestação trabalhista padrão NÃO USAR.docx | 2020-02-10 |
| 14 | Modelo Inicial Aposentadoria Especial FINAL.docx | 2021-03-15 |
| 19 | Peticoes antigas/embargos declaracao modelo.docx | 2021-10-04 |

**Duplicados exatos**

| Grupo | Fica (representante) | Cópias iguais |
|---|---|---|
| D1 | #3 checklist documentos auxílio doença.docx | #7 Cópia de checklist documentos auxílio doença.docx |
| D2 | #17 Modelo Inicial Aposentadoria Especial v3 revisado.docx | #16 Modelo Inicial Aposentadoria Especial v3 revisado (1).docx |

**Famílias de versões**

| Família | Arquivo | Marcas no nome | Última alteração | Duplicado |
|---|---|---|---|---|
| F1 | #4 Contestação trabalhista padrão NÃO USAR.docx | não usar | 2020-02-10 |  |
| F1 | #5 Contestacao trabalhista padrao novo.docx | novo | 2025-04-08 |  |
| F2 | #14 Modelo Inicial Aposentadoria Especial FINAL.docx | final | 2021-03-15 |  |
| F2 | #15 Modelo Inicial Aposentadoria Especial FINAL2.docx | final | 2022-08-02 |  |
| F2 | #17 Modelo Inicial Aposentadoria Especial v3 revisado.docx | vN, revisado | 2024-06-20 |  |
| F2 | #16 Modelo Inicial Aposentadoria Especial v3 revisado (1).docx | (N), vN, revisado | 2024-06-21 | igual ao #17 |
| F3 | #29 tabela honorarios 2023.xlsx | data | 2023-01-20 |  |
| F3 | #30 tabela honorarios 2024 atualizada.xlsx | atualizado, data | 2024-01-25 |  |

Qual versão vale é decisão do advogado. A mais recente é só o ponto de partida da conversa.

## 2. Alertas de dado sensível

Regra: pasta de caso de cliente não é base. O que é dado do caso (laudo, holerite, extrato, documento pessoal, peça com nome do cliente) fica na pasta do cliente. Cada alerta abaixo é uma decisão do advogado, e nenhuma linha com alerta é copiada sem `anonimizacao_conferida = sim` no plano.

**Pastas de cliente (não abertas)**

| # | Pasta | Por que parece de cliente |
|---|---|---|
| P1 | Clientes | nome de pasta de caso ou de cliente |
| P2 | [NOME] [NOME] x Banco Ficticio | nome de pessoa no nome da pasta |

**Arquivos com alerta no nome ou no caminho**

| # | Arquivo | Nível | Alerta | Proposta |
|---|---|---|---|---|
| 9 | extrato bancario cliente 0231.pdf | alto | a palavra cliente no nome, com número ou dado de caso; palavra de dado sensível ou de caso (extrato) | fora da base |
| 11 | laudo pericial [NOME] [NOME].pdf | alto | nome que parece de pessoa; palavra de dado sensível ou de caso (laudo) | fora da base |
| 27 | Réplica [NOME] [NOME] processo [PROCESSO].docx | alto | número de processo; nome de pessoa seguido de processo ou caso; parece peça usada num caso: pode ter dado de cliente no texto | atualizar |
| 6 | contrato honorarios antigo.docx | médio | parece peça usada num caso: pode ter dado de cliente no texto | descartar |
| 10 | holerite_marco_2023.pdf | médio | palavra de dado sensível ou de caso (holerite) | fora da base |
| 20 | Peticoes antigas/replica INSS 2019.docx | médio | parece peça usada num caso: pode ter dado de cliente no texto | atualizar |
| 25 | Recurso inominado consumidor.docx | médio | parece peça usada num caso: pode ter dado de cliente no texto | atualizar |
| 28 | roteiro triagem familia.md | médio | área com pasta restrita (familia) | atualizar |

## 3. Sugestão de setor e tipo

Pelas palavras do nome e da pasta. Setor com alternativo é empate: o advogado escolhe. Sem setor, fica `[A CONFIRMAR]`.

| # | Arquivo | Setor | Área | Tipo | Esqueleto da montar-base | Palavras que pesaram |
|---|---|---|---|---|---|---|
| 1 | ata reuniao equipe.txt | Gestão de equipe |  | outro |  | reuniao, equipe |
| 2 | checklist audiencia trabalhista.md | Audiências e diligências | Trabalhista | checklist |  | audiencia |
| 3 | checklist documentos auxílio doença.docx | Atendimento e triagem | Previdenciário | checklist | checklist-documentos-por-tipo-de-caso | pelo esqueleto checklist-documentos-por-tipo-de-caso |
| 4 | Contestação trabalhista padrão NÃO USAR.docx | Produção de peças | Trabalhista | modelo |  | contestac |
| 5 | Contestacao trabalhista padrao novo.docx | Produção de peças | Trabalhista | modelo |  | contestac |
| 6 | contrato honorarios antigo.docx | Comercial |  | modelo |  | honorario, contrato |
| 7 | Cópia de checklist documentos auxílio doença.docx | Atendimento e triagem | Previdenciário | checklist | checklist-documentos-por-tipo-de-caso | pelo esqueleto checklist-documentos-por-tipo-de-caso |
| 8 | criterios relevancia movimentacao prev.txt | Relacionamento com o cliente | Previdenciário | critério | criterios-relevancia-movimentacao | relevancia, movimentac |
| 9 | extrato bancario cliente 0231.pdf | [A CONFIRMAR] |  | outro |  |  |
| 10 | holerite_marco_2023.pdf | [A CONFIRMAR] |  | outro |  |  |
| 11 | laudo pericial [NOME] [NOME].pdf | [A CONFIRMAR] |  | outro |  |  |
| 12 | manual do estagiario.docx | Gestão de equipe |  | roteiro |  | estagiari |
| 13 | mensagens prontas whatsapp andamento.txt | Relacionamento com o cliente |  | modelo | modelos-mensagem-por-categoria | mensage, whatsapp, andamento |
| 14 | Modelo Inicial Aposentadoria Especial FINAL.docx | Produção de peças | Previdenciário | modelo |  | inicial |
| 15 | Modelo Inicial Aposentadoria Especial FINAL2.docx | Produção de peças | Previdenciário | modelo |  | inicial |
| 16 | Modelo Inicial Aposentadoria Especial v3 revisado (1).docx | Produção de peças | Previdenciário | modelo |  | inicial |
| 17 | Modelo Inicial Aposentadoria Especial v3 revisado.docx | Produção de peças | Previdenciário | modelo |  | inicial |
| 18 | padrao nomes de arquivos.txt | Comum (todos os setores) |  | critério | padrao-nomes-e-pastas | pelo esqueleto padrao-nomes-e-pastas |
| 19 | Peticoes antigas/embargos declaracao modelo.docx | Produção de peças |  | modelo |  | peticoes (pasta), embargo |
| 20 | Peticoes antigas/replica INSS 2019.docx | Produção de peças | Previdenciário | modelo |  | peticoes (pasta), replica |
| 21 | POP peticao inicial FINAL_revisado2.docx | Produção de peças |  | outro (POP) |  | peticao, inicial |
| 22 | post instagram ideias.txt | Marketing e conteúdo |  | outro |  | post, instagram |
| 23 | proposta honorarios modelo.docx | Comercial |  | modelo |  | proposta, honorario |
| 24 | quesitos pericia medica modelo.docx | Produção de peças |  | modelo |  | quesito |
| 25 | Recurso inominado consumidor.docx | Produção de peças | Consumidor | modelo |  | recurso, inominado |
| 26 | regua cobranca.txt | Financeiro e cobrança |  | política | regua-de-cobranca | cobranca, regua |
| 27 | Réplica [NOME] [NOME] processo [PROCESSO].docx | Produção de peças |  | modelo |  | replica |
| 28 | roteiro triagem familia.md | Atendimento e triagem | Família | roteiro | roteiro-triagem-por-area | triagem |
| 29 | tabela honorarios 2023.xlsx | Comercial |  | tabela | tabela-interna-honorarios | honorario |
| 30 | tabela honorarios 2024 atualizada.xlsx | Comercial |  | tabela | tabela-interna-honorarios | honorario |

**Arquivos por setor sugerido**

| Setor | Arquivos |
|---|---|
| Produção de peças | 12 |
| Comercial | 4 |
| Atendimento e triagem | 3 |
| [A CONFIRMAR] | 3 |
| Gestão de equipe | 2 |
| Relacionamento com o cliente | 2 |
| Audiências e diligências | 1 |
| Comum (todos os setores) | 1 |
| Marketing e conteúdo | 1 |
| Financeiro e cobrança | 1 |

## 4. Proposta de triagem

Usar: existe, uma versão, sem alerta. Atualizar: várias versões, alerta ou parado há muito tempo. Descartar: duplicado, antigo ou sem uso (vai para `_arquivo/`, o original fica onde está). Criar: o POP pede e não existe. Fora da base: dado do caso ou POP. Tudo é proposta: o advogado confirma linha a linha.

- Usar: 7 · Atualizar: 10 · Descartar: 9 · Fora da base: 4 (mais 2 pastas de cliente) · Criar: 2

| # | Arquivo | Proposta | Motivo | Rodada |
|---|---|---|---|---|
| 2 | checklist audiencia trabalhista.md | usar | uma versão só, sem alerta no nome | próxima (nenhum POP cita) |
| 3 | checklist documentos auxílio doença.docx | usar | uma versão só, sem alerta no nome | primeira |
| 8 | criterios relevancia movimentacao prev.txt | usar | uma versão só, sem alerta no nome | primeira |
| 13 | mensagens prontas whatsapp andamento.txt | usar | uma versão só, sem alerta no nome | primeira |
| 23 | proposta honorarios modelo.docx | usar | uma versão só, sem alerta no nome | próxima (nenhum POP cita) |
| 24 | quesitos pericia medica modelo.docx | usar | uma versão só, sem alerta no nome | próxima (nenhum POP cita) |
| 26 | regua cobranca.txt | usar | uma versão só, sem alerta no nome | próxima (nenhum POP cita) |
| 5 | Contestacao trabalhista padrao novo.docx | atualizar | família F1 com 2 arquivos: a mais recente é só o ponto de partida, o advogado escolhe a vigente e junta numa só | próxima (nenhum POP cita) |
| 12 | manual do estagiario.docx | atualizar | sem alteração há muito tempo: conferir se ainda vale | próxima (nenhum POP cita) |
| 17 | Modelo Inicial Aposentadoria Especial v3 revisado.docx | atualizar | família F2 com 4 arquivos: a mais recente é só o ponto de partida, o advogado escolhe a vigente e junta numa só | próxima (nenhum POP cita) |
| 18 | padrao nomes de arquivos.txt | atualizar | sem alteração há muito tempo: conferir se ainda vale | próxima (nenhum POP cita) |
| 19 | Peticoes antigas/embargos declaracao modelo.docx | atualizar | sem alteração há muito tempo: conferir se ainda vale | próxima (nenhum POP cita) |
| 20 | Peticoes antigas/replica INSS 2019.docx | atualizar | alerta no nome: abrir, conferir e anonimizar antes de entrar | próxima (nenhum POP cita) |
| 25 | Recurso inominado consumidor.docx | atualizar | alerta no nome: abrir, conferir e anonimizar antes de entrar | próxima (nenhum POP cita) |
| 27 | Réplica [NOME] [NOME] processo [PROCESSO].docx | atualizar | alerta no nome: abrir, conferir e anonimizar antes de entrar | próxima (nenhum POP cita) |
| 28 | roteiro triagem familia.md | atualizar | alerta no nome: abrir, conferir e anonimizar antes de entrar | próxima (nenhum POP cita) |
| 30 | tabela honorarios 2024 atualizada.xlsx | atualizar | família F3 com 2 arquivos: a mais recente é só o ponto de partida, o advogado escolhe a vigente e junta numa só | próxima (nenhum POP cita) |
| 1 | ata reuniao equipe.txt | descartar | não parece documento de base (modelo, checklist, critério, tabela, roteiro, política, resposta aprovada): [A CONFIRMAR] se algum POP usa | não se aplica |
| 4 | Contestação trabalhista padrão NÃO USAR.docx | descartar | o nome diz que não vale mais (não usar) | não se aplica |
| 6 | contrato honorarios antigo.docx | descartar | o nome diz que não vale mais (antigo) | não se aplica |
| 7 | Cópia de checklist documentos auxílio doença.docx | descartar | duplicado exato do #3 (mesmo conteúdo): não precisa de cópia | não se aplica |
| 14 | Modelo Inicial Aposentadoria Especial FINAL.docx | descartar | versão mais antiga da família F2: vai para o arquivo | não se aplica |
| 15 | Modelo Inicial Aposentadoria Especial FINAL2.docx | descartar | versão mais antiga da família F2: vai para o arquivo | não se aplica |
| 16 | Modelo Inicial Aposentadoria Especial v3 revisado (1).docx | descartar | duplicado exato do #17 (mesmo conteúdo): não precisa de cópia | não se aplica |
| 22 | post instagram ideias.txt | descartar | não parece documento de base (modelo, checklist, critério, tabela, roteiro, política, resposta aprovada): [A CONFIRMAR] se algum POP usa | não se aplica |
| 29 | tabela honorarios 2023.xlsx | descartar | versão mais antiga da família F3: vai para o arquivo | não se aplica |
| 9 | extrato bancario cliente 0231.pdf | fora da base | dado do caso: volta para a pasta do cliente, nunca entra na base | não se aplica |
| 10 | holerite_marco_2023.pdf | fora da base | dado do caso: volta para a pasta do cliente, nunca entra na base | não se aplica |
| 11 | laudo pericial [NOME] [NOME].pdf | fora da base | dado do caso: volta para a pasta do cliente, nunca entra na base | não se aplica |
| 21 | POP peticao inicial FINAL_revisado2.docx | fora da base | é POP: leve à gerir-pops (código e nome padrão POP-SIGLA-NN, em 03-pops) | não se aplica |

| # | Documento que falta | Pedido por | Esqueleto |
|---|---|---|---|
| C1 | Glossário de termos processuais em linguagem simples | POP-REL-01 passo 4 | ../montar-base/references/artefatos-por-setor.md |
| C2 | Perguntas frequentes de clientes | POP-REL-01 passo 5 | ../montar-base/assets/esqueletos/faq-clientes.md |

## 5. Plano de reorganização (só depois do ok)

Destino dentro de `escritorio/04-base/`. Nada é aplicado sem o ok. O script só copia: o original continua onde está, e o que for descartado vai para `_arquivo/` com a data no nome.

| # | De | Para | Decisão |
|---|---|---|---|
| 1 | ata reuniao equipe.txt | _arquivo/ata-reuniao-equipe_ate-2026-04-14.txt | descartar |
| 2 | checklist audiencia trabalhista.md | audiencias-e-diligencias/checklist-audiencia-trabalhista.md | usar |
| 3 | checklist documentos auxílio doença.docx | atendimento-e-triagem/checklist-documentos-auxilio-doenca.docx | usar |
| 4 | Contestação trabalhista padrão NÃO USAR.docx | _arquivo/modelo-contestacao-trabalhista_ate-2020-02-10.docx | descartar |
| 5 | Contestacao trabalhista padrao novo.docx | producao-de-pecas/modelos/trabalhista/modelo-contestacao.docx | atualizar |
| 6 | contrato honorarios antigo.docx | _arquivo/modelo-contrato-honorarios_ate-2019-05-03.docx | descartar |
| 7 | Cópia de checklist documentos auxílio doença.docx | (não copia) | descartar |
| 8 | criterios relevancia movimentacao prev.txt | relacionamento-com-o-cliente/criterios-relevancia-movimentacao-previdenciario.txt | usar |
| 9 | extrato bancario cliente 0231.pdf | (não copia) | fora da base |
| 10 | holerite_marco_2023.pdf | (não copia) | fora da base |
| 11 | laudo pericial [NOME] [NOME].pdf | (não copia) | fora da base |
| 12 | manual do estagiario.docx | gestao-de-equipe/trilha-de-leitura.docx | atualizar |
| 13 | mensagens prontas whatsapp andamento.txt | relacionamento-com-o-cliente/modelos-mensagem-por-categoria.txt | usar |
| 14 | Modelo Inicial Aposentadoria Especial FINAL.docx | _arquivo/modelo-inicial-aposentadoria-especial-previdenciario_ate-2021-03-15.docx | descartar |
| 15 | Modelo Inicial Aposentadoria Especial FINAL2.docx | _arquivo/modelo-inicial-aposentadoria-especial-previdenciario_ate-2022-08-02.docx | descartar |
| 16 | Modelo Inicial Aposentadoria Especial v3 revisado (1).docx | (não copia) | descartar |
| 17 | Modelo Inicial Aposentadoria Especial v3 revisado.docx | producao-de-pecas/modelos/previdenciario/modelo-inicial-aposentadoria-especial.docx | atualizar |
| 18 | padrao nomes de arquivos.txt | comum/padrao-nomes-e-pastas.txt | atualizar |
| 19 | Peticoes antigas/embargos declaracao modelo.docx | producao-de-pecas/modelos/modelo-embargos-declaracao.docx | atualizar |
| 20 | Peticoes antigas/replica INSS 2019.docx | producao-de-pecas/modelos/previdenciario/modelo-replica-inss.docx | atualizar |
| 21 | POP peticao inicial FINAL_revisado2.docx | (não copia) | fora da base |
| 22 | post instagram ideias.txt | _arquivo/post-instagram-ideias_ate-2026-03-03.txt | descartar |
| 23 | proposta honorarios modelo.docx | comercial/modelo-proposta-honorarios.docx | usar |
| 24 | quesitos pericia medica modelo.docx | producao-de-pecas/modelos/modelo-quesitos-pericia-medica.docx | usar |
| 25 | Recurso inominado consumidor.docx | producao-de-pecas/modelos/consumidor/modelo-recurso-inominado.docx | atualizar |
| 26 | regua cobranca.txt | financeiro-e-cobranca/regua-de-cobranca.txt | usar |
| 27 | Réplica [NOME] [NOME] processo [PROCESSO].docx | producao-de-pecas/modelos/modelo-replica.docx | atualizar |
| 28 | roteiro triagem familia.md | atendimento-e-triagem/roteiro-triagem-familia.md | atualizar |
| 29 | tabela honorarios 2023.xlsx | _arquivo/tabela-interna-honorarios_ate-2023-01-20.xlsx | descartar |
| 30 | tabela honorarios 2024 atualizada.xlsx | comercial/tabela-interna-honorarios.xlsx | atualizar |

**Como aprovar e aplicar**

1. Abra `plano-de-reorganizacao.tsv` numa planilha (ou confira linha a linha na conversa).
2. Em cada linha que o advogado aprovar, escreva `sim` na coluna `ok_do_advogado`. Ajuste `setor`, `nome_novo` e `destino` se quiser outro lugar ou outro nome.
3. Linha com alerta só é copiada com `sim` também em `anonimizacao_conferida`: quer dizer que o advogado abriu o arquivo e confirmou que não tem dado de cliente, ou trocou a `origem` pelo caminho de uma versão anonimizada feita por ele.
4. Rode primeiro a simulação e depois a cópia:

```
python3 scripts/inventariar_pasta.py --aplicar <saida>/plano-de-reorganizacao.tsv --origem "<pasta original>" --destino "<pasta>/escritorio/04-base" --simular
python3 scripts/inventariar_pasta.py --aplicar <saida>/plano-de-reorganizacao.tsv --origem "<pasta original>" --destino "<pasta>/escritorio/04-base"
```

Tudo que entra na base chega como **rascunho**, com o cabeçalho da montar-base (no próprio arquivo .md ou numa ficha .md ao lado). Só vira "em uso" depois do critério de entrada da montar-base.

## 6. O que os POPs pedem

POPs lidos: POP-REL-01 Andamento no WhatsApp (Em teste)

| POP | Passo | O que o POP pede | O POP diz que existe? | Na pasta |
|---|---|---|---|---|
| POP-REL-01 | 2 | Critérios de relevância de movimentação (previdenciário) | em parte | #8 criterios relevancia movimentacao prev.txt |
| POP-REL-01 | 3 | Modelos de mensagem por categoria | sim | #13 mensagens prontas whatsapp andamento.txt |
| POP-REL-01 | 4 | Glossário de termos processuais em linguagem simples | não | não achei: criar na montar-base |
| POP-REL-01 | 5 | Perguntas frequentes de clientes | não | não achei: criar na montar-base |
| POP-REL-01 | 6 | Checklist de documentos por benefício | sim | #3 checklist documentos auxílio doença.docx |

## 7. Próximo passo

Com a triagem confirmada e a cópia feita, siga na `montar-base` a partir do passo 3 (triagem), depois criar o que falta a partir dos esqueletos, critério de entrada, casos de teste e Projeto no Claude. O rascunho do índice está em `INDICE-rascunho.md`, ao lado deste arquivo.
