# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:07:51 2024

@author: s22sethselv
"""

from Single_Linked_list import ListNode , SingleLinkedList



new_linked_list = SingleLinkedList()

new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(45)
new_linked_list.insert_at_end(50)


print(f'The length of the list:{new_linked_list.list_length()}')
print("List:")
new_linked_list.output_list()