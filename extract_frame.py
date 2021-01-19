import cv2

cap = cv2.VideoCapture("video/Food_Fed_raw_I2.avi")
i=0
while(cap.isOpened() and i<100):

    ret,img=cap.read()
    filename='Test_img'

    img_filename=filename+'_'+str(i)+'.jpg'
    # print(img.shape)
    cv2.imwrite(img_filename,img)
    i=i+20
    print(i)