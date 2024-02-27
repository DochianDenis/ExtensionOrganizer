import os
import shutil

directory = input("Enter the path to the directory that you want to organize: ")

if os.path.isdir(directory):
    files = os.listdir(directory)
    
    moved_files = 0
    folders_created = 0
    
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            continue
        else:
            root, extension = os.path.splitext(file_path)
            check_directory = os.path.join(directory, extension)
            if not os.path.isdir(check_directory):
                os.mkdir(check_directory)
                folders_created += 1
                
                
else:
    print("The directory that you specified does not exist")
    
