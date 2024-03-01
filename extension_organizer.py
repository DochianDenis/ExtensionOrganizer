import os
import shutil
from pathlib import Path

print("""Choose the directory you want to organize:
1. Downloads
2. Documents
3. Desktop
4. Pictures
5. Videos
6. Choose another directory
""")

option = int(input())

match option:
    case 1:
        if os.path.isdir(os.path.join(Path.home(), "Downloads")):
            directory = os.path.join(Path.home(), "Downloads")
        else:
            print("The Downloads directory does not exist")
    case 2:
        if os.path.isdir(os.path.join(Path.home(), "Documents")):
            directory = os.path.join(Path.home(), "Documents")
        else:
            print("The Documents directory does not exist")
    case 3:
        if os.path.isdir(os.path.join(Path.home(), "Desktop")):
            directory = os.path.join(Path.home(), "Desktop")
        else:
            print("The Desktop directory does not exist")
    case 4:
        if os.path.isdir(os.path.join(Path.home(), "Pictures")):
            directory = os.path.join(Path.home(), "Pictures")
        else:
            print("The Picture directory does not exist")
    case 5:
        if os.path.isdir(os.path.join(Path.home(), "Videos")):
            directory = os.path.join(Path.home(), "Videos")
        else:
            print("The Videos folder does not exist")
    case 6:
        directory = input("Enter the path to the folder:")
    case _ :
        print("The option", option, "does not exist")


print(directory)

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
            extension_directory = os.path.join(directory, extension)
            if not os.path.isdir(extension_directory):
                os.mkdir(extension_directory)
                folders_created += 1
            shutil.move(file_path, extension_directory)
            moved_files += 1

else:
    print("The directory that you specified does not exist")
    
