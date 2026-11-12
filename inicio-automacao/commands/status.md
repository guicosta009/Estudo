---
description: Mostra em que etapa da estruturação o escritório está, o que já foi construído, o que ficou pendente e qual é o próximo passo da trilha.
---

# /inicio-automacao:status

Mostre o estado da estruturação do escritório, sem fazer perguntas desnecessárias.

## 1. Ler

1. Procure `escritorio/perfil.md` na pasta de trabalho. Se não existir, diga que a estruturação ainda não começou e ofereça `/inicio-automacao:comecar`.
2. Leia o perfil (porte, trilha, nível, nota, setor-alvo, progresso, etapas puladas).
3. Confira o que existe de fato na pasta, porque o progresso do perfil pode estar desatualizado:
   - `diagnosticos/`: data e nota do último diagnóstico.
   - `01-cultura/codigo-do-escritorio.md` e `instrucoes-do-projeto.md`: versão e data.
   - `01-cultura/regra-de-uso-de-ia.md` e `01-cultura/acordos/`: quantos acordos (na equipe, compare com o número de pessoas).
   - `01-cultura/nucleo/`: plano de 90 dias e última ata.
   - `02-mapa/`: ranking e plano 5W2H.
   - `03-pops/`: o `00-mapa-de-pops.md` (quantos POPs, de quais setores, com que status e em que degrau), se cada POP vigente tem teste em `testes/` e auditoria, e se há mais de uma versão vigente do mesmo código.
   - `04-base/INDICE.md` e `04-base/casos-de-teste/`.
   - `05-automacoes/`: quais automações, em que nível, com plano para erro.
   - `06-medicao/`: valor da hora, linha de base, último painel, incidentes abertos.
4. Se o que está na pasta divergir do perfil, atualize o progresso do `perfil.md` e avise o que mudou.

## 2. Mostrar

Um quadro curto:

| Etapa | Situação | Onde está |
|---|---|---|
| Diagnóstico | feito em [DATA], nota [N], nível [NÍVEL] | `diagnosticos/` |
| Código do escritório | versão [V] de [DATA] / pendente | `01-cultura/` |
| ... | ... | ... |

Depois:
- **Etapas puladas**, se houver, com o risco de cada uma em uma linha (por exemplo: "POP sem código do escritório: a IA escreve no tom errado").
- **Alertas de manutenção:** código sem revisão há mais de um mês; POP sem revisão há mais de 90 dias (6 meses para POP só com passos H); POP vigente sem teste ou sem dono; POP no Projeto no Claude em versão diferente da vigente; diagnóstico com mais de três meses; automação sem registro de uso; incidente sem mudança no POP; painel do mês anterior não preenchido.
- **Próximo passo:** uma única recomendação, com a skill que cuida dela, seguindo a ordem da trilha em `${CLAUDE_PLUGIN_ROOT}/docs/trilhas.md`.

Não refaça nenhuma etapa por conta própria. Só mostre e recomende.
