---
title: "Uma análise estatística do ENEM"
date: 2023-12-22T10:46:10-04:00
draft: false
---

## Como o TRI funciona?

Primeiro, resumindo como o TRI funciona: cada questão possui três parâmetros $a$, $b$ e $c$. O aluno também terá um número $\theta$ associado com sua habilidade no que a questão pede. Elas juntas formam uma curva logística que descreve a probabilidade do candidato acertar a questão dada sua habilidade:

$$ P(acertar | \theta) = c + \frac{(1-c)}{1+\exp[-a(\theta-b)]} $$

O parâmetro $a$ é o de discriminação, ela determina o quão bom é essa questão em separar alunos que sabem ($P \approx 1$) e os que não sabem ($P \approx 0$). Na curva, reflete num crescimento acentuado:

![a](/enem/a.png)

O parâmetro $b$ é o de dificuldade. Na curva, reflete o ponto em que a curva sobe. Ou seja, determina a nota média de corte dos alunos que sabem:

![b](/enem/b.png)

E por fim, $c$ é o parâmatro de assíntota, que descreve basicamente a probabilidade de alguém com habilidade baixa conseguir resolver o problema:

![c](/enem/c.png)

Esses parâmetros de cada questão são obtidos num pré-teste com alunos do terceiro ano do ensino médio. Segundo o INEP, 100 mil estudantes distribuídos por CEP para melhor amostragem. Eles fazem todo o cálculo de regressão.

Depois das provas do ENEM de fato, alguns itens podem ter parâmetros de pré-teste diferentes do reais. Então, eles fazem uma recalibragem dos parâmetros para adequar com os candidatos ao ENEM. Essa última recalibragem é a que será usada nos cálculos de proficiência.

A expressão que nos co

Primeiro, resumindo como o TRI funciona: cada questão possui três parâmetros aa, bb e cc. O aluno também terá um número θθ associado com sua habilidade no que a questão pede. Elas juntas formam uma curva logística que descreve a probabilidade do candidato acertar a questão dada sua habilidade:

P(acertar∣θ)=c+(1−c)1+exp⁡[−a(θ−b)]
P(acertar∣θ)=c+1+exp[−a(θ−b)](1−c)​ncerne aqui é:

$$ E(\theta | x, \eta) = \frac{\int_\mathbb{R} \theta L(x | \eta)f(\theta)d\theta}{\int_\mathbb{R} L(x | \eta)f(\theta)d\theta}  $$

Ok. Muita coisa para compreender. O $E(\theta | x, \eta)$ é, essencialmente, o valor esperado da sua "nota", que é o $\theta$, sua proficiência naquela área, dado suas respostas (o vetor $x$) e os parâmetros pré-determinados ($\eta$).

Para cálcular essa valor esperado, você precisa calcular essas integrais. $f(\theta)$ é a "função a priori", basicamente uma curva normal:

$$ f(\theta) = \frac{e^{\frac{-x^2}{2}}}{\sqrt{2\pi}} $$

E o $L(x | \eta)$ é um mistério baseado apenas no artigo do inep que eu li, mas baseado em outras fontes, é o produto de todas as probabilidades de acertar cada item:

$$ L(x | \eta) = \prod_n P_n $$

Onde $P_n$ é a probabilidade da pessoa ter acertado ou errado a enésima questão daquela área. 

A consequência clara disso, é que se as chances de acertar uma questão dado sua proficiência são baixas, isso vai refletir num valor menor de $L$ e consequentemente a nota não vai valer tanto. Porém, se sua proficiência é alta, essa nota vai valer normalmente.

Essas "notas" $\theta$ estarão numa distribuição normal com média $0$ e desvio padrão $1$. Então, para obter sua nota real naquela área, é preciso fazer a conversão:

$$ \textbf{Nota} = 100\theta + 500 $$

Para que a média seja $500$ e a desvio padrão seja $100$

Por exemplo, assumindo que todas as questões tenham o mesmo parâmetro:

$$ P(acertar | \theta) = 0.1 + \frac{0.9}{1+\exp[-2\theta]} $$

Se eu acertei, digamos, $30$ questões e errei $15$:

$$ L(x | \eta) = P(\theta)^{30}(1-P(\theta))^{15} $$

Então $E(\theta | x, \eta) \approx 0.3$, e a minha nota será $530$. Se eu acertasse todas as $45$, minha nota seria $773$. Aqui um gráfico com a relação de notas e pontuação, assumindo a probabilidade igual pra todas:

![notas](/enem/notas.png)

## Estimando notas

Quero estimar minha nota do ENEM. Problema: é impossível eu obter os parâmetros de cada questão para eu calcular. Apesar disso, é fato que em geral as notas do ENEM por pontuação são mais ou menos consistentes: uma pessoa que acerta $30$ questões em humanas vai tirar $600 - 700$.

Nosso método será simples: obter um intervalo de confiança de 99% para a nota do enem.

Como visto anteriormente, a relação a nota de uma pessoa, dada uma certa pontuação, segue uma distribuição padrão. Isso simplifica nossos cálculos: vamos criar uma distribuição padrão que seja a média de, digamos, os últimos 5 anos do enem.

Por exemplo, se as médias de notas de 2020, 2021 e 2022 para quem acertou $39$ questões sejam $880$, $910$, $900$, então a média das três seria $\approx 896$. Então se eu acertei $39$ questões em 2023, mesmo eu não sabendo nenhum dado da prova desse ano, eu posso estimar que vou tirar uma nota próxima de $896$.

Mas não basta apenas obter a média. Como eu disse antes, eu quero um intervalo de notas, que eu tenha 99% de certeza de que minha nota vai cair dentro deste intervalo. Isso significa obter o desvio padrão $\sigma$ e calcular o intervalo $896 - 2.56\sigma, 896 + 2.56\sigma$ ($2.56$ é o número para um intervalo de 99% de confiança).

Como vamos obter os dados? Bom, o INEP na verdade libera todos os dados: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

Baseado nisso podemos obter milhares de coisas. Por exemplo, aqui eu extrai a relação de pontuação e nota do enem em matemática de 1000 candidatos:

![Pontuação x Nota matemática](/enem/mat.png)