# import cv2
# import pickle
#
#
# width,height=107,48
# try:
#     with open('CarParkPos', 'rb') as f:
#         posList=pickle.load( f)
#
# except:
#     posList=[]
# def mouseClick(events,x,y,flags,params):
#     # to create rectangle with left click
#     if events==cv2.EVENT_LBUTTONDOWN:
#         posList.append((x,y))
#         #To delete rectangle by right click
#     if events==cv2.EVENT_RBUTTONDOWN:
#         for i,pos in enumerate(posList):
#             x1,y1=pos
#             if x1 < x < x1 + width and y1 < y < y1 + height:
#                 posList.pop(i)
#
#     with open('CarParkPos', 'wb') as f:
#        pickle.dump(posList,f)
#
# while True:
#     img = cv2.imread('carParkImg.png')
#
#
#     # 157-50= 107 , 240-192= 48
#     for pos in posList:
#         cv2.rectangle(img,pos,(pos[0] + width, pos[1] + height),(255,0,255),2)
#
#     cv2.imshow("image",img)
#     cv2.setMouseCallback("image",mouseClick)
#     cv2.waitKey(5000)

# import cv2
# import pickle
#
# # Initialize default percentages for rectangle dimensions
# rect_width_pct = 0.15  # 10% of image width
# rect_height_pct = 0.1  # 5% of image height
#
# try:
#     with open('CarParkPos', 'rb') as f:
#         posList = pickle.load(f)
# except FileNotFoundError:
#     posList = []
#
#
# def mouseClick(events, x, y, flags, params):
#     img_width, img_height = params
#     rect_width = int(img_width * rect_width_pct)
#     rect_height = int(img_height * rect_height_pct)
#
#     # To create rectangle with left click
#     if events == cv2.EVENT_LBUTTONDOWN:
#         posList.append((x, y))
#
#     # To delete rectangle by right click
#     if events == cv2.EVENT_RBUTTONDOWN:
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + rect_width and y1 < y < y1 + rect_height:
#                 posList.pop(i)
#
#     # Save updated positions to file
#     with open('CarParkPos', 'wb') as f:
#         pickle.dump(posList, f)
#
#
# while True:
#     img = cv2.imread('carParkImg.png')
#
#
#     img_height, img_width, _ = img.shape
#     rect_width = int(img_width * rect_width_pct)
#     rect_height = int(img_height * rect_height_pct)
#
#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + rect_width, pos[1] + rect_height), (255, 0, 255), 2)
#
#     cv2.imshow("image", img)
#     cv2.setMouseCallback("image", mouseClick, (img_width, img_height))
#     if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
#         break
#
# cv2.destroyAllWindows()

import cv2
import pickle
import os

# Initialize default percentages for rectangle dimensions
rect_width_pct = 0.11  # 15% of image width
rect_height_pct = 0.08  # 10% of image height

# List of images to handle
image_files = ['carParkImg.png', 'carParkImg2.png', 'carParkImg3.png']
current_image_index = 0

# Load or initialize position list for the current image
def load_positions(image_name):
    pos_file = f'{os.path.splitext(image_name)[0]}_CarParkPos.pkl'
    if os.path.exists(pos_file):
        with open(pos_file, 'rb') as f:
            return pickle.load(f)
    return []

def save_positions(image_name, pos_list):
    pos_file = f'{os.path.splitext(image_name)[0]}_CarParkPos.pkl'
    with open(pos_file, 'wb') as f:
        pickle.dump(pos_list, f)

# Mouse click event handler
def mouseClick(event, x, y, flags, params):
    global posList
    img_width, img_height = params
    rect_width = int(img_width * rect_width_pct)
    rect_height = int(img_height * rect_height_pct)

    if event == cv2.EVENT_LBUTTONDOWN:  # Add rectangle with left-click
        posList.append((x, y))

    elif event == cv2.EVENT_RBUTTONDOWN:  # Remove rectangle with right-click
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + rect_width and y1 < y < y1 + rect_height:
                posList.pop(i)
                break

    # Save updated positions for the current image
    save_positions(image_files[current_image_index], posList)

