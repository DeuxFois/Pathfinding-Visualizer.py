import tkinter as tk

colors =['white','deepskyblue','limegreen','dimgray']
class Gui():
    def __init__(self, row, col, sizeCase,win, canDraw, canBtGui):
        self.win = win
        self.canGrid = canDraw
        self.canBtGrid = canBtGui
        self.ROW = row
        self.COL = col
        self.sizeCase = sizeCase

        self.case=[[self.canGrid.create_rectangle(i*self.sizeCase,j*self.sizeCase,(i+1)*self.sizeCase,(j+1)*self.sizeCase,fill="#FFFFFF")
                                                for i in range(col)] for j in range(row)]
        self.grid = [[ 0 for i in range(col)] for j in range(row)]
        self.start = None
        self.end = None 


    def colorCase(self,x,y,color):
        self.canGrid.itemconfigure(self.case[y][x],fill=color)
        if color == "dimgray":
            self.grid[y][x] = -1
        elif color == "white":
            self.grid[y][x] = 0
        self.win.after(0,self.win.update())   


    def paintGrid(self):
        for i in range (0, self.COL):
            for j in range (0,self.ROW):
                if self.grid[j][i] == -1:
                    self.canGrid.itemconfigure(self.case[j][i],fill="dimgray")
                else:
                    self.canGrid.itemconfigure(self.case[j][i],fill="white")
        if self.start:
            self.canGrid.itemconfigure(self.case[self.start[1]][self.start[0]],fill="deepskyblue")
        if self.end:
            self.canGrid.itemconfigure(self.case[self.end[1]][self.end[0]],fill="limegreen")


    def paintPath(self, path):
                for pos in path:
                    self.colorCase(pos[0],pos[1],'limegreen')
                    self.win.after(1,self.win.update())  
    
    def isInsideGrid(self, y, x):
        return (x >= 0 and x < self.ROW and y >= 0 and y < self.COL) 

    def restatGrid(self): 
        self.grid = [[ 0 for i in range(self.COL)] for j in range(self.ROW)]