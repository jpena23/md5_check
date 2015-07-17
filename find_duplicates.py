#!/usr/bin/python

import hashlib
import os

dir_list = os.listdir('.')
dir_dict = {}

for i in dir_list:
    # make sure each iteration is a file and not a directory or something else...
    if os.path.isfile(i):
        with open(i) as file_to_check:
            # read contents of file
            data = file_to_check.read()
            # get the md5 hash of the file
            md5_sum = hashlib.md5(data).hexdigest()
            # check if we have seen this md5, if so append file name to value array
            if md5_sum in dir_dict:
                dir_dict[md5_sum].append(i)
            else:
                dir_dict[md5_sum] = [i]
    elif os.path.isdir(i):
        print "\n%s is a directory\n" % i
    else:
        print "no idea."

results = list(filter(lambda x: len(x) > 1, dir_dict.values()))
print "The following files are duplicates: "
for i in results:
    print "--------------------------------------"
    print i
    print "--------------------------------------"

#print dir_dict
