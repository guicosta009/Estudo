# Prompts do ciclo da peça

Cinco prompts que cobrem o ciclo, na ordem de uso. Eles rodam no **Projeto de peças** no Claude, com o código do escritório, o banco de modelos, o caderno de teses, a ficha de briefing e o checklist de revisão. Troque o que está entre colchetes em maiúsculas antes de enviar.

A skill `organizar-producao-de-pecas` grava estes prompts no Projeto (passo 8) e os POPs de peça os citam pelo número. Quando o escritório validar um prompt, registre em `escritorio/01-cultura/mudanca/registro-de-prompts.md` (quem validou e quando).

**Antes de colar:** documento de cliente só anonimizado e só em conta profissional. Nenhum destes prompts substitui a conferência na fonte: todos pedem que a IA marque `[CONFERIR]` em vez de inventar jurisprudência, súmula, artigo ou prazo. Nas peças, `[CONFERIR]` quer dizer: ninguém abriu a fonte oficial ainda.

Marcações usadas nos prompts:
- `[CONFERIR]`: citação, norma ou regra técnica que ainda não foi aberta na fonte oficial.
- `[A CONFIRMAR]`: fato, data, valor ou documento que não consta nos documentos recebidos.
- `[A DEFINIR]`: decisão que é do advogado (tese, pedidos) e ainda não foi tomada.
- `[SÓ RELATO]`: fato que o cliente contou e nenhum documento mostra.

| # | Prompt | Etapa do ciclo | Passo nos POPs |
|---|---|---|---|
| 1 | Montar o briefing a partir dos documentos anonimizados | 2 | Ficha de briefing |
| 2 | Pesquisa com tabela de citações a conferir | 5 | Pesquisar e montar a tabela de citações |
| 3 | Minuta a partir do modelo do escritório | 6 | Redigir a minuta |
| 4 | Revisão técnica com lista de pontos a conferir | 7 e 8 | Leitura crítica e revisão de forma |
| 5 | Transformar uma peça boa em modelo do banco | Banco de modelos | Alimentar o banco |

## 1. Montar o briefing a partir dos documentos anonimizados

Etapa 2. A IA preenche a ficha, a pessoa confere.

```
Você vai montar a ficha de briefing de uma peça do meu escritório a partir dos documentos que eu vou colar ou anexar. Os documentos já estão anonimizados: as partes aparecem como [CLIENTE], [PARTE CONTRÁRIA], [EMPRESA], [TESTEMUNHA 1] e assim por diante. Mantenha esses códigos e não tente descobrir quem são.

Peça a ser feita: [TIPO DE PEÇA, EX.: PETIÇÃO INICIAL, CONTESTAÇÃO, RECURSO]
Área: [ÁREA]
Lado do cliente: [AUTOR, RÉU, RECORRENTE, RECORRIDO]
Ata da consulta ou resumo do caso: [COLE AQUI]
Documentos: [ANEXE OU COLE, COM O NOME DE CADA ARQUIVO]

Use a ficha de briefing que está neste Projeto e preencha:
1. Identificação: tipo de peça, área, lado do cliente.
2. Objetivo da peça em uma frase.
3. Fatos em ordem cronológica, um por linha, cada um com a fonte: nome do documento e página. Fato que só aparece no relato do cliente, sem documento, marque como [SÓ RELATO].
4. Documentos disponíveis, numerados, com o que cada um prova.
5. Lacunas e contradições: documento que falta, data ou valor que não bate entre documentos, fato sem prova.
6. Pedidos possíveis que os fatos sugerem, em lista, para o advogado decidir. Não escolha nenhum.
7. Tese escolhida: deixe em branco com a marcação [A DEFINIR].
8. Valores que aparecem nos documentos, com a fonte de cada um.
9. O que não pode aparecer na peça: dado sensível desnecessário e informação de terceiros.
10. Perguntas que eu preciso fazer ao cliente antes da minuta.

Regras:
- Não invente fato, data, valor ou documento. O que não estiver nos documentos fica [A CONFIRMAR].
- Não cite jurisprudência, súmula, artigo de lei nem prazo nesta etapa.
- Se algum documento tiver dado pessoal que escapou da anonimização (CPF, endereço, nome completo), me avise no começo da resposta e não reproduza o dado.
- Entregue a ficha em texto simples, pronta para eu conferir campo por campo.
```

