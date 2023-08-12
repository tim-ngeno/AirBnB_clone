#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpretor"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the command interpretor"""
        return True

    def emptyline(self):
        """Emptyline + ENTER does nothing"""
        pass

    def do_EOF(self, arg):
        """End of file"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
