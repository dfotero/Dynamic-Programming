from gurobipy import *
import numpy as np

# -*- coding: utf-8 -*-
"""
LP Method

Created on Mon Apr 22 11:33:00 2019

@author: dfotero
"""

"""
Initialize the model
"""
N= 10
A = 5
R=np.zeros((N,A))
P=np.zeros((A,N,N))
policy=np.zeros(N)
policy=policy.astype(int)
value=np.zeros(N)
alpha=0.9

for i in range(N):
    for j in range(A):
        R[i,j]=random.randint(0,10)
        for k in range(N):
            P[j,i,k]=random.randint(0,10)
            

theSum=P.sum(axis=2)

for a in range(A):
    for i in range(N):
        for j in range(N):
            P[a,i,j]=P[a,i,j]/theSum[a,i]
            

"""
LP Formulation
"""

m = Model("LP Sol")
val=m.addVars(range(N),name="theV")
m.setObjective(sum(val), GRB.MINIMIZE)

for i in range(N):
    for a in range(A):
        theP={j:P[a,i,j] for j in range(N)}
        m.addConstr((val[i] >= R[i,a]+alpha*val.prod(theP)), name="CapacityConstrain" + str(i) + str(a))

m.optimize()

for i in range(N):
    value[i]=m.getVars()[i].X

for i in range(N):
    for a in range(A):
        theVal=R[i,a]+alpha*np.matmul(P[a,i,:],value)
        if np.around(theVal-value[i],decimals=5)==0:
            policy[i]=a+1

print("The expected maximum discounted value and the optimal decisions are:")
for i in range(N):
    print(str(i+1)+": val=" +str(np.around(value[i],decimals=4))+" Decision=" + str(policy[i]))