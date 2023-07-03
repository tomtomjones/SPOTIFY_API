import os
import configparser

module_path = os.path.dirname(os.path.abspath(__file__))  ##absolute path, relevant to all machines
config_file = os.path.join(module_path,"config.ini")

config = configparser.ConfigParser()
config.read(config_file)

def get_config_value(section, key):
    return config.get(section,key)