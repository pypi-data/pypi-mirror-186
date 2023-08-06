from os import walk
import os

try:
    from nrobo.config import nRoboConfig
except ModuleNotFoundError as e:
    from config import nRoboConfig


# Get list of test files under given folder
def get_list_of_files(folder, file_extension, ignore_file_names=[]):
    """
    Get and return list of files with given extension inside given folder

    :param folder:
    :param file_extension:
    :param ignore_file_names:
    :return:
    """

    # folder path
    dir_path = folder

    # list to store files name
    res = []
    for (dir_path_, dir_names, file_names) in walk(dir_path):
        """
        Loop through all directories and subdirectories
        """

        for file_name in file_names:
            """
            Loop thorugh all files
            """

            # print(dir_path_ + "<>" + file_name)
            f_name, f_extension = os.path.splitext(file_name)
            if f_extension == file_extension:
                match_found = False
                for ignore_file_name in ignore_file_names:
                    if f_name == ignore_file_name:
                        match_found = True
                        break
                if not match_found:
                    res.append(dir_path_ + os.sep + file_name)

    return res


def list_test_files_for_launcher(dirname):
    """
    Get and return list of test files in given directory

    :param dirname:
    :return:
    """

    test_files = ""
    list_of_test_files = get_list_of_files(dirname, ".py", ["__init__"])
    for test_file_name in list_of_test_files:
        test_files = test_files + nRoboConfig.Constants.SPACE.value + test_file_name

    return test_files
