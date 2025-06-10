import os
import cv2
import web_cam
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# face_mask 읽기 -> use icon
# 이거 왜 자꾸 안되냐.... 맘같아선 스태틱 파일 만들어서 하고싶은데
icon = cv2.imread('study/face_mask.png')


# face_mask에 contour 찾기 # find contour 는 이진화 이미지만 읽으니
# 전처리 : 흑백 -> 이진화 -> findContours()
gray_icon = cv2.cvtColor(icon, cv2.COLOR_RGB2GRAY)  # 흑백 변환
gray_icon = 255 - gray_icon  # 흑백 반전
_, bin_icon = cv2.threshold(gray_icon, 50, 255, cv2.THRESH_BINARY)

cv2.imshow('test', bin_icon)
# contour로 mask 만들기
contours, _ = cv2.findContours(
    bin_icon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(gray_icon)
cv2.drawContours(mask, contours, -1, 255, -1)


def process(frame):
    # # 회색으로 반환하기
    # gray_color = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # return gray_color

    # 1. 얼굴 인식
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(70, 70)
    )

    # 2. 얼굴 마다 작업 진행

    # 3~4 icon 과 mask를 global 영역에서 구함
    # 얼굴 영역에 mask 이용해서 icon 덮어쓰기
    # (1) frame 직접 그릴수는 없기 때문에, 울굴 영역을 우선 찾는다.

    # (2) 얼굴 영역의 크기를 기준으로 icon의 크기와 mask의 크기를 resize 한다.

    # for (x, y, w, h) in faces:

    # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 얼굴 영역에 mask 이용해서 face_mask 덮어쓰기

    return frame


web_cam.play(process)


# print(os.getcwd())

# path = '../face_mask.png'
# print(os.path.exists(path))
