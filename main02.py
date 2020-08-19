from exercise02 import count_people, create_list_from_file

if __name__ == "__main__":
  print("Count people:", count_people("data01.txt"))
  
  grid = create_list_from_file("grid01.txt")
  print("grid[1][0] == '", grid[1][0], "'")
  print("grid[1][1] == '", grid[1][1], "'")
  
  grid2 = create_list_from_file("grid02.txt")
  print("grid2 has", len(grid2), "lines")
