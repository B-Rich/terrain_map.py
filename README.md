terrain_map.py
==============

Simple python script that uses parallax to scan terrain

This is just a simple program that takes in images with a laser line.  The laser line is used to determine relative 
heights of the terrain to find a smooth area for a quadcopter to land.  This is not a complete program.  Currently,
it just finds any red in the picture and assumes that is the laser line.  So if there are any red objects in the 
picture, it will mess it up.

It's also pretty slow...


Feel free to do whatever you want with this script.
