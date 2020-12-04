#!/usr/bin/env python3
pro = 1
print('Factorial Calculator v1.0 Vasya Pupkin Inc, copyright 2077 RobCo Ind.')
while True:
    num = input('Enter a number for calculating >>')
    try:
        num = int(num)
        for i in range(1, num+1):
            pro *= i
        print(pro)
        pro = 1
    except ValueError: break
print('Bye!')



