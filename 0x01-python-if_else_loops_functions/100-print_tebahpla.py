#!/usr/bin/python3
for c in reversed(range(97, 123)):
    if ord(chr(c)) % 2 == 0:
        print("{}".format(upper(chr(c))), end="")
    else:
        print("{}".format(chr(c)), end="")
