import numpy as np
import matplotlib.pyplot as plt
a =  0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
tempreture_celc = [-140, -130, -120, -110, -100]
temp_klvn = [temp + 273.15 for temp in tempreture_celc]
def vanderwal(V,T):
    P = ((R*T) / (V - b)) - (a / (V**2))
    return P
V = np.linspace(b+10**-5, 10**-3, 1000)
fig, ax = plt.subplots(figsize=(10,6))
P_1 = vanderwal(V, float(temp_klvn[0]))
P_2 = vanderwal(V, float(temp_klvn[1]))
P_3 = vanderwal(V, float(temp_klvn[2]))
P_4 = vanderwal(V, float(temp_klvn[3]))
P_5 = vanderwal(V, float(temp_klvn[4]))
ax.plot(V,P_1, label = f'{tempreture_celc}°С', color = 'black')
ax.plot(V,P_2, label = f'{tempreture_celc}°С', color = 'black')
ax.plot(V,P_3, label = f'{tempreture_celc}°С', color = 'black')
ax.plot(V,P_4, label = f'{tempreture_celc}°С', color = 'red')
ax.plot(V,P_5, label = f'{tempreture_celc}°С', color = 'black')
ax.set_xlabel('Молярный объем')
ax.set_ylabel('Давление')
ax.set_xlim(b + (10**(-5)), 10 ** (-3))
plt.show()