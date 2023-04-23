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

    def mostrarNombreObjeto2(self):
        return self.objeto2.mostrarNombre()

    def statusSolved(self):
        return self.resuelto

class Pantalla(object):

    def __init__(self,objetos,puzzle,dibujar,descripcion,adyacentes):
        self.objetos = objetos
        self.puzzle = puzzle
        self.dibujar = dibujar
        self.descripcion = descripcion
        self.adyacentes = adyacentes

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
        if self.adyacentes != "":
            if self.adyacentes[0] != "":
                print("puedes ir al norte",)
            if self.adyacentes[1] != "":
                print("puedes ir al este",)
            if self.adyacentes[2] != "":
                print("puedes ir al oeste",)
            if self.adyacentes[3] != "":
                print("puedes ir al sur",)
        return

    def mirar(self,objetoAMirar):
        if objetoAMirar == "":
            self.mostrarDescripcion()
            return
        found = False
        if self.objetos != "":
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
        if self.puzzle != "":
            for p in self.puzzle:
                if p.mostrarAccion() == "hablar":
                    if p.mostrarNombreObjeto1() == objetoAHablar:
                        print(p.resolverPuzzle())
                        found = True
        if not found:
            print("No puedes hablar con: " + objetoAHablar)
        return

    def usar(self,objeto1,objeto2):
        if objeto1 == "" or objeto2 == "":
            print("Si no vas a usar dos objetos ni me digas Usar!!!")
            return
        found = False
        if self.puzzle != "":
            for p in self.puzzle:
                if p.mostrarAccion() == "usar":
                    if (p.mostrarNombreObjeto1() == objeto1 and p.mostrarNombreObjeto2() == objeto2) or (p.mostrarNombreObjeto1() == objeto2 and p.mostrarNombreObjeto2() == objeto1):
                       print(p.resolverPuzzle())
                       found = True
        if not found:
            print("No puedes usar " + objeto1 +" con "+ objeto2)
        return

def main():
    objetoPuerta = ObjetoJuego("puerta","Es una puerta de metal reforzada que se ve muy muy fuerte")
    objetoLlave = ObjetoJuego("llave","Es una llave de oro que sirve para abrir puertas reforzdas")
    objetoOSO = ObjetoJuego("oso","Es un Oso que sabe cantar, único en el mundo")
    objetoPlanta = ObjetoJuego("planta", "Puede ver una planta con una hermosa flor")
    puzzlePuerta = Puzzle(objetoLlave,objetoPuerta,"usar","Puedes Ver una Puerta que esta cerrada","La puerta está Abierta")
    puzzleOSO = Puzzle(objetoOSO,"objeto2","hablar","Puedes Ver un OSO con cara de Cantor","El oso canta y canta y canta 51,60")
    puzzles =[puzzlePuerta,puzzleOSO]
    pantallaOso = Pantalla([objetoPuerta,objetoLlave,objetoOSO],[puzzlePuerta,puzzleOSO],"dibujar","Este es el bosque del OSO",["","","","pantallaPatio"])
    pantallaPatio =Pantalla([objetoPlanta],[],"dibujar","Este es un hermoso patio donde da mucho el Sol",["pantallaOso","","",""])
    currentScreen = pantallaOso
    currentScreen = pantallaPatio
    currentScreen.mostrarDescripcion()
    solvedGame = False
    while not solvedGame:
        x = list(map(str, input("Que deseas hacer? ").split()))
        firstWord = str.lower(x[0])
        secondWord = ""
        thirdWord = ""
        if len(x) == 2:
            secondWord = str.lower(x[1])
        elif len(x) >= 3:
            secondWord = str.lower(x[1])
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
        elif firstWord == "usar":
            if len(x) == 1:
                currentScreen.usar("","")
            elif secondWord == "" or thirdWord == "":
                currentScreen.usar("", "")
            else:
                currentScreen.usar(secondWord,thirdWord)
        elif firstWord == "ayuda":
            print("puedes usar los verbos: mirar, hablar, usar y todos con uno o dos objetos")
        else:
            print("No se lo que quieres hacer: " + x[0])

        totalPuzzlesSolved = 0
        totalPuzzles = len(puzzles)
        for p in puzzles:
            if p.statusSolved() == True:
                totalPuzzlesSolved += 1
        if totalPuzzlesSolved == totalPuzzles:
            print ("------------------------------------")
            print("Ganaste!! Campeón de la vida y el Amoorrrrr")
            for p in puzzles:
                print(p.mostrarDescripcion())
            solvedGame = True


if __name__ == "__main__":
    main()