# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:48:29 2019

@author: Cupi2
"""

import math

def calcular_distancia_tierra(t1: float, g1: float, t2: float, g2: float)->float:
    """ Distancia entre dos puntos en la Tierra
    Parámetros:
      t1 (float): Latitud del primer punto en la Tierra
      g1 (float): Longitud del primero punto en la Tierra
      t2 (float): Latitud del segundo punto en la Tierra
      g2 (float): Longitud del segundo punto en la Tierra
    Retorno:
      float: Distancia entre dos puntos en la Tierra a dos cifras decimales.
    """
    #TODO: implemente la función de acuerdo a su documentación
    #remplazando la siguiente línea por el conjunto correcto de instrucciones
    d=6371.01*calcular_angulo(t1, g1, t2, g2)
    return d

def grados_a_radianes(grados:float)->float:
    """ Convierte de grados a radianes usando la función radians
    del módulo math.
    Parámetros:
        grados (float) Grados a convertir. Número decimal positivo o negativo.
    Retorno:
        float: Los radianes correspondientes.
    """
    #TODO: implemente la función de acuerdo a su documentación
    #remplazando la siguiente línea por el conjunto correcto de instrucciones
    return math.radians(grados)


def calcular_angulo (t1:float,g1:float,t2:float,g2:float)->float:
    """ Calcula el ángulo central entre dos puntos de una esfera. 
    Parámetros:
        t1 (float) Latitud del primer punto, en radianes.
        g1 (float) Longitud del primer punto, en radianes.
        t2 (float) Latitud del primer punto, en radianes.
        g2 (float) Longitud del primer punto, en radianes.
    Retorno:
        float: Ángulo central entre los dos puntos.
    """
    #TODO: implemente la función de acuerdo a su documentación
    #remplazando la siguiente línea por el conjunto correcto de instrucciones
    
    math.radians(t1)
    math.radians(g1)
    math.radians(t2)
    math.radians(g2)
    
    return math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

def redondear (numero:float)->float:
    """ Redondea un número flotante a dos posicines decimales. 
    Parámetros:
        numero (float) Número decimal.
    Retorno:
        float: Número redondeado a dos posiciones decimales
    """
    #TODO: implemente la función de acuerdo a su documentación
    #remplazando la siguiente línea por el conjunto correcto de instrucciones
    return round(numero,2)