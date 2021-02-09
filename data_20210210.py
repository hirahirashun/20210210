import numpy as np
import math
import csv

I = 3 #入力層の次元
H = 4 #隠れ層の次元
O = 3 #出力層の次元
N = 100 #データ数

x = np.random.uniform(0, 10, (N, I)) #N × I の配列に0<x<10なるxを入力
y = np.random.random((N, O)) #データ格納用(0から1の範囲のノイズ付与)

#yの計算
for k in range (N):
	for j in range(O):
		for i in range (I):
			if i%3 == 0:
				y[k][j] += 1/(j + 1)*math.sin(x[k][i])
			elif i%3 == 1:
				y[k][j] += (-1)**j * (1/ math.e)**x[k][i]
			else:
				y[k][j] += (-1)**(j + 1) * math.log(x[k][i] + 1)

with open('datax.csv', 'w') as file:
	w = csv.writer(file, lineterminator = '\n')
	w.writerow(['x'+ str(i) for i in range(I)])
	w.writerows(x)

with open('datay.csv', 'w') as file:
	w = csv.writer(file, lineterminator = '\n')
	w.writerow(['y'+ str(i) for i in range(O)])
	w.writerows(y)





