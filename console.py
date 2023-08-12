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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            my_instance = line.split(' ')
            if my_instance[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(my_instance) < 2:
                print("** instance id missing **")
            else:
                keys = "{}.{}".format(my_instance[0], my_instance[1])
                if keys not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[keys]
                    storage.save()

    def do_all(self, line):
        """ Prints string representation of all instances"""
        my_list = []

        if line:
            line = line.split(' ')[0]
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == line:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(my_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
