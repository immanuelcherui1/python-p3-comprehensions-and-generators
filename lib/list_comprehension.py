#!/usr/bin/env python3

def return_evens(num_list=[]):
    evens = [x for x in num_list if x % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    if sentence_list == None:
        return []
    else:
        return [sentence + '!' for sentence in sentence_list]

