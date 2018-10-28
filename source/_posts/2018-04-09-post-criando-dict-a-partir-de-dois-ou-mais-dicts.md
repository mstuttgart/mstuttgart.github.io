---
title: "Criando dicts a partir de outros dicts"
date: 2018-04-09 10:02:29
description: "Aprenda a criar dicionários com o conteúdo de outros dicionarios em Python"
main-class: 'python'
tags: 
- python
- dict
- dicionario
- dica
- tutorial
categories: Python
introduction: "Aprenda a criar dicionários a partir de um ou mais dicionarios com Python"
---

Fala pessoal, tudo tranquilo?

Neste post irei compartilhar com vocês uma dica que aprendi para criar um *dict* ou dicionário, a partir de outros *dicts* em Python. Como já é de costume da linguagem, nós podemos fazer isso de várias maneiras diferentes. 

Vamos supor que temos os seguintes dicionários:

```python
dict_1 = {
    'a': 1,
    'b': 2,
}

dict_2 = {
    'b': 3,
    'c': 4,
}
```

Como exemplo, vamos criar um novo dicionário chamado `n_dict` com os valores dos dois `dicts` acima. Uma abordagem bem conhecida é utilizar o método `update`.

```python
n_dict = {}

n_dcit.update(dict_1)
n_dcit.update(dict_2)
```

Assim, temos que `n_dict` será:

```python
n_dict = {
    'a': 1,
    'b': 3,
    'c': 4,
}
```

Este metodo funciona bem, porém temos de chamar o metodo `update` para cada `dict` que desejamos "inserir" em `n_dict`. Não seria interessante se fosse possível passar todos os `dicts` necessários já na inicialização de `n_dict`?

O Python 3 introduziu uma maneira bem interessante de se fazer isso, utilizando os operadores `**`.

```python
n_dict = {
    **dict_1,
    **dict_2,
}

```

Assim, de maneira semelhante ao exemplo anterior, temos que `n_dict` será :

```python
print(n_dict['a'])

# Saida: 1

print(n_dict['b'])

# Saida: 3

print(n_dict['c'])

# Saida: 4
```

### Cópia de *dicts* dentro de *dicts*

Devemos ter um cuidado extra quando utilizamos o prcedimento de inicialização acima. Apenas os valores do primeiro nível serão realmente duplicados no novo dicionário. Como exemplo, vamos alterar uma chave presente em ambos os `dicts` e verificar se as mesmas possuem o mesmo valor:

```python
dict_1['a'] = 10
n_dict['a'] = 11

print(dict_1['a'])

# Saida: 10

print(n_dict['a'])

# Saida: 11

```

Porém isso muda quando um dos valores de `dict_1` for uma `list`, outro `dict` ou algum objeto complexo. Por exemplo:

```python
dict_3 = {
    'a': 1,
    'b': 2,
    'c': {
        'd': 5,
    }
}
```

e agora, vamos criar um novo `dict` a partir desse:

```python
n_dict = {
    **dict_3,
}

```

Como no exemplo anterior, podemos imaginar que foi realizado uma cópia de todos os elementos de `dict_3`, porém isso não é totalmente verdade. O que realmente aconteceu é que foi feita uma cópia *superficial* dos valores de `dict_3`, ou seja, apenas os valores de *primeito nível* foram duplicados. Observe o que acontece quando alteramos o valor do `dict` presente na chave `c`.

```python
n_dict['c']['d'] = 11

print(n_dict['c']['d'])

# Saida: 11

print(dict_3['c']['d'])

# Saida: 11 (valor anterior era 5)

```

No caso da chave `c`, ela contem uma referência para outra estrutura de dados (um `dict`, no caso). Quando alteramos algum valor de `dict_3['c']`, isso reflete em todos os `dict` que foram inicializados com `dict_3`. Em outras palavras, deve-se ter cuidado ao inicializar um `dict` a partir de outros `dicts` quando os mesmos possuírem valores complexos, como `list`, `dict` ou outros objetos (os atributos deste objeto não serão duplicados).

De modo a contornar este incoveniente, podemos utilizar o método *deepcopy* da *lib* nativa [copy](https://docs.python.org/2/library/copy.html). Agora, ao inicializarmos `n_dict`:

```python
import copy

dict_3 = {
    'a': 1,
    'b': 2,
    'c': {
        'd': 5,
    }
}

n_dict = copy.deepcopy(dict_3)
```

O método `deepcopy` realiza uma cópia recursiva de cada elemento de `dict_3`, resolvendo nosso problema. Veja mais um exemplo:

```python
n_dict['c']['d'] = 11

print(n_dict['c']['d'])

# Saida: 11

print(dict_3['c']['d'])

# Saida: 5 (valor não foi alterado)
```

Para mais detalhes e outros exemplos, deem uma olhada neste *post* do forum da Python Brasil [aqui](https://groups.google.com/forum/#!topic/python-brasil/OhUqYQ32M7E).

É isso pessoal. Espero que esta dica seja útil para vocês!

Até o próximo post!
