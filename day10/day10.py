
clock = 0
reg_x = 1


def tick():
    global clock
    cycles_debug = [20, 60, 100, 140, 180, 220]
    clock += 1
    return clock * reg_x if clock in cycles_debug else 0


with open("input.txt") as f:
    sum = 0
    for line in f:
        line = line.strip()
        if line == "noop":
            sum += tick()
        else:
            add_val = int(line.split()[1])
            sum += tick()
            sum += tick()
            reg_x += add_val
    print(f"part A: {sum}")

# part b

clock = 0
reg_x = 1
crt = ["."] * 240


def tick():
    global clock, reg_x, crt
    queue = []
    with open("input.txt") as f:
        for i in range(240):
            sprite = {x for x in range(reg_x - 1, reg_x + 2)}
            if i % 40 in sprite:
                crt[i] = "#"
            if queue:
                reg_x += queue.pop()
                continue
            l = f.readline().strip()
            if l == "noop":
                continue
            queue.append(int(l.split()[1]))


tick()

print("part B:")
for l in range(0, 240, 40):
    print("".join(crt[l:l + 40]))
