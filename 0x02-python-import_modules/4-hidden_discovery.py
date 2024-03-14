#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    secret = dir(hidden_4)
    for name in secret:
        if name[0:2] != "__":
            print("{}".format(name))
