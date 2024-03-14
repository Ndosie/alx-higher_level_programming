#!/usr/bin/python3
if __name__ == "__main__":
    for a in dir(hidden_4).sort():
        if a[0] == "_":
            continue

    print(a)
