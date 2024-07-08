from Module2.Week1.model.rgb_to_gray import RGB_to_Gray
import matplotlib.image as mpimg

converter = RGB_to_Gray()
img = mpimg.imread('../dataset/dog.jpeg')
converter.set_img(img)

# Ex12
gray_img1 = converter.convert(func='lightness')
print(gray_img1[0, 0])

# Ex13
gray_img2 = converter.convert(func='average')
print(gray_img2[0, 0])

# Ex14
gray_img3 = converter.convert(func='luminous')
print(gray_img3[0, 0])
