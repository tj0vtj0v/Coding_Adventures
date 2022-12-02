#sourcecode of created programm
sourcecode="import numpy as np\n"\
      "from PIL import Image\n"\
      "import math\n"\
      "#enter here additional imports\n"\
      "x_range = {x_range}\n"\
      "y_range = {y_range}\n"\
      "x_guide_point_distance = {x_guide_point_distance}\n"\
      "y_guide_point_distance = {y_guide_point_distance}\n"\
      "coordinate_system_line_size = {coordinate_system_line_size}\n"\
      "x_res = {x_resolution}\n"\
      "y_res = {y_resolution}\n"\
      "x_offset = {x_offset}\n"\
      "y_offset = {y_offset}\n"\
      "line_width_factor = {line_width_factor}\n"\
      "grid_bool = {grid_bool}\n"\
      "backgroud_color = {backgroud_color}\n"\
      "coordinate_system_color = {coordinate_system_color}\n"\
      "coordinate_marker_color = {coordinate_marker_color}\n"\
      "graph_color = {graph_color}\n"\
      "y_range = y_range*2\n"\
      "x_range = x_range*2\n"\
      "y_offset = y_offset*y_res\n"\
      "x_offset = x_offset*x_res\n"\
      "x_range = int(x_range*x_res)\n"\
      "y_range = int(y_range*y_res)\n"\
      "pixel_array = []\n"\
      "for original_y in range(y_range):\n"\
      "\tprint(\"Process: \" + str(original_y) + \"/\" + str(y_range) + \"_________\" + str(int(100*original_y/y_range)), end=\"%\\r\")\n"\
      "\ty = (((original_y - y_range/2) - y_offset)*(1/y_res))\n"\
      "\ty_center = original_y - y_range/2 - y_offset\n"\
      "\tx_pixel_storage = []\n"\
      "\tfor original_x in range(x_range):\n"\
      "\t\tx = (((original_x - x_range/2) + x_offset)*(1/x_res))\n"\
      "\t\tx_center = original_x - x_range/2 + x_offset\n"\
      "\t\tif abs(-({equalation}) - y) <= line_width_factor: x_pixel_storage.append(graph_color)\n"\
      "\t\telif (y%y_guide_point_distance)*y_res <= 2*coordinate_system_line_size and abs(x*x_res) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_marker_color)\n"\
      "\t\telif (x%x_guide_point_distance)*x_res <= 2*coordinate_system_line_size and abs(y*y_res) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_marker_color)\n"\
      "\t\telif abs(y_center) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_system_color)\n"\
      "\t\telif abs(x_center) <= coordinate_system_line_size: x_pixel_storage.append(coordinate_system_color)\n"\
      "\t\telif (y%y_guide_point_distance)*y_res <= 2*coordinate_system_line_size and grid_bool: x_pixel_storage.append(coordinate_marker_color)\n"\
      "\t\telif (x%x_guide_point_distance)*x_res <= 2*coordinate_system_line_size and grid_bool: x_pixel_storage.append(coordinate_marker_color)\n"\
      "\t\telse: x_pixel_storage.append(backgroud_color)\n"\
      "\tpixel_array.append(x_pixel_storage)\n"\
      "array = np.array(pixel_array, dtype=np.uint8)\n"\
      "image = Image.fromarray(array)\n"\
      "image.show()\n"\
      "if \"y\" == input(\"do you whant to save the image? (y/n): \"):\n"\
      "\tname = input(\"please enter filename without file_format (.png, etc): \")\n"\
      "\timage.save(name + \".png\", \"PNG\")\n"

#create file with given parameters
def create_file(equalation = "0",
    x_range = "5",
    y_range = "5",
    x_guide_point_distance = ".5",
    y_guide_point_distance = ".5",
    x_resolution = "500",
    y_resolution = "500",
    x_offset = "0",
    y_offset = "0",
    grid_bool = "False"
    ):
  ##change args and see what happens
  coordinate_system_line_size = "5"
  line_width_factor = ".025"
  backgroud_color = "(0, 0, 0)"
  coordinate_system_color = "(255, 128, 128)"
  coordinate_marker_color = "(228, 228, 228)"
  graph_color = "(255, 255, 255)"
  ##
    
  file = open("Calculation.py", "w")
  file.writelines(sourcecode.format(
    x_range = x_range, 
    y_range = y_range, 
    x_guide_point_distance = x_guide_point_distance, 
    y_guide_point_distance = y_guide_point_distance,
    coordinate_system_line_size = coordinate_system_line_size,
    x_resolution = x_resolution,
    y_resolution = y_resolution,
    x_offset = x_offset,
    y_offset = y_offset,
    line_width_factor = line_width_factor,
    grid_bool = grid_bool,
    backgroud_color = backgroud_color,
    coordinate_system_color = coordinate_system_color,
    coordinate_marker_color = coordinate_marker_color,
    graph_color = graph_color, 
    equalation = equalation
    ))
  file.close()

#execute file and print finished if fails (idk why)
def calculate(Calc):
  try:Calc()
  except:print("finished")

#main method
def main():
  input_equalation = input("please type in your equalation (sin()-->math.sin()): ")
  input_range_x = input("please type in the x range to both side you whant to plot (float>0, default=5): ")
  input_range_y = input("please type in the y range to both side you whant to plot (float>0, default=5): ")
  input_orientation_point_distance_x = input("please type in the distance between the x orientation points (float>0, default=0.5): ")
  input_orientation_point_distance_y = input("please type in the distance between the y orientation points (float>0, default=0.5): ")
  input_resolution_x = input("please type in the x resolution (int>0, default=500): ")
  input_resolution_y = input("please type in the y resolution (int>0, default=500): ")
  input_offset_x = input("please type in the x offset (int, default=0): ")
  input_offset_y = input("please type in the y offset (int, default=0): ")
  input_grid = input("please type in if you whant a grid (bool, default=False): ")
  create_file(equalation=input_equalation, 
    x_range=input_range_x, 
    y_range=input_range_y, 
    x_guide_point_distance=input_orientation_point_distance_x, 
    y_guide_point_distance=input_orientation_point_distance_y, 
    x_resolution=input_resolution_x, 
    y_resolution=input_resolution_y, 
    x_offset=input_offset_x, 
    y_offset=input_offset_y, 
    grid_bool=input_grid)
  import Calculation as Calc
  calculate(Calc)

#run
main()