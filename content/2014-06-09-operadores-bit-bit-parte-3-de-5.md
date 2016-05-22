Title: Operadores Bit-a-Bit (Parte 3 de 5): Operador XOR
Date: 2014-06-09T19:35:00-07:00
Category: C++
Tags: c, c++, algoritmo, tutorial, operador bit-a-bit, binario
Author: Michell Stuttgart
Summary: Exemplos de operações lógicas usando o operador XOR

Continuando a nossa série de tutoriais, hoje veremos o operador XOR (`^`) ou como é conhecido, `OU-Exclusivo`.

#### Operador XOR

Como o próprio nome sugere, o `XOR` é um tipo especial de operação OR.
`XOR (^)` é um operando binário que executa uma operação `XOR (ou-exclusivo)` com cada par de bits dos operandos. O bit resultante é `1` apenas se os dois bits operandos forem diferentes; caso contrário o resultante é `0`.

Bit 1|Bit 2|Saída
:---|:-|:--
0	|0|	0
0	|1|	1
1	|0|	1
1	|1|	0

#### Exemplo

O `operador XOR` utilizado quando desejamos uma verificar se cada um dos bits de um par de operandos são realmente diferentes.

```cpp
unsigned char a = 5; // 00000101
unsigned char b = 9; // 00001001
unsigned char c = a ^ b;
cout << c;
```
A saída é `12` decimal ou `00001100` binário.

Eu não encontrei exemplos mais genéricos de uso do XOR. Se você, leitor, souber algum não deixe de postar nos comentários.

Obrigado por ler e até o próximo tutorial.
