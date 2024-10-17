---
title: "Using Literal Eval for String-to-Object Conversion in Python"
datePublished: Mon Oct 14 2024 12:52:43 GMT+0000 (Coordinated Universal Time)
cuid: cm290l9xw000e09mgfaf47f6y
slug: using-literal-eval-for-string-to-object-conversion-in-python
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1728907288529/8e513ae1-2520-441f-8202-18dbe426c4c4.png
tags: python, developer, python3, python-beginner, eval-function

---

`literal_eval` is an interesting function from Python's built-in library [ast](https://docs.python.org/2/library/ast.html). This function evaluates a string representation of any Python expression and executes it.

#### Prerequisites

* Basic knowledge of Python
    
* Python version: 3.10
    

### Examples

For example, let's convert the string `"True"` to the boolean value `True`:

```python
import ast
value = ast.literal_eval('True')

print(value) # output: True
print(type(value)) # output: <type 'bool'>
```

This command can also handle more complex instructions, like `list`:

```python
import ast

value = ast.literal_eval("[1, 2, 3]")

print(value) # output: [1, 2, 3]
print(type(value)) # output: <type 'list'>
```

and `dict`:

```python
import ast

value = ast.literal_eval("{'a': 1, 'b': 1, 'c': 42}")

print(value) # output: {'a': 1, 'b': 1, 'c': 42}
print(type(value)) # output: <type 'dict'>
```

### Differences between `eval` and `literal_eval`

The `literal_eval` function is similar to the well-known `eval` command, but it only accepts a limited set of Python structures: *strings*, numbers, dictionaries, lists, tuples, boolean values (*True* or *False*), or `None`.

The `eval` command is more powerful, but it can be dangerous if you don't control the strings it processes. For example, running the command `eval('rm -rf /')` on a Linux system (please, **DO NOT** run this command) would delete all files from the root of the operating system. However, if you pass the same string to the `literal_eval` function, it will perform a security check before executing it and will raise a `ValueError` exception.

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

### Conclusion

Despite the limitations on the types of structures accepted by `literal_eval` (which is not really an issue), it is recommended to use `literal_eval` instead of `eval`. The function's validation before executing an instruction can prevent many problems (as shown in the example above) and gives us better control over the code, as we know the types of structures it accepts as parameters.

### References

* ast - Abstract Syntax Trees — Python 3.10.15 documentation. [https://docs.python.org/3.10/library/ast.html](https://docs.python.org/3.10/library/ast.html).