#!/usr/bin/env python3

class multifilter:

    def judge_half(self):
        return self.pos >= self.neg
    
    def judge_any(self):
        return self.pos > 0

    def judge_all(self):
        return self.pos and self.neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for el in self.iterable:
            self.neg, self.pos = 0, 0
            for func in self.funcs:
                if func(el):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self):
                yield el

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [x for x in range(151)]

print(list(multifilter(a, mul2, mul3, mul5)))
