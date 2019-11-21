#C-9.30
from heap import HeapBase

class modHeap(HeapBase):
    """sub class of HeapBase to perform non recursive implementations of upHeap and downHeap methods."""
    
    def upHeap(self,index):
        """Non recursive upheap method."""

        #throw an exception if heap is empty
        if self.heap_size == 0:
            raise Empty("Heap is empty.")

        currentIndex = index

        #get the parent index
        parent_index = (index-1)//2 #integer division
        
        #loop while index is within bounds and current node > parent node
        while self.heap[currentIndex] > self.heap[parent_index] and currentIndex > 0:
        
            #swap the parent with child
            self.swap(currentIndex, parent_index)

            #update the current index as the parent index
            currentIndex = parent_index

            #get the next parent index of the new currentIndex
            parent_index = (parent_index-1)//2 #integer division
            
#C-9.31
    def downHeap(self,index):
        
        """From the root node, swap the parent node with its children if 
        child nodes are larger than parent node. To insure heap properties are met.
        """
        
        index_left = 2*index + 1
        index_right = 2*index + 2
        
        #max heap parent node is greater than child node
        index_largest = index
        
        try:
            #while not out of bounds of array
            while index_largest < self.heap_size:
                
                #store the previous node
                prev_index = index_largest
                
            
                #while heap is within size of array and left index is greater than parent node
                if index_left < self.heap_size and self.heap[index_left] > self.heap[index_largest]:
                    
                    #save left index
                    index_largest = index_left
                
                #check if the right child is greater then the left child: largest is right node
                if index_right < self.heap_size and self.heap[index_right] > self.heap[index_largest]:
                
                    #save right index 
                    index_largest = index_right
                        
                
                #if previous index is not equal to current position
                if prev_index != index_largest:
                
                    #swap the parent node with child node
                    self.swap(prev_index,index_largest)
                    
                
                    #update the new left child and right child
                    index_left = 2*index_largest + 1
                    index_right = 2*index_largest + 2
                    
                else:
                    #break out of the loop if index_largest is still the previous node
                    break
                
        except:
            print("Infinite loop")
            
#C-9.38
    def insert_tree(self, heap2):
        """Input a heap, remove each node from the input heap and append to the existing heap."""
        
        while heap2.heap_size > 0:
            
            #insert removed node from heap 2 into heap 1, 
            #(removing max from heap 2 = O(logN)) + (inserting max from heap 2 to heap 1 = O(logN) due to upheap operation
            self.insert(heap2.removeMax())
            

        
        
if __name__ == "__main__":
    
    heap = modHeap()
    heap2 = modHeap()
    
    heap.insert(10)
    heap.insert(8)
    heap.insert(125)
    heap.insert(20)
    print("heap1")
    print("--------------------------")
    print("heap2")
    heap2.insert(-2)
    heap2.insert(0)
    heap2.insert(1)
    heap2.insert(321)
    print("-------------------------")
    print("Combined heaps")
    heap.insert_tree(heap2)
    heap.heap_sort()
    print("ADFDAF")


