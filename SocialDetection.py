# SocialDetection
# Authors: Nguyen Ngoc Lan Phuong <19520227@gm.uit.edu.vn>
#          Cao Hung Phu           <19520214@gm.uit.edu.vn>
#          Le Quang Nha           <19520195@gm.uit.edu.vn>

# %% Import library
import cv2
import torch
import math

# %% Main SocialDetection
class SocialDetection:
    # Init Threshold + Model  
    def __init__(self, threshold):
        self.threshold = threshold
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.model.classes = [0] # Person
        self.model.conf    = 0.45
    
    # Check ImageSize
    def validImageSize(self, imageSize):
        """480p"""
        return imageSize >= 768 * 480    
        
    # Get BoundingBoxs
    def getBoundingBoxs(self, image):
        results = self.model(image).pandas().xyxy.pop()
        return [(
        (int(box['xmin']), int(box['ymin'])), # Top-left point
        (int(box['xmax']), int(box['ymax'])), # Bottom-right point
        ) for _, box in results.iterrows()]
    
    # Get Centroids
    def getCentroids(self, boxes):
        centroids = []
        for topLeft, bottomRight in boxes:
            x = (topLeft[0] + bottomRight[0]) / 2
            y = (topLeft[1] + bottomRight[1]) / 2
            centroids.append((int(x), int(y)))
        return centroids
    
    # Get Distance
    def getDistance(self, pointA, pointB):
        return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)

    # Get ViolateStatus
    def getViolateStatus(self, boxes, points):
        danger = [ ]
        for u in range(len(points)):
            for v in range(u + 1, len(points)):
                distance = self.getDistance(points[u], points[v])
                if distance < self.threshold:
                    if boxes[u] not in danger: danger.append(boxes[u])
                    if boxes[v] not in danger: danger.append(boxes[v])
                safe = list(set(boxes) - set(danger))
        return danger, safe       
    
    # Draw BoundingBox    
    def drawBoundingBox(self, image, boxes, color):
        for topLeft, bottomRight in boxes:
            cv2.rectangle(image, topLeft, bottomRight, color, 2, cv2.LINE_AA)
        
    # Draw Centroid
    def drawCentroid(self, image, points):
        for point in points:
            cv2.circle(image, point, 3, (184, 162, 23), 2, cv2.LINE_AA)
                 
    # Get Result
    def getResult(self, image):
        image = image.copy()
        boxes = self.getBoundingBoxs(image)
        centroids = self.getCentroids(boxes)

        # Lấy kết quả
        dangerBoxes, safeBoxes = self.getViolateStatus(boxes, centroids)
        colorDanger, colorSafe = (114, 111, 247), (139, 231, 139)

        # Vẽ centroid và bounding box
        self.drawCentroid(image, centroids)
        self.drawBoundingBox(image, safeBoxes, colorSafe)
        self.drawBoundingBox(image, dangerBoxes, colorDanger)

        # Vẽ text
        notice = 'So nguoi vi pham khoang cach: {}'.format(len(dangerBoxes))
        location = (2, image.shape[0] - 30)
        image = cv2.putText(image, notice, location, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        return image
