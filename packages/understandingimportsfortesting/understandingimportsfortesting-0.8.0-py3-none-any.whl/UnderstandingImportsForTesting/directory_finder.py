import os
from pathsingleton.root_path import RootPath


class LocateDirectory:
    def __init__(self):
        pass

    def input_dir_pointer(self):
        input_dir = os.path.join("/Users/ydasari/PycharmProjects/understanding_imports", "Input_folder")
        print("Complete input directory:", input_dir)
        return input_dir

    def using_path_singleton(self):
        # main_dir = os.path.join(RootPath.instance().cwd, "src")
        # print("Using pathsingleton", main_dir)

        working_dir = RootPath.instance().cwd
        src_path = os.path.dirname(__file__)

        input_dir = os.path.join(working_dir, "Input_folder")

        print("Using pathsingleton:", input_dir)
        return input_dir
