Taller grupal / Finding roots - Algoritmos G2

Calculo de la complejidad del algoritmo de la Biseccion.

El proposito del algoritmo es hallar una unica raiz acotada dentro 
de dos parametros, sabiendo que la funcion a evaluar  es continua y
cruza el eje x una sola vez.

Input:

Una intervalo inicial, un valor de tolerancia (que sirve como criterio de parada)
de +-0.0001. 

Teorema: 

Consideremos {x_n} la sucesion generada por el metodo de la biseccion. Si f es una
funcion continua en [a, b] tal que f(a)*f(b) < 0 entonces, si p es un cero de f en
[a, b], la sucesion {x_n} satisface la siguiente desigualdad :

				|x_n - p| <= (b - a)/ 2^(n+1)   	para todo n>=1

Calculo de la complejidad del algoritmo :

Sean [a, b] nuestro intervalo del input, la sucesion {x_n} generada por el algoritmo
es tal que |x_n - p| <= (b - a)/ 2^(n+1). Para que nuestro algoritmo pare, necesitamos
que |x_n - x_(n-1)| < tolerance para algun n >=1. Por lo tanto, como 

	|x_n - p| <= |x_n - x_(n-1)| < tolerance (Los intervalos se van encajando)

Podemos concluir que basta con que, para algun n>=1, se satisfaga que :

				(b - a) / 2^(n+1) < tolerance

Despejando n (el cual es el numero de iteraciones necesitadas), tendremos que :

				n > log_2 ((b - a) / (tolerance)) - 1
				
Es decir, n >= log_2 ((b - a) / (tolerance)). Tomando el minimo valor de n veremos que
al algoritmo le tomara solamente

			n = ceil(log_2 ((b - a) / (tolerance))) iteraciones 

para poder parar (ceil(x) es la funcion techo, el minimo valor entero >= que x). Este valor nos da la cota maxima de iteraciones o el peor caso.

En el caso especifico de la actividad tolerance = t = 0.0001, a=0 y b=1000, de modo que:

  			n = ceil(log2(1000/0.0001)) = ceil=(23.24) = 24 iteraciones.

Concluimos asi que:
		
			time_complexity = O(log_2 ((b - a) / tolerance))
			
Observacion : Como vimos anteriormente, la complejidad del algoritmo depende de los tres valores a, b y tolerance. Para configuraciones distintas la complejidad del algoritmo seguramente varie.
