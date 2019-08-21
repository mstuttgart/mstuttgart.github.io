---
layout: post
title: "#2 Operadores Bit-a-Bit: Operador OR"
date: 2014-06-05T11:19:00-07:00
description: "Exemplos de operações lógicas usando o operador OR"
main-class: 'c'
tags:
- c
- c++
- binario
- bit-a-bit
categories:
- "Operadores Bit-a-Bit"
introduction: "Exemplos de operações lógicas usando o operador OR."
---

No tutorial anterior, realizamos um estudo sobre o `operador AND` e seus exemplos de uso. Se você ainda não leu, veja aqui. Agora vamos prosseguir estudando o `operador OR` e mostrando alguns exemplos de uso do mesmo.

## Operador OR

O `operador OR (|)` é um operador binário que executa uma operação `OR` com cada par de bits dos operandos. O bit resultante é `0` se os dois bits operandos forem 0; caso contrário o bit resultante é `1`.

Bit 1|Bit 2|Saída
:---|:-|:--
0|	0|	0
0|	1|	1
1|	0|	1
1|	1|	1

```cpp
unsigned char a = 5; // 00000101
unsigned char b = 9; // 00001001
unsigned char c = a | b;
cout << c;
```
A saída é `13` em decimal ou `00001101` em binário.

De maneira semelhante ao operador AND, o operador OR também pode ser usado para definir um valor específico para um determinado bit. Só que ao contrário do AND, que era usado para `"desligar"` um dado bit, o operador OR é usado para `"ligá-lo"`, ou seja, torna-lo igual a `1`.

### Exemplo

Vamos ligar o quarto bit do valor armazenado em a;

```cpp
unsigned char a = 5; // 00000101
unsigned char b = 0b00001000
unsigned char c = a | b;
cout << c;
```
A saída é `13` decimal ou `00001101` binário.

Observe que após essa operação, nós conseguimos `"ligar"` o quarto bit enquanto todos os outros bits continuam com seus valores iniciais.

É isso pessoal. Esse tutorial foi mais simples porque a maior parte dos detalhes e explicações eu já havia adicionado na parte 1.

Até o próximo tutorial.
