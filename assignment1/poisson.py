import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

random.seed(0)

bernoulli_trial_success_number = 1
total = 0


def poisson():
    global total
    exponential_count = 0
    poisson_event_samples = []
    exponential_samples = []

    for _ in range(1000):
        bernoulli_trial_count = 0
        for _ in range(1000):
            exponential_count += 1
            if random.randrange(1, 21) == bernoulli_trial_success_number:
                total += 1
                exponential_samples.append(exponential_count)
                exponential_count = 0
                bernoulli_trial_count += 1
        poisson_event_samples.append(bernoulli_trial_count)

    plt.hist(poisson_event_samples, bins=100, density=True)
    plt.xlabel("# of successes")
    plt.xticks(np.arange(30, 70, 2))
    plt.ylabel("Occurrence")
    plt.show()

    lmbd = 50
    x = np.linspace(30, 70, 100)
    y = ((lmbd**x)*np.exp(-lmbd))/factorial(x)
    plt.plot(x, y)
    plt.show()

    plt.hist(exponential_samples, bins=100, density=True)
    plt.xlabel("# of trials")
    plt.ylabel("Occurrence")
    plt.show()

    lmbd = 50/1000
    x = np.linspace(0, 180, 100)
    y = lmbd * np.exp(-lmbd * x) # pdf
    y = 1 - np.exp(-lmbd * x) # cdf
    plt.plot(x, y)
    plt.show()


poisson()