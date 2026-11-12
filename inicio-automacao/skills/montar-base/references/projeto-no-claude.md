# Montar o Projeto no Claude com a base

Leia esta referência no passo 8 da `montar-base`. Os nomes de tela e os recursos dos Projetos mudam conforme o plano e a versão do Claude. Por isso o roteiro abaixo descreve o que fazer, sem prometer onde fica cada botão: conferir na configuração da conta.

## 1. Antes de montar

1. **Conta.** O Projeto que vai receber documentos do escritório roda na conta profissional ou de equipe, com o tratamento de dados conferido e anotado na regra de uso de IA. Conta pessoal gratuita serve só para testar com dado fictício.
2. **Instruções prontas.** Precisa existir `escritorio/01-cultura/instrucoes-do-projeto.md`, gerado pela `codigo-do-escritorio`. Se não existir, pare aqui e ofereça a skill: sem a régua, a IA escreve rápido no tom errado.
3. **Índice fechado.** O `escritorio/04-base/INDICE.md` mostra quais documentos do setor-alvo estão "em uso". Só eles sobem.

## 2. O que vai em cada lugar

| Parte do Projeto | O que colocar | De onde vem |
|---|---|---|
| Instruções | O texto das instruções do Projeto, inteiro | `01-cultura/instrucoes-do-projeto.md` |
| Instruções (acréscimo) | Um bloco curto dizendo qual POP este Projeto atende e que a IA consulta o índice antes de usar qualquer documento | Escrito agora, com o advogado |
| Conhecimento | O POP do setor-alvo, o `INDICE.md` e os documentos "em uso" do setor-alvo | `03-pops/<setor>/` e `04-base/` |
| Conhecimento (opcional) | O código do escritório completo, se as instruções forem um resumo dele | `01-cultura/codigo-do-escritorio.md` |

**Bloco de acréscimo às instruções** (modelo, ajuste com o advogado):

```
Este Projeto atende o setor [SETOR] e segue o POP [NOME DO POP], versão [VERSÃO].
Antes de usar qualquer documento do conhecimento, confira no INDICE.md se ele está "em uso" e qual é a versão vigente.
Quando um passo do POP citar um documento que não está no conhecimento, diga qual é e pare. Não substitua por um texto seu.
Documentos com "Situação: rascunho" não valem como regra do escritório.
```

## 3. O que não colocar

- Versões antigas, "para garantir". A IA não sabe qual delas vale.
- Documentos em rascunho ou fora do índice.
- A pasta inteira do drive, sem triagem.
- Documentos de setores que o POP não cita.
- Os casos de teste. Eles ficam fora para que o teste da automação seja honesto.
- Qualquer dado de cliente, laudo, documento de criança ou adolescente, processo em segredo de justiça.
- Senha, credencial, certificado ou dado de acesso a sistema.

## 4. Testar a consulta

Depois de montar, faça três perguntas dentro do Projeto e confira as respostas com o advogado:
1. "Quais documentos você tem para o passo [N] do POP [NOME]? Diga o nome e a versão." A resposta tem que bater com o índice.
2. "Pelo documento [NOME], [pergunta prática, por exemplo: esta movimentação é rotina ou relevante?]." A resposta tem que citar o documento e seguir o critério escrito.
3. "Qual é o modelo para [algo que a base não tem]?" O acerto é a IA dizer que não tem e parar, sem inventar.

Se alguma falhar, o problema costuma estar no nome do arquivo (pouco claro), em duas versões parecidas ou num critério vago. Corrija na base, não na conversa.

## 5. Quando separar em mais de um Projeto

| Situação | Como separar |
|---|---|
| Consultivo ou partido mensal | Um Projeto por cliente-empresa. Informação de um cliente nunca aparece na consulta de outro |
| Full service com bases muito diferentes por área | Um Projeto por área, com as mesmas instruções do código |
| Pasta restrita (Família com criança, saúde, criminal) | Projeto à parte, compartilhado só com quem trabalha naqueles casos |
| Volume de documentos começou a atrapalhar | Um Projeto por setor, cada um com o seu POP e o seu pedaço da base |

## 6. Sem Projeto: a pasta aberta

Em ambientes em que o Claude trabalha direto na pasta do computador (como o Claude Code), a pasta `escritorio/` faz o papel do Projeto. O `escritorio/CLAUDE.md` manda ler o perfil, seguir o código e consultar só o que o POP cita em `04-base/`. Nesse caso:
- O índice precisa estar em dia, porque é ele que separa o vigente do arquivado.
- A pasta `04-base/_arquivo/` não deve ser consultada. Se o ambiente permitir, deixe isso escrito no `CLAUDE.md` da pasta.
- Os casos de teste ficam em `04-base/casos-de-teste/` e só são abertos durante o teste.

## 7. Manter o Projeto em dia

- Documento mudou na base: troque no Projeto no mesmo dia e tire a versão antiga.
- POP mudou: atualize o bloco de acréscimo (nome e versão) e confira os documentos.
- Na revisão trimestral, compare a lista do conhecimento do Projeto com o índice. Tudo o que está num e não está no outro é corrigido.
- Quem mexe no Projeto: no solo, o titular; na equipe, o dono da base do setor, com o responsável pela automação avisado.
