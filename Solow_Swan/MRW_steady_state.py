# SOLOW SWAN MODEL with GROWTH OF TECHNOLOGY AND 
# POPULATION

# THREE PARTS
# 1. STEADY STATE AND BALANCED GROWTH PATH

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


# KEY PARAMETERS

    # PRODUCTION FUNCTION PARAMETER FOR COBB-DOUGLAS P.F. with C.R.S.: Y_{t}=K_{t}^alpha * (A_{t}*L_{t}) ^(1-alpha)
    
alpha = np.arange(0.15,0.95,0.05) 
beta = np.arange(0.15,0.95,0.05) 
    
    # SAVINGS FUNCTIONS: S_{t} = s Y_{t} 

s_k = np.arange(0.15,0.95,0.05) 
s_h = np.arange(0.15,0.95,0.05) 

    # LAW OF MOTION FOR CAPITAL PARAMETER -- deprecitation rate: K_{t+1} = K_{t}*(1-delta)+I_{t}
    
delta = np.arange(0.06,0.16,0.02)  

    # LAW OF MOTION FOR LABOR PARAMETER -- growth rate of labor: L_{t+1} = L_{t}*(1+gamma_l)
    
gamma_l = np.arange(0.00,0.05,0.01)   

    # LAW OF MOTION FOR TECHNOLOGICAL INDEX PARAMETER -- growth rate of labor: A_{t+1} = A_{t}*(1+gamma_A)

gamma_a = np.arange(0.00,0.10,0.01)

# ix function for indexing 

alphax, betax,s_kx, s_hx,deltax,gamma_lx,gamma_ax = np.ix_(alpha,beta,s_k,s_h,delta,gamma_l,gamma_a)

# reshape

alphax.shape, betax.shape, s_kx.shape, s_hx.shape, deltax.shape, gamma_lx.shape, gamma_ax.shape

# 1. CALCULATION OF STEADY STATE FOR CAPITAL PER EFFECTIVE LABOR

k_al = (s_hx**betax * s_kx**(1-betax)/(gamma_ax + gamma_lx+deltax))**(1/(1-alphax-betax))
h_al = (s_hx**(1-alphax)*s_kx**(alphax)/(gamma_ax + gamma_lx+deltax))**(1/(1-alphax-betax))
y_al = k_al**alphax * h_al**betax
c_al = (1-s_hx-s_kx) * y_al

    
       
    # VARIATION OF SAVINGS RATEs
    # Note: value 4 chooses alpha = beta= 0.35, which implies
    # Golden rule: s_K = alpha, s_H = beta

y_al_opt = y_al[4,4,4,4,0,0,0]
y_al_all = np.zeros(9)
for i in range(0,8):
    y_al_all[i] = y_al[4,4,i,8-i,0,0,0]

y_loss = np.log(y_al_all/y_al_opt)*100
alpha2 = alpha[0:9]

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(alpha2,y_loss,'k-',color='b',label=r'$\ln (\frac{\tilde{y}^{\ast}}{\tilde{y}^{\ast}_{GR}})$')
ax1.legend(loc='best')
ax1.set_xlabel(r'$s_{K}$')
ax1.set_ylabel(r'Output loss in percent')
fig1.savefig('C:/aaaCourses/AdvMacro/aaaHomeworks/2017/MRW_output_loss.png')   # save the figure to file

             