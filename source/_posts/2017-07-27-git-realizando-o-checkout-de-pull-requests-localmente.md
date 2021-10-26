---
layout: post
title: "Como realizar o checkout de um Pull Requests localmente"
date: 2017-07-27 19:44:30
main-class: 'git'
tags:
- git
- github
categories: Git
introduction: "Aprenda a recuperar o conteúdo de um Pull Request."
---


## Motivação

Uma situação muito comum quando mantemos um projeto  *opensource*, é que outros desenvolvedores façam um *fork* do nosso repositório e com o tempo submetam melhorias ou correções de *bugs* para nosso repositório através de um *Pull Request*.

Algumas vezes, torna-se interessante realizarmos um *checkout* do *Pull Request* localmente, em nossa máquina. Isso pode ser útil nas seguintes situações (tomando como base minha modesta experiência com projetos *opensource* ):

* Desejamos testar as novas funcionalidades presentes no *Pull Request*, ou em caso de correções de *bugs*, queremos validar se o mesmo foi corrigido.
* O *Pull Request* precisa de algumas modificações, mas o desenvolvedor que o submeteu simplesmente desapareceu, não respondendo seus pedidos de correção. Porém, apesar das correções a serem feitas, o conteúdo do *Pull Request* é interessante o suficiente para que o mesmo não seja fechado.
* O *fork* de onde veio o pedido de *Pull Request* foi excluído. Neste caso, o *merge* ainda pode ser realizado, porém se for necessário alguma correção no código submetido, a sistuação se complica, pois neste caso você não tem mais acesso ao *fork* do desenvolvedor que realizou  a submissão.

Sendo assim, vamos aprender a resolver esses incovenientes com as ferramentas que o *git* nos oferece. Este tutorial foi testado com o Github, porém acredito que o mesmo processo possa ser realizado em outros serviços que suportam *git* como Gitlab, Bitbucket e etc.

Este tutorial exige um certo nível de conhecimento prévio com *git*. Como por exemplo, saber o conceito de *Pull Request*, *branch* e *push*. Qualquer dúvida, é só postar nos comentários. :)

## Realizando o checkout de um *Pull Request*

O primeiro passo é descobrir o ID do *Pull Request*. Ele normalmente fica do lado direito do título, precedido pelo símbolo `#`.

![](/images/mstuttgart/snapshot_48.png)

Na imagem de exemplo, logo acima, podemos observar que o ID do *Pull request* é `39`. De posse dessa informação, vamos então realizar uma cópia local do *Pull Request*. Isso pode ser feito com o seguinte comando:

```bash
git fetch origin pull/ID/head:NOMEBRANCH
```
Onde:

* ID: ID do Pull Request;
* NOMEBRANCH: é um nome qualquer definido para a *branch* que será criada.

Uma vez que o comando tenha sido executado, veremos uma mensagem semelhante a esta:

```prompt
From github.com:author/nome_repositorio
 * [new ref] refs/pull/39/head -> NOMEBRANCH
```
Se executarmos o comando `git branch`, veremos a *branch* recém-criada listada entre as outras *branchs*.

```prompt
$ git branch
* master
  NOMEBRANCH
```
Agora, basta trocar para a nova *branch* com

```
git checkout NOMEBRANCH
```
e realizar os testes.

No caso em que desejamos inserir modificações no conteúdo do *Pull Request*, nós realizamos os seguintes passos:

- Realizamos as modifições desejadas;
- Executamos o *commit* e o *push* da nova *branch*;
- Finalmente, criamos um novo *Pull Request* com essa mesma *branch* recém-criada.

## Conclusão

Bom, chegamos ao fim de mais um tutorial. Tentei apresentar de maneira objetiva os procedimento que utilizo quando me deparo com algumas das situações descritas no início do tutorial, sendo assim tive de ser mais direto nas explicações. Então caso tenha ficado alguma dúvida, é só postar nos comentários.

É isso pessoal. Até o próximo tutorial.

## Referências

* [https://help.github.com/articles/checking-out-pull-requests-locally](https://help.github.com/articles/checking-out-pull-requests-locally)
