Title: Configurando seu ambiente de desenvolvimento com Ubuntu Make
Date: 2016-03-29 18:46:01 -0300
Category: Desenvolvimento
Tags: linux, tutorial, ubuntu make, desenvolvimento
Author: Michell Stuttgart
Summary: O Ubuntu Make é uma ferramenta incrível para você que utiliza várias ferramentas de desenvolvimento e gostaria de ter esse ambientes instalado com apenas alguns comandos.

[Ubuntu Make](https://wiki.ubuntu.com/ubuntu-make) é uma ferramenta de linha de comando que permite que você faça o download e instalação de das ferramentas de desenvolvimento mais populares, instalando também todas as suas dependências. O objetivo do [Ubuntu Make](https://wiki.ubuntu.com/ubuntu-make) é possibilitar que, através de um comando, você tenha seu ambiente de desenvolvimento pronto para uso.
Ele possui suporte a instalação de IDE's de diversas linguagens, ferramentas para desenvolvimento web frontend(javascript e dart), backend (go and dart), mobile (java e android sdk) e etc.

### Instalação

A instalação depende da inclusão do ppa abaixo. Então, basta abrir o termial e entrar com os comando a seguir:

```bash
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make
```

### Utilizando o Ubuntu Make

#### Categorias

O [Ubuntu Make](https://wiki.ubuntu.com/ubuntu-make) possui uma lista de plataformas suportadas que foram separadas por categorias para facilitar a vida do desenvolvedor na hora de instalar suas ferramentas preferidas.

As categorias existentes podem ser visualizadas com o comando abaixo.

```bash
umake --help
```

No presente momento, temos as seguites categorias. Novas ferramentas sempre estão sendo incluídas pela comunidade:

Categoria | Descrição
----------|----------
games     | Ambiente de desenvolvimento de games
web       | Ambiente de desenvolvimento web
go        | Suporte a linguagem Go
dart      | Ambiente de desenvolvimento Dartlang
ide       | IDE genéricas
android   | Ambiente de desenvolvimento Android
swift     | Suporte a linguagem Swift
scala     | Suporte a linguagem Scala
rust      | Suporte a linguagem  Rust
nodejs    | Versão estável do Nodejs

Se você desejar verificar as opções de uma sub-categoria, basta usar o comando a seguir:

```bash
umake android --help
```

Você encontrará as seguintes opções:

 Categoria | Descrição
 ----------|----------
 android-ndk | Android NDK
 android-sdk    | Android SDK
 android-studio | Android Studio (padrão)

E assim você pode ir navegando nas subcategorias da ferramenta.

#### Exemplos de uso

O uso do Ubuntu Make é muito simples, o que o torna uma ferramenta muito valiosa. Como exemplo vamos realizar a instalação da IDE Netbeans. Basta executar o comando a seguir.

```bash
umake ide netbeans
```

Basta aceitar os termos de uso, entrando com o texto "Eu aceito" e esperar download e instalação da IDE. Depois disso você já pode usá-la. As IDE e SDK's normalmente são instalados nbo diretório `.local/share/umake/`

A instalação do ambiente de desenvolvimento do Android também segue o mesmo princípio, porém possui uma categoria própria.

```bash
umake android android-sdk
umake android android-studio
```

Instalando a versão estável do nodejs

```bash
umake nodejs
```

### Conclusão

Bom, esses são alguns exemplos de uso do Ubuntu Make. Para mais informações você pode consultar a página oficial [aqui](https://wiki.ubuntu.com/ubuntu-make).

Obrigado por ler e até o próximo post! t+
