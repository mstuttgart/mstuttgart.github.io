#javascript #language

Javascript é uma linguagem de auto nível que segue o padrão ECMAScript. Ela é fracamente tipada e possui tipagem dinâmica, Orientação Objetos baseada em Protótipos e funções como cidadão de primeira classe. Suporta os paradigmas de programação imperativo, funcional e orientada a eventos.

## Características

### Fracamente Tipada

Uma linguagem **fracamente tipada** aceita que valores de tipos diferentes sejam atribuídos a uma mesma variável.

```javascript
var a = 'exemplo'

a = 10 // não causa erro
```

Em linguagens **fortemente tipadas** (como C, C++ e Java), ocorreria um erro no codigo acima. Pois um variável que foi declarada com *string*, seria permitido receber apenas valores do tipo *string*.

### Tipagem Dinâmica

Uma linguagem pode possuir tipagem *Estática* ou *Dinâmica*.
****
Na **Tipagem Estática**, quando o tipo da valores que a variável irá receber é determinado na declaração da variável (como ocorre no C, C++ e Java).

Na **Tipagem Dinâmica**, o tipo de valor da variável é determinado somente **no** momento que um valor é atribuído a ela.

Podemos **usar** o comando *typeof* para determinar o tipo do valor contido na variável.

> typeof value

Exemplo:

```javascript
var a = 'exemplo'
typeof a    // string

a = 10
typeof a    // number
```

## Number [^number]

Em Javascript, o tipo **Number** é uma função e representa tanto números inteiros (Integer) como números de ponto flutuante (Float). Ele apresenta várias operações muito úteis, como no exemplo a seguir.

Exemplo:

```javascript
// Exemplo de Numbers
typeof -5    // number
typeof 10    // number
typeof 2.5   // number

// Determinar se um numero é ou não inteiro
Number.isInteger(2.6)   // true
Number.isInteger(15)    // false

// Delimitar o numero de casas decimais
(3.1415).toFixed(2)    // '3.14' 

// Converter valor numerico para string
(3.1415).toString()    // '3.1415'

// Converter valor numerico para string, mas para base binária (2)
(7).toString(2)    // '111'
```

### Números especiais

Javascript possui alguns valores de números especiais que normalmente não encontramos em outra linguagem: `NaN` e `Infinity`.

#### NaN

O valor `Nan` (do inglês, *Not a Number*) é produzido quando o resultado de uma operação retorna um valor que não é um *Number*.

Exemplo:

```javascript
var Number('hello')   // NaN -> o número não pode ser parseado
var Number('12a')     

var Math.sqrt(-4)  // NaN -> operação falhou raiz de numero negativo)

var NaN + 4   // NaN
```

**Importante**:

> `NaN` é o único valor que não ígual a  si mesmo. 

```javascript
NaN === NaN   // false

typeof NaN  // Number
```

