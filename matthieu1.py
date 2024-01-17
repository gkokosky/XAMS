from scipy.integrate import odeint
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt


def matth_x(gamma, t, m, U, V, r_0, omega):
    x, x_dot = gamma

    gamma_dot = [x_dot, (-constants.e / m) * ((U + V * np.cos(omega * t)) / (r_0**2)) * x]

    return gamma_dot


def matth_y(gamma, t, B, C, omega):
    y, y_dot = gamma

    gamma_dot = [y_dot, -B * np.cos(omega * t) - C]

    return gamma_dot


for U in np.arange(0, 1, 0.025):
    gamma_0 = [1, 1]
    t = np.linspace(0, 10, 1001)

    m = 100 * constants.proton_mass
    V = U
    r_0 = 0.01
    omega = 0.1

    sol_x = odeint(matth_x, gamma_0, t, args=(m, U, V, r_0, omega))

    plt.figure()
    plt.plot(t, sol_x[:, 0])
