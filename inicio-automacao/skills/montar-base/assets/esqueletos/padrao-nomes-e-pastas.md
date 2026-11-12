# Padrão de nomes e pastas
Versão: 0.1 · Revisado em: AAAA-MM-DD · Dono: [FUNÇÃO OU NOME] · Situação: rascunho
Setor: Administrativo · Área: todas · Usado por: pop-recebimento-de-documentos (renomear e arquivar) · Acesso: geral

> Como todo arquivo do escritório se chama e onde ele mora. Com o padrão escrito, renomear e arquivar viram passo S. Sem ele, cada pessoa inventa o seu.

## Nome de arquivo de cliente

Formato de exemplo: `AAAA-MM-DD_TIPO_codigodocliente.ext`
- Data: a do documento (ou a do recebimento, se o documento não tiver data). [A DEFINIR] (qual das duas)
- TIPO: sigla em maiúsculas da lista abaixo.
- Código do cliente: o código interno, nunca o nome nem o CPF.
- Exemplo: `2025-03-07_CNIS_cliente0231.pdf`

## Siglas de tipo

| Sigla | Documento |
|---|---|
| (exemplo) CNIS | Extrato do CNIS |
| (exemplo) CTPS | Carteira de trabalho |
| (exemplo) PROC | Procuração |
| [A DEFINIR] | |

## Pastas

```
clientes/
  cliente0231/
    00-entrada/        ← o que chegou e ainda não foi conferido
    01-documentos/
    02-pecas/
    03-comunicacoes/
    restrito/          ← laudo, documento de criança ou adolescente, criminal
```
(Estrutura de exemplo. [A DEFINIR] a do escritório.)

## Regras

- Nada fica só no WhatsApp: o documento vai para a pasta de entrada no mesmo dia.
- Documento no celular pessoal da equipe: transferir ao canal oficial e apagar do celular.
- Sem "final", "v2", "novo" no nome. Versão de peça vai no controle de versões do escritório: [A DEFINIR].
- Descarte de original ou cópia só com autorização do advogado.
- Suspeita de adulteração: para tudo e vai ao advogado.

## Mudanças
- 0.1 · AAAA-MM-DD · rascunho criado na montar-base
