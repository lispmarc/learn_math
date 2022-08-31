from lib2to3.pgen2.pgen import generate_grammar
from learn_math import waves 
import math 

def test_1():
    w1=waves.generate(math.pi,0)
    assert(w1(0)==1)

def test_2():
    w1=waves.generate(math.pi,math.pi)
    w2=waves.generate(math.pi/2,0)
    w=waves.add(w1,w2)
    assert(w(1)==w1(1)+w2(2))  # Causes test to fail
        