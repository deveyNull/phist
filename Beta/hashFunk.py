###################################################################
###################################################################
#
#		DISCLAIMER:
#			THIS IS A PROOF OF CONCEPT AND AS A RESULT, IS AN UGLY, HACKED TOGETHER MESS.
#		 	IN NO WAY SHOULD THIS BE CONFUSED WITH 'GOOD' CODE.
# 		
#			SORRY. 
#					-Devey
#							20 Jan 2015
###################################################################
###################################################################

import os
from PIL import Image
import imgHash  # https://pypi.python.org/pypi/imgHash
import itertools
from collections import defaultdict
import time


###################################################################################
##                 - - - DISCRETE COSINE TRANSFORM - - -                         ##
## 										                                         ##										
##                                    			                                 ##
##			                                                                     ##
##                                                                               ##
###################################################################################
def phashes(image):  # returns 32 byte dct hash, 4 byte, 16 byte
    #return imgHash.phashes(Image.open(image))
    return imgHash.phash(Image.open(image))

###################################################################################
##                        - - - GRADIENT HASH - - -                              ##
## 										                                         ##										
##                                    			                                 ##
##			                                                                     ##
##                                                                               ##
###################################################################################
def dhashes(image):  # returns 32 byte gradient hash, 4 byte, 16 byte
    #return imgHash.dhashes(Image.open(image))
    return imgHash.dhash(Image.open(image))

###################################################################################
##                        - - - Average HASH - - -                               ##
## 										                                         ##										
##                                    			                                 ##
##			                                                                     ##
##                                                                               ##
###################################################################################
def ahashes(image):  # returns 32 byte gradient hash, 4 byte, 16 byte
    #return imgHash.dhashes(Image.open(image))
    return imgHash.average_hash(Image.open(image))
###################################################################################
##                       - - - GET DATA - - -                                    ##
## 									                                        	 ##										
##  As of right now, returns the image name and Date/Time.                       ##
##  Should be customized for different applications of this library.             ##
##										                                         ##
###################################################################################

def getData(image):
    # imageName = image.split("/")[1]
    dateAdded = time.strftime("%H:%M %d/%m/%Y").strip()

    return image, dateAdded  # HUGE CHANGE AGHHH


###################################################################################
##                   - - - GET HAMMING DISTANCE - - -                            ##
## 										                                         ##										
##                                    			                                 ##
##			                                                                     ##
##                                                                               ##
###################################################################################

def hamming1(str1, str2):  # returns distance between strings
    return sum(itertools.imap(str.__ne__, str1, str2))


###################################################################################
##                      - - - GET HASHES - - -                                   ##
## 										                                         ##										
## returns all hashes in format: 		                         				 ##
##			[(32byte, 4byte, 16byte), (32byte, 4byte, 16byte), (data)]                   ##
##                           -Discrete Cosine-	     -Transform     -Info-       ##
###################################################################################

def getHashes(image):
    return [phashes(image), ahashes(image), getData(image)]


def bulkLoader(listOfFiles):  # takes a list of files and returns a list of their full hashes
    hashList = []
    for fileName in listOfFiles:
        # print(fileName)
        # data = fileName
        hashList.append(getHashes(fileName))
    return hashList


def dbBuilder(hashList):  # Database Builder

    for i in hashList:
        p32[i[0][0]].append(list(i[2]))
        a32[i[1][0]].append(list(i[2]))
        pBuckets[i[0][1]].append((i[0][2], i[0][0]))
        aBuckets[i[1][1]].append((i[1][2], i[1][0]))

def readHashes(fileName):  # reads full hashes out of a flat file and returns a list of them
    with open(fileName, 'r') as f:
        hashes = f.readlines()
        fileHashes = []

        for line in hashes:
            c = line
            a = c.split(", ")
            fileHashes.append([(a[0], a[1], a[2]), (a[3], a[4], a[5]), (a[6], a[7].strip())])
        return fileHashes


def writeHashes(hashes, fileName):  # write full hashes to flat file
    f = open(fileName, 'a')  # Open flatFile to append t

    f.write('%s, %s, %s, %s, %s, %s, %s, %s\n' % (
    hashes[0][0], hashes[0][1], hashes[0][2], hashes[1][0], hashes[1][1], hashes[1][2], hashes[2][0], hashes[2][1]))
    f.close()  # File close
    return hashes[0], hashes[1], hashes[2]


def writeMassHashes(listOfHashes, fileName):  # write full hashes to flat file
    listToWrite = []
    for hashes in listOfHashes:
        listToWrite.append('%s, %s, %s, %s, %s, %s, %s, %s\n' % (
        hashes[0][0], hashes[0][1], hashes[0][2], hashes[1][0], hashes[1][1], hashes[1][2], hashes[2][0], hashes[2][1]))

    f = open(fileName, 'a')  # Open flatFile to append t
    f.writelines(listToWrite)
    f.close()  # File close


# return(hashes[0], hashes[1], hashes[2])

