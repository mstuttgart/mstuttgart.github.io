Title: Python - Consulta de CEP com PyCEPCorreios
Slug: consultando-cep-com-pycep-correios
Date: 2017-06-22 22:42:36
Category: Python
Tags: correios, python, api, cep
Author: Michell Stuttgart
Summary: Obtendo dados de um CEP diretamente do webservice dos Correios.

Boa tarde, pessoal. Tudo certo?

Atualização do *post* antigo. Neste *post* irei falar um pouco sobre a nova versão da [PyCEP Correios](https://github.com/mstuttgart/pycep-correios).

O [PyCEPCorreios](https://github.com/mstuttgart/pycep-correios) é uma api desenvolvida em Python que realiza a busca dos dados de um dado CEP diretamente no *webservice* dos Correios, sendo essa a principal diferença em relação a outras api's de consulta de CEP. O retorno dessa consulta é um *dict* contendo os dados do endereço pertencente ao CEP. Este projeto foi iniciado por mim para fins de estudo, porém ele pode ser utilizado normalmente em projetos mais sérios.

**Obs:** A versão *2.0.0* trouxe melhorias consideráveis no código com o objetivo de tornar a API mais
fácil de ser utilizada. Porém, ela é incompatível com as versões anteriores. Houve
grandes melhorias na documentação, código e testes da API. Sendo assim,
decidi republicar esse *post* com novas informações sobre a lib.

### Instalação

O PyCEP Correios pode ser facilmente instalado com o comando a seguir (apenas para python3):

```bash
pip3 install pycep-correios
```

### Como usar

Consultar o endereço de um CEP é muito simples com a [PyCEPCorreios](https://github.com/mstuttgart/pycep-correios). Não importa se o CEP fornecido possui hífen ou ponto. A [PyCEPCorreios](https://github.com/mstuttgart/pycep-correios) trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.

Veja os exemplos a seguir:

```python
import pycep_correios

endereco = pycep_correios.consultar_cep('37503130')

print(endereco['end'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['complemento2'])
print(endereco['uf'])
print(endereco['cep'])

```

Um exemplo alternativo, enviamos um CEP incorreto, com a quantidade de dígitos inferior a 8.

```python
from pycep_correios
from pycep_correios.excecao import CEPInvalido

try:
    endereco = pycep_correios.consultar_cep('00000000')
except CEPInvalido as exc:
    print(exc)

```

Para outras exceções devemos utilizar as exceções da biblioteca *requests*, no qual a
PyCEPCorreios faz uso para comunicação com o *webservice*. As antigas exceções da biblioteca também foram removidas a fim de evitar redundância com as exceções da *requests* e toda a API agora possui comandos e documentação em postuguês.

A PyCEPCorreios também possui funções para validar e formatar números de CEP. Para mais exemplos, veja a documentação [aqui](https://pycep-correios.readthedocs.io/pt/latest/usage.html). Abaixo, segue alguns *links* úteis.

* Repositório: [https://github.com/mstuttgart/pycep-correios](https://github.com/mstuttgart/pycep-correios)
* PyPi: [https://pypi.python.org/pypi/pycep-correios](https://pypi.python.org/pypi/pycep-correios)
* Documentação: [https://pycep-correios.readthedocs.io/pt/latest/](https://pycep-correios.readthedocs.io/pt/latest/)

Se deseja contribuir, por favor dê uma olhada na documentação [aqui](https://pycep-correios.readthedocs.io/pt/latest/contributing.html). Contribuições são sempre bem-vindas.

### Conclusão

É isso pessoal. Este *post* foi feito simplesmente para apresentação da [PyCEP Correios](https://github.com/mstuttgart/pycep-correios) e mostrar exemplos
de utilização da versão *2.0.0* da API. Espero que o módulo seja útil a vocês. Se alguém possuir alguma crítica ou sugestão sinta-se livre para comentar.

Obrigado por ler até aqui! Até o próximo *post*.
