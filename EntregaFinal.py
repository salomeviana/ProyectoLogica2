#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proyecto Final 
Logica para Ciencias de la Computación
Salome Viana y Juanita Gómez
"""


# -----------------------------PRELIMINARES------------------------------
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
LetrasProposicionales= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
niveles = []
conectivos = ['O', 'Y', '>','<->'] 

# -----------------------------CLASE ARBOL-------------------------------

## Clase

class Tree(object):

    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

## Inorder

def inorder(A):
    #Convierte un Tree en una cadena de símbolos
    #Input: A, formula como Tree
    #Output: formula como string
    if A.right == None:
        return A.label
    elif A.label == "-":
        return '-'+ inorder(A.right)
    elif A.label in conectivos:
        return '(' + inorder(A.left) + A.label + inorder(A.right) + ')'

# -------------------------------REGLAS----------------------------------


## Regla1

def reglas():
    reglas = []
    regla=""
    A= LetrasProposicionales
    l="("
    for j in range(1, 37,4):
        lj = ("(("+str((A[j-1]))+'Y(-'+str((A[j]))+'Y(-'+str((A[j+1]))+'Y-'+str(A[j+2])+")))"
            +"O(("+str((A[j]))+'Y(-'+str((A[j+1]))+'Y(-'+str((A[j+2]))+'Y-'+str(A[j-1])+")))"
            +"O(("+str((A[j+1]))+'Y(-'+str((A[j+2]))+'Y(-'+str((A[j-1]))+'Y-'+str(A[j])+")))"
            +"O("+str((A[j+2]))+'Y(-'+str((A[j-1]))+'Y(-'+str((A[j]))+'Y-'+str(A[j+1])+"))))))")
        reglas.append(lj)
    A = reglas[0]
    B = reglas[1]
    C = reglas[2]
    D = reglas[3]
    E = reglas[4]
    F = reglas[5]
    G = reglas[6]
    H = reglas[7]
    I = reglas[8]
    Regla='((((((('+A+'Y'+B+')Y'+C+')Y'+D+')Y'+E+')Y'+F+')Y'+G+')Y'+H+')Y'+I

    return Regla
Regla1= reglas()

## Regla 2

def ponerparentesis(L):
    #Dada una lista de formulas crea una conjuncion de estas acomodando los paréntesis
    #Input: L, lista de formulas como strings
    #Output: st, formula como String
    c=1
    for f in L:
        if c==1:
            st=f+'Y'
            c+=1
        elif c==2:
            st+=2*"(" +f+'Y'
            c+=1
        else:
            st+= f + ')'+'Y'
            c += 1
    st = st[:-1]
    return st

def reglaA(LetrasProposicionales):
    lista=[i for i in range(0,4)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>(-'+LetrasProposicionales[i+4]+'Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaA='('+ponerparentesis(L)+')'
    return(reglaA)

def reglaB(LetrasProposicionales):
    lista=[i for i in range(4,8)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>((-'+LetrasProposicionales[i-4]+'Y-'+LetrasProposicionales[i+4]+')Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaB='('+ponerparentesis(L)+')'
    return(reglaB)

def reglaC(LetrasProposicionales):
    lista=[i for i in range(8,12)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>(-'+LetrasProposicionales[i-4]+'Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaC='('+ponerparentesis(L)+')'
    return(reglaC)

def reglaD(LetrasProposicionales):
    lista=[i for i in range(12,16)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>((-'+LetrasProposicionales[i-12]+'Y-'+LetrasProposicionales[i+4]+')Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaD='('+ponerparentesis(L)+')'
    return(reglaD)

def reglaE(LetrasProposicionales):
    lista=[i for i in range(16,20)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>((-'+LetrasProposicionales[i-12]+'Y(-'+LetrasProposicionales[i-4]+'Y-'+LetrasProposicionales[i+4]+'))Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaE='('+ponerparentesis(L)+')'
    return(reglaE)

def reglaF(LetrasProposicionales):
    lista=[i for i in range(20,24)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>((-'+LetrasProposicionales[i-12]+'Y-'+LetrasProposicionales[i-4]+')Y-'+LetrasProposicionales[i+12]+'))'
        L.append(f)
    reglaF='('+ponerparentesis(L)+')'
    return(reglaF)


def reglaG(LetrasProposicionales):
    lista=[i for i in range(24,28)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>(-'+LetrasProposicionales[i-12]+'Y-'+LetrasProposicionales[i+4]+'))'
        L.append(f)
    reglaG='('+ponerparentesis(L)+')'
    return(reglaG)

def reglaH(LetrasProposicionales):
    lista=[i for i in range(28,32)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>((-'+LetrasProposicionales[i-12]+'Y-'+LetrasProposicionales[i-4]+')Y-'+LetrasProposicionales[i+4]+'))'
        L.append(f)
    reglaF='('+ponerparentesis(L)+')'
    return(reglaF)

def reglaI(LetrasProposicionales):
    lista=[i for i in range(32,36)]
    L=[]
    for i in lista:
        f='('+LetrasProposicionales[i]+'>(-'+LetrasProposicionales[i-12]+'Y-'+LetrasProposicionales[i-4]+'))'
        L.append(f)
    reglaI='('+ponerparentesis(L)+')'
    return(reglaI)

A=reglaA(LetrasProposicionales)
B=reglaB(LetrasProposicionales)
C=reglaC(LetrasProposicionales)
D=reglaD(LetrasProposicionales)
E=reglaE(LetrasProposicionales)
F=reglaF(LetrasProposicionales)
G=reglaG(LetrasProposicionales)
H=reglaH(LetrasProposicionales)
I=reglaI(LetrasProposicionales)

Regla2='((((((('+A+'Y'+B+')Y'+C+')Y'+D+')Y'+E+')Y'+F+')Y'+G+')Y'+H+')Y'+I

## Regla 

Regla = '('+Regla1+')Y('+Regla2+')'

## Regla con condiciones iniciales

# r: E esta coloreado de naranja
# m: C esta coloreado de azul
# x: F esta coloreado de verde
# 8: I esta coloreado de azul

ReglaI = 'mY(8Y(rY(xY('+Regla+'))))'


# ----------------------- PASAR REGLAS A ARBOL----------------------------

## Contador de Niveles

def levelCount(formula):
    #Dada una formula, cuenta el numero de paréntesis en esta.
    #Input: Formula como string
    #Output: Contador 
        if(len(formula)>1):
                contador = 0
                for a in range(0,len(formula)):
                        if(formula[a]=='('): contador += 1
                        elif(formula[a]==')'): contador -= 1
                        niveles.append(contador)
                for b in range(0, len(niveles)):
                        if((niveles[b]==0) and (formula[b] in conectivos)):
                                if((formula[b]=='-')):
                                        if(not(formula[b+1]=='(')): continue
                                        else:
                                                niveles.clear()
                                                return b
                                else:
                                        niveles.clear()
                                        return b
                for c in range(0, len(formula)):
                        if(formula[c] in conectivos):
                                niveles.clear()
                                return c
        return 0

## Polaco

def polaco(formula):
    #Encuentra la forma en polaco de una formula como string.
    #Input: formula, Formula como string
    #Output:Formula en polaco
    if(len(formula)<=2): return formula
    elif(not(levelCount(formula))):
        derecha = ""
        for b in range(2, len(formula)-1):
                derecha+=formula[b]
        return formula[levelCount(formula)] + polaco(derecha)
    else:
            izquierda = ""
            derecha = ""
            for a in range(0, levelCount(formula)):
                izquierda+=formula[a]
            for b in range(levelCount(formula)+1, len(formula)):
                derecha+=formula[b]
            izquierda_nueva = izquierda
            derecha_nueva = derecha
            if(izquierda[0]=='(' and izquierda[len(izquierda)-1]==')'):
                izquierda_nueva = ""
                for a in range(1, len(izquierda)-1):
                    izquierda_nueva+=izquierda[a]
            if(derecha[0]=='(' and derecha[len(derecha)-1]==')'):
                derecha_nueva = ""
                for b in range(1, len(derecha)-1):
                    derecha_nueva+=derecha[b]
            return formula[levelCount(formula)] + polaco(izquierda_nueva) + polaco(derecha_nueva)

## Polaco Inverso

def polacoInverso(polaco, referencia):
    #Encuentra la forma en polaco inverso de una formula en polaco
    #Input:Formula en polaco, referencia
    #Output:Formula en polaco inverso.
        if(referencia == (len(polaco)-1)): return polaco[referencia]
        else:
                return polacoInverso(polaco, referencia+1) + polaco[referencia]

## String de Polaco inverso to tree

def String2Tree(polaco_inverso, LetrasProposicionales):
    #Crea una formula como Tree dada una formula como string en notacion polaca inversa
    #Input: polaco_inverso, Lista de caracteres con una formula escrita en notacion polaca inversa
    #       LetrasProposicionales, lista de strings
    #Output: Formula como Tree
    A = []
    for i in polaco_inverso:
        A.append(i)
    pila = []
    for c in A:
        if c in LetrasProposicionales:
            pila.append(Tree(c, None, None))
        elif c =='-':
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
    return pila[-1]

## RESULTADO

def Reglas2Tree(Regla):
    #Crea una formula como Tree dada una formula escrita como string
    #Input: Regla, string
    #Output: formula como Tree
    return String2Tree((polacoInverso(polaco(Regla),0)),LetrasProposicionales)

# ------------------------------TSEITIN-----------------------------------

## Eliminar dobles negaciones

def elim_doble_negacion(T):
    #Elimina las dobles negaciones en una formula dada como Tree
    #Input: Formula como Tree
    #Output: Formula como Tree sin dobles negaciones
    if T.right == None:
        return T
    elif T.label == '-':
        if T.right.label == '-':
            return elim_doble_negacion(T.right.right)
        else:
            return Tree('-',None,elim_doble_negacion(T.right))
    elif T.label in conectivos:
        return Tree(T.label,elim_doble_negacion(T.left),elim_doble_negacion(T.right))

## Tesitin

def Tseitin(T, LetrasProposicionales):
    #Dada una formula T, halla una formula T' igual de buena que T en forma normla conjuntiva
    #Input: T formula como Tree
    #       LetrasProposicionales, lista de strings
    #Output: Formula como Tree en forma normal conjuntiva
    T = elim_doble_negacion(T)
    A = inorder(T)
    LetrasProposicionales2 = []
    for i in range(1,500):
        LetrasProposicionales2.append(chr(i+1000))
    L  = []
    pila = []
    i = -1
    s = A [0]
    while len(A) > 0:
        if s in LetrasProposicionales and len(pila) > 0 and pila[-1] == "-":
            i += 1
            atomo = LetrasProposicionales2[i]
            pila = pila[:-1]
            pila.append(atomo)
            L.append(Tree("<->", Tree(atomo,None,None), Tree("-",None, Tree(s, None, None))))
            A = A[1:]
            if len(s)>0:
                s = A[0]
        elif s == ")":
            w = pila[-1]
            o = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila) -4]
            i += 1
            atomo = LetrasProposicionales2[i]
            L.append(Tree("<->", Tree(atomo, None, None), Tree(o, Tree(v, None, None), Tree(w,None, None))))
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A)>0:
                s = A[0]
    B = ""
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = LetrasProposicionales2[i]
    for T in L:
        if T.right.label == "-":
            T= Tree("Y", Tree("O", Tree("-", None, T.left), Tree("-", None, T.right.right)), Tree("O", T.left, T.right.right))
        elif T.right.label == "Y":
            T= Tree("Y", Tree("Y", Tree("O", T.right.left, Tree("-", None, T.left)), Tree("O", T.right.right, Tree("-", None, T.left))), Tree("O", Tree("O",Tree("-", None, T.right.left), Tree("-", None, T.right.right)), T.left))
        elif T.right.label == "O":
            T= Tree("Y", Tree("Y", Tree("O", Tree("-", None, T.right.left), T.left), Tree("O", Tree("-", None, T.right.right), T.left )), Tree("O", Tree("O",T.right.left, T.right.right), Tree("-", None, T.left)))
        elif T.right.label == ">":
            T= Tree("Y", Tree("Y", Tree("O", T.right.left, T.left), Tree("O", Tree("-", None, T.right.right), T.left)), Tree("O", Tree("O", Tree("-", None, T.right.left), T.right.right), Tree("-", None, T.left)))
        B += "Y" + inorder(T)
    B = atomo + B
    return B

# -----------------------PASAR A FORMA CLAUSAL----------------------------

## Forma Clausal

def forma_clausal(formula):
    # Crea una formula en su forma clausal dada una formula en forma normal conjuntiva
    #Input: formula, formula como Tree en forma normal conjuntiva
    #Output: Formula en su forma clausal
    lista = []
    count = 0
    while len(formula)>0:
        if count == len(formula) or formula[count] == "Y":
            lista1 = formula[:count]
            lista2 = []
            while len(lista1)>0:
                caracter = lista1[0]
                if caracter in ["O", "(" ,")"]:
                    lista1 = lista1[1:]
                elif caracter == "-":
                    literal = caracter + lista1[1]
                    lista2.append(literal)
                    lista1 = lista1[2:]
                else:
                    lista2.append(caracter)
                    lista1 = lista1[1:]
            lista.append(lista2)

            formula = formula[count+1:]
            count = 0
        else:
            count +=1
    string = ""
    listaFinal = []
    for i in lista:
        for j in i:
            string += j
        listaFinal.append(string)
        string = ""
    return listaFinal

# --------------------------------DPLL------------------------------------

## Clausula Unitaria

def clausulaUnitaria(lista):
    #Encuentra una clausula unitaria en una lista de strings
    #Input: lista, Lista de strings
    #Output:Clausula unitaria
    for i in lista:
        if (len(i)==1):
            return i
        elif (len(i)==2 and i[0]=="-"):
            return i
    return None

## Clausula Vacía

def clausulaVacia(lista):
    #Verifica si una lista contiene una clausula vacía
    #Input: lista, lista de strings
    #Output: booleano
    for i in lista:
        if(i==''):
            return(True)
    return False
#interps= {}

## Unit Propagate

def unitPropagate(lista,interps):
    # Hace Unit Propagate a un conjunto de clausulas
    #Input: lista, lista de strings
    #       interps, diccionario vacio
    #Output: lista, lista de strings
    #        interps, diccionario con interpretaciones parciales
    x = clausulaUnitaria(lista)
    while(x!= None and clausulaVacia(lista)!=True):
        if (len(x)==1):
            interps[str(x)]=1
            j = 0
            for i in range(0,len(lista)):
                lista[i]=re.sub('-'+x,'',lista[i])
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
        else:
            interps[str(x[1])]=0
            j = 0
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
            for i in range(0,len(lista)):
                lista[i]=re.sub(x[1],'',lista[i])
        x = clausulaUnitaria(lista)
    return(lista, interps)

## Literal Complemento

def literal_complemento(lit):
    #Encuentra el literal complemento de un literal
    #Input:Literal
    #Output:Literal complemento.
    if lit[0] == "-":
        return lit[1]
    else:
        lit = "-" + lit
        return lit
## DPLL

def DPLL(lista, interps):
    #Verifica si una formula es satisfacible
    #Input: lista, lista de strings (formula en forma clausal)
    #       interps, diccionario (interpretacion parcial)
    #Output: lista, lista de strings (formula en forma clausal)
    #        interps, diccionario (interpretacion parcial)
    lista, interps = unitPropagate(lista,interps)
    if(len(lista)==0):
        listaFinal = lista
        interpsFinal = interps
        return(lista,interps)
    elif("" in lista):
        listaFinal = lista
        interpsFinal = interps
        return (lista,{})
    else:
        listaTemp = [x for x in lista]
        for l in listaTemp[0]:
            if (len(listaTemp)==0):
                return (listaTemp, interps)
            if (l not in interps.keys() and l!='-'):
                break
        listaTemp.insert(0,l)
        lista2, inter2 = DPLL(listaTemp, interps)
        if inter2 == {}:
            listaTemp = [x for x in lista]
            a =literal_complemento(l)
            listaTemp.insert(0,a)
            lista2, inter2 = DPLL(listaTemp, interps)
        return lista2, inter2

## Interps final

def interpsFinal(interps):
    #Dada una interpretacion ecuentra la interpretacion correspondiente usando solo las letras
    #proposicionales necesarias.
    #Input:Iterpretacion con todas las letras de LetrasProposicionales2
    #Output:Interpretacion con las letras de LetrasProposicionales
    interpsf = {i: interps[i] for i in LetrasProposicionales if i in interps}
    return interpsf

## RESULTADO

def DPLLResultado(lista):
    #Encuentra la interpretacion usando DPLL
    #Input:lista en forma clausal
    #Output:Interpretacion
    lista, inter = DPLL(lista,{})
    interpretacion = interpsFinal(inter)
    return interpretacion

# ----------------------REPRESENTACIÓN GRÁFICA---------------------------

def dicToString(interpretacion):
    #Dadas una interpretaciones crea una lista cuyos elementos literales (sin perdida de generalidad si I(p)=0 mete en la lisa -p y si I(p)=1 mete en la lista p)
    #Input: interpretacion, diccionario (intepretaciones que hacen satisfacible la formula)
    #Output: formula, lista de strings (litelares)
    formula=[]
    for i in LetrasProposicionales:
        if i in interpretacion:
            if interpretacion[i]==1:
                formula.append(i)
            if interpretacion[i]==0:
                formula.append('-'+i)
    return formula

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

def let2num(lista):
    lista1=[]
    L=[str(i) for i in range(0,10)]
    for i in lista:
        if len(i)==1 and i not in L:
            num=ord(i)-96
            lista1.append(str(num))
        elif len(i)!=1 and i[1] not in L:
            num=ord(i[1])-96
            lista1.append('-'+str(num))
        elif len(i)==1 and i in L:
            num=ord(i)-21
            lista1.append(str(num))
        elif len(i)!=1 and i[1] in L:
            num=ord(i[1])-21
            lista1.append('-'+str(num))
    return lista1

###################       FUNCION        #################

def Solucion(Regla):
    #Contiene las funciones necesarias para toda la solucion del problema
    #Input:Regla
    #Output:Interpretacion 
    Tree = Reglas2Tree(Regla)
    Equi = Tseitin(Tree, LetrasProposicionales)
    FC = forma_clausal(Equi)
    interpretacion = DPLLResultado(FC)
    interpString = dicToString(interpretacion)
    dibujar_mapa(let2num(interpString))
    return interpretacion

# Solucion sin condiciones iniciales
print(Solucion(Regla))

# Solucion con algunas condiciones iniciales
print(Solucion(ReglaI))