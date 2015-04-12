import snap

Rnd = snap.TRnd()
Graph = snap.GenRMat(900, 9000, .5, .1, .1, Rnd)
for EI in Graph.Edges():
    print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
