import numpy as np
np.random.seed(3)

alpha_0 = 0.0001
alpha_1 = 0.1
beta_1 = 0.8

N = 1000 # Número de instantes (Tf - Ti)/dt

#inicializar r, sigma, S
r = np.zeros(N)
sigma = np.zeros(N)
S = np.zeros(N)
S[0] = 1 # preço inicial

for t in range(1, N):
    sigma[t] = np.sqrt(alpha_0 + alpha_1*r[t-1]**2 + beta_1*sigma[t-1]**2)
    r[t] = sigma[t] * np.random.normal(0, 1)
    S[t] = S[t-1] * np.exp(r[t])

for t in range(0, N):
    print(t, S[t])
