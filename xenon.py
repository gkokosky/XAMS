# XAMS Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def maak_data(file):
    df = pd.read_table(file)

    x = df["X"].tolist()
    y = df["Y"].tolist()

    x_found = []

    x_nieuw = []
    y_nieuw = []
    for i in range(len(x)):
        if x[i] not in x_found:
            x_nieuw.append(x[i])
            y_nieuw.append(y[i])

            x_found.append(x[i])

        else:
            pass

    return x_nieuw, y_nieuw


x_null, y_null = maak_data("XAMS_null.dat")

x_vol, y_vol = maak_data("XAMS_volume.dat")

y_res = np.array(y_vol) - np.array(y_null)


y_crop = np.array(y_res[120:150])
x_crop = np.array(x_vol[120:150])

y_min = 7.4e-14

y_peaks = []

y_filter = y_crop > y_min
x_peaks = x_crop[y_filter]
y_peaks = y_crop[y_filter]

x_expected = np.array([124, 128, 129, 130, 131, 132, 134, 136])
y_expected = np.array([9.52e-4, 0.0191, 0.264, 0.041, 0.212, 0.269, 0.104, 0.089]) * 100

# x_even = []
# x_odd = []
# x_half = []
# for i in x_expected:
    
#     if i % 2 == 0:
        
#         x_even.append(i)
#         x_half.append(i/2)
#     else:
#         x_odd.append(i)

# y_comp = []
# for i in range(len(x_peaks)):
    
#     if x_peaks[i] in x_half:
#         print(x_peaks[i])
#         y_comp.append(y_peaks[i] + y_peaks[2 * i])        
    
# y_percentage = (np.array(y_comp) / np.sum(y_comp)) * 100

print(y_peaks)
y_percentage = (np.array(y_peaks) / np.sum(y_peaks)) * 100
plt.figure(figsize=(8,6), dpi=500)
plt.bar(x_expected, y_expected)
plt.plot(x_peaks, y_percentage, 'o', color='red')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('mass (amu)', fontsize=15)
plt.ylabel('relative abundance (%)', fontsize=15)