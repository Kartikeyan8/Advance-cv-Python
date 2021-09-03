import cv2
import mediapipe as m
import time
class HandDetect()
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5)
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mhands = m.solutions.hands
        # take hands
        self.hands = self.mhands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mdraw = m.solutions.drawing_utils
    def findhands(self,ima)
        imgRGB = cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
        result = self.hands.process(imgRGB)
        if result.multi_hand_landmarks
            for handslms in result.multi_hand_landmarks
                h, w, c = ima.shape
                cx, cy = int(lms.x  w), int(lms.y  h)
                print(id, cx, cy)
                if id in range(9, 12)
                    cv2.circle(ima, (cx, cy), 15, (255, 5, 25), cv2.FILLED)

                    self.mdraw.draw_landmarks(ima, handslms, self.mhands.HAND_CONNECTIONS)
        return ima
def main()
    ptime = 0
    ctime = 0
    captureme = cv2.VideoCapture(0)
    detector=HandDetect()
    while True
        success, ima = captureme.read()
        ima=detector.findhands(ima)

        ctime = time.time()
        fps = 1  (ctime - ptime)
        ptime = ctime
        cv2.putText(ima, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (25, 8, 255), 5)
        cv2.imshow(hj, ima)
        if cv2.waitKey(1) & 0xFF == ord('q')
            break
if __name__==main
  main()
