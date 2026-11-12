# inicio-automacao

Plugin do Claude que ajuda o advogado a estruturar o escritório para a automação com IA, na ordem certa. Funciona para escritório solo e para escritório com equipe: cada um segue a sua trilha.

> Automação é um POP executado pela IA, consultando a base de conhecimento e dentro da régua da cultura.

Automatizar um escritório que não tem processo escrito, que não tem regra clara e que guarda o conhecimento na cabeça de duas pessoas só faz a bagunça andar mais rápido. O plugin conduz o escritório pelas etapas que vêm antes da automação e depois leva o POP pronto até uma skill que roda dentro do Claude.

## Como começar

```
/inicio-automacao:comecar
```

O comando cria a pasta `escritorio/` na pasta de trabalho, roda o diagnóstico e mostra a trilha. A qualquer momento:

```
/inicio-automacao:status
```

Quem já tem o setor-alvo escolhido e quer levar um processo até a habilidade do Claude:

```
/inicio-automacao:pop
```

## As etapas e as skills

| Etapa | Skill | O que entrega |
|---|---|---|
| Diagnóstico | `diagnostico` | Nota de 0 a 100 em 9 dimensões, nível, modelo de negócio, setor-alvo provisório e trilha |
| Cultura (a régua) | `codigo-do-escritorio` | Código do escritório em 7 seções e as instruções do Projeto no Claude |
| | `regra-de-uso-de-ia` | Política de uso, acordo (ou autocompromisso), anonimização, transparência com o cliente, livro de incidentes |
| | `implantar-a-mudanca` | Piloto, reunião de lançamento, conversa com quem resiste, rituais |
| | `nucleo-de-inovacao` | Papéis, funil de ideias, matriz impacto × esforço, plano de 90 dias |
| Mapa (o endereço) | `mapear-setores` | Atividades, registro de horas, ranking de setores, setor-alvo confirmado, plano 5W2H |
| POP (o roteiro) | `escrever-pop` | POP de 12 campos com S, A e H e fluxograma, a partir do zero, da biblioteca de 19 POPs ou de um POP antigo |
| | `classificar-sah` | Sigla e nível de inserção da IA em cada passo |
| | `auditar-riscos` | Linha vermelha, sigilo, pontos de erro, revisão humana e plano para erro |
| | `desenhar-fluxograma` | O desenho do processo em Mermaid, em texto e em raias (IA, Equipe, Advogado), com 10 fluxogramas de referência, um por setor |
| | `testar-pop` | Checklist de qualidade, teste de mesa, teste com a IA em três casos, piloto e a versão 1.0 aprovada |
| | `gerir-pops` | Código, dono, versão vigente, mapa de POPs, onde guardar, revisão por gatilho, aposentadoria e o degrau de cada POP até a habilidade |
| Setores com roteiro próprio | `organizar-producao-de-pecas` | Ciclo da peça em onze etapas, ficha de briefing, cinco POPs de peça, banco de modelos, caderno de teses e checklist de revisão |
| | `organizar-atendimento-whatsapp` | Regras de canal, os quatro fluxos do WhatsApp, régua de atualização, biblioteca de mensagens no tom do escritório e indicadores |
| Base (a memória) | `inventariar-base` | O inventário da pasta real do escritório: o retrato da bagunça, duplicados, versões, alertas de dado de cliente, a triagem proposta e o plano de reorganização, sem mover nem apagar nada |
| | `montar-base` | A base que o POP consulta, organizada, com casos de teste e o Projeto no Claude |
| Automação | `desenhar-automacao` | Prontidão, nível-meta, instrução por passo, teste e plano para erro |
| | `pop-para-skill` | A skill do processo, pronta para instalar no Claude |
| Medição (a prova) | `medir-retorno` | Valor da hora, linha de base, horas devolvidas, retorno e painel mensal |
| Manutenção | `revisao-periodica` | Rituais semanal, mensal e trimestral e a revisão das siglas |

## As trilhas

- **Solo:** o advogado sozinho, com ou sem estagiário ou secretária. Sem entrevistas nem reunião de lançamento; registro de horas reforçado; bloco fixo semanal; conferência em outro momento para compensar a falta de uma segunda pessoa; plano para erro que prevê a ausência do titular.
- **Equipe:** a partir de 2 pessoas, com intensidade ajustada ao porte (2 a 5, 6 a 20, mais de 20). Acordo assinado por cada pessoa, entrevistas com quem executa, papéis do núcleo, funções separadas em cada passo do POP.

Detalhes em `docs/trilhas.md`.

## Regras que valem em tudo

- Uma pergunta por vez, e retrato de como é hoje antes de qualquer melhoria.
- Nada inventado: `[A DEFINIR]`, `[A CONFIRMAR]` e `[CONFERIR]` marcam o que falta. Normas citadas só pelo nome.
- Dado de cliente só anonimizado e em conta profissional. Laudo completo, dado de criança ou adolescente e segredo de justiça não entram sem autorização. Senha nunca.
- A linha vermelha é sempre humana: tese, notícia ruim, assinatura, cliente vulnerável e envio sem revisão.
- A IA propõe, o advogado decide.

Detalhes em `docs/regras-transversais.md` e `docs/glossario.md`.

## Estrutura do plugin

```
.claude-plugin/plugin.json
commands/        comecar.md, status.md, pop.md
docs/            regras-transversais.md, glossario.md, trilhas.md, pasta-do-escritorio.md
skills/          as 20 skills, cada uma com SKILL.md e, quando precisa, references/, assets/ e scripts/
```

Os scripts usam Python 3. A planilha de horas precisa do pacote `openpyxl`; sem ele, a skill oferece a versão em CSV.

## Versão

0.3.1 · Correção de instalação: a pasta de exemplo da `inventariar-base`, com nomes bagunçados de propósito, saiu de dentro do plugin e passou a ser criada pelo `scripts/criar_pasta_exemplo.py`. Todos os nomes de arquivo do plugin agora usam só letras sem acento, números, ponto, hífen e sublinhado.

0.3.0 · Base de conhecimento: skill nova `inventariar-base`, com script que faz o inventário da pasta real do escritório e o plano de reorganização, e a `montar-base` ligada a ela.

0.2.0 · POP do começo ao fim: cinco skills novas (`desenhar-fluxograma`, `testar-pop`, `gerir-pops`, `organizar-producao-de-pecas`, `organizar-atendimento-whatsapp`), o comando `/inicio-automacao:pop`, código padrão dos POPs (`POP-PEC-01`), status e mapa de POPs, fluxograma em raias e os seis degraus do POP à IA no glossário.

0.1.0 · primeira versão para testes.
