#!/usr/bin/env python3

def primes():
    res = 1
    yield 2 
    while True:
        res += 2
        for i in range(3, res + 1):
            if i < res and res % i == 0:
                break
            elif i == res:
                yield res

if __name__ == '__main__':
    import sys
    numS = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    ct = 0
    gen = iter(primes())
    while ct < numS:
        print(gen.__next__())
        ct += 1

