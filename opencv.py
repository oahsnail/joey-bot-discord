import numpy as np
import cv2
import urllib.request
import os
import imghdr

# returns the file path


def download_img(url):
    filepath = "temp/temp.png"

    urllib.request.urlretrieve(url, filepath)
    if imghdr.what(filepath) == None:
        delete_file(filepath)
        raise Exception('invalid url')
    return filepath


def delete_file(path):
    os.remove(path)


# destructively grayscales an image
def grayscale(filePath):

    img = cv2.imread(filePath)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filePath, imgGrey)


def face_detect():
    face_cascade = cv2.CascadeClassifier(
        'data\cascades\haarcascade_frontalface_alt2.xml')


if __name__ == "__main__":
    path = download_img(
        'https://localtvwtvr.files.wordpress.com/2019/08/walterpic.jpg?quality=85&strip=all&w=770&h=770')
    print(path)
    grayscale(path)
    print(imghdr.what('temp/temp.png'))
