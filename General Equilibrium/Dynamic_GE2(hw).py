# TWO PERIOD GENERAL EQUILIBRIUM MODEL 
# WITH TWO TYPES OF AGENTS IN TERMS OF
# ENDOWMENTS AND PREFERENCES (DISCOUNT RATE)
import numpy as np
import matplotlib.pyplot as plt


# KEY PARAMETERS

# PREFERENCE PARAMETERS
    
alpha = np.arange(0.4,0.6,0.1) # share of agents
pi1 = np.arange(0.1,1.0,0.1) # prob1
pi2 = ((1-pi1)/pi1) #prob2


# ENDOWMENTS
# NOTATION 12 - denotes agent 1 period 2 (see consumption function below)

Q11 = np.arange(1.0,2.0,0.05)
Q12 = np.arange(1.0,2.0,0.05)
Q21 = np.arange(1.0,2.0,0.05)
Q22 = np.arange(1.0,2.0,0.05)

# ix function for indexing shapes

Q11x,Q12x,Q21x,Q22x,alphax,pi1x,pi2x = np.ix_(Q11,Q12,Q21,Q22,alpha,pi1,pi2)

# p ratio - Solution to GE

Q11x.shape, Q12x.shape, Q21x.shape, Q22x.shape, alphax.shape, pi1x.shape, pi2x.shape

p = ((pi2x/pi1x)*(((alphax*Q11x)+((1-alphax)*Q12x))/((alphax*Q21x)+((1-alphax)*Q22x))))

C11 = (1/(1+(pi2x/pi1x)))*(Q11x*p*Q12x)
C12 = ((1/p)*((pi2x/pi1x))/(1+(pi2x/pi1x)))*(Q11x*p*Q12x)
C21 = (1/(1+((pi2x/pi1x))))*(Q21x*p*Q22x)
C22 = ((1/p)*((pi2x/pi1x)))/(1+(pi2x/pi1x))*(Q21x*p*Q22x)



# PLOT 1: VARIATION OF ENDOWMENT of Agent Type 1 in period 1 ; added extra dim (,0)

p_1 = p[:,0,0,0,0,0,0]
C11_1 = C11[:,0,0,0,0,0,0]
C12_1 = C12[:,0,0,0,0,0,0]
C21_1 = C21[:,0,0,0,0,0,0]
C22_1 = C22[:,0,0,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(Q11, p_1,'k-',color='r',label='Price ratio (p2/p1)')
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

# PLOT 2: VARIATION OF ENDOWMENT of Agent Type 1 in period 2

p_2   =   p[0,:,0,0,0,0,0]
C11_2 = C11[0,:,0,0,0,0,0]
C12_2 = C12[0,:,0,0,0,0,0]
C21_2 = C21[0,:,0,0,0,0,0]
C22_2 = C22[0,:,0,0,0,0,0]

fig3 = plt.figure(); ax1=fig3.add_subplot(1,1,1)
ax1.plot(Q12,p_2,'k-',color='r',label='Price ratio (p2/p1)')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{2}$')
ax1.set_ylabel('Price ratio (p2/p1)')

fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
ax1.plot(Q12,C11_2,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(Q12,C12_2,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(Q12,C21_2,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(Q12,C22_2,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel('Endowment $Q_{1}^{2}$')
ax1.set_ylabel('Consumption ')

# PLOT 3: VARIATION OF PREFERENCE PARAMETER alpha for Agent Type 1 in period 2

p_3   =   p[0,0,0,0,:,0,0]
C11_3 = C11[0,0,0,0,:,0,0]
C12_3 = C12[0,0,0,0,:,0,0]
C21_3 = C21[0,0,0,0,:,0,0]
C22_3 = C22[0,0,0,0,:,0,0]

fig5 = plt.figure(); ax1=fig5.add_subplot(1,1,1)
ax1.plot(alpha,p_3,'k-',color='r',label='price ratio')
ax1.legend(loc='best')
ax1.set_xlabel("Alpha")
ax1.set_ylabel("Price ratio (p2/p1)")

fig6 = plt.figure(); ax1=fig6.add_subplot(1,1,1)
ax1.plot(alpha,C11_3,'k-',color='r',label='$C_{1}^{1}$')
ax1.plot(alpha,C12_3,'k--',color='r',label='$C_{2}^{1}$')
ax1.plot(alpha,C21_3,'k-',color='b',label='$C_{1}^{2}$')
ax1.plot(alpha,C22_3,'k--',color='b',label='$C_{2}^{2}$')
ax1.legend(loc='best')
ax1.set_xlabel("Price ratio (p2/p1)")
ax1.set_ylabel('Consumption ')

