# Percobaan 4: Asesoris Grafik
# alpro704.py
'''
plot('--r') akan membuat kurva garis putus-putus dan warna merah
plot('+b') akan membuat kurva plus dan warna biru
tick_params() untuk memberi warna pada setiap parameter angka di setiap sumbunya jika menggunakan axis='both'
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,np.pi/100)
y1 = np.sin(x)
y2 = np.sin(x+np.pi)
plt.plot(x,y1,'--r',label='sin(x)')
plt.plot(x,y2,'+b',label='sin(x+pi)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ploting Data')
plt.grid()
plt.legend()
plt.tick_params(axis='both',labelcolor='tab:orange')
plt.show()