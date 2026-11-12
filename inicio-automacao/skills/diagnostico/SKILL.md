---
name: diagnostico
description: >
  Faz o diagnóstico de prontidão do escritório para automação com IA: retrato do escritório
  (porte, trilha solo ou equipe, áreas, conta de IA), 41 perguntas em 9 dimensões, nota de 0 a
  100, nível (Zero, Base, Estrutura, Automação) com 3 prioridades, mapa dos 10 setores com o
  setor-alvo provisório e, se o advogado quiser, o modelo de negócio. O cálculo é local. Grava em
  escritorio/diagnosticos/, cria ou atualiza o perfil.md e compara com a rodada anterior. Use
  quando o advogado disser "fazer o diagnóstico", "qual a nota do meu escritório", "por onde
  começo a automatizar", "meu escritório está pronto para IA?", "refazer o diagnóstico", "qual é
  o meu modelo de negócio", "qual setor atacar primeiro", ou no início do
  /inicio-automacao:comecar. Não use para medir horas com registro e confirmar o setor-alvo (use
  mapear-setores) nem para revisar o andamento do método (use revisao-periodica).
---

# Diagnóstico do escritório

> Uma foto de hoje: onde o escritório está em cultura, processos, base, IA, governança, comercial, equipe, investimento e medição, qual setor consome mais horas com mais dor e por onde começar. É a primeira camada do método e a régua para medir a evolução nas rodadas seguintes.

Regras comuns do plugin: `../../docs/regras-transversais.md` (caminho relativo à pasta desta skill). Níveis, setores, escalas de horas e de incômodo: `../../docs/glossario.md`. Trilhas: `../../docs/trilhas.md`. Pasta e `perfil.md`: `../../docs/pasta-do-escritorio.md`.

**Fonte única das perguntas:** `references/questionario.json`. Perguntas, opções, pontos, pesos, tetos, opções exclusivas, níveis, prioridades, recomendações, setores e faixas de horas estão lá. Leia o arquivo antes de começar e use os textos exatamente como estão.

## 1. Quando usar

**Use quando:**
- O escritório está começando o método (é o primeiro passo do `/inicio-automacao:comecar`).
- O advogado quer saber por onde começar, qual setor atacar ou se "está pronto para IA".
- É hora de uma nova rodada para ver a evolução (sugestão: na revisão trimestral, ou quando entra ou sai gente da equipe).
- O advogado quer só identificar o modelo de negócio: rode direto o passo 7.

**Não use quando:**
- O pedido é medir as horas de verdade, entrevistar a equipe e confirmar o setor-alvo com o potencial de IA: use `mapear-setores`. O setor-alvo do diagnóstico é provisório.
- O pedido é acompanhar indicadores, rituais e o que mudou no mês: use `revisao-periodica` ou `medir-retorno`.

## 2. Antes de começar

1. **Leia `escritorio/perfil.md`.** Se existir, esta é uma rodada seguinte: não refaça o bloco "Seu escritório" inteiro. Mostre o que está no perfil (porte, apoio ou pessoas, áreas, conta de IA) e pergunte só: "Algo mudou nisso desde a última vez?".
2. **Procure rodadas anteriores** em `escritorio/diagnosticos/`. O arquivo `.md` mais recente é a base da comparação (seção 7). Se já existir um arquivo com a data de hoje, pergunte se é para substituir ou gravar como `AAAA-MM-DD-2.md`.
3. **Rodada interrompida.** Se existir `escritorio/diagnosticos/em-andamento.json`, ofereça continuar de onde parou.
4. **Portão:** nenhum. O diagnóstico é a primeira camada. Se a pasta `escritorio/` não existir, crie só `escritorio/` e `escritorio/diagnosticos/` e avise que o restante da pasta vem com o `/inicio-automacao:comecar`.
5. **Sem perfil:** não precisa do modo rápido das regras transversais. O bloco "Seu escritório" (passo 2) já cobre porte, áreas e conta de IA, e é dele que sai o `perfil.md`.
6. **Privacidade:** diga logo no começo que o cálculo é feito aqui, no computador, e que nada é enviado para fora. O diagnóstico não pede nenhum dado de cliente.

