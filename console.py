#!/usr/bin/python3
"""Importing modules"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpretor"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpretor"""
        return True

    def do_EOF(self, arg):
        """End of file"""
        print()
        return True

    def emptyline(self):
        """Emptyline and ENTER does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
