import numpy as np

# Base Class
class Character:
    def __init__(self, __name = "", __score = 50):
        self.__name = __name
        self.__score = __score

    def __lt__(self, op2):
        return self.__score < op2.__score
    def __lte__(self, op2):
        return self.__score <= op2.__score
    def __gt__(self, op2):
        return self.__score > op2.__score
    def __gte__(self, op2):
        return self.__score >= op2.__score

class Riddler(Character):
    def __init__(self, __question = ""):
        super().__init__()
        self.__question = __question

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)

class Riddlee(Character):
    def __init__(self, __answer = ""):
        super().__init__()
        self.__answer = __answer

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)

class Hint_Guide(Character):
    def __init__(self, __hint = ""):
        super().__init__()
        self.__hint = __hint

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)

class Node:
    def __init__(self, __quest = None, __left = None, __right = None):
        self.__left = __left
        self.__right = __right
        self.__quest = __quest

    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_left(self, src):
        self.__left = src
    def set_right(self, src):
        self.__right = src

class BST:
    """
        Default Constructor
    """
    def __init__(self, __root = None):
        self.__root = __root

    """
        Insert Into The Binary Search Tree
        < >=
    """
    def insert(self, src):
        if(src == None):
            return False
        return True
        #new_node = Node(__quest = src)
        #return new_node

    def retrieve(self):
        if(self.__root == None):
            return None
        return self.__root

    def display(self):
        pass

    def remove(self, to_remove):
        pass

class Menu:

    def intro(self):
        pass

    def prompt_user(self):
        pass

    def run_program(self):
        pass

    def ask_question(self, BST):
        node = BST.retrieve()
        if(node == None):
            return False
        print(str(node))
        return True

    def prompt_hint(self):
        print("Would You like Hint")

    def ask_hint(self, BST):
        Menu.prompt_hint(self)
        #answer = input()
        # Will deduct From Score If Answered Yes
        node = BST.retrieve()
        if(node == None):
            return False
        print(str(node))
        return True

    def prompt_answer(self):
        print("What Would Be Your Answer?")

    def verify_answer(self, BST):

        Menu.prompt_answer(self)
        node = BST.retrieve()
        #answer = input("Calculating The Result")

        # Will test the user answer from the answer in the node
        if(node == None):
            return False
        return True
    
    def prompt_score(self, correct):
        if(correct):
            print("Correct!!!")
        else:
            print("Incorrect!!!")

    def update_score(self, BST):
        answer = Menu.verify_answer(self, BST)
        Menu.prompt_score(self, answer)
        # Update Score 
        if(answer == False):
            # decrement score
            return False
        # increment score
        return True

    def verify_ending(self):
        pass

    def outro(self):
        pass

if __name__ == "__main__":
    # Run Various Menu System Applications For The User
    print("Hello World!!!")

