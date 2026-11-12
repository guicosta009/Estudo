# Diagnóstico de prontidão para automação

- Escritório: Escritório exemplo (solo)
- Rodada: 2026-10-16 · questionário versão 1.0
- Respondido por: Titular ou sócio(a)
- Dono deste documento: [A DEFINIR]
- Porte: Só eu, com ou sem estagiário ou secretária · trilha solo · apoio: Estagiário(a)
- Áreas: Previdenciário
- Processos ativos: 51 a 200
- Conta de IA: Pessoal paga

> A nota é uma foto de hoje, feita por quem respondeu. Ela não julga o trabalho do escritório. O valor está na comparação entre uma rodada e a próxima. O cálculo foi feito no computador, sem envio para fora.

## Resultado

**Nota 37 de 100 · nível Base (26 a 50)**

Existe organização, mas ela não está escrita. O escritório funciona, só que funciona porque as pessoas sabem o caminho. Falta tirar isso da cabeça e colocar no papel, que é onde a IA consegue ler.

## As 9 dimensões

| Dimensão | Pontos | Peso | % |
|---|---|---|---|
| Cultura e liderança | 5,1 | 14 | 37% |
| Processos e POPs | 5,3 | 17 | 31% |
| Base de conhecimento | 4,7 | 13 | 36% |
| Uso de IA | 9,3 | 13 | 71% |
| Governança e proteção de dados | 3,2 | 11 | 29% |
| Comercial e marketing | 2,8 | 11 | 25% |
| Equipe | 2,9 | 7 | 42% |
| Investimento | 2,3 | 5 | 45% |
| Medição | 2 | 9 | 22% |
| **Total** | **37** | 100 | |

A nota é a soma exata dos pontos (37,46), arredondada. Por isso a soma da coluna, já arredondada, pode diferir por pouco.

## Prioridades para o nível Base

1. **Transforme o jeito que já funciona em POP, começando pelo setor-alvo.** O trabalho é registrar o que já existe, sem inventar processo novo. (skill `escrever-pop`)
2. **Organize a base de conhecimento por área e leve para um Projeto no Claude.** Modelos, teses e checklists num lugar só. (skill `montar-base`)
3. **Comece a medir as horas de dois ou três setores.** Uma semana de anotação já mostra onde está o gargalo. (skill `mapear-setores`)

## Também merece atenção

- **Comercial e marketing (25%).** Escreva o roteiro de triagem do primeiro contato e um modelo de proposta por tipo de caso. São as duas peças que a IA precisa para responder lead e montar proposta no mesmo dia. (skill `escrever-pop`)
- **Governança e proteção de dados (29%).** Escreva numa página o que pode e o que não pode ir para a IA, migre para contas profissionais e defina quem revisa antes de sair do escritório. (skill `regra-de-uso-de-ia`)
- **Cultura e liderança (37%).** Escreva o código do escritório: como atendemos, como decidimos, o que nunca fazemos. Ele vira o primeiro arquivo da sua base e a régua para tudo que a IA produzir. (skill `codigo-do-escritorio`)

## Setor-alvo provisório

**Relacionamento com o cliente**: 12 h por semana, incômodo 5 de 5 (pontuação 60).

| # | Setor | Horas por semana | Incômodo | Horas × incômodo |
|---|---|---|---|---|
| 1 | Relacionamento com o cliente | 12 | 5 | 60 |
| 2 | Produção de peças | 12 | 4 | 48 |
| 3 | Atendimento e triagem | 6 | 3 | 18 |
| 4 | Prazos e controladoria | 6 | 3 | 18 |
| 5 | Administrativo | 6 | 2 | 12 |

Total mapeado: 50 h por semana. Próximo da fila: Produção de peças.

O setor-alvo é provisório: ele vem de faixas de horas estimadas. A confirmação vem no `mapear-setores`, com as horas registradas e o potencial de IA de cada setor.

Maior gargalo, nas palavras de quem respondeu: "Perco a manhã inteira respondendo cliente no WhatsApp."

## Modelo de negócio

**Advogado solo ou autônomo** (Advogado solo ou autônomo 9, Full service 2, Boutique 1).

