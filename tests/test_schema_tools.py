#!/usr/bin/env python
'''
Test the gegede.schema.tools module.
'''

from gegede.schema.tools import make_converter, validate_input

def test_converter():
    c = make_converter("1cm")
    c("1m")                     # should be okay

    c = make_converter(int)
    try:
        c("1m")                 # should fail
    except ValueError:
        pass
    else:
        raise (RuntimeError, "Failed to catch mismatch with unitless prototype")

    c = make_converter('1cm')
    try:
        c(1)                    # should fail
    except ValueError:
        pass
    else:
        raise (RuntimeError, "Failed to catch mismatch with unitful prototype")

def test_validate_input():
    proto = (("intnum",int),("fpnum",float),("dist","0cm"))
    validate_input(proto, 1, 2.0, "3meter")

    validate_input(proto, 1, dist='4inch')

    try:
        validate_input(proto, 1, 2.0, 3) # should fail
    except ValueError:
        pass
    else:
        raise (RuntimeError, "Did not catch validation failure.")


if "__main__" == __name__:
    test_converter()
    test_validate_input()