## 3. Fluxo

### Passo 1. Abrir
Diga, com estas ideias e em poucas linhas: antes de automatizar qualquer coisa, a gente precisa saber onde o escritório está hoje. São um retrato rápido, 9 blocos curtos e o mapa dos 10 setores, uns 15 minutos (estimativa). No fim sai uma nota de 0 a 100, o nível e por onde começar. "Responda pelo que acontece hoje no escritório, mesmo que esteja longe do ideal." Pergunte se prefere responder uma pergunta por vez ou receber cada bloco inteiro de uma vez.

### Passo 2. Bloco "Seu escritório" (não pontua)
Uma pergunta por vez, na ordem do bloco `perfil` do `questionario.json`:
1. Nome ou apelido do escritório para os documentos (opcional).
2. **Porte:** Só eu, com ou sem estagiário ou secretária · 2 a 5 pessoas · 6 a 20 pessoas · Mais de 20 pessoas. É esta resposta que **define a trilha**: "Só eu" leva à trilha solo, as demais à trilha equipe (`docs/trilhas.md`).
3. Trilha solo: se tem estagiário(a), secretária(o), os dois ou ninguém. Trilha equipe: quem trabalha no escritório, por função (ex.: 2 advogadas, 1 estagiário). Nunca peça nomes.
4. Papel de quem responde.
5. Áreas de atuação (múltipla).
6. Processos ativos, mais ou menos.
7. Tipo de conta de IA.

Ao final, diga a trilha em uma frase: "Pelo porte, o escritório segue a trilha solo. Isso muda algumas perguntas e o jeito de cada etapa daqui para a frente." Se a conta for pessoal gratuita, avise já: ela serve só para teste com dado fictício; dado de cliente só em conta profissional ou de equipe.

### Passo 3. As 9 dimensões
Siga a ordem do arquivo: Cultura e liderança, Processos e POPs, Base de conhecimento, Uso de IA, Governança e proteção de dados, Comercial e marketing, Equipe, Investimento, Medição.

Em cada bloco:
- Abra com o nome do bloco e a frase de `intro`. Pode dizer o peso ("vale 17 pontos").
- **Uma pergunta por vez**, com o texto e as opções exatos, numerados a partir de 1 para o advogado. Não reescreva opção. Se ele pedir, explique um termo (POP, CRM, anonimizar) em uma linha.
- **Não mostre os pontos das opções** antes do resultado, para não puxar a resposta.
- **Aceite várias respostas de uma vez.** Se o advogado responder "1b, 2a, 3d" ou contar tudo num parágrafo, distribua as respostas, mostre como entendeu e peça confirmação só do que ficou ambíguo. Quem pediu o bloco inteiro recebe o bloco inteiro.
- **Opção "Trabalho sozinho(a)"** (c1, c2, c3, i5, e1): ofereça só na trilha solo, como última opção. Vale 0,5. Solo com estagiário ou secretária pode escolher uma opção comum, se a pergunta descreve o que acontece com essa pessoa. Na trilha equipe, não ofereça.
- **Múltipla escolha** (b3, i2, i3, m2, cm0): diga "pode marcar várias". A opção exclusiva ("Nenhum desses", "Nenhuma", "Ainda não uso", "Nenhum") não combina com as outras: se vier junto, pergunte qual vale.
- **g2 (contas de IA):** proponha a opção que corresponde à conta informada no passo 2 (campo `sugere_g2`) e peça confirmação. Para conta profissional ou de equipe, confirme se tem controle de acesso e se os dados não são usados para treino. Se ele não souber, registre a resposta que ele escolher e anote "conferir na configuração da conta".
- **cm0 (origem dos clientes)** não pontua, mas pergunte: ajuda a ler o modelo de negócio.
- **"Não sei":** peça a opção mais próxima do que acontece hoje, com um exemplo concreto ("e na última vez que alguém tirou férias?"). Se a dúvida continuar, registre a opção de menor pontuação entre as que ele considerou e marque `[A CONFIRMAR]` no arquivo. Todas as perguntas que pontuam precisam de resposta.
- A cada dois ou três blocos, diga quanto falta ("faltam 3 blocos e o mapa de setores").
- Com acesso a arquivos, grave as respostas em `escritorio/diagnosticos/em-andamento.json` ao fim de cada bloco, no formato da seção 8, gravando o **rótulo exato** da opção (evita erro de contagem entre o número mostrado e o índice do arquivo).

