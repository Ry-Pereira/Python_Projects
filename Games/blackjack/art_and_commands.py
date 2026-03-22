welcome_text = "dsds"



card_deck = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10":10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": ace(choice = int(input("Choose from 11 or 1: ")))


def ace(choice):
    if choice == 11:
        return (1)
    elif choice == 11:
        return (11):
    else:
        print("Try a valid option")
        ace(choice = int(input("Choose from 11 or 1: ")))
        
