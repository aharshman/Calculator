# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:39:25 2021

@author: Alexa
"""

from button import Button
from graphics import *


class Calculator:
    
    def __init__(self):
        
        win = GraphWin('Calculator')
        win.setCoords(0,0,6,7)
        win.setBackground('slategray')
        
        self.win = win
        
        self.__createbuttons()
        self.__createDisplay()
        
    def __createbuttons(self):
        
        bspecs = [(1,1,'OFF'), (2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
                  
        self.buttons = []
        
        for (cx, cy, label) in bspecs:
        
            self.buttons.append(Button(self.win, Point(cx, cy), .75, .75, label, 'lightgray'))
            
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, '=', 'lightgray'))
        
        for b in self.buttons:
            
            b.activate()
            
    
    def __createDisplay(self):
        
        box = Rectangle(Point(0.5, 5.5), Point(5.5, 6.5))
        box.setFill('white')
        box.draw(self.win)
        
        text = Text(Point(3,6), ":)")
        text.draw(self.win)
        text.setFace('courier')
        text.setStyle('bold')
        text.setSize(16)
        
        self.display = text
        
    
    def getbutton(self):
        
        while True:
            
            p = self.win.getMouse()
            
            for b in self.buttons:
                
               if b.clicked(p):
                
                    return b.getlabel()
                
    def processButton(self, key):
        
        text = self.display.getText()
        
        if key == 'OFF':
            self.win.close()
        
        if key == 'C':
            self.display.setText('')
            
        elif key == '<-':
            self.display.setText(text[:-1])
        
        elif key == '=':
            
            try: 
                result = eval(text)
            except:
                result = 'SyntaxError'
            
            self.display.setText(str(result))
            
        else:
            self.display.setText(text+key)
            
    def run(self):
        
        while True:
            
            key = self.getbutton()
            self.processButton(key)
            
            
def main():
    
    c = Calculator()
    c.run()
    
main()
            
            
            
            
            
        