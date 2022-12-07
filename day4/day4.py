

with open("input.txt") as f:
    sum = 0
    for lin in f:
        a, b = lin.split(",")
        a_1, a_2 = a.split("-")
        b_1, b_2 = b.split("-")
        a_1, a_2 = int(a_1), int(a_2)
        b_1, b_2 = int(b_1), int(b_2)

        a_range = [x for x in range(a_1, a_2 + 1)]
        b_range = [x for x in range(b_1, b_2 + 1)]

        if b_range[0] >= a_range[0] and b_range[-1] <= a_range[-1]:
            sum += 1
        elif a_range[0] >= b_range[0] and a_range[-1] <= b_range[-1]:
            sum += 1
    print(sum)

with open("input.txt") as f:
    sum = 0
    for lin in f:
        a, b = lin.split(",")
        a_1, a_2 = a.split("-")
        b_1, b_2 = b.split("-")
        a_1, a_2 = int(a_1), int(a_2)
        b_1, b_2 = int(b_1), int(b_2)

        a_range = set((x for x in range(a_1, a_2 + 1)))
        b_range = set((x for x in range(b_1, b_2 + 1)))

        output = a_range & b_range
        if len(output) > 0:
            sum += 1
    print(sum)
