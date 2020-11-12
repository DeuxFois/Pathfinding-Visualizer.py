from pathFinders import Dijkstra
from pathFinders import Astar
from mazeGenerators import randomMaze
from pathFinders import Bfs
from pathFinders import Dfs
import tkinter as tk
import Grid

class main():
    def __init__(self, row, col, sizeCase):
        self.win=tk.Tk()
        self.win.title("pathfiding vizualiser")

        self.canGrid = tk.Canvas(self.win,height=600,width=900)
        self.canBt = tk.Canvas(self.win,height=600,width=900)
        self.canGrid.bind('<ButtonRelease>',self.clic)
        
        self.guiGrid = Grid.Gui(row, col, sizeCase, self.win, self.canGrid, self.canBt)

        self.caseOption = tk.StringVar()
        self.pathOption = tk.StringVar()
        self.mazeControl = [tk.Button()]*1
        self.setBtn()  


    def setBtn(self):
        caseOptions = ("Start","End","Wall","Void") 
        self.caseOption.set(caseOptions[0])
        caseControls = tk.OptionMenu(self.canBt, self.caseOption, *caseOptions)
        caseControls.pack(side=tk.LEFT)

        pathOptions = ("Dijkstra","A*","BFS","DFS") 
        self.pathOption .set(pathOptions[0])
        self.pathOptions = tk.OptionMenu(self.canBt, self.pathOption , *pathOptions, command = self.changeCase)
        self.pathOptions.pack(side=tk.RIGHT, anchor = tk.CENTER)

        self.mazeControl[0] = tk.Button(self.canBt, text='random maze', command = lambda gui = self: randomMaze.Generate(self.guiGrid))
        for i in self.mazeControl:
            i.pack(side=tk.LEFT, padx='150')
        self.canGrid.pack()
        self.canBt.pack()#side=tk.LEFT


    def changeCase(self, Q):
        self.pathOptions.config(state="disable")
        self.guiGrid.paintGrid()
        opt = self.pathOption.get()
        path = False
        if(self.guiGrid.start != None and self.guiGrid.end != None):
            if (opt == "Dijkstra"):
                path = Dijkstra.Dijkstra(self.guiGrid)
            elif (opt == "A*"):
                path = Astar.Astar(self.guiGrid)
            elif (opt == "BFS"):
                path = Bfs.Bfs(self.guiGrid)
            elif (opt== "DFS"):
                path = Dfs.Dfs(self.guiGrid)
        if path:
            self.guiGrid.paintPath(path)
        self.pathOptions.config(state="normal")


    def clic(self,event):
        j=event.x//self.guiGrid.sizeCase
        i=event.y//self.guiGrid.sizeCase
        opt = self.caseOption.get()
        if (opt == "Void"):
            self.guiGrid.colorCase(j,i,'white') 

        elif (opt == "Wall"):
            self.guiGrid.grid[i][j] = -1
            self.guiGrid.colorCase(i,j,'dimgray')

        elif (opt == "Start"):
            if self.guiGrid.start:
                    self.guiGrid.colorCase(*(self.guiGrid.start),'white') 
            self.guiGrid.start = (j,i)
            self.guiGrid.colorCase(j,i,'deepskyblue') 

        elif (opt == "End"):
            if self.guiGrid.end:
                    self.guiGrid.colorCase(*(self.guiGrid.end),'white') 
            self.guiGrid.end = (j,i)
            self.guiGrid.colorCase(j,i,'limegreen')      


    def launch(self):
        self.win.mainloop() 