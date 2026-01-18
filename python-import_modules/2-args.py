#!/usr/bin/python3
import sys
def main():
    args = sys.argv[1:]
    count = len(args)
    if count == 0:
        print(f"Number of argument(s) {count}.")
    elif count == 1:
        print(f"Number of argument(s) {count} argument:")
    else:
        print(f"Number of argument(s) {count} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
            if __name__ == "__main__":
                main()
