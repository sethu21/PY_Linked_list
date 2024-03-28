# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:11:15 2024

@author: s22sethselv
"""
class ListNode:
    
    def __init__(self, data, next=None):
        self.data = data
        
        self.next = None
class SingleLinkedList:
    
    def __init__(self):
        
        self.head = None 
        self.tail = None
        
    def insert_at_end(self, item):
        
        if not isinstance(item, ListNode):
            item = ListNode(item)
            
        if self.head is None :
            self.head = item
        else:
            self.tail.next = item
            
        self.tail = item
        
    def list_length(self):
        
        count =0
        current_node =self.head 
        
        while current_node is not None:
            
            count = count +1
            
            current_node = current_node.next
        return count
    
    def output_list(self):
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            
            current_node = current_node.next