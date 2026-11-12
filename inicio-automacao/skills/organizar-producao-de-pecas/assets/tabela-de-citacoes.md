# Tabela de citações do caso

Uma por peça. **Fica na pasta do caso, nunca na base.** Nasce na pesquisa (prompt 2), com todos os candidatos em `[CONFERIR]`, e só a pessoa que abriu a fonte oficial muda o status. As linhas "conferida" vão para o campo 12 da ficha de briefing, e é delas, e só delas, que a minuta tira citação (prompt 3). Na revisão (prompt 4), toda citação da minuta é cruzada com esta tabela.

```
TABELA DE CITAÇÕES
Código do caso: [ ] · Peça: [ ] · Tese escolhida: [ ]

# | Tipo (lei, súmula, precedente, doutrina) | Referência | O que sustenta na peça | Trecho conferido na fonte | Link da fonte oficial | Aberta em | Por | Status
1 | | | | | | | | [CONFERIR] / conferida / descartada (motivo)
```

## Regras

- **Status inicial:** toda linha sugerida pela IA começa `[CONFERIR]`, inclusive as de "grau de certeza alto".
- **Conferida:** número, órgão julgador, data e relator conferidos; o trecho entre aspas copiado da fonte aberta na tela; súmula, tema ou enunciado com a redação atual; artigo de lei na redação vigente, na legislação oficial.
- **Descartada:** a fonte não abriu, ou o texto não diz o que a peça precisava. O advogado decide se o argumento é reescrito sem ela. Fica na tabela com o motivo, para ninguém sugerir de novo.
- **Peça antiga e modelo do banco não são fonte.** Servem de pista para a busca.
- **Quem escolhe o que entra na peça:** o advogado, entre as conferidas.
