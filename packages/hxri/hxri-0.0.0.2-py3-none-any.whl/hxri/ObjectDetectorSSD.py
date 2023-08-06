class ObjectDetectorSSD():
    import numpy as np
    import time

    def __init__(self, classes, path_deep_model, config = {"inpWidth":320,"inpHeight":320,"confThreshold":0.5}, fix_index = False):
        self.classes = classes
        self.config = config
        self.fix_index = fix_index
        self.confThreshold = config["confThreshold"]

        print("[INFO] Loading model...")

        self.net = cv2.dnn.readNetFromCaffe(path_deep_model + "/model.prototxt",  path_deep_model +  "/model.caffemodel")
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        print("[INFO] Model ready...")

    def getObjects(self,img):
        # Runs the detection on a frame and return bounding boxes and predicted labels
        detections = self.predict_detection(img, self.net)
        self.detected = self.proccess_prediction(img, detections, self.confThreshold)
        return self.detected

    def drawObjects(self, img_src):

        new_image = img_src.copy()

        for value in self.detected: 
            startX = value["box"]["x"] 
            startY = value["box"]["y"] 
            endX = startX + value["box"]["w"] 
            endY = startY + value["box"]["h"]
            cv2.rectangle(new_image, (startX, startY), (endX, endY),(255, 0, 0), 2)
            labelPosition = endY - 5
            cv2.putText(new_image, value["label"], (startX, labelPosition),
                    cv2.FONT_HERSHEY_DUPLEX, 0.4, (255, 255, 255), 1)

        # Put efficiency information. The function getPerfProfile returns the 
        # overall time for inference(t) and the timings for each of the layers(in layersTimes)
        t, _ = self.net.getPerfProfile()
        label = 'Inference time: %.2f ms' % (t * 1000.0 / cv2.getTickFrequency())
        cv2.putText(new_image, label, (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        return new_image



    def predict_detection(self,frame, net):
        '''
        Predict the objects present on the frame
        '''
        # Conversion to blob
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),0.007843, (300, 300), 127.5)
        #blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),0.007843, (300, 300), (127.5, 127.5, 127.5), False)
        # Detection and prediction with model
        self.net.setInput(blob)
        return self.net.forward()


    def proccess_prediction(self, frame, detections, threshold):
        '''
        Filters the predictions with a confidence threshold and draws these predictions
        '''

        detected = []
        (height, width) = frame.shape[:2]
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
        
            if confidence > threshold:
                # Index of class label and bounding box are extracted
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])

                # Retreives corners of the bounding box
                (startX, startY, endX, endY) = box.astype("int")
                label_ = "{}: {:.2f}%".format(self.classes[idx], confidence*100)
                label = self.classes[idx]
                position = [(startX + endX)/2, (startY + endY)/2]
                w = endX - startX
                h = endY - startY

                detected.append({"label":label, "center":{"x":int(position[0]), "y":int(position[1])},  "box":{"x":int(startX), "y":int(startY), "w":int(w), "h":int(h)}, "confidence":float(confidence)})

        return detected


"""
import os
os.environ['PATH'] = 'C:/nep/opencv_cuda' + os.pathsep + os.environ['PATH']
import cv2

path_deep_model = 'C:/nep/deep_models/objects/mobilenet-ssd' 
classesFile = path_deep_model + "/model.names"

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')
print(classes)

y = ObjectDetectorSSD(classes, path_deep_model);

import cv2  
import numpy as np

cap = cv2.VideoCapture(0)   
if cap.isOpened():
    while True:
        success, img = cap.read()
        if not success:
            continue

        cv2_im = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
        data  = y.getObjects(cv2_im)
        img = y.drawObjects(img)

        #print(data)
        cv2.imshow("Result", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q') or key == 0x1b:
            break

cap.release()

"""