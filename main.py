# Importamos los módulos requeridos para realizar la actividad.
import os
from colorama import *

# Creamos las variables necesarias.
fichasAjedrez = {
    'RYB': {  # ♔
        'chr': 9812,
        'x': 8,
        'y': 5
    }, 'RAB': {  # ♕
        'chr': 9813,
        'x': 8,
        'y': 4
    }, 'TB': {  # ♖
        'chr': 9814,
        'x': 8,
        'y': 1
    }, 'AB': {  # ♗
        'chr': 9815,
        'x': 8,
        'y': 3
    }, 'CB': {  # ♘
        'chr': 9816,
        'x': 8,
        'y': 2
    }, 'PB': {  # ♙
        'chr': 9817,
        'x': 7,
        'y': 1
    }, 'RYN': {  # ♚
        'chr': 9818,
        'x': 1,
        'y': 5
    }, 'RAN': {  # ♛
        'chr': 9819,
        'x': 1,
        'y': 4
    }, 'TN': {  # ♜
        'chr': 9820,
        'x': 1,
        'y': 1
    }, 'AN': {  # ♝
        'chr': 9821,
        'x': 1,
        'y': 3
    }, 'CN': {  # ♞
        'chr': 9822,
        'x': 1,
        'y': 2
    }, 'PN': {  # ♟
        'chr': 9823,
        'x': 2,
        'y': 1
    }
}

separator = '============================================='

# Creamos la clase principal para desarrollar el Ajedrez en ella

