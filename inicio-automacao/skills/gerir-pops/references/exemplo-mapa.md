# Exemplo de mapa de POPs preenchido

Leia quando o advogado quiser ver como o mapa fica, ou para calibrar o nível de detalhe na rotina 1. Escritório fictício de Previdenciário e Família com 5 pessoas (2 advogadas, 1 advogado, 1 estagiário, 1 secretária). Nomes, versões e datas são de exemplo. No mapa real, as datas vão no formato AAAA-MM-DD; aqui aparecem como distância de hoje para o exemplo não envelhecer.

## O mapa

| Setor | Código | POP | Dono | Versão | Vigente desde | Próxima revisão | Status | Passos com IA (S/A) | Degrau | Onde está a vigente | Observação |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Produção de peças | POP-PEC-01 | Petição inicial previdenciária | Ana | 1.2 | há 2 meses | daqui a 1 mês | Vigente | S: 1, 7 · A: 2, 4, 5 | 4 | `03-pops/producao-de-pecas/pop-pec-01-peticao-inicial-previdenciaria.md` · Projeto "Peças previdenciário" · skill `pop-pec-01-peticao-inicial` | |
| Produção de peças | POP-PEC-02 | Recurso no juizado | Ana | 0.3 | | após o teste | Em teste | S: 1 · A: 2, 3, 5 | 1 | `03-pops/producao-de-pecas/pop-pec-02-recurso-no-juizado.md` | Teste com a IA em andamento |
| Atendimento e triagem | POP-ATD-01 | Triagem no WhatsApp | Bruno | 1.0 | há 1 mês | daqui a 2 meses | Vigente | S: 2 · A: 3, 4 | 3 | `03-pops/atendimento-e-triagem/pop-atd-01-triagem-no-whatsapp.md` · Projeto "Atendimento" | |
| Relacionamento com o cliente | POP-REL-01 | Andamento no WhatsApp | Bruno | 1.0 | há 5 meses | venceu há 2 semanas | Em revisão | S: 2, 4, 8 · A: 5, 7 | 3 | `03-pops/relacionamento-com-o-cliente/pop-rel-01-andamento-no-whatsapp.md` · Projeto "Relacionamento" | Rascunho da 2.0 em `_em-construcao/` |
| Prazos e controladoria | POP-PRZ-01 | Leitura de publicações | Carla | 2.0 | há 3 meses | daqui a 3 semanas | Vigente | S: 1, 2 · A: 4 | 6 | `03-pops/prazos-e-controladoria/pop-prz-01-leitura-de-publicacoes.md` · Projeto "Prazos" · automação `leitura-de-publicacoes` | |
| Financeiro e cobrança | POP-FIN-01 | Cobrança de honorários | Titular | 0.1 | | | Rascunho | | 1 | `03-pops/financeiro-e-cobranca/pop-fin-01-cobranca-de-honorarios.md` | |
| Administrativo | POP-ADM-01 | Nome dos PDFs digitalizados | Carla | 1.1 | | | Aposentado | | | `_arquivo/pop-adm-01-nome-dos-pdfs-digitalizados-v1-1.md` | Absorvido pelo POP-ADM-02 |
| Administrativo | POP-ADM-02 | Arquivo digital do cliente | Carla | 1.0 | há 6 semanas | daqui a 6 semanas | Vigente | S: 1, 2, 3 · A: 5 | 2 | `03-pops/administrativo/pop-adm-02-arquivo-digital-do-cliente.md` | Ainda fora do Projeto |

**Setores sem POP:** Comercial (proposta de honorários feita de cabeça pela titular), Audiências e diligências, Marketing e conteúdo, Gestão de equipe.

**Ordem sugerida:** terminar a 2.0 do POP-REL-01 (setor-alvo); tirar o POP-PEC-02 do teste; escrever a proposta de honorários (Comercial).

O POP-ADM-01 foi absorvido pelo POP-ADM-02. A linha continua no mapa com o motivo, para ninguém recriar a mesma coisa daqui a um ano. O número 01 de Administrativo não volta a ser usado.

## A leitura que a rotina 6 faria deste mapa

**Alertas:**
- POP-REL-01: revisão vencida e status Em revisão. A 1.0 continua valendo até a 2.0 ser aprovada. Conferir há quanto tempo o rascunho está parado.
- POP-FIN-01: rascunho sem data de revisão e com a titular como dona. Combinar uma data para sair do rascunho.
- Carla é dona de dois POPs vigentes e Ana de um vigente e um em teste. Sem sobrecarga por enquanto.
- POP-ADM-02 vigente fora do Projeto. Causa de POP que morre: "mora longe do trabalho".

**A escada:**

| POP | Degrau | Próximo passo | Skill |
|---|---|---|---|
| POP-ADM-02 | 2 | Subir para o Projeto do setor, com o padrão de nomes e pastas da base | `montar-base` |
| POP-ATD-01 | 3 | Checklist de prontidão e instrução por passo para os passos 2, 3 e 4 | `desenhar-automacao`, depois `pop-para-skill` |
| POP-REL-01 | 3 | Fechar a revisão antes de subir de degrau | rotina 4, depois `testar-pop` |
| POP-PEC-01 | 4 | Medir a skill contra a linha de base antes de pensar em disparo por gatilho | `medir-retorno` |
| POP-PRZ-01 | 6 | Manter as revisões e o painel do mês | `revisao-periodica`, `medir-retorno` |

**Recomendação (no máximo duas):** fechar a revisão do POP-REL-01, que é o setor-alvo; e colocar o POP-ADM-02 no Projeto.

## O mesmo mapa em formato de planilha

Primeiras linhas do `00-mapa-de-pops.tsv` (colunas separadas por tabulação; no arquivo real, datas no formato AAAA-MM-DD):

```
Setor	Código	POP	Dono	Versão	Vigente desde	Próxima revisão	Status	Passos com IA (S/A)	Degrau	Onde está a vigente	Observação
Produção de peças	POP-PEC-01	Petição inicial previdenciária	Ana	1.2	[AAAA-MM-DD]	[AAAA-MM-DD]	Vigente	S: 1, 7 · A: 2, 4, 5	4	03-pops/producao-de-pecas/pop-pec-01-peticao-inicial-previdenciaria.md · Projeto Peças previdenciário · skill pop-pec-01-peticao-inicial	
Produção de peças	POP-PEC-02	Recurso no juizado	Ana	0.3		após o teste	Em teste	S: 1 · A: 2, 3, 5	1	03-pops/producao-de-pecas/pop-pec-02-recurso-no-juizado.md	Teste com a IA em andamento
```
