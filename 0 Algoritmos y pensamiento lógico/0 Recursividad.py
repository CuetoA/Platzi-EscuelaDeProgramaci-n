# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:36:42 2021

@author: ADMIN
"""

def probandoRecursividad(contador):
    contador += 1
    print('Entrando a la función recursiva en la iteracion ', contador)
    
    if contador < 10:
        probandoRecursividad(contador)
    else:
        print('\nHemos terminado de contar\n')
        
    print('Saliendo de la función recursiva en la iteración ', contador)
    

contador = 0
probandoRecursividad(contador)
    