class Ajedrez():
    def __init__(self):
        self.tablero = [] # Aquí se almacenará el tablero con la posición de las fichas
        self.jugador1 = '' # Nombre del primer jugador
        self.jugador2 = '' # Nombre del segundo jugador
        self.jugando = 0 # Variable que determina de quién es el turno
    def crearTablero(self):
        n1 = 8 # Tando n1 como n2 son variables que sirven para más adelante realizar la creación del tablero
        n2 = 65
        for i in range(18):
            self.tablero.append(([' ']*18)) # Crea una lista de listas a la cual se irán incorporando las "paredes" del tablero y las fichas
        for a in range(18):
            for b in range(18):
                if b != 17 and a != 17:
                    if (b % 2) == 0:
                        if a == 0 or a == 16:
                            self.tablero[a][b] = '--' # Posiciona las primeras columnas
                        else:
                            self.tablero[a][b] = '||' # Posiciona las filas
                    elif (a % 2) == 0:
                        self.tablero[a][b] = '---' # Rellena los espacios entre fila y fila con un elemento de mayor tamaño para que en este puedan entrar las fichas correctamente centradas.

                    elif (b % 2) != 0 or (a % 2) != 0:
                        self.tablero[a][b] = '   '
                if a == 17 and (b % 2) == 0 and n2 != 73:
                    self.tablero[a][b] = '   ' + chr(n2) # Coloca las Letras laterales que indican las coordenadas de las casillas. Se emplea la variable n2 para que se creen las letras necesarias exactamente gracias al código ASCII de las mismas, el cual es ascendente y continuo
                    n2 += 1
                self.tablero[17][0] = '    A' # Se le da más espacio en la primera casilla para que las Letras que indican las coordenadas aparezcan centradas
                if b == 17 and (a % 2) != 0 and n1 > 0:
                    self.tablero[a][b] = ' ' + str(n1) # De la misma manera que con las Letras, se colocan los números.
                    n1 -= 1
        for value in fichasAjedrez:
            x = fichasAjedrez[value]['x'] + (fichasAjedrez[value]['x'] - 1) # Se ajustan las coordenadas a usar para que se adapten al tablero debido a que en este hay líneas que delimitan el tablero.
            y = fichasAjedrez[value]['y'] + (fichasAjedrez[value]['y'] - 1)
            self.tablero[x][y] = ' ' + chr(fichasAjedrez[value]['chr']) + ' ' # Se colocan las fichas empleando las coordenadas registradas en la variable fichasAjedrez.
            if value == 'CN' or value == 'CB':
                self.tablero[x][y + 10] = ' ' + chr(fichasAjedrez[value]['chr']) + ' ' # Si la ficha es un Caballo, la duplica en la posición opuesta del tablero, ya que hay 2
            elif value == 'AN' or value == 'AB':
                self.tablero[x][y + 6] = ' ' + chr(fichasAjedrez[value]['chr']) + ' ' # Si la ficha es un Alfil, la duplica en la posición opuesta del tablero, ya que hay 2
            elif value == 'TN' or value == 'TB':
                self.tablero[x][y + 14] = ' ' + chr(fichasAjedrez[value]['chr']) + ' ' # Si la ficha es una Torre, la duplica en la posición opuesta del tablero, ya que hay 2
            elif value == 'PN' or value == 'PB':
                for i in range(17):
                    if (i % 2) != 0 and i != 0:
                        self.tablero[x][i] = ' ' + chr(fichasAjedrez[value]['chr']) + ' ' # Si la ficha es un Peón, añade peones a lo largo de toda la fila en la que el primer Peón se encuentra.
        toWrite = []
        for r in range(18):
            toWrite.append(' '.join(self.tablero[r]) + '\n')
        with open('./tablero.txt', 'w', encoding="utf-8") as f:
            f.writelines(toWrite)
    def printTablero(self):
        for r in range(18):
            print(' '.join(self.tablero[r])) # Printea el trablero sin brackets, comillas y comas, en varias líneas; con el objetivo de dar la imagen de tablero real.
    def pedirNombres(self):
        self.jugador1 = str(input('¿Cuál es el nombre del primer jugador?: ' + Fore.GREEN)) # Registra el nombre del primer jugador
        self.jugador2 = str(input(Fore.RESET + '¿Y el nombre del segundo jugador?: ' + Fore.BLUE)) # Registra el nombre del segundo jugador
        print(Fore.RESET) # Resetea el color del texto para que no sea azul constantemente.
        aj.printTablero() # Printea el tablero para que los jugadores puedan verlo.
    def movimiento(self):
        if self.jugando == 0: # Con esta condición comprueba de quien es el turno (gracias a la variable self.jugando) y printea su nombre para informar de que es su turno.
            print('Turno de ' + Fore.GREEN + self.jugador1 + Fore.RESET)
            self.jugando = 1
        else:
            print('Turno de ' + Fore.BLUE + self.jugador2 + Fore.RESET)
            self.jugando = 0
        ficha = input('Introduce las coordenadas de la posición de la Ficha que quieres mover: ')
        destino = input('Introduce las coordenadas de la posición de la Casilla a donde quieres mover la Ficha: ')
        xold = ord(ficha[:1].upper()) - 64
        yold = ficha[1:2]
        y = xold + (xold - 1)
        x = 8 - (int(yold) - 1)
        x = x + (x - 1)
        founded = False
        for h in range(9812, 9824):
            if h == ord(self.tablero[int(x)][int(y)][1:2]):
                founded = True
        if not founded:
            if self.jugando == 0:
                self.jugando = 1
            else:
                self.jugando = 0
            os.system('cls')
            aj.printTablero()
            print('Aqui no hay ninguna Ficha para mover, prueba con otra casilla.')
            return aj.movimiento()
        for i in range(9812, 9824):
            if i == ord(self.tablero[int(x)][int(y)][1:2]):
                print('Hay una ficha')
                xold2 = ord(destino[:1].upper()) - 64
                yold2 = destino[1:2]
                y2 = xold2 + (xold2 - 1)
                x2 = 8 - (int(yold2) - 1)
                x2 = x2 + (x2 - 1)
                for j in range(9812, 9823):
                    if j == ord(self.tablero[int(x2)][int(y2)][1:2]):
                        if self.jugando == 0:
                            self.jugando = 1
                        else:
                            self.jugando = 0
                        print('Aqui hay una ficha, prueba con otra casilla.')
                        return aj.movimiento()
                self.tablero[int(x2)][int(y2)] = self.tablero[int(x)][int(y)]
                self.tablero[int(x)][int(y)] = '   '
                os.system('cls')
                aj.printTablero()
                toWrite = []
                for r in range(18):
                    toWrite.append(' '.join(self.tablero[r]) + '\n')
                with open('./tablero.txt', 'a', encoding="utf-8") as f:
                    if self.jugando == 0:
                        f.write(separator + ' Movimento de ' + self.jugador2 + ': ' + ficha.upper() + ' -> ' + destino.upper() + ' ' + separator + '\n')
                    else:
                        f.write(separator + ' Movimento de ' + self.jugador1 + ': ' + ficha.upper() + ' -> ' + destino.upper() + ' ' + separator + '\n')
                    f.writelines(toWrite)
                return aj.movimiento()
    def inciarJuego(self):
        print(Back.CYAN + Fore.BLACK + Style.DIM + '♔ Bienvenidos al Ajedrez ♚' +
              Back.RESET + Fore.RESET + Style.RESET_ALL)
        aj.crearTablero()
        aj.pedirNombres()
        aj.movimiento()

aj = Ajedrez()
aj.inciarJuego()