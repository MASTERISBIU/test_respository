import random

import numpy as np
import matplotlib.pyplot as plt
import pylab
import pylab as pl
a = np.array([1, 2, 3])

b = np.array([[4, 5, 6], [7, 8, 9]])

#imread可以返回一个numpy数组
c = plt.imread('C:/Users/hp/Pictures/v2-4a19c6aa7a299764420b4cbc18d2d6dd_r.jpg')

d = np.linspace(0,50,num=10)

e = np.random.randint(0,100,size=(5,6))

# plt.imshow(c[500:900,2500:2900,:])
# pylab.show()

c_a = np.concatenate((c,c,c),axis=1)
c_9 = np.concatenate((c_a,c_a,c_a),axis=0)
print(b)
print(b.T)
