---
layout: post
title: "MkDocs - Documentação de Projetos com Markdown"
date: 2017-01-25 14:02:40
description: 'Crie documentação para seus projetos com stilo'
main-class: 'dev'
tags:
- mkdocs
- documentação
- python
categories: Dev
introduction: 'MkDocs é um gerador de site estático rápido e simples, destinado a criação de documentação de projetos.'
---

Fala pessoal, tudo certo?

O *post* de hoje é sobre uma ferramenta que descobri algum tempo atrás e que achei bacana compartilhar. Neste *post* vamos estudar a criação de um site para a documentação de nossos projetos utilizando a ferramenta *MkDocs*.

O *MkDocs* é um gerador de site estático minimalista e muito simples de usar. Ele funciona de maneira semelhante a outros geradores como *Pelican* e *Jenkill*, entretanto, diferente desses, o *MkDocs* é voltado à criação de documentação ao invés de blogs.

Os sites contruídos com o *MkDocs* podem ser hospedados facilmente em muitos lugares, inclusive utilizando o *github pages*.

## Instalação

O *MKDocs* possui suporte para as versões 2.7+ e 3.3+ do Python. A sua instalação é semelhante a outros pacotes Python.

```bash
pip install mkdocs
```
Podemos utilizar o seguinte comando para verificar se tudo foi instalado corretamente:

```bash
mkdocs --version
```
Se tudo estiver funcionado corretamente, o resultado do comando será a versão do *MkDocs* instalado.

### Criando o Projeto

A utilização do *MkDocs* é bem simples. Inicialmente criamos o nosso projeto com:

```bash
mkdocs new my-project
cd my-project
```
Dentro da pasta *my-projet* teremos a seguinte estrutura de diretórios:

```bash
.
├── docs
│   └── index.md
└── mkdocs.yml
```
Todas as páginas do seu site serão armazenadas dentro da pasta *docs*. Inclusive dentro dessa mesma pasta existe o arquivo *index.md*. Este arquivo será a página principal do site. Além do diretório *docs*, também temos o arquivo *mkdocs.yml*, que é o arquivo de configuração utilizado pelo *MkDocs*.

### Servidor de Desenvolvimento

O *MkDocs* possui um servidor de desenvolvimento, que nos permite pré-visualizar nossa documentação. Para utilizar entre com o comando:

```bash
mkdocs serve
```
Veremos algo semelhante em nosso terminal:
```bash
INFO    -  Building documentation...
INFO    -  Cleaning site directory
[I 170125 15:05:33 server:283] Serving on http://127.0.0.1:8000
[I 170125 15:05:33 handlers:60] Start watching changes
[I 170125 15:05:33 handlers:62] Start detecting changes
```
Um ponto interessante deste servidor de desenvolvimento é que ele atualiza automaticamente o conteúdo exibido na página sem necessidade de reiniciá-lo. Sendo necessário apenas atualizar a página do navegador.
Uma vez que o servidor esteja sendo executado, podemos acessar o site de documentação no navegador pelo seguinte endereço: *http://localhost:8000/* ou *http://127.0.0.1:8000*

![](/images/mstuttgart/snapshot_46.png)

### Adicionado Novas Páginas

A página da imagem acima é o conteúdo do *index.md*. Podemos adicionar outra página facilmente editando a tag `pages` presente no arquivo *mkdocs.yml*.
```yml
site_name: My Docs
pages:
    - Home: index.md
    - About: about.md
```
Em seguida, criamos um arquivo `about.md` dentro da pasta `docs` e atualizamos a página no navegador para que o menu aparecera no topo do site, nos permitindo navegar entre as páginas.

![](/images/mstuttgart/snapshot_47.png)

### Outras Configurações
Para trocarmos o nome do site, basta alterarmos o nome presente na tag `site_name`. Também podemos trocar o tema do site através da tag `theme`. O *MkDocs* vem com alguns temas próprios, que são os temas `mkdocs` (utilizado neste tutorial) e o `readthedocs` (utilizado muito em documentação de api Python). Também existem temas feitos por terceiros, que podem ser encontrados [aqui](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes). Para utilizá-los siga as instruções de instalação de cada tema.

### Compilando

Quando o site de documentação estiver pronto, o próximo passo é compilá-lo. Isso é feito através do comando:

```bash
mkdocs build
```
Um diretório chamato `site` será criado.

```bash
about
css
fonts
img
js
mkdocs
404.html
index.html
sitemap.xml
```

O conteúdo deste diretório é o nosso site em si, pronto para ser hospedado no *github-pages* (o seu conteúdo pode ser lançado na *branch* `gh-pages`) ou em outro servidor, de acordo com a preferência.

O *MkDocs* possui um comando onde ele compila o site e já o envia para o *github-pages*. Para mais informações, dê uma olhada na documentação (em inglês) [aqui](http://www.mkdocs.org/user-guide/deploying-your-docs/).

## Conclusão

Chegamos ao fim de mais um tutorial. Este foi bem curto, apenas para apresentar o *mkdocs*. Futuramente, pretendo fazer outro tutorial explicando como realizar o deploy no *github-pages* e inclusive, como automatizar esse processo.

Eu recentemente utilizei o *MkDocs* no site/documentação do meu leitor de quadrinhos *Pynocchio* [aqui](https://pynocchio.github.io/).

É isso pessoal! Obrigado por ler até aqui. Até o próximo *post*!

## Referências

* [Documentação MKDocs (inglês)](http://www.mkdocs.org/)
