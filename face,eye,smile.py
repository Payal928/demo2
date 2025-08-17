import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,h,w) in faces:
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"face detected",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,2),2)

        ri_gray = gray[y:y+h,x:x+w]
        ri_color = frame[y:y+h,x:x+w]

        eyes = eye_cascade.detectMultiScale(ri_gray,1.10)
        smiles = smile_cascade.detectMultiScale(ri_gray,1.7,20)

        if len(eyes)>0:
            cv2.putText(frame,"eyes detected",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)

        if len(smiles)>0:
            cv2.putText(frame,"smile detected",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)

    cv2.imshow("face,eyes,smile detecting",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        print("quit...")
        break
cap.release()
cv2.destroyAllWindows()



     