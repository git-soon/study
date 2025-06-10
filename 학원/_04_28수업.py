import cv2
import web_cam
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# icon mask 만들기
# 3. face_mask 읽기 -> icon 사용
icon = cv2.imread('face_mask.png')

# 4. face_mask에 contour 찾기
# - 전처리: 흑백 -> 이진화 -> findContours()
gray_icon = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)
gray_icon = 255 - gray_icon
_, bin_icon = cv2.threshold(gray_icon, 50, 255, cv2.THRESH_BINARY)

# 5. contour로 mask 만들기
contours, _ = cv2.findContours(
    bin_icon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(gray_icon)
cv2.drawContours(mask, contours, -1, 255, -1)


def process(frame):

    # 1. 얼굴인식
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=3, minSize=(70, 70))

    # 2. 얼굴마다 작업 진행
    for (x, y, w, h) in faces:

        # 3 ~ 4. icon과 mask를 global 영역에서 구함

        # 6. 얼굴영역에 mask이용해서 icon 덮어쓰기
        # (1) frame 직접 그릴수는 없기 때문에, 얼굴 영역을 우선 찾는다.
        roi = frame[y:y+h, x:x+w]

        # (2) 얼굴 영역의 크기를 기준으로 icon의 크기와 mask의 크기를 resize한다.
        r_icon = cv2.resize(icon, (w, h))
        r_mask = cv2.resize(mask, (w, h))

        cv2.imshow('r_icon', r_icon)
        cv2.imshow('r_mask', r_mask)

        # (3) roi에다가 r_icon을 r_mask를 이용하여 복사한다.
        roi[r_mask == 255] = r_icon[r_mask == 255]

    return frame


web_cam.play(process)
