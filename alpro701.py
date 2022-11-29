# Percobaan 1: Dasar plot grafik
# alpro701.py
'''
matplotlib merupakan library tambahan pada python yang digunakan untuk memplot suatu data
untuk memplot digunakan module pyplot
Maka dari itu
from matplotlib import pyplot
atau
import matplotlib.pyplot

plot(x,y) digunakan untuk memplot pasangan data, sumbu x dan sumbu y secara berurutan
show() digunakan untuk menampilkan hasil plotingan data dengan aplikasi window tambahan
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [12,16,18,23,27,30]
plt.plot(x,y)
plt.show()