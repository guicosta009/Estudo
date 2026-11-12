## Registro de revisão e aprovação

(Este bloco vai no fim do POP, depois de "Controle de versões" (Versão, Data, O que mudou, Por quê, Quem aprovou, Equipe avisada ou treinada em). Mostra quem olhou, quando e com qual decisão.)

POP: POP-[SIGLA]-[NN] [NOME DO PROCESSO] · Versão revisada: [0.3] · Dono do POP: [NOME]
Status do POP: [EM TESTE] · Etapa da esteira: [CHECKLIST / TESTE DE MESA / TESTE COM A IA / APROVADO PARA O PILOTO / EM PILOTO / APROVADO PARA USO / DEVOLVIDO]

### Testes feitos

- Checklist de qualidade: [AAAA-MM-DD] · resultado [PRONTO PARA O TESTE DE MESA] · `testes/checklist-[sigla]-[nn]-AAAA-MM-DD.md`
- Teste de mesa: [AAAA-MM-DD] · executor [FUNÇÃO] · resultado [APROVADO / AJUSTAR E REPETIR] · `testes/teste-de-mesa-[sigla]-[nn]-AAAA-MM-DD.md`
- Teste com a IA: [AAAA-MM-DD] · casos fácil, comum e difícil · fichas em `testes/teste-com-ia-[sigla]-[nn]-AAAA-MM-DD.md`
- Etapa pulada e motivo (também em "Etapas puladas" do `perfil.md`): [NENHUMA / QUAL]

### Revisão por par

Revisor: [NOME OU FUNÇÃO; no solo, "colega de outro escritório" ou "IA como revisora, decisão do titular"] · Data: [AAAA-MM-DD]
- Eu executaria isso numa segunda-feira cheia, sem perguntar? [...]
- O que este POP recebe do setor anterior bate com o que aquele setor entrega? [...]
- Algum passo depende de uma pessoa específica que pode faltar? [...]
- As fichas mostram teste com caso difícil? [...]
- Tem passo que a gente faz e o POP não mostra? [...]

Pontos levantados: [LISTA] · Resolvidos na versão: [0.x] · Pendentes: [LISTA OU "NENHUM"]

### Revisão do titular

Titular: [NOME] · Data: [AAAA-MM-DD] (no solo, em outro dia, com o checklist na mão)
- Passos H conferidos (decisão, julgamento ético, conversa delicada, assinatura): [SIM/NÃO]
- "Nunca sai sem revisão humana" cobre prazo, notícia de decisão, valor e citação: [SIM/NÃO]
- Caminho do dado de cliente (conta profissional, anonimização, sigilo profissional, LGPD Lei 13.709/2018): [SIM/NÃO]
- Tom com o cliente segue o código do escritório; se algo é público, respeita o Provimento 205/2021 do CFOAB [CONFERIR]: [SIM/NÃO/NÃO SE APLICA]
- Relatório da `auditar-riscos` lido: [SIM, NOTA X / NÃO EXISTE]
- Eu assinaria o que sair deste POP sem ter visto cada execução? Resposta por escrito: [...]

Decisão: [APROVADO PARA O PILOTO / APROVADO COM RESSALVAS / DEVOLVIDO] · Ressalvas: [...]

### Fechamento do piloto

Data: [AAAA-MM-DD] · Arquivo: `testes/piloto-[sigla]-[nn].md`
- Revisão por par no fechamento: [NOME, PONTOS]
- Passos aprovados para seguir à automação: [NÚMEROS]
- Passos que subiram de sigla, e por quê: [...]
- Erros que chegaram ao cliente ou ao tribunal: [0 / QUAIS, CAUSA CORRIGIDA E TESTADA EM AAAA-MM-DD]

### Aprovação para uso

Titular: [NOME] · Data: [AAAA-MM-DD] · Versão aprovada: [1.0 NO POP NOVO; 1.x OU 2.0 NA REVISÃO DE UM POP VIGENTE]
Próxima revisão do POP: [MARCO RELATIVO, POR EXEMPLO "NA REVISÃO TRIMESTRAL" OU "DEPOIS DE 4 SEMANAS DE USO"]
Publicar como Vigente, avisar ou treinar a equipe e atualizar o mapa de POPs: `gerir-pops` · [FEITO EM AAAA-MM-DD / PENDENTE]
