import numpy as np
import pandas as pd

df = pd.read_excel("real_estate.xlsx")

np.set_printoptions(suppress=True)

learning_rate = 0.000000001



w = np.load("intelligence_w.npy2.npy")
b = np.load("intelligence_b.npy2.npy")

x = df[['Masa7a' , 'Ghoraf' , 'Doraat_Miah' , '3omr_Albeet' , 'Al_Mantaqa']].values
y = df[['Target_Price' , 'Target_Installment' , 'Target_Deposit']].values

x_mean = np.mean(x, axis=0)

x_std = np.std(x, axis=0)

scaled_x = (x - x_mean) / x_std

no = np.dot(w, x.T) + b
loss = no - y.T


for ai in range(50000):

  ww = np.dot(loss, x)
  bb = np.sum(loss, axis=1, keepdims=True)


  w = w - (learning_rate * ww)
  b = b - (learning_rate * bb)

  new_no = np.dot(w, x.T) + b
  loss = new_no - y.T

  if ai % 5000 == 0:
    print("result:")
    print(f'{(ai -1 ) + 1}-price is {new_no[0][0]:,.2f} | loon is {new_no[1][0]:,.2f} | 3rboon is {new_no[2][0]:,.2f}')

    mae_loss = np.mean(np.abs(loss))
    print(f'{(ai - 1) + 1}-the mean loss is {mae_loss:,.2f}')
    print()

np.save("intelligence_w.npy2", w)
np.save("intelligence_b.npy2", b)