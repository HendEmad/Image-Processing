import obstacles_detection
occupied_grids, planned_path = obstacles_detection.main("img_1.png")
print ("Occupied Grids : ")
print (occupied_grids)
print ("Planned Path :")
print (planned_path)