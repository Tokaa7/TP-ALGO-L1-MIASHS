"""

    TP6 - 1.1 Les matrices avec numpy

"""

import numpy as np

A=np.array([[1,-1,0],[0,1,-1],[1,1,1]],dtype=float)

B=np.array([[1,1,1,-3],[2,-2,2,5],[1,2,3,1],[-1,2,-2,-4]],dtype=float)

A_diag=np.diag([1,-1,1])
B_diag=np.diag([1,-1,1,-1])

print("\n A :\n",A)
print("\n B :\n",B)
print("\n A_diag :\n",A_diag)
print("\n B_diag :\n",B_diag)

A+=A_diag
B+=B_diag

print("\n A+A_diag :\n",A)
print("\n B+B_diag :\n",B)

A2=np.copy(A*2)
B2=np.copy(B*2)

print("\n A2 :\n",A2)
print("\n B2 :\n",B2)

for i in range(len(A2)):
    A2[i]*=(i+1)
for i in range(len(B2)):
    B2[i]*=(i+1)
    
print("\n A2 :\n",A2)
print("\n B2 :\n",B2)

for i in range(len(A2)) :
    A2[i,1]/=3
for i in range(len(B2)):
    B2[i,1]/=3

print("\n A2 :\n",A2)
print("\n B2 :\n",B2)

A2[[0,2]]=A2[[2,0]]
B2[[0,2]]=B2[[2,0]]

print("\n A2 :\n",A2)
print("\n B2 :\n",B2)

A2[:,[0,2]]=A2[:,[2,0]]
B2[:,[0,2]]=B2[:,[2,0]]

print("\n A2 :\n",A2)
print("\n B2 :\n",B2)
#A FAIRE