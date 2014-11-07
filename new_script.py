# Import libraries
from PIL import Image		# For image processing
import time			# For keeping time
import numpy as np		# For calculations

''' Record starting time (for testing purposes) '''
start_time = time.time()

# Declare constants
number_of_images = 16
ground_level = 30	# Pixels from bottom of image
width = 200			# Pixels
height = 200		# Pixels
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
	all_heights_temp = []	# Stores information for all heights (temporarily)
	for x in range(width):
		y = 0
		line = False
		while y < (height-1):
			R,G,B = pixels[x,y]
			
			# Check for red
			if (R>180 and G<80 and B<80 and line == False):
				all_heights_temp.append(2*(width-y))
				line = True
			y = y + 1
			
			# If no red line is found in a vertical line of pixels,
			#	then the line is assumed to be at ground level
			if y == (height-1) and line == False:
				all_heights_temp.append(2*ground_level)
	
	# Store image heights into matrix
	all_heights.append(all_heights_temp)


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
