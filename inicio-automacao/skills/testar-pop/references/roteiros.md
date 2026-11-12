# Roteiros de análise da esteira

Cinco roteiros, na ordem da esteira. Cada um diz como a skill faz a análise dentro da conversa e traz a versão para colar no Projeto do escritório no Claude, quando quem testa prefere rodar lá (é o caso do teste com a IA, que deve rodar no ambiente real). Antes de colar: troque o que está entre colchetes e não cole dado de cliente que não seja necessário.

## 1. Auditar o POP com o checklist de qualidade

**Quando:** passo 2 da skill, antes do teste de mesa. Complementa a `auditar-riscos`, que lê o mesmo POP pelo lado do risco.

**Como a skill faz:**
- Lê o POP inteiro uma vez, sem corrigir nada.
- Para cada um dos 13 itens: situação (ok, parcial ou falta), o trecho do POP que comprova ou que falha (copiado), a correção sugerida.
- Reescreve só os trechos que falham. Nunca o POP inteiro.
- Lista os passos sem verbo, sem responsável ou sem critério de pronto, cada um reescrito.
- Aponta os S que deveriam ser A e os A que deveriam ser H, pelos seis critérios da `classificar-sah`. Na dúvida, a sigla mais humana.
- Responde: pronto para o teste de mesa? Se qualquer item (E) estiver parcial ou falta, a resposta é não.
- Não inventa prazo, regra, número de lei, artigo ou provimento. Onde falta decisão, `[A DEFINIR]`. Norma mencionada, `[CONFERIR]`.

**Para colar no Projeto:**
```
Você vai auditar um POP (procedimento operacional padrão) de um escritório de advocacia que usa inteligência artificial em alguns passos. Cada passo tem uma sigla:
- S (Substituição): a IA faz no lugar da pessoa;
- A (Auxílio): a IA prepara, resume, rascunha ou revisa, e a pessoa decide;
- H (Humano): decisão estratégica, julgamento ético, conversa delicada, assinatura e responsabilidade.

POP:
[COLE AQUI O POP]

Audite com estes 13 itens. Os marcados com (E) são eliminatórios.
1. Objetivo em uma frase, com o resultado para o cliente ou para o escritório.
2. Gatilho: um acontecimento observável que inicia o processo.
3. Entradas: cada modelo, lista e critério com nome e lugar, inclusive o que a IA consulta.
4. (E) Cada passo começa com verbo de ação e diz quem executa e quem confere.
5. Cada passo tem critério de pronto, em especial os passos A.
6. (E) Cada sigla S, A ou H tem justificativa.
7. Exceções: cada decisão tem o "e se não?" escrito.
8. Prazo do gatilho à saída e das etapas críticas.
9. Saída: o que foi entregue, para quem, onde ficou registrado.
10. (E) Onde a IA entra: o que faz, o que consulta, em que conta roda e o que se anonimiza antes.
11. (E) Nunca sai sem revisão humana: lista curta, com quem revisa e o que confere.
12. Indicador com fórmula, fonte e linha de base.
13. Dono, versão, data e data da próxima revisão.

Entregue:
1. Uma tabela com as colunas: item, situação (ok, parcial ou falta), trecho do POP que comprova ou que falha (copie o trecho), correção sugerida.
2. A lista dos passos sem verbo, sem responsável ou sem critério de pronto, cada um reescrito.
3. Os passos S que deveriam ser A e os passos A que deveriam ser H, pelos critérios: clareza da regra, volume, risco do erro, dado sensível, relação com o cliente e quem assina o resultado. Na dúvida, a sigla mais humana.
4. A resposta: o POP está pronto para o teste de mesa? Se qualquer item (E) estiver como "parcial" ou "falta", a resposta é não.

Regras: não reescreva o POP inteiro, só os trechos que falham. Não invente prazo, regra, número de lei, artigo ou provimento. Onde faltar informação, escreva [A DEFINIR]. Se mencionar alguma norma, marque [CONFERIR].
```

## 2. Ler o POP como quem acabou de chegar

**Quando:** ensaio antes do teste de mesa com uma pessoa, ou complemento no escritório solo. Nunca substitui o teste com uma pessoa: a IA completa lacunas com bom senso sem perceber, e a pessoa nova trava.

