import numpy as np
import pandas as pd

df = pd.read_excel("real_estate.xlsx")

np.set_printoptions(suppress=True)

learning_rate = 0.0000000001

w = np.load("intelligence_w.npy")
b = np.load("intelligence_b.npy")

x = df[['Masa7a' , 'Ghoraf' , 'Doraat_Miah' , '3omr_Albeet' , 'Al_Mantaqa']].values

y = df[['Target_Price' , 'Target_Installment' , 'Target_Deposit']].values

no = np.dot(w, x.T).T + b

loss = no - y
for ai in range(5000000):

  ww = np.dot(loss.T, x)
  bb = np.sum(loss, axis=0)


  w = w - (learning_rate * ww)
  b = b - (learning_rate * b)

  new_no = np.dot(w, x.T).T + b
  loss = new_no - y

  if ai % 1000000 == 0:
    print(f'{ai + 1}-pre is {new_no}')
    print(f'{ai + 1}loss is {loss}')

np.save("intelligence_w.npy", w)
np.save("intelligence_b.npy", b)