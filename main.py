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

#ir al puzzle de esa pantalla con la accion y los objetos y ver si se resuelve y que la clase puzzle conteste

class ObjetoJuego(object):
    def __init__(self,nombre,descripcion,removable):
        self.nombre = nombre
        self.descripcion = descripcion
        self.removable = removable

    def mostrarDescripcion(self):
        return self.descripcion

    def mostrarNombre(self):
        return self.nombre

    def isRemovable(self):
        return self.removable

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

class Personaje(object):

    def __init__(self,name,inventory=[]):
        self.name = name
        self.inventory = inventory

    def addInventory(self,objeto):
        self.inventory.append(objeto)

    def removeInventory(self,objeto):
        if objeto.isRemovable():
            self.inventory.remove(objeto)

    def showInventory(self):
        return self.inventory

    def showName(self):
        return self.name

    def printInventory(self):
        stringObjetos = ""
        if self.inventory != "":
            for o in self.inventory:
                stringObjetos += o.mostrarNombre() + ","
            print("Tiene en tu inventario: " + stringObjetos)

    def mirar(self,objetoAMirar):
        found = False
        if self.inventory != "":
            for o in self.inventory:
                if o.mostrarNombre() == objetoAMirar:
                    print(o.mostrarDescripcion())
                    found = True
        # if not found:
        #     print("No encuentro ese objeto para mirar")
        return found

class Pantalla(object):

    def __init__(self,name,puzzle,dibujar,descripcion):
        self.name = name
        self.objetos = []
        self.puzzle = puzzle
        self.dibujar = dibujar
        self.descripcion = descripcion
        self.adyacentes = ["", "", "", ""]

    def addObjects(self,objecto):
        self.objetos.append(objecto)

    def removeObjects(self,objecto):
        if objecto.isRemovable():
            self.objetos.remove(objecto)

    def showObjects(self):
        return self.objetos

    def showPuzzles(self):
        return self.puzzle

    def addScreen(self,position,screen):
        self.adyacentes[position] = screen

    def mostrarName(self):
        return self.name

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

    def mirar(self,objetoAMirar,objetosPersonaje):
        if objetoAMirar == "":
            self.mostrarDescripcion()
            return
        found = False
        objetosTotales = self.objetos+objetosPersonaje
        if objetosTotales != "":
            for o in objetosTotales:
                if o.mostrarNombre() == objetoAMirar:
                    print(o.mostrarDescripcion())
                    found = True
        return found

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

    def usar(self,objeto1,objeto2,objetosPersonaje):
        if objeto1 == "" or objeto2 == "":
            print("Si no vas a usar dos objetos ni me digas Usar!!!")
            return
        found = False
        objetosTotales = self.objetos+objetosPersonaje
        haveObject1 = False
        haveObject2 = False
        for o in objetosTotales:
            if o.mostrarNombre() == objeto1:
                haveObject1 = True
            if o.mostrarNombre() == objeto2:
                haveObject2 = True
        if not haveObject1:
            print("No tienes el objeto " + objeto1)
        if not haveObject2:
            print("No tienes el objeto " + objeto2)
        if not haveObject1 or not haveObject2:
            return
        if self.puzzle != "":
            for p in self.puzzle:
                if p.mostrarAccion() == "usar":
                    if (p.mostrarNombreObjeto1() == objeto1 and p.mostrarNombreObjeto2() == objeto2) or (p.mostrarNombreObjeto1() == objeto2 and p.mostrarNombreObjeto2() == objeto1):
                       print(p.resolverPuzzle())
                       found = True
        if not found:
            print("No puedes usar " + objeto1 +" con "+ objeto2)
        return

    def ir(self, dondeIr):
        dondeIr = str.lower(dondeIr)
        if dondeIr == "":
            print("Si no sabes donde ir no vayas a ningún lado!!")
            return
        found = False
        if dondeIr == "norte" and self.adyacentes[0] != "":
            found = True
            screen = self.adyacentes[0]
        elif dondeIr == "este" and self.adyacentes[1] != "":
            found = True
            screen = self.adyacentes[1]
        elif dondeIr == "oeste" and self.adyacentes[2] != "":
            found = True
            screen = self.adyacentes[2]
        elif dondeIr == "sur" and self.adyacentes[3] != "":
            found = True
            screen = self.adyacentes[3]
        else:
            print("No puedes ir en esa dirección!!")
            found = False
            screen = ""
        return screen, found

    def tomar(self, objetoATomar,personaje):
        if objetoATomar == "":
            print("Si no me decis que tomar no podremos tomar nada")
            return
        found = False
        for o in self.showObjects():
            if o.mostrarNombre() == objetoATomar:
                if o.isRemovable():
                    personaje.addInventory(o)
                    self.removeObjects(o)
                    print("Haz tomado el objeto " + objetoATomar)
                else:
                    print("No puedes llevarte el objeto " + objetoATomar)
                found = True
        if self.puzzle != "":
            for p in self.puzzle:
                if p.mostrarAccion() == "tomar":
                    if p.mostrarNombreObjeto1() == objetoATomar:
                        print(p.resolverPuzzle())
                        found = True
        if not found:
            print("No se encuentra el objeto: " + objetoATomar)
        return

    def dejar(self, objetoADejar,personaje):
        if objetoADejar == "":
            print("Si no me decis que dejar no podremos dejar nada")
            return
        found = False
        for o in personaje.showInventory():
            if o.mostrarNombre() == objetoADejar:
                if o.isRemovable():
                    personaje.removeInventory(o)
                    self.addObjects(o)
                    print("Haz dejado el objeto " + objetoADejar)
                else:
                    print("No puedes dejar el objeto " + objetoADejar)
                found = True
        if self.puzzle != "":
            for p in self.puzzle:
                if p.mostrarAccion() == "dejar":
                    if p.mostrarNombreObjeto1() == objetoADejar:
                        print(p.resolverPuzzle())
                        found = True
        if not found:
            print("No se encuentra el objeto: " + objetoADejar)
        return

