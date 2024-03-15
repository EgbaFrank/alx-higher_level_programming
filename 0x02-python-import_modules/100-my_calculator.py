#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, cal.add(a, b)))

    elif operator == '-':
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))

    elif operator == '*':
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))

    elif operator == '/':
        print("{} / {} = {}".format(a, b, cal.div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
