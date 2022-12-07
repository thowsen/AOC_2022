from functools import reduce
with open("input.txt") as f:
    init_stacks = []
    for lin in f:
        if lin == "\n":
            break
        lin = lin.replace("\n", "")
        lin = lin.replace("   ", " . ").replace(
            "[", "").replace("]", "")
        init_stacks += [lin]
    var = int(list(filter(lambda a: a != "", init_stacks[-1].split(" ")))[-1])
    stacks = [[] for _ in range(var)]

    init_stacks = init_stacks[0:-1]
    init_stacks.reverse()

    for l in init_stacks:
        l = l.replace(" ", "")
        for i, char in enumerate(l):
            if char == ".":
                continue
            stacks[i].append(char)
        # print(l)
    list(map(lambda a: a.reverse(), stacks))

    stacks[5] = ['N'] + stacks[5]
    stacks[6] = stacks[6][1:]
    print(stacks)

    for inst in f:
        inst = inst.split(" ")
        num, frm, to = int(inst[1]), int(inst[3]) - 1, int(inst[-1]) - 1

        nums = stacks[frm][:num]
        rem = stacks[frm][num:]
        stacks[frm] = rem
        # nums.reverse() # part B lol
        stacks[to] = nums + stacks[to]

    strss = ""
    for stack in stacks:
        strss += stack[0]
    print(strss)
    # print(init_stacks)

# wrong NJRTZTPFN
