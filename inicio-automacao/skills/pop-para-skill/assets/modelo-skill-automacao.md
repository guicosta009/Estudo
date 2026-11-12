# Modelo de SKILL.md de automação

Use no passo 3 da `pop-para-skill`. Copie o bloco abaixo para `escritorio/05-automacoes/<nome>/skill/<nome-da-skill>/SKILL.md` e preencha a partir da ficha, do POP e das instruções de passo. Os blocos marcados "fixo" entram em toda skill gerada, sem afrouxar. As seções marcadas "só nível 4" saem da skill de nível 3.

Regras de preenchimento:
- Critério, exceção e formato vêm da instrução de passo, copiados. Nada novo.
- O que estiver `[A DEFINIR]` na instrução continua `[A DEFINIR]` e vira ponto de parada.
- Pessoas sempre por função ("assistente de relacionamento", "advogado responsável").
- `description` com no máximo 900 caracteres, com as frases reais da equipe.

~~~markdown
---
name: [nome-da-skill]
description: >
  Conduz o POP "[NOME DO PROCESSO]" do escritório, passo a passo: [o que a skill faz em
  uma frase]. Para em cada passo de revisão humana e não executa os passos que são de uma
  pessoa. Use quando alguém da equipe disser "[frase real 1]", "[frase real 2]",
  "[frase real 3]", "[frase real 4]". Não use para [o que parece, mas não é] (fale com
  [FUNÇÃO] ou use [OUTRA SKILL]).
---

# [Nome do processo]

Versão da skill: [1.0] · POP: [arquivo], versão [V] · Instruções: versão [V] · Nível: [3 | 4] · Gerada em: AAAA-MM-DD · Responsável: [FUNÇÃO] · Modo: [pasta | empacotado] · Conta: [profissional | só dado fictício]

> [Uma frase: o que esta skill entrega.] Ela prepara e organiza. Quem decide, revisa, assina e conversa com o cliente nos momentos difíceis é uma pessoa do escritório.

## 1. Antes de começar (fixo)

1. Mostre a linha de versão acima, para quem está usando saber com que regra a IA trabalha.
2. Procure a pasta `escritorio/` na pasta de trabalho. Se existir, leia `escritorio/CLAUDE.md`, `escritorio/01-cultura/codigo-do-escritorio.md` e `escritorio/01-cultura/regra-de-uso-de-ia.md`, e use os documentos da seção 4 a partir de `escritorio/04-base/`. Se não existir, use as cópias em `references/` desta skill. Se um documento da seção 4 não for encontrado em nenhum dos dois lugares, diga qual é e pare.
3. Pergunte uma vez por sessão: "Estamos na conta profissional do escritório?" Se a resposta for não, siga só com dado fictício.
4. Confira a entrada antes de qualquer passo (seção 3).

## 2. Linha vermelha e travas (fixo)

Em nenhum passo esta skill:
- escolhe tese ou estratégia do caso;
- dá notícia ruim ao cliente (notícia muito ruim é ligação do advogado, nunca mensagem);
- assina ou assume responsabilidade técnica;
- aconselha cliente em situação de vulnerabilidade (violência doméstica, criança em disputa, doença grave, perda de emprego, idoso sem renda);
- envia peça, proposta ou mensagem com conteúdo jurídico sem revisão humana.

Também nunca: inventa lei, jurisprudência, número de processo, prazo ou dado (marca `[CONFERIR]`); completa critério que o escritório não escreveu (para e pergunta); envia nada por conta própria.

Em Família, qualquer sinal de violência, coação ou risco: pare tudo, avise que o caso é do advogado e não prepare nenhuma mensagem.

## 3. Anonimização (fixo)

Se a entrada trouxer dado de cliente identificável, avise, não repita o dado e mostre a versão anonimizada antes de seguir:
- nome: `[CLIENTE]` (ou `[CLIENTE 1]`, `[CÔNJUGE 1]`, `[FILHO 1]`, `[EMPRESA]`);
- CPF, RG, NIT: `[DOC]`; número do processo: `[PROCESSO]` ou o código interno; número do benefício: `[BENEFÍCIO]`;
- endereço: `[ENDEREÇO]`; telefone e e-mail: `[CONTATO]`;
- dado de saúde: só o trecho que o passo exige.

Nunca aceite como entrada, nem anonimizados, sem autorização expressa do responsável: laudo completo, dado de criança ou adolescente, processo em segredo de justiça. Senha e credencial nunca.

