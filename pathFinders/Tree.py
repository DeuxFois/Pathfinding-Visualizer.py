class Node():
    def __init__(self,position,parent):
        self.position = position
        self.parent = parent
        self.s = 0 # Distance to start node
        self.g = 0 # Distance to goal node
        self.t = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.t < other.t
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.t))
