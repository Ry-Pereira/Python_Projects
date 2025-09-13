from linked_list import *


class ToDoList:
    def __init__(self):
        self.to_do_lists = []

    def main_menu(self):
        print("1:Add todo list to todo lists")
        print("2: Delete todo list from todo lists")
        print("3: Edit todo list from todo lists")
        print("4: Print todo list from todo lists")
        print("5: Print todo list length from todo lists")

    def sub_menu(self):
        print("1:Add item to do list")
        print("2:Remove item from to do list")
        print("3:Search item from to do list")
        print("4:Update item from to do list")


    def add_item(self,item):
        self.list.add(item)

    def remove_item(self,item):
        self.list.remove(item)

    def view_items(self):
        self.list.print()

    def delete_items(self):
        self.list.erase()


    def run():
        print("Welcome to the To DO List Program")
        print("Made By Ryan Pereira\n\n")


