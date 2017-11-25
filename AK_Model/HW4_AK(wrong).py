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
delta = 0.1* np.ones(T+1)
gamma = 0.5*np.ones(T+1)
A = np.ones(T+1)

for t in index_set[10:]:
   A[t] = 1





# Key variables


beta = np.ones(T+1)


gamma_c = np.ones(T+1)

# aggregate values

K = np.zeros(T+1)
s = np.zeros(T+1)
Y = np.zeros(T+1)
C = np.zeros(T+1)
I = np.zeros(T+1)

##


# INITIAL VALUES

gamma_c[0] = ((beta[0]*1-delta[0]+Y[0])**(1/gamma[0]))-1
s[0] = (((beta[0]*(1-delta[0]+A[0]))**(1/gamma[0]))-1+delta[0])/A[0]
K[0] = s[0]*A[0]*gamma[0]
Y[0] = A[0]*K[0]






# THE LAW OF MOTION FOR CAPITAL PER EFFECTIVE LABOR

for t in index_set[1:]:
    
    gamma_c[t] = ((beta[t-1]*1-delta[t-1]+Y[t-1])**(1/gamma[t-1]))-1
    
    s[t] = (((beta[t]*(1-delta[t]+A[t]))**(1/gamma[t]))-1+delta[t])/A[t]
    K[t] = s[t-1]*A[t]*gamma[t-1]
    Y[t] = A[t-1]*K[t-1]
    gamma_c[t] = ((beta[t]*1-delta[t]+Y[t])**(1/gamma[t]))-1
    
    
    
print (gamma_c)



fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(index_set,s,'k-',color='r',label=r'$\tilde{k}$')
ax1.plot(index_set,Y,'k-',color='k',label=r'$\tilde{y}$')
#ax1.plot(index_set,c_tilde,'k-',color='b',label=r'$\tilde{c}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time')
ax1.set_ylabel(r'Variables per effective labor')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex4SS_fig1_s_k_tilde.png')   # save the figure to file
#
#fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
#ax1.plot(index_set,k,'k-',color='r',label=r'$k$')
#ax1.plot(index_set,y,'k-',color='k',label=r'$y$')
#ax1.plot(index_set,c,'k-',color='b',label=r'$y$')
#ax1.legend(loc='best')
#ax1.set_xlabel(r'Time')
#ax1.set_ylabel(r'Variables per unit of labor')
##fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex4SS_fig2_s_k.png')   # save the figure to file
#
#            
#            