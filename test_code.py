from code import adder

def test01():
    TEST_VALUES:list = [10, 20, 30]
    EXPECTED_VALUE:float = 60.0

    b_OK:bool = adder(TEST_VALUES) == EXPECTED_VALUE

    assert(b_OK)
# def test01