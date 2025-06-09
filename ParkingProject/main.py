
import cv2
import pickle
import cvzone
import numpy as np
import os

# Video feed
video_files = ['carPark.mp4', 'carPark2.mp4', 'carPark3.mp4']  # List of videos
image_files = ['carParkImg.png', 'carParkImg2.png', 'carParkImg3.png']  # Corresponding annotation images
current_video_index = 0

width, height = 107, 48  # Rectangle dimensions

# Load parking space positions for the current video/image
def load_positions(image_name):
    pos_file = f'{os.path.splitext(image_name)[0]}_CarParkPos.pkl'
    if os.path.exists(pos_file):
        with open(pos_file, 'rb') as f:
            return pickle.load(f)
    return []

def checkParkingSpace(imgProcess, img, posList):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgProcess[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 1500:  # Threshold to consider the space empty
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        # Draw rectangles on video
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 4), scale=1, thickness=2, offset=0, colorR=color)

    # Display available spaces
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=2, thickness=4, offset=15, colorR=(0, 200, 0))

while True:
    # Load the current video and its associated parking positions
    current_video = video_files[current_video_index]
    current_image = image_files[current_video_index]

    posList = load_positions(current_image)

    cap = cv2.VideoCapture(current_video)
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break

        # Preprocess the frame
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.Canny(imgBlur, 50, 150)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgThreshold, kernel, iterations=1)

        # Check parking spaces and draw on the video
        checkParkingSpace(imgDilate, img, posList)

        # Display video frames
        cv2.imshow("Parking Lot", img)
        
        key = cv2.waitKey(10) & 0xFF
        if key == 27:  # Esc key to exit
            cap.release()
            cv2.destroyAllWindows()
            exit(0)
        elif key == ord('n'):  # Move to the next video
            current_video_index = (current_video_index + 1) % len(video_files)
            break
        elif key == ord('p'):  # Move to the previous video
            current_video_index = (current_video_index - 1) % len(video_files)
            break

    cap.release()
