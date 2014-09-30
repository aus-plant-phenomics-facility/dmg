#!/usr/bin/python
import os
import sys
from subprocess import call
from os import listdir
from os.path import isfile, join


def printDir(mypath,c,local):
	heading = ''
	for i in range(0,c):
		heading+= '#'
	heading+=  mypath.split('/')[-1]
	for i in range(0,c):
		heading+=  '#'
	print heading
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and f.endswith('.md') and not f.startswith('_')]
	for p in onlyfiles:
		printpath = mypath
		if(local != 0):
			printpath = 'aus-plant-phenomics-facility/dmg/wiki'
		print '['+p.replace('-',' ')[:-3]+'](/'+printpath+'/'+p[:-3]+')\n'

	for item in os.listdir(mypath):
		if os.path.isdir(os.path.join(mypath, item)) and not item.startswith('.'):
				printDir(os.path.join(mypath, item),c+1,local)

sys.stdout = open('_Sidebar.md','w')
mypath = ('.')
try:
	printDir(mypath,1,-1)
finally:
	sys.stdout.close()
call(['git','add','_Sidebar.md'])
call(['git','commit', '-m"Updating Sidebar"'])
call(['git','push', 'origin', 'master'])
sys.stdout = open('_Sidebar.md','w')
try:
	printDir(mypath,1,0)
finally:
	sys.stdout.close()
call(['git','add', '_Sidebar.md'])
call(['git','commit', '-m"Updating Sidebar"'])
