import resources_task

__author__ = 'abel'


def __help():
    print("this is help")


def __loop_command():
    while True:
        command = input()
        if command == "source":
            resources_task.config_source_path()
        elif command == "target":
            resources_task.config_target_path()
        elif command == "help":
            __help()


def __start():
    # task.config_source_path()
    # task.config_target_path()
    resources_task.copy_resource()

    __loop_command()


if __name__ == '__main__':
    print("__main__")
    __start()