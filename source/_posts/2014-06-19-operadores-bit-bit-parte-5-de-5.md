---
layout: post
title: "#5 - Operadores Bit-a-Bit: Operador SHIFT"
date: 2014-06-19T09:30:00-07:00
description: "Exemplos de operações lógicas usando o operador SHIFT"
main-class: 'c'
tags:
- c
- c++
- binario
- bit-a-bit
categories:
- "Operadores Bit-a-Bit"
introduction: "Exemplos de operações lógicas usando o operador SHIFT."
---

Neste ultimo tutorial sobre os operadores Bit-a-Bit, vamos falar sobre o operador `SHIFT`. O operador SHIFT serve para deslocarmos os bits de um número para esquerda ou para direita uma determinada quantidade de vezes. Embora pareça algo sem simples, esse deslocamento possui muitas aplicações. É o que veremos a seguir.

## SHIFT Esquerdo (<<)

O SHIFT Esquerdo (`<<`) desloca para esquerda todos os bits de um número um determinado número de vezes.

```cpp
unsigned char a = 5; // 00000101
unsigned char c = a << 1;
cout << c;
```
Valor de saída é `10` decimal ou `00001010` em binário.

Ao observarmos o valor de `c`, percebemos que ele dobrou. Esse detalhe está relacionado com uma das aplicações mais comuns do operador `SHIFT Esquerdo`: a multiplicação.

Toda vez que utilizamos o operador `<<` obtemos como resultado um valor equivalente ao operando multiplicado por 2 elevado ao número de deslocamentos, ou seja:

> x << n* é o mesmo que x \* 2^n

As operações de multiplicação e divisão são operações custosas para o processador, sendo uma das que levam mais tempo (ou ciclos) para serem completadas. Quando necessitamos executar operações de multiplicação por valores que são potência de 2, podemos usar o operador `<<` que é uma operação mais rápida que a multiplicação usando o operador `*` e nos devolve o mesmo resultado.

## SHIFT Direito (>>)

O SHIFT para direita (`>>`) desloca para direita todos os bits de um número um determinado número de vezes.

```cpp
unsigned char a = 5; // 00000101
unsigned char c = a >> 1;
cout << c;
```
A saída é `2` decimal ou `00000010` em binário.

Assim como o SHIFT Esquerdo, o `SHIFT Direito` pode realizar operações aritméticas, porém neste caso ele realiza a divisão (inteira) do operando por uma potência de 2. No exemplo acima podemos perceber que a variável c recebeu o parte inteira da divisão de `5` por `2^1`.

> x >> n* é o mesmo que x / 2^n

O operador SHIFT ainda possui diversos exemplos de uso, então não deixe de procurá-los.

Espero que essa série de tutoriais tenha lhe ajudado a entender mais sobre essas ferramentas interessante s que são os operadores Bit-a-Bit.

Obrigado por ler! Até o próximo post.
t+
