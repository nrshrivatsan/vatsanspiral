#Thanks to  http://stackoverflow.com/a/2659378/2917986
import numpy as np
import scipy.misc
import sys

# Variable that holds the size of the variables
count = 0

# The input argument to this python file HAS to be a 'valid number'.
# There has to be text file with the name being the 'valid number'
# Eg. 191.txt has to be the file name where 191 is the 'valid number'
if sys.argv and sys.argv[1] and sys.argv[1].isdigit():
	count = int(sys.argv[1])	

# Reading the matrix from Text file 
data = np.genfromtxt(str(count)+".txt")

#Writing it to the image
scipy.misc.imsave('./'+str(count)+'.png', data)
