# Cabeçalho completo e registro de mudanças do POP

Use na rotina 2 (padronizar) e a cada publicação. O POP já sai do `escrever-pop` com a primeira linha do cabeçalho. Esta skill acrescenta a segunda linha e completa o registro no fim do arquivo.

## 1. Topo do POP

```
# POP-[SIGLA]-[NN] [NOME CURTO DO PROCESSO]

Setor: [UM DOS 10 SETORES] · Área: [ÁREA, SE HOUVER] · Versão: [X.Y] · Atualizado em: [AAAA-MM-DD] · Dono do POP: [FUNÇÃO E NOME] · Status: [Rascunho | Em teste | Vigente | Em revisão | Aposentado] · Próxima revisão: [AAAA-MM-DD]

Aprovado por: [NOME] em [AAAA-MM-DD] · Vigente desde: [AAAA-MM-DD] · Substitui: [versão anterior, ou "primeira versão"] · Passos com IA: S [nº dos passos] · A [nº dos passos] · Onde está a versão vigente: escritorio/03-pops/[setor]/pop-[sigla]-[nn]-[processo].md · Projeto no Claude "[NOME DO PROJETO]" · skill [nome, se houver]

Se você está lendo uma versão diferente desta em outro lugar, ela está desatualizada.
```

Regras:
- Em Rascunho e Em teste, "Aprovado por" e "Vigente desde" ficam em branco e a versão é 0.x.
- "Aprovado por" é preenchido com o nome que o advogado disser. A IA nunca aprova.
- A versão não vai no nome do arquivo. Ela mora aqui e no registro.

## 2. Fim do POP: controle de versões

Substitui a tabela curta do modelo do `escrever-pop` (mesma seção, com duas colunas a mais).

```
## Controle de versões

| Versão | Data | O que mudou | Por quê | Aprovado por | Equipe avisada ou treinada em |
|---|---|---|---|---|---|
| 0.1 | [AAAA-MM-DD] | Primeiro rascunho a partir do fluxograma | Início do POP | | |
| 1.0 | [AAAA-MM-DD] | Aprovação depois do teste em [nº] casos anonimizados | Fim do teste | [NOME] | [AAAA-MM-DD] |
```

Exemplo de linha bem preenchida (fictício):

```
| 2.0 | [AAAA-MM-DD] | Passo 6 passou de S para A: a IA rascunha a lista de documentos e o advogado confere antes de enviar ao cliente | Em um mês, duas listas saíram com documento que não se aplicava ao caso | Titular | Treino de 20 min, dois dias depois da aprovação |
```

O "por quê" é o que some primeiro da memória. Mesmo que o editor de texto guarde histórico automático, escreva o registro.

## 3. Anotações de uso (logo abaixo do controle de versões)

```
## Anotações de uso (ainda sem decisão, para a próxima revisão)

- [AAAA-MM-DD] · [FUNÇÃO] · [o que aconteceu ou a dúvida que apareceu]
```

Toda vez que alguém pula um passo, faz a mesma pergunta ou repete um erro, o dono anota aqui, mesmo sem decisão. É a primeira coisa lida na revisão de 20 minutos. Anotação sem nome de cliente: use `[CLIENTE]`, `[PROCESSO]`.

## 4. Anexo de prompts (quando não houver automação desenhada)

```
## Anexo: instruções dos passos com IA · vale para a versão [X.Y]

Passo [N] · [S/A] · [verbo + tarefa]
Resultado esperado: [o que a IA entrega, em que formato]
Texto da instrução: [o prompt usado hoje]
Quem confere e o quê: [função · objeto da conferência]
```

Quando a `desenhar-automacao` gravar as instruções em `escritorio/05-automacoes/<nome>/instrucoes/`, o anexo é substituído por uma linha apontando para essa pasta.
