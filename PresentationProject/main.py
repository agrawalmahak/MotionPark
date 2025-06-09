#
# import os
# import numpy as np
# import time
# import cv2
# import pyautogui
# import pygetwindow as gw
# import webbrowser
# from cvzone.HandTrackingModule import HandDetector
#
# # Open PowerPoint Online
# OFFICE_PPT_URL = "https://abes365-my.sharepoint.com/:p:/g/personal/preeti_21b0131210_abes_ac_in/ER4P1oYis_dEtkt76Z7CBiIBVpAxtVLcrVR-LLNax7-geQ?e=TN660I"
# webbrowser.open(OFFICE_PPT_URL)
# print("Office PowerPoint Online Opened Successfully!")
#
# time.sleep(5)
# pyautogui.hotkey("ctrl", "tab")  # Switch to PowerPoint
# time.sleep(2)
#
# ppt_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if win.visible]
#
# if ppt_windows:
#     ppt_windows[0].activate()
#     print("PowerPoint is now active!")
# else:
#     ppt_windows = [win for win in gw.getWindowsWithTitle("Microsoft Edge") if win.visible]
#     if ppt_windows:
#         ppt_windows[0].activate()
#         print("PowerPoint is now active!")
#
# if ppt_windows:
#     time.sleep(2)
#     pyautogui.hotkey("ctrl", "fn", "f5")
#     pyautogui.hotkey("alt", "enter")
#     print("Slideshow Mode Activated!")
# else:
#     print("PowerPoint window not found! Click inside the window manually.")
#
# # Gesture Control
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(3, 640)
# cap.set(4, 480)
# detector = HandDetector(detectionCon=0.7, maxHands=1)
# last_gesture = None
# frame_skip = 2  # Reduce for smoother detection
# frame_count = 0
# gestureThreshold = 300  # Threshold for gestures
# gesture_cooldown = 1  # Cooldown time in seconds for repeating gestures
# last_gesture_time = time.time()
# drawing = False  # Flag for drawing mode
# draw_points = []  # Stores drawn points
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame_count += 1
#     if frame_count % frame_skip != 0:
#         continue  # Skip frame for better performance
#
#     frame = cv2.flip(frame, 1)
#     hands, img = detector.findHands(frame, flipType=False)
#
#     cv2.line(frame, (0, gestureThreshold), (700, gestureThreshold), (255, 0, 0), 10)  # Visual Gesture Threshold
#
#     if hands:
#         hand = hands[0]
#         lmList = hand["lmList"]
#         cx, cy = hand["center"]
#         fingers = detector.fingersUp(hand)
#         current_time = time.time()
#         index_finger = tuple(lmList[8][:2])
#
#         if cy <= gestureThreshold:  # Gesture only above threshold area
#             if fingers == [1, 0, 0, 0, 1]:
#                 if current_time - last_gesture_time > gesture_cooldown:
#                     pyautogui.press("pagedown")
#                     print("Next Slide")
#                     last_gesture_time = current_time
#
#
#             elif fingers == [0, 0, 0, 0, 0]:               # 0 for thumbs up and 1 for thumbs down
#                 if current_time - last_gesture_time > gesture_cooldown:
#                     pyautogui.press("pageup")
#                     print("Previous Slide")
#                     last_gesture_time = current_time
#         #
#         screen_x, screen_y = pyautogui.size()
#         ppt_x = int((index_finger[0] / 640) * screen_x)  # Convert to screen coordinates
#         ppt_y = int((index_finger[1] / 480) * screen_y)
#         if fingers == [1, 1, 1, 0, 0]:  # Enable drawing
#             drawing = True
#             draw_points.append(index_finger)
#         elif fingers == [0, 1, 1, 0, 0]:  # Stop drawing (Thumbs Down)
#             drawing = False
#
#         elif fingers == [1, 1, 1, 1, 1]:  # Clear drawings (Full Hand Open)
#             draw_points = []
#     for point in draw_points:
#         cv2.circle(frame, point, 6, (239, 51, 47), cv2.FILLED)
#             # drawing = not drawing
#                 # erasing = False
#                 # if drawing:
#         #         pyautogui.hotkey("ctrl", "alt", "p")  # Enable pen mode
#         #     else:
#         #         pyautogui.hotkey("esc")  # Exit drawing mode
#         #     print("Drawing Mode:", drawing)
#         #
#         # elif fingers == [1, 0, 0, 0, 0] and smooth_gesture("erase"):
#         #     erasing = not erasing
#         #     drawing = False
#         #     if erasing:
#         #         pyautogui.hotkey("ctrl", "e")  # Enable eraser mode
#         #     else:
#         #         pyautogui.hotkey("esc")  # Exit eraser mode
#         #     print("Eraser Mode:", erasing)
#         #
#         # if drawing:
#         #     if fingers == [0, 1, 0, 0, 0]:
#         #         index_finger = lmList[8][:2]
#         #         x, y = index_finger
#         #         pyautogui.moveTo(x * 2, y * 2)  # Move cursor to hand position
#         #         pyautogui.dragTo(x * 2, y * 2, duration=0.1)
#         #
#         # if erasing:
#         #     if fingers == [0, 1, 0, 0, 0]:
#         #         index_finger = lmList[8][:2]
#         #         x, y = index_finger
#         #         pyautogui.moveTo(x * 2, y * 2)
#         #         pyautogui.click()
#         #
#         # if fingers == [1, 1, 1, 1, 1] and smooth_gesture("zoom in"):
#         #     pyautogui.hotkey("ctrl", '+')
#         #     print("Zoom In")
#         #
#         # if fingers == [0, 1, 1, 1, 1] and smooth_gesture("zoom out"):
#         #     pyautogui.hotkey("ctrl", '-')
#         #     print("Zoom Out")
#     cv2.imshow("Gesture Presentation", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
import time
import cv2
import pyautogui
import pygetwindow as gw
import webbrowser
from cvzone.HandTrackingModule import HandDetector

