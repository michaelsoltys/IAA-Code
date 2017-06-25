# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 5.30 - Paging
## Ryan McIntyre
## 6/22/2017
## python 3.5.2

from collections import Counter as counter

"""
Online*:
    LRU = "Least Recently Used", self explanatory
    FIFO = "First In / First Out", self explanatory
    LIFO = "Last In / First Out", self explanatory but stupid in most situations
    LFU = "Least Frequently Used", self explanatory. Use LRU as "backup" sort?
    CLOCK = go to wikipedia, but short version:
            cache is circular linked list, with auxillary circular reference list.
            reference list is set to '1' at position of pointer when a new page is
            inserted into cache. In order to evict, look at pointer. if referenced
            list at pointer is 1, change to 0 and move to next item to repeat. If
            referenced is 0, evict and add new page (set reference to 0) and move
            pointer.
            
            Basically "LRU" but each inserted page has an "extra life" before it
            gets evictet. Small cost for (usually) larger gain over LRU, worst
            case is LRU + "extra check" for each eviction.

Offline:
    LFD = "Longest Forward Distance", self explanatory, equivalent to OPT
"""

#------------------------------------------------------------------------------
#------------------------------------------------------------------linked_lists
#------------------------------------------------------------------------------


class ll_item():
    
    def __init__(self,tag=0):
        self.tag = tag
        self.prev = None
        self.next = None
    
    def set_next(self,n):
        self.next = n
    
    def set_prev(self,n):
        self.prev = n
        
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
        
    def set_tag(self,tag):
        self.tag = tag
    
    def get_tag(self):
        return self.tag
        
            
class ll():
    
    def __init__(self,cache_size):
        self.head = ll_item('head')
        body = [ll_item() for i in range(cache_size)]
        self.head.set_next(body[0])
        body[0].set_prev(self.head)
        for i in range(1,len(body)):
            body[i-1].set_next(body[i])
            body[i].set_prev(body[i-1])
        self.current = self.head.get_next()
        
    def get_cur(self):
        return self.current.get_tag()
    
    def set_cur(self,tag):
        self.current.set_tag(tag)
    
    def get_head(self):
        return self.head
        
    def turn(self):
        self.current = self.current.get_next()
    
    def get_next(self):
        return self.current.get_next()
        
    def detach(self):
        self.current.get_prev().set_next(self.current.get_next())
        if self.current.get_next():
            self.current.get_next().set_prev(self.current.get_prev())
        self.turn()
    
    def prepend(self,tag):
        new = ll_item(tag)
        h = self.head.get_next()
        self.head.set_next(new)
        new.set_prev(self.head)
        h.set_prev(new)
        new.set_next(h)
        self.current = new
    
    def mtf(self):
        c = self.current
        self.detach()
        h = self.head.get_next()
        self.head.set_next(c)
        c.set_prev(self.head)
        c.set_next(h)
        h.set_prev(c)
    
    def reset(self):
        self.current = self.head
    
#------------------------------------------------------------------------------
#---------------------------------------------------------------------------LRU
#------------------------------------------------------------------------------


class LRU():
    
    def __init__(self,cache_size):
        self.ll = ll(cache_size)
        self.fault_count = 0
    
    def process(self,request):
        self.ll.reset()
        done = False
        while self.ll.get_next():
            self.ll.turn()
            tag = self.ll.get_cur()
            if tag == request:
                done = True
                self.ll.mtf()
                break
            elif tag == 0:
                self.fault_count += 1
                self.ll.set_cur(request)
                self.ll.mtf()
                done = True
                break
        if not done:
            self.ll.set_cur(request)
            self.ll.mtf()
            self.fault_count += 1
        
    def reset_cache_size(self,n):
        self.__init__(n)

#------------------------------------------------------------------------------
#--------------------------------------------------------------------------FIFO
#------------------------------------------------------------------------------


class FIFO():
    
    def __init__(self,cache_size):
        self.ll = ll(cache_size)
        self.fault_count = 0
    
    def process(self,request):
        self.ll.reset()
        done = False
        while self.ll.get_next():
            self.ll.turn()
            tag = self.ll.get_cur()
            if tag == request:
                done = True
                break
            elif tag == 0:
                self.fault_count += 1
                self.ll.set_cur(request)
                self.ll.mtf()
                done = True
                break
        if not done:
            self.ll.set_cur(request)
            self.ll.mtf()
            self.fault_count += 1
            
    def reset_cache_size(self,n):
        self.__init__(n)

#------------------------------------------------------------------------------
#--------------------------------------------------------------------------LIFO
#------------------------------------------------------------------------------


