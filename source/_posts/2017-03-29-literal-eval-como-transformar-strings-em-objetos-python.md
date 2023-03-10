---
title: "Aprenda a tranformar strings em objetos com literal_eval e Python"
date: 2017-03-29 20:53:56
tags:
- python
- literal_eval
- eval
categories: Python
---

O comando *literal_eval* é um interessante comando da biblioteca Python [ast- *Abstract Syntax Trees*](https://docs.python.org/2/library/ast.html). Ele avalia uma *string* contendo uma expressão Python e a executa.

## Exemplos

Executando a *string* 'True' como o valor booleano `True`:
```python
import ast
valor = ast.literal_eval('True')

print(valor) # saida: True
print(type(valor)) # saída: <type 'bool'>
```

Ou convertendo uma *string* contendo uma lista em um objeto *list*.

```python
import ast
valor = ast.literal_eval('[1, 2, 3]')

print(valor) # saída: [1, 2, 3]
print(type(valor)) # saída: <type 'list'>
```
Podemos também utilizá-lo para gerar um dicionário a partir de uma *string*:

```python
import ast
valor = ast.literal_eval("{'a': 1, 'b': 1, 'c': 42}")

print(valor) # saída: {'a': 1, 'b': 1, 'c': 42}
print(type(valor)) # saída: <type 'dict'>
```

## Diferenças entre 'eval' e 'literal_eval'

O `literal_eval` funciona de maneira semelhante ao conhecido comando `eval`, porém aceita apenas um pequeno conjunto de estruturas Python: *strings*, números, dicionários, listas, tupla, valores booleanos(*True* ou *False*) ou `None`. A partir da versão *3.2*, ele também passou a aceitar *bytes* e *set*.

O comando `eval` é mais poderoso, porém pode ser um problema se você não tem controle das *strings* fornecidas a ele. Se executarmos o seguinte comando `eval('rm -rf /')` em um sistema Linux (por favor, **NÃO** executem esse comando), todos os arquivos a partir da *raiz* do sistema operacional serão deletados. Entretanto, se passarmos a mesma *string* à instrução `literal_eval`, ela realizará uma validação de segurança na instrução antes de executá-la, lançando uma exceção do tipo `ValueError`.

```python
>>> ast.literal_eval("__import__('os').system('rm -rf /')")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/ast.py", line 84, in literal_eval
    return _convert(node_or_string)
  File "/usr/lib/python3.5/ast.py", line 83, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: <_ast.Call object at 0x7f120ed568d0>
```

## Conclusão

Apesar das limitação de tipo de estruturas aceitas pelo `literal_eval` (não que isso seja um problema), é aconselhável fazer uso do `literal_eval` ao invés do `eval`, pois o validação que a função realiza antes de executar a instrução pode nos evitar muita dor de cabeça (como exemplificado no exemplo acima) ao mesmo tempo que nos dá um controle maior sobre o código, pois sabemos os tipos de estruturas que o comando aceita como parâmetro.

## Referências

* Documentação (em inglês): [https://docs.python.org/3/library/ast.html](https://docs.python.org/3/library/ast.html)
* Um pouco mais da comparação entre os dois comandos (em inglês): [http://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval](http://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval)