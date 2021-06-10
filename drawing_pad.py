import numpy as np
import cv2 as cv
import datetime
drawing = False 
c = (255,255,255) 
ix,iy = -1,-1
t=2
datet = str(datetime.datetime.now())[:10]
font=cv.FONT_HERSHEY_SIMPLEX

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),t,c,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),t,c,-1)
        cv.circle(img,(x+1,y+1),t,c,-1)
def save():
    cv.imwrite("Mydrawing{}.png".format(datet),img)
img = np.zeros((712,912,3), np.uint8)
img_in = np.zeros((322,354,3), np.uint8)
img_in[:]=(246,246,246)
txt='''Press Key
'p' -> Pink     'b' -> Blue
'r' -> Red      'g' -> Green
'y' -> Yellow   'c'-> Cyan
'w' -> White    'e' -> Erase
'+' -> to increase the \nsize of pencil
'-' -> to decrease the \nsize of pencil
'ESC' -> to close the window
's' -> to Save'''
y0, dy = 20, 29
for i, line in enumerate(txt.split('\n')):
    y = y0 + i*dy
    cv.putText(img_in,line,(13,y),font,0.6,(0,0,0),1,cv.LINE_AA)
cv.namedWindow('Drawing pad')
cv.setMouseCallback('Drawing pad',draw_circle)
cv.imshow('Guide',img_in)
while(1):
    cv.putText(img,datet,(770,695),font,0.6,(25,155,235),1,cv.LINE_AA)
    cv.imshow('Drawing pad',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord("-") and t!=1:
        t-=1
    elif k == ord("="):
        t+=1
    elif k == ord('p'):
        c=(120,95,185)
    elif k == ord('w'):
        c=(255,255,255)
    elif k == ord('r'):
        c=(0,0,255)
    elif k == ord('b'):
        c=(255,0,0)
    elif k == ord('g'):
        c=(0,255,0)
    elif k == ord('c'):
        c=(255,255,0)
    elif k == ord('y'):
        c=(0,255,255)
    elif k == ord('e'):
        c=(0,0,0)
    elif k == ord('s'):
        save()
    elif k == 27:
        break
cv.destroyAllWindows()