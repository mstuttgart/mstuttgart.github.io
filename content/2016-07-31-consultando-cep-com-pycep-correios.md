Title: Python - Consulte CEPs com pycep-correios
Slug: consultando-cep-com-pycep-correios
Date: 2016-07-31 16:28:36
Category: Python
Tags: correios, python, api, cep
Author: Michell Stuttgart
Summary: Obtendo dados de um cep diretamente do webservice dos Correios.

Boa tarde, pessoal. Tudo certo?

Neste *post* irei falar um pouco sobre um pequeno projeto meu. Trata-se do [PyCEP Correios](https://github.com/mstuttgart/pycep-correios).

O [PyCEP Correios](https://github.com/mstuttgart/pycep-correios) é uma api desenvolvida em Python que realiza a busca dos dados de um dado CEP diretamente no *webservice* dos Correios, sendo essa a principal diferença em relação a outras api's de consulta de CEP. O retorno dessa consulta é um *dict* contendo os dados do endereço pertencente ao CEP. Este projeto foi iniciado por mim para fins de estudo, porém ele pode ser utilizado normalmente em projetos mais sérios.

### Instalação

O PyCEP Correios pode ser facilmente instalado com o comando a seguir (apenas para python3):

```bash
pip3 install pycep-correios
```

### Como usar

Consultar o endereço de um CEP é muito simples com o [PyCEP Correios](https://github.com/mstuttgart/pycep-correios). Não importa se o CEP fornecido possui hífen ou ponto. O [PyCEP Correios](https://github.com/mstuttgart/pycep-correios) trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.

Veja os exemplos a seguir:

```python
from pycep_correios.correios import Correios

# Tambem pode ser usado .get_cep('37503130')
endereco = Correios.get_cep('37503130')

print(endereco['rua'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['uf'])
print(endereco['outro'])

```

Outro exemplo, usando o CEP anterior, porém com hífen "-" e ponto ".".

```python
from pycep_correios.correios import Correios

endereco = Correios.get_cep('37.503-130')

print(endereco['rua'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['uf'])
print(endereco['outro'])

```

Um exemplo alternativo, enviamos um CEP incorreto, com o numero de digitos inferior a 8.

```python
from pycep_correios.correios import Correios

try:
    endereco = Correios.get_cep('37.50-130')
except CorreiosCEPInvalidCEPException as exc:
    print(exc.message)
```

### Conclusão

É isso pessoal. Este *post* foi feito simplemesnte para apresentação do [PyCEP Correios](https://github.com/mstuttgart/pycep-correios). Eu recentemente migrei toda api para Python 3.4. A api usada para consulta (*suds*) foi substituída pela *requests*, já que esse ultimo tem um desenvolvimento ativo. Espero que o módulo seja útil a vocês. Se alguém possuir alguma crítica ou sugestão sinta-se livre para comentar.

Obrigado por ler até aqui! Até o próximo *post*.
