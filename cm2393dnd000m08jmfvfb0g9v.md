---
title: "How to Merge Multiple Dictionaries with Python"
datePublished: Thu Oct 10 2024 12:04:07 GMT+0000 (Coordinated Universal Time)
cuid: cm2393dnd000m08jmfvfb0g9v
slug: how-to-merge-multiple-dictionaries-into-one-in-python
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1728652963001/f62d0190-d451-444b-baa0-fe69bc893e90.png
tags: python, python3, beginners, python-beginner

---

In this tutorial, we'll explore how to create a `dict`, or dictionary, from one or more existing dictionaries in Python.

As usual in programming, there are several ways to achieve this.

> I recently started to practice my writing in English. I apologize in advanced for any errors. :)

#### Prerequisites

* Basic understanding of Python
    

## **Initial Approach**

To begin, let's assume we have the following dictionaries:

```python
dict1 = {
    'a': 1,
    'b': 2,
}

dict2 = {
    'b': 3,
    'c': 4,
}
```

For example, let's create a new dictionary called `dictx` using the values from `dict1` and `dict2` mentioned above. A common method to do this is by using the `update` method.

```python
dictx = {}

dictx.update(dict1)
dictx.update(dict2)
```

So, `dictx` will be:

```python
print(dictx)
# output: {'a': 1,'b': 3,'c': 4}
```

This method works well, but we have to call the `update` method for each dictionary we want to merge into `dictx`. Wouldn't it be interesting if we could pass all the dictionaries needed right when we create `dictx`?

# **Create a dictionary from multiple dictionaries**

Python 3 introduced a very useful way to do this by using the `**` operator.

```python
dictx = {
 **dict1,
 **dict2,
}

print(dictx)
# output: {'a': 1,'b': 3,'c': 4}
```

# **A real copy of Dictionaries**

When using the method described above, we need to keep a few things in mind. Only the first-level values will be copied into the new dictionary. For example, let's change the key `'a'` present in both dictionaries and see if they have the same value:

```python
dict1['a'] = 10
dictx['a'] = 11

print(dict1['a'])
# output: 10

print(dictx['a'])
# output: 11
```

We change the value of key `'a'` in both dictionaries. However, this changes if one of the values in `dict1` is a data structure, like a `list`, another `dict`, or a complex object. For example:

```python
dict3 = {
    'a': 1,
    'b': 2,
    'c': {
        'd': 5,
    },
}
```

We have a `dict` object under the key `'c'`. Now, let's create a new `dict` from it:

```python
dictx = {
**dict3,
}
```

As in the previous example, we might think all the elements of `dict3` are copied, but this isn't completely accurate. What actually happens is a **shallow copy** of `dict3`'s values is made, meaning only the **first-level** values are duplicated. Let's see what happens when we change the value of the dictionary under the key `'c'`.

```python
dictx['c']['d'] = 11

print(dictx['c']['d'])
# output: 11

print(dict3['c']['d'])
# output: 11 (previous value was 5)
```

For the key `'c'`, it holds a reference to another data structure (a `dict` in this case). When we change any value in `dict3['c']`, it affects all dictionaries that were initialized with `dict3`. In other words, we need to be careful when creating a dictionary from others if they have complex values like `list`, `dict`, or other objects, as the attributes of these objects will not be duplicated.

To solve this issue, we can use the built-in dictionary method `copy`. Now, when we create `dictx`:

```python
dict3 = {
    'a': 1,
    'b': 2,
    'c': {
        'd': 5,
    },
}

dictx = dict3.copy()
```

The `copy` method creates a shallow copy of each element in `dict3`, which helps solve our problem.

Here's another example:

```python
dictx['c']['d'] = 11

print(dictx['c']['d'])
# output: 11

print(dict3['c']['d'])
# outuput: 5 (value has not been changed)
```

The values in `dictx` and `dict3` are not equal because `'d'` in `dict3['c']` and `dictx['c']` are references to different objects.

# **Conclusion**

This article aims to simply demonstrate how to create *dictionaries* using some features the language offers, along with the pros and cons of each approach.

That's it.

Thanks for reading!