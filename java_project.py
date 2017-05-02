#!/usr/bin/python3

import os
import sys

if len(sys.argv) <2:
    exit()
else:
    num='Test'+sys.argv[1]

temdir='/home/susan/software/eclipse/workspace/Template/'

newdir=lambda x:x.replace('Template',num)
os.mkdir(newdir(temdir))

def deepcopy(fl):
    global newdir
    for fn in fl:
        if os.path.isfile(fn):
            fin=open(fn,'rt')
            buff=fin.read()
            buff=buff.replace('Test30001',num)
            fn=newdir(fn).replace('Test30001',num)
            fout=open(fn,'wt')
            fout.write(buff)
            fout.close()
            fin.close()
        else:
            os.mkdir(newdir(fn))
            nfl=os.listdir(fn)
            nfl=map(lambda x:fn+'/'+x,nfl)
            deepcopy(nfl)

fl=os.listdir(temdir)
fl=map(lambda x:temdir+x,fl)
deepcopy(fl)

