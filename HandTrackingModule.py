import cv2
import mediapipe as mp


class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param maxHands: Maximum number of hands to detect
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectionCon, min_tracking_confidence=self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}
                ## lmList
                mylmList = []
                myPointslist=[]
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])
                    myPointslist.append((px,py))
                    xList.append(px)
                    yList.append(py)

                ## bounding Box
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] = (cx, cy)

                if flipType:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

                ## draw
                if draw:
                    # self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

                    for i in range(21):
                        if(0<=i<=3):
                            img=cv2.line(img,myPointslist[i],myPointslist[i+1],(0,200,200),3) 
                            img=cv2.circle(img,myPointslist[i],3,(0,200,200),3)
                            img=cv2.circle(img,myPointslist[4],3,(0,200,200),3)

                        if(5<=i<=7):
                            img=cv2.line(img,myPointslist[i],myPointslist[i+1],(0,200,0),3) 
                            img=cv2.line(img,myPointslist[0],myPointslist[5],(0,200,0),3)
                            img=cv2.circle(img,myPointslist[i],3,(0,200,0),3)
                            img=cv2.circle(img,myPointslist[8],3,(0,200,0),3)

                        if(9<=i<=11):
                            img=cv2.line(img,myPointslist[i],myPointslist[i+1],(0,0,200),3) 
                            img=cv2.line(img,myPointslist[0],myPointslist[9],(0,0,200),3)
                            img=cv2.circle(img,myPointslist[i],3,(0,0,200),3)
                            img=cv2.circle(img,myPointslist[12],3,(0,0,200),3)

                        if(13<=i<=15):
                            img=cv2.line(img,myPointslist[i],myPointslist[i+1],(200,0,0),3) 
                            img=cv2.line(img,myPointslist[0],myPointslist[13],(200,0,0),3)
                            img=cv2.circle(img,myPointslist[i],3,(200,0,0),3)
                            img=cv2.circle(img,myPointslist[16],3,(200,0,0),3)

                        if(17<=i<=19):
                            img=cv2.line(img,myPointslist[i],myPointslist[i+1],(200,0,200),3) 
                            img=cv2.line(img,myPointslist[0],myPointslist[17],(200,0,200),3) 
                            img=cv2.circle(img,myPointslist[i],3,(200,0,200),3)
                            img=cv2.circle(img,myPointslist[20],3,(200,0,200),3)
                            
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (255, 0, 255), 2)
                    cv2.putText(img, myHand["type"], (bbox[0] - 30, bbox[1] - 30), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 0, 255), 2)
        if draw:
            return allHands, img
        else:
            return allHands

