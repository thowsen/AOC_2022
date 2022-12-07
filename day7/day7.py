
file_dir = {}
context = []


class Item:
    def __init__(self, path, parent=None, size=None):
        self.path = path
        self.type = "DIR" if size is None else "FILE"
        self.contents = []
        self.parent = parent
        self._size = size

    @property
    def size(self):
        if self._size is not None:
            return self._size
        self._size = 0
        for f in self.contents:
            self._size += f.size
        return self._size

    @property
    def sub_folders(self):
        out = []
        for f in self.contents:
            if f.type == "DIR":
                out.append(f)
        return out

    def add_contents(self, name, size=None):
        assert self.type == "DIR"
        p = self.path + [name]
        for f in self.contents:
            if f.path == p:
                return f

        new_child = Item(self.path + [name], parent=self, size=size)

        self.contents.append(new_child)
        return new_child


def report_file_sizes(node):
    out = []
    queue = [node]
    while queue:
        curr = queue.pop()
        out.append(curr)
        queue = queue + curr.contents
    return out


with open("input.txt") as f:

    lines = f.readlines()
    root = Item([])
    curr_dir = root
    for line in lines:

        if line == "$ cd /":
            continue
        line = line.replace("\n", "").split(" ")

        if line[1] == "ls":
            continue
        elif line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                curr_dir = curr_dir.parent
                continue
            curr_dir = curr_dir.add_contents(line[2])
        else:
            size = int(line[0]) if line[0] != 'dir' else None
            curr_dir.add_contents(line[1], size)
    root = root.contents[0]
    x = report_file_sizes(root)

    out = (list(filter(lambda a: a.type == "DIR" and a.size < 100000, x)))
    print(f"part A: {sum([x.size for x in out])}")

    goal = 30000000
    curr_size = 70000000 - root.size
    needed = goal-curr_size

    out = sorted(list(filter(lambda a: a.type == "DIR" and a.size > needed, x)),
                 key=lambda a: a.size)[0].size
    print(f"part B: {out}")
