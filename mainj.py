import cv2
import pytesseract
from Receipt import Receipt
import datetime
import re
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\jakul\anaconda3\Library\bin\tesseract.exe'

def read_receipt(filepath):
    # Read image usingVOpenCS
    img = cv2.imread(filepath, 0)
    # configurations
    config = r'-l eng --oem 3 --psm 6'

    # Parse text using pytesseract
    text = pytesseract.image_to_string(img, config=config, lang='eng')

    # Create a Receipt object using the parsed text
    return Receipt(text)

if __name__ == '__main__':
    rec = read_receipt('receipts/receipt-ocr-original.jpg')
    print(rec.item_lst)
    #print(rec.identification_lst)
