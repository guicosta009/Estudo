# Inventário sem acesso à pasta (Claude no navegador)

Leia esta referência quando a conversa não tem pasta aberta nem Python: o Claude no navegador ou no aplicativo, sem o Cowork e sem o Claude Code. O raciocínio é o mesmo do script, feito à mão com as regras de `references/regras-de-classificacao.md`. O que muda é que o advogado traz a lista e aplica o plano com as próprias mãos.

## 1. Pedir a lista de arquivos

Pergunte, uma por vez:

1. "Você consegue me mandar a lista dos arquivos da pasta de modelos? Pode colar aqui, ou me descrever o que aparece na tela, pasta por pasta."
2. "Para cada arquivo, me diga, se der, a data da última alteração e o tamanho. Na janela da pasta, o modo de exibição em lista mostra as duas colunas."
3. "Tem pasta de cliente ou de processo dentro dela? Se tiver, não precisa me dizer o que tem dentro. Só o nome da pasta, para eu deixar de fora."

**Atalhos para gerar a lista** (só se o advogado souber usar; não é obrigatório):
- Windows: abrir o PowerShell dentro da pasta (botão direito no espaço vazio da pasta, opção de abrir no Terminal ou no PowerShell; o nome do menu muda conforme a versão do Windows) e rodar `Get-ChildItem -Recurse -File | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize`. Copiar o resultado e colar na conversa.
- Mac: no Terminal, `cd` até a pasta e rodar `find . -type f -exec ls -lh {} \;`. Copiar e colar.
- Print da tela: aceito, desde que o advogado descreva em texto o que não ficar legível. Antes de mandar o print, ele confere se não aparece nome de cliente na tela.

**Se aparecer nome de cliente, CPF ou número de processo na lista:** avise, não repita o dado e passe a usar a versão mascarada (`[NOME]`, `[DOC]`, `[PROCESSO]`, `[NÚMERO]`) em tudo que escrever. A pasta de cliente que aparecer na lista vira uma linha "fora da base", sem detalhar o que tem dentro.

**Sem hash, sem duplicado exato.** À mão não dá para saber se dois arquivos têm o mesmo conteúdo. Trate como "possível duplicado" os arquivos com o mesmo nome depois de tirar as marcas de versão e o mesmo tamanho, e peça ao advogado para abrir os dois e confirmar.

## 2. Fazer o inventário à mão

Siga a mesma ordem do script e entregue as mesmas seções, em tabelas no chat:

1. **O retrato em números:** total de arquivos, por extensão, por ano da última alteração, os cinco mais antigos, quantos têm marca de versão no nome, as famílias e os possíveis duplicados.
2. **Alertas:** pastas de cliente (fora, sem abrir), arquivos com alerta alto ou médio, com o nome mascarado.
3. **Setor, área e tipo** de cada arquivo, pelas tabelas da referência de regras. Na dúvida, `[A CONFIRMAR]` e pergunte.
4. **Triagem proposta** (usar, atualizar, descartar, criar, fora da base), com o motivo.
5. **O que os POPs pedem:** peça ao advogado para colar a tabela "O que a IA vai precisar consultar" do POP do setor-alvo, ou o campo Entradas. Marque o que existe na lista e o que falta.
6. **Plano de reorganização** com o nome novo e o destino de cada arquivo.
7. **Rascunho do índice** no formato do `../montar-base/assets/indice-modelo.md`.

Para listas longas (mais de 60 arquivos), faça por pasta, uma de cada vez, e junte no fim.

## 3. Entregar o plano para o advogado aplicar

Depois do ok linha a linha, entregue três blocos prontos para copiar.

**Bloco 1. As pastas a criar** dentro de `escritorio/04-base/` (ou de `02 Base` no Drive ou no OneDrive), só as que o plano usa:

```
04-base/
  relacionamento-com-o-cliente/
  producao-de-pecas/modelos/previdenciario/
  _arquivo/
```

**Bloco 2. A tabela de cópia**, uma linha por arquivo aprovado:

| # | Arquivo de hoje | Copiar para | Nome novo | Antes de copiar |
|---|---|---|---|---|
| (exemplo) 8 | criterios relevancia movimentacao prev.txt | relacionamento-com-o-cliente/ | criterios-relevancia-movimentacao-previdenciario.txt | nada |
| (exemplo) 20 | replica INSS 2019.docx | producao-de-pecas/modelos/previdenciario/ | modelo-replica-inss.docx | abrir e anonimizar (alerta) |
| (exemplo) 14 | Modelo Inicial Aposentadoria Especial FINAL.docx | _arquivo/ | modelo-inicial-aposentadoria-especial-previdenciario_ate-AAAA-MM-DD.docx | nada |

**Bloco 3. As regras da cópia**, para o advogado seguir:
1. **Copiar, nunca mover.** No Windows, arrastar com Ctrl apertado; no Mac, com Option apertado; ou Copiar e Colar. O original fica onde está até a base estar conferida.
2. Renomear só a cópia, com o nome novo da tabela.
3. Arquivo com alerta: abrir antes, conferir e anonimizar pela tabela de troca padrão. Se tiver dado de cliente e não der para limpar, não copia.
4. Pasta de cliente: não copia nada.
5. Se já existir um arquivo com o mesmo nome no destino, não substitui: me avise e a gente decide.
6. No topo de cada documento copiado (ou numa ficha .md com o mesmo nome, para .docx e .pdf), colar o cabeçalho da montar-base com "Situação: rascunho".

Depois que o advogado disser que copiou, entregue o `INDICE.md` em bloco pronto para copiar, com o caminho `escritorio/04-base/INDICE.md`, e siga para a `montar-base` (passo 3 em diante).
