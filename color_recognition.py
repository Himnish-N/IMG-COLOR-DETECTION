import cv2

cap = cv2.VideoCapture(0) #importing the video from the webcam change index to change webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #setting the width of the video
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) #setting the height of the video 


while True:

    _, frame = cap.read() #reading the video

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converting the video from BGR to HSV

    height, width, _ = frame.shape #getting the height and width of the video
    
    centre_of_x = int(width/2) #getting the centre of the width
    centre_of_y = int(height/2) #getting the centre of the height

    pixel_center = hsv_frame[centre_of_y, centre_of_x] #getting the pixel value of the centre of the video
    
    hue_value = pixel_center[0] #getting the hue value of the pixel
    saturation_value = pixel_center[1] #getting the saturation value of the pixel
    value_value = pixel_center[2] #getting the value value of the pixel

    print(pixel_center) #printing the pixel value of the centre of the video
    cv2.circle(frame, (centre_of_x, centre_of_y), 2, (0, 0, 255), 3) #drawing a circle at the centre of the video


    cv2.imshow("Frame", frame) #showing the video
    key = cv2.waitKey(1) #wait for 1 millisecond
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()