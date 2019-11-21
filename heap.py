
#max number of items that can be stored in the heap
CAPACITY = 8

class HeapBase:
    
    def __init__(self):
    
        #create an array with capacity elements
        self.heap = [0]*CAPACITY
        
        #counter to keep track of num items in heap
        self.heap_size = 0
        
    #O(logN) because need to make sure heap propertises are not violated
    def insert(self, item):
        
        #if capacity is reached don't insert any more items
        if CAPACITY == self.heap_size:
            return
        
        #insert the item + increment the counter
        self.heap[self.heap_size] = item
        self.heap_size += 1
        
        #1. insert item to last position of array
        #2. Validate heap properties are not violated
        
        self.upHeap(self.heap_size-1)
    
    #O(logN)
    def upHeap(self, index):
        """check if node meets heap properties, otherwise swap nodes until the heap properties are met
        going up the tree. (upheap)
        
        """
        
        #get the parent index
        parent_index = (index-1)//2 #integer division
        
        #while root node is not reached and the parent node is smaller than child node
        if index > 0 and self.heap[index] >self.heap[parent_index]:
            
            #swap parent and child node
            self.swap(index,parent_index)
            
            #recursively go up the tree
            self.upHeap(parent_index)
            
    def swap(self, index1, index2):
        
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]
    
    #O(1) 
    def get_max(self):
        #return the root node
        return self.heap[0]
    
    #O(logN)
    def removeMax(self):
        """Return the max item + removes it from the heap.
           Check if node is in correct position not violating heap properties.
        """
        
        max = self.get_max()
        
        #swap last element with root node
        self.swap(0,self.heap_size-1)
        
        #update the size 
        self.heap_size = self.heap_size - 1
        
        #move the root node down the heap to not violate heap properties.
        self.downHeap(0)
        
        return max
        
    def downHeap(self, index):
        """From the root node, swap the parent node with its children if 
        child nodes are larger than parent node. To insure heap properties are met.
        """
        
        index_left = 2*index + 1
        index_right = 2*index + 2
        
        #max heap parent node is greater than child node
        index_largest = index
        
        #while heap is within size of array and left index is greater than parent node
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left
        
        #check if the right child is greater then the left child: largest is right node
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right
            
        if index != index_largest:
        
            #swap the parent node with child node
            self.swap(index,index_largest)
            
            #go down the heap with largest node
            self.downHeap(index_largest)
            
    def heap_sort(self):
        """Sort N nodes in heap.
        Every removeMax operation called takes O(logN) because of downHeap()
        
        Complete running time: O(N*logN)
        """
        
        tempList = []
        
        #store size of heap
        size = self.heap_size
        
        for i in range(0,size):
            
            #call removeMax N times to return max element and remove max every iteration
            max = self.removeMax()
            
            tempList.append(max)
            
            #print(max._key,max._value,max._price)
        
        for i in range(0,size):
            
            self.insert(tempList[i])
            
            
if __name__ == '__main__':
    
    heap = HeapBase()
    
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)
    
    heap.heap_sort()