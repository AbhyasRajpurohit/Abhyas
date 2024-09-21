import cv2
image = r"C:\Users\abc\Downloads\abhyas_.jpg"
src = cv2.imread(image, cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", src)

scale = 50

width = int(src.shape[1] * scale / 100)
height = int(src.shape[0] * scale/100) 

output = cv2.resize(src, (width, height))

cv2.imwrite("changed_image.png", output)
cv2.waitKey(0)