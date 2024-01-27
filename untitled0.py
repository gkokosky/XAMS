import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class GetData:
    def __init__(self, path):
        self.df = pd.read_csv(path, sep="\t", skiprows=8)

    def get_data(self, data):
        return self.df[data]


bestand = GetData("longrun18january.dat")
t = bestand.get_data("Time Relative (sec)")
O_2 = bestand.get_data("32_amu")
O = bestand.get_data("16_amu")
N_2 = bestand.get_data("28_amu")
N = bestand.get_data("14_amu")
H_2_O = bestand.get_data("18_amu")


# plt.plot(t, O_2, "o", label="O$_2$")
# plt.plot(t, N_2, "o", label="N_2")
# plt.plot(t, O, "o", label="O")
# plt.plot(t, N, "o", label="N")
# plt.plot(t, H_2_O, "o", markersize=0.5,label="H$_2$O")
# plt.yscale('log')
# plt.legend()

# bestand2 = GetData("19january.dat")
# t_twee = bestand2.get_data("Time Relative (sec)")
# O_2_twee = bestand2.get_data("32_amu")
# O_twee = bestand2.get_data("16_amu")

# plt.plot(t, O_2, "o")
# plt.plot(t_twee, O_2_twee, "o")


# plt.xlim(0, max(t_twee))

x = []
y = []
for i in range(1, 40):
    
    x.append(i)
    y.append(bestand.get_data(f'{i}_amu')[100])
    
y_percentage = (np.array(y) / np.sum(y)) * 100
plt.figure(dpi=500)
plt.plot(x,y_percentage, 'o')
plt.xlim(0,30)
plt.ylim(0,80)
plt.yticks([0, 20, 40, 60, 80], fontsize=15)
plt.yticks([10,30,50,70], minor=True, fontsize=10)
plt.xticks([0,5,10,15,20,25,30], fontsize=15)
plt.xticks([i for i in range(0,31)], minor=True)
plt.xlabel('mass (amu)', fontsize=15)
plt.ylabel('relative abundance (%)', fontsize=15)

    

