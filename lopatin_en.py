# Program Lopatin Burial History
# Create burial history diagram using Lopatin method

# import library for graphics
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import math

# input the number of formation
N = int(input("Input the number of formation: "))

# Init'd value parameter
formation   = [] # formation name
thickness = [] # thickness
isoT      = [] # isotemperature

# inputting formation name
for i in range(N):
	formname = str(input("Enter formation " + str(i+1) + " name: \n"))
	formation.append(formname)

print()

# inputting age parameter
age = list(map(float, input("Enter age parameters: \n").split()))

print()

# menerima input thickness formation.
for i in range(len(formation)):
	in_ket = list(map(int, input("Thickness for formation " + formation[i] + ": \n").split()))
	thickness.append(in_ket)

# increment of thickness to depth
for i in range(len(age)):
	sigma = 0
	for j in range(len(formation)):
		sigma += thickness[j][i]
		thickness[j][i] = sigma

for i in range(len(formation)):
	for j in range(len(age)):
		print(thickness[i][j], end=" ")
	print()

maximum = max([max(i) for i in thickness])

temp = 20
interval = math.ceil(maximum / 132)

for i in range(0, interval):
	isoT.append(temp)
	temp += 10

# plot in graphics
# set x-axis label position to top
plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.top'] = True
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.labeltop'] = True

fig, ax1 = plt.subplots()

# secondary label axis
ax2 = ax1.twinx()
ax2.set_ylabel("isotemperature")
ax2.set_ylim(bottom=20, top=max(isoT))

temperature = []

for i in range(len(isoT)):
	int_isot = []
	for j in range(len(age)):
		int_isot.append(isoT[i])

	ax2.plot(age, int_isot, color='red', linestyle="--", linewidth=0.5)
	temperature.append(int_isot)

ax2.invert_yaxis()

for i in range(len(formation)):
    ax1.plot(age, thickness[i], label=(formation[i]))    # line plot
    ax1.scatter(age, thickness[i])						# scatter plot

# posisi label sumbu primer
ax1.set_xlabel("age (million years)")
ax1.xaxis.set_label_position('top')
ax1.set_ylabel("depth")
ax1.set_ylim(bottom=0, top=maximum)

ax1.invert_yaxis()

np.savetxt("csv/file_name.csv", np.row_stack((age, thickness)), delimiter=",", fmt='%s')
np.savetxt("csv/temperature.csv", np.row_stack((age, temperature)), delimiter=",", fmt='%s')

plt.title("Lopatin Burial History")
ax1.legend(bbox_to_anchor=(1,0), ncol=4, prop={'size': 8})             # menampilkan legenda
fig.tight_layout()
plt.xlim(min(age), max(age))
ax1.invert_xaxis()
ax2.invert_xaxis()
# plt.gca().invert_xaxis() # membalik sumbu-x
# plt.gca().invert_yaxis() # membalik sumbu-y
# ax1.grid()
plt.savefig("image.png")
plt.show()
