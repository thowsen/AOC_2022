from typing import Tuple, List, Set
from subprocess import call
import os
from numpy import sign

Snek = List[Tuple[int, int]]

direction = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}


def create_snek(length: int) -> Snek:
    return [(0, 0)] * length


def move_head(snek: Snek, dir: str) -> Snek:
    dx, dy = direction[dir]
    headx, heady = snek[0]
    snek[0] = headx + dx, heady + dy
    return snek


def clear():
    call('clear' if os.name == 'posix' else 'cls')


def move_body(snek: Snek, visited: Set[Tuple[int, int]]) -> Snek:
    prev_x, prev_y = snek[0]
    out_snek = [snek[0]]
    for curr_x, curr_y in snek[1:]:
        dist = abs(curr_x - prev_x) + abs(curr_y - prev_y)
        if dist < 2 or dist == 2 and curr_x != prev_x and curr_y != prev_y:
            out_snek.append((curr_x, curr_y))
            prev_x, prev_y = curr_x, curr_y
            continue
        change_x = prev_x - curr_x
        change_y = prev_y - curr_y
        curr_x += sign(change_x)
        curr_y += sign(change_y)
        prev_x, prev_y = curr_x, curr_y
        out_snek.append((curr_x, curr_y))
    visited.add(out_snek[-1])
    return out_snek, visited


def paint_snake(snek, visited):
    pic = list(['.'] * 32 for _ in range(32))
    head_x, head_y = snek[0]
    for x, y in visited:
        pic[y + 16][x + 16] = '#'
    for i, segment in enumerate(snek[1:]):
        x, y = segment
        pic[y + 16][x + 16] = f"{i + 1}"
    pic[head_y + 16][head_x + 16] = 'H'
    clear()
    pic.reverse()
    for line in pic:
        print("".join(line))


with open("input.txt") as f:
    # snek = create_snek(2) # part A
    snek = create_snek(10)  # part B
    visited = set()

    paint_snake(snek, visited)
    for line in f:
        dir, amount = line.split()
        for _ in range(int(amount)):
            snek = move_head(snek, dir)
            snek, visited = move_body(snek, visited)
            # --- code for stepping ---
            #paint_snake(snek, visited)
            #print(f"current instruction: {dir}, {amount}")
            #print(f"current headpos: ({snek[0][0]},{snek[0][1]})")
            # input()
    print(len(visited))
