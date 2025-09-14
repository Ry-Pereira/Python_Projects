from todolist import *


class ToDoListExecutive:
    def __init__(self):
        self.to_do_lists = []

    def main_menu(self):
        print("1:Add todo list to todo lists")
        print("2: Delete todo list from todo lists")
        print("3: Edit todo list from todo lists")
        print("4: Print todo list from todo lists")
        print("5: To exit out of program entirely")

    def sub_menu(self):
        print("1:Add item to do list")
        print("2:Remove item from to do list")
        print("3:Update item from to do list")
        print("4: To exit out of sub menu")

    def operation(self):
        self.main_menu()
        user_choice = int(input("User Choice: "))
        while user_choice != 6:
            if user_choice == 1:
                self.add_to_do_list()
            elif user_choice == 2:
                self.delete_to_do_list()

            elif user_choice == 3:
                self.edit_to_do_list()
                
            elif user_choice == 4:
                self.print_to_do_list()
            else:
                print(user_choice,":is not a valid choice")
            user_choice = int(input("User Choice: "))



                
           
    def add_to_do_list(self):
        todolist_name = input("Name for To do list: ")
        self.to_do_lists.append(ToDoList(todolist_name))

    def delete_to_do_list(self):
        todolist_to_remove = input("Name of To do list to remove: ")
        for todolistpos in range(len(self.to_do_lists)):
            if todolist_to_remove == self.to_do_list[todolistpos].name:
                self.to_do_lists.pop(todolistpos)
                


    def print_to_do_list(self):
        todolist_name = input("Name for To do list to be printed: ")
        for todolist in self.to_do_lists:
             if todolist_name == todolist.name:
                todolist.print()

    def edit_to_do_list(self):
        self.sub_menu()
        todolist_to_edit = input("ToDolist to edit")
        user_choice = int(input("User Choice: "))
        for todolist in self.to_do_lists:
            if todolist_to_edit == todolist.name:
                todolist_to_edit = todolist
                        
            while(user_choice != 4):
                if user_choice == 1:
                    pass
                elif user_choice == 2:
                    pass
                elif user_choice == 3:
                    pass
                else:
                    print(user_choice,": is not a valid choice")



    def run(self):
        print("Welcome to the To DO List Program")
        print("Made By Ryan Pereira\n\n")
        self.operation()




