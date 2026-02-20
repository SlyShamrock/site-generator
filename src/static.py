import os
import shutil

def copy_content(source, destination):
    exists = os.path.exists(destination)
    if exists:
        shutil.rmtree(destination)
    os.mkdir(destination)
    list = os.listdir(source)
    for item in list:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        i = os.path.isfile(source_path)
        if i == True:
            shutil.copy(source_path, destination_path)
        else:
            copy_content(source_path, destination_path)