# 실습 3

import cv2

# image 읽기
image = cv2.imread('cat.jpg')
print(image.shape)

# 이미지 하단 구하기
low_img = image[334:].copy()

# 흑백으로 변경
low_img = cv2.cvtColor(low_img, cv2.COLOR_BGR2GRAY)
print(low_img.shape)    # (334, 1000)

# 다시 형식을 컬로로 변경, shape을 컬러 형식으로 변경
low_img = cv2.cvtColor(low_img, cv2.COLOR_GRAY2BGR)
print(low_img.shape)    # (334, 1000, 3)

# 원본이미지에 흑백으로 변경한 부분을 붙여넣기
image[334:, :] = low_img

cv2.imshow('cat', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
