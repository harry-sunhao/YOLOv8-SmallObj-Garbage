from IPython import display

display.clear_output()

import ultralytics

ultralytics.checks()

from roboflow import Roboflow
rf = Roboflow(api_key="unauthorized")
project = rf.workspace().project("taco-mqclx")
dataset = project.version(1).download("yolov8")

model = project.version(2).model

# infer on a local image
print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
ultralytics.YOLO.task