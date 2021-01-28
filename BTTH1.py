import cv2
import numpy as np
cv2.namedWindow("Cau 1")
vc = cv2.VideoCapture(0)
if vc.isOpened():
    ret, frame = vc.read()
else:
    ret = False
n=0
def help():
    print(
        'nhan phim\n1 :  Line  \n'
                  '2 :  Rectangle \n'
                  '3 :  Circle \n'
                  '4 :  Ellipse \n'
                  '5 :  Polylines\n'
                  '6 :  Nhom1\n'.format()

    )
help()
def Line():
    cv2.line(frame, (181, 102), (474, 273), (255, 0, 0), 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Line', (321, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


def Rectangle():
    cv2.rectangle(frame, (181, 102), (473, 273), (0, 255, 0), 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Rectangle', (271, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def Circle():
    cv2.circle(frame, (332, 174), 103, (0, 0, 255), 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Circle', (290, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def Ellipse():
    cv2.ellipse(frame, (332, 172), (150, 100), 0, 0, 360, 255, 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Ellipse', (290, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def Polylines():
    pts = np.array([[117, 198], [276, 262], [470, 155], [601, 310]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(frame, [pts], True, (0, 255, 255))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Polylines', (290, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
def Nhom1():
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Nhom1', (151, 84), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'Hong Nhung', (151, 145), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'Manh Dat', (151, 220), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'Dinh Long', (151, 290), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

while ret:
    cv2.imshow("Cau 1", frame)
    ret, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('1'):
        n = 1
    elif key == ord('2'):
        n = 2
    elif key == ord('3'):
        n = 3
    elif key == ord('4'):
        n = 4
    elif key == ord('5'):
        n = 5
    elif key == ord('6'):
        n = 6

    if n == 1:
        Line()
    elif n == 2:
        Rectangle()
    elif n == 3:
        Circle()
    elif n == 4:
        Ellipse()
    elif n == 5:
        Polylines()
    elif n == 6:
        Nhom1()

vc.release()
cv2.destroyWindow("Cau 1")