import numpy as np
import matplotlib.pyplot as plt

#Parameters
alpha = np.arange(0.05,0.95,0.05)     #Production function par
beta = np.arange(0.5,0.95,0.05)      #Human Capital parameter
sk = np.arange(0.05,0.95,0.05)       #Savings function for K and H
sh = np.arange(0.05,0.95,0.05) 
delta = np.arange(0.01,0.10,0.01)    #Law of motion for K par 
gamma_l = np.arange(0.01,0.05,0.01)  #Law of motion for Labor par
gamma_a = np.arange(0.01,0.10,0.01)  #Law of motion for Tech par

#Numpy stuff
alphax,skx,shx,deltax,gamma_lx,gamma_ax,betax= np.ix_(alpha,sk,sh,delta,gamma_l,gamma_a,beta)
alphax.shape, skx.shape, shx.shape, deltax.shape, gamma_lx.shape, gamma_ax.shape, betax.shape

#Steady state for capital per effective labor
k_al = (((skx**alphax)*(shx**(1-alphax)))/(gamma_ax+gamma_lx+deltax)) ** (1/(1-alphax-betax))
h_al = (((shx**(1-betax)*(shx**(betax)))/(gamma_ax+gamma_lx+deltax))) ** (1/(1-alphax-betax))
q_al = (k_al**alphax)*(h_al**betax)
i_al = (shx+skx)*q_al
c_al = q_al - i_al

#Variation of sh, alpha = 0,35
k_al_1 = k_al [4,0,:,0,0,0,0]
h_al_1 = h_al [4,0,:,0,0,0,0]
q_al_1 = q_al [4,0,:,0,0,0,0]
i_al_1 = i_al [4,0,:,0,0,0,0]
c_al_1 = c_al [4,0,:,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(sk,q_al_1,'k-',color='red',label=r'$\tilde{k}^{\ast}$')
ax1.plot(sk,i_al_1,'k--',color='b',label=r'$\tilde{i}^{\ast}$')
ax1.plot(sk,c_al_1,'k--',color='k',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Savings rate $sk$')
ax1.set_ylabel(r'Variables per effective labor $\tilde{k}^{\ast}$')
#
#for i in range (0,8):
#    q_al_2 = [6,i,(8-i),0,0,0,6]
#
#fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
#ax1.plot(sk,q_al_2,'k-',color='red',label=r'$\tilde{k}^{\ast}$')
##ax1.plot(sk,i_al_1,'k--',color='b',label=r'$\tilde{i}^{\ast}$')
##ax1.plot(sk,c_al_1,'k--',color='k',label=r'$\tilde{c}^{\ast}$')
##ax1.legend(loc='best')
##ax1.set_xlabel(r'Savings rate $sk$')
#ax1.set_ylabel(r'Variables per effective labor $\tilde{k}^{\ast}$')
#
#    