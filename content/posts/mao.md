---
title: "Matemática na mão"
date: 2023-09-26T20:54:35-04:00
draft: true
---

Dicas gerais para fazer cálculos na mão.

## Trigonometria

O método geral é simples: $\pi$ é trocado por $\frac{22}{7}$ e as funções são expandidas com as séries de taylor.

Comecemos com o cosseno. Na maioria das aplicações práticas, você lida com ângulos em graus e não radianos. Isso significa que queremos não computar $\cos(x)$ (com $x$ em radianos) mas sim $\cos(\frac{\pi}{180}x)$ (com $x$ em graus).

Agora, podemos fazer a troca $\pi \to \frac{22}{7}$, e então a função em graus é:

$$ \cos\left(\frac{11}{630}x\right) $$

E essa expressão pode ser expandida com as séries de Taylor, onde truncarei apenas para dois termos:

$$ \cos\left(\frac{11}{630}x\right) \approx 1 - \frac{\left(\frac{11}{630}x\right)^2}{2} = 1-\frac{121}{793800}x^2 $$

Porém, essa fração monstruosa $\frac{121}{793800}$ é muito próxima de uma fração bem mais simples de trabalhar: $\frac{1}{6560}$. Tem a ótima propriedade de o denominador ser múltiplo de $10$ e várias vezes de $2$: $6560 = 2^5 \cdot 5 \cdot 41$. Então nossa aproximação é:

$$ \cos(x°) \approx 1-\frac{x^2}{6560} $$

Uma análise gráfica rápida mostra que o erro para ângulos menores que $40°$ é menor que $0.01$. Tome cuidado: para ângulos maiores o erro fica bem maior, por exemplo, para $80°$ o erro é de $0.15$, que é muito grande para a maioria das aplicações, então o ideal é usar a fórmula de ângulo duplo $\cos(2x) = 2\cos(x)^2-1$.

Para a função seno o processo é similar:

$$ \sin(x°) \approx \sin\left(\frac{11}{630}x\right) \approx \left(\frac{11}{630}x\right) - \frac{\left(\frac{11}{630}x\right)^3}{6} $$
