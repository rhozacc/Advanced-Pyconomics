# SOLOW SWAN MODEL with GROWTH OF TECHNOLOGY AND 
# POPULATION

# THREE PARTS
# 1. STEADY STATE AND BALANCED GROWTH PATH

import numpy as np
import matplotlib.pyplot as plt

# KEY PARAMETERS
    # PRODUCTION FUNCTION PARAMETER FOR COBB-DOUGLAS P.F. with C.R.S.: Y_{t}=K_{t}^alpha * (A_{t}*L_{t}) ^(1-alpha)    
alpha = np.arange(0.15,0.75,0.05) 
    
    # SAVINGS FUNCTION: S_{t} = s Y_{t} 
s = np.arange(0.15,0.95,0.05) 

    # LAW OF MOTION FOR CAPITAL PARAMETER -- deprecitation rate: K_{t+1} = K_{t}*(1-delta)+I_{t}    
delta = np.arange(0.06,0.16,0.02)  

    # LAW OF MOTION FOR LABOR PARAMETER -- growth rate of labor: L_{t+1} = L_{t}*(1+gamma_l)    
gamma_l = np.arange(0.00,0.05,0.01)   

    # LAW OF MOTION FOR TECHNOLOGICAL INDEX PARAMETER -- growth rate of labor: A_{t+1} = A_{t}*(1+gamma_A)
gamma_a = np.arange(0.00,0.10,0.01)

# ix function for indexing 
alphax,sx,deltax,gamma_lx,gamma_ax = np.ix_(alpha,s,delta,gamma_l,gamma_a)

# reshape
alphax.shape, sx.shape, deltax.shape, gamma_lx.shape, gamma_ax.shape

# 1. CALCULATION OF STEADY STATE FOR CAPITAL PER EFFECTIVE LABOR

k_al = (sx/(gamma_ax + gamma_lx+deltax))**(1/(1-alphax))
q_al = k_al**alphax
i_al = (deltax+gamma_lx+gamma_ax)* k_al
c_al = q_al - i_al

    # VARIATION OF PRODUCTION FUNCTION PARAMETER


k_al_1 = k_al[:,0,0,0,0]
q_al_1 = q_al[:,0,0,0,0]
i_al_1 = i_al[:,0,0,0,0]
c_al_1 = c_al[:,0,0,0,0]

            
fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(alpha,k_al_1,'k-',color='red',label=r'$\tilde{k}^{\ast}$')
ax1.plot(alpha,q_al_1,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(alpha,i_al_1,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(alpha,c_al_1,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Production function parameter $\alpha$')
ax1.set_ylabel(r'Variables per effective labor $\tilde{k}^{\ast}$')
#fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig1_alpha_eq.png')   # save the figure to file

    # VARIATION OF SAVINGS RATE
    # Note: value 4 chooses alpha = 0.35, which implies
    # Golden rule s is alpha = s

k_al_2 = k_al[4,:,0,0,0]
q_al_2 = q_al[4,:,0,0,0]
i_al_2 = i_al[4,:,0,0,0]
c_al_2 = c_al[4,:,0,0,0]

fig2a = plt.figure(); ax1=fig2a.add_subplot(1,1,1)
ax1.plot(s,k_al_2,'k-',color='r',label=r'$\tilde{k}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Savings rate $s$')
ax1.set_ylabel(r'Capital per effective labor $\tilde{k}^{\ast}$')
#fig2a.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig2a_s_eq.png')   # save the figure to file

            
fig2b = plt.figure(); ax1=fig2b.add_subplot(1,1,1)
ax1.plot(s,q_al_2,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(s,i_al_2,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(s,c_al_2,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Savings rate $s$')
ax1.set_ylabel(r'Variables per effective labor')
#fig2b.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig2b_s_eq.png')   # save the figure to file


    # VARIATION OF DEPRECIATION RATE 
    # alpha = s = 0.35 (number 4 in k_al etc.)

k_al_3 = k_al[4,4,:,0,0]
q_al_3 = q_al[4,4,:,0,0]
i_al_3 = i_al[4,4,:,0,0]
c_al_3 = c_al[4,4,:,0,0]

fig3a = plt.figure(); ax1=fig3a.add_subplot(1,1,1)
ax1.plot(delta,k_al_3,'k-',color='r',label=r'$\tilde{k}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Depreciation rate $\delta$')
ax1.set_ylabel(r'Capital per effective labor $\tilde{k}^{\ast}$')
#fig3a.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig3a_delta_eq.png')   # save the figure to file

            
fig3b = plt.figure(); ax1=fig3b.add_subplot(1,1,1)
ax1.plot(delta,q_al_3,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(delta,i_al_3,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(delta,c_al_3,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Depreciation rate $\delta$')
ax1.set_ylabel(r'Variables per effective labor')
#fig3b.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig3b_delta_eq.png')   # save the figure to file

# VARIATION OF POPULATION GROWTH RATE 
    # alpha = s = 0.35, delta = 0.10 (number 4 in k_al, 2 for delta etc.,)

k_al_3 = k_al[4,4,2,:,0]
q_al_3 = q_al[4,4,2,:,0]
i_al_3 = i_al[4,4,2,:,0]
c_al_3 = c_al[4,4,2,:,0]

fig4a = plt.figure(); ax1=fig4a.add_subplot(1,1,1)
ax1.plot(gamma_l,k_al_3,'k-',color='r',label=r'$\tilde{k}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Growth rate of population $\gamma_{L}$')
ax1.set_ylabel(r'Capital per effective labor $\tilde{k}^{\ast}$')
#fig4a.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig4a_delta_eq.png')   # save the figure to file

            
fig4b = plt.figure(); ax1=fig4b.add_subplot(1,1,1)
ax1.plot(gamma_l,q_al_3,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(gamma_l,i_al_3,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(gamma_l,c_al_3,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Growth rate of population $\gamma_{L}$')
ax1.set_ylabel(r'Variables per effective labor')
#fig4b.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig4b_delta_eq.png')   # save the figure to file


# VARIATION OF TECHNOLOGICAL GROWTH RATE 
    # alpha = s = 0.35, delta = 0.10 (number 4 in k_al, 2 for delta etc.,)

k_al_4 = k_al[4,4,2,:,0]
q_al_4 = q_al[4,4,2,:,0]
i_al_4 = i_al[4,4,2,:,0]
c_al_4 = c_al[4,4,2,:,0]

fig5a = plt.figure(); ax1=fig5a.add_subplot(1,1,1)
ax1.plot(gamma_l,k_al_3,'k-',color='r',label=r'$\tilde{k}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Growth rate of technology $\gamma_{A}$')
ax1.set_ylabel(r'Capital per effective labor $\tilde{k}^{\ast}$')
#fig5a.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig5a_delta_eq.png')   # save the figure to file

            
fig5b = plt.figure(); ax1=fig5b.add_subplot(1,1,1)
ax1.plot(gamma_l,q_al_3,'k--',color='b',label=r'$\tilde{q}^{\ast}$')
ax1.plot(gamma_l,i_al_3,'k--',color='k',label=r'$\tilde{i}^{\ast}$')
ax1.plot(gamma_l,c_al_3,'k--',color='g',label=r'$\tilde{c}^{\ast}$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Growth rate of technology $\gamma_{A}$')
ax1.set_ylabel(r'Variables per effective labor')
#fig5b.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/Python/ex3SS_fig5b_delta_eq.png')   # save the figure to file


