import random

from math import floor


def Generate(GUI):
    h = GUI.COL
    w = GUI.ROW
    GUI.restatGrid()
    GUI.paintGrid()
    for i in range (0,w):
        GUI.colorCase(0,i, "dimgray")
        GUI.colorCase(h-1,i, "dimgray")
    for i in range (0,h):
        GUI.colorCase(i,0, "dimgray")
        GUI.colorCase(i,w-1, "dimgray")
    divide(w-1,h-1,1,1,GUI)


def divide(ax,ay,zx,zy,GUI):
    dx = ax - zx
    dy = ay - zy
    if dx < 2 or dy < 2:
        if dx > 1:
            for x in range(zx, ax):
                        GUI.colorCase(zy,x,"dimgray")  
        elif dy > 1:
            for y in range(zy, ay-1):
                    GUI.colorCase(y,zx,"dimgray")
        return

    isVertical = 1 if dy > dx else (0 if dx > dy else random.randrange(2))
    xp = random.randrange(zx, ax-(isVertical))
    yp = random.randrange(zy, ay-(isVertical))
    
    if isVertical:
        for i in range(xp,ax):
                GUI.colorCase(yp,i,"white")          
        divide(ax,ay, zx, yp, GUI)
        divide(ax,yp,zx, zy, GUI)
    else:
        for i in range (yp,ay):
                GUI.colorCase(i,xp,"white")    
        divide(ax,ay,xp+1, zy,GUI)
        divide(xp,ay,zx, zy,GUI)