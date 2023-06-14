#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg_count = len(sys.argv) -1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ['+', '-', '*', '/']
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    n1 = int(sys.argv[1])
    n2 = int(sys.argv[3])
    functions =[add, sub, mul, div]
    for func, op in enumerate(operators):
        if sys.argv[2] == op:
            print("{} {} {} = {}".format(n1, op, n2, functions[func](n1, n2)))
            break
    sys.exit(0)
