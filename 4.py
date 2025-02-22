import numpy as np
import matplotlib.pyplot as plt
a =  0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
temp_celc = -130
temp_klvn = -130 + 273.15
P1= 3664186.998
def
def vanderwal(V,T):
    P = ((R*T) / (V - b)) - (a / (V**2))
    return P
V = np.linspace(b+10**-5, 10**-3, 1000)
x = []
vanderwal(V, temp_klvn) - P1 == 0
