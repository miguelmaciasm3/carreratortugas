import turtle
import random

class Circuito():
    corredores = []
    __posicionystart = (-30, -10, 10, 30)
    __colortortuga = ('red', 'green', 'purple', 'blue', 'black')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startline = -width/2 + 20
        self.__finishline = width/2 - 20
        self.__createrunners()
    
    def __createrunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.color(self.__colortortuga[i])
            new_turtle.setpos(self.__startline, self.__posicionystart[i])
            
            
            self.corredores.append(new_turtle)
    def competir(self):
        hayganador = False
        while not hayganador:
            for tortuga in self.corredores:
                avance = random.randint(1, 6)
                tortuga.fd(avance)
                if tortuga.position()[0] >= self.__finishline:
                    hayganador = True
                    print("¡¡¡Ha ganado la toruga de color {}!!!".format(tortuga.color()[0]))
            
            
if __name__ == '__main__':
    Circuito = Circuito(640, 480)
    Circuito.competir()