# Import the add function so the test can use it
from calculator import add,divide
import pytest

def test_add():
   # Check that it adds two positive integers
   assert add(1, 2) == 3

   # Check that it adds zero
   assert add(5, 0) == 5

   # Check that it adds two negative integers
   assert add(-1, -2) == -3

def test_divide():	
	with pytest.raises(ZeroDivisionError):
		divide(1,0)
def test_subtract():
    assert subtract(5, 3) == 2

