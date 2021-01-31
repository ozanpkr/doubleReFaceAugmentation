#import libraries
import cv2
import os
import numpy as np

#click event function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:#left click operation check
        aug(x)#call augmentation function
        
#save function
def save(left,right):
    
    main="./face_Dataset_Aug/"+filename[:-4]
    
    left_way=main+"_left"+".png"#determine doubleLeft image name
    right_way=main+"_right"+".png" #determine doubleright image name
    
    cv2.imwrite(left_way, left) #save doubleLeft image
    cv2.imwrite(right_way, right) #save doubleright image
    print("Done!!!!")
    
#augmentation function
def aug(x):
     
    crop_img_left = img[0:int(size[0]), 0:int(x)] #left side of image according to user point
    crop_img_right = img[0:int(size[0]), int(x):size[1]] #right side of image according to user point
    
    flipHorizontal_left = cv2.flip(crop_img_left, 1) #mirror left side
    flipHorizontal_right = cv2.flip(crop_img_right, 1) #mirror right side
    
    im_left = cv2.hconcat([crop_img_left, flipHorizontal_left]) #image that created from left side
    im_right = cv2.hconcat([flipHorizontal_right, crop_img_right]) #image that created from right side
    
    save(im_left,im_right)#call function for save augmentated image
    
for filename in os.listdir("./face_Dataset"):
    
    img = cv2.imread(os.path.join("./face_Dataset",filename))#read image from base folder
    size=img.shape#get image size for cropping operations
    
    cv2.imshow("image", img)#original image show to user
    cv2.setMouseCallback("image", click_event)#determine click operation
    
    im_file="./face_Dataset/"+filename#original image
    cv2.waitKey(0)
    os.remove(im_file)#delete original image from base folder
    cv2.destroyAllWindows()
