ElemRng={'Plates':(1,62655),
         'Fingers':(353693,574593),
         'GasPlenum':(574595,574596),
         'OilTubes':(574597,1228786)}
NodeRng={}
#----------------------------------------
aa=session.odbs[session.odbs.keys()[0]].rootAssembly
#--------elements----
for name in ElemRng.keys():
	ElementLabels=range(ElemRng[name][0],ElemRng[name][1])
	aa.instances[aa.instances.keys()[0]].ElementSetFromElementLabels(name, ElementLabels)
#--------nodes-------
for name in NodeRng.keys():
	NodeLabels=range(NodeRng[name][0],NodeRng[name][1])
	aa.instances[aa.instances.keys()[0]].NodeSetFromNodeLabels(name, NodeLabels)