# Open PowerPoint Online
OFFICE_PPT_URL = "https://abes365-my.sharepoint.com/:p:/r/personal/mahak_21b0131127_abes_ac_in/_layouts/15/Doc.aspx?sourcedoc=%7BEC786BA1-F1C7-4BD2-B86D-12372DFCC3CF%7D&file=Project%20Presentation%20(P1)%20Format%208th%20Sem.pptx&action=edit&mobileredirect=true&ct=1741101374275&wdOrigin=OFFICECOM-WEB.MAIN.UPLOAD&cid=4ae21ebd-296d-423a-bb96-4455cc1ba919&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=6bf321ca-411d-4a85-8ed7-48ea33d35bdb"
# import webbrowser
# import os

# Full path to your Chrome executable (adjust if installed in a different path)
chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

# Register and open in Chrome
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(OFFICE_PPT_URL)

webbrowser.open(OFFICE_PPT_URL)
print("Office PowerPoint Online Opened Successfully!")

time.sleep(5)
pyautogui.hotkey("ctrl", "tab")  # Switch to PowerPoint
time.sleep(2)

ppt_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if win.visible]

if ppt_windows:
    ppt_windows[0].activate()
    print("PowerPoint is now active!")
else:
    ppt_windows = [win for win in gw.getWindowsWithTitle("Microsoft Edge") if win.visible]
    if ppt_windows:
        ppt_windows[0].activate()
        print("PowerPoint is now active!")

if ppt_windows:
    time.sleep(2)
    pyautogui.hotkey("ctrl", "fn", "f5")  # Start slideshow
    pyautogui.hotkey("alt", "enter")  # Full-screen mode
    print("Slideshow Mode Activated!")
else:
    print("PowerPoint window not found! Click inside the window manually.")

# Gesture Control
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(detectionCon=0.7, maxHands=1)

gestureThreshold = 300  # Threshold for gestures
gesture_cooldown = 1  # Cooldown time in seconds for repeating gestures
mode_switch_cooldown = 3  # Cooldown for mode switching (pen/eraser)
last_gesture_time = time.time()
last_mode_switch = time.time()

