#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:53:23 2021

@author: hbc
"""
from collections import deque

class LRUCache:

    # intilialize the size, dictionary and the deque
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = dict()
        self.que = deque()

    def get(self, key: int) -> int:
        # if not in the map, return -1
        if key not in self.map:
            return -1
        # if it is in the map, then first remove it then append it 
        # and return its value
        else:
            self.que.remove(key)
            self.que.append(key)
            return self.map[key]

    def put(self, key: int, value: int) -> None:
        # if not in the map, add it
        if key not in self.map:
            # however, if the capacity is full, then find the leftmost key and delete it
            if len(self.que) >= self.cap:
                oldest = self.que.popleft()
                del self.map[oldest]
            self.map[key] = value
            self.que.append(key)
        # if it is in the map, then first remove it, update the value, and then append it
        else:
            self.que.remove(key)
            self.map[key] = value
            self.que.append(key)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
    
s = LRUCache(3)

s.put(1, 1000)
s.put(2, 2000)
s.put(3, 3000)
print(s.get(1))
s.put(4, 4000)
print(s.get(2))
