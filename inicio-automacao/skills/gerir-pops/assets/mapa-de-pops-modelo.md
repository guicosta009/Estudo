# Mapa de POPs · [NOME DO ESCRITÓRIO]

Versão: [N] · Atualizado em: [AAAA-MM-DD] · Dono do mapa: [RESPONSÁVEL PELA INOVAÇÃO; NO SOLO, O TITULAR]

Uma linha por POP, inclusive os aposentados. Status: Rascunho · Em teste · Vigente · Em revisão · Aposentado. Degrau: 1 Prompt solto · 2 POP escrito e guardado · 3 Projeto no Claude · 4 Habilidade do POP · 5 Plugin do escritório · 6 Automação. Número de POP nunca é reaproveitado.

| Setor | Código | POP | Dono | Versão | Vigente desde | Próxima revisão | Status | Passos com IA (S/A) | Degrau | Onde está a vigente | Observação |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Produção de peças | POP-PEC-01 | [NOME CURTO] | [NOME] | 0.1 | | após o teste | Rascunho | S: [nº] · A: [nº] | 1 | `03-pops/producao-de-pecas/pop-pec-01-[processo].md` | |
| Atendimento e triagem | POP-ATD-01 | | | | | | | | | | |
| Comercial | POP-COM-01 | | | | | | | | | | |
| Prazos e controladoria | POP-PRZ-01 | | | | | | | | | | |
| Audiências e diligências | POP-AUD-01 | | | | | | | | | | |
| Financeiro e cobrança | POP-FIN-01 | | | | | | | | | | |
| Relacionamento com o cliente | POP-REL-01 | | | | | | | | | | |
| Marketing e conteúdo | POP-MKT-01 | | | | | | | | | | |
| Gestão de equipe | POP-EQP-01 | | | | | | | | | | |
| Administrativo | POP-ADM-01 | | | | | | | | | | |

Apague as linhas de setor que não têm POP nem processo listado, mas mantenha a lista "Setores sem POP" abaixo: ela é o lugar para olhar quando for escolher o próximo setor.

**Onde está a vigente:** o caminho do arquivo, mais o nome do Projeto no Claude e o nome da skill, quando houver. Exemplo: `03-pops/producao-de-pecas/pop-pec-01-peticao-inicial.md` · Projeto "Peças previdenciário" · skill `pop-pec-01-peticao-inicial`.

**Observação:** "publicado sem teste", motivo da aposentadoria e código que substitui, dono provisório, revisão em andamento.

## Setores sem POP

- [SETOR]: [processo que a equipe faz de cabeça, se houver]

## Ordem sugerida para escrever ou revisar

1. [Setor-alvo: POP e ação]
2. [...]

## Regras do mapa

- Uma linha por POP, inclusive os aposentados.
- Quem mantém é o responsável pela inovação (no solo, o titular). O dono do POP avisa a cada mudança.
- Na reunião semanal do núcleo (no solo, no começo do bloco fixo), olhar "Revisão vencida" e "Sem data".
- Mapa e cabeçalho do POP dizem a mesma versão. Se discordarem, vale o que foi aprovado no registro de mudanças, e o outro é corrigido no mesmo dia.

---

## Versão para planilha (`00-mapa-de-pops.tsv`)

Colunas separadas por tabulação. Cole na célula A1 de uma planilha em branco e cada coluna cai no seu lugar. Primeira linha:

```
Setor	Código	POP	Dono	Versão	Vigente desde	Próxima revisão	Status	Passos com IA (S/A)	Degrau	Onde está a vigente	Observação
```

Datas no formato AAAA-MM-DD, para a planilha reconhecer como data. Se a planilha mostrar a data como texto, formate a coluna G como data. Conferir na sua planilha.

## Coluna de alerta (opcional)

Na coluna M, a partir da linha 2, numa planilha em português. A coluna G é a próxima revisão e a coluna H é o status:

```
=SE(H2="Aposentado";"Aposentado";SE(NÃO(ÉNÚM(G2));"Sem data";SE(G2<HOJE();"Revisão vencida";"Em dia")))
```

Texto como "após o teste" na coluna G aparece como "Sem data", de propósito: POP em teste também precisa de uma data para sair do teste. Em planilha configurada em inglês, a mesma fórmula fica com IF, NOT, ISNUMBER e TODAY, e com vírgula no lugar do ponto e vírgula. Conferir na sua planilha.
