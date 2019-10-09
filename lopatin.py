# Program Lopatin Burial History
# Membuat grafik burial history menggunakan metode Lopatin

# import library untuk grafik
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import math

# fungsi mencari gradien
def gradien(y2, y1, x2, x1):
	return (y2 - y1) / (x2 - x1)

# input jumlah formasi
N = int(input("Masukkan jumlah formasi: "))

# inisiasi parameter nilai
formasi   = [] # nama formasi
ketebalan = [] # ketebalam
isoT      = [] # isotemperature

# mengisi nama formasi
for i in range(N):
	formname = str(input("Masukkan nama formasi ke-" + str(i+1) + ": \n"))
	formasi.append(formname)

print()

# mengisi parameter umur batuan
umur = list(map(float, input("Masukkan umur batuan: \n").split()))

print()

# menerima input ketebalan formasi.
for i in range(len(formasi)):
	in_ket = list(map(int, input("Masukkan ketebalan untuk formasi " + formasi[i] + ": \n").split()))
	ketebalan.append(in_ket)

# penyesuaian kedalaman formasi dengan ketebalan
for i in range(len(umur)):
	sigma = 0
	for j in range(len(formasi)):
		sigma += ketebalan[j][i]
		ketebalan[j][i] = sigma

for i in range(len(formasi)):
	for j in range(len(umur)):
		print(ketebalan[i][j], end=" ")
	print()

maximum = max([max(i) for i in ketebalan])

temp = 20
interval = math.ceil(maximum / 132)

for i in range(0, interval):
	isoT.append(temp)
	temp += 10

# plot dalam grafik
# mengubah posisi sumbu-x ke attas
plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.labeltop'] = True

fig, ax1 = plt.subplots()

# label sumbu sekunder
ax2 = ax1.twinx()
ax2.set_ylabel("isotemperature")
ax2.set_ylim(bottom=20, top=max(isoT))

temperature = []

for i in range(len(isoT)):
	int_isot = []
	for j in range(len(umur)):
		int_isot.append(isoT[i])

	ax2.plot(umur, int_isot, color='red', linestyle="--", linewidth=0.5)
	temperature.append(int_isot)

ax2.invert_yaxis()

for i in range(len(formasi)):
    ax1.plot(umur, ketebalan[i], label=(formasi[i]))    # line plot
    ax1.scatter(umur, ketebalan[i])						# scatter plot

# posisi label sumbu primer
ax1.set_xlabel("umur (dalam juta tahun)")
ax1.xaxis.set_label_position('top')
ax1.set_ylabel("kedalaman")
ax1.set_ylim(bottom=0, top=maximum)

ax1.invert_yaxis()

np.savetxt("file_name.csv", np.row_stack((umur, ketebalan)), delimiter=",", fmt='%s')
np.savetxt("temperature.csv", np.row_stack((umur, temperature)), delimiter=",", fmt='%s')

plt.title("Lopatin Burial History")
ax1.legend(bbox_to_anchor=(1,0), ncol=4, prop={'size': 8})             # menampilkan legenda
fig.tight_layout()
plt.xlim(min(umur), max(umur))
plt.gca().invert_xaxis() # membalik sumbu-x
# plt.gca().invert_yaxis() # membalik sumbu-y
ax1.grid()
plt.show()
