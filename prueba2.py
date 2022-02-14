
# Cuando llamamos a esta función, multiplicará 
# lo que sea dado por sí mismo y luego devolver ese valor. 
# El valor devuelto se puede usar en el punto en que la función
#fue invocado

def square(n):
    return n * n

# Almacene el resultado del cuadrado en una variable
resultado = square( 4)
print(resultado)
# envia el resultado del cuadrado inmediatamente a tra funcion
print(square( 5))
# Usar el resultado devuelto por el cuadrado en una expresión condicional
if square(3) < 15:
    print(' Todavía menos de 15')