class EvenNumbers():

    def __init__(self, start = 0, end = 1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.value = self.start if self.start % 2 == 0 else self.start + 1
        return self

    def __next__(self):
        if self.value <= self.end:
            t = self.value
            self.value += 2
            return t
        else:
            raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    print(i)