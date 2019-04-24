#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:55:23 2019

Juanita Gomez
Salome Viana

"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage



def dibujar_mapa(f):
    # Visualiza una coloración del mapa de una interpretación dada f
    
    # Input:
    #   - f, una lista de literales
    
    # Output:
    #   - archivo de imagen tablero1.png

    # Inicializa el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibuja el tablero
    step = 1./3
    tangulos = []
    
    for l in f:
        if '-' not in l:
            l=int(l)
            # Calcula el numero de la casilla a la cual se refiere el literal
            casilla = int((l-1)/4) +1
            # Calcula las coordenadas de la casilla
            x = (casilla-1)%3 
            yinvert = (int((casilla-1) / 3))
            y = 2-yinvert
            
            # Colorea las casillas de acuerdo a las letras proposicionales
            if (int(l)%4 == 1):
                tangulos.append(patches.Rectangle((x*step, y*step), step, step,\
                                                    facecolor='mediumpurple'))
            if (int(l)%4 == 2):
                tangulos.append(patches.Rectangle((x*step, y*step), step, step,\
                                                    facecolor='darkorange'))
            if (int(l)%4 == 3):
                tangulos.append(patches.Rectangle((x*step, y*step), step, step,\
                                                    facecolor='dodgerblue'))
            if (int(l)%4 == 0):
                tangulos.append(patches.Rectangle((x*step, y*step), step, step,\
                                                    facecolor='limegreen'))
                
    
    # Calcula las coordenadas del centro de cada casilla 
            
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]
    
    # Ubica los números de las casillas 
    
    i=1;
    while i<10:
        
        string = ['A', 'B', 'C', 'D' ,'E', 'F' , 'G', 'H', 'I']
        plt.text(direcciones[i][0], direcciones[i][1],string[i-1], fontsize=15, 
                 horizontalalignment='center', 
             verticalalignment='center')
        i=i+1
        
        
    # Crea el mapa con las coloraciones y los numeros de las casillas
   
    for t in tangulos:
        axes.add_patch(t)
    # plt.show()
    fig.savefig("solucion_" + str(1) + ".png")
    
#---------------------------------//----------------------------------------//    
    
# Interpretación f con 36 literales
    
f =  ['-1', '2', '-3', '-4', '5', '-6', '-7', '-8', '-9','-10', '-11', '12',
      '-13', '-14', '15', '-16', '-17', '-18', '-19','20', '-21', '22', '-23', 
      '-24', '25', '-26', '-27', '-28', '-29','30', '-31', '-32', '-33', '-34'
      , '35', '-36']

dibujar_mapa(f)