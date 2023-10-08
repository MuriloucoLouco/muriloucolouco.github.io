---
title: "Sobre uma questão da OBMEP"
date: 2023-10-08T00:12:42-04:00
draft: false
---

## As regras

Não lembro direito de como estava escrito, mas vai mais ou menos assim:

> Você quer pintar todos os números inteiros de preto ou branco

> Regra 1: $n$ e $n+5$ devem ter a mesma cor.

> Regra 2: Se $n = ab$ ($a, b$ inteiros) for branco, então pelo menos um dos fatores ($a, b$) também serão brancos.

A questão pedia três coisas:

## a) prove que se $38$ for branco, então $3$ também será.

Isso é bem fácil: pela regra 1, temos que, como $n+5 = 38$ é branco, então $n = 33$ também é. Podemos prosseguir da mesma forma: como $n+5 = 33$ é branco, então $n = 28$ também é. Sempre subtraindo $5$ do valor (38, 33, 28, 23, 18, 13, 8, 3), até chegarmos no 3.

Mas mais importante que isso é generalizar esse resultado:

> Teorema 1: se $x$ é de uma cor, então $x + 5k$ ($k \in \mathbb{Z}$) é da mesma cor.

Podemos comprovar isso por indução. Primeiro, o caso base ($k = 1$) é válido pela definição da regra 1.

Agora o passo indutivo: se $x + 5k$ é de uma cor, então $x + 5(k+1)$ é da mesma cor. Para provar isso, basta aplicar a regra 1: $(x + 5k)$ deve ter a mesma cor que $(x + 5k) + 5$, que é igual a $x + 5(k+1)$.

Porém, provamos apenas para os casos em que $x$ aumenta. Para provar para todos os inteiros, precisamos considerar as substrações. O passo indutivo nesse caso é que, se $x + 5k$ é de uma cor, então $x + 5(k-1)$ é da mesma cor. 

Para provar este caso, usamos a regra 1 novamente: $(x + 5(k-1))$ deve ter a mesma cor que $(x + 5(k-1)) + 5$, que é igual a $(x + 5k)$.

## b) prove que se $4$ for branco, então $2$ também será.

Podemos aplicar a regra 2 com $n = 4$, $a = 2$, $b = 2$. A regra 2 diz que pelo menos um dos fatores deve ser branco também. A questão é que, independente de escolhermos $a$ ou $b$, teremos que $2$ é branco, pois ambos são iguais.

> Corolário: pela mesma lógica, se $x^2$ é branco, então $x$ também é branco.

Mas agora vamos generalizar este resultado:

> Teorema 2: Se $x^k$ é branco ($k \in \mathbb{N}$), então $x$ também é branco.

Este teorema é provado por contradição. Vamos assumir que o teorema é falso.

Podemos aplicar a regra 2 com $x^k = x^{k-1} \cdot x$. Existem duas possibilidades: se $x$ for o branco, então nosso teorema deve ser verdadeiro, chegando a uma contradição.

O branco então necessariamente será o $x^{k-1}$ (lembrando, ao menos um deles deve ser branco pela regra 2), então agora a regra 2 com $x^{k-1} = x^{k-2} \cdot x$. Novamente, temos duas possibilidades: se $x$ for o branco, então nosso teorema é verdadeiro, chegando a uma contradição. Portanto, o branco precisa ser o $x^{k-2} = x^{k-3} \cdot x$.

Se prosseguirmos assim de forma recursiva, considerando apenas os casos que o fator branco é o $x^{k-\ldots}$, eventualmente chegaremos no caso em que $x^{k-\ldots} = x^2 = x \cdot x$, e pelo corolário, $x$ é branco.

Provamos então, que independente de qual fator fosse o branco, você necessariamente chegaria a que $x$ é branco, contradizendo nossa presunção que o teorema é falso, e portanto, provando o teorema.

## c) prove que $2$ e $3$ devem ter a mesma cor.

