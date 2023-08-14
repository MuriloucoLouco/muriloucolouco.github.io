---
title: "Uma curta introdução à Teoria Quântica de Campos (TQC)"
date: 2023-08-13T17:21:04-04:00
draft: false
---

## Quantizando uma teoria clássica

O próposito deste artigo é introduzir a TQC para quem já está familiarizado com a mecânica quântica tradicional e teoria dos campos lagrangianos.

Primeiro, precisamos entender como surge a mecânica quântica a partir da mecânica clássica. Este processo é denominado quantização. O pressuposto básico é que, para sairmos do mundo clássico para o quântico, nós pegamos todos os valores físicos, como o momento $p$ ou a energia $E$, e transformamos em operadores quânticos: $\hat{p} = -i \hbar \nabla$ e $\hat{E}= i\hbar\frac{\partial}{\partial t}$.

Então, por exemplo, na mecânica clássica dizemos que o hamiltoniano é a energia do sistema ($H = E$), onde o hamiltoniano é a soma da energia cinética mais a energia potencial $H = T + V$. Porém, sabemos que a energia cinética de um corpo de massa $m$ e momento $p$ é $T = \frac{p^2}{2m}$, logo:

$$\frac{p^2}{2m} + V = E$$

Aplicando a quantização, o momento e a energia viram operadores que atuam num estado quântico:

$$\frac{\hat{p}^2}{2m}|\psi\rangle + V|\psi\rangle = \hat{E}|\psi\rangle$$
$$\Rightarrow \frac{-\hbar^2}{2m}\nabla^2|\psi\rangle + V|\psi\rangle = i\hbar\frac{\partial}{\partial t}|\psi\rangle$$

Que é a equação de Schrödinger. Estes operadores não vêm ao acaso. Por exemplo, o operador do momento pode ser derivado da seguinte relação:

$$[\hat{x}, \hat{p}] = i\hbar $$

Chamada de relação de comutação canônica. De forma resumida, nós começamos com a teoria clássica, e pegamos esses valores físicos relevantes (como o momento), e trocamos por operadores, e a maneira que fazemos isso é estabelecendo essa relação de comutação, dessa forma, quantizamos a teoria clássica.

## Lagrangianos

Na mecânica clássica, um sistema mecânico é determinado por um lagrangiano $L$ e um espaço de configuração, que são os parâmetros que determinam o sistema. Por exemplo, num sistema dinâmico que analise o movimento de uma partícula de massa $m$, os parâmetros são suas coordenadas no espaço, e o lagrangiano é:

$$L = T - V$$

Onde $T$ é a energia cinética (função da variação da coordenada espacial):

$$T = \frac{1}{2}m (\frac{\partial x}{\partial t})^2$$

E $V$ é a energia potencial. Num espaço livre, o potencial é nulo, mas poderia ser o potencial gravitacional (função da coordenada espacial).

Mas o lagrangiano por si só não faz nada. O lagrangiano atua como uma "lei da física" que está sendo analisada, ele o fundamento de tudo que está sendo estudado. Para completarmos a teoria, aplicamos o princípio da mínima ação, que diz que a ação $S = \int L dt$ deve ser mínimo: $\delta S = 0$.

Ou seja, um lagrangiano compila todas as leis da física em uma única coisa, e a maneira que pegamos essas leis é resolvendo $\delta S = 0$.

Ainda neste tópico, é bom lembrar da existência do momento, e como adquirimos ele de um lagrangiano. Se pegarmos o exemplo do lagrangiano da partícula livre acima $L = \frac{1}{2}m \dot{x}^2$, (onde $\dot{x} = \frac{\partial x}{\partial t}$, a velocidade), e derivarmos $L$ em função de $\dot{x}$ temos:

$$ \frac{\partial L}{\partial \dot{x}} = m\dot{x}$$

Porém $m\dot{x}$ é exatamente o momento. Então, faz sentido dizer que se $q$ é o parametro de uma teoria lagrangiana, então $\frac{\partial L}{\partial \dot{q}}$ é o momento dessa teoria.

