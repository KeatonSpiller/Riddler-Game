import pytest
from Spiller_Keaton_Prog4 import *

# Mock The Class
@pytest.fixture
def setup_BST():
    return BST()

# Mock The Class
@pytest.fixture
def setup_Menu():
    return Menu()