#Linked List

#To create a node - node_name = node(data)
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    #To print a node - node_name.print_node()   
    def print_node(self):
        print(self.data)

#To create a linked list - name = linked_list()
class linked_list:
    def __init__(self):
        self.head = None

    #To append node - list.append_node(data)
    def append_node(self, data):
        if not self.head:
            self.head = node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node(data)

    #To search for a node - list.search(data)
    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Found it!")
                return True
            
            else:
                current = current.next
        print("Not here.")
        return False
    
    #To print the linked list - list.print_list()      
    def print_list(self):
        node = self. head
        while node is not None:
            print(node.data, end =" ")
            node = node.next
        print("\n")           


