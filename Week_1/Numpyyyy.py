import numpy as np

a = np.random.normal(0 , 1 , size=(5,5))
print(a)
a= np.where(a > 0.09 , a **2 , a)
a= np.where(a < 0.09 , 42 , a)

print(a[:,3])


