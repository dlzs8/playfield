#!/usr/bin/env python

num = raw_input()

while num.isdigit():
    num = int(num)
    res = 0
    while num:
        res += num % 10
        num /= 10
    print(res)
    num = raw_input()


