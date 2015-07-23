#!/usr/bin/python
# https://github.com/AbelJoo/Move-Fucking-Android-Resources


import os
import shutil

__author__ = 'abel'

__source_path = None
__target_path = None


def user_task_config_source_path():
    global __source_path
    data = __u_input("请输入待导入的资源目录路径：")
    __source_path = data if data != "" else __source_path


def user_task_config_target_path():
    global __target_path
    data = __u_input("请输入目标工程的res目录路径：")
    __target_path = data if data != "" else __target_path


def user_task_copy_resource():
    resource_names = [file_name for file_name in os.listdir(__source_path) if not os.path.isdir(file_name)]

    def check_res(source_path, target_path):
        print(os.path.split(source_path)[1] + "\n将会被拷贝到 " + target_path)

    def copy_res(source_path, target_path):
        shutil.copyfile(source_path, target_path)
        print(target_path + str(" 已生成"))

    def operation(function):
        __operation_resource_with_condition("drawable-xhdpi", "xh_", resource_names, function)
        __operation_resource_with_condition("drawable-xxhdpi", "xxh_", resource_names, function)

    operation(check_res)

    command = __u_input("是否继续？（Y/N）")
    if not (command == "y" or command == "Y"):
        print("操作已取消")
        return

    operation(copy_res)

    print("已完成" + str(len(resource_names)) + "个资源文件分类")


def user_task_show_help():
    print("")
    print("命令列表：")
    print("copy\t\t从资源目录分类拷贝文件到工程res资源目录")
    print("cs\t\t(config source)设置待导入的资源目录路径")
    print("st\t\t(config target)设置目标工程的res目录路径")
    print("info\t\t当前脚本配置信息")
    print("\nMove-Fucking-Android-Resources 如何使用？")
    print("Step1:\n将需要导入到工程的资源文件按尺寸命名，如xh_arrow.png xxh_arrow.png xh_background.png xxh_background.png，以此类推")
    print("Step2:\n将Step1中的所有资源文件放到同一目录下，并执行“cs”，设置为该目录路径")
    print("Step3:\n执行“ct”，设置为您项目工程的资源文件目录（res目录,即drawable-xhdpi，drawable-xxhdpi等资源目录的父目录）")
    print("Step4:\n执行“copy”，上述Step1中的xh_前缀文件将拷贝到资源目录下的drawable-xhdpi，以此类推")
    print("")


def user_task_show_info():
    print("当前待导入的资源目录路径：\n" + __get_source_path())
    print("当前目标工程的res目录路径：\n" + __get_target_path())


def __u_input(message=""):
    """
    自定义的input
    :param message:
    :return:
    """

    return input(">>>" + message)


def __get_source_path():
    return __source_path


def __get_target_path():
    return __target_path


def __operation_resource_with_condition(target_dir_name,
                                        prefix,
                                        resource_names,
                                        function):
    """
    对指定前缀的资源及所给的目录进行function操作
    :param target_dir_name: 目标分类目录名称
    :param prefix: 资源标记前缀
    :param resource_names: 资源文件名集合
    :param function: 传入一个方法。该方法务必能够接受两个参数：第一个参数是源文件完整路径，第二个参数是目标文件生成的完整路径
    :return:
    """

    resource_names = [resource for resource in resource_names if str(resource).startswith(prefix)]

    target_dir_path = os.path.join(__target_path, target_dir_name)
    if not os.path.exists(target_dir_path):
        os.mkdir(target_dir_path)

    for resource_name in resource_names:
        source = os.path.join(__source_path, resource_name)
        target = os.path.join(target_dir_path, resource_name[len(prefix):])
        function(source, target)


def __loop():
    while True:
        __command_distribution(__u_input())


def __command_distribution(command):
    """
    命令分发
    :param command:
    :return:
    """

    if command == "cs":
        user_task_config_source_path()
    elif command == "ct":
        user_task_config_target_path()
    elif command == "copy":
        user_task_copy_resource()
    elif command == "help":
        user_task_show_help()
    elif command == "info":
        user_task_show_info()
    else:
        print("无效命令。如需帮助，请键入“help”")


def __start():
    user_task_config_source_path()
    user_task_config_target_path()

    print("配置完成。")
    user_task_show_info()
    print("如需帮助，请键入“help”")

    __loop()


if __name__ == '__main__':
    print("")
    print("#######################################################")
    print("#                                                     #")
    print("#      Welcome to Move-Fucking-Android-Resources      #")
    print("#  github.com/AbelJoo/Move-Fucking-Android-Resources  #")
    print("#                                                     #")
    print("#######################################################")
    print("")
    __start()