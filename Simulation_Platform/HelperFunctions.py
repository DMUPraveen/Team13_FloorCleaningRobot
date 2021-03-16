
from .Simulation import Grid
class DijkstarNode():
    def __init__(self,orientation,distance,Id,parent=None):
        self.orientation = orientation
        self.distance = distance
        self.parent = parent
        self.id = Id

class Dijkstar():
    def __init__(self):
        self.NodeMap = {} #Id -> Node
        self.Nodes= []
        self.finished = set()


    def reset(self):
        self.NodeMap.clear()
        self.Nodes.clear()
        self.finished.clear()
    
    def popNode(self):
        if(len(self.Nodes) == 0):
            return None
        else:
            return self.Nodes.pop(0)

    def sort(self):
        self.Nodes.sort(key = lambda x : x.distance)

    def addNewNode(self,Node : DijkstarNode):
        if(Node.id in self.NodeMap):
            return False
        else:
            self.NodeMap[Node.id] = Node
            self.Nodes.append(Node)
            self.sort()
        
        return True

    def updateNodeDistance(self,Id,newDistance,newOrientation,newParent):
        if(Id not in self.NodeMap):
            return False

        Node = self.NodeMap[Id]
        assert(Node.distance > newDistance)
        Node.distance = newDistance
        Node.newOrientation = newOrientation
        Node.parent = newParent
        self.sort()
        return True

    def finish(self,id):
        self.finished.add(id)

    def Isfinished(self,id):
        return (id in self.finished)

    def Isin(self,id):
        return (id in self.NodeMap)
    def Run(self,startId,startOrientation,endFunction,grid :Grid,distanceFunction,initialDistance=0):
        '''endfunction is of the form Node->bool'''
        finished = False
        self.addNewNode(
            DijkstarNode(startOrientation,initialDistance,startId)
        )
        topNode = None
        while (len(self.Nodes) != 0):
            topNode = self.popNode()
            self.finish(topNode.id)
            if(endFunction(topNode)):
                finished = True
                break
            x,y = grid.getXY(topNode.id)
            connections = grid.getNeighbours(x,y,topNode.orientation,topNode.distance,distanceFunction)
            for connection in connections:
                Id,distance,orientation = connection
                if(not self.Isfinished(Id)):
                    if(self.Isin(Id)):
                        if(self.NodeMap[Id].distance > distance):
                            self.updateNodeDistance(Id,distance,orientation,topNode)
                    else:
                        self.addNewNode(
                            DijkstarNode(orientation,distance,Id,topNode)
                        )

        path = []
        if(not finished):
            return path
        while(topNode != None):
            path.append(topNode.id)
            topNode = topNode.parent
        self.reset()
        path.reverse()
        return path









