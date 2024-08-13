# Diccionario que describe las conexiones entre las distintas habitaciones
laberinto = {
    'Inicio': {'este': 'Sala de Estudio', 'sur': 'Comedor'},
    'Sala de Estudio': {'oeste': 'Inicio', 'norte': 'Biblioteca'},
    'Comedor': {'norte': 'Inicio', 'este': 'Cocina'},
    'Biblioteca': {'sur': 'Sala de Estudio'},
    'Cocina': {'oeste': 'Comedor'}
}

# Ubicación actual del jugador en el laberinto
posicion_actual = 'Inicio'

def mostrar_informacion():
    print(f"Estás en: {posicion_actual}")
    print("Puedes ir a:", ', '.join(laberinto[posicion_actual].keys()))

def mover(direccion):
    global posicion_actual
    # Verifica si la dirección es válida y si el jugador puede moverse
    if direccion in laberinto[posicion_actual]:
        posicion_actual = laberinto[posicion_actual][direccion]
        print(f"Te has movido a: {posicion_actual}")
    else:
        print("No puedes ir en esa dirección.")

def juego():
    print("Bienvenido al laberinto de texto!")
    
    while True:
        mostrar_informacion()
        direccion = input("¿A dónde quieres ir? (o escribe 'salir' para terminar): ").lower()
        
        if direccion == 'salir':
            print("¡Gracias por jugar!")
            break
        
        mover(direccion)

# Inicia el juego
juego()
