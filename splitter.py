#!/usr/bin/env python3
import sys, os                         # import operating system modules

def split(file, size, rm = False):                 # main function
    workpath = '%sparts' % file
    obj = open(file, 'rb')             # opening source file
    filepart = 1                       # part counter
    os.mkdir(workpath)                 # creating directory with parts of file
    open('%s/header' % workpath, 'w').write(file)     # creating "header" = a file with info about original filename
    run = True                         # while loop condition
    while run:
        part = obj.read(size)          # reading data from source file
        if part: open('./%s/part%04d' % (workpath, filepart), 'wb').write(part); filepart += 1   # write part if data in source
                                                                                                 # file still exists; increasing
                                                                                                 # counter

        else: obj.close(); run = False                                                           # else = stop loop
    if rm: os.remove(file)
    print('%s parts of %s in %s was created' % (filepart - 1, file, workpath))                   # print results of task
    
if __name__=='__main__':                                     # run function only if program running as "main", not imported
    rm = True if '-r' in sys.argv else False
    split(sys.argv[1], int(sys.argv[2])*1024, rm)                # run "split" with 2 command line arguments = filename and size 
                                                             # in KB
