# Node represents a distributed entity, such as a router or a client.
# In reality, these nodes would probably be talking over some communication channel, such as sockets or pipes.
# In order to simulate that, in this code, the nodes are talking by calling functions on each other.
global iterations
iterations = 0

class Node:

    def __init__(self, name):
        self.name = name
        # initally has no neighbors
        self.nbrs = {}
        self.weights = {}
        # only knows d to itself, which is 0
        self.table = {name: 0}
        self.nbr_tables = {}
        self.iterations = 0

    def add_nbr(self, node, weight):
        self.nbrs[node.name] = node
        self.weights[node.name] = weight
        self.table[node.name] = weight

    # returns weight from current node to any other node
    def weight(self, nbr):
        if nbr == self.name:
            return 0
        if nbr in self.weights:
            return self.weights[nbr]
        return float("inf")

    # signals that the node can talk to other nodes (start the simulation)
    def start(self):
        # when node can talk to neighbors, tell neighbors to update on itsef
        for nbr in self.nbrs.values():
            nbr.update(self)

    def get_row(self):
        return self.table

    # returns shortest distance from one node to another by accessing its table/row
    def D(self, node_name):
        return self.table[node_name]

    # updates weight to another node and reruns algorithm.
    def update_weight(self, node, weight):
        self.iterations = 0
        if self.weights[node.name] != weight:
            self.weights[node.name] = weight
            self.table[node.name] = weight
            return self.update(self, True)
        

    # update our table based on an update of a neighboring node
    def update(self, node, update = False):
        updated = False

        # Get the row of the updating node
        row = node.get_row()
        self.nbr_tables[node.name] = row

        # for every other node in the node's DV, use formula to calculate distance
        for node, distance in row.items():
            if node != self.name:
                # D is a list of possible distances to node
                D = []
                # for every one of our nbrs, calculate distance to node and add to distances list
                for nbr, table in self.nbr_tables.items():
                    if node in table and nbr != self.name:
                        # distance to node is weight to nbr + distance to node from neighbor
                        D.append(self.weight(nbr) + table[node])
                        #if update and (self.name == "y" or self.name == "z"):
                        #    print("appending", "to:", node, "via:", nbr, D[-1], self.weight(nbr), table[node])
                # also append just the weight to that node (c(x,y
                D.append(self.weight(node))
                # take the min as the distance
                d = min(D)
                # if this min is different, update and table and set updated
                if node not in self.table or self.table[node] != d:
                    self.table[node] = d
                    updated = True
        
        # If table is updated, notify neighbor
        if updated:
            global iterations
            iterations += 1
            if update and (self.name == "y" or self.name == "z"):
                print(self.name, self.table)
            for nbr in self.nbrs.values():
                #if update and (self.name == "y" or self.name == "z"):
                #    print("notifying", nbr.name)
                nbr.update(self, update)