Agora é meramente uma questão de aplicar os dois teoremas.

Pelo teorema 1, se $2$ for branco, então $27 = 2 + 5\cdot 5$ também é. Pelo teorema 2, se $27 = 3^3$ for branco, $3$ também é. Ou seja, se $2$ é branco, $3$ é branco.

Similarmente, se $3$ for branco, então $8 = 3 + 5\cdot 1$ também é. Pelo teorema 2, se $8 = 2^3$ for branco, $2$ também é. Ou seja, se $3$ é branco, $2$ é branco.

Essas duas afirmações implicam que se um dos números for branco, o outro também será. É impossível terem cores diferentes.

## Aprofundando

Essa última questão é interessante: simplesmente somando múltiplos de $5$ a $2$, chegamos numa potência de $3$. Isso abre a pergunta: quais potências perfeitas ($m^n$ com $m, n$ inteiros) podem ser obtidos somando um múltiplo de $5$ a outro número?

Vou dar outro exemplo: se $7$ for branco, então $3$ também será, pois $27 = 7 + 5 \cdot 4$, e $27 = 3^3$.

Em geral a pergunta é essa: quais potências perfeitas podem ser escritas tanto como $a^m$ e $b + 5k$ (significando que se $b$ for branco, então $a$ também será)?

> Antes de prosseguir vou introduzir uma notação: $m B \to n B$ vai significar "Se $m$ é branco, então $n$ é branco". Similarmente teremos $m P \to n P$ para preto, e $m C \to n C$ para ambas as cores.

Vamos dar um exemplo primeiro: as potências de $3$ terminam em $1$, $3$, $9$ ou $7$. No caso do final $7$, obtemos $2B \to 3B$ (no item c)) e $7B \to 3B$. Pela regra 1, isso estenderá sempre que somarmos $5$ ao número: $12B \to 3B$, $17B \to 3B$, $\ldots$. Agora, usando o final $9$, obtemos outro conjunto de implicações: $9 = 4 + 5 \cdot (1)$ significa que $4B \to 3B$, e em seguida $9B \to 3B$, $14B \to 3B$, $\ldots$.

Observamos que, para cada último dígito $u$ das potências perfeitas de $a$, obtemos um conjunto de implicações $(u + 5k)B \to aB$.

Isso cobre um monte de casos. Por exemplo, para o caso do $3$, podemos montar a tabela:

> $1B \to 3B$, pois $1B \to 81B$ ($81 = 1 + 5 \cdot 16$), e $81B \to 3B$ pela regra 2

> $2B \to 3B$, pois $2B \to 27B$ ($27 = 2 + 5 \cdot 5$), e $27B \to 3B$ pela regra 2

> $3B \to 3B$, obviamente

> $4B \to 3B$, pois $4B \to 9B$ ($9 = 4 + 5 \cdot 1$), e $9B \to 3B$ pela regra 2

Os seguintes também podem ser obtidos simplesmente somando $5$ aos anteriores:

> $6B \to 3B$, pois $6B \to 81B$ ($81 = 6 + 5 \cdot 15$), e $81B \to 3B$ pela regra 2

> $7B \to 3B$, pois $7B \to 27B$ ($27 = 7 + 5 \cdot 4$), e $27B \to 3B$ pela regra 2

> $8B \to 3B$, pela regra 1

> $9B \to 3B$, pela regra 2

Somente um número não entrou na brincadeira, que é o $5$. A tabela anterior também significa que se qualquer número for branco (com exceção dos múltiplos de $5$), então $3$ também será.

A mesma lógica também pode ser aplicada para outros números. No caso do $2$, suas potências terminam em $2$, $4$, $8$ e $6$, então $2B \to 2B$; $4B \to 2B$; $8B \to 2B$ e $6B \to 2B$. Somando ou subtraindo $5$ obtemos também: $2+5 = 7B \to 2B$; $4+5 = 9B \to 2B$; $8-5 = 3B \to 2B$; $6-5 = 1B \to 2B$.

