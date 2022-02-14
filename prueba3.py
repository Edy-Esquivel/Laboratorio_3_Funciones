def swap(a, b):
    return b, a

a = 2
b = 3
x,y = swap (a,b)

#De hecho, el resultado devuelto por la función de intercambio es lo que se llama una tupla
#que es una forma sencilla de agrupar datos. Esto significa que también podríamos
#haber escrit:
z = swap(a, b) 
print(z)
