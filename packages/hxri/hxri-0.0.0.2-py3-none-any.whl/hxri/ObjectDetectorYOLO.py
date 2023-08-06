class ObjectDetectorYOLO():

    import numpy as np
    import time


    def __init__(self, classes, path_deep_model, config = {"inpWidth":320,"inpHeight":320,"confThreshold":0.5, "nmsThreshold":0.5},  use_gpu = False, fix_index = False):
        self.classes = classes
        self.config = config
        self.fix_index = fix_index
        self.confThreshold = config["confThreshold"]
        self.nmsThreshold =  config["nmsThreshold"]

        print("[INFO] Loading model...")

        modelConfiguration = path_deep_model + "/model.cfg";
        modelWeights = path_deep_model + "/model.weights";

        self.net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        if use_gpu:
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
            print("[INFO] Using GPU...")
        else:
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) # DNN_TARGET_OPENCL_FP16,DNN_TARGET_OPENCL,DNN_TARGET_CPU = 0
            print("[INFO] Using CPU...")

        print("[INFO] DL model ready...")


    def _getOutputsNames(self, net):
        # Get the names of all the layers in the network
        layersNames = net.getLayerNames()
        if(self.fix_index == True):
            # Get the names of the output layers, i.e. the layers with unconnected outputs
            return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        else:
            # Get the names of the output layers, i.e. the layers with unconnected outputs
            return [layersNames[i-1] for i in net.getUnconnectedOutLayers()]

    # Remove the bounding boxes with  low confidence using non-maxima suppression
    def _postprocess(self, frame, outs):
        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]

        classIds = []
        confidences = []
        boxes = []
        # Scan through all the bounding boxes output from the network and keep only the
        # ones with high confidence scores. Assign the box's class label as the class with the highest score.
        classIds = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    classIds.append(classId)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

        # Perform non maximum suppression to eliminate redundant overlapping boxes with
        # lower confidences.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confThreshold, self.nmsThreshold)
        #list_labels = []
        #list_index = []
        detected = []


        for i in indices:
            index = i
            try:
                index = i[0]
            except:
                index = i
                pass
            box = boxes[index]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]

            if confidences[index] > 0.5:
                label = self.classes[classIds[index]]
                position = [left + width/2, top + height/2]
                #list_index.append(classIds[i])
                #list_labels.append(label)
                detected.append({"label":label,"center":{"x":int(position[0]), "y":int(position[1])}, "box":{"x":left, "y":top, "w":width, "h":height}, "confidence":confidences[index]})
        return detected

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
    
    def getObjects(self, img):

        blob = cv2.dnn.blobFromImage(img, 1/255, (self.config["inpWidth"], self.config["inpHeight"]), [0,0,0], 1, crop=False)
        
        # Sets the input to the network
        self.net.setInput(blob)
        
        # Runs the forward pass to get output of the output layers
        outs = self.net.forward(self._getOutputsNames(self.net))
     
        # Remove the bounding boxes with low confidence
        self.detected = self._postprocess(img, outs)

        return self.detected



"""
import os
os.environ['PATH'] = 'C:/nep/opencv_cuda' + os.pathsep + os.environ['PATH']
import cv2

path_deep_model = 'C:/nep/deep_models/objects/yolo4' 
classesFile = path_deep_model + "/model.names"

classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')
print(classes)

y = ObjectDetectorYOLO(classes, path_deep_model);

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

        print(data)
        
        cv2.imshow("Result", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q') or key == 0x1b:
            break

cap.release()
"""