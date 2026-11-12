# Estimar a redução de tempo a partir do POP

Leia no passo 6 do `medir-retorno`. Serve para preencher o percentual de redução da calculadora com critério, passo a passo, em vez de chutar um número para o setor inteiro.

## O que precisa existir

- O POP do setor com a sigla de cada passo (S, A ou H), vindo do `escrever-pop` ou da `classificar-sah`.
- O tempo médio de cada passo, medido na linha de base (minutos por unidade e volume por semana).

Sem POP, ofereça o `escrever-pop`. Sem linha de base, faça a estimativa com os tempos que o advogado souber, escreva "estimado" ao lado de cada um e diga que ela só serve para escolher, nunca para afirmar resultado.

## Regras

1. **Passo H fica com redução zero.** A IA pode preparar o material em volta, mas o tempo do passo continua com a pessoa.
2. **Em passo A e S, a revisão humana entra na conta.** Passo A cria tempo de revisão de tudo. Passo S pede conferência por amostra. A redução estimada é o tempo antes menos o tempo com IA, já somada a revisão que vai continuar existindo.
3. **Faixa conservadora: mínimo e máximo,** com o raciocínio em uma frase por passo.
4. **Sem percentual de mercado nem promessa de fornecedor.** O percentual é palpite do escritório, olhando o próprio POP, e quem confirma é a medição.
5. **Não arredondar para cima.** Se um dado parecer inconsistente (volume que não fecha com o tempo, passo sem tempo), pergunte antes de calcular.

## Fluxo

1. Peça o POP com tempos e siglas (ou leia de `escritorio/03-pops/<setor>/`).
2. Para cada passo, pergunte só o que faltar, uma pergunta por vez: quanto tempo leva hoje, quantas vezes por semana, e, nos passos A, quanto tempo a revisão deve levar.
3. Monte a tabela abaixo. Mostre e peça ajuste.
4. Some e entregue a redução do setor em horas por semana e em percentual, no cenário mínimo e no máximo.
5. Leve a faixa para a calculadora (`"reducao_pct": {"min": x, "max": y}`).

## Tabela de estimativa

| Passo | Sigla | Minutos por vez hoje | Vezes por semana | Horas por semana hoje | Minutos com IA, com revisão (mín. e máx.) | Redução mínima | Redução máxima | Raciocínio em uma frase |
|---|---|---|---|---|---|---|---|---|

Redução do setor (%) = soma das horas por semana reduzidas ÷ soma das horas por semana hoje × 100, em cada cenário.

## Exemplo resolvido (números fictícios)

Setor Relacionamento com o cliente, 18 h por semana na linha de base.

| Passo | Sigla | Horas por semana hoje | Redução mínima | Redução máxima | Raciocínio |
|---|---|---|---|---|---|
| Conferir movimentações e separar as relevantes | S | 3,4 | 1,4 h | 2,0 h | A IA separa e a pessoa confere por amostra; a amostra toma tempo no começo |
| Escrever a atualização de andamento | A | 4,5 | 1,1 h | 1,8 h | A IA rascunha no tom do código, mas toda mensagem é revisada antes de sair |
| Responder dúvida no WhatsApp | A | 6,0 | 0,9 h | 1,8 h | Rascunho ajuda nas dúvidas repetidas; as personalizadas continuam lentas |
| Dar notícia desfavorável | H | 2,0 | 0 | 0 | Linha vermelha: o advogado liga |
| Pedir documento pendente | S | 2,1 | 0,6 h | 0,9 h | Mensagem de modelo aprovado, conferência por amostra |
| **Total** | | **18,0** | **4,0 h (22%)** | **6,5 h (36%)** | |

Leitura: a faixa de 22% a 36% é estimativa. Ela entra na calculadora como `{"min": 22, "max": 36}` e é conferida na medição depois de pelo menos 4 semanas de uso.
