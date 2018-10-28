---
layout: post
title: "#1 - Operadores Bit-a-Bit: Operador AND"
date: 2014-06-04T19:30:00-07:00
description: "Exemplos de operações lógicas usando o operador AND"
main-class: 'c'
tags:
- c
- c++
- binario
- bit-a-bit
categories:
- "Operadores Bit-a-Bit"
introduction: "Exemplos de operações lógicas usando o operador AND."
---

Operadores Bit-a-Bit são usados quando desejamos manipular diretamente os bits de um determinado número. Seu uso é muito fundamental em aplicações onde precisamos lidar diretamente com bits, como aplicações envolvendo hardware (Arduino, por exemplo) e até mesmo emuladores. Os exemplos estão em C++, mas podem ser facilmente adaptados para outras linguagens. Para fins de organização, pretendo dividir os tutoriais em 5 partes, cada um deles abordando um operador (AND, OR, XOR, NOT e SHIFT) e mostrando exemplos de uso.

Para se trabalhar com os operadores bit-a-bit, nossos dados devem ser valores numéricos, não-negativos e inteiros. As variáveis devem ser do tipo unsigned, como por exemplo, unsigned short ( 16 bits ) e unsigned char (8 bits ou 1 byte), dependendo do número de bits que você precisar.

## Operador AND

O operador `AND (&)` é um operando binário que executa uma operação AND com cada par de bits dos operandos. O bit resultante é 1 se os dois bits operandos forem 1; caso contrário o resultante é 0.

Bit 1	|Bit 2|Saida
:---:|:-:|:--:
0|0|0
0|1|0
1|0|0
1|1|1

```cpp
unsigned char a = 5;   // 00000101
unsigned char b = 9;   // 00001001
unsigned char c = a & b;
cout >> c
```

Saída: `1` ou `00000001` em binário.

O operador AND também pode ser usado quando desejamos verificar se um determinado bit de um operando é 0 ou 1.  No exemplo abaixo, vamos verificar se o terceiro bit do valor armazenado em a é 0 ou 1.

```cpp
unsigned char a = 5;   // 00000101
unsigned char b = 4;   // 00000100
unsigned char c = a & b;
cout >> c
```
Saída: `4` ou `00000100` em binário.

Porque usamos o valor 4 para a variável `b`?

Note que o valor 4 possui todos os seus bits iguais a 0 com exceção do terceiro bit, que é o que desejamos. Sempre devemos escolher um número que possua o bit `1` na posição dos bit(s) que desejamos verificar se é `0` ou `1`. Se o nosso objetivo fosse encontrar o valor do quarto bit de a, deveríamos fazer

```cpp
unsigned char a = 5; // 00000101
unsigned char b = 8; // 00001000
unsigned char c = a & b;
cout >> c
```

Saída: `8` ou `00000000` em binário.

Com exemplo acima percebemos que, se o o digito em questão for `1`, o resultado de `a & b` será igual a ao valor armazenado em `b`. Se o digito for `0`, o resultado da operação `a & b` será `0`.

Outra uso do operador `AND` é quando desejamos "desligar", ou seja, tornar igual a `0` um determinado bit do número.

```cpp
unsigned char a = 5; // 00000101
```

Vamos supor que desejamos desligar o terceiro bit de a. Basta realizarmos uma operação `AND` com um operando que possua o valor `0` no digito que desejamos "desligar" e `1` nos demais bits.

### Exemplo

```cpp
unsigned char b = 251; // 11111011
```
Realizando o `AND`, teremos:

```cpp
a = a & b;
cout >> a;
```
Saida: `1` ou `0000 0001` em binário.

Como podemos observar, conseguimos "desligar" o terceiro bit do valor de `a`.
Uma pergunta que pode surgir é como saber que valor usar em `b`. No exemplo acima utilizamos `b = 251`, mas como sabemos que esse valor daria certo. A ideia aqui é se basear na representação binária e não na decimal, ou seja, você deve encontrar um valor em binário que satisfaça a operação que você deseja (no nosso caso, o valor `11111011`).

Uma maneira de deixar esse raciocínio mais intuitivo é usar um valor diretamente na base binária ao invés da base decimal. No C++, a operação que fizemos logo acima ficaria assim:

```cpp
unsigned char b = 0b11111011; // 251
a = a & b;
cout >> a;
```
Saida: `1` ou `00000001` em binário.

Lembrando que o número de bits não deve ultrapassar a capacidade do tipo da variável. Acima utilizamos `unsigned char` que tem capacidade para `8 bits`. Se armazenarmos um valor que necessita de mais de 8 bits, esse valor será truncado (quebrado) para que possa ser armazenado em 8 bits. Provavelmente você terá uma valor errado como saída, então sempre se atente a isso, ok?

Com este tutorial, tentei mostrar algumas exemplos de uso do operador AND. É claro que existem muitos outros caso de uso, mas tentei focar aqui no mais básico.

É isso pessoal! Obrigado por ler e até o próximo *post*!
