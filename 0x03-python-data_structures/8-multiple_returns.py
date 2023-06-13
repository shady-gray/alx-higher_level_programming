#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        result = (0, None)
        return result
    else:
        rem = (sen_len, sentence[0:1])
        return rem