drawing_mode = False  # Track if we are in drawing mode

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame, flipType=False)

    cv2.line(frame, (0, gestureThreshold), (700, gestureThreshold), (255, 0, 0), 10)  # Visual Gesture Threshold

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        cx, cy = hand["center"]
        fingers = detector.fingersUp(hand)
        current_time = time.time()
        index_finger = tuple(lmList[8][:2])  # (x, y) of index finger tip

        # Ensure PowerPoint is active
        ppt_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if win.visible]
        if ppt_windows:
            ppt_windows[0].activate()

        if cy <= gestureThreshold:  # Gesture only above threshold area
            if fingers == [1, 0, 0, 0, 1]:  # Next Slide
                if current_time - last_gesture_time > gesture_cooldown:
                    pyautogui.press("pagedown")
                    print("Next Slide")
                    last_gesture_time = current_time

            elif fingers == [0, 0, 0, 0, 0]:  # Previous Slide
                if current_time - last_gesture_time > gesture_cooldown:
                    pyautogui.press("pageup")
                    print("Previous Slide")
                    last_gesture_time = current_time

        # **DRAWING MODE ON POWERPOINT**
        screen_x, screen_y = pyautogui.size()
        ppt_x = int((index_finger[0] / 640) * screen_x)  # Convert to screen coordinates
        ppt_y = int((index_finger[1] / 480) * screen_y)

        if fingers == [1, 1, 1, 0, 0]:  # Enable Drawing Mode
            if not drawing_mode and (current_time - last_mode_switch > mode_switch_cooldown):
                pyautogui.press("p")  # Enable pen tool in PowerPoint
                drawing_mode = True
                last_mode_switch = current_time
                print("Drawing Mode Enabled")

            pyautogui.moveTo(ppt_x, ppt_y)
            pyautogui.mouseDown()  # Simulate pen down

        elif fingers == [0, 1, 1, 0, 0]:  # Stop drawing
            pyautogui.mouseUp()

        elif fingers == [1, 1, 1, 1, 1]:  # Clear drawings
            if current_time - last_mode_switch > mode_switch_cooldown:
                pyautogui.press("e")  # Eraser Mode
                time.sleep(0.5)
                pyautogui.hotkey("ctrl", "a")  # Select all annotations
                pyautogui.press("delete")  # Delete annotations
                drawing_mode = False
                last_mode_switch = current_time
                print("Annotations Cleared")

    cv2.imshow("Gesture Presentation", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# import time
# import cv2
# import pyautogui
# import pygetwindow as gw
# import webbrowser
# from cvzone.HandTrackingModule import HandDetector
#
# # Open PowerPoint Online
# OFFICE_PPT_URL = "https://abes365-my.sharepoint.com/:p:/r/personal/mahak_21b0131127_abes_ac_in/_layouts/15/Doc.aspx?sourcedoc=%7BEC786BA1-F1C7-4BD2-B86D-12372DFCC3CF%7D&file=Project%20Presentation%20(P1)%20Format%208th%20Sem.pptx&action=edit"
# webbrowser.open(OFFICE_PPT_URL)
# print("Opening PowerPoint Online...")
#
# time.sleep(5)
#
# # Get PowerPoint Window (Avoid `activate()` error)
# ppt_windows = [win for win in gw.getWindowsWithTitle("Google Chrome") if win.visible]
# if ppt_windows:
#     ppt_window = ppt_windows[0]
#     try:
#         ppt_window.bringToFront()  # More reliable than activate()
#         print("PowerPoint is now active!")
#     except Exception as e:
#         print(f"Could not bring PowerPoint to front: {e}")
# else:
#     print("PowerPoint window not found! Click manually.")
#
# # Start slideshow mode
# time.sleep(2)
# pyautogui.hotkey("ctrl", "fn", "f5")  # Start slideshow
# time.sleep(1)
# pyautogui.hotkey("alt", "enter")  # Full-screen mode
# print("Slideshow Mode Activated!")
#
# # Gesture Control
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(3, 640)
# cap.set(4, 480)
# detector = HandDetector(detectionCon=0.7, maxHands=1)
#
# gestureThreshold = 350  # Increased threshold
# gesture_cooldown = 1  # Cooldown for gestures
# last_gesture_time = time.time()
#
# # Keep OpenCV window always on top
# cv2.namedWindow("Gesture Presentation", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("Gesture Presentation", cv2.WND_PROP_TOPMOST, 1)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame = cv2.flip(frame, 1)
#     hands, img = detector.findHands(frame, flipType=False)
#
#     # Draw threshold line
#     cv2.line(frame, (0, gestureThreshold), (700, gestureThreshold), (255, 0, 0), 10)
#
#     if hands:
#         hand = hands[0]
#         lmList = hand["lmList"]
#         cx, cy = hand["center"]
#         fingers = detector.fingersUp(hand)
#         current_time = time.time()
#
#         print(f"Gesture detected: {fingers}, Position: ({cx}, {cy})")
#
#         if cy <= gestureThreshold:  # Gesture only above threshold area
#             if fingers == [1, 0, 0, 0, 1]:  # Next Slide
#                 if current_time - last_gesture_time > gesture_cooldown:
#                     pyautogui.press("pagedown")
#                     print("Next Slide")
#                     last_gesture_time = current_time
#
#             elif fingers == [0, 0, 0, 0, 0]:  # Previous Slide
#                 if current_time - last_gesture_time > gesture_cooldown:
#                     pyautogui.press("pageup")
#                     print("Previous Slide")
#                     last_gesture_time = current_time
#
#     # Keep OpenCV window on top
#     cv2.setWindowProperty("Gesture Presentation", cv2.WND_PROP_TOPMOST, 1)
#     cv2.imshow("Gesture Presentation", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
