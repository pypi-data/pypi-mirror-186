import cv2
import numpy as np
import math

class MediapipeBody():

    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        import mediapipe as mp
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)
        self.skeleton_detection = self.mp_pose.Pose(static_image_mode=True,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles


    def drawBody(self, image_src):
        new_image = image_src.copy()
        self.mp_drawing.draw_landmarks(
            new_image,
            self.hand_results.pose_landmarks,
            self.mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())


        return new_image
    
  
    def getBody(self, image_src):
        image_src.flags.writeable = False
        image_src = cv2.cvtColor(image_src, cv2.COLOR_BGR2RGB)
        self.hand_results = self.skeleton_detection.process(image_src)
        y_resolution, x_resolution, c = image_src.shape

        # Draw the pose annotation on the image.
        image_src.flags.writeable = True
        image_src = cv2.cvtColor(image_src, cv2.COLOR_RGB2BGR)

        list_pose = ["NOSE",
            "LEFT_EYE_INNER",
            "LEFT_EYE",
            "LEFT_EYE_OUTER",
            "RIGHT_EYE_INNER",
            "RIGHT_EYE",
            "RIGHT_EYE_OUTER",
            "LEFT_EAR",
            "RIGHT_EAR",
            "MOUTH_LEFT",
            "MOUTH_RIGHT",
            "LEFT_SHOULDER",
            "RIGHT_SHOULDER",
            "LEFT_ELBOW",
            "RIGHT_ELBOW",
            "LEFT_WRIST",
            "RIGHT_WRIST",
            "LEFT_PINKY",
            "RIGHT_PINKY",
            "LEFT_INDEX",
            "RIGHT_INDEX",
            "LEFT_THUMB",
            "RIGHT_THUMB",
            "LEFT_HIP",
            "RIGHT_HIP",
            "LEFT_KNEE",
            "RIGHT_KNEE",
            "LEFT_ANKLE",
            "RIGHT_ANKLE",
            "LEFT_HEEL",
            "RIGHT_HEEL",
            "LEFT_FOOT_INDEX",
            "RIGHT_FOOT_INDEX"]

        init_value = {"x":0,"y":0, "p":0}
        pose_values = {};

        for element in list_pose:
            pose_values[element] = init_value
            #print(element)
            try:
                value = self.hands_results.pose_landmarks.landmark[self.mp_pose.PoseLandmark[element]]
                value.x, value.y = self._normalized_to_pixel_coordinates(value.x, value.y, x_resolution,y_resolution)
                pose_values[element] = {"x":value.x,"y":value.y, "p":1}
            except:
                pass
    
        return pose_values

    def _normalized_to_pixel_coordinates(self, normalized_x, normalized_y, image_width,image_height):

      x_px = min(math.floor(normalized_x * image_width), image_width - 1)
      y_px = min(math.floor(normalized_y * image_height), image_height - 1)
      
      return x_px, y_px