import configparser
import sys
import os


def get_version():
    config = configparser.ConfigParser()

    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    config_file_path = os.path.join(parent_directory, 'setup.cfg')

    config.read(config_file_path)

    print('current_directory', current_directory)
    print('parent_directory', parent_directory)
    print('config_file_path', config_file_path)
    print(config['warise-first']['version'])
    print('sys.argv', sys.argv)

    return config['warise-first']['version']

if __name__ == '__main__':
    print(sys.argv)
    if '--version' in sys.argv:
        print(get_version())
