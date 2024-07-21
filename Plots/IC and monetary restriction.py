# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:18:05 2024

@author: luusa
"""

import matplotlib.pyplot as plt
import numpy as np
def Yu(x,u): return (u**2)/x
def Ym(x,M,px,py): return M/py-px*x/py
xlist = np.linspace(0,50,num=1000)
Cilist = np.linspace(7,40,num=1000)
#IC
Yu2list = Yu(Cilist, 20)
Yu4list = Yu(Cilist, 25)
Yu6list = Yu(Cilist, 30)
Yu8list = Yu(Cilist, 35)
#Monetary Restriction
Ymlist = Ym(xlist, 7000, 200, 100)

# IC Plots
plt.figure(num=1,dpi=120)
plt.plot(Cilist,Yu2list)
plt.plot(Cilist,Yu4list)
plt.plot(Cilist,Yu6list)
plt.plot(Cilist,Yu8list)

#M plots
plt.plot(xlist,Ymlist)