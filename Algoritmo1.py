# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:17:17 2020

@author: miguel
"""
if __name__=="__main__":
    import random
    list=random.sample(range(0,100),6)
    print(list)
    
    def orden(lista):
        for j in range(0,len(lista)-2):
            for i in range(0,len(lista)-2):
                if lista[i]>lista[i+1]:
                    (lista[i], lista[i+1]) = (lista[i+1], lista[i])  # Intercambio
    
        return(lista)
    print(orden(list))
            