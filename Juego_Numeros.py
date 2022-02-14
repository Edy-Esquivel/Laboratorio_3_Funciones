import random
#Saludo de Inicio a Juego
def saludo():
    print()
    print('****| BIENVENIDO AL JUEGO DE ADIVINAR NUMEROS |****')
    print()
saludo()
#ingreso de Datos
def ingreso_datos():
    print('Ingrese nombre: '); nombre = input ()
    print()
    print('Ingrese Apellido: '); apellido = input ()
    print()
    print('Ingrese edad: '); edad = input ()
    print()
    print("Bienvenido", nombre, apellido, 'con una edad de ', edad, 'años ya puedes empezar a Jugar')
    print()
ingreso_datos()
#inicio Juego
def juego():
    numero_adivinar = random.randint(1, 10)
    contador_intentos = 1
    adivinar = int(input("Adivina un número entre 1 y 10: "))
    while numero_adivinar != adivinar:
        print('Numero incorrecto')
        adivinar = int(input('Adivina de nuevo: '))
        if contador_intentos == 4:
            break
        elif adivinar < numero_adivinar:
            print('tu ingreso es menor al numero')
        else:
            print('tu ingreso es mayor al numero')
            adivinar = int(input('Adivina de nuevo: '))
        contador_intentos += 1
    if numero_adivinar == adivinar:
        print('Felicidades Ganaste!')
        print('Ingresaste', contador_intentos, 'para completar el juego')
    else:
        print('Lo Sentimos haz perdido')
        print('El número que debes debiste adivinar fue: ', numero_adivinar)
    print('Fin del Juego')
juego()