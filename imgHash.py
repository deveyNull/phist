"""
Image hashing library
======================

Example:

>>> from PIL import Image
>>> import imagehash
>>> hash = imagehash.average_hash(Image.open('test.png'))
>>> print(hash)
d879f8f89b1bbf
>>> otherhash = imagehash.average_hash(Image.open('other.bmp'))
>>> print(otherhash)
ffff3720200ffff
>>> print(hash == otherhash)
False
>>> print(hash - otherhash)
36
>>> for r in range(1, 30, 5):
...     rothash = imagehash.average_hash(Image.open('test.png').rotate(r))
...     print('Rotation by %d: %d Hamming difference' % (r, hash - rothash))
...
Rotation by 1: 2 Hamming difference
Rotation by 6: 11 Hamming difference
Rotation by 11: 13 Hamming difference
Rotation by 16: 17 Hamming difference
Rotation by 21: 19 Hamming difference
Rotation by 26: 21 Hamming difference
>>>

"""

from PIL import Image
import numpy
import scipy.fftpack


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


# noinspection PyPep8,PyPep8
def toHashes(binary_array, binary_array2, binary_array3):
    hash1 = binary_array
    hash2 = binary_array2
    hash3 = binary_array3
    a = (
    _binary_array_to_hex(hash1.flatten()), _binary_array_to_hex(hash2.flatten()), _binary_array_to_hex(hash3.flatten()))
    return a


def phashes(image, hash_size=12, highfreq_factor=4, hash_size2=4, highfreq_factor2=4, hash_size3=8, highfreq_factor3=4):
    """
    Perceptual Hash computation.

    Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

    @image must be a PIL instance.
    :param highfreq_factor3:
    :param hash_size3:
    :param highfreq_factor2:
    :param hash_size2:
    :param highfreq_factor:
    :param hash_size:
    :param image:
    """
    image2 = image
    image3 = image
    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:hash_size, :hash_size]
    med = numpy.median(dctlowfreq)
    diff = dctlowfreq > med
    img_size = hash_size2 * highfreq_factor2
    image2 = image2.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels2 = numpy.array(image2.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct2 = scipy.fftpack.dct(scipy.fftpack.dct(pixels2, axis=0), axis=1)
    dctlowfreq2 = dct2[:hash_size2, :hash_size2]
    med2 = numpy.median(dctlowfreq2)
    diff2 = dctlowfreq2 > med2
    img_size = hash_size3 * highfreq_factor3
    image3 = image3.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels3 = numpy.array(image3.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct3 = scipy.fftpack.dct(scipy.fftpack.dct(pixels3, axis=0), axis=1)
    dctlowfreq3 = dct3[:hash_size3, :hash_size3]
    med3 = numpy.median(dctlowfreq3)
    diff3 = dctlowfreq3 > med3
    return toHashes(diff, diff2, diff3)


def dhashes(image, hash_size1=12, hash_size2=4, hash_size3=8):
    """
    Difference Hash computation.

    following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html

    @image must be a PIL instance.
    :param hash_size3:
    :param hash_size2:
    :param hash_size1:
    :param image:
    """
    image2 = image
    image3 = image
    image = image.convert("L").resize((hash_size1 + 1, hash_size1), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size1 + 1, hash_size1))
    # compute differences
    diff = pixels[1:, :] > pixels[:-1, :]
    image2 = image2.convert("L").resize((hash_size2 + 1, hash_size2), Image.ANTIALIAS)
    pixels2 = numpy.array(image2.getdata(), dtype=numpy.float).reshape((hash_size2 + 1, hash_size2))
    # compute differences
    diff2 = pixels2[1:, :] > pixels2[:-1, :]
    image3 = image3.convert("L").resize((hash_size3 + 1, hash_size3), Image.ANTIALIAS)
    pixels3 = numpy.array(image3.getdata(), dtype=numpy.float).reshape((hash_size3 + 1, hash_size3))
    # compute differences
    diff3 = pixels3[1:, :] > pixels3[:-1, :]
    return toHashes(diff, diff2, diff3)


class ImageHash(object):
    """
    Hash encapsulation. Can be used for dictionary keys and comparisons.
    """


    def __init__(self, binary_array, binary_array2):
        self.hash = binary_array
        self.hash2 = binary_array2
        self.a = (_binary_array_to_hex(self.hash.flatten()), _binary_array_to_hex(self.hash2.flatten()))
        return a  # Fine, sorry. No returning from init

    def __repr__(self):
        return repr(self.hash)

    def __sub__(self, other):
        if other is None:
            raise TypeError('Other hash must not be None.')
        if self.hash.size != other.hash.size:
            raise TypeError('ImageHashes must be of the same shape.', self.hash.shape, other.hash.shape)
        return (self.hash.flatten() != other.hash.flatten()).sum()

    def __eq__(self, other):
        if other is None:
            return False
        return numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    def __ne__(self, other):
        if other is None:
            return False
        return not numpy.array_equal(self.hash.flatten(), other.hash.flatten())

    def __hash__(self):
        # this returns a 8 bit integer, intentionally shortening the information
        return sum([2 ** (i % 8) for i, v in enumerate(self.hash.flatten()) if v])


def hex_to_hash(hexstr):
    """
    Convert a stored hash (hex, as retrieved from str(Imagehash))
    back to a Imagehash object.
    :param hexstr:
    """
    l = []
    if len(hexstr) != 16:
        raise ValueError('The hex string has the wrong length')
    for i in range(8):
        h = hexstr[i * 2:i * 2 + 2]
        v = int("0x" + h, 16)
        l.append([v & 2 ** i > 0 for i in range(8)])
    return ImageHash(numpy.array(l))


def average_hash(image, hash_size=8):
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
    # make a hash
    return ImageHash(diff)


def phash(image, hash_size=8, highfreq_factor=4):
    """
    Perceptual Hash computation.

    Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

    @image must be a PIL instance.
    :param highfreq_factor:
    :param hash_size:
    :param image:
    """
    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:hash_size, :hash_size]
    med = numpy.median(dctlowfreq)
    diff = dctlowfreq > med
    return ImageHash(diff)


def phash4(image, hash_size=4, highfreq_factor=4):
    """
    Perceptual Hash computation.

    Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

    @image must be a PIL instance.
    :param highfreq_factor:
    :param hash_size:
    :param image:
    """
    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels, axis=0), axis=1)
    dctlowfreq = dct[:hash_size, :hash_size]
    med = numpy.median(dctlowfreq)
    diff = dctlowfreq > med
    return ImageHash(diff)


def phash_simple(image, hash_size=8, highfreq_factor=4):
    """
    Perceptual Hash computation.

    Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

    @image must be a PIL instance.
    :param highfreq_factor:
    :param hash_size:
    :param image:
    """
    img_size = hash_size * highfreq_factor
    image = image.convert("L").resize((img_size, img_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((img_size, img_size))
    dct = scipy.fftpack.dct(pixels)
    dctlowfreq = dct[:hash_size, 1:hash_size + 1]
    avg = dctlowfreq.mean()
    diff = dctlowfreq > avg
    return ImageHash(diff)


def dhash(image, hash_size=8):
    """
    Difference Hash computation.

    following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html

    @image must be a PIL instance.
    :param image:
    :param hash_size:
    """
    image = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
    pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size + 1, hash_size))
    # compute differences
    diff = pixels[1:, :] > pixels[:-1, :]
    return ImageHash(diff)
