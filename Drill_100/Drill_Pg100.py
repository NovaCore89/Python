
# Script for locating .txt files within a directory, establishing the absolute path and last time modified

import os, time


# Block for displaying the 10 files within the directory
path = "C:\\Drill_Pg100\\"
dir_list = os.listdir(path)

print(dir_list)

# Block for locating the .txt files and displaying the absolute file path
for files in dir_list:
    if files.endswith(".txt"):
        print(os.path.join("C:\\Drill_Pg100\\", files))

# Block for checking the last modified date of .txt files within the directory

fpath = "C:\\Drill_Pg100\\"

for files in dir_list:
    if files.endswith(".txt"):
        print(os.path.getmtime(fpath))

modification_time = os.path.getmtime(fpath) 
print("Last modification time:", modification_time)
  







