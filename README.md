# phist
##Perceptual Hashing Image Similarity Tool

A perceptual hash is a function that is able to transform a given image into a hash of a specified length based off of the image's visual properties, which means that similar images return similar hashes and visually identical images return matching hashes. Queries to a database of these hashes returns the hash of the image that is most similar to the queried one. My method of storing the database allows a constant time lookup instead of the customary order n lookup, allowing perceptual hashing to be implemented at scale. 

What this all means is that this tool can find similar images in a database significantly faster than any other method *that I know of*.

This is a side-project, a labor of love, but it's a damn good time and we'll be making shit happen with it soon.

###Here's a quick description of each file:

**imgHash.py** = The actual file containing the perceptual hashing functions
**hashFunk.py** = The guts of the tool, an absolute pile of functions that make everything else work
**phash.py** = The pretty file every other tool imports
**phashT.py** = a terminal client that can be used to index directories, check images, or check directories


**omarax_local.py** = A fantastic tool written by the awesome Jaime Filson, takes screenshots of webpages
**screenshotchecker.py** = A tool which, given a list of websites(domain.txt), calls omarax to take screenshots and a seperate tool to download all images on the page and check them against a database


**imageGUI.py** = Fully functional tkinter GUI that checks one image against a database and returns all data associated
**dirGUI.py** = Sorta functional tkinter GUI, work in progress


