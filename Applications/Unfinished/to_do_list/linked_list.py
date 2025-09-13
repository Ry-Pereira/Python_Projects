from node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def erase(self):
        self.head = None

    def length(self):
        linked_list_length = 0
        if self.head == None:
            return linked_list_length
        else:
            current = self.head
            while(current != None):
                linked_list_length += 1
                current = current.next
            return linked_list_length



    def print(self):
        if self.head == None:
            print("The Linked List is empty")
        else:
            current = self.head
            while(current != None):
                print(current.data)
                current = current.next



    def add(self,data):
        if self.head == None:
            self.head = Node(data)
        
        elif self.head.next == None:
            self.head.next = Node(data)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(data)
        

    def search(self,data):
        if self.head == None:
            return False
        else:
            current = self.head
            while(current != None):
                if current.data == data:
                    return True
                current = current.next
            return False
        
    def updata(self,data_to_edit,data_to_updata):
        if self.head == None:
            print("The list is empty")
        else:
            current = self.head
            while(current != None):
                if current.data == data_to_edit:
                    current.data = data_to_edit
                current = current.next

    
    def remove(self,data):
        if self.head == None:
            print("The list is empty")
            return

        if self.search(data) == False:
            print("Value is not in list")
            return

        else:
            if self.head.data == data:
                self.head = self.head.next
            
            
            else:
                current = self.head
                while(current.next.data != data):
                    current = current.next
                temp = current.next.next
                current.next = temp
                
            

    


        




            





#Checking to see if Linked List works

#Check to see if the Linkedlist is initializing correctly
linked_list = LinkedList()

#Check to see if the Linkedlist is adding nodes correctly
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)


#Check to see if the node data are being printed by the next nodes in descending order, when they were being added
'''print(linked_list.head.data)
print(linked_list.head.next.data)
print(linked_list.head.next.next.data)
print(linked_list.head.next.next.next.data)'''

#Checking to see if the print function works for the class
linked_list.print()


#Checking to see if the length function works for the class
print("Length: ",linked_list.length())

#Checking to see if the erase function workds for the class
#linked_list.erase()
#print("Length: ",linked_list.length())


#Check to see if the search function works for the class
print("The linked list have the value (T/F): ",linked_list.search(0))

#Check to see if the search function works for the class
print("The linked list have the value (T/F): ",linked_list.search(2))



#Check to see if the first value will be removed
linked_list.remove(2)
print("After removing 2")
linked_list.print()
print("Length: ",linked_list.length())

#Check to see if the unapparent value will be removed
linked_list.remove(0)
print("After removing 0")
linked_list.print()
print("Length: ",linked_list.length())

#Check to see if the value will be removed
linked_list.remove(3)
print("After removing 4\n")
linked_list.print()
print("Length: ",linked_list.length())


#Check to see if the last value will be removed
linked_list.remove(5)
print("After removing 5")
linked_list.print()