Essa peculiaridade vem da regra [IEEE](https://en.wikipedia.org/wiki/IEEE_754) utilizada para operações com ponto flutuante. Isso ocorre devido a natureza dos valores que o `NaN` pode representar.

```javascript
var raizA = Math.sqrt(-4)   // NaN
var raizB = Math.sqrt(-25)  // NaN

raizA === raizB  // false
```

Para realizar a verificação se um determinado valor é `NaN`, ddevemos utilizar a função `isNaN`:

```javascript
isNaN('12a')  // true
isNan(4)      // false
```

#### Infinity

É considerado o maior "número" da linguagem, assim como `-Infinty` é considerado o menor, com exceção do `NaN`. De modo a verificar se um *Number* assume um dos valores `Infinity`, utilizamos a função `isFinite`.

```javascript
isFinite(1000)      // true
isFinite(Infinity)  // false
isFinite(NaN)       // false
```

### Operações aritméticas

O Javascript apresenta alguma excentricidades em relação ao *Number* que devem ser observadas.

#### Divisão por zero

Diferente de outras linguagens, o Javascript não irá acusar erro ou disparar uma exceção quando ocorrer uma divisão por zero. Ao invés disso, a linguagem possui o tipo **Infinity**, um tipo especial para representar valores infinitos.

```javascript
a = 5/8   // Infinity
```

#### Operações com tipos diferentes

Por ser fracamente tipada, o Javascript permite alguns tipos de operações envolvendo valores de tipos diferentes.

```javascript
a = '10' / 2    // 5
b = '10' * 2    // 10

c = '10,2' * 2    // Nan (indefinido, por causa da virgula, o JS nao sabe que é um número)
```

#### Chamando funções diretamente

Quando desejado podemos chamar as funções diretamente pelo Number, sem precisar guardar o valor em uma variável primeiro.

```javascript
10.toString()    // Uncaught SyntaxError: Invalid or unexpected token

(10).toString()    // '10'
```

#### Operações com números de ponto flutuante

Em operações com números de ponto flutuante, o Javascript sempre irá retornar o número máximo de casas decimais, seguindo o padrão IEEE [^IEEE].

```javascript
var soma = 0.1 + 0.7    //0.7999999999999999
```

### Math [^math]

O objeto **Math** nos permite executar tarefas matemáticas, como raiz quadrada, elevar um número a determinada potência, seno e cosseno de um determinado angulo e determinar o máximo e mínimo de um determinado conjunto de valores, entre outras funções. 

**Math** não é um construtor, então todos os metodos do objeto podem ser chamados sem criá-lo (semelhante a funções estática de outras linguagens).

```javascript
Math.PI    // valor PI

Math.sqrt(4)    // raiz quadrada de 4.

Math.pow(2, 3)    // 2^3

Math.max(2, 1, 5, 4)    // 5 -> maior valor de um conjunto de valores

Math.floor(3.1415)    // 3 -> arredondamento para o inteiro anterior
Math.ceil(3.1415)     // 4 -> arredondamento para o inteiro superior
```

## String [^string]

Em Javascript, uma *string* pode ser representada tanto por aspas duplas quanto por aspas simples. A *string*  é tratada como uma lista, isso nos permite realizar buscas e cortes na mesma, conforme a necessidade.

Exemplos:

```javascript
text = 'Javascript'

// Retorna o caracter de uma determinada posicao
text.charAt(0)    // 'J'
text.charAt(20)    // '' . string vazia quando o indice nao existir na string

// Retorna o indice de um determinado caracter
text.indexOf('c')    // 5 
text.indexOf('a')    // 1 retorna a primeira ocorrencia do caracter 'a'

// Retorna substring a partir de um intervalor de indices
text.substring(1)    // 'avascript' . Do indice 1 até o final da string
text.substring(0, 3)    // 'Java'. Do indice 0 ao 3

// Separa uma string a partir de um caracter delimitador
'Javascript, Python, Go'.split(',')    // ['Javascript', 'Python', 'Go']

// Busca dentro da string (pode ser utilizado Regex)
'Javascript, Python, Go'.search('Python')    // 12. Indice da primeira ocorrencia que coincide coma busca
```

### Interpolação e Concatenação de strings

O Javascript, assim como outras linguagens, também apresenta recursos para *interpolação* e *concatenação* de strings. **Interpolação de Strings** seria utilizar uma string como *template*,  onde essa string possui variaveis nas partes de texto que valores reais durante o processo de interpolação.

Exemplo  *concatenação*:

```javascript
text = 'Javascript'

// Concatenacao utilizando a funcao 'cocat'
text.cocat(' é ', ' nota', ' 10!')    // 'Javascript é nota 10!'

// Concatenacao usando operador +
text = text + ' é ' + ' nota ' + ' 10!'
```

Exemplo *interpolação*:

```javascript
var nota = 10

// Transformamos a string em uma template string, onde a chave #{nota} recebe
// o valor da variavel 'nota'
text = `Javascript é nota ${nota}!`    // 'Javascript é nota 10!'
```

O Javascript tentará executar tudo o que esta dentro da chave `${}`. Desde a execução de funções até operações aritméticas.

```javascript
text = `2 + 3 = ${2 + 3}`    // '2 + 3 = 5'
```

## Boolean [^boolean]

Em Javascript, os valores booleanos são representados por *true* e *false*. Como ocorre em algumas linguagens, alguns valores também podem representar *true* ou *false* quando utilizados em determinados contextos. 

Os valores a seguir são considerados *true*:

- `true`,
- `1`: ou qualquer inteiro diferente de zero,
- `' '`: string com pelo menos um caracter (mesmo que seja espaço) ,
- `Infinity`: palavra reservada,
- `[]`: array vazio,
- `{}`: objeto literal.

Os valores a seguir são considerados *false*:

- `false`,

- `0`: valor inteiro,

- `null`: palavra reservada,

- `undefined`: palavra reservada,

- `NaN`: palavra reservada (*Not a Number*).
 
  ## Declaração de variáveis

**let** e **const** são substitutos para **var**, introduzidos no [ECMAScript6](https://www.w3schools.com/js/js_es6.asp) e proveem escopo de block para o Javascript. Antes do ES6 (2015), o JavaScript possuia apernas *escopo global* e *escopo de função*.

### var[^var]

As variáveis definidas com *var* possuem as seguintes propriedades:

- Devem ser declaradas antes do uso
- Podem ser redeclaradas
- Possuem escopo global ou de função

ECMAScript6 (ES6 / JavaScript 2015) encoraja a declaração de varáveis com **let**, de modo a evitar alguns possíveis problemas. O primeiro diz respeito ao escopo.

Exemplo:

```javascript
var n = 5

{
    var n = 10
}

console.log(n)    // 10
```

No exemplo acima, vericamos que o valor impresso nas duas situações foi `10`. Isso ocorre porque *var* permite a redeclaração de variáveis e redeclar uma variável dentro de um block iŕa redeclará-la fora do bloco. Sendo assim, o Javascript intepretou que as duas variáveis `n` eram na verdade, a mesma variável. Por isso o valor impresso foi o valor da última atribuição.

Outro inconveniente de `var` é o fato dele permitir o acesso externo de variáveis declaras dentro do bloco `{}`.

Exemplo:

```javascript
{
    var nome = 'Maria' 
}

console.log(nome)    // 'Maria'
```

Essa liberdade de acesso independente do escopo pode atrapalhar a legibilidade de código e causar erros de inconsistência no estado das variáveis (valor armazenado pela mesma), algo muito importante em linguagens de paradigma funcional.

### let [^let]

As variáveis definidas com *let* possuem as seguintes propriedades:

- Devem ser declaradas antes do uso
- Não podem ser redeclaradas
- Possuem escopo de bloco `{}`

O uso de *let* resolve os incoveniêntes apresentado pelo uso do *var*. 

Exemplo:

```javascript
let n = 5

{
    let n = 10
}

console.log(n)    // 5 (o valor foi mantido)
```

O *let* não permite a redeclaração de variáveis em um mesmo escopo de bloco `{}`. Sendo assim, o Javascript entende que, salvo terem o mesmo nome, as varáveis `n` são variáveis diferentes.

```javascript
{
    let nome = 'Maria'
    let nome = 'Pedro' // SyntaxError: Identifier 'nome' has already been declared
}
```

O *let* também não permite o acesso fora do escopo de bloco onde ele foi declarado.

Exemplo:

```javascript
{
    let nome = 'Maria' 
}

console.log(nome)    // ReferenceError: nome is not defined
```

A tentativa de acesso resultará em um `ReferenceError` indicando que a variável `nome` não foi definida.

### const [^const]

As variáveis definidas com *const* possuem as seguintes propriedades:

- Devem ser declaradas e inicializas com um valor antes do uso
- Não podem ser redeclaradas
- Não podem sofrer reatribuição
- Possuem escopo de bloco `{}`

Exemplo:

```javascript
const PI = 3.1414   // Declaramos a constante PI e a inicializamos
PI = 3.14           // TypeError: Assignment to constant variable.

const PI = 3.14     // SyntaxError: Identifier 'PI' has already been declared
```

Sempre declaramos uma variável com *const* quando sabemos que a *referência* ao qual ela aponta não deve mudar. Recomenda-se o uso de *const* quando declaramos:

- Um novo *array*
- Um novo *object*
- Uma nova *Function*

O *const* não define um uma valor constante. Ela define um referência constante a uma valor. Sendo assim, não podemos reatribuir outro *object* a uma constante, mas podemos alterar os valores do mesmo.

Exemplo:

```javascript
const pessoa = {nome: 'Maria'}

pessoa.nome = 'Joao'       // conseguimos alterar o atributo do object

pessoa = {nome: 'Pedro'}  // TypeError: Assignment to constant variable.
```

### Hoisting [^hoisting]

**Hoisting** é um comportamento padrão do Javascript de mover todas as declaração para o topo do escopo atual (para o topo do *script* ou da função). Isso permite que variáveis possam ser utilizadas antes de serem declaradas.

```javascript
n = 10

.
. // codigo qualquer
.

var n
```

É a mesma coisa que:

```javascript
n = 10
var n

.
.  // codigo qualquer
.
```

O Javascript somente executa o *hoisting* para declarações, não inicializações:

```javascript
var a = 10
var b = 2

console.log(a + b)  // 12
```

É diferente de:

```javascript
var a = 10

console.log(a + b)  // b is undefined

var b = 2
```

O Javascript irá indicar que `b` esta `undefined`. Isso ocorre porque somente a declaração `var b`, e não atribuição `= 2`, sofreu *hoisting* para o topo do *script*. Em outras palavras, ocorre o comportamento semelhante ao seguinte código:

```javascript
var a = 10    // inicializa 'a'
var b         // declara 'b'

console.log(a + b)  // 'b' is undefined

b = 2   // somente aqui atriuimos um valor a 'b'
```

#### Comportamento para o *let* e *const*

Variáveis declaradas com *let* e *const* sofrem *hoisting* para o topo do bloco, mas não são inicializadas. Isso significa que o bloco sabe da existência das variáveis, mas não pode usá-las até que as mesmas sejam declaradas.

Exemplo:

```javascript
{
    nome = 'Maria'
    let nome   // ReferenceError: Cannot access 'nome' before
}

{
    PI = 3.14
    const PI  // SyntaxError: Missing initializer in const declaration
}
```

#### Boas práticas

O funcionamento do *hoisting* pode causar erros dificeis de depurar caso não saibamos do seu funcionamento e resultar em estados inesperados nas variáveis. De modo a evitar o surgimento de bugs e melhorar a legibilidade do código, é uma boa prática *sempre* declarar as variáveis no inicio de cada escopo e evitar usar variaveis que ainda não foram declaradas (o uso de *let* e *const* evita isso).

### Null e Undefined

São valores denominados ***nullish***.

**Undefined** é utilizado pelo Javascript quando temos uma variável que não foi inicializada com nenhum valor. 

```javascript
var n
console.log(n)    // sera retornado o tipo undefined
```

**Null** é utilizado quando queremos evitar que uma variável fique como *undefined* mas não desejamos atribui nenhum valor a ela.

```javascript
var n = null
console.log(n)    // sera retornado null
```

O Javascript utiliza *cópia por referência* para atribuição de valores. O mesmo não ocorre para tipos primitivos, onde é utilizada a *cópia por valor*.

```Javascript
// Object simples
var a = {nome: 'João'}

// Na atribuicao de objetos, ocorre a copia por referencia.
var b = a

/* 
Como as variáveis 'a' e 'b' apontam para o mesmo endereco de memoria, se alterarmos uma propriedade de 'b', o conteúdo de 'a' tambem sera alterado
*/
b.nome = 'Pedro'

console.log(b.nome)    // 'Pedro'
console.log(a.nome)    // 'Pedro'
```

O **null** também é util quando desejamos reinicializar o valor de um objeto.

```javascript
var a = {nome: 'João'}

a = null
console.log(a)    // null
```

## Operadores [^operators]

Existem diferentes tipos de operadores em Javascripts e esses são separados nas seguintes categorias:

- Operadores Aritméticos
- Operadores de Atribuição
- Operadores de Comparação
- Operadores Lógicos
- Operadores Condicionais
- Operadores de Tipo

### Operadores Aritméticos

São utilizados para executar operações aritméticas de números.

| Operador | Descrição                                                          |
| -------- | ------------------------------------------------------------------ |
| +        | Adição                                                             |
| -        | Subtração                                                          |
| *        | Multiplicação                                                      |
| **       | Exponenciação ([ES2016](https://www.w3schools.com/js/js_2016.asp)) |
| /        | Divisão                                                            |
| %        | Modulo (resto da divisão)                                          |
| ++       | incremento                                                         |
| --       | Decremento                                                         |


### Operadores de Atribuição

São utilizados para atribuir valores as variáveis.

Exemplo:

```javascript
x += y    // x = x + y
x++       // x = x + 1

x -= y    // x = x - y
x--       // x = x - 1

x *= y    // x = x * y
x /= y    // x = x / y

x %= y    // x = x % y
x **= y   // x = x ** y
```

#### Atribuição Via Desestruturação

No Javascript, uma **atribuição via desestruturação** (do inglês, *destructuring assignment*), é uma expressão que permite extrair dados de *arrays* ou *objects* em variáveis distintas.

Exemplo com *object*:

```javascript
const pessoa = {
    nome: 'Maria',
    idade: '20'
}

// destructuring padrao
var {nome, idade} = pessoa

console.log(nome)    // 'Maria'
console.log(idade)   // 20

// pessoa nao possui o atributo 'curso', entao 'curso' recebe um valor padrao
var {nome, idade, curso='Enfermagem'} = pessoa

console.log(nome)    // 'Maria'
console.log(idade)   // 20
console.log(curso)   // 'Enfermagem'

// destructuring ignorando valores (no caso, a propriedade 'idade')
var {nome, , curso='Enfermagem'} = pessoa

console.log(nome)    // 'Maria'
console.log(curso)   // 'Enfermagem'
```

### Operadores de Tipo

| Operador   | Descrição                                                     |
| ---------- | ------------------------------------------------------------- |
| typeof     | Retorna o tipo da variável                                    |
| instanceof | Retorma `true` se um objeto é uma instância de um tipo objeto |

Exemplo:

```javascript
const langs = ['Javascript', 'Python', 'Go', 'C']

console.log(langs instanceof Array)    // true
console.log(langs instanceof Object)   // true
console.log(langs instanceof Number)   // false
```

### Operadores de Manipulação de Bits

São operadores de *bits* utilizados para trabalhar com numeros de 32 bits. Qualquer valor númerico na operação é convertido em um número de 32 bits. O resultado é reconvertido para um `Number`.

| Operador | Descrição            |
| -------- | -------------------- |
| &        | AND                  |
| \|       | OR                   |
| ~        | NOT                  |
| ^        | XOR                  |
| <<       | left shift           |
| >>       | right shift          |
| >>>      | unsigned right shift |

## Estruturas de Controle

As estruturas de controle no Javascript são semelhantes ao encontrado em outras linguagens. 

### Estrutura IF/ELSE [^ifelse]

Possui estrutura semelhante ao de outras linguagens com C e Java.

Exemplo:

```javascript
if (condicao_1) {  
    //  codigo qualquer 
  
} else if (condicao_2) {
    // codigo qualquer

} else {  
    // codigo quanlquer
}
```

Se o bloco de código do `IF` possuir apenas uma linha, podemos omitir as chaves `{}`.

```javascript
if (condicao)
    console.log('A')

    console.log('B')
```

No exemplo acima, como não utilizamos chaves `{}` para o `IF`, o Javascript interpreta que o bloco de código do `IF` contem apenas a linha com o comando `console.log('A')`. Sendo assim, a *string* `'A'` será impressa apenas se `condicao` for verdadeira. Por outro lado, a *string* `'B'` sempre será impressa, independente do valor.

### Estrutura Switch [^switch]

Funciona também de modo semelhate ao de outras linguagens.

Exemplo:

```javascript
switch(expressao) {  
  case x:  
    // codigo qualquer
    break;  
  case y:  
    // codigo qualquer
    break;  
  default:  
     // codigo qualquer
}
```

É uma boa prática sempre utilizar o `default`, de modo a garantir o tratamento para todos os possíveis resultados de `expressao`.

### Estrutura While e Do While [^while]

Segue o mesmo funcionamento do *while* e do *do while* presente em outras linguagens.

Exemplo:

```javascript
while (condicao) {  
    // codigo qualquer
}
```

Exemplo: 

```javascript
do {  
    // codigo qualquer
}  
while (condicao)
```

### Estrutura FOR e FOR/IN

O Javascript nos fornece dois tipos de estrutura de repetição **for**.

- `for`: percorre um bloco de código, um determinado número de vezes. 
- `for/in`: percorre as propriedades de um objeto.
- `for/of`: percorre os valores das propriedades um objeto .

A seguir, temos alguns exemplos do uso da estrutura **for** , **for/in** e **for/of** e suas descrições.

#### FOR

O **for** comum, encontrado em outras linguagens com `C` e `Java`.  É utilizado para percorrer *arrays*.

Exemplo:

```javascript
const alunos = ['Maria', 'Joao', 'Pedro']

for (let i = 0; i < alunos.length; i++) {
    console.log(i, alunos[i])
}

// -> 0 'Maria'
// -> 1 'Joao'
// -> 2 'Pedro'
```

#### FOR/IN

É utilizado para percorrer as propriedades enumeradas de um objeto. No caso de *arrays*, temos o seguinte comportamento.

Exemplo:

```javascript
// Percorrendo um array
const alunos = ['Maria', 'Joao', 'Pedro']

for (let a in alunos) {
    console.log(a)
}

// 0
// 1
// 2
```

A variável `a` recebeu em cada interação, não o valor contido no *array*, mas o seu indice. O laço **for/in** interage sobre propriedades enumeradas de um objeto, na ordem original de inserção. 

Para *objects*, o **for/in** funciona retornando as propriedades dos objetos, e não seus valores.

Exemplo:

```javascript
// Percorrendo um object
const pessoa = {
    nome: 'Maria', 
    idade: 20
}

for (let p in pessoa) {
    console.log(`${p} = ${pessoa[p]}`)
}

//  -> nome = Maria
//  -> idade = 20
```

#### FOR/OF

O **for/of** foi introduzido no [ECMAScript 6 (2015)](https://www.w3schools.com/js/js_es6.asp) e é utilizado para interar através dos valores de objetos interaveis. Ele nos permite iterar através de estruturas de dados como *Arrays, Sets, Maps* e *Strings*.

Exemplo:

```javascript
// Percorrendo um array
const alunos = ['Maria', 'Joao', 'Pedro']

for (let a of alunos) {
    console.log(a)
}

// Maria
// Joao
// Pedro
```



Se tentarmos utilizar o **for/of** com um *object*, como no código a seguir:

```javascript
// Percorrendo um object
const Pessoa = {
    nome: 'Maria', 
    idade: 20
}

for (let p of Pessoa) {
    console.log(p)
}

// TypeError: Pessoa is not iterable
```

Isso ocorre porque o objeto `Pessoa` não implementa a propriedade que permite a iteração.

### Break e Continue

Ainda cobrindo a área de *loops*, temos dois comandos muito úteis:

- `break`: comando que "pula fora" do *loop*.
- `continue`: comando que "pula" uma iteração do *loop*.

Exemplo **break**:

```javascript
const alunos = ['Maria', 'Joao', 'Pedro', 'Mel']

for (let a of alunos) {

    // Se a primeira letra do nome for 'P',saimos do loop
    if (a.charAt(0) == 'P') {
        break
    } else {
        console.log(a)
    }

}

// Saida do script:
// Maria
// Joao
```

No exemplo acima, percorremos o *array* de nomes, imprimindo cada um deles até encontrarmos um nome que começa com a leta `P`. Nesse caso, utilizamos o `break` para encerrar o *loop* **for**.

Exemplo **continue**:

```javascript
const alunos = ['Maria', 'Joao', 'Pedro', 'Mel']

for (let a of alunos) {

    // Se a primeira letra do nome for 'P',pulamos para o proximo item
    if (a.charAt(0) == 'P') {
        continue
    } else {
        console.log(a)
    }

}

// Saida do script:
// Maria
// Joao
// Mel
```

No exemplo acima, também percorremos o *array* de nomes, imprimindo cada um deles até encontrarmos um nome que começa com a leta `P`. Nesse caso, utilizamos o `continue` para pular para o próximo valor presente no *array*.

## Tratamento de Erros [^errors]

O tratamento de erros em Javascript possui as seguintes palavras chaves:

- `try`: define o bloco de código a ser executado (*obrigatório*)
- `catch`: define o bloco de código que irá tratar o erro (*obrigatório*)
- `finally`: define um bloco de código que será executado indeferente do resultado (*opcional*)
- `throw`: utilizado para disparar um erro criado pelo usuário.

Exemplo:

```javascript
function foo () {
    throw TypeError
}

.
.
.

try {
    foo()   // pode disparar mais de um tipo de expection
} catch (e if e instanceof TypeError) {
    // tratar o erro do tipo TypeError
} catch (e) {
    // tratar o erro default
} finally {
    // executa outro codigo
}
```

## Array [^array]

O *array* é utilizado para armazenar multiplos valores em uma unica variável. Funciona como uma lista e apresenta os métodos mais conhecidos desse tipo de estrutura de dados.

Exemplo:

```javascript
const lista = [2, 4.5, 'abc', 0]

// Consulta por indice
console.log(lista[0])   // 2

// Consulta por indice quando o indice nao existe
console.log(lista[4])    // undefined

// Consulta do comprimento do array
console.log(lista.length)    // 4

// Inseri um novo elemento ao final do array e retorna o novo comprimento do mesmo
lista.push('js')    // [2, 4.5, 'abc', 0, 'js'] - retorna 5

// Remove o ultimo elementro do array, retornado-o
lista.pop()    // 'js'

// Remove o primeiro elementro do array, retornado-o
lista.shift()    // 2

// Adiciona um ou mais elementos ao inicio do Array, retornando o novo comprimeiro do mesmo
lista.unshift('Python')  // ['Python', 4.5, 'abc', 0]

// Remove ou substitui um ou mais elementos do array em um determinada posicao. Retorna um Array com os objetos removidos

//
// splice(start=0, deleteCount, item1, item2, itemN)
//
lista.splice(1, 2)  // [4.5, 'abc']
```

Quando atribuimos um valor a um indice que não existe no *array*, o Javascript irá estender o *array*, o preenchendo com *undefined* até o indice desejado, que receberá o valor que foi fornecido.

Exemplo:

```javascript
const lista = [2, 'abc', 4]

// Atribimos um valor a um indice que nao existe na lista
lista[5] = true

console.log(lista[3])    // undefined
console.log(lista[4])    // undefined
console.log(lista[5])    // true
```


### Array Destructuring

É um modo prático de extrair valores de um *array* e atribui-los a variáveis distintas.

Exemplo:

```javascript
var lista = ['x', 'y', 'z']

// destructuring padrao
var [a, b, c] = lista

console.log(a)    // 'x'
console.log(b)    // 'y'
console.log(c)    // 'y'

// Trocando valor entre variáveis
var [a, b] = [b, a]

console.log(a)    // 'y'
console.log(b)    // 'x'

```

## Rest e Spread

O Javascript possui o operador `...`, que facilita trabalhar com lista que não conhecemos a quantidade de elementos. Dependendo do contexto de uso (lado esquerdo ou direito da atribuição), é chamado de operador `rest` ou operador `spread`.

### Rest Elements

Quando o operador `...` aparece do lado esquerdo da atribuição, é denominado como operador `rest`. Este operador coleta zero ou mais valores, armazenando-os em um *array*.

```javascript
// Separando valores em particular
var [a, b, ...resto] = [1, 2, 3, 4, 5]

console.log(a)      // 1
console.log(b)      // 2
console.log(resto)  // [3, 4, 5]

```

O *array* `resto` que aparece acompanhada do operador é denominado `rest elements`.

> O *elemento `rest`* deve ser o último elemento do operação de *destructurig*.

```javascript
const [...resto, a, b] = [1, 2, 3, 4, 5]
```

O exemplo acima irá apresentar um `SyntaxError`, porque o *rest element* não esta no final da operação de *destructuring*.

### Rest Properties

Também podemos aplicar o mesmo conceito do operador `rest` para propriedades de objetos.

Exemplo:

```javascript
const {nome, ...endereco} = {
    nome: 'Maria',
    rua: 'Rua 123',
    cidade: 'Sao Paulo',
}

console.log(home)       // Maria
console.log(endereco)   // {rua: 'Rua 123', cidade: 'Sao Paulo'}

```

### Rest Parameters

O operador `rest` também pode ser utilizado como parâmento de uma função, possibilitando que passemso um número variável de parametros durante a chamada da função.

```javascript
function printName(...name) {
    console.log(name.join(' '))
}

printName('Maria')       // Maria
printName('Joao', 'Paulo')  // Joao Paulo
```

## Spread

### Spread Elements

Quando o operador `...` aparece do lado direto do operador de atribuição, ele é denominado operador `spread`. Esse operador expande um *array* em uma lista de elementos e, diferente do operador `rest`, pode ser usado mais de uma vez e em qualquer lugar da expressão.

```javascript
const resto = [3, 4, 5]

const a = [1, 2, ...resto]

console.log(a)   // [1, 2, 3, 4, 5]
```
### Spread Properties

Assim como o operador `rest`, também podemos utilizar o `spread` sobre propriedades de objetos.

```javascript
let endereco = {
    rua: 'Rua 123',
    cidade: 'Sao Paulo',
}

endereco = {...endereco, estado: 'SP'}

console.log(endereco)   // {rua: 'Rua 123', cidade: 'Sao Paulo', estado: 'SP'}
```

## Array Analysis

São método nativos para analisar o conteúdo de um array. A maioria desses métodos recebe uma *function* como parâmetro (denominada *predicate*) e devolve *true* ou *false* como parâmetro. Normalmente são utilizadas no lugar de laços *for*.

#### include

Verifica se um array contem um determinado valor.

Exemplo:

```javascript
const lista = ['one', 2, 3, 'four', 5];

lista.include('one');  // true
lista.include(4);      // false
```

#### every

Verifica se todos os elementos do array cumprem o requisito analisado pela *function*, retornando *true* ou *false*.

Exemplo:

```javascript
const pares = [2, 4, 6, 8];

pares.every((n) => n % 2 == 0)  // true (todos sao pares)
```

> Funcionamento semelhante ao *all()* em Python.

#### some

Verifica se pelo menos um dos elementros do array cumpre o requisito analisado pela função, retornando *true* ou *false*.

Exemplo:

```javascript
const lista = [1, 2, 4, 6];

lista.some((n) => n % 2 != 0); // true (o numero 1 é impar)
```

> Funcionamento semelhante ao *any()* em Python.
#### find

Retorna o valor do primeiro elemento que satisfaça a condição analisada pela função.

Exemplo:

```javascript
const lista = [1, 2, 3, 4]

lista.find((n) => n % 3 == 0); // 3 (primeiro numero divisivel por 3)
```

#### findIndex

Funciona de forma semelhante ao *find()*, porém retorna o indice do elemento ao invés do elemento em si.

Exemplo:

```javascript
const lista = [1, 2, 3, 4];

lista.findIndex((n) => n % 3 == 0);  // 2 (indice do numero 3)
```

### Array Transformations

A classe Array possui muitos metodos para manipulação de valores. Esses métodos são denominados *puros* quando não alteram o array original. Quando os valores do array original são alterados, a função é denominada *impura*.

Exemplo função *pura*:

```javascript
const lista = [1, 2, 3, 4];

lista.filter(n => n % 2 == 0);  // [2, 4]
```

Exemplo função *impura*:

```javascript
const lista =  [1, 2, 3, 4];

lista.reverse(); // [4, 3, 2, 1]
```

## Object [^obj]

**Object** é uma *function* do Javascript. É utilizado para armazenar coleços de *chave: valor*. 

> Não confundir *object* com o formato *JSON(Javascript Object Notation)*. Apesar de serem parecidos, o **JSON** é um formato textual e aceita apenas aspas duplas como delimitador de texto, enquanto **Object** é uma notação literal para objetos e aceita tanto aspas simples como aspas duplas para delimitar textos

O exemplo a seguir cria um *object* com 2 propriedades *chave: valor*.

> O *object* funciona de modo semelhante ao *dict* do Python.

Exemplo:

```javascript
const aluno = {
    nome: 'João',
    idade: 15,
    curso: 'Engenharia',
}

// Acessando valores
console.log(aluno.nome)      // 'João'
console.log(aluno['idade'])  // 15

// Adicionando novas chaves ao object
aluno.turma = '2A'  // ou
aluno['turma'] = '2A'

// Deletando chaves do object
delete aluno.curso     // ou
delete aluno['curso']

// Verificando se uma chave existe no object
aluno.hasOwnProperty('idade') // true

// Nova versao
Object.prototype.hasOwnProperty.call(aluno, 'idade')
```

Podemos também utilizar um *object* como base para a criaçãoi de outro *objeto*.

Exemplo:

```javascript
const objA = {
    a: 1,
    b: 2,
}

const objC = { ...objA, c: 3} // novo object {a: 1, b: 2, c:3}
```

## Funções [^function]

No Javascript, funções são consideradas **Objetos de Primeira Classe** (do inglês, *First Class Object*). Isso significa que as funções tem papel central na linguagem e que podemos tratá-la com um dado. Como consequência disso, tanto **object** como **class** também sao do tipo *function* e cada função instânciada é portanto um objeto da classe **Function**.

```javascript
typeof Object            // function
typeof class Aluno {}    // function
```

Podemos armazenar uma **function** em uma variável e invocá-la posteriormente.

```javascript
const foo = function () {
    return 'Hello World!'
}

consolo.log(foo())    // 'Hello World'
```

### Passagem de parâmetros

Assim como em outras linguagens, uma *function* pode aceitar um conjunto de parâmetros de qualquer tipo de modo a executar seu código. Entretanto, em **Javascript**, passar mais ou menos argumentos do que a quantidade de parâmetros que a *function* recebe não dispara nenhum erro.

> Parâmetros e retornos em Javascript são *opcionais*.

Exemplo:

```javascript
function imprimirSoma(a, b) {
    console.log(a + b)
}

imprimirSoma(2, 3)    // 5
imprimirSoma(2)       // NaN (o valor do parâmetro 'b' é undefined)
imprimirSoma(2, 3, 4, 5)   // 5 (os argumentos 4 e 5 são ignorados)
```

Podemos atribuir um valor *default* para os parâmetros, de modo a evitar que os mesmo fiquem como *undefined* se nenhum argumento correspondente não forem passados para a *function*.

Exemplo:

```javascript
function imprimirSoma(a, b=1) {
    console.log(a + b)
}

// Como não foi fornecido argumento para 'b', ele recebe o valor default de 1

imprimirSoma(2)   // 3 
```

O Javascript também nos permite passar **functions** como parâmetro.

Exemplo:

```javascript
function imprimir(foo){
    // aqui, invocamos a function
    foo()
}

// passamos a function como parametro
imprimir(function () {
    console.log('Hello World')
})

// Saida:
// 'Hello World!'
```

### Retorno de função

Uma *function* pode retornar valores de quaiquer tipos, porém pode retornar apenas um valor por vez. Uma *function* que não retorna valor ou que possui o *return* ausente, retorna *undefined*. No Javascript não existem *return* implicitos.

Exemplo:

```javascript
function imprimirFoo(foo) {
    console.log(foo)
    return
}

imprimir('texto')  // retorna undefined

function imprimirFoo2(foo) {
    console.log(foo)
}

imprimitFoo2('texto')  // retorna undefined
```

### Função Anônima

Como funções são membros de primeira classe*, também podemos atribuí-las a variáveis. Esse recurso é muito util em diversas funções do Javascript que muitas das vezes, devido a sua natureza funcional, recebem outras funções como parâmetro.

Exemplo:

```javascript
const imprimirSoma = function (a, b) {
    console.log(a + b)
}

imprimirSoma(2, 3)    // 5
```

Também podemos atribuir uma função como uma *property* de um objeto.

Exemplo:

```javascript
const aluno = {
    nome: 'João',
    idade: 15,
    curso () {
        return 'Engenharia'
    },
}

aluno.curso()  // Retorna 'Engenharia'
```

#### Arrow Functions

As funções anônimas também podem ser escritas usando *arrow functions*. Essa função foi introduzida no ES6 e possibilita uma notação mais exuta da função.

Exemplo:

```javascript
const imprimirSoma = (a, b) => {
    console.log(a + b)
}

imprimirSoma(2, 3)    // 5

// Outra notação
const imprimirSoma = (a, b) => console.log(a + b)

imprimirSoma(2, 3)    // 5
```

### Função Callback [^callback]

São funções passadas como argumento para outras funções e é executada dentro dessa função para completar algum tipo de rotina. Função de *callback* são normalmente utilizadas em de assincrono.

Exemplo: 

```javascript
function printHello() {
    console.log('Hello World!');
}

button.addEventListener(printHello);
```

No exemplo acima, quando o botão `button` for pressionado, a função `printHello` será invocada e mensagem `Hello World!` será impresso.

### Função Nested (*nested function*) [^nested-functio]

Uma função é denominada *nested* (ou aninhada), quando é declara dentro de outra função. Normalmente é utilizada de modo a centralizar um código que ocorre repetidas vezes dentro do escopo da função ao qual ela foi inserida.

```javascript
function printHello(firstName, lastName) {

    function getName() {
        return `${firstName} ${lastName}`;
    }

    console.log('Hello, ' + getName());
    console.log('Bye ' + getName());
}
```


## Prototypes & Classes

Javascript permite programação orientada a objetos utilizando herança baseada em prototipos.

### Prototype Syntax

#### Constructor Function

Quando uma *function* é utilizada como *template* (*class*), ela é chamada *contructor function* (o nome da função deve seguir o padrão *CamelCase* para esse caso). As instâcias (objetos) derivados do template utilizam *new* para invocar o contrutor do template.

```javascript
function Car() {
   // ...
}

const car1 = new Car();
const car2 = new Car();
```

Os objetos criados possuem uma *property* interna denominada *prototype*. Essa *property* é uma relação com a *contructor functon*. Ela armazena uma referência para a chave *prototype* da *contructor function*.

#### Campos e métodos

Os campos de uma *contructor function* podem ser acessadas utilizando o *this*.

```javascript
function Car(color) {
	this.color = color;
}

const car = new Car('azul');
console.log(car.color);   // azul
```

Os métodos podém ser acessados usando a *property* **prototype** da *constructor function*.

```javascript
function Car(color) {
	this.color = color;
	this.engineRunning = false;
}

Car.prototype.start = function () {
	this.engineRunning = true;
}

const car = new Car('azul');
car.start();
```

### Class Syntax

Nas versões mais recentes, Javascript trouxe a palavra chave *class*, utilizada para criação de templates como o mesmo funcionamento de outras linguagens 
Orientadas a Objetos.

```javascript
class Car {

	contructor(color) {
		this.color = color;
		this.startEngine = false;
	}

	start() {
		this.startEngine = true;
	}

	addGas(litre) {
		// ...
	}
}

const car = new Car('red');
car.start();
```

Mesmo com a utilização de classes, Javascript ainda continua sendo uma linguagem baseadas em protótipos.

Os *get* e *set* de outras linguagens OO também estão presentes.

```javascript
class Car {

	contructor(color) {
		this._color = color; // atributos privados
		this._gas = 100;
	}

	// Consulta de atributo
	get gas() {
		return this._gas;
	}

	// Atribuicao de valor
	// podemos bloquear a atribuicao por aqui
	set gas(value) {
		this._gas = value;
	}
}

const car = new Car('red');

console.log(car.gas); // 100

car.gas = 0;
```

#### Herança de classes

Podemos também utilizar herança entre as classes utilizando a palavra chave *extends*.

```javascript

class Car {

	contructor(color) {
		this.color = color;
		this.gas = 100;
	}

	addGas(value) {
		this.gas = value;
	}
}

class Ferrari extends Car {

	contructor(color) {
		super(color);
	}

	addGas(value) {
		super.addGas();
		console.log('Add gas');
	}
}

const car = new Ferrari('red');
car.addGas(50);

```

## Referências

[^number]: https://www.w3schools.com/jsref/jsref_obj_number.asp
[^math]: https://www.w3schools.com/jsref/jsref_obj_math.asp
[^IEEE]: https://en.wikipedia.org/wiki/IEEE_754
[^string]: https://www.w3schools.com/jsref/jsref_obj_string.asp
[^boolean]: https://www.w3schools.com/jsref/jsref_obj_boolean.asp
[^array]: https://www.w3schools.com/jsref/jsref_obj_array.asp
[^obj]: https://www.w3schools.com/jsref/jsref_obj_object.asp
[^var]: https://www.w3schools.com/jsref/jsref_var.asp
[^let]: https://www.w3schools.com/js/js_let.asp
[^const]: https://www.w3schools.com/js/js_const.asp
[^hoisting]: https://www.w3schools.com/js/js_hoisting.asp
[^operators]: https://www.w3schools.com/js/js_operators.asp
[^coales]: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing
[^errors]: https://www.w3schools.com/js/js_errors.asp 
[^ifelse]: https://www.w3schools.com/js/js_if_else.asp
[^switch]: https://www.w3schools.com/js/js_switch.asp
[^while]: https://www.w3schools.com/js/js_loop_while.asp
[^function]: https://www.w3schools.com/js/js_functions.asp
[^callback]: https://developer.mozilla.org/en-US/docs/Glossary/Callback_function
[^nested-function]: https://javascript.info/closure#nested-functions







