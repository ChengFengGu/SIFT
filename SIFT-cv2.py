import cv2


def sift_kp(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将图像转变为灰度图像
    sift = cv2.xfeatures2d.SIFT_create()  # 提取SIFT特征
    kp, des = sift.detectAndCompute(image, None)
    kp_image = cv2.drawKeypoints(image, kp, None)
    return kp_image,kp,des

image = cv2.imread('dog.jpg')
kp_image, _, des = sift_kp(image)
print(image.shape, des.shape)
cv2.namedWindow('dog',cv2.WINDOW_NORMAL)
cv2.imshow('dog', kp_image)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


