import cv2,time
video=cv2.VideoCapture(0)#Capture object
while True:
    check,frame=video.read()
    #check is boolean data type
    #frame is used for numpy array
    #frame is a 3 dimensional-array
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#to GRAY Scale
    #cv2.imshow("Capturing",frame)#Capture frame

    #time.sleep(3)#stay for sometime
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)#wait for 2 seconds
    if key==ord('q'):#if key pressed is q then
        break#quit
video.release()
cv2.destroyAllWindows#Destroy
