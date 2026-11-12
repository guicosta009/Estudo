# Biblioteca de POPs: índice

São 19 POPs de referência: 10 por setor, escritos para um escritório genérico com equipe, e 9 por área, escritos para um escritório genérico de 3 a 10 pessoas. Todos estão no formato de 12 campos do glossário, com cada passo no formato `[S/A/H] Verbo + tarefa. Executa: ... Confere: ...` e fluxograma em Mermaid e em texto. Nenhum deles vale como está: são o ponto de partida da entrada B do `escrever-pop` (adaptar um POP da biblioteca).

Em escritório de duas pessoas, ou solo com estagiária, os responsáveis mudam e os passos continuam quase os mesmos. "Uma pessoa acumula várias funções, e tudo bem, mas o passo continua existindo."

## POPs por setor

| Arquivo | POP | Setor | Área | Passos | S | A | H |
|---|---|---|---|---|---|---|---|
| `setor-01-atendimento-triagem.md` | Triagem do primeiro contato e consulta inicial | Atendimento e triagem | todas | 12 | 5 | 5 | 2 |
| `setor-02-comercial.md` | Proposta de honorários e contrato | Comercial | todas | 12 | 5 | 4 | 3 |
| `setor-03-producao-pecas.md` | Elaboração de petição a partir de modelo e documentos | Produção de peças | todas | 12 | 3 | 6 | 3 |
| `setor-04-prazos-controladoria.md` | Tratamento diário de publicações e intimações | Prazos e controladoria | todas | 10 | 5 | 3 | 2 |
| `setor-05-audiencias-diligencias.md` | Preparação de audiência | Audiências e diligências | todas | 11 | 3 | 5 | 3 |
| `setor-06-financeiro-cobranca.md` | Cobrança de honorários e inadimplência | Financeiro e cobrança | todas | 11 | 6 | 3 | 2 |
| `setor-07-relacionamento-cliente.md` | Atualização de andamento processual | Relacionamento com o cliente | todas | 11 | 5 | 4 | 2 |
| `setor-08-marketing-conteudo.md` | Produção de conteúdo com revisão ética | Marketing e conteúdo | todas | 10 | 4 | 5 | 1 |
| `setor-09-gestao-equipe.md` | Integração de novo colaborador | Gestão de equipe | todas | 10 | 2 | 5 | 3 |
| `setor-10-administrativo.md` | Recebimento e organização de documentos | Administrativo | todas | 11 | 6 | 3 | 2 |
| **Total por setor** | | | | **110** | **44** | **43** | **23** |

## POPs por área

| Arquivo | POP | Setor | Área | Passos | S | A | H |
|---|---|---|---|---|---|---|---|
| `area-previdenciario-viabilidade.md` | Análise de viabilidade de benefício | Atendimento e triagem | Previdenciário | 11 | 4 | 5 | 2 |
| `area-previdenciario-requerimento.md` | Requerimento administrativo e exigência | Prazos e controladoria | Previdenciário | 12 | 2 | 6 | 4 |
| `area-trabalhista-triagem-provas.md` | Triagem e organização de provas do reclamante | Atendimento e triagem | Trabalhista | 10 | 4 | 4 | 2 |
| `area-trabalhista-reclamatoria.md` | Reclamatória com cálculo preliminar | Produção de peças | Trabalhista | 11 | 3 | 5 | 3 |
| `area-trabalhista-defesa-empresa.md` | Defesa da empresa em reclamatória | Produção de peças | Trabalhista | 10 | 2 | 5 | 3 |
| `area-familia-divorcio.md` | Divórcio consensual, com e sem filhos | Produção de peças | Família | 12 | 3 | 4 | 5 |
| `area-familia-alimentos.md` | Ação de alimentos | Produção de peças | Família | 12 | 3 | 4 | 5 |
| `area-consumidor-indenizatoria.md` | Ação indenizatória de consumo | Produção de peças | Consumidor | 10 | 3 | 5 | 2 |
| `area-civel-massa.md` | Demandas de massa com petição padrão | Produção de peças | Cível | 11 | 4 | 4 | 3 |
| **Total por área** | | | | **99** | **28** | **42** | **29** |