### Passo 4. Mapa dos 10 setores (não pontua)
Explique: "Para cada setor, quantas horas por semana ele consome, somando todo mundo que toca nele, e quanto ele incomoda hoje." Lembre as regras do glossário: contar o tempo picado (WhatsApp, ligação rápida, procurar documento); na dúvida entre duas faixas, a maior; setor terceirizado continua no mapa com as horas de coordenação.

Para cada um dos 10 setores (nomes e exemplos do arquivo):
- **Horas por semana:** Não temos · 1 a 3 h · 4 a 8 h · 9 a 15 h · 16 a 25 h · 26 h ou mais.
- **Incômodo (1 a 5)**, obrigatório quando o setor tem horas. Leia a escala do glossário na primeira vez (1 "quase não lembro que existe" até 5 "cliente reclama, prazo fica em risco ou tira o seu sono").

O advogado pode responder em tabela ou numa frase por setor. Todos os 10 precisam de resposta: se o setor não existe, "Não temos". No solo, Gestão de equipe costuma ser "Não temos".

Feche com o campo opcional: "Em uma frase: qual é o maior gargalo do seu escritório hoje?" (até 280 caracteres). Se aparecer dado de cliente, avise, não repita o dado e grave a versão anonimizada.

### Passo 5. Calcular
- **Com Python:** grave as respostas em `escritorio/diagnosticos/em-andamento.json` e rode, a partir da pasta da skill:
  `python3 scripts/calcular_diagnostico.py <pasta>/escritorio/diagnosticos/em-andamento.json --anterior <último AAAA-MM-DD.md> --perfil <pasta>/escritorio/perfil.md --formato md`
  (`--anterior` e `--perfil` só se existirem). O script devolve o arquivo da rodada pronto. Se ele acusar erro (resposta faltando, opção exclusiva junto com outra, rótulo não encontrado), corrija com o advogado e rode de novo.
- **Sem Python:** faça a conta da seção 4 com os pontos do `questionario.json`, mostre a conta de cada dimensão em uma linha e preencha `assets/modelo-resultado.md`.

### Passo 6. Mostrar o resultado
Nesta ordem:
1. **Nota e nível**, com a frase e o texto do nível. Lembre: "A nota é uma foto de hoje, feita por você. Ela não julga o seu trabalho. O valor está na comparação com a próxima rodada."
2. **As 9 dimensões:** pontos, peso e percentual.
3. **As 3 prioridades do nível**, com a skill que cuida de cada uma. Na trilha solo, use o `detalhe_solo` quando existir.
4. **Também merece atenção** (seção 5), com a recomendação de cada dimensão.
5. **Cuidados com dados e revisão**, se algum alerta do arquivo disparou (conta pessoal gratuita, documento de cliente "do jeito que está", conferência só "quando dá tempo" ou nenhuma).
6. **Setor-alvo provisório**, os 5 primeiros do ranking e o total de horas mapeadas.
7. **Trilha** e **próximo passo** (seção 12).
8. Na rodada seguinte, a **evolução** (seção 7).

Pergunte: "Alguma coisa aqui não bate com o que você vê no dia a dia?" Se ele mudar uma resposta, refaça a conta. A nota acompanha as respostas: ela só muda quando uma resposta muda.

