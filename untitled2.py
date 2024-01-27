from untitled0 import GetData
import matplotlib.pyplot as plt
import numpy as np

bestand = GetData("longrun18january.dat")
t = bestand.get_data('Time Relative (sec)')
t = bestand.get_data("Time Relative (sec)")
O_2 = bestand.get_data("32_amu")
O = bestand.get_data("16_amu")
N_2 = bestand.get_data("28_amu")
N = bestand.get_data("14_amu")
H_2_O = bestand.get_data("18_amu")

plt.plot(t, O, 'o', label="O")
plt.plot(t, N, 'o', label="N")
plt.plot(t, O_2, 'o',label="O$_2$")
plt.plot(t, N_2, 'o', label="N$_2$")
plt.yscale('log')
plt.legend()

plt.figure(dpi=500)
plt.plot(t, N_2/O_2, 'o')
plt.xlim(0,8000)
plt.xticks([0,2000,4000,6000,8000],fontsize=15)
plt.xticks([i for i in np.arange(0,8000,1000)], minor=True)
plt.ylim(0,5.3)
plt.yticks([i for i in np.arange(0,5.5,0.5)], minor=True)
plt.yticks(fontsize=15)
plt.xlabel('time (s)', fontsize=15)
plt.ylabel('N$_2$ / O$_2$', fontsize=15)
plt.savefig('ratio.pdf')

