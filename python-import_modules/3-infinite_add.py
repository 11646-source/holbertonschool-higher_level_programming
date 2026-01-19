#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) <= 1:
        print(0)
        return
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)
if __name__ == "__main__":
    main()
