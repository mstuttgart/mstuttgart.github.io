---
layout: post
comments: true
title: "Mate e Cinnamon: como reiniciar a configuração dos painéis de menu"
date: 2018-01-21 18:31:03
description: 'Aprenda a reiniciar os paineis de ambos para as configurações iniciais'
tags:
- linux mint
- cinnamon
- mate
- linux
categories: Linux
---

Fala pessoal, tudo certo?

Algum tempo atrás, eu removi alguns *apps* do painel de menu do meu *Cinnamon* sem querer e, após alguma pesquisa, encontrei uma maneira prática de restaurá-lo para a sua configuração inicial. Sendo assim, eu decidi compartilhar a solução, na esperança que isso seja útil para mais alguém.

## Como reiniciar o painel

Os comando a seguir foram testados nos ambientes *Mate* e *Cinnamon* do Linux Mint (versões 17+ e 18+). Não testei o funcionamento em outras *distros* que também utilizam *Mate*/*Cinnamon*, mas acredito que os comandos devem funcionar nelas também, provavelmente.

Para reiniciar os painéis dos ambientes, abra o terminal e entre com um dos comandos abaixo, de acordo com seu ambiente:

* Ambiente *Cinnamon*:

```console
gsettings reset-recursively org.cinnamon
```

* Ambiente *Mate*:

```console
gsettings reset-recursively org.mate.panel
```

Após digitar os comandos, tecle *Enter*. O ambiente gráfico vai recarregar e todos os painéis irão voltar a sua configuração inicial. Pode ser que seja necessário reiniciar o sistema para que todos os painéis efetivamente voltem para suas posições corretas.

## Referências

Eu encontrei esta dica no fórum do Linux Mint [aqui](https://community.linuxmint.com/tutorial/view/2195). Sendo assim, os créditos pela resolução do problema são do autor do *post* no fórum, o usuário [valdy9](https://community.linuxmint.com/user/view/138919).

## Conclusão

É isso pessoal. Qualquer dúvida, é só deixar um comentário. Ótima semana para vocês!