

class DijkstarNode():
    def __init__(self,orientation,connections,distance=float('inf'),parent=None):
        self.orientation = orientation
        self.distacne = distance
        self.parent = parent
        self.connections = connections







class PriorityQueue:
    NoIndex = -1
    def __init__(self,compareFunction):
        '''The compare function should return True if the first index
        should be higher in the priority queue '''
        self.array = []
        self.compareFunction = compareFunction
        self.size = 0
        self.indexes = {}
        


    def IndexOf(self,val):
        if(val not in self.indexes):
            return NoIndex

        else:
            return self.indexes[val]

    def higher(self,Index1,Index2):
        return self.compareFunction(self.array[Index1],self.array[Index2])
    
    @staticmethod
    def left(i):
        return 2*i+1

    @staticmethod
    def right(i):
        return 2*i+2

    @staticmethod
    def parent(i):
        return (i-1)//2


    def swap(self,i,j):
        self.indexes[self.array[i]] = j
        self.indexes[self.array[j]] = i
        self.array[i] ,self.array[j] = self.array[j] , self.array[i]
        

    def heapify(self,index):
        
        largest = index
        left = self.left(index)
        right = self.right(index)
        if(left < self.size and self.higher(left,largest)):
            largest = left
        
        if(right < self.size and self.higher(right,largest)):
            largest = right

        if(largest != index):
            self.swap(index,largest)
            self.heapify(largest)


    def bubbleUp(self,index):
        while True:
            if(index == 0):
                break
            parent = self.parent(index)
            if(self.higher(index,parent)):
                self.swap(index,parent)
            else:
                break
            index = parent



    def push(self,value):
        self.array.append(value)
        self.size +=1
        self.indexes[value] = self.size-1
        self.bubbleUp(self.size-1)
    
    def empty(self):
        return self.size == 0

    def pop(self):
        if(self.empty()):
            raise Exception("Priority Queue Underflow")
        self.swap(0,self.size-1)
        self.size -=1
        self.heapify(0)
        return self.array.pop(-1)







def main():
    P = PriorityQueue(lambda x,y : x > y)
    example = [1,8,5,7,6,3,4,9,8,6,3,2,1]
    print(sorted(example))
    for i in example:
        P.push(i)

    test = []
    while(not P.empty()):
        test.append(P.pop())

    print(test)


if __name__ == "__main__":
    main()