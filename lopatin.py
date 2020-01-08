# Program Lopatin Burial History
# Membuat grafik burial history menggunakan metode Lopatin

# import library untuk grafik
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import math

# fungsi mencari gradien
# mencari ketebalan pada formasi 0
def depth0(x, y2, y1, x2, x1):
	return (x - x1) * ((y2 - y1) / (x2 - x1)) + y1

# menvari delta pembentukan formasi pada isotemperature
def deltaTime(y, y2, y1, x2, x1):
	return (y - y1) / ((y2 - y1) / (x2 - x1)) + x1

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

# penyesuaian kedalaman formasi pada dengan umur 0
umur.insert(0, 0)

for i in range (len(formasi)):
	ketebalan[i].insert(0, depth0(umur[0], ketebalan[i][0], ketebalan[i][1], umur[1], umur[2]))

# for i in range(len(formasi)):
# 	for j in range(len(umur)):
# 		print(ketebalan[i][j], end=" ")
# 	print()

maximum = max([max(i) for i in ketebalan])

temp = 20
interval = math.ceil(maximum / 132)

for i in range(0, interval):
	isoT.append(temp)
	temp += 10

# # perhitungan TTi

# TTI = []

# depth_isoT = 0 # kedalaman pada isotemperature
# depth_temp = 20 # temperature pada kedalaman tertentu

# minus = 1

# for h in range(len(formasi) - 1, -1, -1):
# 	for i in range(len(umur) - minus, -1, -1):
# 		j = len(formasi) - 1
# 		while (j >= 0 and depth_isoT < ketebalan[j][0]):
# 			print(i, j)
# 			print(depth_isoT, ketebalan[j][i], ketebalan[j][i-1], umur[i], umur[i-1])
# 			TTI.append(deltaTime(depth_isoT, ketebalan[j][i], ketebalan[j][i-1], umur[i], umur[i-1]))

# 			if (depth_isoT > ketebalan[j][i-1]):
# 				j -= 1

# 			depth_temp += 10
# 			depth_isoT += 132

# 	minus += 1
# # print(TTI)

# plot dalam grafik
# mengubah posisi sumbu-x ke attas
plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.labeltop'] = True

fig, ax1 = plt.subplots()

# label sumbu sekunder
ax2 = ax1.twinx()
ax2.set_ylabel("isotemperature", fontsize=20)
ax2.set_ylim(bottom=20, top=(max(isoT) + ((maximum - ((len(isoT)-1) * 132)) / 132) * 10))

temperature = []

for i in range(len(isoT)):
	int_isot = []
	for j in range(len(umur)):
		int_isot.append(isoT[i])

	ax2.plot(umur, int_isot, color='red', linestyle="--", linewidth=5)
	temperature.append(int_isot)

ax2.invert_yaxis()

for i in range(len(formasi)):
    ax1.plot(umur, ketebalan[i], label=(formasi[i]), linewidth=5)    # line plot
    ax1.scatter(umur, ketebalan[i], s=400)						# scatter plot

# posisi label sumbu primer
ax1.set_xlabel("umur (dalam juta tahun)", fontsize=20)
ax1.xaxis.set_label_position('top')
ax1.set_ylabel("kedalaman", fontsize=20)
ax1.set_ylim(bottom=0, top=maximum)

ax1.invert_yaxis()

ax1.tick_params(axis="x", labelsize=20)
ax1.tick_params(axis="y", labelsize=20)
ax2.tick_params(axis="y", labelsize=20)

np.savetxt("csv/file_name.csv", np.row_stack((umur, ketebalan)), delimiter=",", fmt='%s')
np.savetxt("csv/temperature.csv", np.row_stack((umur, temperature)), delimiter=",", fmt='%s')

# np.savetxt("csv/tt_index.csv", TTI, delimiter=",", fmt='%s')

plt.title("Lopatin Burial History", fontsize=20)
ax1.legend(bbox_to_anchor=(1,0), ncol=4, prop={'size': 20})             # menampilkan legenda
fig.tight_layout()
plt.xlim(min(umur), max(umur))
ax1.invert_xaxis()
ax2.invert_xaxis()

fig.set_size_inches(46.81,33.11)

# plt.gca().invert_xaxis() # membalik sumbu-x
# plt.gca().invert_yaxis() # membalik sumbu-y
# ax1.grid()
plt.savefig("image.jpg", quality=100)
# plt.show()