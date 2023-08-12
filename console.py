#!/usr/bin/python3
"""Importing modules"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpretor"""

    prompt = '(hbnb) '

    classes = {
                'BaseModel': BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review
                }

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

    def do_create(self, arg):
        """ Creates new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """ Prints string representation of an instance
        based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            instance = arg.split(' ')
            if instance[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(instance) < 2:
                print("** instance id missing **")
            else:
                keys = "{}.{}".format(instance[0], instance[1])
                if keys not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[keys])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
