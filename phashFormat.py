
import sys
from phash import *


class phistAction:
    def __init__(self, *args):
        self.hashDirectory = 0
        self.directoryCheck = 0
        self.imageCheck = 0

        self.dirToHash = ""
        self.flatDbName = ""
        self.queryDirectory = ""

        # https://docs.python.org/2/library/argparse.html
        # You lazy little shit
        if sys.argv[1] == "-hd":
            self.hashDirectory = 1
            self.dirToHash = sys.argv[2]
            self.flatDbName = sys.argv[3]
        elif sys.argv[1] == "-dc":
            self.directoryCheck = 1
            self.queryDirectory = sys.argv[2]
            self.flatDbName = sys.argv[3]
        elif sys.argv[1] == "-ic":
            self.imageCheck = 1
            self.imageName = sys.argv[2]
            self.flatDbName = sys.argv[3]

        if self.hashDirectory == 1:
            self.hDirectory()
        elif self.directoryCheck == 1:
            self.cDirectory()
        elif self.imageCheck == 1:
            self.cImage()


    def hDirectory(self):
        hashDirectory(self.dirToHash, self.flatDbName)


    def cImage(self):
        hester = imageChecker(self.imageName, self.flatDbName)
        print(hester)


    def cDirectory(self):
        hester = directoryChecker(self.queryDirectory, self.flatDbName)
        
        print("\n\tFile Queried:\t\tFile Matched:\t\tDate Entered:\n")
        for i in hester:
           
            s = "\t" + str(i[0].split("/")[3])
            
            for j in i:
                #print(j)
                tmp = j[0]
                while len(tmp) < 20:
                    tmp += " "
            s += ":\t" + "\t" + i[1][2][0][0] + "\t""\t" + i[1][2][0][1] 
            print(s)      
        print("\n") 
    


a = phistAction()
