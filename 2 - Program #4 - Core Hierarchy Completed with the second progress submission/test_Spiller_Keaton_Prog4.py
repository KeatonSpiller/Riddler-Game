from conftest import *

"""
    Note:
        Future: Replace exception handling inside the test
        (try, catch) to be handled by main code
        Instead 
            Check if the exception was raised "with raises"
        - look into paramaterized tests
        - Began setup_valid_Node as first parameterized test, very sleek, and reduces duplication of code
"""


# 0. Insert Into The Tree To Start The Game
def test_insert_None(setup_BST):
    invalid_node = None
    result = setup_BST.insert_wrapper(invalid_node)
    try:
        assert result == None
    except:
        pytest.fail(f"None node incorrectly added to the Tree")

# 0. Insert Into The Tree To Start The Game
def test_insert_Root(setup_BST, setup_valid_Node):
    result = setup_BST.insert_wrapper(setup_valid_Node)
    try:
        assert result != None
    except:
        pytest.fail(f"None node incorrectly added to the Tree")

"""
# 0. Insert Into The Tree To Start The Game
def test_insert_multiple(setup_BST, setup_valid_Node):
    result = setup_BST.insert_wrapper(setup_valid_Node)
    result2 = setup_BST.insert_wrapper(setup_valid_Node)
    try:
        assert result2 != None
    except:
        pytest.fail(f"None node incorrectly added to the Tree")
"""

# 1. Read Question From The Tree Based On Score
# Will choose based on score comparison from Tree
def test_retrieve_invalid(setup_BST):
    setup_BST.__root = None

    result = setup_BST.retrieve()
    try:
        assert result == None
    except:
        pytest.fail(f"Attempted To Retrieve From An Empty Root")

# 1. Read Question From The Tree Based On Score
# Will choose based on score comparison from Tree
def test_retrieve_valid(setup_BST, setup_valid_Node):

    setup_BST.__init__(setup_valid_Node)
    result = setup_BST.retrieve()
    try:
        assert result != None
    except:
        pytest.fail(f"Failed To Retrieve From A Valid Tree")

# 2. Read Question From Tree Based On Score
# calls Retrieve to Retrieve Question
# Riddler Asks Question
def test_ask_question_invalid(setup_Menu, setup_BST):

    setup_BST.__root = None

    result = setup_Menu.ask_question(setup_BST)

    try:
        assert result == False
    except:
        pytest.fail(f"Unable To Ask Question")

# 2. Read Question From Tree Based On Score
# calls Retrieve to Retrieve Question
# Riddler Asks Question
def test_ask_question_valid(setup_Menu, setup_BST, setup_valid_Node):

    setup_BST.__init__(setup_valid_Node)
    result = setup_Menu.ask_question(setup_BST)

    try:
        assert result == True
    except:
        pytest.fail(f"Unable To Ask Question")


# 3. Option To Ask For Hint
# Ask For Hint From hint Guide
def test_ask_hint_valid(setup_Menu, setup_BST, setup_valid_Node):

    setup_BST.__init__(setup_valid_Node)

    result = setup_Menu.ask_hint(setup_BST)

    try:
        assert result == True
    except:
        pytest.fail(f"Unable To Ask Question")

# 3. Option To Ask For Hint
# Ask For Hint From hint Guide
def test_ask_hint_valid(setup_Menu, setup_BST):

    setup_BST.__init__(None)

    result = setup_Menu.ask_hint(setup_BST)

    #answer = "yes"
    # Take A Different approach if input answer one way or another

    try:
        assert result == False
    except:
        pytest.fail(f"Unable To Ask Question")


# 4. The User Answers What Is Their Response to The Riddle
# Ask For Hint From hint Guide
def test_verify_answer_valid(setup_Menu, setup_BST, setup_valid_Node):

    Menu.prompt_answer(setup_Menu)

    # Will Take In the User's Answer And compare to The actual Answer
    setup_BST.__init__(setup_valid_Node)

    result = setup_Menu.verify_answer(setup_BST)

    try:
        assert result == True
    except:
        pytest.fail(f"Unable To Verify valid Answer")

# 4. The User Answers What Is Their Response to The Riddle
# Ask For Hint From hint Guide
def test_verify_answer_invalid(setup_Menu, setup_BST):

    Menu.prompt_answer(setup_Menu)

    # Will Take In the User's Answer And compare to The actual Answer

    setup_BST.__init__(None)

    result = setup_Menu.verify_answer(setup_BST)

    try:
        assert result == False
    except:
        pytest.fail(f"Unable To Verify invalid Answer")


# 5. The User Answers What Is Their Response to The Riddle
# Ask For Hint From hint Guide
def test_update_score_valid(setup_Menu, setup_BST, setup_valid_Node):

    setup_BST.__init__(setup_valid_Node)

    answer = setup_Menu.verify_answer(setup_BST)
    setup_Menu.prompt_score(answer, 50)

    result = setup_Menu.update_score(setup_BST)

    try:
        assert result == True
    except:
        pytest.fail(f"Unable To Update Valid Score")

# 5. The User Answers What Is Their Response to The Riddle
# Ask For Hint From hint Guide
def test_update_score_invalid(setup_Menu, setup_BST):

    setup_BST.__init__(None)

    answer = setup_Menu.verify_answer(setup_BST)
    setup_Menu.prompt_score(answer, 50)

    result = setup_Menu.update_score(setup_BST)

    try:
        assert result == False
    except:
        pytest.fail(f"Unable To Update Invalid Score")

# 6
# a.
# if out character is > 100 End Win
def test_verify_ending_win(setup_Menu, setup_BST):

    setup_Menu.verify_ending()

    # Read In Score
    score = 100

    try:
        assert score > 100
    except:
        pytest.fail(f"Unable To validate winning score")

# 6
# b. 
# if out character is <= 0 End Loss
def test_verify_ending_win(setup_Menu, setup_BST):

    setup_Menu.verify_ending()

    score = 0

    try:
        assert score <= 1
    except:
        pytest.fail(f"Unable To validate Losing score")

# 6
# c.
# if We Are Out Of Prompts End Game Draw
def test_verify_ending_win(setup_Menu, setup_BST):

    setup_Menu.verify_ending()

    node = None

    try:
        assert node == None
    except:
        pytest.fail(f"Unable To validate Running Out of Prompts")

if __name__ == "__main__":
    pytest.main()
