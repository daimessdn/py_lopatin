# Program Lopatin Burial History
# Membuat grafik burial history menggunakan metode Lopatin

# import library untuk grafik
import matplotlib
import matplotlib.pyplot as plt

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
	in_ket = list(map(float, input("Masukkan ketebalan untuk formasi " + formasi[i] + ": \n").split()))
	ketebalan.append(in_ket)

# penyesuaian kedalaman formasi dengan ketebalan
for i in range(len(formasi)-1, -1, -1):
	sigma = 0
	for j in range(len(umur)):
		if (ketebalan[i][j] == -1):
			ketebalan[i][j] = ketebalan[i][j-1] - gradien(ketebalan[i+1][j-1], ketebalan[i+1][j], umur[j-1], umur[j]) * (umur[j-1] - umur[j])
		else:
			ketebalan[i][j] += sigma
			sigma = ketebalan[i][j]

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

ax2 = ax1.twinx()
ax2.set_ylabel("isotemperature")
ax2.set_ylim(bottom=20, top=max(isoT))
for i in range(len(isoT)):
	int_isot = []
	for j in range(len(umur)):
		int_isot.append(isoT[i])

	ax2.plot(umur, int_isot, color='red', linestyle="--", linewidth=1)

for i in range(len(formasi)):
    ax1.plot(umur, ketebalan[i], label=(formasi[i]))    # line plot
    ax1.scatter(umur, ketebalan[i])						# scatter plot

ax1.set_title("Umur (dalam juta tahun)")
ax1.set_ylabel("Kedalaman")
ax1.set_ylim(bottom=0, top=maximum)


ax1.legend(bbox_to_anchor=(1,0), ncol=4, prop={'size': 8.5})             # menampilkan legenda
fig.tight_layout()
plt.xlim(0, max(umur))
# plt.gca().invert_xaxis() # membalik sumbu-x
# plt.gca().invert_yaxis() # membalik sumbu-y
# plt.grid()
plt.show()

