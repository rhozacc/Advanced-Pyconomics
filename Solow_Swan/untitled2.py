#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:31:30 2017

@author: Alen
"""

import numpy as np
#import matplotlib as plt

#Parameters
alpha = np.arange(0.20,0.80,0.1)      #Production function parameter
beta = np.arange(0.20,0.80,0.1)       #Human Capital parameter
sk = np.arange(0.20,0.80,0.1)         #Savings function for K and H
#sh = np.arange(0.20,0.80,0.1) 
delta = np.arange(0.20,0.80,0.1)      #Law of motion for K par 
gamma_l = np.arange(0.20,0.80,0.1)    #Law of motion for Labor par
gamma_a = np.arange(0.20,0.80,0.1)    #Law of motion for Technological ix par

alphax,betax,skx,deltax,gamma_lx,gamma_ax,betax= np.ix_(alpha,beta,sk,delta,gamma_l,gamma_a,beta)
alphax.shape, betax.shape, skx.shape, deltax.shape, gamma_lx.shape, gamma_ax.shape

#k1_al = (shx/(gamma_ax + gamma_lx+deltax))**(betax/(1-alphax-betax))
#k2_al = (skx/(gamma_ax + gamma_lx+deltax))**(1-betax/(1-alphax-betax))
k_al = (skx/(gamma_ax+deltax+gamma_lx))**(betax/(1-alphax-betax))
#h1_al = (shx/(gamma_ax + gamma_lx+deltax))**(1-alphax/(1-alphax-betax))
#h2_al = (skx/(gamma_ax + gamma_lx+deltax))**(alphax/(1-alphax-betax))
h_al = (skx/(gamma_ax+deltax+gamma_lx))**(alphax/(1-alphax-betax))
q_al = (k_al**alphax)*(h_al**betax)