**Como a skill faz:** segue o texto ao pé da letra com um caso anonimizado ou fictício, sem poder perguntar. Para cada passo, diz o que faria, onde teria que adivinhar (e qual palpite daria), que informação buscaria fora do POP e onde imagina que ela está, e como saberia que o passo terminou. Depois lista as perguntas que faria ao autor, da mais grave para a menos grave, os trechos com duas leituras (mostrando as duas) e se chegaria a uma saída. Não melhora o POP: cada lacuna completada sozinha é uma lacuna escondida.

**Para colar no Projeto:**
```
Faça de conta que você entrou hoje no meu escritório de advocacia e recebeu o POP abaixo para executar sozinho, com o caso abaixo, sem poder perguntar nada a ninguém. Siga o texto ao pé da letra.

POP:
[COLE AQUI O POP]

Caso (anonimizado ou fictício):
[DESCREVA O CASO SEM NOMES, DOCUMENTOS OU NÚMEROS REAIS]

Para cada passo, diga:
- o que exatamente você faria;
- onde teria que adivinhar, e qual palpite daria;
- que informação você buscaria fora do POP, e onde imagina que ela está;
- como você saberia que o passo terminou.

Depois:
1. Liste as perguntas que você faria ao autor do POP, da mais grave para a menos grave.
2. Aponte os trechos que admitem duas leituras, mostrando as duas.
3. Diga se você chegaria a uma saída, e qual.

Importante: não melhore o POP e não preencha lacunas com bom senso. O objetivo é encontrar as lacunas, então cada uma que você completar sozinho é uma lacuna escondida.
```

## 3. Gerar casos de teste

**Quando:** falta caso real anonimizado para o teste com a IA, falta o caso difícil, ou a conta de IA ainda é pessoal (aí só caso fictício).

**Como a skill faz:** pergunta a área e, sem dados pessoais, os tipos de caso que mais aparecem e os que mais dão trabalho. Cria quatro casos: fácil (caminho feliz), comum (o tipo que mais aparece, com uma ou duas variações), difícil (informação faltando, documento conflitante ou notícia ruim) e exceção (ativa uma exceção escrita ou revela uma que falta). Para cada um: código, por que tem essa dificuldade, material de entrada com nomes evidentemente fictícios, gabarito de cada passo S e A (e em qual passo uma pessoa assume), e a armadilha mais provável. No fim, sugere um erro plantado para testar a revisão. Não cita norma, artigo ou jurisprudência: descreve a situação e marca `[CONFERIR]`.

**Para colar no Projeto:**
```
Quero testar o POP abaixo antes de colocar a equipe para usar. Crie casos de teste fictícios, realistas para um escritório de [ÁREA DE ATUAÇÃO], sem nenhum dado real de cliente.

POP:
[COLE AQUI O POP]

Os tipos de caso que mais aparecem no meu dia a dia, e os que mais dão trabalho (sem dados pessoais):
[DESCREVA EM POUCAS LINHAS]

Crie 4 casos:
1. Fácil: caminho feliz, informação completa, nenhuma exceção.
2. Comum: o tipo que mais aparece, com uma ou duas variações.
3. Difícil: informação faltando, documento conflitante ou notícia ruim para o cliente.
4. Exceção: um caso que ativa uma exceção escrita no POP ou que revela uma exceção que falta.

Para cada caso, entregue:
- código (CASO-01 a CASO-04) e por que ele tem essa dificuldade;
- o material de entrada, com nomes evidentemente fictícios (Cliente A, Empresa B) e sem número de processo, CPF ou benefício que pareça real;
- o gabarito: o que uma execução correta produz em cada passo S e A, e em qual passo uma pessoa precisa assumir;
- a armadilha: o erro mais provável que a IA ou uma pessoa cometeria nesse caso.

No final, sugira um erro plantado para testar a revisão humana: um defeito discreto, como uma data trocada ou um pedido faltando, dizendo em qual passo inserir e o que o revisor deveria perceber.

Não cite norma, artigo ou jurisprudência. Se o caso depender de uma regra jurídica, descreva a situação e marque [CONFERIR].
```

## 4. Comparar a saída da IA com o trabalho humano

**Quando:** passo 4 da skill, para preencher cada ficha do teste com a IA. Um passo e um caso por vez.

