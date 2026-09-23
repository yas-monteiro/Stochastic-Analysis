# Yasmin Monteiro e Silva
# Homework 1.3: Numerically testify the half order convergence of Monte Carlo integration

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

N = [i for i in range(100, 10000, 100)]
true_value = spi.quad(np.sin, 0, 1)[0]
n_trials = 100
Error = []

for i in N:
    errors = []
    for _ in range(n_trials):
        X = np.random.uniform(0, 1, i)
        Y = []
        for x in X:
            Y.append(np.sin(x))
        I_est = sum(Y)/i
        errors.append(abs(I_est - true_value))
    Error.append(np.mean(errors))

C = Error[0] * N[0]**0.5
Y_compare = [C * i**(-0.5) for i in N]

plt.plot(N, Error, 'b')
plt.plot(N, Y_compare, 'r')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Absolute Error')
plt.title('Homework 1.3')

plt.show()