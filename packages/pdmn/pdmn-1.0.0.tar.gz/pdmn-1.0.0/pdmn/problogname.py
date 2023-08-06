"""
This file is part of the pDMN solver.
Author: Simon Vandevelde
s.vandevelde@kuleuven.be
"""


def problog_name(string: str):
    """
    Formats a string to be compatible for the ProbLog system.
    This means that it changes some characters to others.

    :arg string: the string to change.
    :returns str: the ProbLog compatible string.
    """
    string = str(string)
    try:
        return str(int(string))
    except ValueError:
        pass
    try:
        return str(float(string))
    except ValueError:
        pass

    return f'{string}'\
           .replace(' ', '_')\
           .replace('“', '"')\
           .replace('”', '"')
