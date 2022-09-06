from package_file_reader.src.package_file_reader.message import *
import json
import os
import xmltodict

__file_name= None
__path = None



def read_file()-> dict: 
    """Method to read csv with format csv

    Raises:
        FileNotFoundError: throw exception when No such file or directory.

    Returns:
        dict: return a dic with all data structured
    """
    try:
        path = __path + __file_name
        with open(path, "r") as json_file:
            result = json.load(json_file)
            return result
    except Exception as e:
        raise FileNotFoundError(e)


def check_logical_file_size(size=None):
    """Method to check file size in path, in case the file size satisfy the validation

    Args:
        size (int, optional): size value of file readed. Defaults to None.
    
    Raises:
        Exception: throw exception in case of error

    Returns:
        boolean: return a boolean to be validated .
    """
    try:
        path = __path + __file_name   
        file_size = os.path.getsize(path)
        flag=True
        if file_size < size:
            flag=False
        
        return flag
    except Exception as e:
        raise Exception(e)


def check_parameter_file(parameter=None):
    """Method to validate parameters parameter size in file

    Args:
        parameter (string, optional): value of the json readed. Defaults to None.

    Raises:
        Exception: throw exception when parameter is not valid

    Returns:
        boolean: return a boolean to be validated
    """
    try:
        file = read_file()  
        flag=True
        if len(file[parameter]) <= 0 :
            flag=False
        
        return flag
    except Exception as e:
      raise KeyError(e)



def set_path(path:None):
    """Method to set path configuration

    Args:
        path (None): path of file
    """
    global __path 
    __path = path



def get_path():
    """Method to get path configuration

    Returns:
        string: value of path
    """
    return __path



def set_file_name(file:None):
    """Method to set file configuration

    Args:
        file (None): seter the file name
    """
    global __file_name
    __file_name=file



def get_file_name():
    """Method to get file configuration

    Returns:
        string: the name file
    """
    return __file_name


def xml_to_dict(data : None)->str:
    """_summary_
    Method to convert an String XML struct in Json object
    Args:
        data (None): str xml to convert in json object
    Raises:
        Exception: Launch exception in case of not convert to json
    Returns:
        str: json
    """
    try:
        if bool(data) != False :
            return xmltodict.parse(str(data).strip())
        else:
            raise Exception(message_reader.ERROR_SIZE_XML_TO_DICT)     
    except Exception as e:
        raise Exception(e)
