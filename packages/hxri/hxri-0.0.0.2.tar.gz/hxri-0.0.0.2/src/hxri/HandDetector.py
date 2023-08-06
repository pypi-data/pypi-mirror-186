import cv2
import numpy as np

def points2vector(tail, head):
    return (np.array(head) - np.array(tail))

def getAngle(vector1, vector2):
    inner_product = np.inner(vector1, vector2)
    norm_v1 = np.linalg.norm(vector1)
    norm_v2 = np.linalg.norm(vector2)

    if norm_v1 == 0.0 or norm_v2 == 0.0:
        return np.nan
    cos = inner_product / (norm_v1*norm_v2)
    # result in radians
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    # covert to degrees
    theta = np.rad2deg(rad)


class MediapipeHand():

    def __init__(self, max_num_hands=2,min_detection_confidence=0.7, min_tracking_confidence=0.7):
        import mediapipe as mp
        self.mp_hands = mp.solutions.hands


        self.landmark_line_ids = [ 
            (0, 1), (1, 5), (5, 9), (9, 13), (13, 17), (17, 0),  
            (1, 2), (2, 3), (3, 4),        
            (5, 6), (6, 7), (7, 8),        
            (9, 10), (10, 11), (11, 12),   
            (13, 14), (14, 15), (15, 16),  
            (17, 18), (18, 19), (19, 20),   
        ]

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_num_hands,min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)

        self.HAND_KEYPOINTS = ["WRIST",
          "THUMB_CMC",
          "THUMB_MCP" ,
          "THUMB_IP",
          "THUMB_TIP",
          "INDEX_FINGER_MCP",
          "INDEX_FINGER_PIP",
          "INDEX_FINGER_DIP",
          "INDEX_FINGER_TIP",
          "MIDDLE_FINGER_MCP",
          "MIDDLE_FINGER_PIP",
          "MIDDLE_FINGER_DIP",
          "MIDDLE_FINGER_TIP",
          "RING_FINGER_MCP",
          "RING_FINGER_PIP",
          "RING_FINGER_DIP",
          "RING_FINGER_TIP",
          "PINKY_MCP",
          "PINKY_PIP",
          "PINKY_DIP",
          "PINKY_TIP"]

        self.dict_points = {"WRIST":{},"THUMB_CMC":{},"THUMB_MCP":{},
          "THUMB_IP":{},"THUMB_TIP":{},
          "INDEX_FINGER_MCP":{},"INDEX_FINGER_PIP":{},
          "INDEX_FINGER_DIP":{},"INDEX_FINGER_TIP":{},
          "MIDDLE_FINGER_MCP":{},"MIDDLE_FINGER_PIP":{},
          "MIDDLE_FINGER_DIP":{},"MIDDLE_FINGER_TIP":{},
          "RING_FINGER_MCP":{},"RING_FINGER_PIP":{},
          "RING_FINGER_DIP":{},"RING_FINGER_TIP":{},
          "PINKY_MCP":{},"PINKY_PIP":{},
          "PINKY_DIP":{},"PINKY_TIP":{}}


        self.HAND_VECTORS = {"TWC":["WRIST", "THUMB_CMC"],
                "TCM":["THUMB_CMC", "THUMB_MCP"],
                "TMI":["THUMB_MCP", "THUMB_IP"],
                "TIT":["THUMB_IP", "THUMB_TIP"],
                "IWM":["WRIST", "INDEX_FINGER_MCP"],
                "IMP":["INDEX_FINGER_MCP", "INDEX_FINGER_PIP"],
                "IPD":["INDEX_FINGER_PIP", "INDEX_FINGER_DIP"],
                "IDT":["INDEX_FINGER_DIP", "INDEX_FINGER_TIP"],
                "MWM":["WRIST", "MIDDLE_FINGER_MCP"],
                "MMP":["MIDDLE_FINGER_MCP", "MIDDLE_FINGER_PIP"],
                "MPD":["MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP"],
                "MDT":["MIDDLE_FINGER_DIP", "MIDDLE_FINGER_TIP"],
                "RWM":["WRIST", "RING_FINGER_MCP"],
                "RMP":["RING_FINGER_MCP", "RING_FINGER_PIP"],
                "RPD":["RING_FINGER_PIP", "RING_FINGER_DIP"],
                "RDT":["RING_FINGER_DIP", "RING_FINGER_TIP"],
                "PWM":["WRIST", "PINKY_MCP"],
                "PMP":["PINKY_MCP", "PINKY_PIP"],
                "PPD":["PINKY_PIP", "PINKY_DIP"],
                "PDT":["PINKY_DIP", "PINKY_TIP"]
        }

        self.HAND_JOINTS2 = {"WRIST_THUMB_INDEX":["TWC","IWM"],
                "INDEX_MIDDLE":["IMP","MMP"],
                "WRIST_MIDDLE":["MWM","MMP"]
        }

        self.HAND_JOINTS = {"WRIST_THUMB_INDEX":["TWC","IWM"],
                "WRIST_INDEX":["IWM","IMP"],
                "INDEX_1":["IMP","IPD"],
                "INDEX_2":["IPD","IDT"],
                "WRIST_MIDDLE":["MWM","MMP"],
                "MIDDLE_1":["MMP","MPD"],
                "MIDDLE_2":["MPD","MDT"]
        }

        self.dict_joints = {"WRIST_THUMB_INDEX":np.zeros((1,3,)),
                "WRIST_THUMB":np.zeros((1,3,)),
                "THUMB_1":np.zeros((1,3,)),
                "THUMB_2":np.zeros((1,3,)),
                "WRIST_INDEX":np.zeros((1,3,)),
                "INDEX_1":np.zeros((1,3,)),
                "INDEX_2":np.zeros((1,3,)),
                "INDEX_MIDDLE":np.zeros((1,3,)),
                "WRIST_MIDDLE":np.zeros((1,3,)),
                "MIDDLE_1":np.zeros((1,3,)),
                "MIDDLE_2":np.zeros((1,3,))
        }




    def getAnglesFromVectors(self):

        Left = self.hand_vectors["Left"]
        Right = self.hand_vectors["Right"]
        score_l = self.data["scores"]["Left"]
        score_r = self.data["scores"]["Right"]

        for vector_name, value in self.HAND_JOINTS.items():
            if (score_l>.2):
                vector1 = self.hand_vectors["Left"][value[0]]
                vector2 = self.hand_vectors["Left"][value[1]]
                getAngle(vector1,vector2)
            
            if (score_r>.2):

                vector1 = self.hand_vectors["Right"][value[0]]
                vector2 = self.hand_vectors["Right"][value[1]]
                getAngle(vector1,vector2)

        return 0

    def getHandVectors(self):

        Left = self.data["data"]["Left"]
        Right = self.data["data"]["Right"]
        score_l = self.data["scores"]["Left"]
        score_r = self.data["scores"]["Right"]

        self.hand_vectors = {"Left":self.dict_joints.copy(), "Right":self.dict_joints.copy()} 

        for vector_name, points in self.HAND_VECTORS.items():
            if (score_l>.2):
                self.hand_vectors["Left"][vector_name] = points2vector(tail = Left[points[0]], head = Left[points[1]])
            if (score_r>.2):
                self.hand_vectors["Right"][vector_name] = points2vector(tail = Right[points[0]], head = Right[points[1]])

        return self.hand_vectors







    def getHands(self,img, draw_image = True):

        """ Get landmarks from hands 
        
        Parameters
        ----------

        img : cv2 image 
            OpenCV image

        draw_image : bool
            If true, draw landmarks in the image

        Returns
        ----------

        data : dict
            Hand data

        img : cv2 image
            Image with hands


        """

        img_h, img_w, _ = img.shape    
        img = cv2.flip(img, 1)

        self.data = {"data":{"Right": self.dict_points.copy(),"Left": self.dict_points.copy()}, "scores":{"Right":0,"Left":0}}
        results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for h_id, hand_landmarks in enumerate(results.multi_hand_landmarks):

                if draw_image:
                    # plot lines
                    for line_id in self.landmark_line_ids:
                        lm = hand_landmarks.landmark[line_id[0]]
                        lm_pos1 = (int(lm.x * img_w), int(lm.y * img_h))
                        lm = hand_landmarks.landmark[line_id[1]]
                        lm_pos2 = (int(lm.x * img_w), int(lm.y * img_h))
                        cv2.line(img, lm_pos1, lm_pos2, (128, 0, 0), 1)

                    # plot circles
                    z_list = [lm.z for lm in hand_landmarks.landmark]
                    z_min = min(z_list)
                    z_max = max(z_list)
                    for lm in hand_landmarks.landmark:
                        lm_pos = (int(lm.x * img_w), int(lm.y * img_h))
                        lm_z = int((lm.z - z_min) / (z_max - z_min) * 255)
                        cv2.circle(img, lm_pos, 3, (255, lm_z, lm_z), -1)

                    hand_texts = []
                    for c_id, hand_class in enumerate(results.multi_handedness[h_id].classification):
                        #hand_texts.append("#%d-%d" % (h_id, c_id)) 
                        hand_texts.append("- Index: %d" % (hand_class.index))
                        hand_texts.append("- Label: %s" % (hand_class.label))
                        #hand_texts.append("- Score:%3.2f" % (hand_class.score * 100))
                    lm = hand_landmarks.landmark[0]
                    lm_x = int(lm.x * img_w) - 50
                    lm_y = int(lm.y * img_h) - 10
                    lm_c = (104, 0, 0)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    for cnt, text in enumerate(hand_texts):
                        cv2.putText(img, text, (lm_x, lm_y + 12 * cnt), font, 0.4, lm_c, 2)

                for c_id, hand_class in enumerate(results.multi_handedness[h_id].classification):
                    index = hand_class.index
                    label = hand_class.label
                    score = hand_class.score

                    self.data["scores"][label] = score
                    
                    j = 0
                    for lm in hand_landmarks.landmark:
                        #print(self.HAND_JOINTS)
                        self.data["data"][label][self.HAND_KEYPOINTS[j]] = [lm.x*img_w,lm.y*img_h, lm.z]
                        j = j + 1
                        
        return self.data, img

"""
h = HandDetector();

cap = cv2.VideoCapture(0)  
if cap.isOpened():
    while True:
        success, img = cap.read()
        if not success:
            continue
        data, img = h.getHands(img);
        vectors = h.getHandVectors();

        print(vectors)

        cv2.imshow("Result", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q') or key == 0x1b:
            break

cap.release()
"""