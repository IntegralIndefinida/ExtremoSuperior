# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import matplotlib.pyplot as plt
def f(x):return np.sin(x)
def g(x,A,w,s):return A*np.sin(x*w+s)
x1list = np.linspace(-np.pi,np.pi,num=1000)
x2list = np.linspace(-1.57,1.57+np.pi,num=1000)
flist = f(x1list)
g1list = g(x2list,A=1,w=1,s=0)
plt.figure(num=1,dpi=120)
plt.plot(x1list,flist)
plt.plot(x2list,g1list)
#I'm so good at this shit