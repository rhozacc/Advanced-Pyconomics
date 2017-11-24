# =============================================================================
# AK Model - Homework 4 
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

T = 100
index_set = range(0,T+1)

beta = np.ones(T+1)
for t in index_set[10:]:
    beta[t] = 0.3

delta = 0.1* np.ones(T+1)
gamma = 0.5*np.ones(T+1)
gamma_c = np.ones(T+1)
A = np.ones(T+1)

#Aggregate vars
#A = np.zeros(T+1)
K = np.zeros(T+1)
s = np.zeros(T+1)
Y = np.zeros(T+1)
C = np.zeros(T+1)
I = np.zeros(T+1)

#init vals
s[0] = (((beta[0]*(1-delta[0]+A[0]))**(1/gamma[0]))-1+delta[0])/A[0]
K[0] = s[0]*A[0]*gamma[0]
Y[0] = A[0]*K[0]
C[t] = ((((1-delta[0])*K[0])+A[0]*K[0]))

# Law of motion
for t in index_set[1:]:
    
    C[t] = ((((1-delta[t-1])*K[t-1])+A[t-1]*K[t]))
    s[t] = (((beta[t]*(1-delta[t]+A[t]))**(1/gamma[t]))-1+delta[t])/A[t]
    K[t] = s[t]*A[t]*gamma[t]
    Y[t] = A[t]*K[t]
  
print(Y)

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(index_set,s,'k-',color='r',label=r's')
ax1.plot(index_set,Y,'k-',color='k',label=r'Y')
#ax1.plot(index_set,c_tilde,'k-',color='b',label=r'$\tilde{c}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time')
ax1.set_ylabel(r'Variables')