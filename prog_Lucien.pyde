#!/usr/bin/env python3

"""

faire test position avant ajouter click souris
>mouvements legaux : dir
> arbre miini max

"""

nb_squares = 8
size_square = 30
turn = 0
hasPlayed=False

coordinates = [[0] * nb_squares for i in range(nb_squares)]

legalPositions = []

direction = [[0,1],[-1,0],[0,-1],[1,0],[-1,1],[-1,-1],[1,-1],[1,1]]

def setup():

    size(nb_squares*size_square, nb_squares*size_square)
    background(255)
    fill(0,255,0)
    for i in range(0,nb_squares):
        for j in range(0,nb_squares):
            rect(i*size_square,j*size_square,size_square,size_square)
            ellipse(i*size_square+size_square/2,\
            j*size_square+size_square/2,size_square/2,size_square/2)

    fill(255,255,255)
	
    ellipse(3*size_square+size_square/2,3*size_square+size_square/2,\
    size_square/2,size_square/2)
    ellipse(4*size_square+size_square/2,4*size_square+size_square/2,\
		size_square/2,size_square/2)

    fill(0,0,0)

    ellipse(3*size_square+size_square/2,4*size_square+size_square/2,\
		size_square/2,size_square/2)
    ellipse(4*size_square+size_square/2,3*size_square+size_square/2,\
		size_square/2,size_square/2)

    coordinates[3][3]=1
    coordinates[4][4]=1
    coordinates[3][4]=2
    coordinates[4][3]=2

    print("player "+str(turn))
    legalMooves(turn)
    
def mouseClicked():
    global turn
    global hasPlayed
    global coordinates

    try:
        legalPositions.index((mouseY/size_square,mouseX/size_square)) # if position clicked is legal        
        clearLegalMooves()

        #check the color to draw²
        stroke(0,0,0)
        if(turn == 0):
            fill(255,255,255)
        else:
            fill(0,0,0) 
        
        ellipse(
                 (mouseX/size_square)*size_square+size_square/2,\
                 (mouseY/size_square)*size_square+size_square/2,\
                size_square/2,size_square/2)
        
        coordinates[mouseY/size_square][mouseX/size_square] = int(turn ==1)+1  # turn = [0,1] and color : [1,2]

        hasPlayed = True

        applyChanges(mouseY/size_square , mouseX/size_square)
        prinCoordinates()

    except:   # si hay error : position illegal  > do nothing
        pass

def applyChanges():

    pass
    

def printCoordinates():
    for i in range(0,nb_squares):
        print(coordinates[i])
    print("\n")

def legalMooves(turn):


    piecePosition = []
    
    global legalPositions
    global direction

    for i in range(0,nb_squares):
        for j in range(0,nb_squares):
            if (coordinates[i][j] == turn+1):
                piecePosition.append((i,j))

    if turn == 0: #white
        oppositeColor = 2
    elif turn == 1: # black turn
        oppositeColor = 1

    for pos in piecePosition:            
        for dir in direction:
            while  0<=pos[0]+dir[0]<=7 and 0<=pos[1]+dir[1]<=7 and coordinates[pos[0]+dir[0]][pos[1]+dir[1]] == oppositeColor:
                # make the direction vector greater : a square longer
                dir[0] = dir[0] + dir[0]
                dir[1] = dir[1] + dir[1]

                if coordinates[pos[0]+dir[0]][pos[1]+dir[1]] == 0:  # if next square is free
                    # append the new position if it doesnt exists 
                    try:
                        coordinates.index((pos[0]+dir[0],pos[1]+dir[1]))
                        # do nothing
                    except:  # -> doesnt exist : append it
                        legalPositions.append((pos[0]+dir[0],pos[1]+dir[1]))
                    break
                
                elif coordinates[pos[0]+dir[0]][pos[1]+dir[1]] == turn+1:  # if next squre is taken by one of player's piece
                    break

        direction = [[0,1],[-1,0],[0,-1],[1,0],[-1,1],[-1,-1],[1,-1],[1,1]]
                 
    for pos in legalPositions:
        stroke(255,0,0)
        fill(0,255,0)
        ellipse(pos[1]*size_square+size_square/2,pos[0]*size_square+size_square/2,\
    size_square/2,size_square/2)
    

    print("pos legales "+str(legalPositions))

def clearLegalMooves():

    global legalPositions

    stroke(0,0,0)
    fill(0,255,0)

    for pos in legalPositions:
        ellipse(pos[1]*size_square+size_square/2,\
            pos[0]*size_square+size_square/2,size_square/2,size_square/2)

    legalPositions = []

def draw():

    global hasPlayed
    global turn

    if(hasPlayed == True):
        turn = (turn+1)%2 
        print("player "+str(turn))

        legalMooves(turn)
         
        hasPlayed = False

    return
