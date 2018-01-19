"SOLOW-SWAN MODEL TEMPLATE"

import numpy as np
import matplotlib as plt


#KEY PARAMETERS
alpha = np.arange(0.15,0.75,0.05)   #Production function parameter
s = np.arange()                     #Savings function
delta                               #Law of motion for K par deprecitation rate: K_{t+1} = K_{t}*(1-delta)+I_{t} ; dont go to 0 (it would grow forever)
gamma_l                             #Law of motion for Labor par: growth rate of labor: L_{t+1} = L_{t}*(1+gamma_l)
gamma_a                             #Law of motion for Technological index par: A_{t+1} = A_{t}*(1+gamma_A)

#INDEX
alphax.shape, ... = np.ix_(alpha, ...)

#RESHAPE
alphax.shape, ...

#CALCULATIONS (in this case: Per effective labor)
k_al = (sx/(gamma_ax + gamma_lx+deltax))**(1/(1-alphax))
q_al
i_al
c_al

#VARIATIONS (number of elements in [] = number of key parameters.)
k_al1 = k_al[:,0,0,0,0]

#PLOTTING
fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(alpha,k_al_1,'k-',color='red',label=r'$\tilde{k}^{\ast}$')
ax1.plot(alpha,q_al_1,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(alpha,i_al_1,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(alpha,c_al_1,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Production function parameter $\alpha$')
ax1.set_ylabel(r'Variables per effective labor $\tilde{k}^{\ast}$')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig1_alpha_eq.png')   # save the figure to file



