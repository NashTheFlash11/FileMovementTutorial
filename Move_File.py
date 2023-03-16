import os
import shutil

from_dir = "/Users/nashwanhaque/Downloads"
# Make sure to change your to_dir 
to_dir = "/Users/nashwanhaque/Desktop/Tutorial_folder"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.png', 'jpg', '.jpeg', '.gif', '.webp']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Photos"
        path3 = to_dir + '/' + "Photos" + '/' + file_name

        print("path1", path1)
        print("path2", path2)
        print("path3", path3)

        if os.path.exists(path2):
            print("Moving " + file_name + '....')

            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + '....')
            shutil.move(path1, path3)