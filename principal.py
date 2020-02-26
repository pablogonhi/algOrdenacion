# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:40:19 2020

@author: pablo
"""
import random
n=10

def aleatorio(n):
    lista=[]
    for i in range(n):
        a=random.randrange(1,11,1)
        if a in lista:
            i-=1
            continue
        else:
            lista.append(a)
    return lista
            
def invertida(n):
    lista=[]
    for i in range(n):
            lista.append(9-i)
    return lista
            
def quasiordenada(n):
    lista=[]
    lista.append(n-1)
    for i in range(n-1):
            lista.append(i)
    return lista
def alterna(n):
    lista=[]
    for i in range(n):
        if i%2==0:
            lista.append(int(i/2))
        else:
            lista.append(10-int((i-1)/2))
    return lista
        
#n variables
#random
#invertida
#quiasiordenada
#alterna


if __name__=="__main__":
    print(aleatorio(n))
    print(invertida(n))
    print(quasiordenada(n))
    print(alterna(n))