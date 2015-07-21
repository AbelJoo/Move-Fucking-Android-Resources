import os
import shutil

__author__ = 'abel'

__source_folder__ = "/home/abel/桌面/source/"
__target_folder__ = "/home/abel/桌面/target/"


def config_source_folder():
    __source_folder = input("请输入来源目录：")
    if not __source_folder.endswith("/"):
        __source_folder += "/"


def config_target_folder():
    __target_folder = input("请输入目标目录：")
    if not __target_folder.endswith("/"):
        __target_folder += "/"


def __copy_resource_to_dir(target_dir_path, prefix, resource_names):
    """

    :param target_dir_path: 目标目录路径
    :param prefix: 资源标记前缀
    :param resource_names: 资源文件名集合
    :return:
    """
    resource_names = [resource for resource in resource_names if str(resource).startswith(prefix)]
    if not os.path.exists(target_dir_path + '/'):
        os.mkdir(target_dir_path + "/")
    for resource_name in resource_names:
        shutil.copyfile(__source_folder__ + resource_name, target_dir_path + "/" + resource_name)


def copy_resource():
    resource_names = [file_name for file_name in os.listdir(__source_folder__) if not os.path.isdir(file_name)]
    __copy_resource_to_dir(__target_folder__ + "xh_dir_dir_dir" + "/", "xh", resource_names)