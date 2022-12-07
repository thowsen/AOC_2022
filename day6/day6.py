
buffer_lst = []

# change span for part A


def buffer(char):
    global buffer_lst
    buffer_lst.append(char)
    buffer_lst = buffer_lst[1:15] if len(buffer_lst) > 14 else buffer_lst
    x = set(buffer_lst)
    print(x)
    return len(x) == 14


with open("input.txt") as f:
    buf = []
    f = f.readline()
    for i, c in enumerate(f):
        if buffer(c):
            print(i + 1)
            exit()
