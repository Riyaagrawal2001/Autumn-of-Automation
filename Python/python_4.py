import numpy as np

X = np.random.normal(0.0,1.0,(20,20))    
print(X)

y = np.random.randint(2,100,size=(20,1),dtype=np.int32)

A = np.dot(X.T,X)
B = np.linalg.inv(A)
C = np.dot(B,X.T)

theta = np.dot(C,y)