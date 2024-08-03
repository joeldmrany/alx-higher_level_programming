#!/usr/bin/python3
"""
Remember
Don't forget your feedback
I hope you find the code will
"""


def text_indentation(text):
    """
    text_indentation function you can see what it do
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i in range(len(text)):
        if text[i] in ".?:":
            print(text[i] + '\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
