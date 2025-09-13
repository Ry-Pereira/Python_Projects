from linked_list import *


class ToDoList:
    def __init__(self):
        self.list = LinkedList()

    def add_item(self,item):
        self.list.add(item)

    def remove_item(self,item):
        self.list.remove(item)

    def view_items(self):
        self.list.print()

    def delete_items(self):
        self.list.erase()