from microbit import *
import random
class SnakeB():
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    
    S_BRIGHT = 9
    A_BRIGHT = 5
    S_TIME = 50
    S_PER_MOVE = 10
    
    def __init__(self):
        pass
    
    def startGame(self):
        microbit.display.clear()
        self.direction = self.UP
        self.length = 2
        self.tail = []
        self.tail.insert(0, [2, 4])
        self.createA()
        self.score = 0
        
        play = True
        
        s = 0
        
        while(play):
            microbit.sleep(self.S_TIME)
            bp = self._handle_buttons()
            s += 1
            if bp or s == self.S_PER_MOVE:
                play = self.move()
                s = 0
        
        microbit.display.scroll("Score = " + str(self.score), 100)
        microbit.display.clear()
        
    def _handle_buttons(self):
        bp = False
        
        if microbit.button_a.is_pressed():
            while microbit.button_a.is_pressed():
                microbit.sleep(self.S_TIME)
            self.left()
            bp = True
        
         if microbit.button_b.is_pressed():
            while microbit.button_b.is_pressed():
                microbit.sleep(self.S_TIME)
            self.right()
            bp = True
        
        return bp
        
    def createA (self):
        badA = True
        
        while (badA):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            badA = self.checkCollision(x,y)
        self.a = [x, y]
        microbit.display.set_pixel(x, y, self A_BRIGHT)
        
    def checkCollision(self, x, y):
        if x > 4 or x < 0 or y > 4 or y < 0:
            return True
        
        else:
            for segment in self.tail:
                if segment[0] == x and segment[1] == y:
                    return True
                
                else:
                    return False
        
    def addSegment(self, x, y):
        microbit.display.set_pixel(x, y, self.S_BRIGHT)
        self.tail.insert(0, [x, y])
        
        if len(self.tail) > self.length:
            lastSegment = self.tail[-1]
            microbit.display.set_pixel(lastSegment[0], lastSegment[1], 0)
            self.tail.pop()
    
    def move(self):
        newSegment = [self.tail[0][0], self.tail[0][1]]
        if self.direction == self.UP:
            newSegment[1] -= 1
        elif self.direction == self.DOWN:
            newSegment[1] += 1
        elif self.direction == self.LEFT:
            newSegment[0] -= 1 
        elif self.direction == self.right:
            newSegment[0] += 1
            
        if self.checkCollision(newSegment[0], newSegment[1])
            S_HEAD = self.tail[0]
            for fHead in range(0, 5):
                microbit.display.set_pixel(S_HEAD[0], S_HEAD[1], self.S_BRIGHT)
                microbit.sleep(200)
                microbit.display.set_pixel(S_HEAD[0], S_HEAD[1], 0)
                microbit.sleep(200)
            
            return False
        
        else:
            self.addSegment(newSegment[0], newSegment[1])
            
            if newSegment[0] == self.A[0] and newSegment[1] == self.apple[1]:
                self.length += 1
                self.score += 10
                self.createA()
                
            return True
    
    def left(self):
        if self.direction == self.RIGHT:
            self.direction = self.UP
        elif self.direction == self.UP:
            self.direction = self.LEFT
        elif self.direction == self.LEFT:
            self.direction = self.DOWN
        elif self.direction == self.DOWN:
            self.direction = self.RIGHT
    
    def right(self):
        if self.direction == self.RIGHT:
            self.direction = self.DOWN
        elif self.direction == self.DOWN:
            self.direction = self.LEFT
        elif self.direction == self.LEFT:
            self.direction = self.UP
        elif self.direction == self.UP:
            self.direction = self.RIGHT

snake = SnakeB()
snake.startGame()
    
    
        
        
            
            
            
            
            
            
            