# SOLOW SWAN MODEL with GROWTH OF TECHNOLOGY AND 
# POPULATION
# BALANCED GROWTH PATH AND TRANSITION DYNAMICS


# THREE PARTS
# 1. STEADY STATE AND BALANCED GROWTH PATH

import numpy as np
import matplotlib.pyplot as plt

# Number of time periods

T = 100
index_set = range(0,T+1)

# Basic parameter values

alpha = 1/3*np.ones(T+1)
s = 0.25*np.ones(T+1)
for t in index_set[10:]:
    s[t] = 0.3


delta = 0.1* np.ones(T+1)
gamma_l = 0.01*np.ones(T+1)
gamma_a = 0.02*np.ones(T+1)

# Key variables

# per effective labor

k_tilde = np.zeros(T+1)
y_tilde = np.zeros(T+1)
c_tilde = np.zeros(T+1)
i_tilde = np.zeros(T+1)

gamma_k_tilde = np.zeros(T+1)

# per unit of labor

y = np.zeros(T+1)
k = np.zeros(T+1)
c = np.zeros(T+1)
i = np.zeros(T+1)

# aggregate values

Y = np.zeros(T+1)
K = np.zeros(T+1)
C = np.zeros(T+1)
I = np.zeros(T+1)
A = np.zeros(T+1)
L = np.zeros(T+1)

# INITIAL VALUES

k_tilde[0] = (s[0]/(delta[0]+gamma_l[0]+gamma_a[0]))**(1.0/(1.0-alpha[0]))
y_tilde[0]= k_tilde[0]**alpha[0]
c_tilde[0] = y_tilde[0]-s[0]*y_tilde[0]
A[0] = 1.0
k[0] = A[0]*k_tilde[0]
y[0] = k[0]**alpha[0]
c[0] = k[0]**alpha[0]


# THE LAW OF MOTION FOR CAPITAL PER EFFECTIVE LABOR

for t in index_set[1:]:
    k_tilde[t] =s[t-1]*k_tilde[t-1]**alpha[t-1]+(1.0-delta[t-1]-gamma_l[t-1]-gamma_a[t-1])*k_tilde[t-1]

    y_tilde[t] = k_tilde[t]**alpha[t]
    c_tilde[t] = y_tilde[t]-s[t]*y_tilde[t]

    gamma_k_tilde[t] = (k_tilde[t]-k_tilde[t-1])/k_tilde[t-1]

    A[t] = A[t-1]*(1+gamma_a[t])
    
    k[t] = k_tilde[t]*A[t]
    y[t] = y_tilde[t]*A[t]
    c[t] = c_tilde[t]*A[t]

    L[t] = L[t-1]*(1+gamma_l[t])
    
    K[t] = k[t]*L[t]
    Y[t] = y[t]*L[t]


fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(index_set,k_tilde,'k-',color='r',label=r'$\tilde{k}$')
ax1.plot(index_set,y_tilde,'k-',color='k',label=r'$\tilde{y}$')
ax1.plot(index_set,c_tilde,'k-',color='b',label=r'$\tilde{c}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time')
ax1.set_ylabel(r'Variables per effective labor')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex4SS_fig1_s_k_tilde.png')   # save the figure to file

fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
ax1.plot(index_set,k,'k-',color='r',label=r'$k$')
ax1.plot(index_set,y,'k-',color='k',label=r'$y$')
ax1.plot(index_set,c,'k-',color='b',label=r'$y$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time')
ax1.set_ylabel(r'Variables per unit of labor')
#fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex4SS_fig2_s_k.png')   # save the figure to file

            
            