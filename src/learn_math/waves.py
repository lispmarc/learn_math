import math 

def generate(wave_length,wave_phase):
    def result(x):
        return math.cos(2*math.pi/wave_length*x+wave_phase)
    return result 

def add(wave1,wave2):
    def result(x):
        return wave1(x)+wave2(x)
    return result
    