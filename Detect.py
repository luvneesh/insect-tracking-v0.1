import cv2
import numpy as np
# cv2.startWindowThread()
cap = cv2.VideoCapture("video/Food_Fed_raw_I2.avi")
#143x289
#332x324
#background is rgb(213, 213, 213)
#wing is rgb(152, 152, 152)

while(cap.isOpened()):

    cv2.waitKey(1)
    _,img=cap.read()
    cv2.imshow("input",img)
    img3=img.copy()
    img2=img.copy()
    output=img.copy()
    img3[:,:,:]=0
    print(img[143,143,1])
    img[322-280:,:146,0]=255
    img[322-280:,:146,1]=255
    img[322-280:,:146,2]=255

    img[:,:5,0]=255
    img[:,:5,1]=255
    img[:,:5,2]=255

    img[:5,:,0]=255
    img[:5,:,1]=255
    img[:5,:,2]=255

    img[322-280:,187:,0]=255
    img[322-280:,187:,1]=255
    img[322-280:,187:,2]=255


    Bodydet=[]
    fly_img=img.copy()
    # cv2.imshow('out',img)
    '''
    Body Detection 
    '''
    mask=cv2.inRange(img2,np.array([0, 0,0]),np.array([50,50,50]))
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        i = max(contours, key = cv2.contourArea)
        rect=cv2.minAreaRect(i)
        box=cv2.boxPoints(rect)
        box=np.int0(box)
        centre=rect[0]
        Bodydet.append(centre)

        cv2.circle(output,(int(centre[0]), int(centre[1])), 7, (0,0,255), -1)
        cv2.circle(img3,(int(centre[0]), int(centre[1])), 20, (255,255,255), -1)
        # cv2.imshow("othermask",img3)
        # cv2.circle(fly_img,(int(centre[0]), int(centre[1])), 50, (77,93,100), -1)
    else: 
        centre=Bodydet[-1]
        cv2.circle(output,(int(centre[0]), int(centre[1])), 7, (0,0,255), -1)
        cv2.circle(img3,(int(centre[0]), int(centre[1])), 20, (255,255,255), -1)
        # cv2.imshow("othermask",img3)
    mask2=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
    '''
    wing detection
    '''

    mask=cv2.inRange(img,np.array([110,110,110]),np.array([180,180,180]))
    kernel = np.ones((3,3),np.uint8)
    mask=cv2.bitwise_and(mask,mask2)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    mask=erosion
    cv2.imshow('mask',mask)
    contours1, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours1) != 0:
        i = max(contours1, key = cv2.contourArea)
        rect1=cv2.minAreaRect(i)
        box1=cv2.boxPoints(rect1)
        box1=np.int0(box1)
        centre1=rect1[0]
        cv2.circle(output,(int(centre1[0]), int(centre1[1])), 7, (255,0,0), -1)
        # cv2.circle(fly_img,(int(centre[0]), int(centre[1])), 50, (77,93,100), -1)
    cv2.imshow('out',output)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)