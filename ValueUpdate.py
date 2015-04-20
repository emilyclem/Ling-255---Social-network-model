#Sorry for the messiness. I'll eventually organize this more, just wanted to throw something up here.
#currently this goes as far as calculating the probability that a node will copy any neighbor.


#import needed packages
import snap
import numpy

#generate RMAT graph using snap package
Rnd = snap.TRnd()
Graph = snap.GenRMat(900, 9000, .6, .1, .15, Rnd)

#define class that puts a node (i.e. speaker) with a value (i.e. linguistic variable)
class Speaker: 
    def __init__(self, node, indeg, outdeg, value):
        self.node = node
        self.indeg = indeg
        self.outdeg = outdeg
        self.value = value

#create a list of "Speaker" objects for each node in the RMAT graph 
nodes_ = []
for node in Graph.Nodes():
    nodes_.append(Speaker(node.GetId(), node.GetInDeg(), node.GetOutDeg(), numpy.random.randint(8)))

#create list of all nodes that can be influenced (i.e. have an out degree?)
#I hope I'm interpreting this bit right from the article
Copyers = []
for edge in Graph.Edges():
    Copyers.append(edge.GetSrcNId())
copyers = sorted(set(Copyers))

#calculate the probability that each node will be influenced by any of its neighbors
def ValueUpdate(speakers):
    for i in speakers:
        xneighbors = []
        indegs = 0
        for edge in Graph.Edges():
            if edge.GetSrcNId() == i:
                xneighbors.append(edge.GetDstNId())
        for n in xneighbors:
            for y in nodes_:
                yindeg = 0
                if y.node == n:
                    yindeg = float(y.indeg)
                    indegs = indegs + yindeg
        for n in xneighbors:
            nindeg = 0
            for y in nodes_:
                if y.node == n:
                    nindeg = float(y.indeg)
                probn = float(nindeg/indegs)
            print(i, n, probn)

#run this function on the set of nodes that can be influenced
ValueUpdate(copyers)

#for now I just threw in the print statement at the end so I knew it was doing what I wanted it to.
#There are definitely ways to clean this up. I just haven't had the time to go back through it.
