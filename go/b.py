#Thanks to  http://stackoverflow.com/a/2659378/2917986
import numpy as np
import sys
import scipy.misc
import gevent
import Image, ImageFont, ImageDraw
from array import *

def paint(array):
	global img
	global count
	greenlets = []
	pix = img.load()

	for i in array:		
		for j in array[i]:								
			# print i,j
			x = array[i].index(array[i][j])
			y = array.index(i)
			print x, y
			if array[i][j] == 1: 
				# pix[i,j] = 255

				# dr.rectangle(((i,j),(i+1,j+1)), fill="black")
				# img.putpixel((i,j),255)
				greenlets.append(gevent.spawn(	img.putpixel, (i,j) , 255))
			else:
				# dr.rectangle(((i,j),(i+1,j+1)), fill="white")
				# pix[i,j] = 0
				# img.putpixel((i,j),0)
				greenlets.append(gevent.spawn(	img.putpixel, (i,j) , 0))
	# gevent.joinall(greenlets, timeout=2)
	img.save("new_"+str(len(array))+".png")


# The input argument to this python file HAS to be a 'valid number'.
# There has to be text file with the name being the 'valid number'
# Eg. 191.txt has to be the file name where 191 is the 'valid number'

# Variable that holds the size of the variables
count = 0

if sys.argv and sys.argv[1] and sys.argv[1].isdigit():
	count = int(sys.argv[1])	

# img = Image.new("L", (count, count), "white")
img = Image.new('RGB', (count,count), (255,255,255))
dr = ImageDraw.Draw(img)
# dr.rectangle(((290,290),(310,310)), fill="blue")
# Reading the matrix from Text file 
data = np.genfromtxt(str(count)+".txt", delimiter=" ", dtype=int, autostrip=True)
print data
# if len(data) == count:
# 	# paint(data)
# 	array = data.tolist()
# 	for i in range(len(array)):		
# 		print array[i]
# 		for j in range(len(array[i])):
# 			# print i,j, array[i][j]
# 			if array[i][j] == 1:
# 				dr.rectangle(((i,j),(i+1,j+1)), fill="black")
# 			if array[i][j] == 0:	
# 				dr.rectangle(((i,j),(i+1,j+1)), fill="white")
# 	img.save(str(count)+"_x.png")
#Writing it to the image
# scipy.misc.imsave('./'+str(count)+'.png', data)
