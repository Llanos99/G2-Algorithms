import math

# Implementacion del algoritmo encontrada en la siguiente pagina :
# https://nickcdryan.com/2017/09/13/root-finding-algorithms-in-python-line-search-bisection-secant-newton-raphson-boydens-inverse-quadratic-interpolation-brents/

def brent_method(f, x0, x1, max_iterations = 50, tolerance = 10e-5):
    
    fx0 = f(x0)
    fx1 = f(x1)

    assert (fx0 * fx1) <= 0, "No existe una raiz en el intervalo dado."

    if abs(fx0) < abs(fx1) : 
        temp1 = x0
        temp2 = fx0
        x0 = x1
        x1 = temp1
        fx0 = fx1
        fx1 = temp2
    
    x2 = x0
    fx2 = fx0

    flag = True
    count_iterations = 0

    while count_iterations < max_iterations and abs(x1-x0) > tolerance :
        
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        if fx0 != fx2 and fx1 != fx2 : 
            L0 = (x0*fx1*fx2) / ((fx0 - fx1)*(fx0 - fx2))
            L1 = (x1*fx0*fx2) / ((fx1 - fx0)*(fx1 - fx2))
            L2 = (x2*fx1*fx0) / ((fx2 - fx0)*(fx2 - fx1))
            new = L0 + L1 + L2
        else:
            new = x1 - ((fx1*(x1 - x0)) / (fx1 - fx0))
        
        if ((new < ((3*x0 + x1)/4) or new > x1) or (flag == True and (abs(new - x1)) >= (abs(x1 - x2)/2)) or (flag == False and (abs(new - x1)) >= (abs(x2 - d)/2)) or (flag == True and (abs(x1-x2)) < tolerance) or (flag == False and (abs(x2 - d)) < tolerance)):
            new = (x0 + x1)/2
            flag = True
        else:
            flag = False
        
        fnew = f(new)
        d = x2
        x2 = x1

        if (fx0*fnew) < 0:
            x1 = new
        else:
            x0 = new

        if abs(fx0) < abs(fx1):
            temp3 = x0
            x0 = x1
            x1 = x0
        
        count_iterations += 1

    return x1, count_iterations

f = lambda x: (-1*(math.pow(x,4)))+(30*(math.pow(x,3)))+(15*(math.pow(x,2)))+(34*x)+(540)

root, number_iterations = brent_method(f, 20, 40, tolerance=10e-5)

print('La raiz es ' + str(root))
print('Numero de iteraciones hechas ' + str(number_iterations))

