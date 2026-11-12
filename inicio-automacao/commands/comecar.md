---
description: Começa a estruturação do escritório. Cria a pasta do escritório, roda o diagnóstico e mostra a trilha (solo ou equipe) com os próximos passos.
---

# /inicio-automacao:comecar

Você vai conduzir o início da estruturação do escritório para a automação. Siga as regras de `${CLAUDE_PLUGIN_ROOT}/docs/regras-transversais.md` do plugin: uma pergunta por vez, nada de dado de cliente, nada inventado.

## 1. Abertura (curta)

Explique em poucas frases, sem tom de venda:
- O método segue a ordem: diagnóstico, cultura, mapa de setores, POP com IA, base de conhecimento, automação e medição.
- A ideia que organiza tudo: automação é um POP executado pela IA, consultando a base de conhecimento e dentro da régua da cultura. Automatizar um escritório sem processo escrito só faz a bagunça andar mais rápido.
- Tudo o que for construído fica numa pasta `escritorio/`, dentro da pasta de trabalho, para ser reaproveitado por todas as etapas.

## 2. Pasta do escritório

1. Verifique se já existe `escritorio/perfil.md` na pasta de trabalho.
   - **Existe:** não recomece do zero. Leia o perfil, mostre onde o escritório parou (como no `/inicio-automacao:status`) e pergunte se o advogado quer seguir de onde parou ou refazer o diagnóstico.
   - **Não existe:** pergunte se pode criar a pasta `escritorio/` aqui. Se o advogado preferir outro lugar, use o caminho que ele indicar.
2. Crie a estrutura descrita em `${CLAUDE_PLUGIN_ROOT}/docs/pasta-do-escritorio.md` (pastas vazias e o `CLAUDE.md` da pasta, com o nome do escritório preenchido depois do diagnóstico).
3. Se não houver acesso a arquivos nesta conversa, avise que os documentos serão entregues no chat, prontos para copiar, com o caminho de cada um.

## 3. Diagnóstico

Acione a skill `diagnostico` no modo completo. Ela define o porte, a trilha, a nota, o nível, o setor-alvo provisório e grava o `perfil.md`.

Se o advogado disser que não tem tempo agora (o diagnóstico leva cerca de 12 minutos), faça o modo rápido das regras transversais (porte, áreas, conta de IA), grave um perfil mínimo e registre em "Etapas puladas" que o diagnóstico ficou pendente.

## 4. A trilha

Mostre a trilha do escritório com base em `${CLAUDE_PLUGIN_ROOT}/docs/trilhas.md`:

**Trilha solo** (só o advogado, com ou sem estagiário ou secretária):
1. `codigo-do-escritorio`: o código do escritório, escrito para você e para a IA.
2. `regra-de-uso-de-ia`: a regra de uma página e o seu autocompromisso.
3. `nucleo-de-inovacao`: o bloco fixo semanal, tratado como audiência.
4. `mapear-setores`: o registro de horas de uma semana e o setor-alvo confirmado.
5. `escrever-pop`: o POP do setor-alvo, com S, A e H. Se o setor-alvo for produção de peças ou o WhatsApp, comece por `organizar-producao-de-pecas` ou `organizar-atendimento-whatsapp`, que chamam o `escrever-pop` para cada POP.
6. `desenhar-fluxograma`, `testar-pop` e `gerir-pops`: o desenho, o teste e a versão vigente guardada no lugar certo.
7. `inventariar-base` e `montar-base`: o inventário da pasta real e a base que o POP precisa consultar.
8. `pop-para-skill` e `desenhar-automacao`: a habilidade do POP e a primeira automação.
9. `medir-retorno` e `revisao-periodica`: a prova e a manutenção.

**Trilha equipe** (2 pessoas ou mais):
1. `codigo-do-escritorio`, com o retrato cultural respondido por duas pessoas.
2. `regra-de-uso-de-ia`, com o acordo assinado por cada pessoa.
3. `implantar-a-mudanca`: o piloto, a reunião de lançamento e a conversa com quem resiste.
4. `nucleo-de-inovacao`: os papéis do tamanho do escritório.
5. `mapear-setores`, com entrevistas de quem executa.
6. `escrever-pop`, com quem executa, confere e decide em cada passo (ou a skill do setor: `organizar-producao-de-pecas`, `organizar-atendimento-whatsapp`).
7. `desenhar-fluxograma` em raias, `testar-pop` com quem não escreveu o POP e `gerir-pops` com um dono para cada POP.
8. `inventariar-base` e `montar-base`.
9. `pop-para-skill` e `desenhar-automacao`.
10. `medir-retorno` e `revisao-periodica`.

Ajuste a lista ao nível do diagnóstico:
- **Zero ou Base:** reforce que o ganho está nas etapas 1 a 6. Não prometa automação antes delas.
- **Estrutura:** aponte quais etapas já parecem resolvidas pelas respostas do diagnóstico e onde estão as lacunas.
- **Automação:** sugira confirmar rapidamente cultura, POP e base e ir para `desenhar-automacao`.

## 5. Fechamento

- Mostre o resumo: nota, nível, trilha, setor-alvo provisório e as três prioridades do nível.
- Proponha o próximo passo concreto (normalmente `codigo-do-escritorio`) e pergunte se quer começar agora.
- Lembre que `/inicio-automacao:status` mostra o progresso a qualquer momento e que `/inicio-automacao:pop` leva direto do processo de hoje até a habilidade do POP, para quem já tem o setor-alvo escolhido.
