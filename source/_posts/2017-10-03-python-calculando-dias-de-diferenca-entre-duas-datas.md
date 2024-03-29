---
layout: post
title: "Como calcular a diferença de dias entre duas datas com Python"
date: 2017-10-03 07:16:57
description: "Aprenda a calcular a quantidade de dias entre duas datas."
tags:
- python
- tutorial
categories: Python
---

Neste tutorial vou mostrar um procedimento bem simples que utilizei recentemente para calcular a diferença de dias entre duas datas com a biblioteca nativa *datetime*.

Inicialmente, calculamos a data inicial e a data final:

```python
from datetime import datetime

# Data final
d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')

```

 e finalmente calculamos a quantidade de dias entre elas:

```python
# Calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)
```

Utilizamos a função `abs` para garantir que a quantidade de dias de diferença seja sempre positiva, independente da ordem em que as datas foram subtraídas.