## 2. Pesquisa com tabela de citações a conferir

Etapa 5. Ponto de partida da pesquisa. A citação final sai da fonte oficial.

```
Preciso pesquisar fundamentação para uma peça e quero um ponto de partida organizado para eu conferir na fonte oficial.

Tese escolhida pelo advogado: [DESCREVA A TESE]
Fatos centrais, anonimizados: [RESUMO EM POUCAS LINHAS]
Área e tipo de peça: [ÁREA, PEÇA]
Onde vai tramitar: [JUSTIÇA, TRIBUNAL OU INSTÂNCIA, SE SOUBER]

O que eu quero:
1. Linhas de pesquisa: os argumentos jurídicos que sustentam a tese e os contra-argumentos mais prováveis da outra parte.
2. Termos de busca que eu posso usar nos sites oficiais dos tribunais e na legislação oficial.
3. Uma tabela de candidatos a citação com as colunas: tipo (lei, súmula, precedente, doutrina), referência como você lembra, o que ela sustentaria na peça, seu grau de certeza (alto, médio, baixo) e status. Preencha a coluna status com [CONFERIR] em todas as linhas.

Regras:
- Se você não tiver certeza de que uma decisão existe, com número, órgão e data, não escreva a referência. Descreva o que eu devo buscar.
- Nunca invente número de processo, súmula, tema, artigo, relator ou data.
- Não trate nenhuma linha da tabela como confirmada. Nada dela vai para a peça antes de eu abrir a fonte oficial e conferir o texto.
```

## 3. Minuta a partir do modelo do escritório

Etapa 6. Por blocos, só com a ficha conferida e as citações já checadas.

```
Vamos redigir a minuta de uma peça a partir do modelo do meu escritório. Neste Projeto estão o código do escritório e o banco de modelos. Siga o tom e as regras do código.

Modelo a usar: [CÓDIGO DO MODELO NO ÍNDICE DO BANCO, EX.: CONS_INICIAL_cobranca-indevida, VERSÃO 3.0] (se não estiver no Projeto, eu colo aqui)
Ficha de briefing conferida: [COLE A FICHA, COM A TESE E OS PEDIDOS JÁ DECIDIDOS]
Citações conferidas na fonte: [COLE A TABELA DE CITAÇÕES CONFERIDAS, OU ESCREVA "NENHUMA"]

Como quero que você trabalhe:
1. Antes de escrever, me diga em até 5 linhas como vai usar o modelo: que blocos mantém, quais adapta e quais o caso não pede. Espere o meu ok.
2. Escreva por blocos, na ordem do modelo: qualificação com campos, fatos, fundamentos, pedidos. Pare depois de cada bloco para eu revisar.
3. Nos fatos, use só o que está na ficha, na ordem dela, e indique entre colchetes o documento de cada fato, ex.: [DOC 3, p. 2]. Fato marcado [SÓ RELATO] só entra se a ficha disser que o advogado decidiu incluir.
4. Nos fundamentos, siga a tese escolhida. Não troque nem acrescente tese. Se achar que falta algo, me pergunte em vez de escrever.
5. Use apenas as citações da tabela de citações conferidas. Se precisar de outra, não invente: escreva [CONFERIR: o que precisa ser buscado].
6. Nos pedidos, use só os pedidos decididos na ficha. Valores só os da ficha, com a mesma grafia.
7. Mantenha os dados das partes como campos: [CLIENTE], [QUALIFICAÇÃO DO CLIENTE], [PARTE CONTRÁRIA]. A qualificação real entra depois, fora da IA, a partir do cadastro.
8. No final, liste tudo o que ficou marcado como [CONFERIR], [A CONFIRMAR] ou [A DEFINIR].

Nunca invente jurisprudência, súmula, número de artigo, prazo ou decisão.
```