O que a tabela mostra: todo POP tem pelo menos um H, e em nenhum setor a IA vai do começo ao fim. O que ela esconde: a proporção muda conforme a base de conhecimento, a conta de IA e a confiança que o indicador dá com o tempo. Um S da biblioteca pode ser A no escritório hoje (trava por estágio do `classificar-sah`).

## Onde a IA mais ajuda e onde precisa ser humano (por área)

| POP | Onde a IA mais ajuda | Onde precisa ser humano |
|---|---|---|
| Previdenciário: viabilidade | Extrair o CNIS, cruzar com CTPS e PPP, simular | Decidir a viabilidade, dar o "não dá agora" |
| Previdenciário: requerimento | Dossiê, carta de exigência, status | Protocolo com credencial, conferência do prazo, decisão no indeferimento |
| Trabalhista: triagem e provas | Áudio em linha do tempo, holerites, matriz | Escolher os pedidos, explicar o risco |
| Trabalhista: reclamatória | Memória de cálculo, rascunho, consistência | Teses, revisão integral, precedentes, protocolo |
| Trabalhista: defesa da empresa | Resumo da inicial, cruzamento com o RH | Risco, faixa de acordo, treino do preposto |
| Família: divórcio | Planilha de bens, plano de convivência, minuta | Primeiro atendimento, guarda e convivência, via, leitura |
| Família: alimentos | Planilha de gastos, controle de pagamento | Valor pedido, limite de acordo, sinal de violência |
| Consumidor: indenizatória | Linha do tempo dos prints, checklist de provas | Viabilidade, rito, valor da causa |
| Cível: massa | Ficha, enquadramento, preenchimento, controle do lote | Aprovar a tese, revisar cada petição |

O Previdenciário tem muito documento, então a IA assume mais. Família tem muita conversa delicada, então o H aparece mais e em passos inegociáveis. Trabalhista e Consumidor ficam no meio, com muito A na produção e H em tese e risco. "A IA ganha espaço onde o trabalho é ler e organizar. Ela para onde começa a escolha e a conversa."

## Ordem de leitura sugerida

1. O POP do setor-alvo (o maior "horas × incômodo" do diagnóstico ou a maior pontuação do mapeamento).
2. O POP do setor vizinho (quem entrega para o setor-alvo ou recebe dele).
3. Se o escritório tem área dominante: o POP da área no mesmo setor. Junte com o genérico do setor, corte o que sobra e adapte pela entrada B, com as perguntas de `../perguntas-por-area.md`.

Quase todo POP tem um passo de "enviar checklist" e outro de "avisar o cliente". Eles moram em Atendimento e em Relacionamento e muitas vezes são a primeira automação que dá certo.

## O que foi normalizado em relação ao material de origem

- **Campo 11 (Dados pessoais e sensíveis)** acrescentado aos POPs por setor, a partir dos cuidados que cada POP já trazia e das regras transversais do plugin. Nos POPs por área, o campo já existia.
- **Campo 12 (Indicador)** gerado para os 9 POPs por área, marcado como "sugestão da biblioteca". Nos POPs por setor, o indicador é o do material.
- **Executa e Confere** escritos em todos os passos. Onde o material deixava a conferência implícita, ela foi tirada dos responsáveis do próprio POP; frequência de amostra que o material não dava ficou `[A DEFINIR]`.
- **Siglas e passos preservados.** A regra de leitura é a do glossário: a sigla diz quem produz o primeiro resultado do passo; a conferência fica no "Confere".
- **Prazos** marcados como exemplo em todos os POPs.
- **Fluxogramas:** os POPs de Atendimento, Prazos, Financeiro, Relacionamento, Marketing, Previdenciário (viabilidade), Família (divórcio) e Cível (massa) partem do fluxograma do material. Os demais foram desenhados a partir dos passos e dizem isso no arquivo.
- **Tabela "Antes e com a IA"** nos 10 POPs por setor, como no material. Os POPs por área não tinham.
- **Exceções novas**, quando aparecem para responder a um "e se não?" que o material deixava aberto, vêm com `[A DEFINIR]` ou são marcadas como sugestão.
