from flask import Flask, send_file, render_template, request
from debug import request_dump
from PIL import Image

import os

from helpers import foldercheck, genfilename, consolecheck
from config import host, loc, debug, secret_key, imglimit, consolelimit, port

app = Flask(__name__)

global latestimg

latestimg = "../static/default.jpg"

@app.route('/')
def main():
    global latestimg

    if debug == True:
        request_dump(request)

    useragent = request.headers.get('User-Agent')

    consoleraw = consolecheck(useragent)

    match consoleraw:
        case "n3ds":
            console = "a New Nintendo 3DS"
        case "wiiu":
            console = "a Nintendo Wii U"
        case "o3ds":
            console = "an Old Nintendo 3DS"
        case "ndsi":
            console = "a Nintendo DSi"
        case "unk":
            console = "an unknown device"
        case _:
            console = "_"

    return render_template('index.html', console=console, latestimg=latestimg)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global latestimg

    if debug == True:
        request_dump(request)
    useragent = request.headers.get('User-Agent')
    console = consolecheck(useragent)

    if request.method == 'POST':
        file = request.files['file']

        filename = genfilename(console, file.filename, 8)

        img = Image.open(file)

        if console == "unk":
            return render_template('error.html', error="You are not uploading from a 3DS/Wii U console.")
        if img.size[0] not in [400, 320, 854, 1920, 1360, 1366, 1280]:
            return render_template('error.html', error="Image width is incorrect.")
        if img.size[1] not in [240, 480, 720, 1080]:
            return render_template('error.html', error="Image height is incorrect.")

        img.save(os.path.join(loc, filename))

        latestimg = filename

        return render_template('complete.html', uploadname=filename, url=host)

    return render_template('upload.html')


@app.route('/list')
def list():
    if debug == True:
        request_dump(request)

    n3dsimages = []
    wiiuimages = []
    o3dsimages = []

    for image in os.listdir(loc):
        if "n3ds_" in image:
            n3dsimages.append(image)
        if "wiiu_" in image:
            wiiuimages.append(image)
        if "o3ds_" in image:
            o3dsimages.append(image)

    useragent = request.headers.get('User-Agent')
    consoleraw = consolecheck(useragent)

    if consoleraw == "unk" and imglimit is not None:
        while len(n3dsimages) > imglimit:
            n3dsimages.pop()
        while len(wiiuimages) > imglimit:
            wiiuimages.pop()
        while len(o3dsimages) > imglimit:
            o3dsimages.pop()
    
    if consoleraw != "unk" and consolelimit is not None:
        while len(n3dsimages) > consolelimit:
            n3dsimages.pop(-1)
        while len(wiiuimages) > consolelimit:
            wiiuimages.pop()
        while len(o3dsimages) > consolelimit:
            o3dsimages.pop()


    return render_template("list.html", n3dsimages=n3dsimages, wiiuimages=wiiuimages, o3dsimages=o3dsimages, limit=imglimit if consoleraw == "unk" else consolelimit)


@app.route('/css/<sheet>.css')
def css(sheet):

    return send_file(f"./static/{sheet}.css")


@app.route('/uploads/<image>')
def view(image):

    return send_file(f"{loc}/{image}")


if __name__ == '__main__':
    foldercheck()
    app.secret_key = secret_key
    app.run(host, port, debug)
