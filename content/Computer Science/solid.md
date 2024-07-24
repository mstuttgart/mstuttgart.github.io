---
title: SOLID
draft: true
tags:
  - solid 
  - poo 
  - object-oriented-programming
---

`SOLID` é um acrônimo para descrever os 5 principios de design para projetos de softwares usando linguagens de [[Programação Orientada a Objetos (POO)]]. Esses princípios são agnośticos em relação a linguagem de programação, ou seja, independem da linguagem de programação escolhida (desde que a mesma siga o paradigma POO). Os princípios foram apresentados por [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) em uma plubicação intitulada [Design Principles and Design Patterns](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf). A abreviação `SOLID` foi proposta, posteriormente, por [Michael Feathers](https://www.google.com/search?client=firefox-b-lm&q=Michael+Feathers).

As letras do acrônimo possuem o seguinte siginificado:

* S - [Single Responsability Principle](#single-responsability-principle-srp-1)
* O - [Open Close Principle](#open-closed-principle-ocp-2)
* L - [Liskov Substitution Principle]
* I - [Interface Segregation Principle]
* D - [Dependency Inversion Principle]

Estes principios (ou postulados) auxiliam o desenvolvedor a projetar e escrever softwares Orientado a Objetos com baixo acoplamento, alta coesão e facilitando a manutenção e refatoração do código, quando necessárias.

## Single Responsability Principle (SRP) [^srp]

*Princípio da Responsábilidade Única, em pt-BR.* 

Este postulado define o seguinte:

> Uma classe deve ter um, e somente um, motivo para mudar.

Dizemos que a classe deve ser coesa. Em outras palavras, ela deve ter uma *única* responsabilidade.
 
Por que uma classe ter mais de uma responsibilidade é um problema? 

Porque cada resposabilidade é algo passível de sofrer mudanças, e quanto mais responsabilidades nossa classe tiver, mais acoplada ela será, ou seja, mais impacto ela irá causar nas classes que dependem dela quando houver uma alteração em uma das responsabilidades e mais dificil será extendê-la, caso seja necessário. 

A título de exemplo, vamos analisar a seguinte classe:

```python
class Server: 

	def create_connection(self):
		pass

	def check_connection(self):
		pass

	def close_connection(self):
	    pass

	def send_package(self):
	    pass

	def receive_package(self):
		pass
	
```

Analisando a classe acima, percebemos claramente que ela possui duas responsabilidades: uma relacionada a conexões (criar, destruir e checar) e outra relacionado ao gerenciamento de pacotes de dados (envio e recebimento). Desse modo, todas as classes que herdarem dela, também receberão esses dois comportamentos não relacionados. Usando o `Single Responsability Principle` podemos separar a classe em duas outras classes, cada uma tratando adequadamente de sua própria responsabilidade:

```python
class ConnectionManager:
	"""Gerencia apenas a conexao"""

	def create_connection(self):
		pass

	def check_connection(self):
		pass

	def close_connection(self):
	    pass	
```

e 

```python
class PackageManager:
	"""Gerencia apenas o envio e recebimento de pacotes de dados"""

	def send_package(self):
	    pass

	def receive_package(self):
		pass	
```

O `Single Responsability Principle` é um dos princípios mais dificieis de serem aplicados, porque a definição da resposabilidade da classe pode variar de desenvolvedor para desenvolvedor, onde o mesmo define se algo esta ou não dentro do escopo da classe. Então, de modo a tornar mais fácil a aplicação deste princípio, devemos sempre ter em mente o domínio do problema que estamos tentando resolver e a arquitetura que iremos utilizar no design do software.

## Open-Closed Principle (OCP) [^ocp]

*Princípio do Aberto-Fechado, em pt-BR.*

Este postulado define o seguinte:

> Entidades de software devem ser abertas para extensão, mas fechadas para modificação.

Em outras palavras:

* "aberta para extensão": significa que o comportamento da classe pode ser extendido. Podemos fazer um método da classe se comportar de forma diferente de acordo com as mudanças exigidas pela aplicação ao qual ele pertence, ou para ir de encontro as necessidades de novas aplicações.
* "fechadas para modificação": o código fonte da classe é inviolável. Ninguém tem a permissão de alterar o código fonte original da classe para atender a novos requisitos da aplicação. O risco de alterar o código fonte da classe é que isso pode impactar no funcionamento de outras rotinas que dependem do comportamento dessa classe.

Com exemplo, vamos considerar a seguinte classe que representa as figuras geométricas quadrado e circulo.

```python
class Square:
	
	def __init__(self, lenght):
		super().__init__()
		self.lenght = lenght

```

e

```python
class Circle:
	
	def __init__(self, radius):
		super().__init__()
		self.radius = radius

```

Também temos uma classe que calcula a área e o perímetro dessas figuras e imprimem o resultado na tela:

```python
import math

class ShapeCalculator:

	def calc_area(self, shape):

		if isinstance(shape, Square):
			area = shape.lenght ** 2
			print(area)
			
		elif isinstance(shape, Circle):
			area = math.pi * shape.radius ** 2
			
	
```



que calcula o bonus de um funcionário, de acordo com seu cargo. Para isso vamos inicialmente definir a classe `Employee` (funcionario):

```python
class Employee:

	salary = 0
	role = ''
	
	def __init__(self, salary, role):
		super().__init__()
		self.salary = salary
		self.role = role
```

Em seguida, definimos a classe que calcula o bonus de cada funcionário de acordo com seu cargo:

```python


```

[^srp]: https://web.archive.org/web/20150202200348/http://www.objectmentor.com/resources/articles/srp.pdf
[^ocp]: https://web.archive.org/web/20150415215806/http://www.objectmentor.com/resources/articles/ocp.pdf
