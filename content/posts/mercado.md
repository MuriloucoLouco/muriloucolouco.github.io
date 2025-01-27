---
title: "Análise Técnica, Análise Quantitativa e Ficar Milionário"
date: 2025-01-26T17:13:57-04:00
draft: false
---

Esse é um post que merece muita matemática, mas ele tem o propósito de _desmistificar_. Porque sim, o tema é polêmico até mesmo no meio científico.

## Análise Técnica

Você já deve ter visto alguma propaganda de virar day trader, de um curso de como atuar no mercado financeiro, e no meio disso, a maneira milagrosa de prever o futuro do mercado: análise técnica.

Mas o que é exatamente a "análise técnica"? Você vai ver os caras desenhando linhas nos gráficos para observar padrões geométricos e tentar fazer afirmações de como o gráfico vai desenrolar no futuro. Essas ondas de elliot, padrões de reversão, etc. Como descreve Martin Pring, famoso analista técnico:

> A abordagem técnica para investimentos é, essencialmente, um reflexo da ideia de que os preços se movem em tendências determinadas pelas atitudes mutáveis dos investidores em relação a uma variedade de forças econômicas, monetárias, políticas e psicológicas. A arte da análise técnica, pois é uma arte, consiste em identificar uma reversão de tendência em um estágio relativamente inicial e acompanhar essa tendência até que o peso das evidências mostre ou prove que a tendência se inverteu.

Basicamente isto aqui:

{{< youtube 98CdC826okU >}}
.

