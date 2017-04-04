Title: C++ - Encontrando o maior valor de um vetor
Date: 2014-01-17T20:21:00-07:00
Category: Algoritmo
Tags: Java, Tutorial, C++, Programação, Algoritmo
Author: Michell Stuttgart
Summary: Algoritmo a seguir encontra o maior valor entre um conjunto de valores armazenados em um vetor

Iniciando as nossas postagens, o algoritmo a seguir encontra o maio valor entre um conjunto de valores armazenados em um vetor.
Os valores são armazenados em um vetor de inteiros e, em seguida, damos início ao processo de procura de maior valor.
A técnica utilizada é muito simples e pode ser adaptada para encontrarmos o menor valor e até mesmo para realizarmos a ordenação dos valores presentes no vetor em ordem crescente ou decrescente.

A seguir temos o algoritmo em C++, mas pode facilmente ser adaptado para outras linguagens.

```cpp

#include <iostream>
using namespace std;

int main( int argc, char** argv ){

	   // Vetor com os valores que desejamos ordenar
	   int vNumeros[] = {2,3,8,7,5};

	   // Variavel que recebera o maior valor
	   int maiorValor;

	   // Inicializamos maiorValor com o primeiro numero do vetor
	   maiorValor = vNumeros[0];

	   for( int j = 1; j < n; j++ ){

				// Aqui esta a parte importante!
			   if( vNumeros[j] > maiorValor )
				    maiorValor = vNumeros[j];


		}//for

		cout << "\nO maior numero e: " << maiorValor << endl;
		return 0;
}
```

Inicialmente, inicializamos a variável maiorValor com o primeiro valor do vetor. Fazemos isso porque ao percorremos o vetor, o começamos do primeiro valor, ou seja, do índice 0 do vetor.

```cpp
maiorValor = vNumeros[0];
```

Em seguida, utilizamos o for para percorrermos o vetor a partir da segunda posição, ou seja, do índice 1.

```cpp
for( int j = 1; j < n; j++ ){

	  if( vNumeros[j] > maiorValor )
		   maiorValor = vNumeros[j];

}//for
```

Lembre-se que o maiorValor está com o valor de vNumeros[0], ou seja, 2.
Para cada posição do vetor, verificamos se o seu valor é maior que maiorValor. Se for, atualizamos a variável maiorValor com este novo valor.
Seguindo esse algoritmo, quando terminarmos de percorrer o vetor, teremos na variável maiorValor, o maior valor do vetor, ou seja, o valor 8.
Vale ressaltar que este algoritmo pode ser utilizado com outros tipos de valores, como floats, doubles, e com strings.

Até o próximo tutorial.
