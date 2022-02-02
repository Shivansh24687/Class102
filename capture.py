import cv2
def take_snapshot():
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        cv2.imwrite("Img1.jpg",frame)
    videocaptureobject.release()
    cv2.destroyAllWindows()
take_snapshot()
