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

    def mostrarAccion(self):
        return self.accionResuelve

    def resolverPuzzle(self):
        self.resuelto=True
        return self.descripcionResuelto

    def mostrarNombreObjeto1(self):
        return self.objeto1.mostrarNombre()


class Pantalla(object):

    def __init__(self,objetos,puzzle,dibujar,descripcion):
        self.objetos = objetos
        self.puzzle = puzzle
        self.dibujar = dibujar
        self.descripcion = descripcion

    def mostrarDescripcion(self):
        stringObjetos = ""
        print(self.descripcion)
        if self.objetos != "":
            for o in self.objetos:
                stringObjetos += o.mostrarNombre() + ","
            print("puedes ver: " + stringObjetos)
        if self.puzzle != "":
            for p in self.puzzle:
                print(p.mostrarDescripcion())
        return

    def mirar(self,objetoAMirar):
        if objetoAMirar == "":
            self.mostrarDescripcion()
            return
        found = False
        for o in self.objetos:
            if o.mostrarNombre() == objetoAMirar:
                print(o.mostrarDescripcion())
                found = True
        if not found:
            print("No encuentro ese objeto para mirar")
        return

    def hablar(self, objetoAHablar):
        if objetoAHablar == "":
            print("Hablas solo como un loco!!")
            return
        found = False
        for p in self.puzzle:
            if p.mostrarAccion() == "hablar":
                print(p.mostrarNombreObjeto1())
                if p.mostrarNombreObjeto1() == objetoAHablar:
                    print(p.resolverPuzzle())
                    found = True
        if not found:
            print("No puedes hablar con: " + objetoAHablar)
        return


def main():
    objetoPuerta = ObjetoJuego("puerta","Es una puerta de metal reforzada que se ve muy muy fuerte")
    objetoLlave = ObjetoJuego("llave","Es una llave de oro que sirve para abrir puertas reforzdas")
    objetoOSO = ObjetoJuego("oso","Es un Oso que sabe cantar, único en el mundo")
    puzzlePuerta = Puzzle(objetoLlave,objetoPuerta,"usar","Puedes Ver una Puerta que esta cerrada","La puerta está Abierta")
    puzzleOSO = Puzzle(objetoOSO,"objeto2","hablar","Puedes Ver un OSO con cara de Cantor","El oso canta y canta y canta 51,60")
    pantallaOso = Pantalla([objetoPuerta,objetoLlave,objetoOSO],[puzzlePuerta,puzzleOSO],"dibujar","Este es el bosque del OSO")
    currentScreen = pantallaOso
    currentScreen.mostrarDescripcion()
    while True:
        x = list(map(str, input("Que deseas hacer? ").split()))
        firstWord = str.lower(x[0])
        secondWord = ""
        if len(x) >= 2:
            secondWord = str.lower(x[1])
        elif len(x) >= 3:
            thirdWord = str.lower(x[2])
        if firstWord == "mirar":
            if len(x) == 1:
                currentScreen.mirar("")
            else:
                currentScreen.mirar(secondWord)
        elif firstWord == "hablar":
            if len(x) == 1:
                currentScreen.hablar("")
            else:
                currentScreen.hablar(secondWord)
        else:
            print("No se lo que quieres hacer: " + x[0])


if __name__ == "__main__":
    main()