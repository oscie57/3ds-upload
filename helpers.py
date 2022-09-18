import os, string, random
from config import url, loc, locname, debug, secret_key, local, imglimit, consolelimit, port


def foldercheck():

    if locname not in os.listdir('./'):
        os.mkdir(loc)


def genfilename(console, filename, length):

    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result = ''.join(random.choice(letters) for i in range(length))

    split_tup = os.path.splitext(filename)
    file_extension = split_tup[1]
    file_extension = str(file_extension).lower()

    finalname = console + "_" + result + file_extension

    if finalname in os.listdir(loc):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        result = ''.join(random.choice(letters) for i in range(length))

        split_tup = os.path.splitext(filename)
        file_extension = split_tup[1]

        finalname = console + "_" + result + file_extension

    return finalname


def consolecheck(useragent):

    if "New Nintendo 3DS like iPhone" in useragent:
        console = "n3ds"
    elif "Nintendo WiiU" in useragent:
        console = "wiiu"
    elif "Nintendo 3DS" in useragent:
        console = "o3ds"
    elif "Nintendo DSi" in useragent:
        console = "ndsi"
    else:
        console = "unk"

    return console
