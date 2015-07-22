import os
import shutil

__author__ = 'abel'

__source_path = "/ssd/Abel/documents/Super/Android,iOS-Client-Social/下课聊/切图/发布"
__target_path = "/home/abel/桌面/target"


def config_source_path():
    global __source_path
    __source_path = input("请输入来源目录：")


def config_target_path():
    global __target_path
    __target_path = input("请输入目标目录：")


def get_source_path():
    return __source_path


def get_target_path():
    return __target_path


def __copy_resource_to_dir(target_dir_name, prefix, resource_names):
    """
    将指定前缀的资源放入指定名字的目录
    :param target_dir_name: 目标分类目录名称
    :param prefix: 资源标记前缀
    :param resource_names: 资源文件名集合
    :return:
    """

    resource_names = [resource for resource in resource_names if str(resource).startswith(prefix)]

    target_dir_path = os.path.join(__target_path, target_dir_name)
    if not os.path.exists(target_dir_path):
        os.mkdir(target_dir_path)

    for resource_name in resource_names:
        source = os.path.join(__source_path, resource_name)
        target = os.path.join(target_dir_path, resource_name[len(prefix):])
        shutil.copyfile(source, target)
        print(resource_name + str("\n已拷贝到 ") + target)


def copy_resource():
    resource_names = [file_name for file_name in os.listdir(__source_path) if not os.path.isdir(file_name)]
    __copy_resource_to_dir("xh_drawable", "xh_", resource_names)
    __copy_resource_to_dir("xxh_drawable", "xxh_", resource_names)
    print("已完成" + str(len(resource_names)) + "个资源文件分类")