class LIFO():
    
    def __init__(self,cache_size):
        self.ll = ll(cache_size)
        self.fault_count = 0
    
    def process(self,request):
        self.ll.reset()
        done = False
        while self.ll.get_next():
            self.ll.turn()
            tag = self.ll.get_cur()
            if tag == request:
                done = True
                break
            elif tag == 0:
                self.fault_count += 1
                self.ll.set_cur(request)
                done = True
                break
        if not done:
            self.ll.set_cur(request)
            self.ll.mtf()
            self.fault_count += 1
            
    def reset_cache_size(self,n):
        self.__init__(n)

#------------------------------------------------------------------------------
#---------------------------------------------------------------------------LFU
#------------------------------------------------------------------------------


class LFU():
    
    def __init__(self,cache_size):
        self.count = counter()
        self.fault_count = 0
        self.size = cache_size
    
    def process(self,request):
        if request in self.count:
            self.count[request] += 1
        elif len(self.count) < self.size:
            self.fault_count += 1
            self.count[request] += 1
        else:
            lfu = min(self.count, key = lambda x : self.count[x])
            del self.count[lfu]
            self.count[request] += 1
            self.fault_count += 1
            
    def reset_cache_size(self,n):
        self.__init__(n)

#------------------------------------------------------------------------------
#-------------------------------------------------------------------------CLOCK
#------------------------------------------------------------------------------


#CLOCK requires a circular linked list
class cll():
    
    def __init__(self,cache_size):
        items = [ll_item() for i in range(cache_size)]
        for i in range(cache_size-1):
            items[i].set_next(items[i+1])
            items[i+1].set_prev(items[i])
        items[0].set_prev(items[-1])
        items[-1].set_next(items[0])
        self.current = items[0]
    
    def get_cur(self):
        return self.current.get_tag()
        
    def get_cur_node(self):
        return self.current
    
    def set_cur(self,tag):
        self.current.set_tag(tag)

    def turn(self):
        self.current = self.current.get_next()
    
    def get_next(self):
        return self.current.get_next()
        
        
class CLOCK():
    
    def __init__(self,cache_size):
        self.clock = cll(cache_size)
        self.referenced = cll(cache_size)
        self.size = cache_size
        self.fault_count = 0
    
    def turn(self):
        self.clock.turn()
        self.referenced.turn()
    
    def process(self,request):
        done = False
        cur = self.clock.get_cur_node()
        r = self.referenced.get_cur_node()
        i = 0
        passed = []
        while i < self.size:
            if cur.get_tag() == request:
                r.set_tag(1)
                done = True
                for re in passed:
                    re.set_tag(0)
                break
            elif cur.get_tag() == 0:
                self.fault_count += 1
                r.set_tag(0)
                cur.set_tag(request)
                done = True
                break
            passed.append(r)
            r = r.get_next()
            cur = cur.get_next()
            i += 1
        if not done:
            self.fault_count += 1
            while True:
                if self.referenced.get_cur == 1:
                    self.referenced.set_cur(0)
                    self.turn()
                else:
                    self.clock.set_cur(request)
                    self.referenced.set_cur(0)
                    self.turn()
                    break
                
    def reset_lists(self):
        i = 0
        while i < self.size:
            self.clock.set_cur(0)
            self.referenced.set_cur(0)
            self.turn()
            i += 1
    
    def reset_score(self):
        self.score = 0
    
    def full_reset(self):
        self.reset_lists()
        self.reset_score()
        
    def reset_cache_size(self,n):
        self.__init__(n)

#------------------------------------------------------------------------------
#---------------------------------------------------------------------LFD / OPT
#------------------------------------------------------------------------------


class LFD:
    
    def __init__(self,cache_size):
        self.distance = dict()
        self.size = cache_size
        self.fault_count = 0
        
    def process(self,request_list):
        i = 0
        while i < len(request_list):
            r = request_list[i]
            if r in self.distance:
                if r in request_list[i+1:]:
                    self.distance[r] += request_list[i+1:].index(r)+1
                else:
                    self.distance[r] = float('inf')
            elif len(self.distance) < self.size:
                self.fault_count += 1
                if r in request_list[i+1:]:
                    self.distance[r] = i+1+request_list[i+1:].index(r)
                else:
                    self.distance[r] = float('inf')
            else:
                self.fault_count += 1
                d = max(self.distance, key = lambda x : self.distance[x])
                del self.distance[d]
                if r in request_list[i+1:]:
                    self.distance[r] = i+1+request_list[i+1:].index(r)
                else:
                    self.distance[r] = float('inf')
            i += 1
            
    def reset_cache_size(self,n):
        self.__init__(n)