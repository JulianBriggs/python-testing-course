from advanced_calculator import power, is_prime
import pytest

def test_power():
    """Test for the power function"""
    assert power(2, 3) == 8
    assert power(3, 3) == 27



@pytest.mark.parametrize('n,expected',
[
pytest.param(2,True),
pytest.param(3,True),
pytest.param(4,False),
]
)
def test_is_prime(n,expected):
	assert is_prime(n) == expected
	
	