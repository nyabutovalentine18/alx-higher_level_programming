#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir(hidden_4)
    for name in names:
        if names[:2] != "__":
            print(name)
