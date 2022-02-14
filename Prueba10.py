def mi_funcion(*argumentos, **argumentospalaclav):
    for arg in argumentos:
        print('argumento:', arg)
    for key in argumentospalaclav.keys():
        print('llave:', key, 'con valor: ', argumentospalaclav[key])

#Esto se puede llamar con cualquier número de argumentos de cualquier tipo:

mi_funcion('Juan', 'Maria', hija='Juana', hijo='Adan')
print('-' * 50)
mi_funcion('pablo', 'Clara', hijo_uno='Andres',
hijo_2='Jorge', hija='Joselyn')