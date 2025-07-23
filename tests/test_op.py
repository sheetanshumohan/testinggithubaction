from src.math_op import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(2,10)==12
    assert add(-1,-3)==-4
    assert add(0,-2)==-2

def test_sub():
    assert subtract(2,3)==-1
    assert subtract(2,5)==-3
    assert subtract(4,1)==3
    assert subtract(4,2)==2