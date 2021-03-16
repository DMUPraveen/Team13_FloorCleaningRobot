class Grid:
    """
    Grids upper left corner is 0,0 and the positive direction for x and y are left(east)
    and down(south) respectively
    
    
    
    """
    Directions = {
        "N"     : 0,
        "E"     : 1,
        "S"     : 2,
        "W"     : 3
    }
    DirectionMap = {
        0 : (0,-1)  , #North 
        1 : (1,0)   , #East
        2 : (0,1)   , #South
        3 : (-1,0)  , #West
    }
    states = {
        "INVALID"   : -1,
        "FREE"      : 0,
        "BLOCKED"   : 1,
        "CLEANED"   : 2,
    }
    def __init__(self,rows,columns,array=None):
        if(array == None):
            self.array = [0 for _ in range(rows*columns)] #By default all the tiles are free
        else:
            if(len(array) != rows*columns):
                raise Exception("Invalid map provided")
            self.array = [i for i in array]
        self.rows = rows
        self.columns = columns
        self.UnblockedTiles = self.array.count(self.states["FREE"])
        self.cleanedTiles = 0
    def getTileState(self,x,y)->int:
        if(x <0 or y <0 or x>self.columns or y > self.rows):
            return -1
        return self.array[y*self.columns +x]
    def setstate(self,x,y,state:str):
        assert(self.getTileState(x,y) !=self.states["Invalid"])
        self.array[y*self.columns+x] = self.states[state]

    def cleanTile(self,x,y):
        if(self.getTileState(x,y) == self.states["FREE"]):
            self.setstate(x,y,"CLEAN")
            self.cleanedTiles += 1
            return True
        return False


    def Invalid(self,x,y):
        return self.getTileState(x,y) == self.states["INVALID"]
    
    def blocked(self,x,y):
        return self.getTileState(x,y) == self.states["BLOCKED"]
    
    def Id(self,x,y):
        if(x <0 or  y <0 or x>self.columns or y > self.rows):
            return None
        return y*self.columns +x
    
    def getNeighbours(self,x,y):
        connections = []
        if(self.Invalid(x,y)):
            return connections
        for key in self.DirectionMap:
            dx,dy = self.DirectionMap[key]
            newX,newY = x+dx,y+dy
            Id = self.Id(newX,newY)
            if(Id != None):
                connection.append(Id)
    


class Robot:
    Directions = {
        "N"     : 0,
        "E"     : 1,
        "S"     : 2,
        "W"     : 3
    }
    DirectionMap = {
        0 : (0,-1)  , #North 
        1 : (1,0)   , #East
        2 : (0,1)   , #South
        3 : (-1,0)  , #West
    }
    InvalidMove = -1
    MoveForwardTime = 1
    SprayTime = 1
    Turnby90Time = 2
    PossibleMoves = {
        "Spray"                 : "SP",
        "MoveForward"           : "MF",
        "TurnClockwise"         : "TR",
        "TurnCounterClockwise"  : "TL"
    
    }
    RelativeDirections = {
        "Left" : 1,
        "Right": -1,
        "Back" : 2,
        "Forward" : 0,
    }

    def __init__(self,grid :Grid,startX,startY,orientation=Directions["N"]):
        if(grid.getTileState(startX,startY) != grid.states["FREE"]):
            raise Exception("Invalid Start Position")
        self.X = startX
        self.Y = startY
        self.orientation = orientation # [0->3]
        self.Vx ,self.Vy = self.DirectionMap[self.orientation] #X and Y velocities
        self.grid = grid
        self.moves = [self.PossibleMoves["Spray"]] #moves taken so far (Including the first spray)
        self.time = 1 #time taken so far (Time taken for the spray action)

    def incrementTime(self,time:int):
        self.time += time
    def addMove(self,move:str):
        self.moves.append(self.PossibleMoves[move])

    def moveForward(self):
        newX = self.X + self.Vx
        newY = self.Y + self.Vy
        state = self.grid.getTileState(newX,newY)

        if(state == self.grid.states["FREE"]):
            #Setting the new Position of the robot
            self.X = newX
            self.Y = newY
            #Cleaning the Tile
            self.grid.cleanTile(self.X,self.Y)
            self.incrementTime(Robot.MoveForwardTime + Robot.SprayTime)
            self.addMove("MoveForward")
            self.addMove("Spray")
            return True

        if(state == self.grid.states["CLEANED"]):
            #Setting the new Position of the robot
            self.X = newX
            self.Y = newY
            self.incrementTime(Robot.MoveForwardTime)# We don't clean the already cleaned tile
            self.addMove("MoveForward")
            return True
        
        return False

    def setOrientation(self,orientation:int):
        '''Sets the orientation to a given orientation and changes the velocities appropiately'''
        assert(orientation <4 and orientation >=0)

        self.orientation = orientation
        self.Vx ,self.Vy = self.DirectionMap[orientation]

    def turnClockwise(self):
        '''Turns by 90 degrees Clockwise'''
        self.setOrientation((self.orientation+1)%4)
        self.incrementTime(Robot.Turnby90Time)
        self.addMove("TurnClockwise")
    
    def turnCounterClockWise(self):
        '''Turns by 90 degrees Counter-Clockwise'''
        self.setOrientation((self.orientation-1)%4)
        self.incrementTime(Robot.Turnby90Time)
        self.addMove("TurnCounterClockwise")

    def turntoOrientation(self,Neworientation : int): #returns (time,[list of instructions])
        change = (Neworientation - self.orientation) % 4

        if(change == 1):
            self.incrementTime(Robot.Turnby90Time)
            self.addMove("TurnClockwise")
        if(change == 2):
            self.incrementTime(Robot.Turnby90Time*2)
            self.addMove("TurnClockwise")
            self.addMove("TurnClockwise")
        if(change == 3):
            self.incrementTime(Robot.Turnby90Time)
            self.addMove("TurnCounterClockwise")
        
        self.setOrientation(Neworientation)

    def getNeighbourSquareABS(self,orientation:int):
        dx,dy = self.DirectionMap[orientation]
        return self.grid.getTileState(self.X+dx,self.Y+dy)

    def getNeighbourSquareREL(self,relativeDirection:str):
        orientation = (self.orientation+self.RelativeDirections[relativeDirection])%4
        return self.getNeighbourSquareABS(orientation)

    def goToNeighboutSquareABS(self,orientation:int):
        state = self.getNeighbourSquareABS(orientation)
        if(state == Grid.states["CLEAN"] or state == Grid.states["FREE"]):
            self.turntoOrientation(orientation)
            self.moveForward()
            return True
        else:
            return False
    
    def goToNeighboutSquareREL(self,relativeDirection:str):
        orientation = (self.orientation+self.RelativeDirections[relativeDirection])%4
        return self.goToNeighboutSquareABS(orientation)

    






