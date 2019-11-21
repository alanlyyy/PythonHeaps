from heap import HeapBase


class Item:
    """Item is a class in which we create buy or sell objects.
    key = number of shares
    value = Buy or Sell
    price = cost per share
    
    """
    def __init__(self,num_shares,choice,price):
        
        self._key = num_shares
        
        self._value = choice
        
        self._price = price

class stockHeap(HeapBase):
    """stockHeap is a subclass of HeapBase which takes Item objects that contain
    keys,values, and price.
    
    stockHeap uses a min oriented heap.
    
    upheap and downheap are modified to directly access keys of Item objects.
    
    """

    def upHeap(self, index):
        """check if node meets heap properties, otherwise swap nodes until the heap properties are met
        going up the tree. (upheap)

        """

        #get the parent index
        parent_index = (index-1)//2 #integer division

        #while root node is not reached and the parent node is smaller than child node
        if index > 0 and self.heap[index]._key < self.heap[parent_index]._key:

            #swap parent and child node
            self.swap(index,parent_index)

            #recursively go up the tree
            self.upHeap(parent_index)
        
    def downHeap(self, index):
        """From the root node, swap the parent node with its children if 
        child nodes are larger than parent node. To insure heap properties are met.
        """
        
        index_left = 2*index + 1
        index_right = 2*index + 2
        
        #max heap parent node is greater than child node
        index_largest = index
        
        #while heap is within size of array and left index is greater than parent node
        if index_left < self.heap_size and self.heap[index_left]._key < self.heap[index]._key:
            index_largest = index_left
        
        #check if the right child is greater then the left child: largest is right node
        if index_right < self.heap_size and self.heap[index_right]._key < self.heap[index_largest]._key:
            index_largest = index_right
            
        if index != index_largest:
        
            #swap the parent node with child node
            self.swap(index,index_largest)
            
            #go down the heap with largest node
            self.downHeap(index_largest)
            
    def get_min(self):
        
        #return the root node
        return self.heap[0]
        
    #O(logN)
    def removeMin(self):
        """Return the min item + removes it from the heap.
           Check if node is in correct position not violating heap properties.
        """
        
        min = self.get_min()
        
        #swap last element with root node
        self.swap(0,self.heap_size-1)
        
        #update the size 
        self.heap_size = self.heap_size - 1
        
        #move the root node down the heap to not violate heap properties.
        self.downHeap(0)
        
        return min
        
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
            min = self.removeMin()
            
            tempList.append(min)
            
            print(min._key,min._value,min._price)
        
        for i in range(0,size):
            
            self.insert(tempList[i])
            
    def changePrice(self,num_shares,choice,price):
        """Search for num shares and choice in the heap,
        
        if it exists change the price. else do nothing.
        
        O(N(logN) --> N for sorting, and logN for searching.
        """
        
        #sort heap
        self.heap_sort()
        
        #cut the heap in half
        index = self.heap_size// 2

        if num_shares <= self.heap[index]._key:
        
            #search for key in left half of array
            while index >= 0 and self.heap[index] != 0:
                
                if self.heap[index]._key == num_shares:
                    
                    #verify buy or sell option
                    if self.heap[index]._value == choice:
                        
                        prev_price = self.heap[index]._price
                        
                        #change the price of the stock
                        self.heap[index]._price = price
                        
                        print("%s %s shares, changed price from %s to %s." %(self.heap[index]._value, self.heap[index]._key, prev_price, price))
                    
                        break

                #go left of the array
                index -= 1
                
            
            #search right half of array            
        else:
            #search for key in right half of array
            while index <= self.heap_size and self.heap[index] != 0:
                
                #found the key
                if self.heap[index]._key == num_shares:
                    
                    #verify buy or sell option
                    if self.heap[index]._value == choice:
                        
                        prev_price = self.heap[index]._price
                        #change the price of the stock
                        self.heap[index]._price = price
                        
                        print("%s %s shares, changed price from %s to %s." %(self.heap[index]._value, self.heap[index]._key, prev_price, price) )
                    
                        break
                        
                #go right of the array
                index += 1
        
        #item does not exist in array
        print("%s %s shares for %s $ does not exist." %(choice, num_shares,price))
        
        
    def processOrder(self):
        """online computer system for trading stocks needs to process orders of
        the form “buy 100 shares at $x each” or “sell 100 shares at $y each.” A
        buy order for $x can only be processed if there is an existing sell order
        with price $y such that y ≤ x. Likewise, a sell order for $y can only be
        processed if there is an existing buy order with price $x such that y ≤ x.
        If a buy or sell order is entered but cannot be processed, it must wait for a
        future order that allows it to be processed.
        
        min oriented heap options are processed.
        if we want to process an buy option, we have to find a sell option with the same number of shares or greater.
        The difference between the share price is calculated as capital gains.
        """
        
        #sort by min
        self.heap_sort()
        
        min_shares = self.get_min()
        
        #store capital gains after processing stock order
        capitalGains = 0
        
        #at child node
        index = 1
        
        if min_shares._value == 'Buy':
            
            while index < self.heap_size:
            
                if self.heap[index]._value == 'Sell':
                    
                    #subtract min shares from current sell option, always positive since we are workin with min heap, account for bought shares
                    self.heap[index]._key -= min_shares._key
                    
                    #calculate the price and return to user
                    capitalGains = min_shares._key*(min_shares._price - self.heap[index]._price)
                    
                    #remove the min and update the heap to proper order
                    self.removeMin()
                    
                    break
                    
                else:
                    if index < self.heap_size:
                        #update the index 
                        index += 1
            if index > self.heap_size:
                return "Cannot process order, due to lack of sell options."
        else:
        
            while index < self.heap_size:
                if self.heap[index]._value == 'Buy':
                    
                    #subtract min shares from current sell option, always positive since we are workin with min heap, account for bought shares
                    self.heap[index]._key -= min_shares._key
                    
                    #calculate the price and return to user
                    capitalGains = min_shares._key*(min_shares._price - self.heap[index]._price)
                    
                    #remove the min and update the heap
                    self.removeMin()
                    
                    break
                    
                else:
                    if index < self.heap_size:
                        #update the index 
                        index += 1
            if index > self.heap_size:
                return "Cannot process order, due to lack of buy options."
            
        #organize heap to be min oriented
        self.heap_sort()
                    
        return capitalGains
            



            

if __name__ == "__main__":
    
    
    stock = stockHeap()
    stock.insert(Item(100,"Buy",500))
    #stock.insert(Item(50,"Buy",10))
    stock.insert(Item(100,"Sell",30))
    stock.insert(Item(20,"Buy",22))
    stock.insert(Item(199,"Buy",3))
    stock.insert(Item(66,"Sell",55))
    stock.changePrice(98,"Sell",15)
    
    #case where choice does not exist, but num shares exist.
    stock.changePrice(1000,"Sell",15)
    
    #case where choice and num shares does not exist.
    stock.changePrice(187,"Sell",15)
    
    print(stock.processOrder())