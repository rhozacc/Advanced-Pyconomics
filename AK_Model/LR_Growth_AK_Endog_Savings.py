# LR Growth in AK Model with Endogenous Savings rate

# THREE PARTS
# 1. STEADY STATE AND BALANCED GROWTH PATH

import numpy as np
import matplotlib.pyplot as plt


# KEY PARAMETERS
special:np.random

    # PRODUCTION FUNCTION PARAMETER FOR COBB-DOUGLAS P.F. with C.R.S.: Y_{t}=K_{t}^alpha * (A_{t}*L_{t}) ^(1-alpha)
    
A = np.arange(0.05,0.15,0.01) 

    # Utility function 
    
rho = np.arange(0.0,0.1,0.01) 
sigma = np.arange(0.51,2.61,0.25) 
    
    
    # LAW OF MOTION FOR CAPITAL PARAMETER -- deprecitation rate: K_{t+1} = K_{t}*(1-delta)+I_{t}
    
delta = np.arange(0.06,0.16,0.02)  


# ix function for indexing 

Ax,rhox,deltax,sigmax = np.ix_(A,rho,delta,sigma)

# reshape

Ax.shape, rhox.shape, deltax.shape, sigmax.shape

# CALCULATION OF GROWTH RATES

gamma_c = (Ax-deltax-rhox)/sigmax

# Figure 1: Productivity (A) and growth rate
          
gamma1  = gamma_c[:,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(A,gamma1,'k-',color='red',label=r'$\gamma_{C}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Production function parameter $A$')
ax1.set_ylabel(r'Growth rate')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/hw4_AK_fig1_A.png')   # save the figure to file

# Figure 2: Patience (rho) and growth rate
          
gamma2  = gamma_c[4,:,0,0]

fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
ax1.plot(rho,gamma2,'k-',color='red',label=r'$\gamma_{C}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Discount rate $\rho$')
ax1.set_ylabel(r'Growth rate')
#fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/hw4_AK_fig2_rho.png')   # save the figure to file

# Figure 3: Depreciation rate (delta) and growth rate
          
gamma3  = gamma_c[4,0,:,0]

fig3 = plt.figure(); ax1=fig3.add_subplot(1,1,1)
ax1.plot(delta,gamma3,'k-',color='red',label=r'$\gamma_{C}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Discount rate $\delta$')
ax1.set_ylabel(r'Growth rate')
#fig3.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/hw4_AK_fig3_delta.png')   # save the figure to file

# Figure 3: Depreciation rate (delta) and growth rate
          
gamma4  = gamma_c[4,0,0,:]

fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
ax1.plot(delta,gamma3,'k-',color='red',label=r'$\gamma_{C}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Discount rate $\delta$')
ax1.set_ylabel(r'Growth rate')
#fig4.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/hw4_AK_fig4_sigma.png')   # save the figure to file
