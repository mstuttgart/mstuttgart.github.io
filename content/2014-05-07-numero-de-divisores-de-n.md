Title: Encontrando os divisores de n
Date: 2014-05-07T20:21:00-07:00
Category: Algoritmo
Tags: Java, Tutorial, C++, Programação, Algoritmo
Author: Michell Stuttgart
Summary: Algoritmo que imprime todos os divisores de um dado número inteiro fornecido pelo usuário.


Nesta postagem, vamos aprender a criar um algoritmo que imprime todos os divisores de um dado número **n**.

Um dado valor **p**, onde **p** diferente de **zero**, é chamado divisor de **n** se o resultado da divisão de **n** por **p** resultar em um quociente inteiro e resto **zero**. Simplificando...

#### Exemplo

A divisão 6/2 possui quociente 3 e resto 0\. Desse modo, temos:

* O dividendo n é 6;
* O divisor p é 2;
* O quociente q é 3;
* O resto r é 0;

Em outras palavras, podemos dizer que:

```
**q \* p + r = n => 3 * 2 + 0 = 6**.
```

Seguindo outro exemplo:  7/2 possui quociente 3 e resto 1\.  

Com os exemplos acima, podemos verificar que se um número **n** é divisivel por **p**, o resto da divisão de **n** por **p** é nulo. Entendido esse conceito, basta passa-lo para o código.

```cpp
#include <iostream>
using namespace std;

int main(){

    int n, resto;
    cout << "Digite o valor de n: ";
    cin >> n;

    // Percorremos todo os numeros de 1 a n,   
    // verificando quais sao divisiveris por n  
    for(int i = 1; i <= n; i++){  

        // Calculamos o resto da divisao   
        // de n por i, sendo que i vai de 1 a n  
        resto = n%i;

        // Se o resto for nulo (0), i e divisor de n.   
        // Imprimos o valor.
        if(resto == 0)
        	cout << i << " ";
    }
    cout << endl;  
    return 0;  
}
```

É isso. Até mais pessoal.
