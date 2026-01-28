#!/usr/bin/python3
import importlib.util

spec = importlib.util.spec_from_file_location("SquareModule", "5-square.py")
square_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(square_module)
Square = square_module.Square

mysquare = Square(3)
mysquare.my_print()

print("--")

mysquare.size = 10
mysquare.my_print()

print("--")

mysquare.size = 0
mysquare.my_print()

print("--")

