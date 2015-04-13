#Generates a recursive matrix 
#GenRMat(nodes, edges, a, b, c, Rnd)
#a,b,c = probabilities that quadrant will be chosen

import snap

Rnd = snap.TRnd()
Graph = snap.GenRMat(900, 9000, .5, .1, .1, Rnd)
for EI in Graph.Edges():
    print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