- Setor-alvo provável do perfil: Relacionamento com o cliente (alternativo: Atendimento e triagem, se entra pouca gente).
- Mistura de S, A e H: Muito A, com peso do H alto: aceitar caso, definir preço e dar notícia ruim continuam com você.
- Tipo de base de conhecimento: Perguntas frequentes com respostas-modelo e o código do escritório.
- Risco que mais pesa: Depender de uma pessoa, e a tentação da conta pessoal.
- Primeiro passo típico: Tire o WhatsApp do improviso: respostas-modelo, atualização de andamento e hora marcada para responder.

O perfil e o diagnóstico apontam o mesmo setor: Relacionamento com o cliente.

## Próximo passo

- **Código do escritório**, com a skill `codigo-do-escritorio`. O código é escrito para você e para a IA, e já prepara a primeira contratação: quem chegar aprende pelo papel.
- Enquanto isso, escreva o passo a passo atual do setor-alvo, do jeito que acontece hoje, sem melhorar nada. Ele é a matéria-prima do escrever-pop.

## Respostas

**Cultura e liderança**

- c1 Quem decide as mudanças no escritório? → Trabalho sozinho(a) (0,5)
- c2 Quando você delega uma tarefa, o que costuma acontecer? → Delego, mas refaço boa parte (0,25)
- c3 Quando surge uma ferramenta ou um jeito novo de trabalhar, a equipe: → Trabalho sozinho(a) (0,5)
- c4 Com que frequência vocês param para olhar como o escritório está funcionando? → Quando dá problema (0,3)
- c5 Do seu tempo de trabalho, quanto vai para o operacional (peça, prazo, atendimento) e quanto para pensar o escritório? → Uns 80% operacional (0,35)
- c6 O jeito de ser do escritório (como atende, o que valoriza, o que nunca faz) está escrito? → Está na minha cabeça (0,3)

**Processos e POPs**

- p1 Se você ou seu principal colaborador ficar 15 dias fora, o escritório continua? → Alguém se vira, mas com muita perda (0,3)
- p2 Quantos setores do escritório têm o passo a passo escrito (POP, checklist ou fluxograma)? → Um (0,35)
- p3 Do primeiro contato do cliente até o protocolo, como o caso anda? → Existe um jeito, mas está na cabeça de quem faz (0,3)
- p4 Onde vocês controlam prazos e tarefas? → Planilha, e-mail ou WhatsApp (0,3)
- p5 Os modelos de petição e documentos são padronizados? → Existe uma pasta, mas desatualizada (0,3)

**Base de conhecimento**

- b1 Onde ficam as teses, jurisprudências e argumentos que já deram certo? → Espalhados em processos antigos (0,3)
- b2 Chegou um caso parecido com um antigo. Quanto tempo leva para achar o material? → De 30 minutos a 1 hora (0,35)
- b3 O que já está documentado hoje? → Modelos de petição; Modelos de contrato e procuração; Checklist de documentos por tipo de caso (0,5)
- b4 Você já usa documentos do escritório dentro de uma IA (Projetos no Claude, NotebookLM, GPTs)? → Testei uma vez (0,3)

**Uso de IA**

- i1 Com que frequência você usa IA no trabalho? → Todos os dias (1)
- i2 Quais ferramentas você usa? → Claude; ChatGPT; NotebookLM (1)
- i3 Para que você usa IA hoje? → Pesquisa de jurisprudência; Redação de peças; Análise de documentos e provas; Resumo de processos (0,6667)
- i4 Qual frase descreve melhor o seu uso hoje? → Tenho prompts que reaproveito (0,4)
- i5 E a equipe, usa IA? → Trabalho sozinho(a) (0,5)

**Governança e proteção de dados**

- g1 Existe uma regra escrita sobre o que pode e o que não pode ir para a IA? → Não (0)
- g2 As contas de IA usadas no escritório são: → Pessoais pagas (0,4)
- g3 Antes de colocar um documento de cliente na IA, vocês: → Às vezes tiram nomes e dados (0,35)
- g4 Como está a adequação do escritório à LGPD? → Sei que preciso, mas não comecei (0,2)
- g5 O cliente sabe que a IA participa do trabalho? → Nunca pensei nisso (0,1)
- g6 Quem confere o que a IA produz antes de sair do escritório? → Sempre alguém confere (0,7)

**Comercial e marketing**

- cm0 De onde vêm os clientes hoje? → Indicação de clientes; Instagram (não pontua)
- cm1 Quando um possível cliente chama, o que acontece? → Alguém responde, mas sem roteiro nem prazo (0,3)
- cm2 Como sai a proposta de honorários? → Tenho um modelo, mas monto na mão e demora (0,35)
- cm3 E quem consultou e não fechou? → Às vezes alguém lembra de chamar (0,3)
- cm4 Onde ficam os contatos de leads e clientes? → Na agenda do celular e no WhatsApp (0)
- cm5 Como é a produção de conteúdo do escritório? → Posto quando sobra tempo (0,3)

