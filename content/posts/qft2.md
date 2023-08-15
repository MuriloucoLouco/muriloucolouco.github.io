---
title: "Uma visualização dos campos quânticos e como obter suas fórmulas"
date: 2023-08-14T21:24:53-04:00
draft: false
---

## Osciladores harmônicos quânticos

Comecemos com um problema da mecânica clássica: o Oscilador Harmônico Quântico. Aqui, temos um oscilador harmônico simples (a famosa mola com F = -kx), só que quantizado. O parâmetro desta teoria será o $\hat{x}$ (escreverei apenas $x$ para não conflitar com o $\dot{x}$ que é a velocidade) representando o deslocamento do oscilador. Livros normalmente usam $\hat{q}$, mas quero que esse texto seja condizente com o post anterior. O hamiltoniano é dado por:

$$ \hat{H} = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}\kappa x^2$$

O primeiro termo é a energia cinética usual e o segundo a energia potencial elástica, que também pode ser escrito como $\frac{1}{2}m\omega^2 x^2$, onde $\omega = \sqrt{\kappa/m}$. Se você estudou mecânica quântica, e eu estou presumindo que sim, sabe que os auto-estados $\psi_n$ da equação $\hat{H}|\psi\rangle = E|\psi\rangle$ é dado por uma fórmula maluca e complexa que raramente é derivada nos livros:

$$ \psi_n = \frac{1}{\sqrt{2^n n!}} (\frac{m\omega}{\pi\hbar})^{1/4} e^{-\frac{m\omega x^2}{2\hbar}} H_n(\sqrt{\frac{m\omega}{\hbar}}x) $$

onde $H_n$ são os polinômios de Hermite. Também não me darei ao trabalho de derivar ela, mas ela é importante na hora de computar numericamente os valores do estado. Este trabalho porém residirá apenas à mim.

Válido lembrar também que utilizando os operadores de criação e aniquilação que são definidos por:

$$ a = \sqrt{\frac{m\omega}{2\hbar}}(\hat{x} + \frac{i}{m\omega}\hat{p}) $$
$$ a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}(\hat{x} - \frac{i}{m\omega}\hat{p}) $$

E portanto permitem escrever o hamiltoniano de forma muito mais elegante:

$$ \hat{H} = \hbar\omega(a^\dagger a + \frac{1}{2})$$

E que se $\hat{H}\psi = E\psi$, então $\hat{H}(a^\dagger\psi) = (E + \hbar\omega)\psi$, ou seja, $a^\dagger$ cria um "pacote de energia" de $\hbar\omega$. Similarmente, $a$ remove o "pacote de energia" do estado. Outra forma de dizer isso de forma mais inequívoca é que $\psi_n = c_n (a^\dagger)^n\psi_0$ (onde $c_n$ é apenas uma constante de normalização).

Fazendo um gráfico do de $\psi_1$, por exemplo, temos:

![Gráfico 1](/qft2/eigenstate.png)

Porém, podemos representar tudo em uma única linha, usando cores ao invés de altura para representar o valor de $\psi_1$. Também rotacionei por 90 graus, pois será útil no futuro. Note também que eu não coloquei a cor para todos os pontos da linha, mas para um monte de pontos aleatórios uniformemente distribuídos na linha. Isso será útil no futuro também.

![Gráfico 2](/qft2/eigenstateline.png)

## Generalizando

Agora vamos supor dois osciladores harmônicos. Nosso estado dependerá de dois parâmetros agora, um para cada oscilador: $x_1, x_2$. Por hora, assumiremos que esses osciladores não interagem entre si. O hamiltoniano é:

$$ \hat{H} = \sum_{n=1,2} \frac{1}{2}m\dot{x_n}^2 + \frac{1}{2}\kappa x_n^2 $$

Claro que esse hamiltoniano será generalizado para $N$ osciladores no futuro, mas ainda quero apenas olhar no caso $N=2$ pelos gráficos. Um fato interessante é que por não interagirem entre si, o auto-estado onde um deles é $\psi_{\nu_1}$ e outro $\psi_{\nu_2}$ é:

$$ \psi_{\nu_1, \nu_2} = \psi_{\nu_1}\psi_{\nu_2} $$

Usando o mesmo método de pontos, como agora temos dois parâmetros vou colocar cada ponto não numa reta como antes, mas num retângulo, e a cor do ponto ainda representa a intensidade de $\psi$. Por exemplo, no caso $\psi_{1, 2}$, o gráfico fica:

![Gráfico 3](/qft2/eigenstateplane.png)

Outra possível representação, é ao invés de representar os parâmetros $\vec{x} = (x_1, x_2)$ como um ponto num espaço, podemos ter um eixo paralelo para cada parâmetro, e uma linha que conecte os dois pontos em cada eixo. Por exemplo, o ponto $\vec{x} = (0.5, -0.2)$ seria desenhado assim: