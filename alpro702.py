# Percobaan 2: Judul dan label grafik
# alpro702.py
'''
xlabel() untuk menambah keterangan pada sumbu x
ylabel() untuk menambah keterangan pada sumbu y
title() untuk memberi judul grafik
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [12,16,18,23,27,30]
plt.plot(x,y)
plt.xlabel('Keterangan sumbu x')
plt.ylabel('Keterangan sumbu y')
plt.title('Judul Grafik')
plt.show()