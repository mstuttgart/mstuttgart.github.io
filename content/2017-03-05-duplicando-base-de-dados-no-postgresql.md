Title: PostgreSQL - Duplicando banco de dados
Slug: duplicando-banco-de-dados-no-postgresql
Date: 2017-03-05 20:30:53
Category: Banco de Dados
Tags: linux, tutorial, banco de dados, postgresql
Author: Michell Stuttgart
Email: michellstut@gmail.com
Github: mstuttgart
Linkedin: michell.stuttgart
Facebook: michell.stuttgart
Site: http://codigoavulso.com.br
Summary: Aprenda de maneira simples a duplicar um banco de dados com PostgreSQL.

Fala pessoal, tudo bem?

No outro tutorial sobre PostgreSQL ([link aqui](backup-e-restore-de-um-banco-de-dados-postgresql.html)), nós aprendemos a realizar o *backup* e *restore* de um banco de dados com PostgreSQL. Neste tutorial, veremos como duplicar um banco de dados já existente.

Inicialmente, pecisamos trocar para o usuário `postgres`. Isso pode ser feito através do comando:

```bash
sudo su - postgres
```

Uma vez como usuário `postgres`, podemos listar todos os bancos existentes com o comando:

```bash
psql -l
```

A título de exemplo, vamos supor que temos um banco de dados chamado `codigo_avulso` e queremos duplicá-lo, criando um novo banco de dados chamado `codigo_avulso_copia`.

Antes de presseguir, é aconselhável encerrar qualquer aplicação ou serviço que esteja fazendo uso do banco de dados a ser duplicado. Feito isso, basta executar o comando a seguir:

```sql
createdb --template=codigo_avulso --owner=postgres codigo_avulso_copia
```

No comando acima, temos o parâmetro *template*, que indica o nome do banco de dados original. Sempre que criamos um novo banco de dados no PostgreSQL, um *template* é utilizado. Se esse parâmetro não for passado para o comando `createdb`, um novo banco de dados vazio será criado utilizando um *template* pré-definido chamado `template1`.


O parâmetro *owner* indica o usuário `postgres` (não confundir com usuário linux do PostgreSQL) dono do banco de dados que será criado. Se nenhum *owner* for especificado, o novo banco de dados será atribuído ao *owner* `postgres`.

O parâmetro *owner* é muito útil quando alguma aplicação utiliza um usuário diferente de *postgres*. Utilizando o parâmetro *owner* com o nome do usuário do banco utilizado pela aplicação, não teremos erros de permissão quando a aplicação for acessar o novo banco de dados.

Agora, se executarmos novamente o comando `psql -l`, veremos o banco de dados original e o novo banco recém-criado.

É isso pessoal! Até o próximo *post*.
