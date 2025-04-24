from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')  # YOLO 모델 v8, n : nano 버전
# print(model.names)

image_path = ['./motocamp.jpeg', './cheers.jpeg', './campfood.jpg']

# 격체 탐지
results = model.predict(source=image_path,
                        save=False, save_txt=False, conf=0.5)
# conf: 기준을 설정하는것 (여기선 0.5이상의 것들만 선택)
# save,save_txt : 파일과 텍스트로 저장되는것

# 결과 시각화
for result in enumerate(results):

frame = result.plot()  # plot() : 탐지된 객체를 시각화한 이미지를 반환

cv2.imshow('YOLO', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
