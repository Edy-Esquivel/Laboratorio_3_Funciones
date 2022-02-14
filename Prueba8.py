def saludo(name,
        titulo = 'Dr',
        inicio = 'Bienvenido',
        mensaje = 'Tenga una vida Prospera'):
    print(inicio, titulo, name, '-', mensaje)

    #Esto ahora plantea la pregunta de cómo proporcionamos el nombre y el mensaje.     
    # argumentos cuando nos gustaría tener el título y el indicador predeterminados? 
    # La respuesta es usar argumentos con nombre (o argumentos de palabras clave). 
    # En este enfoque proporcionamos el nombre del parámetro al que queremos que 
    # se le asigne un argumento/valor; la posición ya no es relevante. Por ejemplo:
    
saludo(mensaje = 'Nos gusta Python', name = 'Marcos')