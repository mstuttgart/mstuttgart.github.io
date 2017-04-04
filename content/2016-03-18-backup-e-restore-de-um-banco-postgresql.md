Title: PostgreSQL - Backup e Restore de um banco de dados
Slug: backup-e-restore-de-um-banco-de-dados-postgresql
Date: 2016-03-18 11:59:51 -0300
Category: Banco de Dados
Tags: linux, tutorial, banco de dados, backup, restore, postgresql
Author: Michell Stuttgart
Summary: Aprenda a executar de maneira simples o backup e restore de um banco de dados PostgreSQL

Quando trabalhamos com alguma aplicações que faz uso de um banco de dados, muitas vezes precisamos realizar um `backup` do nosso banco (antes de alguma atualização importante na aplicação) ou executar o `restore` desse banco caso seja necessário.

Eu trabalhei por um tempo desenvolvendo funcionalidades para o ERP Odoo. Esse ERP faz uso do PostgreSQL, e frequentemente eu precisava realizar `backup` e `restore` dos bancos que criava para atualizar as máquinas dos clientes. Então, segue abaixo o procedimento que eu utilizava.

### Backup

Para realizar o `backup`, primeiro precisamos logar como usuário `postgres`. No terminal entre com:

```bash
sudo su - postgres
```

Uma vez logado, voce pode reparar que o nome de usuário no terminal mudou. Caso seja necessário, é possível visualizar a lista de bancos existentes na sua máquina através do comando abaixo:

```sql
psql -l
```

Agora, vamos realizar o backup do banco com o seguinte comando:

```sql
pg_dump -Fc nome_banco > nome_banco_backup.dump
```

Assim será criado um arquivo com a extensão `.dump` no diretório `/var/lib/postgressql`.

Também podemos incrementar o comando de modo a deixarmos registrado o dia, hora e minuto em que o `backup` foi realizado, algo muito útil caso você precise realizar a restauração do banco.

```sql
pg_dump -Fc nome_banco > nome_banco-backup-`date +%Y-%m-%d-%H-%M`.dump
```

### Restore

A restauração do banco é tão simples quanto o `backup`.
Primeiramente, vamos criar uma entrada para o banco que será restaurado.

```sql
createdb banco_do_cliente_x
```

Apenas uma observação, antes de criar uma entrada para o novo banco, é uma boa prática verificar se já não existe outro banco com o mesmo nome. Isso pode ser feito com o comando `psql -l`.

Caso o seu objetivo seja mesmo substituir o banco `banco_do_cliente_x`, você pode usar o comando abaixo:

```sql
dropdb banco_do_cliente_x
createdb banco_do_cliente_x
```

Finalmente realizamos o `restore` do banco com o comando:

```sql
pg_restore -d banco_do_cliente_x banco_backup.dump
```

Vale lembrar que para executar o comando acima, o arquivo .dump deve estar no diretório `/var/lib/postgressql` (mova o arquivo para esse diretório caso ele ainda não esteja).

É isso pessoal. Esse dica já me salvou muito vezes e espero que seja útil para vocês também.

Até o próximo post!
