# Plano de ação 5W2H do setor-alvo (passo 7)

Leia no passo 7 do `mapear-setores`. O ranking diz onde. O 5W2H diz o que vai acontecer, quem cuida e até quando. São sete perguntas, e o plano só está pronto quando as sete têm resposta.

## Os campos

| Campo | A pergunta | Como preencher bem |
|---|---|---|
| What · O quê | Qual é a ação? | Uma frase com verbo, específica o bastante para saber o dia em que terminou. "Melhorar o atendimento" não serve. |
| Why · Por quê | Que problema ela resolve? | O número de hoje: horas por semana, incômodo, reclamação, atraso. É ele que se compara depois. |
| Where · Onde | Em que canais, sistemas e documentos? | WhatsApp do escritório, software jurídico, planilha, Projeto do escritório no Claude. Tudo o que a ação toca. |
| When · Quando | Começa e termina quando? | Data de início, marcos no meio e data de conclusão, em marcos do próprio escritório (veja abaixo). |
| Who · Quem | Quem responde pela ação? | **Um nome só** como responsável. Quem participa vem ao lado, mas o dono é um. |
| How · Como | Em que passos? | Passos numerados, cada um com a sigla S, A ou H. Depois do `escrever-pop`, o POP do setor vira esse campo. |
| How much · Quanto | Quanto custa e quanto devolve? | Horas da equipe para implantar, custo de ferramenta se houver e a meta de horas por semana depois da mudança. |

**Marcos do When:** POP do setor escrito (`escrever-pop`) · base do setor organizada (`montar-base`) · checklist de prontidão e primeira automação (`desenhar-automacao`) · primeira medição depois de pelo menos 4 semanas de uso (`medir-retorno`). Use datas do calendário do escritório, contadas a partir de hoje ("semana 1", "semana 3").

## Perguntas antes de montar (até cinco, uma por vez)

Pergunte só o que faltar, nesta ordem:
1. Quem pode ser o responsável por este plano? (Uma pessoa só. Na trilha solo, é o titular.)
2. Que ferramentas o setor já usa hoje (software jurídico, CRM, planilha, WhatsApp Business)?
3. Que conta de IA vai rodar este setor: pessoal ou profissional? (Dado de cliente só em conta profissional ou de equipe.)
4. Que prazo é realista para o POP e para a primeira versão rodando, olhando a agenda das próximas semanas?
5. Qual é a meta de horas por semana do setor depois da mudança? (Palpite do escritório, marcado como meta, confirmado depois pela medição.)

Não invente custo, preço de ferramenta nem número. Onde faltar, escreva `[A DEFINIR]`.

## Modelo em branco (grave em `escritorio/02-mapa/plano-5w2h-<setor>.md`)

```
PLANO DE AÇÃO 5W2H · SETOR-ALVO: [SETOR]
Versão: 1 · Data da revisão: [DATA] · Dono: [RESPONSÁVEL]
Revisão quinzenal: [DIA DA SEMANA]

WHAT · O QUÊ (a ação, com verbo)
[...]

WHY · POR QUÊ (o problema e o número de hoje)
Horas por semana hoje: [...]   Incômodo: [1 a 5]
[...]

WHERE · ONDE (canais, sistemas, documentos)
[...]

WHEN · QUANDO
Início: [...]
Marcos: [...]
Conclusão: [...]

WHO · QUEM
Responsável (um só): [...]
Participam: [...]

HOW · COMO (passos com S, A ou H)
1. [...] (S/A/H)
2. [...] (S/A/H)
3. [...] (S/A/H)
Cuidados com dado de cliente: conta profissional, anonimização quando couber, revisão
humana antes de sair do escritório.

HOW MUCH · QUANTO
Horas para implantar: [...]
Custo de ferramenta: [...]
Meta de horas por semana depois: [...]

INDICADORES DA REVISÃO QUINZENAL (três)
1. [...]
2. [...]
3. [...]
```

No fim, sugira os três indicadores para a revisão quinzenal (seção "Acompanhamento" do SKILL.md).

## Exemplo resolvido (números de exemplo, escritório fictício de Previdenciário com 5 pessoas)

**Relacionamento com o cliente** · atualização de andamento e respostas de WhatsApp com rascunho da IA.

- **What:** padronizar a atualização de andamento e as respostas de dúvida no WhatsApp, com a IA rascunhando no tom do código do escritório e a equipe revisando antes de enviar.
- **Why:** exemplo: o setor consome 18 horas por semana e recebeu incômodo 5. Cliente cobra andamento pelo WhatsApp, a resposta depende de quem está livre e cada pessoa escreve de um jeito.
- **Where:** WhatsApp do escritório, software jurídico onde chegam as movimentações e o Projeto do escritório no Claude, com o código do escritório e os modelos de mensagem.
- **When:** semana 1, POP da atualização de andamento escrito (`escrever-pop`) · semana 3, modelos de mensagem por tipo de movimentação na base de conhecimento (`montar-base`) · semana 5, primeira versão rodando no nível 3 e checklist de prontidão (`desenhar-automacao`) · 4 semanas de uso depois, primeira medição (`medir-retorno`).
- **Who:** responsável, a assistente de controladoria. Participam o advogado responsável, que valida as mensagens sobre decisão, e o titular, que aprova o POP e cobra os prazos.
- **How:**
  1. A IA lê as movimentações do dia e separa rotina de relevante. (S)
  2. A IA rascunha a mensagem de cada movimentação relevante no tom do código. (A)
  3. A assistente revisa e envia. Decisão de mérito passa pelo advogado. (A)
  4. Notícia muito ruim: o advogado liga. (H)
  5. A IA monta o resumo mensal de cada cliente com as movimentações de rotina. (S)
  - Dado de saúde em laudo ou perícia sai anonimizado do que vai para a IA, sempre pela conta profissional.
- **How much:** exemplo: umas 6 horas da assistente e 2 do advogado para implantar, mais o custo da ferramenta, que fica `[A DEFINIR]` conforme o plano que o escritório contratar. Meta de exemplo: o setor sair de 18 para 10 horas por semana em 60 dias.
- **Onde a IA entra:** nos passos 1, 2 e 5, e como apoio no 3. Nada disso funciona sem o código do escritório e os modelos de mensagem: por isso o plano depende do `escrever-pop` e da `montar-base`.

## Trilha solo

O responsável é sempre o titular, e revisão e aprovação recaem na mesma pessoa. Compense no campo How: conferência em outro momento do dia (não logo depois de fazer), checklist curto de revisão e a IA como segundo olhar, sem transformar o passo em S por isso. Em "Participam", liste a pessoa de apoio, se houver.
