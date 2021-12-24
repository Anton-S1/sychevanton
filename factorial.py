import itertools
class Factorial:
    class _Factorial_iter:
        def __init__(self):
            self.p = 1
            self.i = 1
        def __next__(self):
            a = self.p
            self.p = self.p * self.i
            self.i += 1
            return a
    def __iter__(self):
        return Factorial._Factorial_iter()

f = Factorial()
print(list(itertools.islice(Factorial(), 15)))
