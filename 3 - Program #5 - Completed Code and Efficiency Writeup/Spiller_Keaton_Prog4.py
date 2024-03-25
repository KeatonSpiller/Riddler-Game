# Keaton Spiller 
# CS302
# Program 4/5
# Winter 2024

"""
    Creating a Game of Riddles within a binary Search Tree,
    Correct answer increase the score starting at 50
    Incorrect answers decrease the score
    Win is  > 100
    loss is < 0
    Or End If we run out of prompts
"""

import numpy as np
import pandas as pd
import pyarrow



# Base Class
"""Character Class

Returns:
    Base Class for all Characters
    Holds The Name Of Each Character and Score of Answer, Hint, or Hero
"""
class Character:
    def __init__(self):
        self.__name = ""
        self.__score = 50

    def win(self):
        return self.__score >= 100
    
    def loss(self):
        return self.__score < 0
    
    def beginning(self):
        return  self.__score == 50
    
    def get_score(self):
        return self.__score
    
    def add_to_score(self, amount):
        self.__score = self.__score + amount 

    def subtract_from_score(self, amount):
        self.__score = self.__score - amount

    def copy_constructor(self, character):
        self.__name = character.__name
        self.__score = character.__score

    def prompt_character(self):
        return input("What Is The Name Of Your Adventurer?\n")

    def insert(self, name_toadd, score_toadd):
        self.__name = name_toadd
        self.__score = score_toadd

    def display(self):
        print(f"name:",  self.__name)
        print(f"Score:", self.__score)

    def __lt__(self, op2):
        return np.int64(self.__score) < np.int64(op2.__score)
    def __lte__(self, op2):
        return self.__score <= op2.__score
    def __gt__(self, op2):
        return self.__score > op2.__score
    def __gte__(self, op2):
        return self.__score >= op2.__score
    
"""Riddler

Returns:
    Holds The Questions To Answer
"""
class Riddler(Character):
    def __init__(self, character):
        super().copy_constructor(character)
        self.__question = ""

    def insert(self, my_question):
        self.__question = my_question

    def repeat_question(self):
        print(super().display())
        print(self.__question)

    def give_backstory(self):
        print("I am the wisest Of the Wise, And Listen Close So I can Tell You A Question of The Century")
        print("ZZZZZ, oops did I fall Asleep, ..., well anyways")

    def get_score(self):
        return super().get_score()

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
    
"""Riddlee

Returns:
    Holds the Answers to solve
    Embedded with out Hero
"""
class Riddlee(Character):
    def __init__(self, character):
        super().copy_constructor(character)
        self.__answer = ""

    def display(self):
        print(f"*" * 40)
        print(f"Riddlee")
        super().display()
        print(self.__answer)
        print(f"*" * 40)
    
    def insert(self, correct_answer):
        self.__answer = correct_answer

    def compare_answer(self, user_answer):
        print(self.__answer + " " + user_answer)
        return self.__answer.lower() == user_answer.lower()

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)
    #def __eq__(self, answer):
    #    return self.__answer.lower == (answer)

"""Hint Guide

Returns:
    Hints to Questions
    Decrement the hero's questions when a hint is asked
"""
class Hint_Guide(Character):
    def __init__(self, character):
        super().copy_constructor(character)
        self.__hint = ""

    def insert(self, my_hint):
        self.__hint = my_hint

    def display(self):
        print(f"*" * 40)
        print(f"Hint Guide")
        super().display()
        print(self.__hint)
        print(f"*" * 40)

    def get_score(self):
        return super().get_score()

    def subtract(self, from_score):
        return super().subtract_from_score(from_score)
    
    def add(self, from_score):
        return super().add_to_score(from_score)
    
    def hint_message(self):
        response = input("would you like a hint? 'y' for a hint \n")
        if(response.lower() == 'y'):
            print(self.__hint)
            return True
        else:
            return False

    def __lt__(self, op2):
        return super().__lt__(op2)
    def __lte__(self, op2):
        return super().__lte__(op2)
    def __gt__(self, op2):
        return super().__gt__(op2)
    def __gte__(self, op2):
        return super().__gte__(op2)
    
