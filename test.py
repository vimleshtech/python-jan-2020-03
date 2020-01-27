import numpy as np
x = np.arange(1,10)

y = x.reshape(-1,3)  
print(y)
print(y[1,:])

print(y[1,1])

