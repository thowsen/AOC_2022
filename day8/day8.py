
# part A logic
def is_visible(x, y, grid):

    col = list(map(lambda a: a < grid[x][y], grid[x]))
    if all(col[y+1:]) or all(col[:y]):
        return True
    transposed_grid = list(map(list, zip(*grid)))
    col = list(map(lambda a: a < transposed_grid[y][x], transposed_grid[y]))
    if all(col[x+1:]) or all(col[:x]):
        return True
    return False

# part B logic


def calc_scenic_score(x, y, grid):
    y = len(grid) - y - 1
    grid = list(map(list, zip(*grid)))

    def scenic(height, list):
        sum = 0
        for l in list:
            sum += 1
            if l >= height:
                break
        return sum
    scenic_score_right = scenic(grid[y][x], grid[y][x+1:])
    scenic_score_left = scenic(grid[y][x], reversed(grid[y][:x]))

    grid = list(map(list, zip(*grid)))
    scenic_score_up = scenic(grid[x][y], reversed(grid[x][:y]))
    scenic_score_down = scenic(grid[x][y], grid[x][y+1:])

    return scenic_score_down * scenic_score_up * scenic_score_right * scenic_score_left


with open("input.txt") as f:
    grid = [list(map(int, l.strip())) for l in f]
    grid = list(map(list, zip(*grid)))
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_visible(i, j, grid):
                sum += 1
    print(f"part A: {sum}")

    maxim = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            scr = calc_scenic_score(j, i, grid)
            maxim = maxim if scr < maxim else scr

    print(f"part B: {maxim}")
