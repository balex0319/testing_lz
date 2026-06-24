import pytest
from tests import log

if log(1,10,6) == 2:
    print('True')
else:
    print('False')

if log(0.1,2,2) < 0:
    print('true')
else:
    print('false')    

if log(5, 5, 2) == 1:
    print('true')
else:
    print('false')

if log(1, 5, 2) == 0:
    print('true')
else:
    print('false')

if log(0,0,1) == True:
    print('true')
else:
    print('false')


def test_1():
    assert log(1, 10, 6) == 2

def test_2():
    assert log(0.1, 2, 2) < 0

def test_3():
    assert log(0, 0, 1) == True

def test_4():
    assert log(5, 5, 1) == 1

def test_5():
    assert log(1, 5, 1) == 0  
