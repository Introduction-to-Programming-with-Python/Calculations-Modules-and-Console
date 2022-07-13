#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:12:37 2020

@author: davidnaranjo
"""


import distancia_puntos as dist

def ejecutar_calcular_distancia()->None:
    t1 = int(input("Ingrese la latitud del primer punto en la Tierra: ")) 
    # TODO: Remplace la siguiente línea, pidiendo la longitud del primer punto
    g1 = int(input("Ingrese la longitud del primer punto en la Tierra: ")) 
    t2 = int(input("Ingrese la latitud del segundo punto en la Tierra: ")) 
    # TODO: Remplace la siguiente línea, pidiendo la longitud del segundo punto
    g2 = int(input("Ingrese la longitud del segundo punto en la Tierra: ")) 
    resultado = round((dist.calcular_distancia_tierra(t1,g1,t2,g2)),2)
    # TODO: Imprima el resultado obtenido arriba, en un mensaje descriptivo
    print(resultado)

def iniciar_aplicacion()->None:
    print("Bienvenido al calculador de distancias!")
    ejecutar_calcular_distancia()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()