**Equipe**

- e1 Quem chega novo no escritório aprende como? → Trabalho sozinho(a) (0,5)
- e2 Alguém recebeu treinamento em IA? → Só eu (0,4)
- e3 Existe alguém responsável por tecnologia e inovação? → Eu, no tempo que sobra (0,35)

**Investimento**

- v1 Quanto o escritório gasta por mês com assinaturas de IA? → De R$ 101 a R$ 300 (0,65)
- v2 E com software jurídico e de gestão, somando tudo? → Até R$ 300 (0,35)
- v3 Como você enxerga esse gasto? → Necessário, mas não sei se volta (0,35)

**Medição**

- m1 Você sabe quantas horas por semana cada setor consome? → Tenho uma noção (0,3)
- m2 Quais números você acompanha? → Nenhum (0)
- m3 Você já calculou quanto vale uma hora sua? → Mais ou menos (0,35)

## Dados para a próxima rodada

Não edite este bloco: a próxima rodada do diagnóstico lê daqui para comparar.

```json
{
  "versao_questionario": "1.0",
  "data": "2026-10-16",
  "trilha": "solo",
  "porte": "solo",
  "nota": 37,
  "nivel": "Base",
  "dimensoes": {"cultura": {"pontos": 5.1333, "pct": 0.3667}, "processos": {"pontos": 5.27, "pct": 0.31}, "base": {"pontos": 4.7125, "pct": 0.3625}, "ia": {"pontos": 9.2733, "pct": 0.7133}, "governanca": {"pontos": 3.2083, "pct": 0.2917}, "comercial": {"pontos": 2.75, "pct": 0.25}, "equipe": {"pontos": 2.9167, "pct": 0.4167}, "investimento": {"pontos": 2.25, "pct": 0.45}, "medicao": {"pontos": 1.95, "pct": 0.2167}},
  "setor_alvo": "Relacionamento com o cliente",
  "horas_total": 50,
  "ranking": ["Relacionamento com o cliente", "Produção de peças", "Atendimento e triagem", "Prazos e controladoria", "Administrativo"],
  "modelo": "solo",
  "entrada": {
    "perfil": {"escritorio": "Escritório exemplo (solo)", "porte": "solo", "apoio": "Estagiário(a)", "papel": 0, "areas": ["Previdenciário"], "volume": "51 a 200", "conta_de_ia": "pessoal-paga"},
    "respostas": {"c1": 4, "c2": 1, "c3": 4, "c4": 1, "c5": 1, "c6": 1, "p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "b1": 1, "b2": 1, "b3": [0, 1, 5], "b4": 1, "i1": 3, "i2": [0, 1, 3], "i3": [0, 1, 2, 3], "i4": 1, "i5": 4, "g1": 0, "g2": 1, "g3": 1, "g4": 1, "g5": 1, "g6": 2, "cm0": [0, 2], "cm1": 1, "cm2": 1, "cm3": 1, "cm4": 0, "cm5": 1, "e1": 4, "e2": 1, "e3": 1, "v1": 2, "v2": 1, "v3": 1, "m1": 1, "m2": [9], "m3": 1},
    "setores": {"atendimento": {"horas": "4 a 8 h", "incomodo": 3}, "comercial": {"horas": "1 a 3 h", "incomodo": 2}, "producao": {"horas": "9 a 15 h", "incomodo": 4}, "prazos": {"horas": "4 a 8 h", "incomodo": 3}, "audiencias": {"horas": "1 a 3 h", "incomodo": 2}, "financeiro": {"horas": "1 a 3 h", "incomodo": 4}, "relacionamento": {"horas": "9 a 15 h", "incomodo": 5}, "marketing": {"horas": "1 a 3 h", "incomodo": 3}, "equipe": {"horas": "Não temos", "incomodo": null}, "administrativo": {"horas": "4 a 8 h", "incomodo": 2}},
    "gargalo": "Perco a manhã inteira respondendo cliente no WhatsApp.",
    "modelo": {"q1": 0, "q2": 1, "q3": 0, "q4": 4, "q5": 0, "q6": 0}
  }
}
```
