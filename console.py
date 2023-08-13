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
import shlex


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
                    my_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                my_list.append(str(v))

        print(my_list)

    def do_update(self, line):
        """
         Updates an instance based on the class name and id by adding or
         updating attribute (saves the change into JSON file)"""
        instance = shlex.split(line)
        my_integers = ["number_rooms", "number_bathrooms", "max_guest",
                       "price_by_night"]
        my_floats = ["latitude", "longitude"]
        if len(instance) == 0:
            print("** class name missing **")
        elif instance[0] in HBNBCommand.classes:
            if len(instance) > 1:
                k = instance[0] + "." + instance[1]
                if k in storage.all():
                    if len(instance) > 2:
                        if len(instance) > 3:
                            if instance[0] == "Place":
                                if instance[2] in my_integers:
                                    try:
                                        instance[3] = int(instance[3])
                                    except ValueError:
                                        instance[3] = 0
                                elif instance[2] in my_floats:
                                    try:
                                        instance[3] = float(instance[3])
                                    except ValueError:
                                        instance[3] = 0.0
                            setattr(storage.all()[k], instance[2], instance[3])
                            storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
