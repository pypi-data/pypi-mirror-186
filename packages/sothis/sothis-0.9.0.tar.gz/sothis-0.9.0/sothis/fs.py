"""
Name: fs.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: file system related helper functions
"""
import os  # import os features such as path formation and path checking
from typing import List
import shutil as sh  # for copying and moving files
from .nums import is_perfect_square
from PIL import Image


def file_list(abspath: os.PathLike):
    """
    returns absolute paths of the files within a given
    directory
    :param abspath: an absolute exisiting folder path
    :return: list of full fill names
    """
    if not os.path.exists(abspath):
        raise ValueError(f"{abspath} does not exist")
    if not os.path.isdir(abspath):
        raise ValueError(f"{abspath} is not a directory")
    
    return list(map(lambda f: os.path.join(abspath, f), os.listdir(abspath)))


def getfilename(abspath):
    """get the sole file name from an absolute path"""
    return os.path.split(abspath)[1]


def get_extension(filename):
    """get the file extension of a file"""
    return filename.split('.')[-1]


def move_file(start, destination, file):
    """
    moves a file from a starting location to a destination
    :param start: starting path, (parent of file)
    :param destination: absolute path of directory for file to go
    :param file: filename of file to move (just the file name and extension, not absolute)
    :return:
    """
    __operate_on_file(start, destination, file, sh.move)


def copy_file(start, destination, file):
    """
    copies a file from a starting location to a destination
    :param start: starting path, (parent of file)
    :param destination: absolute path of directory for file to go
    :param file: filename of file to move (just the file name and extension, not absolute)
    :return:
    """
    __operate_on_file(start, destination, file, sh.copy)


def __operate_on_file(start, destination, file, func):
    """ execution function """
    
    def last_occurrence(s, c):
        idx = 0
        for i in range(len(s)):
            if s[i] == c:
                idx = i
        return idx
    
    ext_idx = last_occurrence(file, '.')
    name = file[:ext_idx]
    extension = file[ext_idx + 1:]
    name_org = name
    count = 0
    # deal with potential duplicates, opt to make a copy rather than overwrite
    while os.path.exists(os.path.join(destination, f"{name}.{extension}")):
        count += 1
        name = name_org + " ({})".format(count)
    new_file_path = os.path.join(destination, f"{name}.{extension}")
    src = os.path.join(start, file)
    func(src, new_file_path)


def createCollage(name: str, imageFileList: List[os.PathLike], showfile=True):
    """
    creates a collage out of given list of images, only works with filelists with
    a length of a perfect square
    :param name: the desired name of the finished product file (not including extension)
    :param imageFileList: list of absolute paths of images
    :param showfile: toggle of whether to open the image once the process has finished
    :return: new file location string
    """
    numImages = len(imageFileList)
    if not is_perfect_square(numImages):
        raise ValueError("Collage only accepts perfect squares")
    # New image constants
    (WIDTH, HEIGHT) = 1280, 1280
    root = int(math.sqrt(numImages))
    (rows, cols) = root, root
    MODE = "RGB"
    newImage = Image.new(MODE, (WIDTH, HEIGHT))  # create new image
    subimageDimension = HEIGHT // root
    # convert image filepath list to Image objects
    for i in range(len(imageFileList)):
        try:
            imageFileList[i] = Image.open(imageFileList[i])
        except PIL.UnidentifiedImageError:
            imageFileList[i] = None
    
    imageFileList = filter(lambda x: x != None, imageFileList)
    
    # resize all images in image list
    imageFileList = list(map(lambda x: x.resize((subimageDimension, subimageDimension)), imageFileList))
    # paste all images onto new image file
    locations = []
    for x in range(0, rows):
        for y in range(0, cols):
            locations.append((x * subimageDimension, y * subimageDimension))
    
    for i in range(len(imageFileList)):
        newImage.paste(imageFileList[i], locations[i])
    
    # save new image collage file
    fileName = f"{'-'.join((name.lower()).split(' '))}.jpg"
    dest = os.path.join(IMAGES_PATH, fileName)
    newImage.save(dest)
    if showfile:
        print(dest)
        newImage.show()
    
    return fileName
