import cv2
import numpy as np
import AirTouchModule as htm
import time
import autopy

######################
wCam, hCam = 640, 480
frameR = 100     #Frame Reduction
smoothening = 7  #random value
######################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

# print(wScr, hScr)

# Variable to store the previous state of fingers for left and right-click
prev_left_click = 0
prev_right_click = 0
holdFlag = False


def leftToggleOn(x, y):
    autopy.mouse.move(x, y)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)

def leftToggleOff():
    autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)

def caseMovement(lmList):
    global plocX, plocY, clocX, clocY
    x3 = np.interp(lmList[8][1], (frameR, wCam - frameR), (0, wScr))
    y3 = np.interp(lmList[8][2], (frameR, hCam - frameR), (0, hScr))

    # Apply increased smoothening
    clocX = plocX + (x3 - plocX) / smoothening
    clocY = plocY + (y3 - plocY) / smoothening

    autopy.mouse.move(wScr - clocX, clocY)
    plocX, plocY = clocX, clocY


while True:
    # Step1: Find the landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Step2: Get the tip of the index, middle, and ring fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger
        x2, y2 = lmList[12][1:]  # Middle finger
        x3, y3 = lmList[16][1:]  # Ring finger

        # Step3: Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # Step4: Only Index Finger: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:

            # Step5: Convert the coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Step6: Smooth Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Step7: Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # Step8: Index and middle fingers are up: Left-click Mode
        if fingers[1] == 1 and fingers[2] == 1:
            if prev_left_click == 0:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
                prev_left_click = 1
        else:
            if prev_left_click == 1:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
                prev_left_click = 0

        # Step9: Thumb is up and index finger is down: Right-click Mode
        if fingers[4] == 1 and fingers[1] == 0:
            if prev_right_click == 0:
                autopy.mouse.toggle(autopy.mouse.Button.RIGHT, True)
                prev_right_click = 1
        else:
            if prev_right_click == 1:
                autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
                prev_right_click = 0

        if len(lmList) != 0:
            # Check if index, middle, and ring fingers are up
            fingers = detector.fingersUp()
            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
                if not holdFlag:
                    holdFlag = True
                    leftToggleOn(int(lmList[8][1]), int(lmList[8][2]))  # Hold left mouse button
            else:
                if holdFlag:
                    holdFlag = False
                    leftToggleOff()  # Release left mouse button

            # If holding and dragging, move the mouse cursor
            if holdFlag:
                caseMovement(lmList)

    # Step11: Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
