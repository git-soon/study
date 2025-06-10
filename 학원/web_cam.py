import cv2


def play(x):
    cap = cv2.VideoCapture(0)  # 웹캠 캡쳐 객체 생성

    while True:
        ret, frame = cap.read()
        if not ret:
            print(("웹캠에서 프레임을 읽을 수 없습니다."))
            break  # 프레임을 더 이상 읽을 수 없으면 종료

        cv2.imshow('ex3', x(frame))

        if cv2.waitKey(0) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
            break                              # waitkey :

    cap.release()
    cv2.destroyAllWindows()

# def process(frame):
#     return frame        # 아무것도 안하는 함수
