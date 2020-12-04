#!/usr/bin/env python3

num = input()

while num.isdigit():
    res = 0
    num = int(num)
    while num:
        res += num % 10
        num //= 10
    print(res)
    num = input()
