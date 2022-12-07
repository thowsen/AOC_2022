
beats = ["A", "B", "C"]

with open("real_input.txt") as f:
    trans = {"X": "A", "Y": "B", "Z": "C"}
    beats = ["A", "B", "C"]
    sm = 0
    for lin in f:
        a, b = lin.split()
        b = trans[b]
        score_choice = beats.index(b) + 1

        if a == b:
            sm += score_choice + 3
            print(f"{score_choice} + {3}")
        elif beats.index(a) == (beats.index(b) + 1) % 3:
            sm += score_choice
            print(f"{score_choice} + {0}")
        else:
            sm += score_choice + 6
            print(f"{score_choice} + {6}")

    print(sm)


def lose(l):
    choice = (beats.index(l) + 3 - 1) % 3 + 1
    print(f"lose with score: {choice} + {0}")
    return choice + 0


def win(l):
    choice = (beats.index(l) + 1) % 3 + 1
    print(f"win with score: {choice} + {6}")
    return choice + 6


def draw(l):
    choice = beats.index(l) + 1
    print(f"draw with score: {choice} + {3}")
    return choice + 3


with open("real_input.txt") as f:
    beats = ["A", "B", "C"]
    sum = 0
    for lin in f:
        a, b = lin.split()
        if b == "X":
            sum += (beats.index(a) + 3 - 1) % 3 + 1
        elif b == "Y":
            sum += draw(a)
        else:
            sum += win(a)
    print(sum)
