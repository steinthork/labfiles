__author__      = "Steinthor Kristinsson"
__copyright__   = "GPLv2"

import sys
import os
import errno
import string
import random
from sys import platform as _platform
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def percentage(part, whole):
  return 100 * float(part)/float(whole)

#Clear the screen
if _platform == "linux" or _platform == "linux2":
    os.system('clear')
elif _platform == "darwin":
    os.system('clear')
elif _platform == "win32":
    os.system('cls')

#Get the current path
path=os.path.normpath(os.getcwd()) + os.sep

print "********************************************\n"
print "********************************************\n"
print "Simple script to create test binary files\n"
print "*******************************************\n"
print "*******************************************\n"
print "\n\n"

#Get user input
foldernum = int(raw_input('How many folders to create?\n>>'))
filenum = int(raw_input('How many files to create in each folder?\n>>'))
kbsize = int(raw_input('How big should the files be KB?\n>>'))
path = os.path.normpath(raw_input('Where should I create these folders/files?\n[%s]\n>>' % path )) + os.sep

total_items = foldernum * filenum
#check if the path typed exists
while not os.path.exists(path):
	print "\n>>Cant find this path!\n>>%s\n" % path
	path = os.path.normpath(raw_input('Where should I create these folders/files\n[%s]\n>>' % path )) + os.sep

confirm = str(raw_input('I will now create %d %sKB files in %d folders [approx %s KB]\nDo you want to continue?\n[y or n]' % (total_items,kbsize,foldernum, total_items*kbsize)))
if not confirm.lower() == str('y'):
	exit()

g=0
#Create the folders
for x in range(foldernum):
	lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(7)]
	randpath = "".join(lst)
#Create the files
	for c in range(filenum):			
		newpath = path + str(randpath) + os.sep
		make_sure_path_exists(newpath)	
		su = [random.choice(string.ascii_letters + string.digits) for k in xrange(7)]
		shii = "".join(su)
		fp = open("%sfilebinary%03d%s.dat" % (newpath, c, shii), "wb")
		filesize = kbsize*1024
		fp.write('\0'*filesize)
		fp.close()
		g+=1
	
	sys.stdout.write('\rProgress [%d%% of %d%%]' % (percentage(g,total_items), 100))
	sys.stdout.flush()
