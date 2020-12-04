#!/usr/bin/env python3
import sys, os; from glob import glob


def join(path, rm = False):
    obj = open(open('%s/header' % path, 'r').read(), 'wb')           # opening file with original filename from "header"
    parts = glob('%spart*' % path)                                   # creating a list with all parts' filenames
    parts.sort()                                                     # sorting that list
    files = len(parts) 
    for filename in parts:
        obj.write(open(filename, 'rb').read())                       # reading data from part and writing it in file
    if rm:                                                           # if "rm" then script will remove all source data
        os.remove('%s/header' % path)
        for filename in parts:
            os.remove(filename)
        os.rmdir(path)
    print('%s from %s parts in %s was restored' % (path[:-6], files, path))      # printing results of task
    

if __name__=='__main__':                                                         # run program only if it running as "main"
    rm = True if '-r' in sys.argv else False
    join(sys.argv[1] if len(sys.argv) > 1 else print('Not enough arguments!'), rm)
