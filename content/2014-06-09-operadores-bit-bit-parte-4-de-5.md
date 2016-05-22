Title: Operadores Bit-a-Bit (Parte 4 de 5): Operador NOT
Date: 2014-06-09T20:31:00-07:00
Category: C++
Tags: c, c++, algoritmo, tutorial, operador bit-a-bit, binario
Author: Michell Stuttgart
Summary: Exemplos de operações lógicas usando o operador NOT

Mais um capítulo do nosso tutorial sobre operadores lógicos e operações bit-a-bit.
Hoje veremos o operador `NOT`.

#### Operador NOT

O operador `NOT (~)`, talvez seja o mais simples de todos. Diferente dos outros operadores Bit-a-Bit, o operador NOT opera apenas sobre um operando, invertendo o estado de cada bit, ou seja, se o bit for `1` ele será mudado para `0`, e vice-versa.

Bit|Saída
:---:|:-:
0|1
1|0

#### Exemplo

Abaixo temos um exemplo de uso do operador `NOT`.

```cpp
unsigned char a = 5; // 00000101
unsigned char c = ~a;
cout << c;
```
Saída igual a `250` decimal ou `11111010` binário.

Um dos mais comuns usos do operador NOT é para encontrar o `complemento de 2` de um número binário. Em um número binário de 8 bits conseguimos representar valores de `0` a `255` (`11111111` em binário), considerando que estamos trabalhando com número absolutos, ou seja, maiores ou iguais a zero . Entretanto, quando desejamos representar valores negativos e positivos usando valores binários devemos usar o complemento de 2. Desse modo, o nosso intervalo de representação de 8 bits diminui o valor positivo máximo, mas por outro lado, conseguimos representar números negativos. Sendo assim nossos valores vão de `-128` a `127`.

#### Exemplo 2

Para encontrarmos o `complemento de 2` (o valor negativo) de um número usando o operador NOT, seguimos os seguintes passos:

```cpp
unsigned char a = 5; // 00000101
unsigned char c = ~a + 1;
cout << c;
```
Saída igual a `-5` decimal ou `11111011` binário.

Os números em complemento de 2, quando são negativos, sempre possuem seu bit mais significativo (bit mais à direita) com o valor `1`. A principal vantagem de usarmos essa técnica é que as regras para as operação de soma e de subtração são as mesmas, ou seja, se desejamos subtrair um número `b` de outro número `a`, basta simplesmente somar-lo ao complemento de 2 de `b`.

É isso pessoal. Até o próximo tutorial.
