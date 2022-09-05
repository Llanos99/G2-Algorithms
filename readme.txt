Complejidad Algoritmo de Fuerza Bruta:

Vemos que hay dos ciclos que iteran sobre la longitud de la cadena a analizar.

7*O(1) + O(n)*[O(1)[[2*O(1)]] + O(1)*O(n)[O(1) + O(1)[5*O(1) + O(1)[2*O(1)] + O(1)*O(1)] + O(1)*3*O(1)] + O(1)*O(1)] + O(1)*2*O(1) + O(1).

Reduciendo gracias a las propiedades del Big O, en particular las siguientes:

k*O(f(n)) = O(k*f(n))
O(f(n))+O(g(n)) = O(max{f(n), g(n)})
O(f(n)*g(n)) = O(f(n))*O(g(n))

tenemos que la complejidad de tiempo del algoritmo es aproximadamente de orden cuadrático, es decir:

Tiempo_Complejidad = O(n^2)
 
donde n = len(String), ie, la longitud de la cadena inicial sobre la cual buscamos la aparición de patrones.


