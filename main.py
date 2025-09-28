import pytesseract
import argparse
import cv2
import os

# Set up the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to apply to the image")
args = vars(ap.parse_args())

def main():
    #Reads the image from the command line argument
    image = cv2.imread(args["image"])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #use Tesseract to OCR the image
    text = pytesseract.image_to_string(image)
    print(text)


if __name__ == "__main__":
    main()
