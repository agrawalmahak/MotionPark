# import cv2
# import pickle
# import cvzone
# import numpy as np
#
# #Video feed
# cap=cv2.VideoCapture('carPark.mp4')
# width,height=107,48
#
# def checkParkingSpace(imgProcess):
#
#     spaceCounter=0
#     for pos in posList:
#         x,y=pos
#         imgCrop=imgProcess[y:y+height,x:x+width]
#         # cv2.imshow(str(x*y),imgCrop)
#         count=cv2.countNonZero(imgCrop)
#
#         if count<1500:
#             color=(0,255,0)
#             thickness=5
#             spaceCounter+=1
#         else:
#             color=(0,0,255)
#             thickness = 2
#         cv2.rectangle(img,pos,(pos[0] + width, pos[1] + height),color,thickness)
#         cvzone.putTextRect(img,str(count),(x,y+height-4),scale=1,thickness=2,offset=0,colorR=color)
#
#         cvzone.putTextRect(img,f'Free: {spaceCounter}/{len(posList)}',(100,50),scale=2,thickness=4,offset=15,colorR=(0,200,0))
#
#
#
#
# with open('CarParkPos', 'rb') as f:
#     posList = pickle.load(f)
#
# while True:
#
#     if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#         cap.set(cv2.CAP_PROP_POS_FRAMES,0)
#     success, img = cap.read()
#     imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     imgBlur=cv2.GaussianBlur(imgGray,(3,3),1)
#     #below line code to convert in binary image (both lines work same)
#     #imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
#     imgThreshold = cv2.Canny(imgBlur,50,150)
#     kernel=np.ones((3,3),np.uint8)
#     imgDilate=cv2.dilate(imgThreshold,kernel,iterations=1)
#
#     checkParkingSpace(imgDilate)

    #for pos in posList:






    # cv2.imshow("image",img)
    # # cv2.imshow("imageBlur",imgBlur)
    # cv2.imshow("imageThreshload", imgThreshold)
    #
    # cv2.waitKey(10)
#

# import cv2
# import pickle
# import cvzone
# import numpy as np
# import os
#
# # Paths to the video files
# video_paths = [
#     "carPark.mp4",
#     "carPark2.mp4",
#     "carPark3.mp4"
# ]
#
# # Define dimensions for parking spaces
# width, height = 107, 48
#
# # Function to generate unique file names for each video
# def get_position_file_path(video_path):
#     base_name = os.path.splitext(os.path.basename(video_path))[0]
#     return f"{base_name}_CarParkPos.pkl"
#
# # Function to load positions for a specific video
# def load_positions(video_path):
#     position_file = get_position_file_path(video_path)
#     if os.path.exists(position_file):
#         with open(position_file, 'rb') as f:
#             return pickle.load(f)
#     return []
#
# # Function to save positions for a specific video
# def save_positions(video_path, positions):
#     position_file = get_position_file_path(video_path)
#     with open(position_file, 'wb') as f:
#         pickle.dump(positions, f)
#
# # Function to check parking spaces
# def checkParkingSpace(imgProcess, img, posList):
#     spaceCounter = 0
#
#     for pos in posList:
#         x, y = pos
#         imgCrop = imgProcess[y:y + height, x:x + width]
#         count = cv2.countNonZero(imgCrop)
#
#         if count < 1500:  # Threshold to determine if a parking space is free
#             color = (0, 255, 0)
#             thickness = 5
#             spaceCounter += 1
#         else:
#             color = (0, 0, 255)
#             thickness = 2
#
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y + height - 4), scale=1, thickness=2, offset=0, colorR=color)
#
#     # Display the count of free spaces
#     cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=2, thickness=4, offset=15, colorR=(0, 200, 0))
#
# # Process videos
# def process_videos(video_paths):
#     for video_path in video_paths:
#         cap = cv2.VideoCapture(video_path)
#
#         # Load parking positions for the current video
#         posList = load_positions(video_path)
#
#         while True:
#             if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#                 cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#
#             success, img = cap.read()
#
#             # Preprocess the video frame
#             imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
#             # imgThreshold = cv2.Canny(imgBlur, 50, 150)
#             imgThreshold = cv2.Canny(imgBlur, 50, 150)
#             kernel = np.ones((3, 3), np.uint8)
#             imgDilate = cv2.dilate(imgThreshold, kernel, iterations=1)
#
#             # Check parking spaces
#             checkParkingSpace(imgDilate, img, posList)
#
#             # Display the frames
#             cv2.imshow(f"Parking Detection - {os.path.basename(video_path)}", img)
#             cv2.imshow(f"Threshold - {os.path.basename(video_path)}", imgThreshold)
#
#             key = cv2.waitKey(10)
#
#
# # Start processing videos
# process_videos(video_paths)

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
