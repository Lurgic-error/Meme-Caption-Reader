import cv2
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf8')


meme = cv2.imread('./memes/meme-2.jpg')

caption = pytesseract.image_to_string(meme)

print(caption)

