#!/usr/bin/python3
"""
This is 5-text_indentation module

The 5-text_indentation module has one function ``text_indentation(text)``,
Which prints the `text` and add new line after `.`, `?` and `:` characters.

>>> text_indentation("My name. is? Esther:Ndosi")
My name

is

Esther

Ndosi
"""


def text_indentation(text):
    """Prints text and new line after ., ? and : characters"""

    i = 0

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    while (i < len(text)):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if (i + 1) != len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
