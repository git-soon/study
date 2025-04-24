import cv2

print(cv2.__version__)  # cv2 버전체크

# image 읽기 => imread
# cv2.IMREAD_COLOR: 이미지를 컬러(BGR)로 읽음 (기본값)
image = cv2.imread('../cat.jpg')

# cv2.IMREAD_GRAYSCALE: 이미지를 흑백으로 읽음
gray_image = cv2.imread('../cat.jpg', cv2.IMREAD_GRAYSCALE)


# image 새창으로 열기
# 이미지 파일 컬러로 열기(기본값)
# cv2.imshow('cat', image)

# 이미지 파일 흑백으로 열기
# cv2.imshow('gray_cat', gray_image)

print(image.shape)  # (668, 1000, 3) 가로,세로 , 차원(rgb 3개 다쓰니까 3차원!)
print(image.dtype)
print(gray_image.shape)
print(gray_image.dtype)

# 윈도우가 닫히지 않게 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()

# # image 저장
# cv2.imwrite('cat_gray.jpg', gray_image)


# 실습 1
# 1. image의 shape을 출력하시요.
print(image.shape)

# 2. image array의 행의 절반을 slicing 하시요.
h_image = image[334:]

# 2-1. image array의 열의 절반을 slicing
image = gray_image[:, 500:]

# 3. slicing한 결과를 imshow()로 출력하시요
cv2.imshow('cat', h_image)

cv2.imshow('cat', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# # 추가. 1/4 로 자르게
# image = image[334:, 500:]
# cv2.imshow('cat', image)


# # 크기 조정(폭 300, 높이 200)
# resized_image = cv2.resize(image, (300, 200))  # shape 찍어보면 (200,300,3)나온다
# cv2.imshow('cat', resized_image)
# # 그 이유는 사진은 가로 X 세로 이지만 numpy는 행 렬 이라 그렇다.
# print(resized_image.shape)

# # 가로/세로 비율로 크기 조정
# scale = 0.5  # 50%
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 실습 2
# 1.cat image를 50 % 크기로 축소하고 새로운 창에 표시하세요.
scale = 0.5  # 50%
resized_image2 = cv2.resize(image, None, fx=scale, fy=scale)
cv2.imshow('cat', resized_image2)


# 2.이미지를 90도 회전하여 저장하세요
(h, w) = image.shape[:2]
center = (w//300, h//200)  # 중심좌표

# 90도 회전, 배율 1.0
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))


# 실습3 cat image의 하단 절반(image[338:])을 흑백으로 변환하시요
# 1. 이미지 하단 구하고
# 2. 구한것을 흑백으로 변경하고
# 3. 다시 형식을 컬러로 변경
# 4. 원본 이미지에 흑백으로 변경한 부분을 붙여넣기

# 이미지 하단 절반 구하기
# bottom_half = image[334:]

# # 하단 절반을 흑백으로 변환
# bottom_half_gray = cv2.cvtColor(bottom_half, cv2.COLOR_BGR2GRAY)

# # 흑백 이미지를 다시 컬러로 변경
# bottom_half_gray_colored = cv2.cvtColor(bottom_half_gray, cv2.COLOR_GRAY2BGR)

# # 원본 이미지에 흑백으로 변경한 부분 붙여넣기
# image[334:] = bottom_half_gray_colored

# # 결과 출력
# cv2.imshow('cat', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# open cv로 비디오 파일 출력

# 동영상 파일 경로 설정 (파일 이름은 업로드된 파일로 대체)
# video_path = "video.mp4"


# # 비디오 캡쳐 객체 생성
# cap = cv2.VideoCapture(video_path)

# print(cap.isOpened())

# # 동영상 재생
# while cap.isOpened():  # 비디오 캡쳐 객체가 열려있는 동안 반복

#     ret, frame = cap.read()  # 프레임 읽기

#     if not ret:  # 프레임을 더 이상 읽을 수 없으면 종료
#         print("비디오 재생 완료")
#         break

#     cv2.imshow('Video', frame)  # 프레임 표시

#     # 속도 조절(프레임 사이에 잠시 대기)
#     if cv2.waitKey(0) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
#         break

# # 캡쳐 객체 해제
# cap.release()  # 비디오 캡쳐 객체 해제
# cv2.destroyAllWindows()  # 모든 윈도우 닫기


# # 웹 캠으로 사진 찍기
# 웹캠 캡쳐 객체 생성
# cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미 # 0

# if cap.isOpened():
#     while True:
#         ret, img = cap.read()
#         if ret:
#             cv2.imshow('camera', img)
#             if cv2.waitKey(10) != -1:
#                 break

# else:
#     print("can't open camera")
# cap.release()
# cv2.destroyAllWindows()