class Sinonimos(object):

    def __init__(self):
        self.sino ={ "mirar": ["observar","examinar","estudiar"],
                     "tomar": ["coger", "agarrar", "levantar"]}

    def checkSinonimo(self,word):
        for key in self.sino.keys():
            for valueList in self.sino[key]:
                if word in valueList:
                    wordResult = key
                    return wordResult
        return word

class Game(object):

    def __init__(self):
        self.createGameObjects()
        self.createGamePuzzles()
        self.createGameScreens()
        self.createGameCharacter()
        self.actionVerbs = {"mirar": self.mirar,
                           "usar": self.usar,
                           "hablar": self.hablar,
                           "ir": self.ir,
                           "tomar": self.tomar,
                           "dejar": self.dejar,
                           "ayuda": self.ayuda,
                       }
        self.sinonimosVerbos = Sinonimos()

    def createGameObjects(self):
        # definición de objetos del juego
        self.objetoNada= ObjetoJuego("nada", "nada", False)
        self.objetoPuerta = ObjetoJuego("puerta", "Es una puerta de metal reforzada que se ve muy muy fuerte", False)
        self.objetoLlave = ObjetoJuego("llave", "Es una llave de oro que sirve para abrir puertas reforzadas", True)
        self.objetoOSO = ObjetoJuego("oso", "Es un Oso que sabe cantar, único en el mundo", False)
        self.objetoPlanta = ObjetoJuego("planta", "Puede ver una planta con una hermosa flor", True)
        self.objetoCarta = ObjetoJuego("carta",
                                  "Hola Aventurero Bienvenido al Juego del OSO, podrás resolver todos los misterios?",
                                  True)
        self.objetoCanaDePescar = ObjetoJuego("caña", "Es una caña de pescar que sirve para pescar", True)
        self.objetoAlmacenero = ObjetoJuego("almacenero", "Es el dueño del almacen vende cosas por monedas", False)
        self.objetoMoneda = ObjetoJuego("moneda", "Es una moneda de oro sirve para comprar cosas", True)

    def createGamePuzzles(self):
        self.puzzlePuerta = Puzzle(self.objetoLlave, self.objetoPuerta, "usar", "Puedes Ver una Puerta que esta cerrada",
                              "La puerta está Abierta")
        self.puzzleOSO = Puzzle(self.objetoOSO, self.objetoNada, "hablar", "Puedes Ver un OSO con cara de Cantor",
                           "El oso canta y canta y canta 51,60")
        self.puzzleOSOPlanta = Puzzle(self.objetoOSO, self.objetoPlanta, "usar", "A este Oso le encantan las plantas",
                           "El Oso está feliz de tener su planta")
        self.puzzles = [self.puzzlePuerta, self.puzzleOSO,self.puzzleOSOPlanta]

    def createGameScreens(self):
        self.pantallaOso = Pantalla("pantallaOso", [self.puzzlePuerta, self.puzzleOSO,self.puzzleOSOPlanta], "dibujar", "Este es el bosque del OSO")
        self.pantallaPatio = Pantalla("pantallaPatio", [], "dibujar", "Este es un hermoso patio donde da mucho el Sol")
        self.pantallaOso.addObjects(self.objetoPuerta)
        self.pantallaOso.addObjects(self.objetoOSO)
        self.pantallaOso.addScreen(3, self.pantallaPatio)
        self.pantallaPatio.addScreen(0, self.pantallaOso)
        self.pantallaPatio.addObjects(self.objetoPlanta)
        self.pantallaPatio.addObjects(self.objetoLlave)

    def createGameCharacter(self):
        #definición de personaje del Juego
        self.personaje = Personaje("Donatella")
        self.personaje.addInventory(self.objetoCarta)

    # no esta chequeando que el personaje tenga los objetos o que la pantalla los tenga
    # def puzzleCheckSolved(self,allInputsOrdered):
    #     x = allInputsOrdered[0]
    #     firstWord = allInputsOrdered[1]
    #     secondWord = allInputsOrdered[2]
    #     thirdWord = allInputsOrdered[3]
    #     for puzzle in self.currentScreen.showPuzzles():
    #         accion = puzzle.mostrarAccion()
    #         obj1 = puzzle.mostrarNombreObjeto1()
    #         obj2 = puzzle.mostrarNombreObjeto2()
    #         print("entro",accion,obj1,obj2,firstWord,secondWord,thirdWord)
    #         if (firstWord == accion) and (secondWord == obj1 or secondWord == obj2 or obj2 == "nada") \
    #                 and (thirdWord == obj1 or thirdWord == obj2 or obj2 == "nada"):
    #             print("puzzle resuelto: ",puzzle.mostrarDescripcion())

    def start(self):
        # Comienza el juego START
        self.currentScreen = self.pantallaOso
        self.currentScreen.mostrarDescripcion()
        self.personaje.printInventory()
        self.solvedGame = False
        self.play()

    def mirar(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        found = False
        if len(x) == 1:
            found = self.currentScreen.mirar("", self.personaje.showInventory())
            self.personaje.printInventory()
        else:
            found = self.currentScreen.mirar(secondWord, self.personaje.showInventory())
            if not found:
                print("No encuentro ese objeto para mirar")
        return found

    def hablar(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        if len(x) == 1:
            self.currentScreen.hablar("")
        else:
            self.currentScreen.hablar(secondWord)

    def usar(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        if len(x) == 1:
            self.currentScreen.usar("", "", self.personaje.showInventory())
        elif secondWord == "" or thirdWord == "":
            self.currentScreen.usar("", "", self.personaje.showInventory())
        else:
            self.currentScreen.usar(secondWord, thirdWord, self.personaje.showInventory())

    def ir(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        found = False
        if len(x) == 1:
            screen = self.currentScreen.ir("")
        else:
            screen, found = self.currentScreen.ir(secondWord)
        if found:
            self.currentScreen = screen
        self.currentScreen.mostrarDescripcion()

    def tomar(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        if len(x) == 1:
            self.currentScreen.tomar("",self.personaje)
        else:
            self.currentScreen.tomar(secondWord,self.personaje)

    def dejar(self,allInputsOrdered):
        x = allInputsOrdered[0]
        firstWord = allInputsOrdered[1]
        secondWord = allInputsOrdered[2]
        thirdWord = allInputsOrdered[3]
        if len(x) == 1:
            self.currentScreen.dejar("",self.personaje)
        else:
            self.currentScreen.dejar(secondWord,self.personaje)

    def ayuda(self,allInputsOrdered):
        verbos = ""
        for key in self.actionVerbs.keys():
            verbos += key + ", "
        print("puedes usar los verbos: "+verbos+"y todos con uno o dos objetos")

    def parseInput(self):
        x = list(map(str, input(self.personaje.showName() + ", que deseas hacer? ").split()))
        firstWord = str.lower(x[0])
        secondWord = ""
        thirdWord = ""
        if len(x) == 2:
            secondWord = str.lower(x[1])
        elif len(x) >= 3:
            secondWord = str.lower(x[1])
            thirdWord = str.lower(x[2])
        allInputsOrdered =[x,firstWord,secondWord,thirdWord]
        return allInputsOrdered

    def checkGameSolved(self):
        solvedGame = False
        totalPuzzlesSolved = 0
        totalPuzzles = len(self.puzzles)
        for p in self.puzzles:
            if p.statusSolved():
                totalPuzzlesSolved += 1
        if totalPuzzlesSolved == totalPuzzles:
            print("------------------------------------")
            print("Ganaste!! " + self.personaje.showName() + " Campeón de la vida y el Amoorrrrr")
            for p in self.puzzles:
                print(p.mostrarDescripcion())
            solvedGame=True
        return solvedGame

    def checkAction(self,allInputsOrdered):
        x = allInputsOrdered[0]
        verboCheckear = allInputsOrdered[1]
        verbo = self.sinonimosVerbos.checkSinonimo(verboCheckear)
        if verbo in self.actionVerbs.keys():
            # self.puzzleCheckSolved(allInputsOrdered)
            self.actionVerbs[verbo](allInputsOrdered)
        else:
            print("No se lo que quieres hacer: " + x[0])

    def play(self):
        while not self.solvedGame:
            allInputsOrdered = self.parseInput()
            self.checkAction(allInputsOrdered)
            self.solvedGame = self.checkGameSolved()

def main():
    juego = Game()
    juego.start()


if __name__ == "__main__":
    main()