#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tablero:
    ''' Definicion de un tablero para el juego de Othello '''
    def __init__(self, dimension=8, tamCasilla=60):
        ''' Constructor base de un tablero
        :param dimension: Cantidad de casillas en horizontal y vertical del tablero
        :type dimension: int
        :param tamCasilla: El tamano en pixeles de cada casilla cuadrada del tablero
        :type tamCasilla: int
        '''
        self.dimension = dimension
        self.tamCasilla = tamCasilla
        self.turno = True # Representa de quien es el turno bajo la siguiente convencion: true = jugador 1, false = jugador 2
        self.numeroDeTurno = 0 # Contador de la cantidad de turnos en el tablero
        
        self.mundo = [[0 for i in range(self.dimension)] for j in range(self.dimension)] # Representacion logica del tablero. Cada numero representa: 0 = vacio, 1 = ficha jugador1, 2 = ficha jugador 2
        # Configuracion inicial (colocar 4 fichas al centro del tablero):
        
        self.mundo[(self.dimension/2)-1][self.dimension/2] = 1
        self.mundo[self.dimension/2][(self.dimension/2)-1] = 1
        self.mundo[(self.dimension/2)-1][(self.dimension/2)-1] = 2
        self.mundo[self.dimension/2][self.dimension/2] = 2
        
        self.posicionesLegales = []
        self.direcciones= [[0,1],[-1,0],[0,-1],[1,0],[-1,1],[-1,-1],[1,-1],[1,1]]

    def printMundo(self): 
        """
            Mostrar el tablero del juego, con su forma tralsada para que corresponda al tablero de la ventana
        """

        transpose = [[0 for i in range(self.dimension)] for j in range(self.dimension)]
        for i in range(0,self.dimension):
            for j in range(0,self.dimension):
                transpose[j][i] = self.mundo[i][j]
            
        for i in range(0,8):
            print(transpose[i])        
  
    def findLegalMooves(self):  
        """
            Fucnion para encontrar y fijar los movimientos legales en el tablero
            La funcion itera sobre cada ficha del jugador, para cada una, itera sobre las 8 direcciones
            e intenta encontrar posiciones de juego
        """
        
        piecePosition = []
        
        if self.turno == False: #white
            oppositeColor = 1
            playersColor = 2
        elif self.turno == True: # black turn
            oppositeColor = 2
            playersColor=1

        for i in range(0,self.dimension):  # encontrar las fichas del jugador
            for j in range(0,self.dimension):
                if (self.mundo[i][j] == playersColor):
                    piecePosition.append((i,j))

        for pos in piecePosition:     #para cada ficha del jugador         
            for dir in self.direcciones:  # para cada direccion
                mov = list(dir)       # copiar la referencia
              
                while  ( 0<=pos[0]+mov[0] < self.dimension and 0<pos[1]+mov[1]<self.dimension ) and self.mundo[pos[0]+mov[0]][pos[1]+mov[1]] == oppositeColor:
                    # make the direction vector greater : a square longer
                   
                    if (0<= pos[0] + mov[0] + dir[0] < self.dimension and 0<= pos[1] + mov[1] + dir[1] <  self.dimension):   # para no salir del tablero
                        mov[0] = mov[0] + dir[0]
                        mov[1] = mov[1] + dir[1]

                    if self.mundo[pos[0]+mov[0]][pos[1]+mov[1]] == 0:  # if next square is free
                     
                        # append the new position if it doesnt exists 
                        try:
                            self.mundo.index((pos[0]+mov[0],pos[1]+mov[1]))   #si no hay error : esta posicion ya existe en la lista
                            # do nothing
                        except:  # -> doesnt exist : append it
                            self.posicionesLegales.append((pos[0]+mov[0],pos[1]+mov[1]))
                        break
                    
                    elif self.mundo[pos[0]+mov[0]][pos[1]+mov[1]] == playersColor:  # if next squre is taken by one of player's piece
                        break
                    else:
                        break
                     
        # fijar las posiciones en el tablero

        for pos in self.posicionesLegales:
            stroke(255,0,0)
            fill(0,255,0)
            ellipse(pos[0]*self.tamCasilla+self.tamCasilla/2,pos[1]*self.tamCasilla+self.tamCasilla/2,\
        self.tamCasilla/2,self.tamCasilla/2)
        
    def display(self):
        ''' Dibuja en pantalla el tablero, es decir, dibuja las casillas y las fichas de los jugadores '''
        
        fondo = color(63, 221, 24) # El color del fondo del tablero
        linea = color(0) # El color de linea del tablero
        grosor = 2 # Ancho de linea (en pixeles)
        jugador1 = color(0) # Color de ficha para el primer jugador
        jugador2 = color(255) # Color de ficha para el segundo jugador
        
        # Doble iteracion para recorrer cada casilla del tablero
        for i in range(self.dimension):
            for j in range(self.dimension):
                # Dibujar cada casilla del tablero:
                fill(fondo)
                stroke(linea)
                strokeWeight(grosor)
                rect(i*self.tamCasilla, j*self.tamCasilla, self.tamCasilla, self.tamCasilla)
                # Dibujar las fichas de los jugadores:
                if not self.mundo[i][j] == 0 and (self.mundo[i][j] == 1 or self.mundo[i][j] == 2): # en caso de que la casilla no este vacia
                    fill(jugador1 if self.mundo[i][j] == 1 else jugador2) # establecer el color de la ficha
                    noStroke() # quitar contorno de linea
                    ellipse(i*self.tamCasilla+(self.tamCasilla/2), j*self.tamCasilla+(self.tamCasilla/2), self.tamCasilla*3/5, self.tamCasilla*3/5)
    
    def setFicha(self, posX, posY, turno=None):
        ''' Coloca o establece una ficha en una casilla especifica del tablero.
        Nota: El eje vertical esta invertido y el contador empieza en cero.
        :param posX: Coordenada horizontal de la casilla para establecer la ficha
        :type posX: int
        :param posY: Coordenada vertical de la casilla para establecer la ficha
        :type posY: int
        :param turno: Representa el turno o color de ficha a establecer
        :type turno: bool
        '''
      #  turno = self.turno if turno is None else turno # permite definir un parametro default que es instancia de la clase (self.turno)
        

        try:
            self.posicionesLegales.index((posX,posY)) # verificar si el lugar del click es legal      
            self.clearLegalMooves()  # si no hay error :

            #check the color to draw²
            stroke(0,0,0)
            if(self.turno == False):
                fill(255,255,255)
                numero = 2
            else:
                fill(0,0,0)
                numero =1 
            
            ellipse(
                     posX*self.tamCasilla+self.tamCasilla/2,\
                     posY*self.tamCasilla+self.tamCasilla/2,\
                    self.tamCasilla/2,self.tamCasilla/2)
            
            self.mundo[posX][posY] = numero  # turn = [0,1] and color : [1,2]


            self.applyChanges((mouseX/self.tamCasilla , mouseY/self.tamCasilla))

        except:   # si hay error : position illegal  > no se hace nada
            pass

    def applyChanges(self,(pos)):  
        """ 
            Despues de cada ficha jugada, hay que actualizar las fichas del tablero
            La funcion itera sorbre las 8 direcciones alrededor de la nueva ficha, 
            para encontrar las fichas del adversario que hay que cambiar


        """

        movimiento = []

        if self.turno == False: #white
            oppositeColor = 1
            playersColor = 2
            fill(255,255,255)
        elif self.turno == True: # black turn
            oppositeColor = 2
            playersColor=1
            fill(0,0,0) 

        for dir in self.direcciones:   # iterar sobre las 8 direcciones

            mov = list(dir) # copiar la referencia
            size_of_line = 0 # length of the line to be filled 

            if (0<=pos[0]+mov[0]<self.dimension and 0<=pos[1]+mov[1]<self.dimension ):  # para no salir del tablero

                while self.mundo[pos[0]+mov[0]][pos[1]+mov[1]] == oppositeColor and\
                     0<=pos[0]+mov[0]+dir[0]< self.dimension and 0<=pos[1]+mov[1]+dir[0]< self.dimension :  #mientras no se sale del tablero y hay fichas adversarias

                    if (0<= pos[0] + mov[0] + dir[0] <  self.dimension and 0<= pos[1] + mov[1] + dir[1] < self.dimension):
                        mov[0] = mov[0] + dir[0]  # orientacion exploracion ; > segun un sentido (direccion) pero con mas de 1 casilla
                        mov[1] = mov[1] + dir[1]
                        size_of_line = size_of_line +1
                    
                    if self.mundo[pos[0]+mov[0]][pos[1]+mov[1]] == playersColor:  # if the color is the player's one
                        for i in range(1,size_of_line+1):
                         
                            x = (pos[0]+i*dir[0])
                            y = (pos[1]+i*dir[1])

                            ellipse(
                                x*self.tamCasilla+self.tamCasilla/2,\
                                y*self.tamCasilla+self.tamCasilla/2,\
                                self.tamCasilla/2,self.tamCasilla/2)
                
                            self.mundo[x][y] = playersColor    #actualizar el mundo
                            self.printMundo()   
            
    def cambiarTurno(self):
        ''' Representa el cambio de turno. Normalmente representa la ultima accion del turno '''
        self.turno = not self.turno
        self.numeroDeTurno += 1
        
    def estaOcupado(self, posX, posY):
        ''' Verifica si en la posicion de una casilla dada existe una ficha (sin importar su color)
        :param posX: Coordenada horizontal de la casilla a verificar
        :type posX: int
        :param posY: Coordenada vertical de la casilla a verificar
        :type posY: int
        :returns: True si hay una ficha de cualquier color en la casilla, false en otro caso
        :rtype: bool
        '''
        return self.mundo[posX][posY] != 0
    
    def clearLegalMooves(self):
        """
            Al anadir una ficha en un lugar legal, hay que borrar los lugares legales
        """
        stroke(0,0,0)
        fill(0,255,0)

        for pos in self.posicionesLegales:
            ellipse(pos[0]*self.tamCasilla+self.tamCasilla/2,\
                pos[1]*self.tamCasilla+self.tamCasilla/2,self.tamCasilla/2,self.tamCasilla/2)

        #reinitializar la lista
        self.posicionesLegales = []

    def cantidadFichas(self):
        ''' Cuenta la cantidad de fichas en el tablero
        :returns: La cantidad de fichas de ambos jugadores en el tablero como vector donde x = jugador 1, y = jugador 2
        :rtype: PVector 
        '''
        contador = PVector()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.mundo[i][j] == 1:
                    contador.x = contador.x + 1
                if self.mundo[i][j] == 2:
                    contador.y = contador.y + 1
        return contador
    
