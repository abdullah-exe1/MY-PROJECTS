import numpy as np
import pandas as pb

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

learning_rate = 0.001

trueY = np.array([99.43, 75.34, 1000000.32])

w = np.array([
    [0.3,  0.2,  0.2, -1.2, -0.6],  
    [0.1, -0.4,  0.8,  0.5, -0.2],  
    [-0.5, 0.6, -0.1,  0.2,  0.4]   
])

x = np.array(
    [0.12, 0.1232, 1.3, 0.554, 0.43]
    ) 

b = np.array(
    [1]
    )



no = np.dot(w, x) + b
no1= sigmoid(no)


loss = no1 - trueY


w = np.load("intelligence_w.npy")
b = np.load("intelligence_b.npy")

for ai in range(50000):

    new_w = np.outer(loss * learning_rate, x)


    w = w - new_w
    b = b - learning_rate * loss

    new_no = np.dot(w, x) + b

    loss = new_no - trueY
    if ai % 1000 == 0:
        print(f'{ai +1}-Production is {new_no}')
        print(f'{ai + 1}-loss is {loss}')


np.save("intelligence_w.npy", w)
np.save("intelligence_b.npy", b)