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


x_null, y_null = maak_data("/home/gideon/Documents/Research Practicum/XAMS_null.dat")

x_vol, y_vol = maak_data("/home/gideon/Documents/Research Practicum/XAMS_volume.dat")

plt.figure()
plt.plot(x_null, y_null)
plt.title("null")

plt.figure()
plt.plot(x_vol, y_vol)
plt.title("vol")

y_res = np.array(y_vol) - np.array(y_null)

plt.figure()
plt.bar(x_vol, y_res)
plt.xlim(120, 150)
plt.ylim(0, 0.3e-9)
plt.xlabel("mass (u)")
plt.ylabel("prominence")

y_crop = y_res[120:150]
x_crop = x_vol[120:150]

y_min = 7.4e-13

y_peaks = []
x_peaks = []
for i in range(len(y_crop)):
    if y_crop[i] > y_min:
        y_peaks.append(y_crop[i])
        x_peaks.append(x_crop[i])


y_sum = np.sum(y_peaks)
print(y_sum)

y_percentage = (np.array(y_peaks) / y_sum) * 100

for i in range(len(y_peaks)):
    print(f"mass: {x_peaks[i]}, prominence: {y_percentage[i]} %")
