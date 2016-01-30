from hashFunk import *
import sys


def showImage(img):
    Image.open(img).show()
    print(img)


def hDirectory(dirToHash, flatDbName):
    newFile(dirToHash, flatDbName)


def cImage(image, flatDbName):
    flatFileLoad(flatDbName)

    hester = list(checkImage(image, flatDbName))
    return hester


def cDirectory(checkDirectory, flatDbName):
    flatFileLoad(flatDbName)
    listOfImages = directoryEater(checkDirectory)

    hester = []

    for image in listOfImages:
        a = checkImage(str(image), flatDbName)
        if a:
            hester.append([image, a])
    return hester


hashDirectory = 0
directoryCheck = 0
imageCheck = 0

dirToHash = ""
flatDbName = ""
checkDirectory = ""

