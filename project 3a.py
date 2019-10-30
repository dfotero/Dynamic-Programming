import numpy as np
import random
# -*- coding: utf-8 -*-
"""
Policy Improvement

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
            

x=np.zeros((N,N))
for i in range(N):
    for j in range(N):
        x[i,j]=P[policy[i],i,j]


x=np.identity(N)-alpha*x

y=np.zeros(N)
for i in range(N):
    y[i]=R[i,policy[i]]

value=np.linalg.solve(x,y)

areDif=1


"""
Policy improvement algorithm
"""

while areDif==1:
    
    theVal=np.zeros(N)
    theDec=np.zeros(N).astype(int)
    
    for i in range(N):
        theMaxV=0
        theMax=-1
        
        for a in range(A):
            v=R[i,a]+alpha*np.matmul(P[a,i,:],value)
            if v>theMaxV:
                theMaxV=v
                theMax=a
        
        theVal[i]=theMaxV
        theDec[i]=theMax
    
    theDif=theVal-value
    theDif=np.around(theDif,decimals=5)
    
    if theDif.sum()==0:
        
        areDif=0
        value=theVal
        policy=theDec
    
    else:
        
        policy=theDec
        x=np.zeros((N,N))
        for i in range(N):
            for j in range(N):
                x[i,j]=P[policy[i],i,j]
        
        x=np.identity(N)-alpha*x
        
        y=np.zeros(N)
        for i in range(N):
            y[i]=R[i,policy[i]]
        
        value=np.linalg.solve(x,y)   
        
policy=policy+1

print("The expected maximum discounted value and the optimal decisions are:")
for i in range(N):
    print(str(i+1)+": val=" +str(np.around(value[i],decimals=4))+" Decision=" + str(policy[i]))
