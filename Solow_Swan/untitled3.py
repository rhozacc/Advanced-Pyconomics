import numpy as np
import matplotlib.pyplot as plt
#np.seterr(over='ignore')

#Parameters 15steps
alpha = np.arange(0.00,0.15,0.01)      #Production function parameter
beta = np.arange(0.00,0.15,0.01)       #Human Capital parameter
sk = np.arange(0.00,0.15,0.01)         #Savings function for K and H
#sh = np.arange(0.20,0.80,0.1) 
delta = np.arange(0.00,0.15,0.01)      #Law of motion for K par 
gamma_l = np.arange(0.00,0.15,0.01)    #Law of motion for Labor par
gamma_a = np.arange(0.00,0.15,0.01)    #Law of motion for Technological ix par

alphax,betax,skx,deltax,gamma_lx,gamma_ax,betax= np.ix_(alpha,beta,sk,delta,gamma_l,gamma_a,beta)
alphax.shape, betax.shape, skx.shape, deltax.shape, gamma_lx.shape, gamma_ax.shape

k1_al = ((skx/(gamma_ax+gamma_lx+deltax))
k11_al = (betax/(1-alphax-betax)))
k12_al = ((skx/(gamma_ax + gamma_lx+deltax))**(1-betax/(1-alphax-betax)))
k12_al = (skx/(gamma_ax + gamma_lx+deltax))**(1-betax/(1-alphax-betax))
k_al = np.power(k1_al,k2_al)
h_al = ((skx/(gamma_ax+gamma_lx+deltax))**(1-alphax/(1-alphax-betax)))*((skx/(gamma_ax + gamma_lx+deltax))**(alphax/(1-alphax-betax)))
#h2_al = (skx/(gamma_ax + gamma_lx+deltax))**(alphax/(1-alphax-betax))
#h_al = (skx/(gamma_ax+deltax+gamma_lx))**(alphax/(1-alphax-betax))
q_al = (k_al**alphax)*(h_al**betax)
i_al = (deltax+gamma_lx+gamma_ax)*k_al
c_al = q_al-i_al

#kk_al = np.power((shx/(gamma_ax+gamma_lx+deltax),(betax/(1-alphax-betax)))


k_al1 = k_al[:,0,0,0,0,0]
h_al1 = h_al[:,0,0,0,0,0]
q_al1 = q_al[:,0,0,0,0,0]
i_al1 = i_al[:,0,0,0,0,0]
c_al1 = c_al[:,0,0,0,0,0]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(beta,k_al1,'k-',color='red',label=r'$\tilde{k}^{\ast}$')

