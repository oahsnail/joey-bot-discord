import numpy as np
import cv2
import urllib.request
import os
import imghdr


# returns the file path


# downloads a image from the internet and returns the file path it is stored in
def download_img(url):
    filepath = "temp/downloaded_temp.png"

    urllib.request.urlretrieve(url, filepath)
    if imghdr.what(filepath) == None:
        delete_file(filepath)
        raise Exception('invalid url')
    return filepath


def delete_file(path):
    os.remove(path)


def clean_temp():
    for file in os.scandir('temp'):
        if file.name.endswith(".png"):
            os.unlink(file.path)


def grayscale(filePath):  # destructively grayscales an image

    img = cv2.imread(filePath)
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filePath, imgGrey)


def face_detect(filePath):
    front_face_cascade = cv2.CascadeClassifier(
        'data\cascades\haarcascade_frontalface_alt.xml')

    img = cv2.imread(filePath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = front_face_cascade.detectMultiScale(
        gray_img, scaleFactor=1.5, minNeighbors=1)

    for i, (x, y, w, h) in enumerate(faces):
        print(x, y, w, h)
        roi_gray = gray_img[y:y+h, x:x+w]
        img_item = f'temp/face-image-{i}.png'
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)
        stroke = 3
        end_x_coord = x + w
        end_y_coord = y + h
        cv2.rectangle(img, (x, y), (end_x_coord, end_y_coord), color, stroke)
    cv2.imwrite(filePath, img)


# mostly just here for testing, this script is never actually run on its own in normal use
if __name__ == "__main__":
    path = download_img(
        'https://i.redd.it/01ovjyjwl3h41.jpg')
    print(path)
    face_detect(path)

    clean_temp()
