Title: Desfazendo um commit que já foi enviado para o repositório
Date: 2016-06-14 14:02:11
Category: Git
Tags: git, github, tutorial
Author: Michell Stuttgart
Summary: Aprenda a desfazer commits que já foram enviados para o repositório remoto de maneira correta, sem corromper o histórico do repositório.

Fala pessoal, tudo bem?

Caro leitor, se você costuma utilizar o *git* como controle de versão e trabalha em um mesmo repositório com vários contribuidores (ou mesmo sozinho), já deve ter se deparado com a situação em que você precisava desfazer um *commit* que já havia sido enviado para repositório. Existem algumas maneiras de corrigir isso, mas de longe, a mais correta é utilizar o comando *revert*, pois o mesmo não altera o histórico de *commits* do repositório e ao mesmo tempo expões de forma clara o que foi corrigido.

O comando `revert` cria um *commit* que desfaz todas as modificações do *commit* que você corrigir. Seu funcionamento é bem simples. Podemos definir o intervalo, a partir do último *commit* (HEAD) que será revertido.

```bash
git revert HEAD~3
```
No exemplo acima, os últimos 3 *commits* serão revertidos, ou seja, o git irá criar um novo *commit* que desfaz as modificações realizadas pelo 3 últimos *commits* da *branch* atual em que você está.

Outro mode de uso consiste em passarmos um intervalo como parâmetro contendo os *commits* que desejamos reverter. Vamos considerar que estamos trabalhando com na *branch* `master`.

```bash
git revert -n master~5..master~2
```
No exemplo acima, vamos reverter o intervalo que vai do quinto *commit* (incluindo o mesmo) mais recente ao terceiro *commit* mais recente. Repare que o intervalor funciona da seguiten forma: `[commit antigo, commit recent[`. O intervalo inclui o *commit* mais antigo e vai até o *commit* mais recente, NÃO incluindo este último.

Outra possibilidade é utilizar a *hash* dos *commits* seja passando uma *hash* unica ou um intervalo. Por exemplo:

```bash
git revert -n f44db377210fad4f1980663f58d4be9fa9c09e36..f167fc86d574a25393d50f11e620a9364cf6257f
```

É isso pessoal. Para saber mais detalhes do commando, basta dar uma olhada na documentação oficial [aqui](https://git-scm.com/docs/git-revert). Qualquer dúvida é só deixar um comentário.

Obrigado por ler e até o próximo *post* pessoal. Até mais!