"""BST Node

Returns:
    Holds the next pointers
    Data of all three characters inside a dictionary {key:value} pair
    __quest = {"riddler": riddler , "riddlee": riddlee, "hint_guide": hint_guide}
"""
class Node:
    def __init__(self):
        self.__left = None
        self.__right = None
        self.__quest = None

    def insert(self, my_quest):
        self.__quest = my_quest

    def copy_node(self, to_copy):
        if(to_copy != None):
            self.__left = to_copy.__left
            self.__right = to_copy.__right
            self.__quest = to_copy.__quest

    def display(self):
        riddler =    self.__quest["riddler"]
        riddlee =    self.__quest["riddlee"]
        hint_guide = self.__quest["hint_guide"]
        riddler.display()
        riddlee.display()
        hint_guide.display()
    
    def ask_question(self):
        riddler =    self.__quest["riddler"]
        riddler.repeat_question()

    def ask_hint(self):
        hint_guide =    self.__quest["hint_guide"]
        return hint_guide.hint_message()
    
    def update_hint(self, my_character):
        hint_guide =    self.__quest["hint_guide"]
        my_character.subtract_from_score(hint_guide.get_score())

    def riddler_score(self):
        riddler =    self.__quest["riddler"]
        return riddler.get_score()
        
    def compare_previous(self, my_character):
        previous_score = self.__quest["riddler"]
        return my_character.get_score() < previous_score.get_score()

    # __lt__(self, op2)
    # compare The Scores of Riddle Question's In The Tree
    def question_score_less_than(self, to_compare):
        if(to_compare != None and self.__quest != None):
            # my_hero =    self.__quest["riddlee"]
            # other_score = to_compare.__quest["riddlee"]
            in_tree =    self.__quest["riddler"]
            other_score = to_compare.__quest["riddler"]
            return other_score.__lt__(in_tree)
        else:
            return False

    def answer_equals(self, user_answer):
        if(user_answer != None and self.__quest != None):
            my_hero =    self.__quest["riddlee"]
            return my_hero.compare_answer(user_answer)
        return False

    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_left(self, src):
        self.__left = src
    def set_right(self, src):
        self.__right = src

"""BST

Returns:
    Holds the Root of BST
    Traverses the Tree, and handles the navigation amoungst the nodes
"""
class BST:
    """
        Default Constructor
    """
    def __init__(self):
        self.__root = None

    """
        Insert Into The Binary Search Tree
        < >=
    """
    def insert_wrapper(self, to_add):
        if(to_add == None):
            return 0
        if(self.__root == None):
            self.__root = Node()
            self.__root.copy_node(to_add)
            return 1
        return self.insert_recursion(self.__root, to_add)

    def insert_recursion(self, src, to_add):
        if(src == None):
            src = Node()
            src.copy_node(to_add)
            return src

        smaller = src.question_score_less_than(to_add)

        #print(f"Comparison: {smaller}")

        if(smaller):
            #print("Smaller")
            src.set_left(self.insert_recursion(src.get_left(), to_add))
        else:
            #print("Larger")
            src.set_right(self.insert_recursion(src.get_right(), to_add))
        return src
    
    def retrieve(self, my_hero, previous):
        if(my_hero == None):
            return 0
        compare = my_hero.beginning()
        if(compare):
            return self.__root
        else:
            return self.retrieve_cmp(my_hero, previous)

    def retrieve_cmp(self, my_hero, previous):
        comparison = previous.compare_previous(my_hero)
        if(comparison):
            return previous.get_left()
        else:
            return previous.get_right()

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
    
    def load_game(self, my_character):

        # Riddler_Name Riddler_Score Riddler_Question Answer Hint_Guide_Name Hint_Score Hint
        data = pd.read_csv(filepath_or_buffer="./character_data.csv", engine= "pyarrow", header=0)
        riddler_name_col = data["Riddler_Name"]
        riddler_score_col = data["Riddler_Score"]
        riddler_question_col = data["Riddler_Question"]
        answer_col = data["Answer"]
        hint_guide_name_col = data["Hint_Guide_Name"]
        hint_score_col = data["Hint_Score"]
        hint_col = data["Hint"]

        # Read All Characters and Prompts Into The Tree
        for row in range(0, answer_col.size):

            my_riddler = Character()
            my_riddler.insert(riddler_name_col.iloc[row], riddler_score_col.iloc[row])

            my_hint_guide = Character()
            my_hint_guide.insert(hint_guide_name_col.iloc[row], hint_score_col.iloc[row])

            question = Riddler(my_riddler)
            question.insert(riddler_question_col.iloc[row])

            answer = Riddlee(my_character)
            answer.insert(answer_col.iloc[row])

            hint = Hint_Guide(my_hint_guide)
            hint.insert(hint_col.iloc[row])

            quest = {"riddler":question, "riddlee":answer, "hint_guide":hint}

            myNode = Node()
            myNode.insert(quest)

            self.insert_wrapper(myNode)

    def IOS(self, src):
        if(src == None or src.get_left() == None):
            return None
        if(src.get_left().get_left() == None):
            ios = src.get_left()
            right_child = ios.get_right()
            src.set_left(right_child)
            return ios
        return self.IOS(src.get_left())

    def insert_tree(self, src):
        if(src == None):
            return
        self.insert_tree(src.get_left())
        self.insert_wrapper(src)
        self.insert_tree(src.get_right())
        return 
    
    def remove_all(self):
        self.__root = None

    def remove_wrapper(self, answer):
        if(answer == None):
            return 
        return self.remove(self.__root, answer)

    def remove(self, src, answer):
        if(src == None):
            return 0
        if(src.answer_equals(answer)):
            print ("Do I Enter Here?")
            hold_left = src.get_left()
            hold_right = src.get_right()
            if(hold_left):
                if(hold_left.get_left()):
                    print("IOS 2 Nodes")
                    replace = self.IOS(self.__root.get_right())
                else:
                    print("IOS 1 Node")
                    src.set_left(None)
                    replace = hold_left
                src.copy_node(replace)
                if(hold_right != None):
                    self.insert_tree(hold_right)
            else:
                print("No left Node")
                src.set_right(None)
                src.copy_node(hold_right)
            return src
        self.remove(src.get_left(), answer)
        self.remove(src.get_right(), answer)
        return src
    