def checkHashes(imgHashes, fileName):  # O(1) Lookup... This is how we do it
    if imgHashes[0][0] in p32:  # Check dct hashtable for hash

        return "p32", imgHashes[0][0], p32[imgHashes[0][0]]

    elif imgHashes[1][0] in a32:  # Check gradient hashtable for hash

        return "a32", imgHashes[1][0], a32[imgHashes[1][0]]

    elif imgHashes[0][1] in pBuckets:  # If 4 byte hash in pBuckets
        bucket = pBuckets[imgHashes[0][1]]
        for i in bucket:  # For all items in bucket
            h1 = hamming1(imgHashes[0][2], i[0])  # Get hamming distance between queried images 16 byte phash and item
            if h1 < 3:  # If hamming distance is less than ___
                return "pBk", i[1], p32[i[1]]  # Return True, 32 byte pHash, data

            else:  # Should modularize this more, no time now
                if imgHashes[1][1] in aBuckets:  # If 4 byte hash in aBuckets
                    bucket = aBuckets[imgHashes[1][1]]
                    for j in bucket:  # Same thing
                        h1 = hamming1(imgHashes[1][2], j[0])
                        if h1 < 3:
                            return "p-a", j[1], a32[j[1]]
                        else:  # Image not in database
                            return False
                else:  # Image not in database
                    return False

    elif imgHashes[1][1] in aBuckets:  # If 4 byte hash in aBuckets
        bucket = aBuckets[imgHashes[1][1]]
        for i in bucket:  # Same thing
            h1 = hamming1(imgHashes[1][2], i[0])
            if h1 < 3:
                
                return "aBk", i[1], a32[i[1]]
            else:  # Image not in database
                return False
    else:  # Does not match any buckets
        return False


def checkHashesAdd(imgHashes, fileName):  # O(1) Lookup... This is how we do it
    if imgHashes[0][0] in p32:  # Check dct hashtable for hash

        return "p32", imgHashes[0][0], p32[imgHashes[0][0]]

    elif imgHashes[1][0] in a32:  # Check gradient hashtable for hash

        return "a32", imgHashes[1][0], a32[imgHashes[1][0]]

    elif imgHashes[0][1] in pBuckets:  # If 4 byte hash in pBuckets
        bucket = pBuckets[imgHashes[0][1]]
        for i in bucket:  # For all items in bucket
            h1 = hamming1(imgHashes[0][2], i[0])  # Get hamming distance between queried images 16 byte phash and item
            if h1 < 3:  # If hamming distance is less than ___
                writeHashes(imgHashes, fileName)  # Add hash to databases
                return "pBk", i[1], p32[i[1]]  # Return True, 32 byte pHash, data

            else:  # Should modularize this more, no time now
                if imgHashes[1][1] in aBuckets:  # If 4 byte hash in aBuckets
                    bucket = aBuckets[imgHashes[1][1]]
                    for j in bucket:  # Same thing
                        h1 = hamming1(imgHashes[1][2], j[0])
                        if h1 < 3:
                            writeHashes(imgHashes, fileName)
                            return "p-a", j[1], a32[j[1]]
                        else:  # Image not in database
                            # print("p-a fail. Not in Database, adding.")
                            writeHashes(imgHashes, fileName)  # Add to database
                            return False
                else:  # Image not in database
                    return False

    elif imgHashes[1][1] in aBuckets:  # If 4 byte hash in aBuckets
        bucket = aBuckets[imgHashes[1][1]]
        for i in bucket:  # Same thing
            h1 = hamming1(imgHashes[1][2], i[0])
            if h1 < 3:
                writeHashes(imgHashes, fileName)
                return "aBk", i[1], a32[i[1]]
            else:  # Image not in database
                # print("d fail. Not in Database, adding.")
                writeHashes(imgHashes, fileName)  # Add to database
                return False
    else:  # Does not match any buckets
        # print("No matches. Not in Database, adding.")
        writeHashes(imgHashes, fileName)  # Add to database
        return False


def directoryEater(directoryName):  # Given a directory name, returns list of files in directory for entering into bulkLoader
    path = os.getcwd()
    fileNamesWSpaces = os.listdir(path)
    for filename in fileNamesWSpaces:
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(" ", "-")))
    fileNames = os.listdir(directoryName)
    b = []
    for i in fileNames:
        b.append(directoryName + "/" + i)
    return b


def flatFileLoad(fileName):  # Given the name of a flat file, enters them into the database
    dbBuilder(readHashes(fileName))


def bulkFlatFileWrite(dbName, listOfFiles):  # Given a list of files, write full hashes to specified flat file
    listOfHashes = []
    for i in listOfFiles:
        listOfHashes.append(getHashes(i))
    writeMassHashes(listOfHashes, dbName)


def newFile(directoryName, fileName):  # Create a new flatFile from a directory of images
    listOfFiles = directoryEater(directoryName)
    bulkFlatFileWrite(fileName, listOfFiles)


def checkImage(image, dbName):
    return checkHashes(getHashes(image), dbName)


def checkImageAdd(image, dbName):
    return checkHashesAdd(getHashes(image), dbName)


##########################
##	Globals		##
##    Don't Touch!	##
##########################
p32 = defaultdict(list)  # 32 byte discrete cosine transform hash table
a32 = defaultdict(list)  # 32 byte gradient hash table
pBuckets = defaultdict(list)  # Staggered(4 byte -> 16 byte) dct hash table
aBuckets = defaultdict(list)  # Staggered(4 byte -> 16 byte) gradient hash table

########################################################################################
