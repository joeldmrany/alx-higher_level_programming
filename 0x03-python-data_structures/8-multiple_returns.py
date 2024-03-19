#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or (sentence == None):
        tuple_a = (0, None)
    else:
        i = 0
        for num in sentence:
            i = i + 1
        tuple_a = (i, sentence[0])
        return tuple_a
