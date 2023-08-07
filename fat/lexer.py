class Lexer:
    def __init__(self, args):
        self.args = args
        self.nargs = len(args)
        self.i = 0

    def __len__(self):
        return self.nargs - self.i

    def __getitem__(self, i):
        return self.args[self.i+i] if self.i+i < self.nargs else None

    def has_next(self):
        return self.i < self.nargs
    
    
    @staticmethod
    def _clamp(v : int, a, b) -> int: return min(max(v, a), b)

    def move(self, i = 1):
        self.i = Lexer._clamp(self.i + i, 0, self.nargs - 1)

    def read(self):
        if self.i < self.nargs:
            self.i += 1
            return self.args[self.i-1]
        else:
            return None

    def peek(self, i = 0):
        return self.args[self.i+i] if self.i+i < self.nargs else None

        
