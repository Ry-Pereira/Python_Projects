welcome_text =('''
..######.....###....##........######..##.....##.##..........###....########..#######..########.
.##....##...##.##...##.......##....##.##.....##.##.........##.##......##....##.....##.##.....##
.##........##...##..##.......##.......##.....##.##........##...##.....##....##.....##.##.....##
.##.......##.....##.##.......##.......##.....##.##.......##.....##....##....##.....##.########.
.##.......#########.##.......##.......##.....##.##.......#########....##....##.....##.##...##..
.##....##.##.....##.##.......##....##.##.....##.##.......##.....##....##....##.....##.##....##.
..######..##.....##.########..######...#######..########.##.....##....##.....#######..##.....##
                                                                                               
                                                                                               
                                                                                  
                                                                                                           ''')
caluclator_commands = {
    "+": add(first_val,second_val),
    "-": subtract(first_val,second_val),
    "*": multiply((first_val,second_val),
    "/": divide((first_val,second_val),
    "**": power((first_val,second_val),
    "//": long_divide(first_val,second_val),
    "%": remainder(first_val,second_val)
                }



def add(first_val,second_val):
    return first_val + second_val

def subtract(first_val,second_val):
    return first_val - second_val

def multiply(first_val,second_val):
    return first_val * second_val

def divide(first_val,second_val):
    return first_val / second_val

def power(first_val,second_val):
    return first_val ** second_val

def long_divide(first_val,second_val):
    return first_val // second_val

def remainder(first_val,second_val):
    return first_val % second_val



                
