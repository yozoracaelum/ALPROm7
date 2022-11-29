# Percobaan 5: Diagram Lingkaran 
# alpro705.py
'''
pie() untuk membuat diagram lingkaran
autopct='' adalah menampilkan desimal persen komposisi setiap bagian dari diagram lingkaran
'''
import matplotlib.pyplot as plt

angkatan = '2018','2019','2020'
sizes = [78,67,63]

figl,ax1=plt.subplots()
ax1.pie(sizes,labels=angkatan,autopct='%.2f%%')
ax1.axis('equal')

ax1.set_title("Mahasiswa Prodi Fisika")
plt.show()