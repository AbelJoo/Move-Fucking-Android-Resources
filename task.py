import os
import shutil

__author__ = 'abel'

__source_path__ = "/ssd/Abel/documents/Super/Android,iOS-Client-Social/下课聊/切图/发布/"
__target_path__ = "/home/abel/桌面/target/"


def config_source_folder():
    __source_folder = input("请输入来源目录：")
    if not __source_folder.endswith("/"):
        __source_folder += "/"


def config_target_folder():
    __target_folder = input("请输入目标目录：")
    if not __target_folder.endswith("/"):
        __target_folder += "/"


def __copy_resource_to_dir(target_dir_name, prefix, resource_names):
    """

    :param target_dir_name: 目标分类目录名称
    :param prefix: 资源标记前缀
    :param resource_names: 资源文件名集合
    :return:
    """
    target_dir_path = __target_path__ + target_dir_name + "/"
    resource_names = [resource for resource in resource_names if str(resource).startswith(prefix)]
    if not os.path.exists(target_dir_path):
        os.mkdir(target_dir_path)
    for resource_name in resource_names:
        shutil.copyfile(__source_path__ + resource_name, target_dir_path + resource_name)


def copy_resource():
    resource_names = [file_name for file_name in os.listdir(__source_path__) if not os.path.isdir(file_name)]
    __copy_resource_to_dir("xh_drawable", "xh", resource_names)
    __copy_resource_to_dir("xxh_drawable", "xxh", resource_names)