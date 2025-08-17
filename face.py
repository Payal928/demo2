import cv2
face_cascad = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while True:

    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascad.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.putText(frame,"face detected",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,1.0,3)
    cv2.imshow("face detection",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        print("quiting ....")

cap.release()
cv2.destroyAllWindows()
        







         

        

    

 



