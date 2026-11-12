# A calculadora de investimento e retorno

Leia no passo 7 do `medir-retorno`, quando for rodar a projeção, e sempre que precisar explicar uma conta ao advogado. O script `scripts/calcular_roi.py` aplica exatamente estas fórmulas.

## A conta que organiza tudo

- Valor da hora × horas devolvidas = retorno bruto.
- Retorno bruto − custo total da inovação = retorno líquido.
- "Se você não sabe para onde foi a hora economizada, ela não foi economizada."

O resultado da calculadora é uma **projeção** a partir das estimativas do escritório. Ele vira resultado só depois da medição (linha de base e medição depois de pelo menos 4 semanas de uso).

## Variáveis

| Variável | Chave no JSON | O que é |
|---|---|---|
| Modo | `modo` | `fat` (método 1, pelo faturamento) ou `direto` (valor da hora informado, métodos 2 ou 3) |
| Faturamento médio mensal | `faturamento_mensal` (`fat`) | Média dos últimos 6 ou 12 meses |
| Horas produtivas por mês | `horas_produtivas` (`hp`) | Soma das de quem produz trabalho faturável |
| Valor da hora | `valor_hora` (`vh`) | Só no modo direto |
| Ferramentas por mês | `ferramentas_mes` (`ferr`) | Assinaturas e upgrades que vieram com a IA |
| Horas de implantação | `horas_implantacao` (`himp`) | POP, Projeto, base, testes, aprendizado (uma vez) |
| Valor da hora de implantação | `valor_hora_implantacao` (`vimp`) | Em branco, usa o valor da hora |
| Outros custos únicos | `custos_unicos` (`unico`) | Treinamento, consultoria, configuração |
| Revisão humana nova | `revisao_h_semana` (`rev`) | Horas por semana de conferência do que a IA fez |
| Aproveitamento | `aproveitamento_pct` (`aprov`) | Quanto das horas devolvidas vira trabalho de fato. Seja conservador. |
| Setores | `setores` | Lista de `{setor, horas_semana, reducao_pct, origem}`. `reducao_pct` pode ser um número ou `{"min": x, "max": y}` |

Valores negativos, vazios ou inválidos viram 0. Redução e aproveitamento acima de 100 são limitados a 100, com aviso.

## Fórmulas exatas (SEM = 52 ÷ 12, cerca de 4,33 semanas por mês)

| Saída | Fórmula |
|---|---|
| Valor da hora (vh) | modo direto: o valor informado · modo fat: faturamento médio mensal ÷ horas produtivas |
| Horas devolvidas no setor por mês | horas por semana × min(redução %, 100) ÷ 100 × SEM |
| Horas devolvidas por mês | max(0, soma de (horas por semana × redução %) − revisão humana por semana) × SEM |
| Valor das horas devolvidas por mês | horas devolvidas por mês × vh × min(aproveitamento %, 100) ÷ 100 |
| Custo mensal | ferramentas por mês |
| Investimento inicial | horas de implantação × (valor da hora de implantação, se informado, senão vh) + outros custos únicos |
| Retorno líquido mensal | valor das horas devolvidas − custo mensal |
| ROI em 12 meses | (12 × valor − (12 × custo mensal + investimento inicial)) ÷ (12 × custo mensal + investimento inicial) × 100. Fica "n/d" se o denominador for 0 |
| Payback | líquido ≤ 0: "não se paga" (ou "n/d", se tudo estiver em 0) · inicial = 0: "imediato" · nos demais casos: investimento inicial ÷ retorno líquido mensal, em meses |

## Avisos automáticos

- Falta o valor da hora.
- Nenhum setor preenchido com horas e redução.
- Revisão humana igual ou maior que as horas devolvidas: "do jeito que está, a automação não devolve tempo".
- Aproveitamento em 0: o valor fica zero.
- Sem custo informado, não há ROI nem payback.

## Exemplo resolvido (números fictícios)

Escritório imaginário com 2 advogados e 1 secretária (arquivo `scripts/exemplos/roi-exemplo.json`).

- Valor da hora pelo método 1: R$ 30.000 de faturamento médio ÷ 250 horas produtivas dos dois advogados = R$ 120.
- Ferramentas: R$ 600 por mês (valor ilustrativo). Implantação: 40 h × R$ 120 = R$ 4.800, mais R$ 1.500 de treinamento: investimento inicial de R$ 6.300.
- Revisão humana: 3 h por semana. Aproveitamento: 60%.

| Setor | Horas por semana | Redução estimada | Devolvidas por semana |
|---|---|---|---|
| Atendimento e triagem | 10 | 30% | 3,0 |
| Comercial | 4 | 20% | 0,8 |
| Produção de peças | 20 | 25% | 5,0 |
| Prazos e controladoria | 6 | 15% | 0,9 |
| Audiências e diligências | 4 | 0% | 0 |
| Financeiro e cobrança | 4 | 20% | 0,8 |
| Relacionamento com o cliente | 6 | 30% | 1,8 |
| Marketing e conteúdo | 5 | 30% | 1,5 |
| Gestão de equipe | 3 | 0% | 0 |
| Administrativo | 4 | 15% | 0,6 |

Resultado: 14,4 h por semana brutas · menos 3 h de revisão = 11,4 h × 4,33 = **49,4 h por mês líquidas** · 49,4 × R$ 120 × 60% = **R$ 3.557 por mês** · menos R$ 600 = **R$ 2.957 de líquido mensal** · ROI em 12 meses = (12 × 3.557 − (12 × 600 + 6.300)) ÷ 13.500 = **216%** · payback = 6.300 ÷ 2.957 = **2,1 meses**.

## Rodar duas vezes quando a hora é de colaborador

A calculadora usa um valor de hora só. Se a maior parte das horas devolvidas é de secretária, estagiário ou assistente, rode de novo com o custo-hora dessa pessoa (método 3): `python3 scripts/calcular_roi.py ENTRADA.json --valor-hora 40`. Para não baratear a implantação feita pelo advogado, preencha `valor_hora_implantacao` com a hora de quem implantou. "A conta mais honesta costuma ficar entre as duas."

## Faixa mínima e máxima

Quando a redução veio do passo 6 (estimar a partir do POP), passe cada setor como `{"min": x, "max": y}`. O script entrega o cenário mínimo e o máximo lado a lado. Apresente os dois, sem escolher o máximo para "vender" a automação a sócio ou equipe. Exemplo em `scripts/exemplos/roi-exemplo-faixa.json`.
