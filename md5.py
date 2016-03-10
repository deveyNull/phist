import os
import hashlib
from hashFunk import *
import sys

with open(sys.argv[2], 'r') as f:
    hashes = f.readlines()
    listOfHashes = []
    for line in hashes:
        listOfHashes.append(line.strip())
 
listOfPaths = directoryEater(sys.argv[1])
for i in listOfPaths:
    tmp = hashlib.md5(open(i, 'rb').read()).hexdigest()
    if tmp in listOfHashes:
        formTmp = i + ": "
        while len(tmp) < 20:
            tmp += " "
        print(formTmp + "\t" + "md5\t" + tmp)