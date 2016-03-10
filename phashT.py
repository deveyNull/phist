from hashFunk import *
import sys
from phash import *
from datetime import datetime

class phistAction:
    def __init__(self, *args):
        self.hashDirectory = 0
        self.directoryCheck = 0
        self.imageCheck = 0

        self.dirToHash = ""
        self.flatDbName = ""
        self.checkDirectory = ""

        # https://docs.python.org/2/library/argparse.html
        # You lazy little shit
        if sys.argv[1] == "-hd":
            self.hashDirectory = 1
            self.dirToHash = sys.argv[2]
            self.flatDbName = sys.argv[3]
        elif sys.argv[1] == "-dc":
            self.directoryCheck = 1
            self.checkDirectory = sys.argv[2]
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


    def showImage(self, img):
        Image.open(img).show()
        print(img)


    def hDirectory(self):
        count = 0
        newFile(self.dirToHash, self.flatDbName)
            


    def cImage(self):
        flatFileLoad(self.flatDbName)
        hester = list(checkImage(self.imageName, self.flatDbName))
        print(hester)


    def cDirectory(self):
        flatFileLoad(self.flatDbName)
        listOfImages = directoryEater(self.checkDirectory)

        hester = []

        for image in listOfImages:

            a = checkImage(str(image), self.flatDbName)

            if a:
                hester.append([image, a])
        for i in hester:
            print(i[0])

startTime = datetime.now()

a = phistAction()
print(datetime.now()  - startTime)