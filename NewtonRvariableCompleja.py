#!/usr/bin/env python 

#Suarez Hernadez Jose Miguel

from sympy import * #importacion de una libreria especial de python

x = Symbol('x') #declaracion de variables
x1 = Symbol('x1')
funcion = 0.0;
centinela1 = 0.0
centinela2 = 1.0

lista = [] #declaracion de una lista para guardar los valores

terminos = input("Cuantos terminos deseas ingresar?: ") #Se piden cuantas variables se desean ingresar

for i in range(0, terminos-1): # ciclo for para guardar n terminos con su coeficiente y exponente
	coef = input("Introduce el valor de x%d: " %i)
	expo = input("Introduce el valor del exponente de x%d: " %i)
	
	terminos = coef*(x**expo) #Se definen los terminos con la sintaxis correcta
	lista.append(terminos) #se agregan los terminos a la lista.
	
const = input("Introduce el valor de la constante: ") # se agrega la constante a la lista.
lista.append(const)

print'\n\n'

for i in range(len(lista)):
	funcion = funcion + lista[i] # si hay terminos con el mismo exponente, estos se suman

print '\t\tf(x) =', funcion, '\n' # se imprime la funcion.

derivada = diff(funcion, x) # se define la derivada

print "\t\tf'(x)=", derivada, '\n' # se imprime la derivada

newtR = x - (funcion/derivada) # se establece la formula para resolver el metodo

print '\t\t x1 = ', newtR, '\n' # se imprime la formula


resp = newtR.evalf(subs = {x:1j}) # se le asigna a X el valor de J (Numero complejo). 
print resp

while centinela1 != centinela2: #Se hacen las iteraciones necesarias, para obtener la raiz.
#for i in range(0,10):	
	resp = newtR.evalf(subs = {x:resp})
	print resp
	
	centinela2 = centinela1
	centinela1 = resp


	
	
