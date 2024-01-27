from scipy import constants
import matplotlib.pyplot as plt
import numpy as np


ener = np.linspace(0,90,5000)

x = 1/(np.exp(((ener-45)*10**(-9)*constants.elementary_charge) / (constants.Boltzmann * 100 * 10 **(-6))) + 1)

plt.plot(ener, x)

x = 1/(np.exp(((46-45)*10**(-9)*constants.elementary_charge) / (constants.Boltzmann * 100 * 10 **(-6))) + 1)
print(x)