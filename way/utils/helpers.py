""" various helper functions """

from random import choice

def generate_hexcode():
    length = 6
    chars = 'abcdef0123456789'
    
    code = ''.join((choice(chars)) for _ in range(length))
    return code