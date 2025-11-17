import cv2
import time
import pyautogui
import numpy as np
from PIL import ImageGrab

def screenRecorder():
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1920, 1080))
    
    print("Recording started... ESC to stop.")
    time.sleep(3)

    cv2.namedWindow("LIVE PREVIEW - DO NOT MAXIMIZE", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("LIVE PREVIEW - DO NOT MAXIMIZE", 400, 225)
    
    while True:
        img = ImageGrab.grab()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        small_frame = cv2.resize(frame, (400, 225))
        cv2.imshow("Preview", small_frame)
        cv2.moveWindow("Preview", screen_size[0]-420, 0)
        
        if cv2.waitKey(1) == 27:  # Escape key
            break

    out.release()
    cv2.destroyAllWindows()

screenRecorder()