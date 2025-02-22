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
V = np.linspace(b+10**-5, 10**-3, 1000)
prom = (0.00013589-7.16308308e-05)/1000
def f1(V):
    P = (R*(-130+273.15)/(V-b)) - a/(V**2)
    return P
lenght = 0
for i in range(999):
    V = prom*i + (7.16308308e-05)
    bet = (((vanderwal(V, temp_klvn)-vanderwal(V +prom, temp_klvn))**2)+prom**2)**(0.5)
    lenght = lenght+bet
print(lenght)