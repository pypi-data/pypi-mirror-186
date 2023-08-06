from os import walk
import os
import shutil
from nrobo.helpers import common

# list to store files name
root = "nrobo"
assets = "assets"
target = "nrobo-backup"
res = []


# copy assets folder
if os.path.exists(target):
    # delete directory
    pass
else:
    shutil.copytree(root + os.sep + assets, target + os.sep + assets)

for (dir_path_, dir_names, file_names) in walk(root):
    """
    Loop through all directories and subdirectories
    """

    if "__pycache__" in dir_path_ or root + os.sep + assets in dir_path_:
        continue
    else:
        print("================================")
        print(dir_path_)

    print(dir_names)
    print(file_names)

    for filename in file_names:

        f_name, f_extension = os.path.splitext(filename)

        if f_extension == ".py":
            print(filename)
            # create file
            print("current directory path: " + dir_path_.replace(root, target))
            common.Common.write_text_to_file(target+os.sep+filename, "from " + dir_path_ + " import " + filename + "\n")