### Passo 7. Modelo de negócio (opcional)
Ofereça: "Quer identificar o modelo de negócio do escritório? São 6 perguntas, uns 3 minutos. Ele ajuda a ler o setor-alvo e a escolher os primeiros POPs."
- Use as perguntas do bloco `quiz_modelo`, uma por vez. A pergunta 1 pode sair do porte: solo leva a "Só eu, às vezes com estagiário ou secretária"; 2 a 5 leva a "De 2 a 10 pessoas, sem departamentos separados"; nas outras faixas, pergunte. Confirme sempre.
- **Pontuação:** opção que aponta para um modelo só dá 2 pontos a ele; opção que aponta para vários dá 1 a cada. Vence quem tem mais pontos. Empate: ordem full service, boutique, volume, solo, consultivo, digital, correspondência. Se o segundo tiver pontos e ficar até 2 atrás, o escritório tem traços dos dois: mostre a combinação, se ela estiver na lista de híbridos.
- Ainda em dúvida: use a tabela de sinais de `references/modelos-de-negocio.md`.
- Mostre o **que muda** no perfil: setor-alvo provável (e o alternativo), mistura de S, A e H, tipo de base, risco que mais pesa e primeiro passo típico. Ofereça abrir o perfil completo em `references/modelos-de-negocio.md`.
- **O modelo orienta, o mapa decide.** Se o setor do perfil for diferente do setor-alvo do diagnóstico, siga o diagnóstico, que usa as horas do escritório, e anote por que o perfil apontou outro.

### Passo 8. Gravar
Depois do ok do advogado: grave `escritorio/diagnosticos/AAAA-MM-DD.md`, crie ou atualize `escritorio/perfil.md` (seção 9; mostre as mudanças antes) e apague o `em-andamento.json`.

## 4. Como a nota é calculada

Sem script, a conta é esta:

1. **Nota de cada pergunta (0 a 1).** Escolha única: o valor `pontos` da opção. Múltipla escolha: opções marcadas que não são exclusivas, limitadas ao `teto`, divididas pelo teto. Opção exclusiva dá 0. Pergunta com `"pontua": false` (cm0) fica fora.
2. **Percentual da dimensão** = média das notas das perguntas dela.
3. **Pontos da dimensão** = percentual × peso. Pesos: Processos 17, Cultura 14, Base 13, IA 13, Governança 11, Comercial 11, Medição 9, Equipe 7, Investimento 5 (somam 100).
4. **Nota final** = soma dos pontos das 9 dimensões, arredondada (meio ponto para cima).
5. **Exibição:** pontos com uma casa decimal, percentual inteiro.

**Exemplo resolvido** (escritório solo fictício, `scripts/exemplos/solo-rodada-1.json`):

| Dimensão | Notas das perguntas | % | Pontos |
|---|---|---|---|
| Cultura (14) | 0,5 + 0,25 + 0,5 + 0,3 + 0,35 + 0,3 = 2,2 ÷ 6 | 36,7% | 5,13 |
| Processos (17) | 0,3 + 0,35 + 0,3 + 0,3 + 0,3 = 1,55 ÷ 5 | 31% | 5,27 |
| Base (13) | 0,3 + 0,35 + (3 de teto 6 = 0,5) + 0,3 = 1,45 ÷ 4 | 36,3% | 4,71 |
| IA (13) | 1 + (3 de teto 3 = 1) + (4 de teto 6 = 0,667) + 0,4 + 0,5 = 3,567 ÷ 5 | 71,3% | 9,27 |
| Governança (11) | 0 + 0,4 + 0,35 + 0,2 + 0,1 + 0,7 = 1,75 ÷ 6 | 29,2% | 3,21 |
| Comercial (11) | 0,3 + 0,35 + 0,3 + 0 + 0,3 = 1,25 ÷ 5 (cm0 fora) | 25% | 2,75 |
| Equipe (7) | 0,5 + 0,4 + 0,35 = 1,25 ÷ 3 | 41,7% | 2,92 |
| Investimento (5) | 0,65 + 0,35 + 0,35 = 1,35 ÷ 3 | 45% | 2,25 |
| Medição (9) | 0,3 + ("Nenhum" = 0) + 0,35 = 0,65 ÷ 3 | 21,7% | 1,95 |

