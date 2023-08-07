# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-01-19 19:23:57
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's zip methods.
"""


from typing import Optional
from zipfile import ZipFile, is_zipfile, ZIP_DEFLATED
import os

from .rbasic import error


def zip_data(path: str, build_dir: Optional[str] = None, format: str = "zip", overwrite: bool = True) -> None:
    """
    Zip file or folder.

    Parameters
    ----------
    path : File or folder path.
    build_dir : Build directory.
        - None : Work directory.
        - str : Use this value.
    
    format : Build file format.
    overwrite : Whether overwrite file.
    """

    if build_dir == None:
        build_dir = os.getcwd()
    if overwrite:
        mode = "w"
    else:
        mode = "x"

    basename = os.path.basename(path)
    file_name = os.path.splitext(basename)[0]
    build_file_name = "%s.%s" % (file_name, format)
    build_path = os.path.join(build_dir, build_file_name)
    with ZipFile(build_path, mode, ZIP_DEFLATED) as zip_file:
        zip_file.write(path, basename)
        is_dir = os.path.isdir(path)
        if is_dir:
            dirname = os.path.dirname(path)
            dirname_len = len(dirname)
            dirs = os.walk(path)
            for folder_name, sub_folders_name, files_name in dirs:
                for sub_folder_name in sub_folders_name:
                    sub_folder_path = os.path.join(folder_name, sub_folder_name)
                    zip_path = sub_folder_path[dirname_len:]
                    zip_file.write(sub_folder_path, zip_path)
                for file_name in files_name:
                    file_path = os.path.join(folder_name, file_name)
                    zip_path = file_path[dirname_len:]
                    zip_file.write(file_path, zip_path)

def unzip_data(path: str, build_dir: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Unzip file or folder.

    Parameters
    ----------
    path : File or folder path.
    build_dir : Build directory.
        - None : Work directory.
        - str : Use this value.
    
    passwrod : Unzip Password.
        - None : No Unzip Password.
        - str : Use this value.
    """

    is_support = is_zipfile(path)
    if not is_support:
        error_text = "unsupported file format"
        error(error_text)
    
    with ZipFile(path) as zip_file:
        zip_file.extractall(build_dir, pwd=password)

def azip(path: str, build_dir: Optional[str] = None) -> None:
    """
    Automatic judge and zip or unzip file or folder.
    
    Parameters
    ----------
    path : File or folder path.
    build_dir : Build directory.
        - None : Work directory.
        - str : Use this value.
    """

    is_support = is_zipfile(path)
    if is_support:
        unzip_data(path, build_dir)
    else:
        zip_data(path, build_dir)