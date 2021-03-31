import numpy as np

x = np.array([(1,0),(1,1),(1,2),(1,4),(1,5),(1,6)])
y = np.array([0,1,2,3,4,5])
xT = x.transpose()

result = np.matmul(np.linalg.inv(np.matmul(xT,x)),np.matmul(xT,y))

print(round(result[0],10),round(result[1],10))