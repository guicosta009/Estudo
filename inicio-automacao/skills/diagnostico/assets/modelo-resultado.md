# Diagnóstico de prontidão para automação

- Escritório: [NOME]
- Rodada: [AAAA-MM-DD] · questionário versão [VERSÃO DO questionario.json]
- Respondido por: [PAPEL DE QUEM RESPONDEU]
- Dono deste documento: [A DEFINIR]
- Porte: [FAIXA] · trilha [solo | equipe] · apoio: [SÓ NA TRILHA SOLO]
- Áreas: [LISTA]
- Processos ativos: [FAIXA]
- Conta de IA: [TIPO]

> A nota é uma foto de hoje, feita por quem respondeu. Ela não julga o trabalho do escritório. O valor está na comparação entre uma rodada e a próxima. O cálculo foi feito no computador, sem envio para fora.

## Resultado

**Nota [0 a 100] de 100 · nível [Zero | Base | Estrutura | Automação] ([FAIXA])**

[FRASE DO NÍVEL] [TEXTO DO NÍVEL]

## As 9 dimensões

| Dimensão | Pontos | Peso | % |
|---|---|---|---|
| Cultura e liderança | [x,x] | 14 | [x]% |
| Processos e POPs | [x,x] | 17 | [x]% |
| Base de conhecimento | [x,x] | 13 | [x]% |
| Uso de IA | [x,x] | 13 | [x]% |
| Governança e proteção de dados | [x,x] | 11 | [x]% |
| Comercial e marketing | [x,x] | 11 | [x]% |
| Equipe | [x,x] | 7 | [x]% |
| Investimento | [x,x] | 5 | [x]% |
| Medição | [x,x] | 9 | [x]% |
| **Total** | **[NOTA]** | 100 | |

A nota é a soma exata dos pontos ([SOMA COM DUAS CASAS]), arredondada. Por isso a soma da coluna, já arredondada, pode diferir por pouco.

## Prioridades para o nível [NÍVEL]

1. **[TÍTULO 1]** [DETALHE 1] (skill `[SKILL]`)
2. **[TÍTULO 2]** [DETALHE 2] (skill `[SKILL]`)
3. **[TÍTULO 3]** [DETALHE 3] (skill `[SKILL]`)

## Também merece atenção

(Só as dimensões abaixo de 60% que o nível não cobre, da menor para a maior, no máximo 3. Se nenhuma, apague a seção.)

- **[DIMENSÃO] ([x]%).** [RECOMENDAÇÃO DA DIMENSÃO] (skill `[SKILL]`)

## Cuidados com dados e revisão

(Só se algum alerta do questionario.json disparou. Se nenhum, apague a seção.)

- [ALERTA]

## Setor-alvo provisório

**[SETOR]**: [H] h por semana, incômodo [1 a 5] de 5 (pontuação [H × INCÔMODO]).

| # | Setor | Horas por semana | Incômodo | Horas × incômodo |
|---|---|---|---|---|
| 1 | [SETOR] | [H] | [I] | [P] |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Total mapeado: [SOMA DAS HORAS DOS 10 SETORES] h por semana. Próximo da fila: [2º DO RANKING].

O setor-alvo é provisório: ele vem de faixas de horas estimadas. A confirmação vem no `mapear-setores`, com as horas registradas e o potencial de IA de cada setor.

Maior gargalo, nas palavras de quem respondeu: "[ATÉ 280 CARACTERES, SEM DADO DE CLIENTE]"

## Modelo de negócio

(Só se o teste foi feito. Se não, apague a seção.)

**[MODELO PRINCIPAL]** ([PONTOS DE CADA MODELO COM PONTO]).
[SE HOUVER SEGUNDO ATÉ 2 PONTOS ATRÁS] Também tem traços de **[MODELO]**: leia os dois perfis e a parte de híbridos em `references/modelos-de-negocio.md`. Combinação conhecida: [POR ONDE COMEÇAR].

- Setor-alvo provável do perfil: [SETOR] (alternativo: [SETOR E CONDIÇÃO]).
- Mistura de S, A e H: [DO PERFIL]
- Tipo de base de conhecimento: [DO PERFIL]
- Risco que mais pesa: [DO PERFIL]
- Primeiro passo típico: [DO PERFIL]

[MESMO SETOR: "O perfil e o diagnóstico apontam o mesmo setor: X." · SETOR DIFERENTE: "O modelo orienta, o mapa decide. O perfil sugere X, mas o diagnóstico, feito com as horas do seu escritório, aponta Y. Siga o diagnóstico e anote por que o perfil apontou outro."]

## Evolução desde a rodada de [DATA ANTERIOR]

(Só a partir da segunda rodada. Se for a primeira, apague a seção.)

Nota: [ANTES] para [AGORA] ([+/-DIFERENÇA]). Nível: [ANTES] para [AGORA]. Setor-alvo: [ANTES] para [AGORA]. Horas mapeadas: [ANTES] para [AGORA].

| Dimensão | Antes | Agora | Diferença |
|---|---|---|---|
| Cultura e liderança | | | |
| Processos e POPs | | | |
| Base de conhecimento | | | |
| Uso de IA | | | |
| Governança e proteção de dados | | | |
| Comercial e marketing | | | |
| Equipe | | | |
| Investimento | | | |
| Medição | | | |

- [OBSERVAÇÕES: TRILHA MUDOU, VERSÃO DO QUESTIONÁRIO MUDOU, SETOR-ALVO MUDOU]

## Próximo passo

- **[ETAPA]**, com a skill `[SKILL]`. [O QUE MUDA NA TRILHA DO ESCRITÓRIO]
- Enquanto isso, escreva o passo a passo atual do setor-alvo, do jeito que acontece hoje, sem melhorar nada. Ele é a matéria-prima do escrever-pop.

## Respostas

**[DIMENSÃO]**

- [ID] [PERGUNTA] → [OPÇÃO ESCOLHIDA] ([PONTOS DA PERGUNTA, 0 A 1])

## Dados para a próxima rodada

Não edite este bloco: a próxima rodada do diagnóstico lê daqui para comparar.

```json
{
  "versao_questionario": "[VERSÃO]",
  "data": "[AAAA-MM-DD]",
  "trilha": "[solo | equipe]",
  "porte": "[solo | 2-5 | 6-20 | 20+]",
  "nota": 0,
  "nivel": "[NÍVEL]",
  "dimensoes": {"cultura": {"pontos": 0, "pct": 0}, "processos": {"pontos": 0, "pct": 0}, "base": {"pontos": 0, "pct": 0}, "ia": {"pontos": 0, "pct": 0}, "governanca": {"pontos": 0, "pct": 0}, "comercial": {"pontos": 0, "pct": 0}, "equipe": {"pontos": 0, "pct": 0}, "investimento": {"pontos": 0, "pct": 0}, "medicao": {"pontos": 0, "pct": 0}},
  "setor_alvo": "[SETOR]",
  "horas_total": 0,
  "ranking": ["[SETOR 1]", "[SETOR 2]", "[SETOR 3]", "[SETOR 4]", "[SETOR 5]"],
  "modelo": "[ID DO MODELO OU null]",
  "entrada": {
    "perfil": {},
    "respostas": {},
    "setores": {},
    "gargalo": "",
    "modelo": null
  }
}
```
