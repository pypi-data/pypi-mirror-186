#!/usr/bin/python3

import importstest.directory_finder


def main():
    input_folder = importstest.directory_finder.LocateDirectory()
    input_dir = input_folder.input_dir_pointer()
    main_dir = input_folder.using_path_singleton()


if __name__ == "__main__":
    main()
