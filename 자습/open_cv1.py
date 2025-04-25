import cv2
import numpy as np
# print(cv2.__version__)  # 깔려있는 opcv 버전 확인


# 이미지 읽기 => imread(파일명,[옵션]) 파일명은 영문이나 숫자
# 옵션 : cv2.IMREAD_COLOR(이미지를 컬러로 읽음, 기본값)
# cv2.IMREAD_GRAYSCALE: 이미지를 흑백으로 읽음

# 이미지 표시 => imshow('(내가 지정할)사진제목', 파일명)

# 창이 닫히지 않게 유지하기 = cv2.waitKey(0), cv2.destroyAllWindows()
# cv2.waitKey(delay) => 키보드 입력을 기다림, 2000 -> 2초,  0은 ‘무한대기
# cv2.destroyAllWinows() =>  모든 창을 닫음
#  cv2.destroyWinow(winname) => 지정된 창을 닫음,  winname : 닫을 창의 이름

# 이미지 저장 => imwrite('파일명', 저장할 파일)
# 파일명.jpg(= jpeg 이미지(손실 압축))
# 파일명.png(= png 이미지(무손실 압축))
# 파일명.bmp(= BNP 이미지(비압축 압축))
# 파일명.tiff(= tiff 이미지(무손실/손실 압축 압축 가능))


# .shape  (높이, 너비, 채널 수)
# 채널(channel) – 흑백 이미지는 하나의 채널(밝기라고 생각해도 됨)
#                 컬러 이미지의 경우에는 빨간색, 초록색, 파란색의 총 3개의 채널을 가짐

# .dtype 데이터 타입 => uint8: 0~255 범위의 정수값을 가진 8비트 배열 (기본값)

# 실습 1
# image의 shape을 출력하시요.
# image array의 행의 절반을 slicing 하시요.
# slicing한 결과를 imshow()로 출력하시요

mowe = cv2.imread('../cat.jpg')
# g_mowe = cv2.cvtColor(mowe, cv2.COLOR_BGR2RGBA)
# gray_mowe = cv2.cvtColor(mowe, cv2.COLOR_RGB2GRAY)
# cv2.imshow('cat', mowe)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


print(mowe.shape)  # shape (668, 1000, 3) : 행(높이), 열(너비), 차원수(채널수 : RGB 3채널 이미지를 의미)
# 사진은 정적이라 스태틱에 지정해라?

# 행, 열 슬라이싱

# # 행 절반만 표시
# x_mowe = mowe[334:]

# # 열 절반만 표시
# y_mowe = mowe[:, 500:]

# cv2.imshow('harf', x_mowe)
# cv2.imshow('another', y_mowe)

# 따라서 사진의 원하는 부분만 표시하려면 픽셀 슬라이싱을 하면된다.

# 크기 조절은 아래와 같다

# # 1. 크기 직접 조정(폭 300, 높이 200)
# resized_image1 = cv2.resize(mowe, (300, 200))
# cv2.imshow('cat', resized_image1)

# # shape 찍어보면 (200,300,3)나온다
# # 그 이유는 사진은 가로 X 세로 이지만 numpy는 행 렬 이라 그렇다.
# print(resized_image1.shape)

# # 2. 크기 비율 조정
# scale = 0.5 #50 %
# resized_image2 = cv2.resize(mowe, None, fx=scale,fy=scale)
# cv2.imshow('cat', resized_image1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 이미지 자르기 및 관심 영역(ROI) 처리
# 주의!!! ROI는 원본 이미지와 메모리를 공유하기때문에 ROI를 수정하면 원본 이미지도 변경됨.
# 복사본을 만들고 싶다면 copy()를 사용

roi_copy = mowe[100:200, 300:500].copy()


# 이미지 회전 및 이동 => warpAffine() : 이미지를 회전하거나 이동하기 위해 변환 행렬을 사용
image = cv2.imread('../campfood.jpg')
(h, w) = image.shape[:2]
center = (w//2, h//2)  # 중심 좌표

# 45도 회전, 배율 1.0
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
# 첫번째 인자(center) :회전 중심
# 두번째 인자(45) : 회전 각도(시계 반대 방향)
# 세번째 인자 (1.0): 확대/축소 비율(1이면 크기 유지)

rotated_image = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('rotated', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 이동
matrix = np.float32(([1, 0, 100], [0, 1, 50]))
# 이동 행렬: [[1, 0, x], [0, 1, y]]
# 여기서는 x축으로 100px, y축으로 50px 이동

sgifted_image = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('move', sgifted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 실습 2
# 1.cat image를 50 % 크기로 축소하고 새로운 창에 표시
# 2.이미지를 90도 회전하여 저장

# 1.cat image를 50 % 크기로 축소하고 새로운 창에 표시
scale = 0.5
h_moew = cv2.resize(mowe, None, fx=scale, fy=scale)
cv2.imshow('harp_size', h_moew)

# 2.이미지를 90도 회전하여 저장
(h, w) = mowe.shape[:2]
center = (w//2, h//2)  # 중심 좌표
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_cat = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('rotated', rotated_cat)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 실습 3
#  cat image의 하단 절반(image[338:])을 흑백으로 변환
# -> 하단 절반 잘라서 그레이 스케일, 그리고 원본에 붙이기


# import os
# print(__file__)
# here = os.getcwd()
# print("here", here)
