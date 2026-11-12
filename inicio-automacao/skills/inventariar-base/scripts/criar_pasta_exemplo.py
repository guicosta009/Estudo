#!/usr/bin/env python3
"""Cria a pasta de exemplo bagunçada usada para demonstrar a inventariar-base.

Os nomes dos arquivos imitam uma pasta real de escritório (espaço, acento, "FINAL2",
"(1)", arquivo temporário do Word) e por isso não podem viajar dentro do plugin.
Este script monta a pasta na hora, com as mesmas datas antigas simuladas.
Todos os nomes, números e conteúdos são fictícios.

Uso:
  python3 criar_pasta_exemplo.py <destino>
Cria <destino>/pasta-baguncada/ e <destino>/03-pops/ (um POP fictício para o cruzamento).
Depois:
  python3 inventariar_pasta.py <destino>/pasta-baguncada --saida <destino>/saida \\
    --pops <destino>/03-pops --setor-alvo "Relacionamento com o cliente"
"""
import base64
import json
import os
import sys
from pathlib import Path

ARQUIVOS = json.loads(r"""[
{
"p": "pasta-baguncada/Clientes/Maria Souza - processo 1234567-89.2023.8.26.0100/procuracao assinada.pdf",
"m": 1685624400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHBhc3RhIGRlIGNhc28gZmljdMOtY2lhCg=="
},
{
"p": "pasta-baguncada/Clientes/Maria Souza - processo 1234567-89.2023.8.26.0100/rg.pdf",
"m": 1685624400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHBhc3RhIGRlIGNhc28gZmljdMOtY2lhCg=="
},
{
"p": "pasta-baguncada/Contestacao trabalhista padrao novo.docx",
"m": 1744117200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGNvbnRlc3Rhw6fDo28gbm92YQo="
},
{
"p": "pasta-baguncada/Contesta\u00e7\u00e3o trabalhista padr\u00e3o N\u00c3O USAR.docx",
"m": 1581339600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGNvbnRlc3Rhw6fDo28gYW50aWdhCg=="
},
{
"p": "pasta-baguncada/C\u00f3pia de checklist documentos aux\u00edlio doen\u00e7a.docx",
"m": 1759237200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGxpc3RhIGRlIGRvY3VtZW50b3MgcGFyYSBhdXjDrWxpbyBwb3IgaW5jYXBhY2lkYWRlCg=="
},
{
"p": "pasta-baguncada/Modelo Inicial Aposentadoria Especial FINAL.docx",
"m": 1615813200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBpbmljaWFsLCBwcmltZWlyYSB2ZXJzw6NvCg=="
},
{
"p": "pasta-baguncada/Modelo Inicial Aposentadoria Especial FINAL2.docx",
"m": 1659445200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBpbmljaWFsLCBzZWd1bmRhIHZlcnPDo28K"
},
{
"p": "pasta-baguncada/Modelo Inicial Aposentadoria Especial v3 revisado (1).docx",
"m": 1718974800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBpbmljaWFsLCB0ZXJjZWlyYSB2ZXJzw6NvCg=="
},
{
"p": "pasta-baguncada/Modelo Inicial Aposentadoria Especial v3 revisado.docx",
"m": 1718888400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBpbmljaWFsLCB0ZXJjZWlyYSB2ZXJzw6NvCg=="
},
{
"p": "pasta-baguncada/POP peticao inicial FINAL_revisado2.docx",
"m": 1681218000,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHBhc3NvIGEgcGFzc28gYW50aWdvIGRhIHBldGnDp8OjbyBpbmljaWFsCg=="
},
{
"p": "pasta-baguncada/Pedro Almeida x Banco Ficticio/inicial pedro.docx",
"m": 1710248400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHBhc3RhIGRlIGNhc28gZmljdMOtY2lhCg=="
},
{
"p": "pasta-baguncada/Peticoes antigas/embargos declaracao modelo.docx",
"m": 1633352400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBlbWJhcmdvcwo="
},
{
"p": "pasta-baguncada/Peticoes antigas/replica INSS 2019.docx",
"m": 1566219600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHLDqXBsaWNhIGFudGlnYQo="
},
{
"p": "pasta-baguncada/Recurso inominado consumidor.docx",
"m": 1728565200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHJlY3Vyc28gdXNhZG8gbnVtIGNhc28K"
},
{
"p": "pasta-baguncada/R\u00e9plica Ana Lima processo 0001234-56.2022.5.02.0001.docx",
"m": 1664456400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHLDqXBsaWNhIGRlIHVtIGNhc28sIGNvbSBub21lIGUgbsO6bWVybyBmaWN0w61jaW9zCg=="
},
{
"p": "pasta-baguncada/Thumbs.db",
"m": 1718974800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGFycXVpdm8gZGUgc2lzdGVtYQo="
},
{
"p": "pasta-baguncada/ata reuniao equipe.txt",
"m": 1776171600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGFub3Rhw6fDtWVzIGRlIHJldW5pw6NvCg=="
},
{
"p": "pasta-baguncada/checklist audiencia trabalhista.md",
"m": 1750078800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG8gcXVlIGxldmFyIHBhcmEgYSBhdWRpw6puY2lhCg=="
},
{
"p": "pasta-baguncada/checklist documentos aux\u00edlio doen\u00e7a.docx",
"m": 1757682000,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGxpc3RhIGRlIGRvY3VtZW50b3MgcGFyYSBhdXjDrWxpbyBwb3IgaW5jYXBhY2lkYWRlCg=="
},
{
"p": "pasta-baguncada/contrato honorarios antigo.docx",
"m": 1556888400,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGNvbnRyYXRvIGFudGlnbwo="
},
{
"p": "pasta-baguncada/criterios relevancia movimentacao prev.txt",
"m": 1759323600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG8gcXVlIGF2aXNhciBhbyBjbGllbnRlIGUgbyBxdWUgc8OzIHJlZ2lzdHJhcgo="
},
{
"p": "pasta-baguncada/extrato bancario cliente 0231.pdf",
"m": 1741006800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHNpbXVsYSB1bSBleHRyYXRvIGRlIGNhc28K"
},
{
"p": "pasta-baguncada/holerite_marco_2023.pdf",
"m": 1680699600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHNpbXVsYSB1bSBob2xlcml0ZSBkZSBjYXNvCg=="
},
{
"p": "pasta-baguncada/laudo pericial joao silva.pdf",
"m": 1706878800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHNpbXVsYSB1bSBsYXVkbyBkZSBjYXNvCg=="
},
{
"p": "pasta-baguncada/manual do estagiario.docx",
"m": 1645534800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG9yaWVudGHDp8O1ZXMgcGFyYSBxdWVtIGNoZWdhCg=="
},
{
"p": "pasta-baguncada/mensagens prontas whatsapp andamento.txt",
"m": 1771074000,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHRleHRvcyBkZSBhbmRhbWVudG8gcGFyYSBvIGNsaWVudGUK"
},
{
"p": "pasta-baguncada/padrao nomes de arquivos.txt",
"m": 1725886800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGNvbW8gbm9tZWFyIGFycXVpdm9zIGRlIGNsaWVudGUK"
},
{
"p": "pasta-baguncada/post instagram ideias.txt",
"m": 1772542800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGlkZWlhcyBzb2x0YXMgZGUgcG9zdAo="
},
{
"p": "pasta-baguncada/proposta honorarios modelo.docx",
"m": 1751893200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBwcm9wb3N0YQo="
},
{
"p": "pasta-baguncada/quesitos pericia medica modelo.docx",
"m": 1746450000,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IG1vZGVsbyBkZSBxdWVzaXRvcwo="
},
{
"p": "pasta-baguncada/regua cobranca.txt",
"m": 1760965200,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHNlcXXDqm5jaWEgZGUgbGVtYnJldGVzIGRlIGNvYnJhbsOnYQo="
},
{
"p": "pasta-baguncada/roteiro triagem familia.md",
"m": 1768050000,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IHBlcmd1bnRhcyBkYSB0cmlhZ2VtIGRlIGZhbcOtbGlhCg=="
},
{
"p": "pasta-baguncada/tabela honorarios 2023.xlsx",
"m": 1674219600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGZhaXhhcyBkZSBob25vcsOhcmlvcyBkbyBhbm8gYW50ZXJpb3IK"
},
{
"p": "pasta-baguncada/tabela honorarios 2024 atualizada.xlsx",
"m": 1706187600,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGZhaXhhcyBkZSBob25vcsOhcmlvcyBhdHVhbGl6YWRhcwo="
},
{
"p": "pasta-baguncada/~$delo Inicial Aposentadoria Especial FINAL.docx",
"m": 1718974800,
"b": "QXJxdWl2byBmaWN0w61jaW8gZG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBTZW0gZGFkbyByZWFsLiBDb250ZcO6ZG8gc2ltdWxhZG86IGFycXVpdm8gdGVtcG9yw6FyaW8gZG8gZWRpdG9yCg=="
},
{
"p": "03-pops/relacionamento-com-o-cliente/pop-rel-01-andamento-no-whatsapp.md",
"m": 1794230126,
"b": "IyBQT1AtUkVMLTAxIEFuZGFtZW50byBubyBXaGF0c0FwcAoKU2V0b3I6IFJlbGFjaW9uYW1lbnRvIGNvbSBvIGNsaWVudGUgwrcgw4FyZWE6IFByZXZpZGVuY2nDoXJpbyDCtyBWZXJzw6NvOiAwLjIgwrcgQXR1YWxpemFkbyBlbTogQUFBQS1NTS1ERCDCtyBEb25vIGRvIFBPUDogQXNzaXN0ZW50ZSDCtyBTdGF0dXM6IEVtIHRlc3RlIMK3IFByw7N4aW1hIHJldmlzw6NvOiBbQSBERUZJTklSXQoKPiBQT1AgZmljdMOtY2lvIGUgcmVzdW1pZG8sIHPDsyBwYXJhIG8gZXhlbXBsbyBkYSBza2lsbCBpbnZlbnRhcmlhci1iYXNlLiBNb3N0cmEgbyBjcnV6YW1lbnRvIGVudHJlIG8gcXVlIG8gUE9QIHBlZGUgZSBvIHF1ZSBleGlzdGUgbmEgcGFzdGEgZGUgbW9kZWxvcy4KCiMjIDEuIE9iamV0aXZvCgpBdmlzYXIgbyBjbGllbnRlIGRhcyBtb3ZpbWVudGHDp8O1ZXMgcmVsZXZhbnRlcyBkbyBwcm9jZXNzbyBlIG1hbmRhciBvIHJlc3VtbyBtZW5zYWwsIG5vIHRvbSBkbyBlc2NyaXTDs3Jpby4KCiMjIDQuIEVudHJhZGFzCgotIE1vdmltZW50YcOnw7VlcyBkbyBkaWEgwrcgc2lzdGVtYSBkZSBhY29tcGFuaGFtZW50bwotIENyaXTDqXJpb3MgZGUgcmVsZXbDom5jaWEgZGUgbW92aW1lbnRhw6fDo28gwrcgcGFzdGEgZGUgbW9kZWxvcwotIE1vZGVsb3MgZGUgbWVuc2FnZW0gcG9yIGNhdGVnb3JpYSDCtyBwYXN0YSBkZSBtb2RlbG9zCi0gUGVyZ3VudGFzIGZyZXF1ZW50ZXMgZGUgY2xpZW50ZXMgwrcgY2FiZcOnYSBkYSBhc3Npc3RlbnRlCgojIyA1LiBQYXNzbyBhIHBhc3NvIGNvbSBTLCBBIGUgSAoKMS4gW1NdIENvbmZlcmlyIGFzIG1vdmltZW50YcOnw7VlcyBkbyBkaWEuIEV4ZWN1dGE6IElBLiBDb25mZXJlOiBBc3Npc3RlbnRlLCBwb3IgYW1vc3RyYS4KMi4gW1NdIENsYXNzaWZpY2FyIGVtIHJvdGluYSBvdSByZWxldmFudGUgcGVsb3MgY3JpdMOpcmlvcyBlc2NyaXRvcy4gRXhlY3V0YTogSUEuIENvbmZlcmU6IEFzc2lzdGVudGUsIGFzIHJlbGV2YW50ZXMuCjMuIFtBXSBFc2NyZXZlciBhIG1lbnNhZ2VtIGRvIHJlbGV2YW50ZSBhIHBhcnRpciBkbyBtb2RlbG8gYXByb3ZhZG8uIEV4ZWN1dGE6IElBLiBDb25mZXJlOiBBc3Npc3RlbnRlLCB0b20gZSBkYWRvcy4KNC4gW0FdIEV4cGxpY2FyIG8gdGVybW8gcHJvY2Vzc3VhbCBlbSBsaW5ndWFnZW0gc2ltcGxlcy4gRXhlY3V0YTogSUEuIENvbmZlcmU6IEFkdm9nYWRhLgo1LiBbQV0gUmVzcG9uZGVyIGEgZMO6dmlkYSBkbyBjbGllbnRlIGEgcGFydGlyIGRhcyByZXNwb3N0YXMgYXByb3ZhZGFzLiBFeGVjdXRhOiBJQS4gQ29uZmVyZTogQXNzaXN0ZW50ZS4KNi4gW1NdIFBlZGlyIGRvY3VtZW50byBwZW5kZW50ZSBwZWxhIGxpc3RhIGRlIGRvY3VtZW50b3MuIEV4ZWN1dGE6IElBLiBDb25mZXJlOiBBc3Npc3RlbnRlLCBwb3IgYW1vc3RyYS4KNy4gW0hdIERhciBub3TDrWNpYSBkZXNmYXZvcsOhdmVsIHBvciBsaWdhw6fDo28uIEV4ZWN1dGE6IEFkdm9nYWRhLiBDb25mZXJlOiBuw6NvIHNlIGFwbGljYS4KCiMjIE8gcXVlIGEgSUEgdmFpIHByZWNpc2FyIGNvbnN1bHRhcgoKfCBJdGVtIChtb2RlbG8sIGNoZWNrbGlzdCwgY3JpdMOpcmlvKSB8IFBhc3NvIHF1ZSB1c2EgfCBFeGlzdGUgcG9yIGVzY3JpdG8/IChzaW0sIGVtIHBhcnRlLCBuw6NvKSB8IE9uZGUgZXN0w6EgaG9qZSB8IERvbm8gfAp8LS0tfC0tLXwtLS18LS0tfC0tLXwKfCBDcml0w6lyaW9zIGRlIHJlbGV2w6JuY2lhIGRlIG1vdmltZW50YcOnw6NvIChwcmV2aWRlbmNpw6FyaW8pIHwgMiB8IGVtIHBhcnRlIHwgcGFzdGEgZGUgbW9kZWxvcyB8IEFkdm9nYWRhIHwKfCBNb2RlbG9zIGRlIG1lbnNhZ2VtIHBvciBjYXRlZ29yaWEgfCAzIHwgc2ltIHwgcGFzdGEgZGUgbW9kZWxvcyB8IEFzc2lzdGVudGUgfAp8IEdsb3Nzw6FyaW8gZGUgdGVybW9zIHByb2Nlc3N1YWlzIGVtIGxpbmd1YWdlbSBzaW1wbGVzIHwgNCB8IG7Do28gfCB8IEFkdm9nYWRhIHwKfCBQZXJndW50YXMgZnJlcXVlbnRlcyBkZSBjbGllbnRlcyB8IDUgfCBuw6NvIHwgY2FiZcOnYSBkYSBhc3Npc3RlbnRlIHwgQXNzaXN0ZW50ZSB8CnwgQ2hlY2tsaXN0IGRlIGRvY3VtZW50b3MgcG9yIGJlbmVmw61jaW8gfCA2IHwgc2ltIHwgcGFzdGEgZGUgbW9kZWxvcyB8IEFzc2lzdGVudGUgfAo="
}
]""")


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) == 2 else 1)
    destino = Path(sys.argv[1]).expanduser().resolve()
    criados = 0
    for item in ARQUIVOS:
        alvo = destino / item["p"]
        if alvo.exists():
            continue
        alvo.parent.mkdir(parents=True, exist_ok=True)
        alvo.write_bytes(base64.b64decode(item["b"]))
        os.utime(alvo, (item["m"], item["m"]))
        criados += 1
    print(f"Pasta de exemplo em {destino}: {criados} arquivos criados, {len(ARQUIVOS) - criados} já existiam.")


if __name__ == "__main__":
    main()
