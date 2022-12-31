# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:59:22 2020

@author: Enda
"""

from matplotlib import pyplot as plt
import numpy as np
from itertools import cycle
cycol = cycle('bgrcmk')

##############################################################################


errs1a=np.array([[1.00000000e+02, 1.00000000e+02, 1.03812103e-03],
       [1.26000000e+02, 1.26000000e+02, 3.71510951e-03],
       [1.58000000e+02, 1.58000000e+02, 5.29582143e-04],
       [2.00000000e+02, 2.00000000e+02, 1.37435182e-03],
       [2.51000000e+02, 2.51000000e+02, 9.02252772e-04],
       [3.16000000e+02, 3.16000000e+02, 2.65869037e-04],
       [3.98000000e+02, 3.98000000e+02, 3.62215738e-04],
       [5.01000000e+02, 5.01000000e+02, 7.32079796e-05],
       [6.31000000e+02, 6.31000000e+02, 1.28569549e-03],
       [7.94000000e+02, 7.94000000e+02, 3.56284476e-05],
       [1.00000000e+03, 1.00000000e+03, 1.75187559e-04]])

errs2a=np.array([[1.00000000e+02, 1.00000000e+02, 5.70960281e-03],
       [1.26000000e+02, 1.26000000e+02, 3.31114422e-03],
       [1.58000000e+02, 1.58000000e+02, 4.64449376e-04],
       [2.00000000e+02, 2.00000000e+02, 3.49582705e-03],
       [2.51000000e+02, 2.51000000e+02, 1.74322443e-03],
       [3.16000000e+02, 3.16000000e+02, 1.35100145e-03],
       [3.98000000e+02, 3.98000000e+02, 9.16152207e-04],
       [5.01000000e+02, 5.01000000e+02, 2.66417928e-03],
       [6.31000000e+02, 6.31000000e+02, 1.72627833e-03],
       [7.94000000e+02, 7.94000000e+02, 2.81278990e-04],
       [1.00000000e+03, 1.00000000e+03, 2.33037669e-04]])

errs3a=np.array([[1.00000000e+02, 1.00000000e+02, 4.58361354e-03],
       [1.26000000e+02, 1.26000000e+02, 8.44535566e-04],
       [1.58000000e+02, 1.58000000e+02, 3.60186418e-03],
       [2.00000000e+02, 2.00000000e+02, 1.07722601e-03],
       [2.51000000e+02, 2.51000000e+02, 1.28188197e-03],
       [3.16000000e+02, 3.16000000e+02, 2.43254665e-04],
       [3.98000000e+02, 3.98000000e+02, 1.34955356e-03],
       [5.01000000e+02, 5.01000000e+02, 3.25942085e-04],
       [6.31000000e+02, 6.31000000e+02, 6.46589637e-04],
       [7.94000000e+02, 7.94000000e+02, 5.78634888e-04],
       [1.00000000e+03, 1.00000000e+03, 1.97211841e-04]])

errs4a=np.array([[1.00000000e+02, 1.00000000e+02, 1.48802234e-03],
       [1.26000000e+02, 1.26000000e+02, 3.80691919e-03],
       [1.58000000e+02, 1.58000000e+02, 8.81871188e-04],
       [2.00000000e+02, 2.00000000e+02, 2.16282239e-03],
       [2.51000000e+02, 2.51000000e+02, 1.18921642e-03],
       [3.16000000e+02, 3.16000000e+02, 1.30833492e-03],
       [3.98000000e+02, 3.98000000e+02, 2.43988376e-04],
       [5.01000000e+02, 5.01000000e+02, 2.01949553e-04],
       [6.31000000e+02, 6.31000000e+02, 3.37773097e-04],
       [7.94000000e+02, 7.94000000e+02, 1.81497023e-03],
       [1.00000000e+03, 1.00000000e+03, 2.51257133e-04]]) 

errs5a=np.array([[1.00000000e+02, 1.00000000e+02, 5.28719662e-03],
       [1.26000000e+02, 1.26000000e+02, 3.08087275e-03],
       [1.58000000e+02, 1.58000000e+02, 3.70598306e-03],
       [2.00000000e+02, 2.00000000e+02, 2.05926738e-04],
       [2.51000000e+02, 2.51000000e+02, 5.56227539e-04],
       [3.16000000e+02, 3.16000000e+02, 7.47113895e-04],
       [3.98000000e+02, 3.98000000e+02, 5.70931931e-04],
       [5.01000000e+02, 5.01000000e+02, 1.02844688e-04],
       [6.31000000e+02, 6.31000000e+02, 3.13475791e-04],
       [7.94000000e+02, 7.94000000e+02, 1.99509742e-03],
       [1.00000000e+03, 1.00000000e+03, 1.02425922e-03]])

errs6a=np.array([[1.00000000e+02, 1.00000000e+02, 2.59060692e-03],
       [1.26000000e+02, 1.26000000e+02, 7.26478737e-04],
       [1.58000000e+02, 1.58000000e+02, 1.47815922e-03],
       [2.00000000e+02, 2.00000000e+02, 2.14292815e-04],
       [2.51000000e+02, 2.51000000e+02, 3.34509498e-03],
       [3.16000000e+02, 3.16000000e+02, 3.31356621e-04],
       [3.98000000e+02, 3.98000000e+02, 7.58382089e-04],
       [5.01000000e+02, 5.01000000e+02, 6.52248217e-04],
       [6.31000000e+02, 6.31000000e+02, 1.01300919e-03],
       [7.94000000e+02, 7.94000000e+02, 5.57626913e-04],
       [1.00000000e+03, 1.00000000e+03, 8.01335984e-04]])

errs7a=np.array([[1.00000000e+02, 1.00000000e+02, 9.66561989e-04],
       [1.26000000e+02, 1.26000000e+02, 2.20226539e-03],
       [1.58000000e+02, 1.58000000e+02, 3.02755584e-04],
       [2.00000000e+02, 2.00000000e+02, 1.69566385e-04],
       [2.51000000e+02, 2.51000000e+02, 5.76766878e-04],
       [3.16000000e+02, 3.16000000e+02, 2.64413436e-03],
       [3.98000000e+02, 3.98000000e+02, 1.05086206e-03],
       [5.01000000e+02, 5.01000000e+02, 8.30099703e-05],
       [6.31000000e+02, 6.31000000e+02, 7.21514054e-04],
       [7.94000000e+02, 7.94000000e+02, 2.46777308e-04],
       [1.00000000e+03, 1.00000000e+03, 5.03462217e-05]])

errs8a=np.array([[1.00000000e+02, 1.00000000e+02, 4.35445122e-05],
       [1.26000000e+02, 1.26000000e+02, 2.49591158e-03],
       [1.58000000e+02, 1.58000000e+02, 2.06935784e-03],
       [2.00000000e+02, 2.00000000e+02, 1.21456006e-03],
       [2.51000000e+02, 2.51000000e+02, 2.30234781e-03],
       [3.16000000e+02, 3.16000000e+02, 5.69280057e-04],
       [3.98000000e+02, 3.98000000e+02, 1.49643686e-03],
       [5.01000000e+02, 5.01000000e+02, 3.19687987e-04],
       [6.31000000e+02, 6.31000000e+02, 1.29304270e-03],
       [7.94000000e+02, 7.94000000e+02, 1.65304295e-03],
       [1.00000000e+03, 1.00000000e+03, 9.70239828e-04]])

errs9a=np.array([[1.00000000e+02, 1.00000000e+02, 3.58863906e-04],
       [1.26000000e+02, 1.26000000e+02, 2.46079054e-04],
       [1.58000000e+02, 1.58000000e+02, 1.92185123e-04],
       [2.00000000e+02, 2.00000000e+02, 1.07695480e-03],
       [2.51000000e+02, 2.51000000e+02, 1.75470890e-03],
       [3.16000000e+02, 3.16000000e+02, 3.65717809e-04],
       [3.98000000e+02, 3.98000000e+02, 6.83482229e-05],
       [5.01000000e+02, 5.01000000e+02, 1.68205671e-04],
       [6.31000000e+02, 6.31000000e+02, 4.29326948e-05],
       [7.94000000e+02, 7.94000000e+02, 9.83236068e-04],
       [1.00000000e+03, 1.00000000e+03, 5.87981068e-04]])

errs10a=np.array([[1.00000000e+02, 1.00000000e+02, 3.13666526e-03],
       [1.26000000e+02, 1.26000000e+02, 4.47207732e-04],
       [1.58000000e+02, 1.58000000e+02, 1.24279494e-03],
       [2.00000000e+02, 2.00000000e+02, 1.36013889e-03],
       [2.51000000e+02, 2.51000000e+02, 2.03091833e-03],
       [3.16000000e+02, 3.16000000e+02, 8.65346999e-04],
       [3.98000000e+02, 3.98000000e+02, 6.94594189e-04],
       [5.01000000e+02, 5.01000000e+02, 2.15387009e-04],
       [6.31000000e+02, 6.31000000e+02, 5.99420317e-04],
       [7.94000000e+02, 7.94000000e+02, 9.25006436e-04],
       [1.00000000e+03, 1.00000000e+03, 2.46293789e-04]])

errs11a=np.array([[1.00000000e+02, 1.00000000e+02, 1.02871944e-03],
       [1.26000000e+02, 1.26000000e+02, 8.98179714e-04],
       [1.58000000e+02, 1.58000000e+02, 2.69483704e-03],
       [2.00000000e+02, 2.00000000e+02, 1.55901437e-03],
       [2.51000000e+02, 2.51000000e+02, 9.07778690e-04],
       [3.16000000e+02, 3.16000000e+02, 1.02223511e-03],
       [3.98000000e+02, 3.98000000e+02, 1.95000838e-03],
       [5.01000000e+02, 5.01000000e+02, 3.54463846e-03],
       [6.31000000e+02, 6.31000000e+02, 1.65717946e-04],
       [7.94000000e+02, 7.94000000e+02, 1.72266101e-03],
       [1.00000000e+03, 1.00000000e+03, 4.31093564e-04]])

errs12a=np.array([[1.00000000e+02, 1.00000000e+02, 2.78153286e-03],
       [1.26000000e+02, 1.26000000e+02, 2.78221841e-03],
       [1.58000000e+02, 1.58000000e+02, 1.62457828e-04],
       [2.00000000e+02, 2.00000000e+02, 1.75525969e-03],
       [2.51000000e+02, 2.51000000e+02, 1.53831693e-03],
       [3.16000000e+02, 3.16000000e+02, 3.73083812e-04],
       [3.98000000e+02, 3.98000000e+02, 4.52095617e-04],
       [5.01000000e+02, 5.01000000e+02, 3.34034010e-05],
       [6.31000000e+02, 6.31000000e+02, 9.17412307e-04],
       [7.94000000e+02, 7.94000000e+02, 1.10717024e-03],
       [1.00000000e+03, 1.00000000e+03, 1.40769340e-03]])

errs13a=np.array([[1.00000000e+02, 1.00000000e+02, 1.34357386e-03],
       [1.26000000e+02, 1.26000000e+02, 2.26137367e-04],
       [1.58000000e+02, 1.58000000e+02, 3.28815822e-04],
       [2.00000000e+02, 2.00000000e+02, 3.36164311e-05],
       [2.51000000e+02, 2.51000000e+02, 2.63270159e-03],
       [3.16000000e+02, 3.16000000e+02, 8.32259192e-05],
       [3.98000000e+02, 3.98000000e+02, 2.83607707e-03],
       [5.01000000e+02, 5.01000000e+02, 8.31274030e-06],
       [6.31000000e+02, 6.31000000e+02, 1.49521928e-03],
       [7.94000000e+02, 7.94000000e+02, 1.09441598e-03],
       [1.00000000e+03, 1.00000000e+03, 5.86649033e-04]])


errs14a=np.array([[1.00000000e+02, 1.00000000e+02, 6.34073747e-04],
       [1.26000000e+02, 1.26000000e+02, 2.63177975e-03],
       [1.58000000e+02, 1.58000000e+02, 6.96874962e-04],
       [2.00000000e+02, 2.00000000e+02, 1.27154822e-03],
       [2.51000000e+02, 2.51000000e+02, 1.02019105e-03],
       [3.16000000e+02, 3.16000000e+02, 6.79053067e-04],
       [3.98000000e+02, 3.98000000e+02, 1.53691473e-04],
       [5.01000000e+02, 5.01000000e+02, 3.79214078e-04],
       [6.31000000e+02, 6.31000000e+02, 8.85458795e-04],
       [7.94000000e+02, 7.94000000e+02, 6.02924630e-04],
       [1.00000000e+03, 1.00000000e+03, 1.12832391e-04]])

########################################################################

#Finding the mean of the error at each number of paths
temp=np.zeros([0])
for i in range(11): #summing the error at each no of paths
    temp=np.append(temp, np.add(errs1a[i,2], errs2a[i,2]))
    temp[i]+=np.add(errs3a[i,2], errs4a[i,2])
    temp[i]+=np.add(errs5a[i,2], errs6a[i,2])
    temp[i]+=np.add(errs7a[i,2], errs8a[i,2])
    temp[i]+=np.add(errs9a[i,2], errs10a[i,2])
    temp[i]+=np.add(errs11a[i,2], errs12a[i,2])
    temp[i]+=np.add(errs13a[i,2], errs14a[i,2])


i=0
for i in range(11): #finding mean
    temp[i]/=11
    
########################################################################


###Error Plot for Non-Antithetic###
plt.ylabel('Error')
plt.xlabel('Number of Paths')
plt.grid(1)
#plt.loglog(errs1a[:,0],errs1a[:,2],'bo-')
plt.loglog(errs1a[:,0],0.25e-1*errs1a[:,0]**-0.5,'--')
plt.loglog(errs1a[:,0],errs1a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) #Plottings errors
plt.loglog(errs2a[:,0],errs2a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs3a[:,0],errs3a[:,2],'-',alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs4a[:,0],errs4a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs5a[:,0],errs5a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs6a[:,0],errs6a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs7a[:,0],errs7a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs8a[:,0],errs8a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs9a[:,0],errs9a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs10a[:,0],errs10a[:,2],'-', alpha=0.9, 
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs11a[:,0],errs11a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs11a[:,0],errs12a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs11a[:,0],errs13a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs11a[:,0],errs14a[:,2],'-', alpha=0.9,
           c=next(cycol), linewidth=0.5) 
plt.loglog(errs1a[:,0],temp[:],'bo-', alpha=1, c='blue',
           linewidth=2.5) 
plt.savefig('Error-NA.pgf')                








































































