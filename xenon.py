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

plt.figure()
plt.plot(x_null, y_null)
plt.title("null")

plt.figure()
plt.plot(x_vol, y_vol)
plt.title("vol")

y_res = np.array(y_vol) - np.array(y_null)


y_crop = y_res[50:150]
x_crop = x_vol[50:150]

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

x_expected = [124, 128, 129, 130, 131, 132, 134, 136]
y_expected = np.array([9.52e-4, 0.0191, 0.264, 0.041, 0.212, 0.269, 0.104, 0.089]) * 100


for i in range(len(y_peaks)):
    print(f"mass: {x_peaks[i]}, prominence: {y_percentage[i]} %")

plt.figure()
plt.plot(x_peaks, y_percentage, "o", alpha=0.5, color="red", label="found values")
plt.bar(x_expected, y_expected, alpha=0.5, label="expected values")
plt.legend()
plt.xlim(60, 75)
plt.xlabel("mass (u)")
plt.ylabel("abundance (%)")