**Como a skill faz:** recebe a instrução do passo como está no POP, o material do caso, a versão da IA e a versão da pessoa. Compara em correção, completude, padrão do escritório (o código é a régua), invenção e saber parar. Entrega uma tabela (critério, versão da IA, versão da pessoa, diferença relevante), o veredito do passo, a decisão sugerida com duas linhas de justificativa e o que faltou na instrução ou no material. Não presume que a versão da pessoa está certa: se ela tiver erro, aponta também.

**Para colar no Projeto:**
```
Compare duas versões do mesmo trabalho, feitas para o mesmo caso anonimizado. A versão A foi feita pela IA seguindo o passo [NÚMERO E VERBO] do POP. A versão B foi feita por uma pessoa da equipe.

Instrução do passo, como está no POP:
[COLE]

Material do caso (anonimizado):
[COLE]

Versão A (IA):
[COLE]

Versão B (pessoa):
[COLE]

Compare nestes critérios:
- correção: fatos, datas, valores e nomes conferem com o material?
- completude: o que uma versão tem e a outra não?
- padrão do escritório: modelo, estrutura e tom, usando o código do escritório deste projeto como régua;
- invenção: alguma das versões traz fato, norma ou jurisprudência que não está no material?
- saber parar: havia ponto que pedia decisão de uma pessoa? A versão A sinalizou?

Entregue uma tabela com: critério, versão A, versão B, diferença relevante. Depois:
1. Veredito para o passo: APROVADO, APROVADO COM AJUSTE ou REPROVADO.
2. Decisão sugerida: manter a sigla, subir de S para A, subir de A para H, reescrever a instrução, criar exceção ou completar a base de conhecimento. Justifique em duas linhas.
3. O que faltou na instrução ou no material para a versão A acertar.

Não presuma que a versão B está certa. Se ela tiver erro, aponte também.
```

## 5. Analisar o resultado do piloto

**Quando:** no fechamento das duas semanas, antes da conversa com o titular.

**Como a skill faz:** roda `scripts/analisar_piloto.py` sobre o registro (ou faz a conta à mão e mostra). Depois, nesta ordem: números por semana; semana 2 contra a linha de base, dizendo se o tipo de caso mudou entre os períodos; passos e tipos de caso que concentram erro, retrabalho ou desvio; sinais de carimbo; recomendação para cada passo S e A (manter, ajustar a instrução, completar a base ou subir a sigla), justificada com os números; e a resposta "prontos para a automação?" (sim, sim com ressalvas ou não). Se algum erro chegou ao cliente ou ao tribunal, a resposta é não até a causa estar corrigida e testada. Usa só os números do registro: não completa lacuna, e se faltar dado para uma conta, diz qual e segue sem ela.

**Para colar no Projeto:**
```
Fiz um piloto de duas semanas de um POP com IA no meu escritório de advocacia e preciso de uma análise para decidir o que vai para a automação.

POP (versão usada na semana 2):
[COLE AQUI O POP]

Linha de base, antes da IA:
- tempo médio por execução: [MINUTOS]
- retrabalho: [% OU "NÃO MEDIDO"]
- tipo de caso no período da linha de base: [DESCREVA]

Registro do piloto, uma linha por execução, sem dados de cliente:
[COLE O REGISTRO]

Mudanças feitas no POP entre a semana 1 e a semana 2:
[LISTA]

Faça, nesta ordem:
1. Para cada semana: número de execuções, tempo médio de execução, tempo médio de revisão, tempo total médio (execução + revisão + retrabalho), percentual de retrabalho, erros pegos por tipo, erros que chegaram ao cliente ou ao tribunal, desvios do POP. Mostre as contas.
2. Compare a semana 2 com a linha de base. Se o tipo de caso foi diferente entre os períodos, diga como isso afeta a comparação.
3. Aponte os passos e os tipos de caso que concentram erro, retrabalho ou desvio.
4. Procure sinais de revisão que virou carimbo: revisões muito curtas e sem nenhuma correção por várias execuções seguidas.
5. Para cada passo S e A, recomende: manter, ajustar a instrução, completar a base de conhecimento ou subir a sigla. Justifique com os números.
6. Responda: os passos S e A estão prontos para automação? Sim, sim com ressalvas, ou não. Se algum erro chegou ao cliente ou ao tribunal, a resposta é não até a causa estar corrigida e testada.

Regras: use só os números que eu passei. Não invente dado e não complete lacunas do registro. Se faltar informação para algum cálculo, diga qual e siga sem ele.
```
