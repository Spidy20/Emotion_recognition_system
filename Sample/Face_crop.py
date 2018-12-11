import cv2,glob

images=glob.glob("*.jpg")

for image in images:

    img=cv2.imread(image,0)

    re=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))


    for f in re:
        f_name = image.split('/')
        f_name = f_name[-1]
        cv2.imshow("checking",sub_face)
        cv2.waitKey(500)
        cv2.destroyAllWindows()



        cv2.imwrite("resized_"+image,sub_face)