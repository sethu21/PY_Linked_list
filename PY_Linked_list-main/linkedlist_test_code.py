class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def unordered_search(self, value, start=0):
        current_node = self.head
        node_id = start
        results = []
        while current_node is not None:
            if current_node.data == value:
                results.append(node_id)
            current_node = current_node.next
            node_id += 1
        return results

    def remove_list_item_by_id(self, item_id):
        current_id = 0
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                    if current_node.next is None:
                        self.tail = previous_node
                else:
                    self.head = current_node.next
            previous_node = current_node
            current_node = current_node.next
            current_id += 1

    def insert_at_start(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_after_item(self, x, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                break
            current_node = current_node.next
        if current_node is not None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def insert_before_item(self, x, data):
        if x == self.head.data:
            self.insert_at_start(data)
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == x:
                break
            current_node = current_node.next
        if current_node.next is not None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return
        i = 0
        current_node = self.head
        while i < index - 1 and current_node is not None:
            current_node = current_node.next
            i += 1
        if current_node is not None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def remove_at_start(self):
        if self.head is not None:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next

    def remove_at_end(self):
        if self.head is not None:
            current_node = self.head
            previous_node = None
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            if previous_node is not None:
                previous_node.next = None
                self.tail = previous_node
            else:
                self.head = None
                self.tail = None

    def delete_element_by_value(self, x):
        if self.head is not None:
            if self.head.data == x:
                if self.head == self.tail:
                    self.tail = None
                self.head = self.head.next
                return
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == x:
                    if current_node.next == self.tail:
                        self.tail = current_node
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next

    def sort(self):
        if self.head is None:
            return
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(current_node.data)
            current_node = current_node.next
        values.sort()
        self.head = ListNode(values[0])
        self.tail = self.head
        for value in values[1:]:
            self.insert_at_end(value)

    def merge_sorted(self, other_list):
        current_node_self = self.head
        current_node_other = other_list.head
        merged_list = LinkedList()
        while current_node_self is not None and current_node_other is not None:
            if current_node_self.data < current_node_other.data:
                merged_list.insert_at_end(current_node_self.data)
                current_node_self = current_node_self.next
            else:
                merged_list.insert_at_end(current_node_other.data)
                current_node_other = current_node_other.next
        while current_node_self is not None:
            merged_list.insert_at_end(current_node_self.data)
            current_node_self = current_node_self.next
        while current_node_other is not None:
            merged_list.insert_at_end(current_node_other.data)
            current_node_other = current_node_other.next
        return merged_list

    def extend(self, other_list):
        current_node = other_list.head
        while current_node is not None:
            self.insert_at_end(current_node.data)
            current_node = current_node.next


