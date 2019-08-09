import glob
import cv2
import glob

a = sorted(glob.glob('images\\asd\*.jpg'))

fps = 144    #保存视频的FPS，可以适当调整
 
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('test'+str(fps)+'.avi',fourcc,fps,(1920,1080))#最后一个是保存图片的尺寸
imgs=glob.glob('images/asd/*.jpg')

for i in range(len(a)):
    frame = cv2.imread('images/asd/'+str(i)+'.jpg')
    print(i)
    videoWriter.write(frame)
videoWriter.release()
