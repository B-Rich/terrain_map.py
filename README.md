terrain_map.py
==============

Simple python script that uses parallax to scan terrain

This is just a simple program that takes in images with a laser line.  The laser line is used to determine relative 
heights of the terrain to find a smooth area for a quadcopter to land.  This is not a complete program.  Currently,
it just finds any red in the picture and assumes that is the laser line.  So if there are any red objects in the 
picture, it will mess it up.

It's also pretty slow...


Feel free to do whatever you want with this script.




Also, very important:  Make sure the images are labeled "image1.jpg", "image2.jpg", ... , "image16.jpg".

Test images can be found here: http://imgur.com/a/1Mk4v


UPDATE:  I've added new_script.py.  This is the same as the other, but it removes all of the unnecessary plots and variables (as well as the plotting libraries)
