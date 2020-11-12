from pathFinders  import Tree

def Bfs(GUI):
    start_node = Tree.Node(GUI.start, None)
    goal_node = Tree.Node(GUI.end, None)
    open = []
    closed = []
    open.append(start_node)
    length = 0
    while len(open) > 0:
        current_node = open.pop(0)
        length -= 1
        (x, y) = current_node.position
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path

        closed.append(current_node)
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for next in neighbors: 
            if GUI.isInsideGrid(*(next)):
                map_value = GUI.grid[next[1]][next[0]]
                if(map_value == -1):
                    continue
                neighbor = Tree.Node(next, current_node)

                if(neighbor in closed):
                    continue
                
                if (neighbor not in open):
                    open.append(neighbor)
                    length += 1
                GUI.colorCase(*(neighbor.position),'lightgray')       
    return None