Novamente, todos os números terão $aB \to 2B$ com exceção dos múltiplos de $5$.

O motivo de não existir $5kB \to nB$ para esses números é simples: para que isso ocorrese, seria necessário que uma potência de $n$ terminasse em $0$ ou $5$, mas isso só ocorre se $n$ for um múltiplo de $5$.

De fato, se agora pegarmos o caso $5$, veremos que somente existe $5kB \to 5B$. Não existe $2B \to 5B$ ou $3B \to 5B$. Isso ocorre porque potências de $5$ sempre terminam em $5$.

Já cobrimos os casos de $b = 2, 3, 5$, continuemos agora com o caso $b = 4$. Dessa vez, os as potências terminam em $4$ ou $6$, obtendo $4B \to 4B$ e $6B \to 4B$. Somando/substraindo $5$ obtemos também $9B \to 4B$ e $1B \to 4B$.

$1^m$ é sempre $1$, então somente obtemos apenas $1B \to 1B$ e $6B \to 1B$.

## Finalmente pintando

Continuando este processo obtemos uma tabela de $aB \to bB$ ($a$ em cima, e $b$ na lateral):

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ✔️ |   |   |   |   | ✔️ |   |   |   |
| 2 | ✔️ | ✔️ | ✔️ | ✔️ |   | ✔️ | ✔️ | ✔️ | ✔️ |
| 3 | ✔️ | ✔️ | ✔️ | ✔️ |   | ✔️ | ✔️ | ✔️ | ✔️ |
| 4 | ✔️ |   |   | ✔️ |   | ✔️ |   |   | ✔️ |
| 5 |   |   |   |   | ✔️ |   |   |   |    |
| 6 | ✔️ |   |   |   |   | ✔️ |   |   |   |
| 7 | ✔️ | ✔️ | ✔️ | ✔️ |   | ✔️ | ✔️ | ✔️ | ✔️ |
| 8 | ✔️ | ✔️ | ✔️ | ✔️ |   | ✔️ | ✔️ | ✔️ | ✔️ |
| 9 | ✔️ |   |   | ✔️ |   | ✔️ |   |   | ✔️ |

Você vai perceber um padrão (que obviamente decorre da regra 1, mas também do fato dos últimos dígitos das potências terem um padrão de repetição a cada 5 números). A tabela de 1-5 se repete:

|   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | ✔️ |   |   |   |   |
| 2 | ✔️ | ✔️ | ✔️ | ✔️ |   |
| 3 | ✔️ | ✔️ | ✔️ | ✔️ |   |
| 4 | ✔️ |   |   | ✔️ |   |
| 5 |   |   |   |   | ✔️ |

Então vamos finalmente pintar os números. Como a regra 1 diz que a pintura será repetida após $5$ números, precisamos apenas determinar quais formas de pintar os números de $1$ à $5$. Ao todo, existem $2^5 = 32$ formas de pintar, mas apenas algumas irão satisfazer a regra 2 também.

Se $1$ for branco, todos os números (com exceção dos múltiplos de $5$) serão branco também. Então uma possível forma de pintar é deixar os múltiplos de $5$ pretos e o resto branco. Ou, também, todos os números, incluindo os múltiplos de $5$, serem brancos:

⬜⬜⬜⬜⬛

⬜⬜⬜⬜⬜

Se $2$ for branco, então também deverá ser o $3$ (esse na verdade foi o exercício c) ). O mesmo se $3$ for branco. Obtemos:


⬛⬜⬜⬛⬛

⬛⬜⬜⬛⬜

Se $4$ for branco, então também será o $2$ e $3$:


⬛⬜⬜⬜⬛

⬛⬜⬜⬜⬜

E por fim os casos de pintar o $5$, que não interfere nos outros números:

⬛⬛⬛⬛⬛

⬛⬛⬛⬛⬜

E esses são todos os casos. 8 possíveis formas de colorir.