Soma 37,46, nota **37**, nível **Base**. O script dá o mesmo resultado (veja a seção 8).

## 5. Níveis, prioridades e "também merece atenção"

| Nota | Nível | Frase | Prioridades fixas (texto completo no arquivo) | Dimensões que as prioridades já cobrem |
|---|---|---|---|---|
| 0 a 25 | Zero | O escritório roda na cabeça das pessoas. | 1. Escrever como o setor-alvo funciona hoje. 2. Regra de uma página do que pode ir para a IA. 3. Pasta única com os 10 modelos mais usados. | Processos, Governança, Base |
| 26 a 50 | Base | Existe organização, mas ela não está escrita. | 1. Transformar o que já funciona em POP, a partir do setor-alvo. 2. Base por área num Projeto no Claude. 3. Medir as horas de 2 ou 3 setores. | Processos, Base, Medição |
| 51 a 75 | Estrutura | Processos escritos em parte, IA em uso pontual. | 1. Completar os POPs críticos com um dono cada. 2. Padronizar o uso de IA. 3. Escolher o primeiro fluxo para automatizar de ponta a ponta. | Processos, IA |
| 76 a 100 | Automação | Pronto para automatizar. | 1. Desenhar a automação dos 3 fluxos com mais horas, com antes e depois. 2. Conectar a IA a agenda, e-mail, drive, CRM e software jurídico. 3. Medir horas devolvidas e decidir onde reinvestir. | Nenhuma |

**Também merece atenção:** entram as dimensões com percentual **menor que 60%**, da menor para a maior, **no máximo 3**, tirando as que o nível já cobre. Empate de percentual: vale a ordem das dimensões no arquivo. Cada uma vem com a sua `recomendacao` e a skill que cuida dela (na trilha solo, Equipe usa a `recomendacao_solo`). No exemplo da seção 4 (nível Base), ficam Comercial (25%), Governança (29%) e Cultura (37%).

## 6. Setor-alvo provisório

- **Pontuação** = valor da faixa de horas × incômodo (se faltar o incômodo, conta 1 e marca `[A CONFIRMAR]`). Valores das faixas: Não temos 0 · 1 a 3 h = 2 · 4 a 8 h = 6 · 9 a 15 h = 12 · 16 a 25 h = 20 · 26 h ou mais = 30.
- Setores com 0 h ficam fora. Ordem decrescente de pontuação. **Empate: vence o setor com mais horas.** Persistindo, vale a ordem dos setores no arquivo.
- O maior é o **setor-alvo provisório**; o segundo vai para `proximo_da_fila` no perfil. Mostre os 5 primeiros e o total de horas dos 10 setores.
- Exemplo (fictício, `scripts/exemplos/equipe.json`): Produção de peças 30 h × 4 = 120; Prazos 20 × 5 = 100; Atendimento 20 × 4 = 80; Comercial 30 × 2 = 60 e Relacionamento 20 × 3 = 60. No empate em 60, Comercial fica na frente por ter mais horas.
- "Provisório" porque as horas são faixas estimadas. O `mapear-setores` confirma com o registro de horas e o potencial de IA, e a regra do glossário decide quando as duas contas discordam.

## 7. Rodadas seguintes: comparar

- Leia o bloco "Dados para a próxima rodada" do diagnóstico anterior (é ele que o script usa com `--anterior`).
- Mostre: nota antes e agora, nível, **pontos por dimensão com a diferença**, setor-alvo e horas mapeadas.
- Avise quando a comparação pede cuidado: a trilha mudou (as opções "Trabalho sozinho(a)" mudam de régua em Cultura, IA e Equipe); a versão do questionário mudou; o setor-alvo mudou (confirme no `mapear-setores` antes de trocar um POP em andamento).
- Leia sem julgar. Nota que cai também é dado: pode ser o escritório enxergando melhor o que antes respondia por otimismo.
- No `perfil.md`, acrescente uma linha no Histórico com a nova nota.

