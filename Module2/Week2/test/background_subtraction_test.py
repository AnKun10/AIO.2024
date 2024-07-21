from Module2.Week2.model.background_subtraction import replace_background
import cv2

obj_img = cv2.imread('../dataset/Object.png', 1)
obj_img = cv2.resize(obj_img, (678, 381))
bg_img = cv2.imread('../dataset/GreenBackground.png', 1)
bg_img = cv2.resize(bg_img, (678, 381))
new_bg_img = cv2.imread('../dataset/NewBackground.jpg', 1)
new_bg_img = cv2.resize(new_bg_img, (678, 381))

replace_bg_img = replace_background(bg_img=bg_img, new_bg_img=new_bg_img, inp_img=obj_img)

cv2.imshow('Image', replace_bg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
