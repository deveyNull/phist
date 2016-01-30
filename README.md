# phist
Perceptual Hashing Image Similarity Tool

A perceptual hash is a function that is able to transform a given image into a hash of a specified length based off of the image's visual properties, which means that similar images return similar hashes and visually identical images return matching hashes. Queries to a database of these hashes returns the hash of the image that is most similar to the queried one. My method of storing the database allows a constant time lookup instead of the customary order n lookup, allowing perceptual hashing to be implemented at scale. 

What this all means is that this tool can find similar images in a database significantly faster than any other method *that I know of*.

This is a side-project, a labor of love, but it's a damn good time and we'll be making shit happen with it soon.
