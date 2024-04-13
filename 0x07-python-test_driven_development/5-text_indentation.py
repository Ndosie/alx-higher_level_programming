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

    if type(text) != str:
        raise TypeError('text must be a string')

    for i in text:
        if i in ".?:":
            print("\n")

        print(i, end="")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
