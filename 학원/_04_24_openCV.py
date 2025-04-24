import cv2

# # .py 파일과 동일한 경로에 .xml 파일을 저장하고 파일을 로딩
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # 이미지 로드
# image = cv2.imread('face.png')

# # 그레이스케일로 변환
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 얼굴 탐지
# faces = face_cascade.detectMultiScale(
#     gray_image,
#     scaleFactor=1.1,
#     minNeighbors=3,
#     minSize=(30, 30)
# )

# # 탐지된 얼굴에 사각형 그리기
# for i, (x, y, w, h) in enumerate(faces):
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     print(w, h)


# # 결과 이미지 표시
# cv2.imshow('face', image)
# cv2.waitKey(0)


# 얼굴
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 눈
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

# 웹캠 초기화
cap = cv2.VideoCapture(0)  # 웹캠 캡쳐 객체 생성
# cap = cv2.VideoCapture('video.mp4')  # 비디오 파일 캡쳐 객체 생성 (비디오 파일 경로를 지정하세요)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        print(("웹캠에서 프레임을 읽을 수 없습니다."))
        break  # 프레임을 더 이상 읽을 수 없으면 종료

    # 그레이 스케일 변환   # cv2.imshow('frame', frame)  # 원본 프레임 표시
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 탐지
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # , cv2.IMREAD_UNCHANGED)  # 이모티콘 이미지 로드 (투명 배경을 지원하는 PNG)
    face_mask = cv2.imread('face_mask.png')

    # 탐지된 얼굴에 mask 그리기
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # print(w, h)
        roi_gray = gray_frame[y:y+h, x: x+w]
        roi_color = frame[y:y+h, x: x+w]

        # 눈
        eyes = eye_cascade.detectMultiScale(
            roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('face and Eye Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
        break                              # waitkey :
    # #이모티콘

    # # 이모티콘 사이즈 조정
    # face_mask_resized = cv2.resize(face_mask, (w, h))

    # # 이모티콘의 위치 조정
    # x_offset = x

    # y_offset = y

    # frame[y_offset:y_offset+h, x_offset:x_offset+w] = face_mask_resized
    # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # cv2.imshow('Face Mask', frame)  # 결과 이미지 표시
    # cv2.waitKey(1)  # 1ms 대기

    # 이모티콘 표시
    # cv2.destroyAllWindows()  # 모든 윈도우 닫기
    #


# 실습 2  웹캠 영상에 얼굴이 나오는 경우, 아이콘으로 가려서 출력하라
# 탐지된 얼굴 사이즈 만큼 이모티콘을 불러온다?
# 불러온 이모지에 흰색 배경을 제거하고 표시한다?
# 이모지의 사이즈를 조정하고, 얼굴에 맞춰서 위치를 조정한다.
# 이모지의 위치를 조정하고, 이모지를 표시한다.

    # # 탐지된 얼굴 그리기
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 얼굴에 사각형 그리기

    # cv2.imshow('Face Detection', frame)  # 결과 이미지 표시
