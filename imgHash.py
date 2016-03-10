from PIL import Image
import numpy
import scipy.fftpack
import numpy as np

def average_hash(image, hash_size=16):
    """
    Average Hash computation

    Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

    @image must be a PIL instance.
    :param hash_size:
    :param image:
    """
    image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata()).reshape((hash_size, hash_size))
    avg = pixels.mean()
    diff = pixels > avg
            
    tempd = diff
    Nbig = 16
    Nsmall = 8
    Nsmall2 = 4

    diff2 = diff.reshape([Nsmall, Nbig/Nsmall, Nsmall, Nbig/Nsmall]).mean(3).mean(1)
    diff3 = tempd.reshape([Nsmall2, Nbig/Nsmall2, Nsmall2, Nbig/Nsmall2]).mean(3).mean(1)

    diff2 = np.around(diff2)
    diff3 = np.around(diff3)
    return toHashes(diff, diff3, diff2)


def _binary_array_to_hex(arr):
    """
    internal function to make a hex string out of a binary array
    """
    h = 0
    s = []
    for i, v in enumerate(arr.flatten()):
        if v:
            h += 2 ** (i % 8)
        if (i % 8) == 7:
            s.append(hex(h)[2:].rjust(2, '0'))
            h = 0
    return "".join(s)


def toHashes(binary_array, binary_array2, binary_array3):
    hash1 = binary_array
    hash2 = binary_array2
    hash3 = binary_array3
    a = (_binary_array_to_hex(hash1.flatten()), _binary_array_to_hex(hash2.flatten()), _binary_array_to_hex(hash3.flatten()))
    return a


class ImageHash(object):


    def __init__(self, binary_array, binary_array2):
        self.hash = binary_array
        self.hash2 = binary_array2
        self.a = (_binary_array_to_hex(self.hash.flatten()), _binary_array_to_hex(self.hash2.flatten()))
        return a  # Fine, sorry. No returning from init


    def __hash__(self):
        # this returns a 8 bit integer, intentionally shortening the information
        return sum([2 ** (i % 8) for i, v in enumerate(self.hash.flatten()) if v])





