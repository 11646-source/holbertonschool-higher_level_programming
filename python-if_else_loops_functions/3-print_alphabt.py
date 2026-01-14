#!/usr/bin/python3
print("{}".format("".join(map(lambda i: chr(i) if i not in (101, 113) else "", range(97, 123)))))
