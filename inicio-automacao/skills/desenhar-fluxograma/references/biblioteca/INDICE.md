# Biblioteca de fluxogramas: índice

Dez fluxogramas de referência, um por setor, desenhados para um escritório genérico com equipe. Cada um traz o desenho em Mermaid e em texto numerado, com a sigla S, A ou H em cada ação e a revisão marcada nos passos A. Os processos escolhidos complementam os POPs por setor da biblioteca do `escrever-pop`: lá está o procedimento principal de cada setor, aqui está um segundo fluxo que costuma travar o escritório.

Nenhum deles vale como está. Use o do setor do escritório como gabarito para **conferir** o desenho feito a partir do retrato, e nunca como substituto do retrato: o valor está em descobrir onde o escritório é diferente.

| Arquivo | Processo | Setor | Gatilho | Caixas | S | A | H | Decisões |
|---|---|---|---|---|---|---|---|---|
| `atd-mensagem-nova-no-whatsapp.md` | Mensagem nova no WhatsApp do escritório | Atendimento e triagem | Qualquer mensagem recebida | 10 | 3 | 3 | 1 | 3 |
| `com-acompanhamento-da-proposta.md` | Acompanhamento da proposta enviada | Comercial | Proposta enviada ao cliente | 10 | 5 | 1 | 1 | 3 |
| `pec-da-intimacao-ao-protocolo.md` | Da intimação à peça protocolada | Produção de peças | Intimação com prazo | 12 | 1 | 5 | 3 | 3 |
| `prz-do-prazo-ao-cumprimento.md` | Do prazo lançado ao prazo cumprido | Prazos e controladoria | Prazo conferido na agenda | 10 | 3 | 1 | 3 | 3 |
| `aud-pos-audiencia.md` | Depois da audiência: registro, cliente e próximos passos | Audiências e diligências | Audiência realizada | 9 | 1 | 4 | 2 | 2 |
| `fin-repasse-ao-cliente.md` | Valor liberado: repasse ao cliente | Financeiro e cobrança | Alvará, requisição de pagamento ou acordo pago | 9 | 2 | 3 | 3 | 1 |
| `rel-resposta-de-andamento.md` | "Como está o meu processo?" | Relacionamento com o cliente | Pergunta de andamento | 9 | 2 | 4 | 1 | 2 |
| `mkt-comentario-ou-direct.md` | Comentário ou direct numa publicação | Marketing e conteúdo | Interação recebida | 10 | 2 | 3 | 1 | 4 |
| `eqp-delegar-tarefa.md` | Delegar uma tarefa com padrão de entrega | Gestão de equipe | Tarefa a delegar | 10 | 2 | 4 | 2 | 2 |
| `adm-encerramento-do-caso.md` | Encerramento e arquivamento do caso | Administrativo | Caso concluído | 9 | 2 | 3 | 2 | 2 |
| **Total** | | | | **98** | **23** | **31** | **19** | **25** |

"Caixas" conta ações e decisões; início e fim não entram. Todos ficam dentro do limite de 15.

O que a tabela mostra: todo desenho tem pelo menos um H, e em nenhum deles a IA vai do gatilho à entrega sem uma pessoa no meio. Comercial tem mais S porque o fluxo é de cadência e registro; Produção de peças e Relacionamento têm mais A porque quase tudo o que a IA faz ali chega ao cliente ou ao tribunal. Um S da biblioteca pode ser A no escritório hoje (trava por estágio do `classificar-sah`).

## Ordem de leitura sugerida

1. O fluxograma do setor-alvo.
2. O POP do mesmo setor na biblioteca do `escrever-pop`, para ver onde um termina e o outro começa.
3. O fluxograma do setor vizinho (quem entrega para o setor-alvo ou recebe dele). Atendimento leva a Comercial; Prazos leva a Produção de peças; Marketing leva a Atendimento.

## O que foi normalizado em relação ao material de origem

- **Formato do plugin:** numeração `N ·`, sigla e responsável no começo de cada ação (`[A · advogado]`), verbo no infinitivo, `[REVISÃO HUMANA]` e a classe `revisao` em todas as caixas A, versão em texto com "vá para".
- **Siglas preservadas.** Nenhuma sigla do material foi trocada. Onde o material dizia só "a IA faz X" num passo A, a caixa ganhou como dona a pessoa que confere, que o próprio material indicava ("advogado aprova", "controladoria confere", "financeiro confere").
- **Quem confere** no passo de conferência do comprovante (Prazos) não vinha no material: ficou "controladoria" com `[A CONFIRMAR]`.
- **Esperas** do Comercial viraram ações com o verbo "aguardar" (S · IA, que acompanha o tempo), como manda a regra dos três símbolos. Em Prazos, a espera pela produção da peça ficou no rótulo da seta, porque ela é outro processo.
- **Voltas acrescentadas** para não deixar seta solta, marcadas como sugestão em cada arquivo: Prazos (corrigir o comprovante volta para a conferência), Financeiro (conversa com o cliente volta para o cálculo).
- **Desvio acrescentado** em Marketing: spam e ofensa, que o material tirava do fluxo numa nota, viraram decisão e ação A, porque o material não dizia quem executa.
- **Prazos e intervalos** (D-5, D-3, D-1, 2 e 3 dias úteis, "mesmo dia útil") marcados como exemplo em todos os desenhos.
