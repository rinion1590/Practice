import cv2

input = "TCU_Bird_0.png"
mid = "gray.png"
output = "edge.png"

graying = cv2.imread(input, cv2.IMREAD_GRAYSCALE)
detedge = cv2.Canny(graying, 50, 110)

cv2.imwrite(output, detedge)
