import cv2
from pytesseract import pytesseract
import matplotlib.pyplot as plt
import os

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(os.getcwd())

# 이미지를 흑백으로 불러오기
# img = cv2.imread(".. cd static/car_number_1.png", cv2.IMREAD_GRAYSCALE)
# , cv2.IMREAD_GRAYSCALE)

img = cv2.imread("study\static/car_number_1.png")

print(img.shape)

cv2.imshow('test', img)
cv2.waitKey(0)

plt.imshow(img, cmap="gray")
plt.axis('off')
plt.show

print(os.getcwd())

path = '../car_number_1.png'
print(os.path.exists(path))
