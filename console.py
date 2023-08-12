#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpretor"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the command interpretor"""
        return True

    #def emptyline(self):
        #"""Emptyline + ENTER does nothing"""
        #pass

    def do_EOF(self, line):
        """End of file"""
        print()
        return True

   # def do_create(self, arg):
    """Creates a new instance of BaseModel and prints its id"""
    #if not arg:
     #   print("** class name missing **")
    #elif arg not in HBNBCommand.classes:
     #   print("**class doesn't exist**")
    #else:

if __name__ == '__main__':
    HBNBCommand().cmdloop()
