# Piloto de duas semanas · POP-[SIGLA]-[NN] [NOME DO PROCESSO]

Versão no começo do piloto: [0.3] · Versão na semana 2: [0.4] · Dono do POP (conduz e consolida): [NOME]
Começo: [AAAA-MM-DD, "semana 1"] · Fim: [AAAA-MM-DD, fim da semana 2] · Situação: [EM PREPARO / SEMANA 1 / SEMANA 2 / FECHADO]

## 1. Combinados antes de começar

- Quem executa: [UMA OU DUAS PESSOAS, POR FUNÇÃO]
- Quem revisa os passos A: [TITULAR OU FUNÇÃO]
- Quem decide no fim: [TITULAR]
- Solo: quem vem de fora para a conversa de fechamento: [COLEGA DE CONFIANÇA, ESTAGIÁRIO, SECRETÁRIA OU "NINGUÉM"]
- Ambiente: [PROJETO NO CLAUDE "NOME", CONTA PROFISSIONAL] · A IA entra pela mão das pessoas, seguindo o campo "Onde a IA entra" do POP. Nenhuma automação roda no piloto.
- Acordo de uso de IA assinado por quem participa (no solo, o autocompromisso): [SIM / FALTA: QUEM]
- Escopo: um POP, um setor, só os casos que entrarem no período.
- O que fica fora do piloto e continua no fluxo antigo: [EXEMPLO: PRAZO FATAL NO MESMO DIA]
- Linha de base: [ARQUIVO `06-medicao/linha-de-base-<setor>.md`, MINUTOS POR EXECUÇÃO, TIPO DE CASO NO PERÍODO / "FALTA: medir antes de começar"]
- Regra de mudança: ajustes entram no fim de cada semana, com versão nova. Erro crítico corrige na hora.

## 2. Conversa de abertura (dia 0, 30 minutos)

- [ ] Apresentar o POP na versão do piloto.
- [ ] Mostrar o registro e combinar que cada linha é preenchida na hora, em até dois minutos.
- [ ] Combinar o que fica fora do piloto.
- [ ] Dizer com todas as letras: o piloto mede o POP, ninguém está sendo avaliado.
- [ ] Combinar quem avisa erro e como. Quem avisa nunca é punido por avisar.

## 3. Registro por execução

Uma linha por execução, preenchida por quem executou. Quem revisou completa a revisão e os erros, com o tipo (fato, data ou prazo, valor, tom, invenção, dado sensível). Sem nome de cliente: o caso vai pelo código. As colunas são separadas por tabulação: cole numa planilha e cada coluna cai no lugar. As duas linhas de exemplo começam com "#" e ficam fora da conta; apague quando entrar a primeira execução real.

```
Dia	Semana	Caso (código)	Tipo de caso	Executor	Min. execução	Min. revisão	Voltou para retrabalho?	Min. retrabalho	Erros pegos na revisão (tipo)	Erro chegou ao cliente ou tribunal?	Desvio do POP? Por quê	Observação
# dia 1	1	CASO-07	Comum	Assistente	35	12	Não	0	1 (data)	Não	Não	Linha de exemplo, apague
# dia 1	1	CASO-08	Difícil	Assistente	50	25	Sim	20	2 (fato, tom)	Não	Sim: pediu ajuda à advogada no passo 4	Linha de exemplo, apague
```

## 4. Durante o piloto

**Ajustar no fim da semana, sem parar o piloto, quando:**
- a mesma pergunta ou o mesmo erro apareceu duas vezes;
- alguém criou um atalho por fora do POP;
- a revisão pega sempre o mesmo tipo de erro no mesmo passo;
- a instrução do passo precisou de explicação extra para dar certo;
- um caso trouxe uma exceção que o POP não previa.

**Voltar atrás na hora quando:**
- um erro chegou ao cliente ou ao tribunal;
- houve erro de prazo, mesmo que a revisão tenha pegado;
- dado de cliente saiu da conta profissional ou sem a anonimização prevista;
- a IA inventou norma ou jurisprudência e passou da primeira conferência;
- a revisão virou carimbo, com aprovação em segundos e zero correção.

Quem recua é o passo, o POP continua. O passo sobe de sigla na hora (S para A, A para H) e só desce de novo depois de um novo teste com os três casos. Incidente e quase incidente vão para `escritorio/06-medicao/incidentes.md`.

| Data | Passo | Sigla antes | Sigla agora | Motivo |
|---|---|---|---|---|
| | | | | |

**Erro plantado (semana 2):** [QUEM PLANTOU, EM QUE PASSO, QUAL DEFEITO] · A revisão pegou? [SIM / NÃO] · O que mudou no POP: [...]

## 5. Conversa do fim da semana 1 (20 minutos)

- O que travou: [...]
- O que se repetiu: [...]
- O que alguém fez diferente do POP, e por quê: [...]
- Ajustes para a semana 2, marcados [ALTERADO] ou [NOVO]: [...] · Versão nova: [0.4]

## 6. Fechamento

Análise do registro (o script `scripts/analisar_piloto.py` ou a conta à mão, mostrada):

| Indicador | Semana 1 | Semana 2 |
|---|---|---|
| Execuções | | |
| Tempo total por execução (execução + revisão + retrabalho, min) | | |
| Retrabalho (%) | | |
| Execuções com correção na revisão | | |
| Erros pegos por tipo | | |
| Erros que chegaram ao cliente ou ao tribunal | | |
| Desvios do POP | | |
| Peso da revisão (revisão ÷ execução + revisão) | | |

Antes e depois (só a semana 2 entra na comparação; a semana 1 carrega a curva de aprendizado):

| Indicador | Antes | Piloto, semana 2 |
|---|---|---|
| Tempo por execução (min) | | |
| Retrabalho (%) | [OU "não medido"] | |
| Erros pegos na revisão | não medido | |
| Erros que passaram | não medido | |

- Por execução: [MIN] a menos ([%] menos tempo) · Por mês, com [N] execuções: [H] horas.
- Os tipos de caso dos dois períodos se parecem? [SIM / NÃO: COMO ISSO AFETA A COMPARAÇÃO]
- Sinal de carimbo: [NENHUM / ONDE]
- Leitura: [GANHO CONSISTENTE / TROCA RUIM / SEM GANHO / NÃO PRONTO]
- Para onde vão as horas: [DESTINO, conferido com a `medir-retorno`]

Decisão do titular, passo a passo:

| Passo | Sigla | Recomendação (manter, ajustar instrução, completar base, subir sigla) | Número que sustenta | Decisão do titular |
|---|---|---|---|---|
| | | | | |

Os passos S e A estão prontos para seguir à automação? [SIM / SIM COM RESSALVAS / NÃO] (se algum erro chegou ao cliente ou ao tribunal, é não até a causa estar corrigida e testada)

Pendências para a base (`montar-base`): [LISTA]