## 8. O script e o formato das respostas

`scripts/calcular_diagnostico.py` usa só a biblioteca padrão do Python 3, lê `references/questionario.json` e um JSON de respostas, e imprime o resultado em JSON e o arquivo da rodada em markdown. Não acessa a internet.

**Formato do JSON de respostas:**

```json
{
  "data": "AAAA-MM-DD",
  "perfil": {
    "escritorio": "Nome ou apelido",
    "porte": "solo",
    "apoio": "Estagiário(a)",
    "pessoas": "só na trilha equipe, por função",
    "papel": "Titular ou sócio(a)",
    "areas": ["Previdenciário"],
    "volume": "51 a 200",
    "conta_de_ia": "pessoal-paga"
  },
  "respostas": {
    "c1": "Trabalho sozinho(a)", "c2": "Delego, mas refaço boa parte",
    "b3": ["Modelos de petição", "Teses organizadas por área"],
    "m2": ["Nenhum"]
  },
  "setores": {
    "atendimento": {"horas": "4 a 8 h", "incomodo": 3},
    "equipe": {"horas": "Não temos"}
  },
  "gargalo": "uma frase, sem dado de cliente",
  "modelo": {"q1": "Só eu, às vezes com estagiário ou secretária", "q2": 1}
}
```

- **Ids** das perguntas: os do arquivo (`c1` a `c6`, `p1` a `p5`, `b1` a `b4`, `i1` a `i5`, `g1` a `g6`, `cm0` a `cm5`, `e1` a `e3`, `v1` a `v3`, `m1` a `m3`, `q1` a `q6`). Ids dos setores: `atendimento`, `comercial`, `producao`, `prazos`, `audiencias`, `financeiro`, `relacionamento`, `marketing`, `equipe`, `administrativo`.
- **Opção:** o rótulo exato (preferível), um começo de rótulo que só sirva para uma opção, o `valor` (no bloco perfil) ou o **índice a partir de 0** na ordem do arquivo. `"solo"` vale como atalho para "Trabalho sozinho(a)". Acentos e maiúsculas não importam.
- **Múltipla escolha:** lista. **Horas:** rótulo ou índice da faixa. **Incômodo:** 1 a 5. **`modelo`:** opcional.
- **Opções do comando:** `--anterior` (o `.md` ou `.json` da rodada anterior), `--perfil` (lê o Progresso para escolher o próximo passo), `--formato ambos|json|md`, `--saida-md` (grava o markdown num arquivo), `--permitir-incompleto` (calcula mesmo com resposta faltando e marca o resultado como incompleto).
- **Erros** (saída 2): resposta obrigatória faltando, opção exclusiva junto com outras, opção não encontrada, porte ausente. **Avisos** (não param a conta): teto ultrapassado, "Trabalho sozinho(a)" na trilha equipe, setor sem resposta, setor com horas e sem incômodo.
- **Exemplos testados** em `scripts/exemplos/`: `solo-rodada-1.json` (nota 37, Base, alvo Relacionamento com o cliente, modelo solo), `equipe.json` (nota 71, Estrutura, alvo Produção de peças, híbrido volume e digital) e `solo-rodada-2.json` (nota 49, comparado com a rodada 1). Os arquivos `*-resultado.md` ao lado mostram a saída.

## 9. O que entrega e onde grava

| Arquivo | O que tem |
|---|---|
| `escritorio/diagnosticos/AAAA-MM-DD.md` | O resultado da rodada no formato de `assets/modelo-resultado.md`: cabeçalho (escritório, rodada, quem respondeu, dono, trilha), nota, nível, dimensões, prioridades, atenção, cuidados, setor-alvo, modelo, evolução, próximo passo, todas as respostas e o bloco de dados para a próxima rodada. |
| `escritorio/perfil.md` | Criado ou atualizado no formato de `docs/pasta-do-escritorio.md`. |
| `escritorio/diagnosticos/em-andamento.json` | Temporário: respostas de uma rodada em curso. Apagado depois de gravar o resultado. |

