#!/usr/bin/python
import os
import sys
from subprocess import call
from os import listdir
from os.path import isfile, join


def printDir(directory, c, isLocal):
    heading = ''
    for i in range(0, c):
        heading += '#'
    heading += directory.split('/')[-1]
    for i in range(0, c):
        heading += '#'
    print heading
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith('.md') and not f.startswith('_')]
    for p in onlyfiles:
        printpath = directory
        if(isLocal != 0):
            printpath = 'aus-plant-phenomics-facility/dmg/wiki'
        print '['+p.replace('-', ' ')[:-3]+'](/'+printpath+'/'+p[:-3]+')\n'

    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)) and not item.startswith('.'):
                printDir(os.path.join(directory, item), c+1, isLocal)

sys.stdout = open('_Sidebar.md', 'w')
directory = ('.')
try:
    printDir(directory, 1, -1)
finally:
    sys.stdout.close()
call(['git', 'add', '_Sidebar.md'])
call(['git', 'commit', '-m"Updating Sidebar"'])
call(['git', 'push', 'origin', 'master'])
sys.stdout = open('_Sidebar.md', 'w')
try:
    printDir(directory, 1, 0)
finally:
    sys.stdout.close()
call(['git', 'add', '_Sidebar.md'])
call(['git', 'commit', '-m"Updating Sidebar"'])
