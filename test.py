from lab1_1 import *
from lab1_2 import *
from lab2_2 import *

def test_lab1_1():
    assert factorial(9) == 362880
    assert factorial2(9) == 362880

def test_lab1_1():
    assert multiples_of_3_and_5(10) == 23
    assert multiples_of_3_and_5_new(10) ==23

def test_lab2_2():
    orders = ["( a+b-c *[d+e]/{f*(g+h) }", " [ ( a+b-c }*[d+e]/{f*(g+h) }", " ( 3 + 2 ) / { 4**5 }"]
    assert matcher2List(orders) == [False, False, True]
