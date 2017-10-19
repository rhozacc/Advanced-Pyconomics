# TWO STATE GENERAL EQUILIBRIUM MODEL 
# WITH TWO TYPES OF AGENTS IN TERMS OF
# ENDOWMENTS AND PREFERENCES (DISCOUNT RATE)

import numpy as np
import matplotlib.pyplot as plt

# KEY PARAMETERS

# PREFERENCE PARAMETERS
    
alpha = np.arange(0.5,1.00,0.05) # share of type 1
pi = np.arange(0.5,1.00,0.05) # probability of state 1

# ENDOWMENTS
# NOTATION 12 - denotes agent 1 period 2 (see consumption function below)

Q11 = np.arange(1.0,2.01,0.05)
Q12 = np.arange(1.0,2.01,0.05)
Q21 = np.arange(1.0,2.01,0.05)
Q22 = np.arange(1.0,2.01,0.05)

# ix function for indexing shapes 12 -individual 1,state 2

Q11x,Q12x,Q21x,Q22x,alphax,pix = np.ix_(Q11,Q12,Q21,Q22,alpha,pi)

# P2/P1 = P2 = P - SOLUTION TO GE

Q11x.shape, Q12x.shape, Q21x.shape, Q22x.shape, alphax.shape, pix.shape
P  = (1-pix)/(pix)* (alphax*Q11x+(1-alphax)*Q21x)/(alphax*Q12x+(1-alphax)*Q22x)

C11 = pix*(Q11x+P*Q12x)
C12 = (1-pix)*(Q11x/P+Q12x)
C21 = pix*(Q21x+P*Q22x)
C22 = (1-pix)*(Q21x/P+Q22x)


# PLOT 1: VARIATION OF ENDOWMENT of Agent Type 1 in state 1


P_1 = P[:,0,0,0,0,0]
C11_1 = C11[:,0,0,0,0,0]
C12_1 = C12[:,0,0,0,0,0]
C21_1 = C21[:,0,0,0,0,0]
C22_1 = C22[:,0,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(Q11,P_1,'k-',color='r',label='Price in state 2')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('$P_{2}$')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig1_P_Q11.png')   # save the figure to file


            
fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
ax1.plot(Q11,C11_1,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q11,C12_1,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q11,C21_1,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q11,C22_1,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{1}$')
ax1.set_ylabel('Consumption ')
#fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig2_C_Q11.png')   # save the figure to file

# PLOT 2: VARIATION OF ENDOWMENT of Agent Type 1 in state 2

P_2   =   P[0,:,0,0,0,0]
C11_2 = C11[0,:,0,0,0,0]
C12_2 = C12[0,:,0,0,0,0]
C21_2 = C21[0,:,0,0,0,0]
C22_2 = C22[0,:,0,0,0,0]

fig3 = plt.figure(); ax1=fig3.add_subplot(1,1,1)
ax1.plot(Q12,P_2,'k-',color='r',label='Price in state 2')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{2}^{1}$')
ax1.set_ylabel('$P_{2}$')
#fig3.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig3_P_Q12.png')   # save the figure to file

fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
ax1.plot(Q12,C11_2,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q12,C12_2,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q12,C21_2,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q12,C22_2,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{2}^{1}$')
ax1.set_ylabel('Consumption ')
#fig4.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig4_C_Q12.png')   # save the figure to file

# PLOT 3: VARIATION OF SHARE of Agent Type 1 ASSUMING TYPE 2 AGENT HAS HIGH ENDOWMENT IN STATE 1

P_3   =   P[20,0,0,0,:,0]
C11_3 = C11[20,0,0,0,:,0]
C12_3 = C12[20,0,0,0,:,0]
C21_3 = C21[20,0,0,0,:,0]
C22_3 = C22[20,0,0,0,:,0]

fig5 = plt.figure(); ax1=fig5.add_subplot(1,1,1)
ax1.plot(alpha,P_3,'k-',color='r',label='Price in state 2')
ax1.legend(loc='best')
ax1.set_xlabel(r'Share of type-1 agents $\alpha^{1}$')
ax1.set_ylabel('$P_{2}$')
#fig5.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig5_P_alpha1.png')   # save the figure to file

fig6 = plt.figure(); ax1=fig6.add_subplot(1,1,1)
ax1.plot(alpha,C11_3,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(alpha,C12_3,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(alpha,C21_3,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(alpha,C22_3,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Share of type-1 agents $\alpha^{1}$')
ax1.set_ylabel('Consumption ')
#fig6.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig6_C_alpha1.png')   # save the figure to file

# PLOT 4: VARIATION OF PROBABILITY OF STATE 1 ASSUMING TYPE 2 AGENT HAS HIGH ENDOWMENT IN STATE 1

P_4   =   P[20,0,0,0,0,:]
C11_4 = C11[20,0,0,0,0,:]
C12_4 = C12[20,0,0,0,0,:]
C21_4 = C21[20,0,0,0,0,:]
C22_4 = C22[20,0,0,0,0,:]

fig7 = plt.figure(); ax1=fig7.add_subplot(1,1,1)
ax1.plot(pi,P_4,'k-',color='r',label='Price in state 2')
ax1.legend(loc='best')
ax1.set_xlabel(r'Probability of state 1 $\pi_{1}$')
ax1.set_ylabel('$P_{2}$')
#fig7.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig7_P_pi1.png')   # save the figure to file

fig8 = plt.figure(); ax1=fig8.add_subplot(1,1,1)
ax1.plot(pi,C11_4,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(pi,C12_4,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(pi,C21_4,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(pi,C22_4,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Probability of state 1 $\pi_{1}$')
ax1.set_ylabel('Consumption ')
#fig8.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex2_fig8_C_pi1.png')   # save the figure to file