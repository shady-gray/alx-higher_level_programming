#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif arg_count == 3:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[3])
        if (sys.argv[2]
                != "+" and sys.argv[2]
                != "-" and sys.argv[2]
                != "*" and sys.argv[2]
                != "/"):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif sys.argv[2] == "+":
            print("{} {} {} = {}\
                ".format(n1, sys.argv[2], n2, calculator_1.add(n1, n2)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}\
                ".format(n1, sys.argv[2], n2, calculator_1.sub(n1, n2)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}\
                ".format(n1, sys.argv[2], n2, calculator_1.mul(n1, n2)))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}\
                ".format(n1, sys.argv[2], n2, calculator_1.div(n1, n2)))
