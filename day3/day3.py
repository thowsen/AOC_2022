with open("input.txt") as f:
    sum = 0
    for l in f:
        s = set()
        left = [s.add(e) for e in l[:(len(l) // 2)]]
        for dup in l[len(l) // 2:]:
            if dup in s:
                sum += ord(dup) - 96 if dup.islower() else ord(dup) - 38
                break
    print(sum)


def lazy_read():
    with open("input.txt") as f:
        x = f.read().split()
        for i in range(0, len(x), 3):
            yield x[i:i + 3]


def solve_b():
    sum = 0
    for gnomes in lazy_read():
        # print(gnomes)
        a, b, c = gnomes
        for ch in a:
            if ch in b and ch in c:
                x = ord(ch) - 96 if ch.islower() else ord(ch) - 38
                sum += x
                break

    print(sum)


solve_b()