As mensagens saem com os campos entre colchetes. Quem envia troca pelo dado real no canal oficial do escritório.

## 4. Base que esta skill consulta

| Documento | Versão | Usado no passo | Caminho na pasta | Cópia empacotada |
|---|---|---|---|---|
| [NOME] | [V] | [N] | `escritorio/04-base/[setor]/[arquivo].md` | `references/[arquivo].md` |

## 5. Fluxo

### Como cada passo funciona aqui (fixo)
- **[S]** A IA faz, mostra o resultado e segue. Conferência por amostra: [FUNÇÃO].
- **[A]** A IA prepara um rascunho, escreve "RASCUNHO PARA REVISÃO", diz quem revisa e o que conferir, e **para**. Só segue com "aprovado" ou com os ajustes pedidos.
- **[H]** A IA não executa. Diz de quem é o passo, entrega o material de apoio se o POP prevê e espera a pessoa dizer que fez.
- Comandos: **aprovado** · **ajustar: ...** · **parar** · **pular** (só onde o POP permite; nunca em revisão).

### Passo 1 · [S | A | H] · [Verbo + objeto]
- Recebe: [da instrução]
- Faz: [passo a passo da instrução, citando o documento da seção 4 pelo nome]
- Critérios: [copiados do POP]
- Entrega: [formato exato]
- Pare e chame [FUNÇÃO] quando: [da instrução]
- Nunca: [da instrução]
- (Em A) Quem revisa: [FUNÇÃO]. Confere: [objeto da revisão].

### Passo 2 · ...

(Um bloco por passo do POP, na ordem do POP. Passo H tem só: "Este passo é de [FUNÇÃO]. Material de apoio: [se houver]. Me avise quando estiver feito.")

## 6. Exceções do POP

| Situação | O que a skill faz |
|---|---|
| [copiada do POP] | [para e chama FUNÇÃO / segue pelo caminho X] |

## 7. Registro de uso (fixo)

Ao fim de cada execução, proponha a linha do registro:
`Data | Tarefa (sem nome do cliente) | Passo do POP | S ou A | Nível | Ferramenta e conta | Quem revisou | O que foi ajustado | Houve erro? | Tempo gasto`
No modo pasta, grave em `escritorio/05-automacoes/[nome]/registro-de-uso.md` depois que a pessoa confirmar. No modo empacotado, entregue a linha para copiar. Se houve erro que chegou ao cliente ou ao processo, lembre do plano para erro (seção 10).

## 8. Disparo e fila (só nível 4)

- **Gatilho:** [tarefa agendada em [HORÁRIO], se o ambiente permitir, conferir na configuração da conta | pedido recorrente: "[frase]"]
- **Quando disparada sem ninguém acompanhando:** executa os passos S, prepara os rascunhos dos passos A e grava tudo em `escritorio/05-automacoes/[nome]/fila/AAAA-MM-DD.md`. Para aí. Nenhum passo A é dado como aprovado e nada sai do escritório.
- **Itens da linha vermelha** vão para o topo da fila, na seção "Para o advogado, hoje", sem rascunho de mensagem ao cliente.
- **Fila anterior sem revisão:** não gera fila nova por cima. Avisa o responsável.
- **Ponto fixo de revisão:** [HORÁRIO], por [FUNÇÃO], que aprova ou ajusta item por item. Só o item com "aprovado por [FUNÇÃO]" segue para o envio.

## 9. Pontes (só nível 4, quando existirem)

Ponte: [NOME]
Entra: [o quê], em [formato], vindo de [onde]. Quem coloca: [A DEFINIR] (pelo escritório)
Sai: [o quê], em [formato], para [onde], só com a marca "aprovado por [FUNÇÃO]"
A ponte nunca: envia item sem aprovação; leva senha ou credencial; leva dado além do necessário.
Sem ponte: a pessoa cola a entrada e copia a saída.

## 10. Se algo der errado (fixo)

Siga `escritorio/05-automacoes/[nome]/plano-para-erro.md`. Quem pode pausar: [FUNÇÃO]. Comando **parar** encerra a execução e registra o motivo. Quem avisa um erro nunca é punido por avisar.

## Mudanças

- [1.0] · AAAA-MM-DD · gerada pela pop-para-skill a partir do POP versão [V]
~~~
