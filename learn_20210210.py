import numpy as np
import pandas as pd

x = np.array(pd.read_csv('datax.csv'))
y = np.array(pd.read_csv('datay.csv'))

I = len(x[0]) #入力層の次元
H = 4 #隠れ層の次元
O = len(y[0]) #出力層の次元
N = len(x) #データ数

#-1 <= w, b < 0, 0 < w, b <= 1となるようなパラメータw, bの生成
#0 < w, b <= 1
w_ = -np.random.random((H, I)) + 1
b_ = -np.random.random(H) + 1
w = -np.random.random((O, H)) + 1
b = -np.random.random(O) + 1
#ランダムに±1のどちらかを乗ずる
random = [-1 ,1]
w_ *= np.random.choice(random, (H, I))
b_ *= np.random.choice(random, H)
w *= np.random.choice(random, (O, H))
b *= np.random.choice(random, O)

#結果格納用
u_ = np.empty((N, H))
h =  np.empty((N, H))
u = np.empty((N, O))
y_ = np.empty((N, O))

#y_の計算
for k in range(N):
	for i in range(H):
		u_[k][i] = np.dot(w_[i], x[k]) + b_[i]
	#f = tanh(u)
	h[k] = np.tanh(u_[k])

	for i in range(O):
		u[k][i] = np.dot(w[i], h[k]) + b[i]
	#g = 1
	y_[k] = u[k]

print(y_)