"""Handles The User Interface Application 

Returns:
    Runs The Game For the user Handling calls from main
"""
class Menu:

    def intro(self):
        print("Hi there!! Welcome To The Program!")

    def prompt_user(self):
        print(f"*" * 40)
        print("What Would you Like To Do")
        print("1 Play The Game | 2 Insert Node | 3 Retrieve Node")
        print("4 Display All   | 5 Remove Node | 6 Remove All")
        print("0 to quit")
        print(f"*" * 40)
        return int(input())

    def run_program(self):
        # Steps 1-6 of UML Design
        t = BST()
        my_character = Character()
        character_name = my_character.prompt_character()
        my_character.insert(character_name, 50)

        t.load_game(my_character)
        self.run_options(t, my_character)
        
    def run_options(self, t, my_character):
        choice = 1
        while(choice != 0):
            choice = self.prompt_user()
            match int(choice): # python's break is built into switch statement ( required version >= 3.10 )
                case 1: # 1 Play The Game
                    self.play_game(t, my_character)
                case 2: # 2 Insert Node
                    entry = self.create_entry(my_character)
                    t.insert_wrapper(entry)
                case 3: # 3 Retrieve Node
                    print()
                case 4: # 4 Display All
                    count = t.display_wrapper()
                    print(f"Number of Nodes Displayed From The Tree: {count}")
                case 5: # 5 Remove Node
                    answer = str(input("Which Answer Would You Like To Remove?\n"))
                    t.remove_wrapper(answer)
                    print()
                case 6: # 6 Remove All
                    t.remove_all()

    def play_game(self, t, my_character):
        # While
        # 1. Not Win / loss
        # 2. Tree available
        # compare question to answer

        # read from the tree
        entry = t.retrieve(my_character, None)
        # while entry to play
        while(entry != None):

            entry.ask_question()
            hint_wanted = entry.ask_hint()
            if(hint_wanted):
                entry.update_hint(my_character)
            user_answer = input("What Is Your Answer:")
            correct = entry.answer_equals(user_answer) # __answer == user_answer
            self.update_score(my_character, correct, entry)
            self.prompt_score(correct, my_character.get_score())
            end = self.verify_ending(my_character)
            if(end):
                return
            # read from the tree
            entry = t.retrieve(my_character, entry)
        print("We Ran Out Of Riddles In Our Adventure!!")
        return


    """
        Insert Entry
        Fill virtul Character Object of
        Riddlee, Riddler, Hint Guide
    """
    def create_entry(self, my_character):
        # Riddler_Name Riddler_Score Riddler_Question Answer Hint_Guide_Name Hint_Score Hint
        my_riddler = Character()
        riddler_name = input("What Is The Riddler Name?\n")
        riddler_score = int(input("What Is The Riddler Score?\n"))
        my_riddler.insert(riddler_name, riddler_score)

        hint_guide_name = input("What Is The Hint Guide Name?\n")
        hint_guide_score = int(input("What Is The Hint Guide Score?\n"))
        my_hint_guide = Character()
        my_hint_guide.insert(hint_guide_name, hint_guide_score)

        riddler_question = input("What Riddle Question?\n")
        question = Riddler(my_riddler)
        question.insert(riddler_question)

        ridlee_answer = input("What Riddle Answer?\n")
        answer = Riddlee(my_character)
        answer.insert(ridlee_answer)

        hint_response = input("What Is The Hint?\n")
        hint = Hint_Guide(my_hint_guide)
        hint.insert(hint_response)

        quest = {"riddler":question, "riddlee":answer, "hint_guide":hint}

        myNode = Node()
        myNode.insert(quest)

        return myNode

    """
        if > 100 win
        if < 0 loss
        if ran out of tree loss
    """
    def verify_ending(self, my_character):
        # Check If Won The Game
        win = my_character.win()
        loss = my_character.loss()
        if(win):
            print("You've Won the Game!!!")
        if(loss):
            print("You've Lost the Game!, Good Try")
        return win or loss
    
    def prompt_score(self, correct, score):
        if(correct):
            print("Correct!!!")
            print(f"Your Updated Score Is {score}!!")
        else:
            print("Incorrect, I know you'll get it next time!!")
            print(f"Your Updated Score Is {score}!!")

    def update_score(self, my_character, correct, entry):
        prize = entry.riddler_score()
        # update score
        if(correct):
            # add to score
            my_character.add_to_score(prize)
        else:
            my_character.subtract_from_score(prize)

    def outro(self):
        print("Thank You For Playing, have a Great Day!!!")

if __name__ == "__main__":
    # Run Various Menu System Applications For The User
    menu = Menu()
    menu.intro()
    menu.run_program()
    menu.outro()

