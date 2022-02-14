#Tenga en cuenta que este es otro uso del bucle for; 
# pero esta vez es una secuencia de
#cadenas en lugar de una secuencia de enteros que se está utilizando.

def saludo(*argumentos):
    for nombre in argumentos:
        print('Bienvenido', nombre)
saludo('Josue', 'Maria', 'Juan', 'Lucas', 'Manuel', 'Juana')