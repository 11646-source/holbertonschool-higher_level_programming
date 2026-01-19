#!/usr/bin/python3
def infinite_add(args):
    total = 0
    for num in args:
        total += int(num)
    return total
if __name__ == "__main__":
    import sys
    print(infinite_add(sys.argv[1:]))
