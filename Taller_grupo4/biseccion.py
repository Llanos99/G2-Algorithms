import matplotlib.pyplot as plt
import numpy as np
from time import time


def f(x):
  """ Definicion de la funcion a estudiar"""
  return ((-1*(pow(x,4)))+(30*(pow(x,3))+(15*(pow(x,2)))+(34*x)+(540)))

def biseccion(a=0,b=1000,delta=10e-5):

  """Definicion e implementacion del archivo de biseccion"""

  #Definicion de variables para sus correspondientes graficas

  dom = np.arange(0,45,0.1)
  z=f(dom)

  dom2 = np.arange(0,1000,0.1)  
  z2 = f(dom2)

  x0 = a
  x1 = b
  t = delta # Rango/particion minimo aceptable cerca a 0 
  iter=0    #Contador de iteraciones del algoritmo
  aprox = []  #Arreglo que guarda la ubicacion de cada particion util para la grafica
  faprox = [] #Arreglo util para la grafica para ver como se comporta el algoritmo
  c=0         #Variable sirve para generar particiones y dar respuesta a la raiz

  start_time = time() #Se empieza a medir el tiempo 

  if f(a)*f(b) < 0:   #Condicional inicial y necesario para desarrollar el algoritmo

    
    while((abs(b-a))>t):        #Se evalua que tan cerca la particion esta de la raiz 
      iter+=1                   #Contador de iteraciones
      c = (a+b)/2               #Creacion de particion

      aprox.append(c)           #Funciones utiles para graficas (guarda ubicacion de las particiones)
      faprox.append(f(c))       

      if (f(a)*f(c)<=0):        #Evalua si la raiz esta en la mitad izquierda
        b=c    
      else:                     #si no en la dereccha
        a=c
  
  end_time = time() - start_time  #se termina de contabilizar el tiempo

  #Muestra de resultados y creacion de graficas

  #2 graficas:
  #1. una con un rango pequeño para mostrar en detalle la ubicacion de raiz
  #2. Rango completo de 0 a 1000, muestra los puntos en los que se creo una particion

  print("la raiz de la funcion en el intervalo " + "["+str(x0)+","+str(x1)+"] es: "+"{:.4f}".format(c))
  print("Tiempo de ejecucion: "+ "{:.6f}".format(end_time)+ " s")
  print("Se encontro una aproximacion a la raiz con "+ str(iter)+ " iteraciones")

  if x0 == 0 and x1 == 1000 and t == 10e-5:    #Graficas con el ejemplo principal

    #2 graficas:
    #1. una con un rango pequeño para mostrar en detalle la ubicacion de raiz
    #2. Rango completo de 0 a 1000, muestra los puntos en los que se creo una particion
    
    plt.subplot(1,2,1)
    plt.plot(dom,z) 
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Raiz en un rango cercano')
    plt.axhline(y=0, color='k')
    plt.axvline(x=c, color='red')
    
    plt.subplot(1,2,2)
    plt.plot(dom2,z2,aprox,faprox,'o')
    plt.title('Raiz en un rango 0 a 1000')
    plt.axhline(y=0, color='k')
    plt.axvline(x=c, color='red')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

#Variacion de parametros
biseccion(0,1000,10e-5)
biseccion(0,1000,10e-2)
biseccion(0,100,10e-5)
biseccion(25,40,10e-5)
biseccion(25,40,10e-8)
biseccion(20, 40, 10e-5)