while True:
    # Load the current image
    current_image = image_files[current_image_index]
    img = cv2.imread(current_image)
    if img is None:
        print(f"Error: Image file {current_image} not found!")
        break

    # Load rectangle positions for the current image
    posList = load_positions(current_image)

    img_height, img_width, _ = img.shape
    rect_width = int(img_width * rect_width_pct)
    rect_height = int(img_height * rect_height_pct)

    # Draw all saved rectangles
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + rect_width, pos[1] + rect_height), (255, 0, 255), 2)

    # Display the current image and listen for mouse events
    cv2.imshow("Parking Lot", img)
    cv2.setMouseCallback("Parking Lot", mouseClick, (img_width, img_height))

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break
    elif key == ord('n'):  # Press 'n' to move to the next image
        current_image_index = (current_image_index + 1) % len(image_files)
    elif key == ord('p'):  # Press 'p' to move to the previous image
        current_image_index = (current_image_index - 1) % len(image_files)

cv2.destroyAllWindows()

# import cv2
# import pickle
# import os
#
# # Initialize default percentages for rectangle dimensions
# rect_width_pct = 0.11  # 15% of image width
# rect_height_pct = 0.08  # 10% of image height
#
# # List of images to handle
# image_files = ['carParkImg.png', 'carParkImg2.png', 'carParkImg3.png']
# current_image_index = 0
#
# # Load or initialize position list for the current image
# def load_positions(image_name):
#     pos_file = f'{os.path.splitext(image_name)[0]}_CarParkPos.pkl'
#     if os.path.exists(pos_file):
#         with open(pos_file, 'rb') as f:
#             return pickle.load(f)
#     return []
#
# def save_positions(image_name, pos_list):
#     pos_file = f'{os.path.splitext(image_name)[0]}_CarParkPos.pkl'
#     with open(pos_file, 'wb') as f:
#         pickle.dump(pos_list, f)
#
# # Mouse click event handler
# def mouseClick(event, x, y, flags, params):
#     global posList
#     img_width, img_height = params
#     rect_width = int(img_width * rect_width_pct)
#     rect_height = int(img_height * rect_height_pct)
#
#     if event == cv2.EVENT_LBUTTONDOWN:  # Add rectangle with left-click
#         posList.append((x, y))
#
#     elif event == cv2.EVENT_RBUTTONDOWN:  # Remove rectangle with right-click
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + rect_width and y1 < y < y1 + rect_height:
#                 posList.pop(i)
#                 break
#
#     # Save updated positions for the current image
#     save_positions(image_files[current_image_index], posList)
#
# while True:
#     # Load the current image
#     current_image = image_files[current_image_index]
#     img = cv2.imread(current_image)
#     if img is None:
#         print(f"Error: Image file {current_image} not found!")
#         break
#
#     # Load rectangle positions for the current image
#     posList = load_positions(current_image)
#
#     img_height, img_width, _ = img.shape
#     rect_width = int(img_width * rect_width_pct)
#     rect_height = int(img_height * rect_height_pct)
#
#     # Draw all saved rectangles
#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + rect_width, pos[1] + rect_height), (255, 0, 255), 2)
#
#     # Display the current image and listen for mouse events
#     cv2.imshow("Parking Lot", img)
#     cv2.setMouseCallback("Parking Lot", mouseClick, (img_width, img_height))
#
#     key = cv2.waitKey(1) & 0xFF
#     if key == 27:  # Press 'Esc' to exit
#         break
#     elif key == ord('n'):  # Press 'n' to move to the next image
#         current_image_index = (current_image_index + 1) % len(image_files)
#     elif key == ord('p'):  # Press 'p' to move to the previous image
#         current_image_index = (current_image_index - 1) % len(image_files)
#
# cv2.destroyAllWindows()
