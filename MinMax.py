

# Modelado a partir de un ejemplo disponible en:
# http://dhconnelly.com/paip-python/docs/paip/othello.html
INFINITO = sys.maxsize - 1

# Función que calcula el mejor resultado según una busqueda alfa beta de los min
# y max.
def busquedaAlfaBeta(color,tablero,alfa,beta,profundidad,funcionEvaluacion):

    # Si la profundidad es 0, regresamos el valor del tablero en ese estado
    if profundidad == 0:
        return funcionEvaluacion(tablero, color), None

    # Los posibles movimientos
    movimientos = []
    for i in range(8):
        for j in range(8):
            if movimientoValido(tablero, color, (i, j)):
                movimientos.append((i, j))

    # Seleccionamos el rival correspondiente
    if color == 1:
        rival = 2
    else:
        rival = 1

    # Si no hay movimientos disponibles es porque o se acabó el juego y regresa-
    # mos el valor actual 
    if len(movimientos) == 0:
        if FinJuego():
            return funcionEvaluacion(tablero, color), None
        # o porque tendríamos que pasar en ese turno
        else:
            # Observemos que en ese caso, se evalúa al resultado del rival, que
            # en dado caso es negativo al nuestro.
            return -busquedaAlfaBeta(rival, tablero, -beta, -alfa, profundidad-1, funcionEvaluacion)

    mejor_movim = None
    # Para todos los movimientos
    for movimiento in movimientos:
        # Dejamos de analizar las ramas que no sirven
        if beta <= alfa :
            break
        # Copiamos el tablero con ese nuevo movimiento
        nuevoTablero = mueve(nuevoTablero, color, movimiento)
        # El paso recursivo, notemos que alternamos el alfa y beta, pues sus 
        # valores serán los mejores para el rival en dado caso.
        recursivo = busquedaAlfaBeta(rival, nuevoTablero, -beta, -alfa, profundidad-1, funcionEvaluacion)
        # Si encontramos un mejor alfa, actualizamos.
        if recursivo[0] >= alfa :
            alfa = recursivo[0]
            mejor_movim = recursivo[1]

    return alfa, mejor_movim

# Nos da el mejor siguiente movimiento
def mejorSigMov(tablero, color, profundidad):
    alfabeta = busquedaAlfaBeta(color,tablero,profundidad,-INFINITO,INFINITO)


# Estas creo ya las tiene lucian, por eso solo las dejo 'pendiente'
pendiente movimientoValido(tablero, color, (x, y))
pendiente mueve(tablero,color,(x,y))