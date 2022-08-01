import numpy as np

def add_one(obj):
    return obj + 1

def add_one_to_first(obj):
    obj[0] = obj[0] + 1
    return obj

def add_one_to_input():
    num = input('Enter a number:')
    return add_one(num)