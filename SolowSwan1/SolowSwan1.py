## TWO PERIOD GENERAL EQUILIBRIUM MODEL 
## WITH TWO TYPES OF AGENTS IN TERMS OF
## ENDOWMENTS AND PREFERENCES (DISCOUNT RATE)
#
import numpy as np
import matplotlib.pyplot as plt

#EXOGENOUS
alpha = np.arange(0.01,1.0,0.1)

d = np.arange(0.1,1.0,0.1)
s = np.arange(0.1,1.0,0.1)

#Arrays
K = np.arange(1.0,2.0,0.1)
L = np.arange(1.0,2.0,0.1)

#ix for shapes
alphax,dx,sx,Kx,Lx = np.ix_(alpha,d,s,K,L)
#shapes
alphax.shape, dx.shape, sx.shape, Kx.shape, Lx.shape

#ENDOGENOUS
g = (sx*(Kx**(alphax-1))*((Lx)**(1-alphax)))-dx
Y = sx*Kx
S = sx*Y
Kss = ((sx/(g+dx))**(1/(1-alphax)))



#PLOTTING

g_1 = g[:,0,0,0,0]
Y_1 = Y[:,0,0,0,0]
S_1 = S[:,0,0,0,0]
Kss_1 = Kss[:,0,0,0,0]


fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(g_1,K,'k-',color='r',label='alpha')
ax1.plot(alpha,K,'k-',color='b',label='d')
ax1.legend(loc='best')
ax1.set_xlabel('K')
ax1.set_ylabel('g,a,d')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig1_r_Q11.png')   # save the figure to file








## KEY PARAMETERS
#
## ENDOGENOUS VARS
#    
#alpha = np.arange(0.0,1.0,0.1) # discount rate 1 
#n = np.arange(0.0,1.0,0.1)
#d = np.arange(0.0,1.0,0.1)
#s = np.arange(0.0,1.0,0.1)
#
#
## ENDOWMENTS
#
#K = np.arange(1.0,2.0,0.1)
#L = np.arange(1.0,2.0,0.1)
#S = np.arange(1.0,2.0,0.1)
#
#
## ix function for indexing shapes
#
#alphax,nx,dx,sx,Kx,Lx = np.ix_(alpha,n,d,s,K,L)
#
##SOLUTION TO GE
#
#alphax.shape, nx.shape, dx.shape, sx.shape, Kx.shape, Lx.shape 
#
#g = (sx*(Kx**(alphax-1))*((Lx*nx)**(1-alphax)))-dx
#Y = (Kx**alphax)*(L**(1-alpha))
#Kss = ((sx/(nx+g+dx))**(1/(1-alphax)))
#
#
## PLOT 1: VARIATION OF ENDOWMENT of Agent Type 1 in period 1
#
#
#g_1 = g[:,0,0,0,0,0]
#Y_1 = Y[:,0,0,0,0,0]
#Kss_1 = Kss[:,0,0,0,0,0]
#S_1 = S[:,0,0,0,0,0]
#
#
#fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
#ax1.plot(Kss_1,alpha,'k-',color='r',label='alpha')
#ax1.plot(Kss_1,g_1,'k-',color='b',label='Kss')
#ax1.legend(loc='best')
#ax1.set_xlabel('Y')
#ax1.set_ylabel('$\gamma$')
##fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig1_r_Q11.png')   # save the figure to file
#
#fig2 = plt.figure(); ax1=fig2.add_subplot(1,1,1)
#ax1.plot(Q11,C11_1,'k-',color='r',label='$C_{1}^{1}$')
#ax1.plot(Q11,C12_1,'k--',color='r',label='$C_{2}^{1}$')
#ax1.plot(Q11,C21_1,'k-',color='b',label='$C_{1}^{2}$')
#ax1.plot(Q11,C22_1,'k--',color='b',label='$C_{2}^{2}$')
#ax1.legend(loc='best')
#ax1.set_xlabel('Endowment $Q_{1}^{1}$')
#ax1.set_ylabel('Consumption ')
##fig2.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig2_C_Q11.png')   # save the figure to file
#
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
##fig3.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig3_r_Q12.png')   # save the figure to file
#
#fig4 = plt.figure(); ax1=fig4.add_subplot(1,1,1)
#ax1.plot(Q12,C11_2,'k-',color='r',label='$C_{1}^{1}$')
#ax1.plot(Q12,C12_2,'k--',color='r',label='$C_{2}^{1}$')
#ax1.plot(Q12,C21_2,'k-',color='b',label='$C_{1}^{2}$')
#ax1.plot(Q12,C22_2,'k--',color='b',label='$C_{2}^{2}$')
#ax1.legend(loc='best')
#ax1.set_xlabel('Endowment $Q_{1}^{2}$')
#ax1.set_ylabel('Consumption ')
##fig4.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig4_C_Q12.png')   # save the figure to file
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
##fig5.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig5_r_rho1.png')   # save the figure to file
#
#fig6 = plt.figure(); ax1=fig6.add_subplot(1,1,1)
#ax1.plot(rho1,C11_3,'k-',color='r',label='$C_{1}^{1}$')
#ax1.plot(rho1,C12_3,'k--',color='r',label='$C_{2}^{1}$')
#ax1.plot(rho1,C21_3,'k-',color='b',label='$C_{1}^{2}$')
#ax1.plot(rho1,C22_3,'k--',color='b',label='$C_{2}^{2}$')
#ax1.legend(loc='best')
#ax1.set_xlabel(r'Discount rate $\rho_{1}$')
#ax1.set_ylabel('Consumption ')
##fig6.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/fig6_C_rho1.png')   # save the figure to file
#            