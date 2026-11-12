# Mudança de sigla com dados

Leia este arquivo quando alguém perguntar se um passo já pode mudar de sigla, na trimestral (passo 2) e sempre que um erro chegar ao cliente ou ao processo.

**Status desta regra:** sugestão conservadora do plugin, a validar pelo escritório. O método define a direção ("na dúvida, a sigla mais humana"; descer "com o tempo, olhando o indicador e os erros pegos na revisão"), mas não fixa números. Todo número entre colchetes abaixo é sugestão e fica `[A DEFINIR]` até o escritório aprovar e gravar a versão dele no código do escritório (seção "Como decidimos").

## 1. De onde vêm os dados

| Dado | Onde está |
|---|---|
| Execuções do passo | `05-automacoes/<nome>/registro-de-uso.md` ou o registro de usos do piloto em `01-cultura/mudanca/` |
| Erros pegos na revisão | As mesmas fontes, coluna "erro pego" e "qual erro" |
| Incidentes e quase incidentes | `06-medicao/incidentes.md` |
| Retrabalho da IA | Revisões quinzenais em `06-medicao/revisoes/` |
| Indicador do POP | Campo 12 do POP e painéis mensais |

Sem registro, não há descida. "Está acertando quase sempre" sem número não conta.

## 2. O que conta como erro pego

Sugestão de critério `[A DEFINIR]`:
- **Conta como erro:** dado trocado (nome, data, valor, prazo, número), citação ou jurisprudência que não confere na fonte, critério do POP não aplicado, tom fora do código, informação inventada, dado de cliente que não deveria estar ali.
- **Não conta como erro:** ajuste de estilo que não muda o sentido (uma vírgula, a ordem de duas frases), desde que quem revisou anote "ajuste de forma".
- Na dúvida, conta como erro.

## 3. Princípios fixos

1. Os cinco passos da linha vermelha nunca descem de H: escolha de tese ou estratégia; notícia ruim ao cliente; assinatura e responsabilidade técnica; aconselhamento de cliente vulnerável; envio de peça, proposta ou mensagem jurídica sem revisão humana.
2. Em Família, caso com sinal de violência, coação ou risco sai do fluxo e não entra em automação.
3. A trava por estágio da `classificar-sah` vence qualquer contagem.
4. Subir é imediato. Descer só na revisão trimestral, com os dados do trimestre na mesa.
5. Depois de uma subida, a contagem para descer recomeça do zero.
6. Volume alto não é motivo para descer.

## 4. Descer de A para S

Todas as condições, ao mesmo tempo:

| Condição | Sugestão `[A DEFINIR]` |
|---|---|
| O resultado fica dentro do escritório (não sai para cliente, tribunal ou público sem conferência depois) | Fixo: se sai, continua A |
| Execuções seguidas sem erro pego | [30] |
| Tempo mínimo de uso como A | [8 semanas] |
| Indicador do POP | Estável ou melhor nas duas últimas mensais |
| Retrabalho da IA nesse passo | Zero no período |
| Plano de amostra escrito | Quem confere, o que confere, [1 a cada 5] nas primeiras [4 semanas] como S, depois [1 a cada 10] |
| Aprovação | Dono do POP e patrocinador; guardião se houver dado de cliente. Solo: decisão escrita, confirmada depois de pausa de 24 horas |

**Exemplo (números ilustrativos).** Passo "Montar o resumo mensal interno de andamentos", sigla A. No trimestre: 42 execuções, as últimas 34 sem erro pego, indicador estável, nenhum retrabalho. O resultado fica dentro do escritório (o cliente recebe outra mensagem, revisada). Passa nas condições: proposta de descer para S, com amostra de 1 em 5 nas primeiras 4 semanas. Se o mesmo passo gerasse a mensagem enviada ao cliente, continuaria A.

## 5. Descer de H para A

Só para passo fora da linha vermelha, e só quando o julgamento que o passo exigia virou critério escrito na base de conhecimento (por exemplo, uma lista do que é movimentação relevante que antes estava na cabeça do advogado).
1. O critério escrito existe em `04-base/`, com dono e data.
2. O passo passa por um piloto de 2 semanas como A, com revisão em tudo, pelo funil do núcleo.
3. A decisão sai na trimestral, com o resultado do piloto.

## 6. Subir na hora

Qualquer pessoa aciona. O dono do POP confirma no mesmo dia e registra.

| O que aconteceu | Efeito |
|---|---|
| Erro chegou ao cliente ou ao processo, ou dado saiu (incidente), num passo S | Sobe para A na hora |
| Incidente num passo A | Sobe para H: a IA para nesse passo até a causa estar corrigida no POP e a revisão ter objeto claro. A volta para A se decide na mensal seguinte |
| Erros na amostra de um passo S | [2 erros do mesmo tipo em 30 dias, ou 1 erro em prazo, valor ou dado de cliente]: sobe para A |
| Mudança de estágio (conta profissional perdida, regra de uso desatualizada, critério ou base do passo mudou ou ficou sem dono) | A trava por estágio volta a valer |
| Mudou a norma, o sistema ou o procedimento de que o passo depende | Sugestão: sobe um degrau até nova contagem [A DEFINIR] |
| Revisar leva mais tempo do que fazer à mão por duas semanas seguidas | O processo volta para a etapa de ajuste (`implantar-a-mudanca`); a sigla não desce por isso |

## 7. Como registrar

No POP, no passo que mudou:
- sigla nova com `[ALTERADO]`;
- versão nova do POP e data;
- motivo, com os números usados (execuções, erros, indicador) ou o incidente;
- quem aprovou.

Na revisão em que foi decidido (trimestral, mensal ou registro do incidente), uma linha na tabela de siglas. Se a mudança afeta uma automação instalada, ofereça `desenhar-automacao` para ajustar a instrução e o plano para erro, e `pop-para-skill` para atualizar a skill.