Eu não preciso nem dizer que essas técnicas malucas de ombro-cabeça-ombro não funcionam. O mero fato do [movimento browniano](https://pt.wikipedia.org/wiki/Movimento_browniano) (efetivamente, movimento aleatório) ser um famoso modelo para o mercado (vide o modelo de [Black-Scholes](https://pt.wikipedia.org/wiki/Black-Scholes)), e o que o movimento browniano possui a [Propriedade de Markov](https://pt.wikipedia.org/wiki/Propriedade_de_Markov), já diz volumes sobre o quanto isso é um absurdo. 

Todavia, como eu acabei de linkar acima, existe muita teoria matemática por trás do mercado. Desde modelos estatísticos básicos até redes neurais, ao ponto que hoje em dia metade de todas as transações são feitas por robôs.

Por isso, aqui eu quero fazer uma distinção: quando eu falar "Análise Técnica" estou me referindo especificamente ao que se conhece como "Charting", que é o que você vai ver num típico curso de ficar milionário. Como eu disse antes, isso não tem nenhuma comprovação científica, e os poucos estudos que se notou lucro sofrem severamente de [P-hacking](https://pt.wikipedia.org/wiki/P-hacking). Mesmo que haja um noção popular entre as pessoas que a Análise Técnica funcione, e que isso influencie os gráficos para além de um mero movimento browniano, isso não se traduz em lucro de fato.

Para mais detalhes sobre a ineficácia, cheque a segunda fonte da lista.

## Análise Quantitativa (os Quants)

$$ dS = \mu S dt + \sigma S dW $$

O resto da Análise Técnica, que possui um pouco de fundamento científico e matemático (através do cálculo estocástico e data-science/aprendizado de máquina), é tipicamente chamado de Análise Quantitativa, e é essa que realmente nos interessa. Talvez até mesmo usando o fato de que as pessoas acreditam em análise técnica, e que isso influencia nos preços.

As técnicas são das mais variadas. Existe modelos de machine learning como redes neurais avançadas, que se alimentam das mais diversas informações globais para determinar como o mercado está se comportando e tentar fazer uma previsão com certeza maior que 50%.

É possível eu, um cidadão sem um supercomputador nem informações secretas que só os bilionários e o governo sabe, lucrar no mercado financeiro de forma consistente, ou é só um cassino gigante? 

## Teoria do Mercado Eficiente (TME)

A ideia dessa teoria é que "você não consegue vencer o mercado". Mais especificamente, dado um conjunto de informações disponíveis, é impossível lucrar com base nesse conjunto de informação, que inclui não só o histórico de valores desse mercado (chamado de eficiência fraca), mas até mesmo os tweets públicos do Elon Musk (eficiência semi-forte) e segredos privados que só o George Soros e seu círculo satânico sabe (eficiência forte).

Mas é verdade a TME? Se sim, quão "forte" é? Fraco, semi-forte ou forte? É fácil assumir que o capitalismo, em sua infinita eficiência de lucrar o máximo possível conseguiria nos vencer. 

Claramente a resposta não é um simples "sim" ou "não". De cara, é podemos logo dizer que TME forte (que informações privadas não podem prever o mercado) não é válido (inclusive eu pessoalmente diria que é uma das formas mais fáceis de gente rica fazer dinheiro, vide o [caso da Americanas](https://www.infomoney.com.br/mercados/americanas-ex-executivos-venderam-r-287-mi-em-acoes-antes-do-anuncio-de-rombo/)), mas a questão para o TME semi-forte e fraco é outra história.

Eugene F. Fama em seu artigo de 1970 argumentou através de modelos matemáticos estocásticos (similar ao que eu falei em um parágrafo acima) que pelo menos a TME fraca seria legítima. 

Porém, os anos se passaram e os estudos foram se empilhando. Não há dúvidas hoje em dia que o mercado não é eficiente. O modelo idealizado e distante da realidade proposto de fato não se encontra com a realidade. Tanto que, diversos estudos mostraram que existem sim métodos pautados na estatística que conseguem ter um lucro a longo prazo. Cheque a terceira e quarta fonte para mais informação.

## Vou ficar rico!!

Não. Sim, é verdade que é possível obter lucro através da análise quantitativa, mas para eu destruir seus sonhos, aqui vai um pouco da área de engenharia de dados e data science:

Empresas que lidam com dados geralmente são compostas de [vários times de especialistas](https://www.alpha-grep.com/career/): 

Primeiro passo da engenharia de dados: obter os dados. Vai ter um time de pessoas especializadas em obter os dados necessários para as análises. Isso envolve vários processos: web-scraping, compra de dados de outras empresas, e propria mineração de dados. Isso obviamente tem um custo muito grande: dados são o novo petróleo da era digital, ficar dias seguidos com máquinas minerando dados nas mais diversas fontes não é barato, tanto pelo tempo dos funcionários, quanto pela energia e outros fatores.

Segundo passo: tratar os dados. Alguém vai pegar essa pilha comicamente grande de centenas de gigabytes e limpar elas do lixo. Eles vão armazenar em bancos de dados caríssimos e dedicados ao grande volume de informação e de transações de informações.

Terceiro passo: elaborar um modelo. Aqui é área mais "bela": um monte de nerds mal pagos vão gastar dias da sua vida lendo o state-of-art de estudos da análise quantitativa para saber como elaborar seus modelos e como elaborar os algoritmos nais eficientes possíveis para a tarefa. Não preciso dizer que isso não é tão simples quanto escrever `pyAI.learn(dataset)`. Grandes estruturas de código escritos em C++ ou Rust, principalmente considerando que as maiores empresas lidam com transações em altíssima velocidade (por motivos que eu não vou explicar aqui).

Quarto passo: executar esses modelos em grandes supercomputadores para aprender e prever o mercado. A quantidade de energia necessária, além do custo de obter novos dados em tempo real na maior velocidade possível geram mais custo ainda. 

Fun-fact: essas empresas não disponibilizam o resultado de suas pesquisas para a população, pois elas não querem que ninguém possa copiar o método de ganhar dinheiro delas. Que surpresa.

É sem dúvidas uma operação que só pode funcionar com um capital gigantesco inicial. Então não, você na sua casa não vai conseguir ficar rico assim. Existe um motivo pelo qual todo mundo da área de análise quantitativa é funcionário de alguma empresa e o trabalho é sua fonte de renda principal. Porque eles não são donos de toda essa estrutura massiva que permite conseguir lucrar.

Você não pode competir com as grandes empresas.

## Eu não vou ficar rico...

Pois é. Eu acabo de escrever 1300 palavras, gastar horas lendo o state of art da pesquisa da área de investimento para concluir algo que Karl Marx tinha descoberto antes mesmo de existir todo esse debate.

Achou que não ia ter política? Pensou errado. Quem estudou sabe bem a realidade do sistema capitalista: A burguesia detém o capital. E somente capital gera mais capital. Somente quem é o dono de toda a infraestrutura digital, quem pode explorar os pesquisadores e cientistas, enfim, os meios de produção. Para o resto, resta o cassino.

Talvez seja por isso que haja tanta controvérsia na área. Talvez seja por isso que misturam análise técnica com análise quantitativa. Talvez seja por isso que os coachs recomendam você a baixar hoje um aplicativo e fazer day trade com suas economias. Talvez seja por isso que você receba tanta propaganda todos os dias de como ficar milionário. Talvez seja por isso que o tigrinho seja famoso. Porque para um ganhar, muitos tiveram que perder as riquezas que elas criaram com seu trabalho. Lucro no mercado financeiro é uma forma de mais-valia, sem vínculo empregatício.

Não significa que você não deva investir seu dinheiro. Pelo contrário: na medida do possível, faça isso. Diversifique sua carteira, coloque seu dinheiro num investimento de baixo risco, sei lá. Não deixe seu dinheiro parado, isso é fundamental para não ter seu pouco dinheiro engolido pela inflação.

Mas pare de acreditar que você vai ficar rico, que você não vai mais precisar trabalhar. Que você vai obter liberdade financeira com uma técnica milagrosa.

[Você não vai. Infelizmente.](https://www.marxists.org/portugues/marx/1848/ManifestoDoPartidoComunista/index.htm)

## Fontes

- P. Kuang, M. Schröder, Q. Wang, (2014). Illusory profitability of technical analysis in emerging foreign exchange markets, International Journal of Forecasting, 30(2), 192-205. https://doi.org/10.1016/j.ijforecast.2013.07.015.

- Fama, E. F. (1970). Efficient Capital Markets: A Review of Theory and Empirical Work. The Journal of Finance, 25(2), 383. doi:10.2307/2325486 

- Park, C.-H. and Irwin, S.H. (2007), WHAT DO WE KNOW ABOUT THE PROFITABILITY OF TECHNICAL ANALYSIS?. Journal of Economic Surveys, 21: 786-826. https://doi.org/10.1111/j.1467-6419.2007.00519.x

- Degutis, A. and Novickytė, L. (2014) “THE EFFICIENT MARKET HYPOTHESIS: A CRITICAL REVIEW OF LITERATURE AND METHODOLOGY”, Ekonomika, 93(2), pp. 7–23. doi:10.15388/Ekon.2014.2.3549.

- Lawrence C. Evans (2013), An Introduction to Stochastic Differential Equations. https://doi.org/10.1090/mbk/082

- MARX, K. O Capital - Livro I – crítica da economia política: O processo de produção do capital. Tradução Rubens Enderle. São Paulo: Boitempo, 2013.

![Análise Técnica](/mercado/analise.png)