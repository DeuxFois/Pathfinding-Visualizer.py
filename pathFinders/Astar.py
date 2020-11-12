from pathFinders  import Tree

def Astar(GUI):
    start_node = Tree.Node(GUI.start, None)
    goal_node = Tree.Node(GUI.end, None)
    start_node.g = start_node.h = start_node.f = 0
    goal_node.g = goal_node.h = goal_node.f = 0

    open = []
    closed = []
    open.append(start_node)

    while len(open) > 0:
        current_node = open[0]
        current_index = 0
        for index, item in enumerate(open):
            if item.t < current_node.t:
                current_node = item
                current_index = index

        open.pop(current_index)
        closed.append(current_node)
        
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path  
        
        children = []
        (x, y) = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] 

        for next in neighbors: 
            if GUI.isInsideGrid(*(next)):
                map_value = GUI.grid[next[1]][next[0]]
                if(map_value == -1):
                   continue
                new_node = Tree.Node(next,current_node)
                if new_node not in children:
                    children.append(new_node)

       
        for child in children:
            for closed_child in closed:
                if child == closed_child:
                    break
            else:
                child.s = current_node.s + 1
                # child.g = (child.position[0] - goal_node.position[0]) + (child.position[1] - goal_node.position[1]) #heuristic distance
                child.g = ((child.position[0] - goal_node.position[0]) ** 2) + ((child.position[1] - goal_node.position[1]) ** 2)
                child.t = child.s + child.g                   
                for open_node in open:
                    if child == open_node and child.s >= open_node.s:
                        break
                else:
                    open.append(child)
                    if(GUI.isInsideGrid(*(child.position))):
                        GUI.colorCase(*(child.position),'lightgray')                
    return None