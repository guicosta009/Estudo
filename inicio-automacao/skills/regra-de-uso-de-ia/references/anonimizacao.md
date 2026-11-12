# Anonimização: tabela de troca, exemplo e cuidados

Leia no passo 7 do modo criar e sempre que o advogado perguntar "como anonimizar". A tabela padrão vai para o Anexo 1 da política. Os cuidados por área e os casos difíceis entram só se o escritório atuar naquela área ou lidar com aquele tipo de documento.

## Princípios

- **Mínimo necessário** (LGPD, Lei 13.709/2018): só o trecho que a tarefa precisa. Se a tarefa é revisar a fundamentação, o relato dos fatos com nomes não precisa ir.
- **Anonimizar antes de colar,** sempre. Mesmo na conta profissional.
- **Dado de saúde** fica só no trecho que a tarefa exige, com cuidado redobrado.
- **Na dúvida, o dado não entra.**

## Tabela de troca padrão

| Dado | Troca por |
|---|---|
| Nome do cliente | `[CLIENTE]` (ou `[CLIENTE 1]`, `[CLIENTE 2]`) |
| Nome de cônjuge, filho, familiar | `[CÔNJUGE 1]`, `[FILHO 1]`, `[FAMILIAR 1]` |
| Nome de empresa | `[EMPRESA]` (ou `[EMPRESA 1]`) |
| CPF, RG, NIT | `[DOC]` |
| Número do processo | `[PROCESSO]` |
| Número do benefício | `[BENEFÍCIO]` |
| Endereço | `[ENDEREÇO]` |
| Telefone e e-mail | `[CONTATO]` |
| Dado de saúde | Fica só o trecho que a tarefa exige |

**Códigos extras sugeridos** (use se o escritório precisar; anote na política quais adotou): `[PARTE CONTRÁRIA]`, `[TESTEMUNHA 1]`, `[TERCEIRO 1]`, `[CONTA]` (conta bancária e cartão), `[ESCOLA]`, `[PLACA]`.

## Exemplo (fictício)

**Antes:**
> Maria Exemplo da Silva, CPF 000.000.000-00, moradora da Rua Fictícia, 100, telefone (00) 00000-0000, teve o auxílio por incapacidade nº 000.000.000-0 negado. O processo 0000000-00.0000.0.00.0000 está na fase de perícia. O laudo do médico assistente descreve depressão grave e afastamento de 8 meses. O ex-marido, João Exemplo, não paga a pensão do filho Pedro, de 7 anos.

**Depois:**
> [CLIENTE], [DOC], moradora de [ENDEREÇO], [CONTATO], teve o benefício [BENEFÍCIO] negado. O processo [PROCESSO] está na fase de perícia. O laudo do médico assistente descreve quadro psiquiátrico com afastamento de 8 meses. *(Dado de saúde mantido só porque a tarefa é preparar quesitos da perícia.)*

**O que mais mudou:**
- A frase sobre o ex-marido e o filho saiu inteira: não serve à tarefa e traz dado de criança.
- O diagnóstico ficou genérico. Se a tarefa exigir o diagnóstico exato, ele entra, e só ele.
- O laudo completo não foi colado. Laudo completo só com autorização expressa do responsável.

## Cuidados por área

| Área | Dado que aparece | Cuidado antes da IA |
|---|---|---|
| Previdenciário | Laudos, atestados, CID, saúde, NIT, renda | Nome, CPF e NIT viram códigos; manter só o que a análise exige; senha gov.br nunca entra |
| Trabalhista | Atestados, assédio, conversas com colegas, salários de terceiros | Anonimizar também os terceiros; o original da conversa fica intacto e fora da IA (é a prova) |
| Família | Crianças e adolescentes, saúde mental, violência, finanças | Proteção reforçada para criança e adolescente; códigos, sem escola e sem endereço; violência fora de qualquer automação |
| Consumidor e Cível | Faturas, extratos, dados bancários, plano de saúde | Tirar conta e cartão; em lote, restringir o acesso à planilha |

## Casos que a tabela não resolve sozinha

- **Terceiros e parte contrária.** Testemunha, empregador, colega de trabalho, ex-cônjuge: também são anonimizados. Dado de quem não é cliente entra no mínimo necessário, com guarda e descarte combinados.
- **Reidentificação pelo contexto.** Sem nome, a pessoa ainda pode ser reconhecida: "a única médica pediatra da cidade", "o acidente na fábrica de tal bairro em tal data". Generalize o que identifica ("profissional da saúde", "município do interior", "no ano passado") quando o detalhe não for necessário à tarefa.
- **PDF escaneado, foto e print.** O nome aparece em cabeçalho, rodapé, carimbo, assinatura, marca d'água e no próprio nome do arquivo. Prefira copiar só o trecho de texto necessário e anonimizar o texto, em vez de subir o arquivo inteiro. Se precisar subir o arquivo, confira página por página e renomeie o arquivo.
- **Print de conversa de WhatsApp.** Nome e foto do contato, número de telefone e mensagens de outras pessoas aparecem junto. Transcreva o trecho e anonimize.
- **A chave de troca.** A correspondência entre `[CLIENTE 1]` e o nome real fica na pasta do cliente, nunca dentro da IA. Quem recoloca os nomes no documento final é uma pessoa, e confere.

## Checklist de anonimização para colocar no POP

Antes de colar qualquer coisa na IA:
- [ ] Estou na conta profissional do escritório.
- [ ] A tarefa precisa mesmo deste trecho? Tirei o que não precisa.
- [ ] Troquei nomes (cliente, familiares, terceiros, parte contrária), documentos, processo, benefício, endereço e contato.
- [ ] Dado de saúde só no trecho que a tarefa exige.
- [ ] Não há laudo completo, dado de criança ou adolescente nem segredo de justiça sem autorização registrada.
- [ ] Não há senha nem credencial.
- [ ] Conferi cabeçalho, rodapé, carimbo e nome do arquivo.
- [ ] O detalhe que sobrou não identifica a pessoa pelo contexto.
