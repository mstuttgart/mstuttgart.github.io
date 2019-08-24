---
layout: post
title: "Crie diretórios e arquivos usando expressões regulares"
date: 2014-08-30T05:47:00-07:00
description: "Utilize regex para criar diretórios e arquivos pelo terminal"
tags:
- linux
- regex
- mkdir
categories: Linux
---

Todo programador linux sabe como o uso do terminal pode ser uma ajuda insubstituível na realização de algumas tarefas. Neste post eu irei compartilhar algumas coisa que descobri usando o terminal.

## Exemplo 1

Para começar, quando desejamos criar um diretório pelo terminal, usamos o seguinte comando:

```powershell
mkdir nome_do_diretorio
```

Algo muito prático. Mas e se precisarmos criar 10 diretórios com o seguinte formato de nome: `minha_pasta_01`, `minha_pasta_02`, `minha_pasta_03`, ..., `minha_pasta_10`.

Certamente a realização dessa tarefa pelo ambiente gráfico é algo muito cansativo e lento. Então vamos fazer uso do terminal do linux para resolver essa situação.

Você talvez não saiba (eu pelo menos não sabia.. hehe), que o comando `mkdir` aceita expressões regulares. Então, vamos usar-las para resolver nosso problema.

```
mkdir minha_pasta_{01..10}
```

Dentro da `{}`, nós inserimos a expressão regular desejada. A expressão `{01..10}` irá criar `10` diretórios seguindo o padrão de nomes desejado.

```
.
├── minha_pasta_01
├── minha_pasta_02
├── minha_pasta_03
├── minha_pasta_04
├── minha_pasta_05
├── minha_pasta_06
├── minha_pasta_07
├── minha_pasta_08
├── minha_pasta_09
└── minha_pasta_10
```

Para deletarmos os diretórios que acabamos de criar também podemos usar a mesma expressão regular.

```
rm -rf minha_pasta_{1-10}
```
## Exemplo 2

Vamos criar 5 arquivos com o seguinte formato de nome: `arquivo_”numero_do_arquivo”.txt`. Basta no terminal, usarmos o comando `touch`.

```
touch arquivo_{1..5}.txt
```
Apos executarmos o comando, `5` arquivos do tipo `.txt` serão criados seguindo a regra de nome que desejamos.

```
.
├── arquivo_1.txt
├── arquivo_2.txt
├── arquivo_3.txt
├── arquivo_4.txt
├── arquivo_5.txt
```

## Exemplo 3

Vamos criar um conjunto de arquivos cujos nomes seguem o formato: `arquivo_a.txt`, `arquivo_b.txt`, … `arquivo_z.txt`. Basta executar o seguinte comando no terminal:

```
touch arquivo_{a..z}.txt
```
Resultado:

```
.
├── arquivo_a.txt
├── arquivo_b.txt
├── arquivo_c.txt
├── arquivo_d.txt
├── arquivo_e.txt
├── arquivo_f.txt
├── arquivo_g.txt
├── arquivo_h.txt
├── arquivo_i.txt
├── arquivo_j.txt
├── arquivo_k.txt
├── arquivo_l.txt
├── arquivo_m.txt
├── arquivo_n.txt
├── arquivo_o.txt
├── arquivo_p.txt
├── arquivo_q.txt
├── arquivo_r.txt
├── arquivo_s.txt
├── arquivo_t.txt
├── arquivo_u.txt
├── arquivo_v.txt
├── arquivo_w.txt
├── arquivo_x.txt
├── arquivo_y.txt
└── arquivo_z.txt
```

## Exemplo 4

Vamos criar um conjunto de arquivo cujo nomes seguem o seguinte formato: `a1.txt`, `a2.txt`, `a3.txt`, …, `a5.txt`, `b1.txt`, `b2.txt`, …, `b5.txt`. Basta executar o seguinte comando no terminal:

```
touch {a-b}{1-5}.txt
```
A seguir temos os arquivos que foram criados pela execução da expressão regular.

```
.
├── a1.txt
├── a2.txt
├── a3.txt
├── a4.txt
├── a5.txt
├── b1.txt
├── b2.txt
├── b3.txt
├── b4.txt
├── b5.txt
```
Como podemos perceber, dentro da `{}` podemos adicionar qualquer expressão regular.

É isso pessoal. Espero que a dica seja útil para vocês. Até o próximo post.
