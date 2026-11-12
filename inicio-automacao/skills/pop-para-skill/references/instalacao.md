# Instalar, testar e distribuir a skill gerada

Leia no passo 10 da `pop-para-skill`. Os ambientes do Claude mudam com frequência e cada plano libera recursos diferentes. Por isso, este roteiro diz o que fazer e onde procurar, sem prometer nome de menu: **conferir na sua versão do Claude e na configuração da conta.**

## 1. Antes de instalar

- O checklist antes de liberar (seção 7 da skill) está todo marcado.
- A fonte da skill está em `escritorio/05-automacoes/<nome>/skill/<nome-da-skill>/`, com o `SKILL.md` na raiz dessa pasta.
- A conta onde a skill vai rodar é a conta profissional ou de equipe do escritório, com o tratamento de dados conferido.
- Se a skill está no modo empacotado, a pasta `references/` tem as cópias dos documentos da base na versão do índice.

## 2. Onde instalar

### Claude Code
O Claude Code lê skills de pastas no computador. Há dois lugares comuns (`[CONFERIR]` na documentação da sua versão):
- **Pasta de skills do usuário** (em geral `~/.claude/skills/<nome-da-skill>/`): a skill vale em qualquer pasta que a pessoa abrir naquele computador. Boa para o titular na trilha solo.
- **Pasta de skills do projeto** (em geral `.claude/skills/<nome-da-skill>/`, dentro da pasta de trabalho): a skill vale para quem abrir aquela pasta. Boa para a equipe que trabalha numa pasta compartilhada do escritório, porque todos usam o mesmo arquivo.

Copie a pasta inteira da skill (não só o `SKILL.md`) para um desses lugares. No modo pasta, abra o Claude Code na pasta de trabalho que contém `escritorio/`, para a skill achar a base.

### App do Claude (web ou desktop)
Com a execução de código ativada, a skill é enviada compactada pelo menu de habilidades da conta (os nomes dos menus mudam com as atualizações):
1. Compacte a pasta da skill num arquivo .zip com a pasta no topo: `nome-da-skill.zip` contém `nome-da-skill/SKILL.md`. Um `SKILL.md` solto na raiz do zip não é reconhecido. O nome da pasta é igual ao `name` do frontmatter.
2. Confira o frontmatter: `name` com letras minúsculas, números e hífens, até 64 caracteres; `description` com até 1.024 caracteres; nenhuma chave fora das aceitas (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), porque chave desconhecida faz o envio falhar.
3. Envie em Personalizar (Customize) > Habilidades (Skills) > + > Criar habilidade > Enviar uma habilidade, e deixe a skill ativada.
4. Em conta de equipe, o recurso pode depender de liberação do administrador. A skill enviada fica só na conta de quem enviou: cada pessoa da equipe envia a mesma versão na própria conta, ou o escritório reúne as skills num plugin.

No app, a skill não enxerga a pasta `escritorio/` do computador. Use o modo empacotado, ou deixe os documentos da base no Projeto onde a skill vai ser usada.

### Outros ambientes
Outros ambientes do Claude que leem skills ou pastas de trabalho seguem a mesma lógica: a pasta da skill inteira, com o `SKILL.md` na raiz. Conferir na documentação do ambiente.

## 3. Testar depois de instalar

1. Peça o trabalho com uma das frases da `description` ("vê o andamento de hoje", por exemplo). A skill deve ser reconhecida e mostrar a linha de versão. Se não for reconhecida, reveja a `description`: ela precisa das frases que a equipe usa de verdade.
2. Rode o caso de teste típico (`caso-01.md`) e confira contra o gabarito.
3. Rode o caso que deve parar. A skill precisa parar e indicar a pessoa.
4. Confira se ela parou em todos os passos A e não executou nenhum passo H.
5. Anote na `ficha.md`: data, ambiente, quem instalou, versão, resultado do teste.

Se qualquer um falhar, desinstale e volte à `pop-para-skill` (ou à `desenhar-automacao`, se o problema estiver na instrução).

## 4. Trilha solo: instalação individual

- Instale na conta do titular, na pasta de skills do usuário (Claude Code) ou nas configurações de skills da conta (app).
- A fonte única continua em `escritorio/05-automacoes/<nome>/skill/`. O instalado é cópia.
- A cada nova versão: desinstale a anterior, instale a nova e rode o caso de teste típico.
- Se houver estagiário ou secretária usando a skill, a conta dele também precisa ser a do escritório, e ele assina o acordo de uso de IA antes.

## 5. Trilha equipe: o mesmo arquivo para todos, com versão controlada

- **Um responsável publica.** Só o responsável pela automação gera e libera versão nova. Ajuste pedido por alguém da equipe vai para ele, nunca direto na cópia instalada.
- **O mesmo arquivo para todos.** No Claude Code, o melhor caminho é a pasta de skills do projeto, numa pasta compartilhada do escritório. No app, o responsável distribui o mesmo .zip, ou o administrador da conta de equipe publica para todos, se a conta permitir `[CONFERIR]`.
- **Versão visível.** A skill mostra a linha de versão no começo de cada execução. Quem revisa confere se é a versão vigente.
- **Lista de instalação** na `ficha.md`:

| Pessoa (função) | Ambiente | Versão instalada | Data | Acordo de uso assinado? |
|---|---|---|---|---|

- **Troca de versão no mesmo dia para todos.** Versão antiga desinstalada quando a nova entra. Durante a troca, quem não atualizou não usa.
- **Acesso a pastas restritas.** Skill que toca caso restrito (Família com criança, saúde) só é instalada para quem trabalha nesses casos.

## 6. Gatilhos do nível 4

A skill de nível 4 é a mesma skill, com a seção de disparo. Como ela é disparada depende do ambiente:
- **Tarefa agendada:** se o seu ambiente do Claude permite agendar uma tarefa recorrente, configure para pedir o trabalho no horário da ficha (`[CONFERIR]` na sua versão e na configuração da conta). A tarefa só dispara a skill. Revisão e envio continuam nos pontos fixos.
- **Pedido recorrente:** sem agendamento, alguém faz o pedido sempre igual, no mesmo horário ("rodar o andamento do dia"). Funciona bem e é o caminho mais simples para começar.
- **Ponte com outra ferramenta:** se o escritório ligar uma ferramenta de automação (n8n, Zapier, Make ou outra), ela só leva a entrada e traz a saída descritas na ponte documentada da skill. A escolha e a configuração da ferramenta passam pela regra de uso de IA antes.

Em qualquer caso: nada sai do escritório sem a marca de aprovação de uma pessoa.

## 7. Desinstalar ou pausar

- **Pausar:** pelo plano para erro. Quem pode pausar para de acionar a skill e, se houver gatilho, desliga o gatilho. A fila fica parada, sem envio.
- **Desinstalar:** remova a pasta da skill do lugar onde foi instalada, ou tire a skill nas configurações da conta. Anote na `ficha.md`.
- A fonte em `escritorio/05-automacoes/<nome>/skill/` nunca é apagada junto: ela é o histórico da automação.
