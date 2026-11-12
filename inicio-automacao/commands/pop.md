---
description: Leva um processo do jeito que ele acontece hoje até a habilidade do POP, na ordem certa: POP com S, A e H, fluxograma, teste, versão vigente guardada e, por fim, a habilidade do Claude.
---

# /inicio-automacao:pop

Você vai conduzir um processo do escritório pelo caminho completo do POP, uma etapa por vez, esperando o ok do advogado entre elas. Siga as regras de `${CLAUDE_PLUGIN_ROOT}/docs/regras-transversais.md`: uma pergunta por vez, nada de dado de cliente sem anonimizar, nada inventado.

## 1. Situar

1. Procure `escritorio/perfil.md`. Se não existir, faça o modo rápido das regras transversais (porte, áreas, conta de IA) e pergunte qual é o setor-alvo. Sugira o `/inicio-automacao:comecar` para depois, sem travar o caminho.
2. Procure `escritorio/03-pops/00-mapa-de-pops.md` e os POPs do setor. Se o processo já tiver POP, mostre o código, a versão, o status e o degrau, e comece pela etapa que falta.
3. Pergunte: "Qual processo do setor [SETOR] vamos levar até a habilidade? Diga em uma frase o que ele entrega."

## 2. O caminho

Mostre o caminho em uma lista curta e marque onde o processo está:

| Etapa | Skill | Sai daqui com |
|---|---|---|
| 1. POP v0.1 (rascunho) | `escrever-pop` (ou a skill do setor: `organizar-producao-de-pecas`, `organizar-atendimento-whatsapp`) | Os 12 campos com S, A e H, o fluxograma em Mermaid e em texto, a lista do que a IA vai consultar |
| 2. Desenho | `desenhar-fluxograma` | As raias (IA, Equipe, Advogado) e as decisões e exceções que o desenho revelou |
| 3. Teste | `testar-pop` | Checklist de qualidade, teste de mesa, teste com a IA em três casos e a versão 1.0 |
| 4. Riscos | `auditar-riscos` | Linha vermelha, sigilo, pontos de erro e plano para erro conferidos |
| 5. Versão vigente | `gerir-pops` | Código, dono, mapa de POPs atualizado, versão vigente guardada e no Projeto no Claude |
| 6. Base | `inventariar-base` e `montar-base` | O inventário da pasta que existe e o que o POP cita, organizado, com índice e dono |
| 7. Instruções | `desenhar-automacao` | Prontidão conferida, nível-meta 3 e uma instrução para cada passo S e A |
| 8. Habilidade | `pop-para-skill` | A habilidade do POP, pronta para instalar: segue os passos na ordem, para em cada A e nunca executa um H |

Acione a skill de cada etapa e, ao terminar, volte a este quadro antes de seguir.

## 3. Atalhos permitidos

- **Com pressa:** as etapas 2 e 4 podem ficar para depois, registradas em "Etapas puladas" do `perfil.md`. As etapas 3, 5 e 7 não se pulam antes da 8: habilidade feita sobre POP que ninguém testou espalha o erro com mais velocidade.
- **POP pronto de outro lugar:** comece na etapa 3, depois de passar o POP pela entrada C do `escrever-pop` se ele foi escrito antes da IA.

## 4. Fechamento

Mostre o processo no degrau em que ficou (`docs/glossario.md`, "Do POP à IA: os seis degraus"), o que ficou pendente com a pergunta que resolve cada pendência e o próximo passo: outro processo do mesmo setor, o próximo setor da fila (`mapear-setores`) ou a `desenhar-automacao`.
