from hashFunk import *

def hashDirectory(dirToHash, flatDbName):
    newFile(dirToHash, flatDbName)


def imageChecker(image, flatDbName):
    flatFileLoad(flatDbName)

    hesterImage = checkImage(image, flatDbName)
    return hesterImage

def imageCheckerSingle(image, flatDbName):
    # DOES NOT LOAD DB
    
    hesterImage = checkImage(image, flatDbName)
    return hesterImage

def directoryChecker(queryDirectory, flatDbName):
    flatFileLoad(flatDbName)
    listOfImages = directoryEater(queryDirectory)

    hester = []
    for image in listOfImages:

        a = imageCheckerSingle(image, flatDbName)

        if a:
            hester.append([image, a])
    return hester



