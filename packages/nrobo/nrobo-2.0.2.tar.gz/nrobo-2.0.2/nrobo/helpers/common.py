import inspect
import json
import locale
import os.path as path
import random
import string
import sys
from builtins import FileNotFoundError
from time import time

# import speedtest

try:
    import yaml
    from termcolor import colored
except ModuleNotFoundError as e:
    try:
        import yaml
    except ModuleNotFoundError as e:
        pass


class Common:
    """
    Customized Selenium WebDriver class which contains all the useful methods that can be re used.
    These methods _help to in the following cases:
    To reduce the time required to write automation script.
    To take the screenshot in case of test case failure.
    To log to provide waits
    """

    color_info = 'magenta'
    color_info_on = 'on_blue'
    color_error = 'red'
    color_error_on = color_info_on
    color_success = 'green'
    color_attribute = ['concealed']

    @staticmethod
    def read_file_as_string(file_path, encoding=None):
        """
        Read file as string

        :param file_path:
        :param encoding:
        :return:
        """

        try:
            if encoding is None:
                with open(file_path, "r") as f:
                    content = f.read()
                    return content
            else:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return content
        except FileNotFoundError as file_not_found_error:
            Common.print_error("No such file or directory found: " + file_path)

    @staticmethod
    def write_text_to_file(file_path, content, encoding=None):
        """
        Write text to file

        :param file_path:
        :param content:
        :param encoding:
        :return:
        """

        try:
            if encoding is None:
                with open(file_path, 'w') as f:
                    f.write(content)
            else:
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(content)

        except FileNotFoundError as file_not_found_error:
            Common.print_error("No such file or directory found: " + file_path)

    @staticmethod
    def read_json(file_path):
        """
        Read Json

        :param file_path:
        :return:
        """

        try:

            with open(file_path) as f:
                data = json.load(f)
                return data

        except FileNotFoundError as file_not_found_error:
            Common.print_error("No such file or directory found: " + file_path)

    @staticmethod
    def write_json(file_path, dictionary):
        """
        Write dictionary data to file

        :param file_path: Path of file where dictionary date is going to be stored
        :param dictionary: Dictionary of data
        :return:
        """

        with open(file_path, 'w') as file:  # Open given file in write mode
            json.dump(dictionary, file, sort_keys=True, indent=4)

    @staticmethod
    def is_file_exist(file_path):
        """
        Checks if given file exists or not.

        :param file_path: Path of file
        :return: True if file exists else return False
        """
        return path.exists(file_path)

    @staticmethod
    def read_yaml(file_path):
        """
        Read yaml file at given path

        :param file_path: Path of file
        :return: Content of yaml file -> dict()
        """

        if not path.exists(file_path):
            """if file does not exist, then let's create it first"""

            with open(file_path, 'w') as file:
                """Create a file"""

                # initialize file with empty dictionary
                yaml.dump({}, file)
        else:
            """Do Nothing as file exists"""

        # Read the file
        with open(r'{0}'.format(file_path)) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.SafeLoader)

            # return with data as dictionary
            return data

    @staticmethod
    def write_yaml(file_path, dictionary):
        """
        Write dictionary data to given file path in yaml format

        :param file_path: Path of file where dictionary data needs to be stored
        :param dictionary: Dictionary data
        :return: Nothin
        """

        with open(file_path, 'w') as file:  # Open given file in write mode
            yaml.dump(dictionary, file)

    @staticmethod
    def convert_string_dictionary_to_dictionary(string_dictionary):
        """
        Converts given string dictionary to dictionary object

        :param string_dictionary:
        :return: dict() Obj
        """

        return json.loads(string_dictionary)

    @staticmethod
    def generate_random_string(length):
        """
        Generate random string

        :param length: length
        :return: str -> Random string of given length
        """

        random_string = ''.join(random.choices(string.ascii_lowercase +
                                               string.digits + string.ascii_uppercase, k=length))
        return random_string

    @staticmethod
    def get_os():
        """
        Return platform name

        :return: str -> Platform name
        """

        platform = sys.platform

        return platform

    # @staticmethod
    # def download_speed():
    #
    #     st = speedtest.Speedtest()
    #
    #     return int(st.download() / 1024 / 1024)  # return download speed in Mb/Sec

    # @staticmethod
    # def upload_speed():
    #
    #     st = speedtest.Speedtest()
    #
    #     return int(st.upload() / 1024 / 1024)  # return upload speed in Mb/Sec

    @staticmethod
    def time():
        """
        Return current time

        :return:
        """

        return time()

    @staticmethod
    def log_page_load_time(page_name, start_time, end_time):
        """
        Print page load time

        :param page_name:
        :param start_time:
        :param end_time:
        :return:
        """
        # internet_speed = Common.download_speed()
        # print(colored("\n Speed: {} Load Time: {} Seconds, Page: {}".
        #              format(internet_speed, int(end_time - start_time), page_name), color_info))
        print(colored("\n[\n\tLoad Time: {} Seconds, \n\tMax Load Time: {} Seconds, \n\tPage: {} \n\tHost Internet "
                      "Speed: {} Mbps\n] "
                      .format(int(end_time - start_time), int(config.wait), page_name, config_v2.internet_speed),
                      color_info))

    @staticmethod
    def is_a_None(anything):
        """
        Check if given parameter is of type, None

        :param anything:
        :return: Returns True if anything is None else returns False
        """

        if type(anything) is type(None):  # Check if _type of anything is None
            return True  # return True if Yes
        else:
            return False  # return False if No

    @staticmethod
    def get_list_of_all_supported_apps():
        """
        Get list of all supported app. Depricated for the time being.

        :return:
        """

        # all module candidates
        candidates = dir(apps)

        # variable to hold variables only
        supported_apps = []

        for name in candidates:
            """loop through all candidates"""

            # get attribute
            obj = getattr(apps, name)

            if not (
                    inspect.isclass(obj) or
                    inspect.isfunction(obj) or
                    inspect.ismodule(obj) or
                    "__" in name
            ):
                # append to variables list
                # print(name)
                supported_apps.append(obj)

        # return list of supported apps
        return supported_apps

    @staticmethod
    def print_error(message):
        """
        Prints given message as error

        :param message:
        :return:
        """

        print(message)

    @staticmethod
    def print_info(message):
        """
        Prints given message as information

        :param message:
        :return:
        """

        print(message)

    @staticmethod
    def print_success(message):
        """
        Prints given message as success

        :param message:
        :return:
        """
        print(message)

    @staticmethod
    def generate_random_numbers(min, max):
        """
        Generate and return a random number in given range denoted by min and max

        :param min:
        :param max:
        :return:
        """
        """
        Returns a random string of given length

        @Returns string a random string
        """
        random_number = random.randint(min, max)

        return random_number


class DatetimeEncoder(json.JSONEncoder):
    """
    Encode date time

    Not yet sure, why I had created!!!

    """

    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)
