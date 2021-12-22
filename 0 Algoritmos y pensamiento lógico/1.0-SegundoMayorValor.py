# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 08:15:44 2021

@author: Cuetorra
Encontrando el segundo mayor valor
"""
arr = [10,2,1,3,5,7,6,9,8]


def segundoMayorValor(arreglo):
    primero = 0
    segundo = 0    
    
    for elemento in arreglo:
        if elemento > primero:
            segundo = primero
            primero = elemento
        if elemento < primero and elemento > segundo:
            segundo = elemento
    
    return segundo


print(segundoMayorValor(arr))