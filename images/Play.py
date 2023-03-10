import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.JPG', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file # ex : if the image is 110.jpg this line of code will write it as 'Images/110'

        print(file_name)
               
        images.append(file_name) # adds all of the items in file_name into the array on line 7
        
print(len(images)) # len tells you amount of items in array and count is a variable that will store that number
count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)


out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size) # first argument is the name of your video file, second argument is the type (fourcc), third argument is frame per second, fourth arg is frame size (we are going to call it a variable size for now and defie it later)

for i in range(count-1,0,-1) : # range takes three arguments : the starting point,ending point, and how much you want to increase
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()#release displays it on the screen
