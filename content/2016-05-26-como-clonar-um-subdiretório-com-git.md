Title: Git - Como mover um subdiretório entre repositórios
Slug: como-mover-um-subdiretorio-de-um-repositorio-para-outro-usando-git
Date: 2017-05-14 15:13:46
Category: Git
Tags: linux, tutorial, git, github, dicas
Author: Michell Stuttgart
Email: michellstut@gmail.com
Github: mstuttgart
Linkedin: michellstut
Facebook: michell.stuttgart
Site: http://mstuttgart.com.br
Summary: Neste tutorial, vamos aprender como transferir um subdiretório de um repositório para outro sem perder seu histórico de contribuições usando git.

Fala pessoal, tudo tranquilo?

Meu caro leitor(a), você já passou por uma situação onde precisava transferir um diretório de um repositório para outro, sem perder o histórico de contribuições referentes a esse diretório?

Semanas atrás me deparei com esse desafio e achei interessante compatilhar com você a solução que encontrei.

#### Analisando o problema

Na situação descrita acima, a *priori*, temos duas possíveis soluções:

1. Criar um novo repositório e copiar o diretório desejado do antigo repositório para o novo.
1. Clonar o repositório original, e no repositório clonado remover todos os outros diretórios e arquivos, deixando apenas diretório desejado.

As duas opções resolvem nosso problema, porém ambas possuem alguns incovenientes.

* Na *opção 1*, o histórico de *commits* do antigo repositório não é mantido, já que apenas o diretório é copiado. Desse modo, perdemos a lista de colaborações feitas por outros desenvolvedores, algo muito ruim.
* Na *opção 2*, o histórico de *commits* do antigo repositório é mantido, porém ele traz *commits* de alterações de outras partes do projeto, o que não é interessante uma vez que desejamos separá-lo do seu antigo projeto.

Não seria interessante que o histórico fosse mantido, porém apenas com os *commits* que dizem respeito ao diretório que desejamos separar do repositório original?

Felizmente, o git nos fornece ferramentas que tornam isso possível.

#### Resolvendo o problema

Para começar, vamos supor que temos dois repositórios: *repo_novo*, atualmente vazio e *repo_antigo*. O *repo_antigo* possui um diretório chamado *dirA*. Como exemplo, vamos transferir o *dirA* do repositório *repo_antigo* para o repositório *repo_novo*, sem perder seu histórico de *commits*.

Incialmente, vamos fazer o clone do *repo_antigo*.

```bash
git clone https://github.com/nomeusuario/repo_antigo.git
```
Entre dentro da pasta recém-clonada:

```bash
cd repo_antigo/
```
Agora vamos executar o seguinte comando:

```git
git filter-branch --subdirectory-filter dirA -f
```

O comando acima aplica um filtro para subdiretórios (--subdirectory-filter) usando como referência o subdiretório que passamos como parâmetro (dirA) e analisando todo os histórico de *commits* procurando por *commits* relacionados a ele, do início do histórico até o *commit* mais atual (HEAD).

Após executar o comando, verifique o conteúdo da pasta *repo_antigo*. Agora os únicos arquivos e diretórios presentes são os que estavam dentro do diretório *dirA*. O próximo passo é jogar tudo novamente dentro de um diretorio de nome *dirA*. Fazemos isso com o comando:

```git
git filter-branch -f --tree-filter 'mkdir -v dirA; git mv -k * dirA' HEAD
```

Se usarmos o comando `git log`, veremos que apenas os *commits* relacionados ao conteúdo de *dirA* permaneceram no histórico. Vale lembrar aqui que os outros *commits* não foram removidos do repositório remoto original, o histórico foi filtrado apenas localmente.

O próximo passo agora é subir tudo isso para o *novo_repo*. Para isso, precisamos primeiro substituir a url do *repo_antigo* pela url do nosso *repo_novo* e em seguida realizar o *push*. Vale lembrar que se seu *repo_novo* já possuir algum *commit* (normalmente adicionando um arquivo README.md e um arquivo LICENSE) será necessário execura um `git pull` antes do *push* ou sobreescrever o commit inicial do novo repositório usando `git push -f`.

```bash
git remote set-url origin https://github.com/usuario/novo_repo.git
git fetch origin
git push
```

Neste caso em especial, eu apenas copiei o conteúdo do diretório *dirA* em um repositório diferente. Entretanto, a principal utilidade desse método é quando desejamos transferir o diretório para um novo repositório, sendo o mesmo posteriormente removido do repositório antigo. Porque assim, todas as novas colaborações para o conteúdo de *dirA* devem, a partir de agora, enviadas para o *novo_repo*.

Apenas para complementar o *post*. Eu fiz uso deste método recentemente, em um dos projetos que contribuo. O repositório [colour-schemes](https://github.com/daylerees/colour-schemes) possui temas de vários editores usados em desenvolvimento (Sublime Text, Atom, Kate e etc), tendo cada um seu respectivo diretório com seus temas.

Sou usuário da IDE [PyCharm](https://www.jetbrains.com/pycharm/), então fiz alguns ajustes nos temas do diretório *jetbrains* (empresa dona do [PyCharm](https://www.jetbrains.com/pycharm/)) presentes nesse repositório. Foram 55 temas ajustados (me custou algumas horas de trabalho haha) mas o resultado foi muito satisfatório. Após terminar os ajustes, enviei um *pull request* para o repositório original. Porém o que me frustrou, foi o fato dos responsáveis pelo repositório demorarem muito tempo (muito mesmo) para revisar e aprovar os *pull requests*. Sendo assim, decidi criar um repositório contendo apenas os temas do [PyCharm](https://www.jetbrains.com/pycharm/) já com minhas alterações, de modo que outros desenvolvedores pudessem usá-los. Então utilizei o método acima, clonei o meu fork do repositório original (que possuia os minhas modificações) e executei o filtro apenas para o diretório *jetbrains*. Em seguida enviei para [este meu repositório](https://github.com/mstuttgart/pycharm-colour-scheme). Compare o conteúdo com o repositório original [aqui](https://github.com/daylerees/colour-schemes/tree/master/jetbrains).

É isso pessoal. Espero que a dica seja útil para vocês. Qualquer dúvida é só postar nos comentários.

Até o próximo tutorial.
