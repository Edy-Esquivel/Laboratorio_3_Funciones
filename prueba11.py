#lambda arguments: expression
double = lambda i : i * i

#print(double(10))
#------------------------------
#Cuando se ejecuta esto, se imprime el valor 100.
#A continuación se dan otros ejemplos de funciones lambda/anónimas (que ilustran
#que una función anónima puede tomar cualquier número de argumentos):
#-------------------------------

func0 = lambda: print('sin argumentos')
func1 = lambda x: x * x
func2 = lambda x, y: x * y
func3 = lambda x, y, z: x + y + z

#Estos se pueden utilizar como se muestra a continuación:
func0()
print(func1(4))
print(func2(3, 4))
print(func3(2, 3, 4))