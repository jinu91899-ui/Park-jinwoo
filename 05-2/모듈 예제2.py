import os


def read_folder(path):
    output = os.listdir(path)
    for item in output:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            read_folder(item_path)
        else:
            print("파일: ", item)


read_folder(".")