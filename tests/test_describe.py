import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mocks.mock_tree import ok_button
from semantics.describe import describe

def test_ok_button(): 
    assert describe(ok_button()) == "OK, Schaltfläche" 