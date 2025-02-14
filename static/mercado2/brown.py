import numpy as np
np.random.seed(69420)

T = 10 # intervalo de tempo
dt = 0.01

# volatilidade e drift rate
sigma = 1.5
mu = 0.1

S = 1 # valor inicial
t = 0 # tempo inicial

while t < T:
    print(t, S)
    dW = np.random.normal(0, dt)
    dS = mu*S*dt + sigma*S*dW
    
    S += dS
    t += dt
