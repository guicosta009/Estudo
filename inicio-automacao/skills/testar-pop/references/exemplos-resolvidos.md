# Exemplos resolvidos

Escritórios fictícios. Todos os números são de exemplo e servem só para mostrar o formato. Use para explicar ao advogado o que cada etapa costuma revelar.

## 1. Teste de mesa: petição inicial previdenciária

Escritório de Previdenciário com 3 pessoas (exemplo), setor-alvo Produção de peças, POP-PEC-01 Petição inicial de aposentadoria por idade, versão 0.1 (Rascunho).

A advogada escreveu o POP e entregou para a assistente executar no papel com um caso já protocolado, anonimizado. Em 40 minutos, a assistente fez cinco perguntas:
- duas sobre a lista de documentos ("o que conta como comprovante de residência atualizado?");
- uma sobre quem decide se o requerimento administrativo do caso é suficiente;
- uma sobre qual modelo usar;
- uma sobre o que fazer quando o CNIS tem vínculo sem data de saída.

As cinco contam: são sobre como fazer, quem decide e qual modelo usar. Resultado: AJUSTAR E REPETIR.

O que mudou na versão 0.2:
- a lista de documentos virou entrada do POP e pendência para a `montar-base`;
- a análise do requerimento virou passo H da advogada;
- o modelo ganhou nome e lugar fixo;
- o vínculo sem data de saída virou exceção escrita, com o que fazer e quem decide.

Nenhuma dessas lacunas apareceria numa releitura da própria autora. Como a versão 0.2 mudou o fluxo (entrou um passo H), a skill sugere repetir o teste de mesa com outro caso antes do teste com a IA.

## 2. Teste com a IA: o mesmo POP, passo 3

POP-PEC-01, versão 0.2. Passo 3: `[A] Redigir a minuta a partir do modelo da inicial e do resumo anonimizado do caso.` Três casos (exemplo):
- **Fácil:** aposentadoria por idade urbana com CNIS completo e documentação toda na pasta. A minuta segue o modelo e o tom. Ajuste só de forma. Revisão de 15 minutos contra 60 da advogada no caso real.
- **Comum:** benefício por incapacidade com laudos de médicos diferentes. Faltou o pedido subsidiário que o escritório sempre faz. A instrução do passo não dizia que o pedido existe: o pedido entra no modelo (pendência para a base) e o passo é testado de novo.
- **Difícil:** CNIS com vínculo em aberto e um documento faltando. A IA redigiu a minuta inteira sem avisar do documento faltando.

Decisão: o passo continua A para os casos comuns, com uma exceção nova, "caso com documento faltando ou vínculo em aberto: a IA não redige; marca a pendência e devolve para a advogada (H)", e o sinal que identifica o caso ("checklist do passo 1 com item pendente"). Versão 0.3.

## 3. Piloto: a revisão que virou carimbo

Escritório de Família com 5 pessoas (exemplo), POP-REL-01 Resposta de andamento no WhatsApp.

Na semana 1, a revisão pegou três vezes o mesmo problema: a IA explicava a movimentação com termo técnico ("conclusos para sentença") e o cliente respondia perguntando o que era. Ajuste da semana: uma lista de termos com a tradução para o cliente, colocada no código do escritório. Versão 0.4 para a semana 2.

Na semana 2, a revisora aprovou dezenas de mensagens seguidas, em poucos segundos cada, sem nenhuma correção. Em vez de comemorar, o titular colocou na fila uma mensagem de teste, de um caso fictício, com a data da audiência errada. Passou.

O que mudou: o POP ganhou um critério de pronto para a revisora ("data e horário conferidos no sistema do tribunal antes de aprovar") e o passo de mensagens com data voltou a exigir essa conferência explícita. O registro marca o passo, a data e o motivo.

## 4. Medição antes e depois

Escritório fictício de Previdenciário, POP de petição inicial, 20 peças na semana 2 do piloto (exemplo).

| Indicador | Antes | Piloto, semana 2 | Como calcular |
|---|---|---|---|
| Tempo por execução | 150 min | 95 min | Antes: registro de horas ÷ volume. Depois: execução + revisão + retrabalho ÷ execuções. |
| Retrabalho | 15% | 10% | Execuções que voltaram ÷ total de execuções. |
| Erros pegos na revisão | não medido | 7 em 20 | Execuções com pelo menos uma correção ÷ total. |
| Erros que passaram | não medido | 0 | Contagem simples. Meta zero. |

Com 80 execuções por mês (exemplo):
- por execução: 55 minutos a menos (cerca de 37% menos tempo);
- por mês: 55 × 80 ÷ 60 = cerca de 73,3 horas;
- retrabalho: 5 pontos a menos.

Leitura: ganho consistente. O tempo caiu sem aumentar o retrabalho e nenhum erro passou. "Não medido" é uma resposta honesta: quase nenhum escritório media erro antes. As horas só viram resultado se alguém decidir para onde elas vão: esse destino, e o valor delas, são da `medir-retorno`.

O arquivo `scripts/exemplos/registro-piloto-exemplo.tsv` traz outro registro fictício, com sinal de carimbo e uma invenção pega na revisão, e `scripts/exemplos/analise-exemplo.md` mostra a saída do script para ele.
