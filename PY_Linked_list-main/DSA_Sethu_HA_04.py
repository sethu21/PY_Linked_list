from linkedlist_test_code import LinkedList

new_linked_list = LinkedList()

# Inserting elements
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(45)
new_linked_list.insert_at_end(50)

# Displaying the length and the list
print(f'The length of the list: {new_linked_list.list_length()}')
print("List:")
new_linked_list.output_list()

# Searching for values
print(f'Searching for the value 5: {new_linked_list.unordered_search(5)}')
print(f'Searching for the value 25: {new_linked_list.unordered_search(25)}')

# Removing elements by id
new_linked_list.remove_list_item_by_id(new_linked_list.list_length()-1)
new_linked_list.output_list()
print()
new_linked_list.remove_list_item_by_id(2)
new_linked_list.output_list()
print()
new_linked_list.remove_list_item_by_id(0)
new_linked_list.output_list()

# Sorting the list
new_linked_list.sort()
print("\nSorted List:")
new_linked_list.output_list()

# Creating another linked list for merge and extend operations
other_linked_list = LinkedList()
other_linked_list.insert_at_end(2)
other_linked_list.insert_at_end(7)
other_linked_list.insert_at_end(10)
other_linked_list.insert_at_end(15)

# Merging sorted lists
merged_list = new_linked_list.merge_sorted(other_linked_list)
print("\nMerged List:")
merged_list.output_list()

# Extending the list
new_linked_list.extend(other_linked_list)
print("\nExtended List:")
new_linked_list.output_list()
