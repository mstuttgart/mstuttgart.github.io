#solid #poo #object-oriented-programming 

`SOLID` é um acrônimo para descrever os 5 principios de design para projetos de softwares usando linguagens de [[Programação Orientada a Objetos (POO)]]. Esses princípios são agnośticos em relação a linguagem de programação, ou seja, independem da linguagem de programação escolhida (desde que a mesma siga o paradigma POO). Os princípios foram apresentados por [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) em uma plubicação intitulada [Design Principles and Design Patterns](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf)

As letras do acrônimo possuem o seguinte siginificado:

* S - [Single Responsability Principle](#single-responsability-principle-1)
* O - [Open Close Principle]
* L - [Liskov Substitution Principle]
* I - [Interface Segregation Principle]
* D - [Dependency Inversion Principle]

Estes principios (ou postulados) auxiliam o desenvolvedor a projetar e escrever softwares Orientado a Objetos com baixo acoplamento, alta coesão e facilitando a manutenção e refatoração do código, quando necessárias.

## Single Responsability Principle [^srp]

*Princípio da Responsábilidade Única, em pt-BR.* 

Este postulado define o seguinte:

> Uma classe deve ter um, e somente um, motivo para mudar.

Dizemos que a classe deve ser coesa. Em outras palavras, ela deve ter uma *única* responsabilidade.
 
Por que uma classe ter mais de uma responsibilidade é um problema? 

Porque cada resposabilidade é algo passível de sofrer mudanças, e quanto mais responsabilidades nossa classe tiver, mais acoplada ela será, ou seja, mais impacto ela irá causar nas classes que dependem dela quando houver uma alteração em uma das responsabilidades. 

## Referências

[^srp]: https://web.archive.org/web/20150202200348/http://www.objectmentor.com/resources/articles/srp.pdf