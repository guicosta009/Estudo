# Plano para erro · [NOME DA AUTOMAÇÃO]
Versão: 1.0 · Revisado em: AAAA-MM-DD · Dono: [RESPONSÁVEL PELA AUTOMAÇÃO]

> Uma página. Escrito antes de a automação rodar, para ninguém improvisar no dia do erro. Quem avisa um erro nunca é punido por avisar.

## 1. Como a gente percebe o erro
[Exemplo: a revisão pega uma classificação errada; o cliente responde estranhando a mensagem; a conferência da semana acha divergência no registro de uso.]

## 2. Quem pausa a automação e como
- Quem pode pausar: [FUNÇÃO OU NOME]
- Como pausar: [Exemplo: avisa no canal interno e para de acionar a skill; se houver gatilho agendado, desliga o gatilho; a fila fica parada sem envio.]

## 3. Se chegou ao cliente ou ao processo, quem avisa e por qual canal
[De preferência o advogado responsável, por ligação. Nunca uma mensagem automática.]

## 4. Como corrigir o que já saiu
[Exemplo: mensagem de correção revisada pelo advogado; nova petição; ajuste no sistema.]

## 5. O que muda para não repetir
[POP, base, instrução ou ponto de revisão. Diga qual arquivo muda e quem muda.]

## 6. Onde fica registrado
`06-medicao/incidentes.md`, como incidente (o dado saiu ou o erro chegou ao cliente ou ao processo) ou quase incidente (a revisão pegou antes). Também uma linha no `registro-de-uso.md`.

## 7. Quando volta a rodar e quem autoriza
- Volta quando: [Exemplo: o ajuste foi feito e todos os casos de teste rodaram de novo sem erro.]
- Quem autoriza: [RESPONSÁVEL PELA AUTOMAÇÃO; em erro que chegou ao cliente, também o advogado responsável]

## Na ausência do responsável (obrigatório na trilha solo)
- Ausências previstas: férias, audiência, doença, viagem.
- Quem pausa no lugar: [A DEFINIR] (A pessoa de apoio pode pausar, nunca decidir)
- O que espera na fila sem sair: [tudo o que vai ao cliente ou ao processo]
- Quem revisa no lugar, se alguém revisar: [A DEFINIR] (Exemplo: advogado parceiro com acordo de sigilo)
- O que é urgente e vai por ligação ao titular ou ao substituto: [prazo correndo, notícia muito ruim, cliente em crise]
- Durante a ausência, a automação: [para | volta ao nível 3, só rascunhando]

## Fadiga de revisão
- Blocos fixos de revisão no dia: [A DEFINIR]
- Limite de itens por bloco: [A DEFINIR]
- Fila acima do limite: diminui o volume da automação, nunca a revisão.
