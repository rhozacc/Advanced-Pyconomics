# TWO PERIOD GENERAL EQUILIBRIUM MODEL 
# WITH TWO TYPES OF AGENTS IN TERMS OF
# ENDOWMENTS AND PREFERENCES (DISCOUNT RATE)

import numpy as np
import matplotlib.pyplot as plt

# KEY PARAMETERS

# PREFERENCE PARAMETERS
    
alpha = np.arange(0.4,0.6,0.1) # discount rate 1 
pi1 = np.arange(0.02,1.0,0.02) # discount rate 2
#pi2 = ((1-pi1)/pi1)


# ENDOWMENTS
# NOTATION 12 - denotes agent 1 period 2 (see consumption function below)

Q11 = np.arange(1.0,2.0,0.05)
Q12 = np.arange(1.0,2.0,0.05)
Q21 = np.arange(1.0,2.0,0.05)
Q22 = np.arange(1.0,2.0,0.05)

# ix function for indexing shapes

Q11x,Q12x,Q21x,Q22x,alphax,pi1x = np.ix_(Q11,Q12,Q21,Q22,alpha,pi1)

# p ratio - Solution to GE

Q11x.shape, Q12x.shape, Q21x.shape, Q22x.shape, alphax.shape, pi1x.shape

p = ((pi1x)*(((alphax*Q11x)+((1-alphax)*Q12x))/((alphax*Q21x)+((1-alphax)*Q22x))))

C11 = (1/(1+pi1x))*(Q11x*p*Q12x)
C12 = (1/p)*(pi1x/(1+pi1x))*(Q11x*p*Q12x)
C21 = (1/(1+(pi1x)))*(Q21x*p*Q22x)
C22 = (1/p)*(pi1x/(1+pi1x))*(Q21x*p*Q22x)


# PLOT 1: VARIATION OF ENDOWMENT of Agent Type 1 in period 1 ---- ":" = does it for all values


p_1 = p[:,0,0,0,0,0]
C11_1 = C11[:,0,0,0,0,0]
C12_1 = C12[:,0,0,0,0,0]
C21_1 = C21[:,0,0,0,0,0]
C22_1 = C22[:,0,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(Q11,p,'k-',color='r',label='Price ratio (p1/p2)')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('Price ratio (p1/p2)')

fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
ax1.plot(Q11,C11_1,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q11,C12_1,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q11,C21_1,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q11,C22_1,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('Consumption ')

#_______________________________________________________________________________________

## PLOT 2: VARIATION OF ENDOWMENT of Agent Type 1 in period 2
#
#r_2   =   r[0,:,0,0,0,0]
#C11_2 = C11[0,:,0,0,0,0]
#C12_2 = C12[0,:,0,0,0,0]
#C21_2 = C21[0,:,0,0,0,0]
#C22_2 = C22[0,:,0,0,0,0]
#
#fig3 = plt.figure(); ax1=fig3.add_subplot(1,1,1)
#ax1.plot(Q12,r_2,'k-',color='r',label='Interest rate')
#ax1.legend(loc='best')
#ax1.set_xlabel('Endowment $Q_{1}^{2}$')
#ax1.set_ylabel('Real interest rate')
#
#fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
#ax1.plot(Q12,C11_2,'k-',color='r',label='$C_{1}^{1}$')
#ax1.plot(Q12,C12_2,'k--',color='r',label='$C_{2}^{1}$')
#ax1.plot(Q12,C21_2,'k-',color='b',label='$C_{1}^{2}$')
#ax1.plot(Q12,C22_2,'k--',color='b',label='$C_{2}^{2}$')
#ax1.legend(loc='best')
#ax1.set_xlabel('Endowment $Q_{1}^{2}$')
#ax1.set_ylabel('Consumption ')
#
## PLOT 3: VARIATION OF PREFERENCE PARAMETER RHO for Agent Type 1 in period 2
#
#r_3   =   r[0,0,0,0,:,0]
#C11_3 = C11[0,0,0,0,:,0]
#C12_3 = C12[0,0,0,0,:,0]
#C21_3 = C21[0,0,0,0,:,0]
#C22_3 = C22[0,0,0,0,:,0]
#
#fig5 = plt.figure(); ax1=fig5.add_subplot(1,1,1)
#ax1.plot(rho1,r_3,'k-',color='r',label='Interest rate')
#ax1.legend(loc='best')
#ax1.set_xlabel(r'Discount rate $\rho_{1}$')
#ax1.set_ylabel('Real interest rate')
#
#fig6 = plt.figure(); ax1=fig6.add_subplot(1,1,1)
#ax1.plot(rho1,C11_3,'k-',color='r',label='$C_{1}^{1}$')
#ax1.plot(rho1,C12_3,'k--',color='r',label='$C_{2}^{1}$')
#ax1.plot(rho1,C21_3,'k-',color='b',label='$C_{1}^{2}$')
#ax1.plot(rho1,C22_3,'k--',color='b',label='$C_{2}^{2}$')
#ax1.legend(loc='best')
#ax1.set_xlabel(r'Discount rate $\rho_{1}$')
#ax1.set_ylabel('Consumption ')
#            