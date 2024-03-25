import pytest
from Spiller_Keaton_Prog4 import *

# Mock The BST
@pytest.fixture
def setup_BST():
    return BST()

# Mock The Valid Node
@pytest.fixture
def setup_valid_Node():
    my_character = Character("Fearless Adventurer", 50)
    my_riddler = Character("Gurtrude The Wise", 10)
    my_hint_guide = Character("Samwise Gamgee", 5)

    question = Riddler(my_riddler, "What Is The Question To The Question?")
    answer = Riddlee(my_character, "??")
    hint = Hint_Guide(my_hint_guide, "Could It be two Question Marks?")

    quest = {"riddler":question, "riddlee":answer, "hint_guide":hint}

    valid_node = Node(quest)
    return Node(valid_node)

# Mock The Menu
@pytest.fixture
def setup_Menu():
    return Menu()