# SocialDetection.py
# Authors: Nguyen Ngoc Lan Phuong <19520227@gm.uit.edu.vn>
#          Cao Hung Phu           <19520214@gm.uit.edu.vn>
#          Le Quang Nha           <19520195@gm.uit.edu.vn>

# %%
import argparse
import cv2
import torch
import math

THRESHOLD       = 120

# %%
# Lấy model của yolo từ thư viện torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.classes = [0] # Person
model.conf    = 0.45

def getBoundingBoxs(image):
  results = model(image).pandas().xyxy.pop()
  return [(
    (int(box['xmin']), int(box['ymin'])), # Top-left point
    (int(box['xmax']), int(box['ymax'])), # Bottom-right point
  ) for _, box in results.iterrows()]

# %%
# Hàm hỗ trợ vẽ
def drawBoundingBox(image, boxes, color):
  for topLeft, bottomRight in boxes:
    cv2.rectangle(image, topLeft, bottomRight, color, 2, cv2.LINE_AA)

def drawCentroid(image, points):
  for point in points:
    cv2.circle(image, point, 3, (184, 162, 23), 2, cv2.LINE_AA)

# %%
# Hàm hỗ trợ tính toán
def getCentroids(boxes):
  centroids = []
  for topLeft, bottomRight in boxes:
    x = (topLeft[0] + bottomRight[0]) / 2
    y = (topLeft[1] + bottomRight[1]) / 2
    centroids.append((int(x), int(y)))
  return centroids

def getDistance(pointA, pointB):
  return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)

def getViolateStatus(boxes, points):
  danger = [ ]
  for u in range(len(points)):
    for v in range(u + 1, len(points)):
      distance = getDistance(points[u], points[v])
      if distance < THRESHOLD:
        if boxes[u] not in danger: danger.append(boxes[u])
        if boxes[v] not in danger: danger.append(boxes[v])
  safe = list(set(boxes) - set(danger))
  return danger, safe

# %%
def validImageSize(imageSize):
  """480p"""
  return imageSize >= 768 * 480

def getResult(image):
  image = image.copy()
  boxes = getBoundingBoxs(image)
  centroids = getCentroids(boxes)

  # Lấy kết quả
  dangerBoxes, safeboxes = getViolateStatus(boxes, centroids)
  colorDanger, colorSafe = (114, 111, 247), (139, 231, 139)

  # Vẽ centroid và bounding box
  drawCentroid(image, centroids)
  drawBoundingBox(image, safeboxes, colorSafe)
  drawBoundingBox(image, dangerBoxes, colorDanger)

  # notice = 'Number of people: {}'.format(len(dangerBoxes))
  # image = Image.fromarray(image)
  # drawer = ImageDraw.Draw(image)
  # drawer.text((32, 32), notice, (1, 83, 183), DEFAULT_FONT)
  # return np.array(image)

  # Vẽ text
  notice = 'So nguoi vi pham khoang cach: {}'.format(len(dangerBoxes))
  location = (2, image.shape[0] - 30)
  image = cv2.putText(image, notice, location, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

  return image

# %%
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str, default='Testcases/SampleV.mp4')
  parser.add_argument('--output', type=str, default='Results/SampleV.avi')

  args = parser.parse_args()
  imFilename = args.input
  omFilename = args.output

  imReader = cv2.VideoCapture(imFilename)
  frWidth  = int(imReader.get(cv2.CAP_PROP_FRAME_WIDTH))
  frHeight = int(imReader.get(cv2.CAP_PROP_FRAME_HEIGHT))
  frNumber = int(imReader.get(cv2.CAP_PROP_FRAME_COUNT))  # aka Number of frames
  frPS     = imReader.get(cv2.CAP_PROP_FPS)               # aka Frame per second

  print('=== CAPTURE INFOMATION ===')
  print('Filename        : {}'.format(imFilename))
  print('Frame size      : {} x {}'.format(frWidth, frHeight))
  print('Number of frame : {}'.format(frNumber))
  print('Frame per second: {}'.format(frPS))

  if not validImageSize(frWidth * frHeight):
    raise 'Oops! What a lovely bug: Image quality lower than 480p'

  imWriter = cv2.VideoWriter(omFilename, cv2.VideoWriter_fourcc(*'XVID'), frPS, (frWidth, frHeight))
  for frIndex in range(frNumber):
    _, image = imReader.read()
    if not _: raise 'Oops! What a lovely bug: Fail to capture image'

    image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
    image = getResult(image)
    # imWriter.write(image)
    # print('\r>>>', frIndex + 1, 'of', frNumber, end='')

    cv2.imshow('SocialDetection.py', image)
    cv2.waitKey(int(1000 / frPS))

# %%
