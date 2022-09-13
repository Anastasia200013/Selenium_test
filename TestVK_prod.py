import pytest

def prod(a, b):
    return a * b

def test_prod():
    res = prod(3, 4)
    assert res == 12

def test_arguments():
    try:
        res = prod("", 4)
    except TypeError as err:
        pass
    else:
        print("Invalid argument is not caught")
        pytest.fail()
        
