# Percobaan 3: Grafik Trigonometri
# alpro703.py
'''
numpy adalah library tambahan untuk membuat array dan perhitungan matematis
arange() untuk membuat serentetan angka dalam bentuk array
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,np.pi/100)
y = np.sin(x)
plt.plot(x,y)
plt.show()
print(x)