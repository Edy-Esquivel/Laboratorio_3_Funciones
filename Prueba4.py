def ingreso_tipo_int(mensaje):
    """
    Esta función mostrará el mensaje al usuario.
    y solicite que ingresen un número entero.
    Si el usuario ingresa algo que no es un número
    entonces la entrada será rechazada
    y se mostrará un mensaje de error.
    A continuación, se le pedirá al usuario que vuelva a intentarlo.
    """
    valor_tip_cadena = input(mensaje)
    while not valor_tip_cadena.isnumeric():
        print('La entrada debe de ser un numero entero')
        valor_tip_cadena = input(mensaje)
        return int(valor_tip_cadena)
edad = ingreso_tipo_int('Por favor ingresa tu edad: ')
print('la edad es:', edad)
#La cadena de documentación se puede leer directamente desde el código, 
# pero también está disponible para los IDE.
#como PyCharm para que puedan proporcionar información sobre la función. 
# es incluso disponible para el programador a través de una propiedad 
# muy especial de la función llamada __doc__ al que se puede acceder 
# a través del nombre de la función utilizando la notación de puntos:

print(ingreso_tipo_int.__doc__)