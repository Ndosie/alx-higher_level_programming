#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    m = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if a_dictionary[k] == m:
            return k
