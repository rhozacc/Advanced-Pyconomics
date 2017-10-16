# TWO PERIOD GENERAL EQUILIBRIUM MODEL # WITH TWO TYPES OF AGENTS IN TERMS OF
# ENDOWMENTS AND PREFERENCES (DISCOUNT RATE)


import numpy as np
import matplotlib.pyplot as plt


# KEY PARAMETERS
# PREFERENCE PARAMETERS
rho1 = np.arange(0.0,0.2,0.02) # discount rate 1 
rho2 = np.arange(0.0,0.2,0.02) # discount rate 2


# ENDOWMENTS# NOTATION 12 - denotes agent 1 period 2 (see consumption function below); (minimum,maximum,step)
Q11 = np.arange(1.0,2.0,0.05)
Q12 = np.arange(1.0,2.0,0.05)
Q21 = np.arange(1.0,2.0,0.05)
Q22 = np.arange(1.0,2.0,0.05)


# ix function for indexing shapes
Q11x,Q12x,Q21x,Q22x,rho1x,rho2x = np.ix_(Q11,Q12,Q21,Q22,rho1,rho2)


# INTEREST RATE - SOLUTION TO GE
Q11x.shape, Q12x.shape, Q21x.shape, Q22x.shape, rho1x.shape, rho2x.shape
r  = -1 + ((1+rho1x)/(2+rho1x)*Q12x+(1+rho2x)/(2+rho2x)*Q22x)/(Q11x/(2+rho1x)+(Q21x/(2+rho2x))

C11 = (1+rho1x)/((2+rho1x)*(Q11x+Q12x/(1+r)))
C12 = (1+r)/(2+rho1x)*(Q11x+Q12x/(1+r))
C21 = (1+rho2x)/(2+rho2x)*(Q21x+Q22x/(1+r))
C22 = (1+r)/(2+rho2x)*(Q21x+Q22x/(1+r))


# PLOT 1: VARIATION OF ENDOWMENT of Agent Type 1 in period 1
r_1 = r[:,0,0,0,0,0]
C11_1 = C11[:,0,0,0,0,0]
C12_1 = C12[:,0,0,0,0,0]
C21_1 = C21[:,0,0,0,0,0]
C22_1 = C22[:,0,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(Q11,r_1,'k-',color='r',label='Interest rate')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('Real interest rate')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig1_r_Q11.png')   # save the figure to file

fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
ax1.plot(Q11,C11_1,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q11,C12_1,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q11,C21_1,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q11,C22_1,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('Consumption ')
#fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig2_C_Q11.png')   # save the figure to file


# PLOT 2: VARIATION OF ENDOWMENT of Agent Type 1 in period 2
r_2   =   r[0,:,0,0,0,0]
C11_2 = C11[0,:,0,0,0,0]
C12_2 = C12[0,:,0,0,0,0]
C21_2 = C21[0,:,0,0,0,0]
C22_2 = C22[0,:,0,0,0,0]

fig3 = plt.figure(); ax1=fig3.add_subplot(1,1,1)
ax1.plot(Q12,r_2,'k-',color='r',label='Interest rate')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{2}$')
ax1.set_ylabel('Real interest rate')
#fig3.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig3_r_Q12.png')   # save the figure to file

fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
ax1.plot(Q12,C11_2,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q12,C12_2,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q12,C21_2,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q12,C22_2,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{2}$')
ax1.set_ylabel('Consumption ')
#fig4.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig4_C_Q12.png')   # save the figure to file


# PLOT 3: VARIATION OF PREFERENCE PARAMETER RHO for Agent Type 1 in period 2
r_3   =   r[0,0,0,0,:,0]
C11_3 = C11[0,0,0,0,:,0]
C12_3 = C12[0,0,0,0,:,0]
C21_3 = C21[0,0,0,0,:,0]
C22_3 = C22[0,0,0,0,:,0]

fig5 = plt.figure(); ax1=fig5.add_subplot(1,1,1)
ax1.plot(rho1,r_3,'k-',color='r',label='Interest rate')
ax1.legend(loc='best')
ax1.set_xlabel(r'Discount rate $\rho_{1}$')
ax1.set_ylabel('Real interest rate')
#fig5.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig5_r_rho1.png')   # save the figure to file

fig6 = plt.figure(); ax1=fig6.add_subplot(1,1,1)
ax1.plot(rho1,C11_3,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(rho1,C12_3,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(rho1,C21_3,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(rho1,C22_3,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Discount rate $\rho_{1}$')
ax1.set_ylabel('Consumption ')
#fig6.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig6_C_rho1.png')   # save the figure to file            
