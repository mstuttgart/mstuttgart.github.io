# Mover conteúdo de várias pastas para uma pasta especifica

Tags: linux
Category: Terminal

O comando a seguir permite mover todos os arquivos do formato `*.mkv` presente no diretorio atual e subdiretorios e movê-los para um diretiroi chamado `filmes`.

```bash
find . -iname *.mkv | while read f; do mv "$f" filmes; done
```