import turtle

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
            
            
            
            
if __name__ == '__main__':
    Circuito = Circuito(640, 480)