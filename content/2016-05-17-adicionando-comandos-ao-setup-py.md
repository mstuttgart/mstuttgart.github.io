Title: Python - Adicione comandos ao setup.py
Date: 2016-05-17 22:48:00
Category: Python
Tags: python, setup, tutorial, PySide, Qt
Status: draft
Author: Michell Stuttgart
Summary: Neste tutorial veremos como adicionar comando personalizados ao arquivo setup.py do seu projeto.

Fala pessoal, tudo certo?

Nas últimas semanas, estive trabalhando em meu projeto [Pynocchio](https://github.com/pynocchio/pynocchio-comic-reader), um leitor de arquivos `.crb` e `.cbz`, normalmente utilizados em arquivos com imagens de histórias em quadrinhos/mangás. Esse projeto foi contruido utilizando a API [PySide](https://pt.wikipedia.org/wiki/PySide), que é um *biding* do framework [QT](https://pt.wikipedia.org/wiki/Qt) para Python.

Durante o desenvolvimento, muitas vezes precisei transformar os arquivos de interface (de extensão `.ui`) em código Python e/ou gerar arquivos de tradução, entre outros comandos. Inicialmente, realizava estas operações usando *shell script*, porém isso deixava a estrutura do meu projeto cheio de *scripts*. Então, me perguntei se não haveria uma maneira mais interessante de "guardar" esses comandos que tanto utilizava.

Como vimos na [primeira do tutorial sobre Unittest](http://mstuttgart.com.br/python-com-unittest-travis-ci-coveralls-e-landscape-parte-1-de-4.html), é possível executar os arquivos de testes do nosso projeto com o comando

```bash
python setup.py test
```

Então, pensei que seria interessante encontrar uma maneira de adicionar os comandos que precisava no `setup.py` para serem executados da mesma maneira e neste tutorial, irei explicar como fiz isso.

### O arquivo setup.py

Durante o desenvolvimento de um módulo Python, nós criamos um arquivo de nome `setup.py`. Esse arquivo possui informações relevantes do módulo, como o seu nome, nome do desenvolvedor, versão, dependências e etc. A seguir temos um exemplo do arquivo `setup.py`.

```python
from setuptools import setup, find_packages

setup(
    name='nomedomodulo'
    version='0.1.1'
    url='https://github.com/mstuttgart/nomedomodulo',
    license='MIT License',
    author='Michell Stuttgart',
    description=u'Interface python para uso dos serviços fornecidos pelo '
                u'SIGEPWeb dos Correios ',
    packages=find_packages(),
    include_package_data=True,
    test_suite='test',
)

```

Um ponto é que possui documentação um tanto esparsa pela internet (principalmente em português), é a possibilidade de adicionar comandos personalizados ao `setup.py`.

### Criando comandos personalizados

Aqui, irei usar novamente como exemplo o módulo que contruímos no tutorial anterior. O seu repositório pode ser acessado [aqui](https://github.com/mstuttgart/codigo-avulso-test-tutorial). Seu `setup.py` pode ser visto a seguir:

```python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='codigo-avulso-test-tutorial',
    version='0.1.1'
    url='https://github.com/mstuttgart/codigo-avulso-test-tutorial',
    license='MIT License',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    keywords='tutorial test unittest codigoavulso',
    description=u'Tutorial de teste unitário em Python para o blog Código Avulso',
    packages=find_packages(),
    install_requires=[],
    test_suite='test',
)

```
No [tutorial anterior](http://mstuttgart.com.br/gerando-relatorios-de-testes-com-coveralls.html), instalamos o módulo `coveralls` que serve para criar relatórios sobre os testes do seu projeto. Neste tutorial, a título de exemplo, iremos adicionar o comando para gerar esses relatórios em nosso `setup.py`. Caso deseje usar o `coveralls` em seu projeto, ele pode ser instalado pelo comando:

```bash
pip install coveralls
```

Agora iremos adicionar os comandos usados no tutorial no `setup.py`do nosso projeto. Para isso, precisamos criar uma classe que herda de `distutils.cmd.Command`. A classe também possui alguns atributos uteis como `description`, onde podemos definir uma descrição para o comando e `user_options`, que recebe uma lista de tuplas que serão os parâmetros do comando.

```python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import distutils.cmd

class BuildProFileCommand(distutils.cmd.Command):

  description = "Compile PySide pro files"

    # The format is (long option, short option, description).
    user_options = [
        ('tipo=', None, 'Tipo de saída do relatorio: no terminal, em html ou xml'),
    ]

setup(
    name='codigo-avulso-test-tutorial',
    version='0.1.1'
    url='https://github.com/mstuttgart/codigo-avulso-test-tutorial',
    license='MIT License',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    keywords='tutorial test unittest codigoavulso',
    description=u'Tutorial de teste unitário em Python para o blog Código Avulso',
    packages=find_packages(),
    install_requires=[],
    test_suite='test',
)

```