**O que esta skill escreve no `perfil.md`:**
- Cabeçalho: `escritorio`, `porte`, `trilha`, `apoio` (só solo) ou `pessoas` (só equipe), `areas`, `conta_de_ia` (se ainda não usa IA: `nenhuma`), `nivel`, `nota`, `setor_alvo`, `proximo_da_fila`, `atualizado_em` e, na primeira vez, `criado_em`.
- `modelo_de_negocio`: só se o teste foi feito. Híbrido grava `hibrido` e registra no Histórico os dois modelos (ex.: "volume + digital").
- Progresso: marca `[x] Diagnóstico`.
- Histórico: "AAAA-MM-DD: diagnóstico, nota X, nível Y, setor-alvo provisório Z" (e a troca de trilha ou de setor-alvo, se houve).
- Nunca apaga Etapas puladas nem linhas antigas do Histórico. Mostre o que muda antes de gravar.

**Sem acesso a arquivos:** entregue o resultado e o `perfil.md` no chat, em blocos prontos para copiar, com o caminho onde cada um deve ficar.

## 10. Trilha solo e trilha equipe

- **Solo:** ofereça "Trabalho sozinho(a)" em c1, c2, c3, i5 e e1 (0,5 cada). Se houver estagiário ou secretária, essa pessoa conta como a equipe nas perguntas em que ela participa de verdade. Nas prioridades e na recomendação de Equipe, use os textos `_solo`. O foco da leitura fica nas dimensões que dependem só do titular. O próximo passo é o código do escritório escrito para o titular e para a IA, que já prepara a primeira contratação.
- **Equipe:** as perguntas de delegação, adoção e padrão comum contam inteiras, sem a opção solo. Registre as pessoas por função. Se quem respondeu não for o titular, anote o papel no cabeçalho: a foto é de quem respondeu. O próximo passo começa pelo retrato cultural, com perguntas a duas pessoas, por escrito e sem identificação.
- **Mudança de trilha** entre rodadas (o solo contratou): grave a nova trilha, avise que a comparação de Cultura, IA e Equipe muda de régua e aponte o que refazer conforme `docs/trilhas.md`.

## 11. Erros que esta skill evita

| Erro | Consequência | Como a skill evita |
|---|---|---|
| Responder pelo escritório ideal | Nota alta, prioridade errada, frustração na automação | "Responda pelo que acontece hoje" e pedido de exemplo concreto quando a resposta vem vaga |
| Mostrar os pontos antes | O advogado escolhe a opção que vale mais | Pontos só aparecem no resultado |
| Reescrever as opções | A rodada seguinte deixa de ser comparável | Textos exatos do `questionario.json` |
| Tratar o setor-alvo como definitivo | POP escrito para o setor errado | "Provisório", com confirmação no `mapear-setores` |
| Deixar o perfil do modelo decidir | Escritório típico no lugar das horas reais | "O modelo orienta, o mapa decide" |
| Mandar respostas para fora | Exposição de dados do escritório | Cálculo local, script sem rede |
| Comparar rodadas sem contexto | Leitura errada de queda ou alta | Avisos de trilha, versão e setor-alvo |

## 12. Próximo passo

Diga a próxima etapa da trilha e a skill que cuida dela:
- **Primeira rodada:** `codigo-do-escritorio`, a régua de tudo o que vem depois. Solo: o código é escrito para o titular e para a IA. Equipe: começa pelo retrato cultural com duas pessoas. Em seguida vem a `regra-de-uso-de-ia`. Se algum alerta de dados disparou, combine desde já que, até a regra existir, dado de cliente só entra anonimizado e em conta profissional.
- **Rodadas seguintes:** o primeiro item não marcado do Progresso no `perfil.md` (o script faz isso com `--perfil`).
- **Tarefa paralela, sempre:** escrever o passo a passo atual do setor-alvo, do jeito que acontece hoje, sem melhorar nada. Ele é a matéria-prima do `escrever-pop`, depois que o `mapear-setores` confirmar o setor.
