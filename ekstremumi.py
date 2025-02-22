import numpy as np
import matplotlib.pyplot as plt
a =  0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
temp_celc = -130
temp_klvn = -130 + 273.15
def vanderwal(V,T):
    P = ((R*T) / (V - b)) - (a / (V**2))
    return P
def find_local_extrema(func, V, T):
    P = func(V, T)
    dP = np.diff(P)
    local_maxima_indices = np.where((dP[:-1] > 0) & (dP[1:] < 0))[0] + 1
    local_minima_indices = np.where((dP[:-1] < 0) & (dP[1:] > 0))[0] + 1
    local_maxima = V[local_maxima_indices], P[local_maxima_indices]
    local_minima = V[local_minima_indices], P[local_minima_indices]
    return local_maxima, local_minima
V = np.linspace(b+10**-5, 10**-3, 1000)
fig, ax = plt.subplots(figsize=(10,6))
P = vanderwal(V, float(temp_klvn))
ax.plot(V,P, label = f'{temp_celc}°С', color = 'black')
maxima, minima = find_local_extrema(vanderwal, V, float(temp_klvn))
ax.scatter(maxima[0], maxima[1], color='red', label='Локальные максимумы', zorder = 5)
ax.scatter(minima[0], minima[1], color='blue', label='Локальные минимумы', zorder=5)
ax.set_xlabel('Молярный объем')
ax.set_ylabel('Давление')
ax.set_xlim(b + (10**(-5)), 10 ** (-3))
plt.show()
print(maxima)
print(minima)