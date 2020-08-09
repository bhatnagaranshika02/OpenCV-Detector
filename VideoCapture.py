import cv2,time
video = cv2.VideoCapture(0)
check,frame = video.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow('capturing',frame)
sv2.waitKey(0)
video.release()
cv2.destroyAllWindows
