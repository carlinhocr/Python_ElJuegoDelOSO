# clases  

# pantallas
#   saben dibujarse
#   tienen personajes (que no son anda mas que un puzzle)
#   tienen lugares donde ir (norte, sur, este, oeste)
#   tienen puzzles que se resuelven usando objetos ejemplo "usar llave con puerta"
#   tienen estado de sus puzzles si esta resuelto o no pasa algo diferente
#   saben su descripción en texto según el estado de sus puzzles

# objetos
#   saben dibujarse
#   saben que acciones se pueden hacer con ellos ?????

# acciones
#   mirar
#   usar X con Y
#   ir (norte, sur, este, oeste, puerta)
#   levantar
#   dejar
#   ayuda (dice que verbos se pueden usar)
#   hablar (con personaje)

# protagonista 
#   hacen acciones con objetos
#   tienen objetos (inventario)

# Armar un juego muy simple de una pantalla sola con una puerta cerrada, hay una llave que 
# puede ser mirada, levantada, dejada y usada con la puerta en cuyo caso la abre y cambia el estado de la pantalla
# te deja ir a través de la pueta una vez abierta


class ObjetoJuego(object):
    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def mostrarDescripcion(self):
        return self.descripcion

    def mostrarNombre(self):
        return self.nombre

class Puzzle(object):

    def __init__(self, objeto1, objeto2, accionResuelve, descripcionNoResuelto, descripcionResuelto):
        self.objeto1 = objeto1
        self.objeto2 = objeto2
        self.accionResuelve = accionResuelve
        self.resuelto = False
        self.descripcionNoResuelto = descripcionNoResuelto
        self.descripcionResuelto = descripcionResuelto

    def mostrarDescripcion(self):
        if self.resuelto:
            descripcion = self.descripcionResuelto
        else:
            descripcion = self.descripcionNoResuelto
        return descripcion

class Pantalla(object):

    def __init__(self,objetos,puzzle,dibujar,descripcion):
        self.objetos = objetos
        self.puzzle = puzzle
        self.dibujar = dibujar
        self.descripcion = descripcion

    def mostrarDescripcion(self):
        print(self.descripcion)
        if self.objetos != "":
            for o in self.objetos:
                print("puedes ver: " + o.mostrarNombre())
        if self.puzzle != "":
            print(self.puzzle.mostrarDescripcion())
        return




def main():
    objetoPuerta = ObjetoJuego("puerta","Es una puerta de metal reforzada que se muy muy fuerte")
    objetoLlave = ObjetoJuego("llave","es una llave de oro que sirve para abrir puertas reforzdas")
    puzzlePuerta = Puzzle("objeto1","objeto2","USAR","Puedes Ver una Puerta que esta cerrada","La puerta está Abierta")
    pantallaOso = Pantalla([objetoPuerta,objetoLlave],puzzlePuerta,"dibujar","Este es el bosque del OSO")
    pantallaOso.mostrarDescripcion()

if __name__ == "__main__":
    main()