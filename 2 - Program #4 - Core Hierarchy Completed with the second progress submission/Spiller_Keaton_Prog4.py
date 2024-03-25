import numpy as np

# Base Class
class Character:
    def __init__(self, __name = "", __score = 50):
        self.__name = __name
        self.__score = __score

    def copy_constructor(self, character):
        self.__name = character.__name
        self.__score = character.__score

    def display(self):
        print(f"name:",  self.__name)
        print(f"Score:", self.__score)

    def __lt__(self, op2):
        return self.__score < op2.__score
    def __lte__(self, op2):
        return self.__score <= op2.__score
    def __gt__(self, op2):
        return self.__score > op2.__score
    def __gte__(self, op2):
        return self.__score >= op2.__score

class Riddler(Character):
    def __init__(self, character, __question = ""):
        super().copy_constructor(character)
        self.__question = __question

    def repeat_question(self):
        print(self.__question)

    def give_backstory(self):
        print("I am the wisest Of the Wise, And Listen Close So I can Tell You A Question of The Century")
        print("ZZZZZ, oops did I fall Asleep, ..., well anyways")

    def statistics(self):
        print("Give question frequency analysis")

    def display(self):
        print(f"*" * 40)
        print(f"Riddler")
        super().display()
        print(f"What Is The Answer To The Question")
        print(self.__question)
        print(f"*" * 40)

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)

class Riddlee(Character):
    def __init__(self, character, __answer = ""):
        super().copy_constructor(character)
        self.__answer = __answer

    def display(self):
        print(f"*" * 40)
        print(f"Riddlee")
        super().display()
        print(self.__answer)
        print(f"*" * 40)
    
    def compare_answer(self, user_answer):
        return self.__answer.lower().replace(" ", "") == user_answer.lower.replace(" ", "")
    
    def win(self):
        return super().__score >= 100
    
    def loss(self):
        return super().__score < 0

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)

class Hint_Guide(Character):
    def __init__(self, character, __hint = ""):
        super().copy_constructor(character)
        self.__hint = __hint

    def display(self):
        print(f"*" * 40)
        print(f"Hint Guide")
        super().display()
        print(self.__hint)
        print(f"*" * 40)

    def subtract(self, from_score):
        return from_score - super().__score
    
    def add(self, from_score):
        return from_score + super().__score
    
    def hint_message(self):
        print("Try Again, You Can Do It!!")

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

    def copy_constructor(self):
        self.__left = self.__left
        self.__right = self.__right
        self.__quest = self.__quest

    def display(self):
        riddler =    self.__quest["riddler"]
        riddlee =    self.__quest["riddlee"]
        hint_guide = self.__quest["hint_guide"]
        riddler.display()
        riddlee.display()
        hint_guide.display()

    # __lt__(self, op2)
    def less_than(self, to_compare):
        if(to_compare != None and self.__quest != None):
            my_hero =    self.__quest["riddlee"]
            other_score = to_compare.__quest["riddlee"]
            return my_hero.__lt__(other_score)
        else:
            return -1

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
    def insert_wrapper(self, to_add):
        if(to_add == None):
            return None
        if(self.__root == None):
            self.__root = to_add
            return to_add
        return self.insert_recursion(self.__root, to_add)

    def insert_recursion(self, src, to_add):
        if(src == None):
            temp = Node.copy_constructor(to_add)
            src = temp
            return src

        smaller = src.less_than(to_add)

        print(f"Comparison: {smaller}")

        if(smaller):
            print("Smaller")
            src.set_left(self.insert_recursion(src.get_left(), to_add))
        else:
            print("Larger")
            src.set_right(self.insert_recursion(src.get_right(), to_add))
        return src

    def retrieve(self):
        if(self.__root == None):
            return None
        return self.__root

    def display_wrapper(self):
        if(self.__root == None):
            return 0
        return self.display_recursion(self.__root)

    # Display In Order Traversal
    def display_recursion(self, src):
        if(src == None):
            return 0
        left = self.display_recursion(src.get_left())
        src.display()
        right = self.display_recursion(src.get_right())
        return 1 + left + right
    
    def load_game(self):
        pass

    def remove(self, to_remove):
        pass

class Menu:

    def intro(self):
        print("Hi there!! Welcome To The Program!")

    def prompt_user(self):
        print(f"*" * 40)
        print("What Would you Like To Do")
        print("1 Play The Game | 2 Insert Node | 3 Retrieve Node")
        print("4 Display All   | 5 Remove Node | 6 Remove All")
        print(f"*" * 40)

    def run_program(self):
        tree = BST()
        # Steps 1-6 of UML Design
        self.intro()
        tree.load_game()
        self.outro()

    def ask_question(self, BST):
        node = BST.retrieve()
        if(node == None):
            return False
        #node.display()
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
        node.display()
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
    
    def prompt_score(self, correct, score):
        if(correct):
            print("Correct!!!")
            print("Your Updated Score Is!!")
        else:
            print("Incorrect, I know you'll get it next time!!")
            print("Your Updated Score Is!!")

    def update_score(self, BST):
        answer = Menu.verify_answer(self, BST)
        Menu.prompt_score(self, answer, 50)
        # Update Score 
        if(answer == False):
            # decrement score
            return False
        # increment score
        return True

    def verify_ending(self):
        pass

    def outro(self):
        print("Thank You For Playing, have a Great Day!!!")

if __name__ == "__main__":
    # Run Various Menu System Applications For The User
    # Replace The Tests in this section with run_program()
    # menu = Menu()
    # menu.run_program()

    t = BST()

    my_character = Character("Fearless Adventurer", 50)
    my_riddler = Character("Gurtrude The Wise", 10)
    my_hint_guide = Character("Samwise Gamgee", 5)

    question = Riddler(my_riddler, "What Is The Question To The Question?")
    answer = Riddlee(my_character, "??")
    hint = Hint_Guide(my_hint_guide, "Could It be two Question Marks?")

    #question.display()
    #answer.display()
    #hint.display()

    quest = {"riddler":question, "riddlee":answer, "hint_guide":hint}

    myNode = Node(quest)
    myNode2 = Node(quest)
    t.insert_wrapper(myNode)
    t.insert_wrapper(myNode2)

    count = t.display_wrapper()

    print(f"Number of Nodes Displayed From The Tree: {count}")
