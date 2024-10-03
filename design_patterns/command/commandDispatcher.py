class Command:
    def execute(self):
        pass


class Copy:
    def execute(self):
        print("copying")


class Paste:
    def execute(self):
        print("pasting")


class CommandDispatcher:
    def __init__(self):
        self.__commands = {}

    def add_command(self, name, command):
        self.__commands[name] = command

    def run_command(self, name):
        self.__commands[name].execute()


if __name__ == "__main__":
    dispatcher = CommandDispatcher()
    dispatcher.add_command("copy", Copy())
    dispatcher.add_command("paste", Paste())

    dispatcher.run_command("copy")
    dispatcher.run_command("paste")

