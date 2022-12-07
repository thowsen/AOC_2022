
with open("input.txt") as f:
    input = f.read().split("\n\n")
    ans = sorted(map(lambda a: sum(map(int, a.split())), input))
    print(f"Answer 1: {ans[-1]}")
    print(f"Answer 2: {sum(ans[-3:])}")
