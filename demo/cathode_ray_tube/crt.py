class Crt:
    def __init__(self, x):
        self.x = x
        self.pixels = ""
        self.extra_cycles = 0
        self.cycle = 0
        self.ic = 0
        self.instructions = []

    def do_cycles(self, n, instruction_lines):
        self.instructions = instruction_lines.split("\n")
        self.ic = 0
        for self.cycle in range(0, n):
            self._set_pixel()
            self._execute()

    def _execute(self):
        if self.instructions[self.ic] == "noop":
            self.ic += 1
        elif self.instructions[self.ic].startWith("addx ") and self.extra_cycles == 0:
            self.extra_cycles = 1
        elif self.instructions[self.ic].startWith("addx ") and self.extra_cycles == 1:
            self.extra_cycles = 0
            self.x += int(self.instructions[self.ic].substring(5))
            self.ic += 1
        else:
            print("TILT")

    def _set_pixel(self):
        pos = self.cycle % 40
        offset = pos - self.x
        if offset >= -1 and 1 >= offset:
            self.pixels += "#"
        else:
            self.pixels += "."
