
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
    
    #inserts at head (creating a new head)
    def insert_at_beginning(self, data):
        node_instance = Node(data, self.head)
        self.head = node_instance
    
    #loops until the last node then sets the last node's next to a new node.
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data, None)
    
    #goes to index b4 specified, and adds node.
    def insert_at(self, index, data):
        if index < 0 or index > len(self):
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        i = self.head
        while i:
            if count == (index - 1):
                node_instance = Node(data, i.next)
                i.next = node_instance
                break
            i = i.next
            count += 1
    
    #look for value specified, then insert Node after it
    def insert_after_value(self, value_after, data):
        i = self.head
        while i:
            if i.data == value_after:
                node_instance = Node(data, i.next)
                i.next = node_instance
                break
            i = i.next

    #takes list of values, and inserts at end of list
    def insert_values(self, list_of_vals):
        i = self.head
        while i.next:
            i = i.next
        for val in list_of_vals:
            self.insert_at_end(val)
    
    #updates pointer from node before index to node after index.
    def remove_index(self, index):
        if index < 0 or index > len(self):
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        i = self.head
        while i:
            if count == (index - 1):
                i.next = i.next.next
                break
            i = i.next
            count += 1

    #loops through the nodes checking for the next nodes value.
    def remove_by_value(self, data):
        i = self.head
        while i:
            if i.next.data == data:
                i.next = i.next.next
                break
            i = i.next

    def __len__(self):
        count = 0
        i = self.head
        while i:
            count += 1
            i = i.next
        return count

    def __repr__(self):
        if self.head is None:
            print("list is empty")
            return
        linked_list_str_rep = ''
        i = self.head           #i is representing the current node here.
        while i:
            linked_list_str_rep += str(i.data) + ' -> '
            i = i.next
        return linked_list_str_rep


if __name__ == '__main__':
    print("running program...")
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(4)
    ll.insert_values(["mango", "banana", "apricot", "grape"])
    ll.remove_index(3)
    ll.insert_at(4, 99)
    ll.insert_after_value("mango", 777)
    ll.remove_by_value(99)
    print(repr(ll))
    print("len: " + str(len(ll)))