## 4. Revisão técnica com lista de pontos a conferir

Etapas 7 e 8. A IA aponta, a pessoa decide. Ela não reescreve a peça.

```
Quero uma primeira revisão técnica da minuta abaixo, antes da minha leitura final. Você não vai reescrever a peça. Vai me entregar uma lista de pontos para eu conferir e decidir.

Tipo de peça: [TIPO]
Ficha de briefing conferida: [COLE A FICHA]
Minuta: [COLE A MINUTA, COM OS DADOS ANONIMIZADOS]
Tabela de citações conferidas: [COLE A TABELA]
Checklist de revisão do escritório: está neste Projeto.

Faça a revisão em quatro partes:
1. Leitura da parte contrária: leia como o advogado do outro lado leria e aponte os pontos mais fáceis de atacar, do mais grave para o menos grave.
2. Coerência: cada pedido tem fato e fundamento que o sustenta? Algum fato importante da ficha ficou de fora? Algum fato da minuta não está na ficha?
3. Citações: liste todas as citações da minuta (lei, súmula, precedente, doutrina) com o trecho da peça, o que foi citado e se está na tabela de citações conferidas (sim ou não). Marque [CONFERIR] em toda citação que não estiver na tabela. Não diga se a citação está certa ou errada: você não está com a fonte aberta.
4. Forma, pelo checklist do escritório: nomes, números, datas e valores iguais em toda a peça e iguais à ficha; documento citado que não está na lista; campo [CLIENTE] esquecido; frase genérica que não diz nada sobre o caso.

Formato: uma tabela por parte, com as colunas "onde está" (bloco e parágrafo), "o que vi" e "o que sugiro conferir", do mais grave ao menos grave.

Regras: não invente jurisprudência, súmula, artigo ou prazo para "corrigir" a peça. Não reescreva trechos inteiros, a não ser que eu peça. A decisão sobre cada ponto é minha.
```

## 5. Transformar uma peça boa em modelo do banco

Banco de modelos, passo "limpe e marque os campos". A escolha da peça é do advogado.

```
Vou colar uma peça que deu certo no meu escritório e quero transformá-la em modelo do nosso banco de modelos.

Peça: [COLE A PEÇA]
Área e tipo de peça: [ÁREA, TIPO]
Dono do modelo: [NOME]

Faça assim:
1. Anonimize: troque todo dado de cliente, parte contrária, terceiros, número de processo e valores do caso por campos entre colchetes, como [CLIENTE], [PARTE CONTRÁRIA], [PROCESSO], [VALOR 1]. No final, liste cada campo criado.
2. Separe o que é fixo (estrutura e argumentos que valem para todo caso desse tipo) do que é variável (fatos, pedidos específicos), marcando os blocos variáveis com [VARIÁVEL: o que preencher].
3. Marque toda citação de lei, súmula, precedente ou doutrina com [CONFERIR · última conferência: A DEFINIR], porque o modelo vai ser reutilizado e a citação precisa ser reconferida.
4. Preencha a ficha do modelo que está neste Projeto: código no padrão [ÁREA]_[TIPO]_[assunto], versão 1.0, quando usar, quando não usar, teses que o modelo usa, campos variáveis, dono e data.
5. Aponte trechos específicos demais daquele caso, que eu deveria tirar do modelo.

Não acrescente argumento, tese ou citação que não estava na peça original. Se algo estiver incompleto, marque [A DEFINIR].
```

Cuidado com este prompt: a peça original tem dado de cliente. Rode só em conta profissional e, se der, anonimize os nomes antes de colar. Confira cabeçalho, rodapé e propriedades do arquivo final, que costumam guardar o nome do cliente.
