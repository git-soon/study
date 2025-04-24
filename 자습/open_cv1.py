# import cv2
# # print(cv2.__version__)  # 깔려있는 opcv 버전 확인


# # 이미지 읽기 => imread(파일명,[옵션]) 파일명은 영문이나 숫자
# # 옵션 : cv2.IMREAD_COLOR(이미지를 컬러로 읽음, 기본값)
# # cv2.IMREAD_GRAYSCALE: 이미지를 흑백으로 읽음

# # 이미지 표시 => imshow('(내가 지정할)사진제목', 파일명)

# # 창이 닫히지 않게 유지하기 = cv2.waitKey(0), cv2.destroyAllWindows()
# # cv2.waitKey(delay) => 키보드 입력을 기다림, 2000 -> 2초,  0은 ‘무한대기
# # cv2.destroyAllWinows() =>  모든 창을 닫음
# #  cv2.destroyWinow(winname) => 지정된 창을 닫음,  winname : 닫을 창의 이름

# # 이미지 저장 => imwrite('파일명', 저장할 파일)
# # 파일명.jpg(= jpeg 이미지(손실 압축))
# # 파일명.png(= png 이미지(무손실 압축))
# # 파일명.bmp(= BNP 이미지(비압축 압축))
# # 파일명.tiff(= tiff 이미지(무손실/손실 압축 압축 가능))


# # .shape  (높이, 너비, 채널 수)
# # 채널(channel) – 흑백 이미지는 하나의 채널(밝기라고 생각해도 됨)
# #                 컬러 이미지의 경우에는 빨간색, 초록색, 파란색의 총 3개의 채널을 가짐

# # .dtype 데이터 타입 => uint8: 0~255 범위의 정수값을 가진 8비트 배열 (기본값)

# # 실습 1
# # image의 shape을 출력하시요.
# # image array의 행의 절반을 slicing 하시요.
# # slicing한 결과를 imshow()로 출력하시요
# mowe = cv2.imread('../cat.jpg')
# # g_mowe = cv2.cvtColor(mowe, cv2.COLOR_BGR2RGBA)
# # gray_mowe = cv2.cvtColor(mowe, cv2.COLOR_RGB2GRAY)
# # cv2.imshow('cat', mowe)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(mowe)

# # 사진은 정적이라 스태틱에 지정해라?


print(__file__)
