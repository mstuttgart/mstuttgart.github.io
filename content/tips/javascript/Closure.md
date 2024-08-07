Uma *closure* é uma função contruída com referências ao escopo externo a ela, o que permite acessar essas referências. Esse padrão permite que variáveis de um escopo externo seja utilizados dentro de um escopo que esteja alinhado a ele.

Em Jajavscript, cada funcão executada, bloco de código `{}` e script (global) possuem um objeto interno denominado como *Lexical Enviromnent*. Esse *Lexical Enviroment* possui duas propriedades principais:

- Um objeto que armazena todas as variáveis locais como propriedades, bem como o valor de *this*;
- Uma referência para outro *Lexical Enviromnent* mais externo a ele.

Diferente de outros objetos do Javascript, o *Lexical Enviromnent* existe apenas internamente. Não temos acesso a ele em nosso código de modo que possamos manipulá-lo diretamente.

## *Lexical Enviromnent* para variáveis

No caso de variáveis, elas nada mais são que propriedades do *Lexical Enviromnent*. Mudar seu valor significa mudar o valor dessas propriedades. Segue um exemplo de criação de variável no escopo do *script* (global).

Exemplo:

```javascript
/* Inicio da execucao: aqui e criado o Lexical Enviromnent do script

Lexical Enviromnent:
   - name: <uninitialized>
   - outer: null
*/

let name;
/*
Lexical Enviromnent:
   - name: undefined
   - outer: null
*/

name = 'Maria'
/*
Lexical Enviromnent:
   - name: 'Maria'
   - outer: null
*/
```

No exemplo acima, podemos perceber dois detalhes interessantes:

- A variável `name` já era conhecida pelo *scritp* antes de ser declarada. Como visto na sessão *hoisting*.
- A propriedade *outer* esta como *null* devido ao fato do escopo do código ser o escopo do *script* ou global.

## *Lexical Enviromnent* para funcões

Diferente do que ocorre com variáveis, a declaração de uma funçãio é totalmente inicializada.

Exemplo:

```javascript
/* Inicio da execucao: aqui e criado o Lexical Enviromnent do script

Lexical Enviromnent:
   - name: <uninitialized>
   - printName: function
   - outer: null
*/

let name;

function printName() {
    console.log(name);
}

/*
Lexical Enviromnent:
   - name: undefined
   - printName: function
   - outer: null
*/
```

Esse comportamente não ocorre para casos envolvendo expressões com funções, como por exemplo:

```javascript
let print = printName(name) { ... }
```

O *Lexical Enviromnent* do escopo interno dasd funções é criado somente no momento da execução das funcões, no inicio da sua chamada. Ainda seguindo o exemplo anterior, ao chamarmos a função `printName`, teremos o seguinte caso:

```javascript
/* Inicio da execucao: aqui e criado o Lexical Enviromnent do script

Lexical Enviromnent (global):
   - name: <uninitialized>
   - printName: function
   - outer: null
*/

let name = 'Maria';

function printName() {
    console.log(name);
}

/*
Lexical Enviromnent (global):
   - name: 'Maria'
   - printName: function
   - outer: null
*/

printName();
/*
Lexical Enviromnent (global):
   - name: 'Maria'
   - printName: function
   - outer: null

Lexical Enviromnent (printName):
   - outer: 'Lexical Enviromnent (global)'

*/
```

Ao tentar acessar a variável `name`, a função `printName` irá buscar a variável `name` em seu próprio *Lexical Enviroment*. Não a encontrado, ele irá buscar no *Lexical Enviromnent* externo imediato *outer*, e assim sucessivamente até o alcançar o *Lexical Envirmnent* global do *script*. Caso não encontre a variável, o Javascript retornará um erro.

Umam variável é atualizada no *Lexical Enviromnent* ao qual ela pertence.

Exemplo:

```javascript
function makeCounter() {
    let counter = 0;

    return function() {
        return counter++;
    }
}

let counter = makeCounter();

/*
Lexical Enviromnent (global):
   - counter: makeCounter()
   - makeCounter: function
   - outer: null

Lexical Enviromnent (makeCounter):
   - outer: 'Lexical Enviromnent (global)'
   - counter: 0
*/

console.log(counter());   // 1

/*
Lexical Enviromnent (counter()):
   - outer: 'Lexical Enviromnent (makeCounter)'
   - counter: 1
*/

console.log(counter());   // 2

/*
Lexical Enviromnent (counter()):
   - outer: 'Lexical Enviromnent (makeCounter)'
   - counter: 2
*/

console.log(counter());   // 3
```

## Garbage Collection

O Javascript possui um um *garbage collector* que remove todas as referências do *Lexical Enviromnent* de uma função após a mesma ser executada. Isso ocorre porque após a execução não há mais referências a ela. Entretanto, caso a função possua uma outra função aninhada a ela, o *Lexical Enviromnent* será mantido, porque o *Lexical Enviromnent* dessa função aninhada ainda faz referência ao *Lexical Enviromnent* da função superior a ela.

Exemplo:

```javascript
// Funcao simples
function printHello() {
    console.log('Hello!')
}

// Apos a execucao, o Lexical Enviromnent dessa funcao
// sera desalocado da memoria
printHello();


// Funcao com outra funcao interna
function makeCounter() {
    let counter = 0;

    return function() {
        return counter++;
    }
}

/* Apos a execucao, o Lexical Enviromnent de 'MakeCounter' 
   ainda permacera em memoria porque ele ainda e apontado pela
   propriedade 'outer' da funcao interna e ainda é referenciada
   variavel 'counter'
*/
let counter = makeCounter();

/*
Lexical Enviromnent (makeCounter):
   - outer: 'Lexical Enviromnent (global)'
   - counter: 0

Lexical Enviromnent (function interna):
   - outer: : 'Lexical Enviromnent (makeCounter)'
*/

counter();
```

# Referências

- [closure](https://javascript.info/closure)