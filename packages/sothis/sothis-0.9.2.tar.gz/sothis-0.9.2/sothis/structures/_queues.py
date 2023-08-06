"""
Name: _queues.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: Queue based and related data structures
"""

class priority_queue:
    """ assumes comparables can be compared based on integer value"""
    
    def __init__(self, key, maxsize=1 << 16, data=None):
        self.heap = [None for _ in range(maxsize + 1)]  # list heap representation
        self.locations = {}
        self.size = 0  # number of nodes currently in queue
        self.maxsize = maxsize  # maxsize of the heap
        self.key = key  # priority function
        if data:
            for e in data:
                self.put(e)
    
    def put(self, __item):
        """
        insert a new item into the priority queue
        :param __item: new item
        :return: None
        """
        if self.size == self.maxsize:
            raise IndexError
        self.size += 1
        self.heap[self.size] = __item
        self.locations[__item] = self.size
        self._heapup(self.size)
    
    def __contains__(self, item):
        return item in self.heap
    
    def update(self, __old, __new):
        """
        update the priority item's priority in
        the queue if it exists by either increasing
        or decreasing the key
        :param __old: exisitng priority item
        :param __new: updated or new version of priority item
        :return: none
        """
        i = self.locations.get(__old, False)  # get the location of the item in the heap
        if not i:
            raise IndexError(f"value {__old} not in queue")
        
        if __new == __old:  # no change to be made
            return
        
        self.heap[i] = MININT32  # update item to be minimum value
        self._heapup(i)  # move it up to the top
        self.min()  # remove it
        self.put(__new)  # insert new value into heap
    
    def min(self):
        """
        extract the minimum item from the queue
        :return: item with min priority key
        """
        if self.size == 0:
            raise IndexError
        
        # swap index locations of items and the items themselves
        (self.locations[self.heap[1]], self.locations[self.heap[self.size]]) = self.size, 1
        (self.heap[1], self.heap[self.size]) = (self.heap[self.size], self.heap[1])
        
        t = self.heap[self.size]
        
        del self.locations[t]
        
        self.heap[self.size] = None  # remove
        self._heapdown(1)  # reheapify starting from root
        self.size -= 1
        return t
    
    def _heapup(self, i):
        """up heapify utility"""
        while i > 1:
            p = i >> 1
            if self.key(self.heap[i]) < self.key(self.heap[p]):
                (self.locations[self.heap[i]], self.locations[self.heap[p]]) = p, i
                (self.heap[p], self.heap[i]) = (self.heap[i], self.heap[p])
                i = p
            else:
                break
    
    def _heapdown(self, i):
        """down heapify utility"""
        while (i + i) < self.size:
            (l, r) = ((i + i), (i + i) + 1)
            mc = l
            if (self.heap[r] != None) and (self.key(self.heap[r]) < self.key(self.heap[l])):
                mc = r
            if self.key(self.heap[mc]) < self.key(self.heap[i]):
                (self.locations[self.heap[mc]], self.locations[self.heap[i]]) = i, mc
                (self.heap[mc], self.heap[i]) = (self.heap[i], self.heap[mc])
                i = mc
            else:
                break
    
    def __str__(self):
        return str(self.heap)
    
    def __len__(self):
        return self.size



