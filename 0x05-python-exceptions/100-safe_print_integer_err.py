#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as er:
        import sys
        sys.stderr.write("Exception: {}".format(er))
        return False
    else:
        return True
