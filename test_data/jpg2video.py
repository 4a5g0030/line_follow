import cv2
import numpy as np
import glob

img_array = []
img_root = 'test_data/output/'
for filename in glob.glob(img_root + '*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('test_data/video/output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 8, size)

for i in range(len(img_array)):
    out.write(img_array[i])
    print('{:.2%}'.format(i/len(img_array)))
print('100%')
out.release()
