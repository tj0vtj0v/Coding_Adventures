import numpy as np
from PIL import Image
import math 
#add import if needed

#def vars
equalation = input("Input equalation: ")
x_range = input("Input x_range: ")
y_range = input("Input y_range: ")
x_guide_point_distance = input("Input point_distance_x: ")
y_guide_point_distance = input("Input point_distance_y: ")
x_res = input("Input x_resolution: ")
y_res = input("Input y_resolution: ")
x_offset = input("Input x_offset: ")
y_offset = input("Input y_offset: ")
grid = input("Input if you whant a grid: ")
coordinate_system_line_size = 4
line_width_factor = .01

#colors
backgroud_color = (0, 0, 0)
coordinate_system_color = (255, 128, 128)
coordinate_marker_color = (228, 228, 228)
graph_color = (255, 255, 255)

#calculate vars
y_range = y_range*2
x_range = x_range*2
y_offset = y_offset*y_res
x_offset = x_offset*x_res
x_range = int(x_range*x_res)
y_range = int(y_range*y_res)

#y loop
pixel_array = []
for original_y in range(y_range):
  #create Process bar
  print("Process: " + str(original_y) + "/" + str(y_range) + "_________" + str(int(100*original_y/y_range)), end="%\r")
  #def vars
  y = (((original_y - y_range/2) - y_offset)*(1/y_res))
  y_center = original_y - y_range/2 - y_offset
  #x loop
  x_pixel_storage = []
  for original_x in range(x_range):
    #def vars
    x = (((original_x - x_range/2) + x_offset)*(1/x_res))
    x_center = original_x - x_range/2 + x_offset
    #draw graph
    if abs(-(eval(equalation)) - y) <= line_width_factor: x_pixel_storage.append(graph_color)
    #draw orientation points
    elif (y%y_guide_point_distance)*y_res <= 2*coordinate_system_line_size and abs(x*x_res) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_marker_color)
    elif (x%x_guide_point_distance)*x_res <= 2*coordinate_system_line_size and abs(y*y_res) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_marker_color)
    #draw main cross
    elif abs(y_center) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_system_color)
    elif abs(x_center) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_system_color)
    #draw grid if wanted
    elif (y%y_guide_point_distance)*y_res <= 2*coordinate_system_line_size and grid: x_pixel_storage.append(coordinate_marker_color)
    elif (x%x_guide_point_distance)*x_res <= 2*coordinate_system_line_size and grid: x_pixel_storage.append(coordinate_marker_color)
    #fill background
    else: x_pixel_storage.append(backgroud_color)
  #save list
  pixel_array.append(x_pixel_storage)

#make array from list
array = np.array(pixel_array, dtype=np.uint8)

#Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.show()

#save img if wanted
if "y" in input("do you want to save the image? (y/n): "):
  name = input("please enter filename without file_format (.png, etc): ")
  new_image.save(name + ".png", "PNG")