## Teoria dos campos

A teoria dos campos pode ser tratada da mesma forma. Antes, o lagrangiano dependia de um número finito de parametros, ou os "graus de liberdade" do sistema. Por exemplo, a posição espacial. Agora, ao invés dessas posições espaciais (ou qualquer outro parâmetro), nós lidamos com infinitos parâmetros, que são os $\phi(x)$, um "parâmetro" para cada lugar no universo, o campo. Esse parâmetro pode ser um único número (um campo escalar), ou vários números (um campo vetorial), ou até mesmo um campo tensorial, se você está familiarizado com eles.

Numa teoria dos campos, o lagrangiano é $L = \int$ 𝓛 $dx$. 𝓛 é a densidade lagrangiana do sistema, e geralmente usamos ela no lugar do lagrangiano (já que para o obter o lagrangiano de fato é apenas uma integral sobre todo o espaço de 𝓛). Como este websítio que eu estou usando não suporta essa letra (𝓛) no meio do LaTeX, eu vou simplesmente usar a letra $L$ como densidade lagrangiana daqui em diante. Isto também é feito por livros, então não é tão anormal.

O exemplo mais famoso é o eletromagnetismo. No estudo básico, existem dois campos, $E$ e $B$. Porém, a teoria é fundamentalmente em torno de um único campo vetorial (de 4 dimensões) $A_\mu$, que é o "quadripotencial eletromagnético", o potencial elétrico (escalar) corresponde a coordenada temporal, e o potencial magnético (vetorial) corresponde às coordernadas espaciais. A densidade lagrangiana é:

$$ L = -\frac{1}{4} F_{\mu\nu}F^{\mu\nu} + \frac{1}{2}m^2 A_\mu A^mu $$

Onde $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. A notação de soma de Einstein é usada aqui (por exemplo, $A_\mu A^\mu = A_0 A^0 + A_1 A^1 + \ldots$). Não vou entrar em mais detalhes por que isso vai exigir conhecimento de cálculo tensorial e está fora do escopo desta introdução. 

Deste lagrangiano pode se obter todas as equações de maxwell de volta. Este é o poder da física lagrangiana.

Também de forma análoga à mecânica, onde a derivada do lagrangiano em relação a derivada do parâmetro é o momento (então se $x$ é o parametro, $\frac{\partial L}{\partial \dot{x}}$ é o momento), faz sentido dizer que no caso de uma densidade lagrangiana de um campo, como $\phi(x)$ são os parametros, logo:

$$\pi(x) = \frac{\partial L}{\partial \dot{\phi}}$$

Pode ser chamado de momento. No caso, ele é chamado de "momento conjugado". Se generalizarmos essa definição para derivadas não só em respeito ao tempo, mas para qualquer coordenada do espaço-tempo, tempo a densidade de momento $\Pi^\mu$, e $\pi = \Pi^0$ pois a coordenada do tempo é a coordenada zero.

## Quantizando uma teoria de campos

Agora, da mesma forma que começamos com uma teoria mecânica clássica e quantizamos ela com as relações de comutação, podemos pegar uma teoria de campos clássica e quantizar ela. Este processo é denominado quantização canônica.

No caso, de forma similar ao $[\hat{x}, \hat{p}] = i\hbar $, se uma teoria é descrita por um campo $\phi(t, x)$, a relação de comutação que quantiza ela é:

$$[\hat{\phi}(t, x), \hat{\pi}(t, y)] = i\hbar \delta(x - y)$$

Faz sentido: o $x$ é analogo ao $\phi(x)$ quando saímos da mecânica para a teoria dos campos, então $\hat{x}$ é analogo ao $\hat{\phi}(x)$. Da mesma forma, $\pi$ é o análogo do momento na teoria dos campos. O $\delta$ aqui nos diz que essas relações de comutação só existem caso estejam no mesmo ponto espacial. Se não, eles comutam normalmente como uma teoria clássica.