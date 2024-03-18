#!/usr/bin/python3

def multiple_returns(sentence):
    # calculate string lenght
    sen_len = len(sentence)

    # check if string is empty, and modify return
    if sen_len == 0:
        return (sen_len, None)

    else:
        return (sen_len, sentence[0])
