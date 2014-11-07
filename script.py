'''
  Author:	Joshua Twigg
  Date:		October 14, 2014
  Purpose:	Analyze images containing laser line to determine relative heights.  Use these
  			to choose the smoothest area.
  ________________________________________________________________________________________
  
  Part 1:	This section will input a group of images, each with a visible laser line.  A
  			loop will be implemented that examines each pixel in search for the laser line
  			to determine the relative heights of the objects in the image (actual heights 
  			are not necessary).
  			
  			The heights from each picture will each be stored in a 1-dimensional matrix, 
  			and combined together to form a large matrix containing all heights of the 
  			scanned area.  This matrix will be plotted to show a terrain mapping of the
  			scanned area.
'''

# Import libraries
from PIL import Image								              # For image processing
import time											                  # For keeping time
import numpy as np									              # For calculations
import matplotlib.pyplot as plt						        # For plot
from mpl_toolkits.mplot3d import Axes3D				    # For plot
from matplotlib.collections import PolyCollection	# For plot
from matplotlib.colors import colorConverter		  # For plot

''' Record starting time (for testing purposes) '''
start_time = time.time()

# Declare constants
number_of_images = 16
ground_level = 70	# Pixels from bottom of image
width = 400			# Pixels
height = 400		# Pixels

heights = []		# Empty array that will store line heights for plot
all_heights = []	# Matrix that will hold all heights (for calculations)
for n in range(1,number_of_images+1):

	# Open images one at a time (image1.jpg, image2.jpg, etc.)
	image = Image.open('image' + str(n) + '.jpg')

	# Resize image to 400x400 using anti-alias downsampling filter
	image = image.resize((width,height),Image.ANTIALIAS)

	# Convert image into RGB format
	if image.mode != 'RGB':
		image = image.convert('RGB')

	# Create matrix containing RGB values for each pixel
	pixels = image.load()

	# Examine each pixel, searching for red
	line_height = [] 		# Stores line heights for one picture at a time
	all_heights_temp = []	# Stores information for all heights (temporarily)
	m = 0
	for x in range(width):
		y = 0
		line = False
		while y < (height-1):
			R,G,B = pixels[x,y]
			
			# Check for red
			if (R>180 and G<80 and B<80 and line == False):
				all_heights_temp.append(width-y)
				temp = (m,width-y)
				line_height.append(temp)
				line = True
			y = y + 1
			
			# If no red line is found in a vertical line of pixels,
			#	then the line is assumed to be at ground level
			if y == (height-1) and line == False:
				temp = (m,ground_level)
				line_height.append(temp)
				all_heights_temp.append(ground_level)
		m = m + 1
	temp = (m,0)
	line_height.append(temp)
	
	# Store image heights into matrix
	heights.append(line_height)
	all_heights.append(all_heights_temp)

'''
Part 2:		This section will take the matrix containing heights of the objects in the 
			images and separate them into 4 matrices.  The standard deviations of each
			matrix will be calculated.  The matrix with the lowest standard deviation will
			represent the smoothest area of terrain (out of the 4 sections).
			
			If two or more areas have the same standard deviations, the program will 
			choose the lowest numbered area (1 over 2, or 2 over 4, etc.).
			
'''

# Divide matrix into 4 sections
heights_1 = []
y = 0
while y < number_of_images/2:
	x = 0
	while x < width/2:
		heights_1.append(all_heights[y][x])
		x = x + 1
	y = y + 1

heights_2 = []
y = 0
while y < number_of_images/2:
	x = width/2
	while x < width:
		heights_2.append(all_heights[y][x])
		x = x + 1
	y = y + 1

heights_3 = []
y = number_of_images/2
while y < number_of_images:
	x = 0
	while x < width/2:
		heights_3.append(all_heights[y][x])
		x = x + 1
	y = y + 1

heights_4 = []
y = number_of_images/2
while y < number_of_images:
	x = width/2
	while x < width:
		heights_4.append(all_heights[y][x])
		x = x + 1
	y = y + 1
		

# Standard Deviation
list_1 = np.array(heights_1)
list_2 = np.array(heights_2)
list_3 = np.array(heights_3)
list_4 = np.array(heights_4)
stand = [np.std(list_1), np.std(list_2), np.std(list_3), np.std(list_4)]

print '\n\nThe standard deviations are as follows:'
print 'Section 1: ' + str(stand[0])
print 'Section 2: ' + str(stand[1])
print 'Section 3: ' + str(stand[2])
print 'Section 4: ' + str(stand[3])
print '\n'

land = 1
hold = stand[0]
for n in range(3):
	if hold > stand[n+1]:
		hold = stand[n+1]


print '\nSection ' + str(land) + ' is the recommended landing zone'



''' Display run time (for testing) '''
print '\n\n'
print('That only took %s seconds') %round((time.time() - start_time),4)
print '\n'


''' Plot surface (for testing) '''
fig = plt.figure()
ax = fig.gca(projection='3d')

cc = lambda arg: colorConverter.to_rgba(arg, alpha=0.4)

poly = PolyCollection(heights, facecolors = [cc('r'), cc('g'), cc('b'), cc('y')])
poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=range(height), zdir='y')

ax.set_xlabel('X')
ax.set_xlim3d(0, width)
ax.set_ylabel('Y')
ax.set_ylim3d(0, number_of_images)
ax.set_zlabel('Z')
ax.set_zlim3d(0, height)

plt.show()







