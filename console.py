#!/usr/bin/python3
"""contains the entry point of the command interpreter
"""
import cmd
import re
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    """
    prompt = "(hbnb) "
    airbnb_engine_classes = {
        "User": User,
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        """Handles empty line
        """
        pass

    def do_EOF(self, arg):
        """exit the program
        """
        return True

    def do_quit(self, arg):
        """exit the program
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file)
            and prints the id
            Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            base_model = self.airbnb_engine_classes[args[0]]()
            base_model.save()
            print(base_model.id)
        except KeyError as ex:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id
        $ show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, id = arg.split()
            if class_name in self.airbnb_engine_classes:
                key = class_name + "." + id
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                    return
                else:
                    print(objects[key])
                    return

            else:
                print("** class doesn't exist ***")
                return

        except ValueError as ex:
            print("** instance id missing **")
            return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, id = arg.split()
            if class_name in self.airbnb_engine_classes:
                key = class_name + "." + id
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                    return
                else:
                    del objects[key]
                    storage.save()
                    return

            else:
                print("** class doesn't exist **")
                return

        except ValueError as ex:
            print("** instance id missing **")
            return

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        $ all BaseModel or $ all.
        """
        value_list = []
        objects = storage.all()

        if not arg:
            for value in objects.values():
                value_list.append(value.__str__())
            print(value_list)
            return

        if arg in self.airbnb_engine_classes:
            for value in objects.values():
                if arg == type(value).__name__:
                    value_list.append(value.__str__())
            print(value_list)
            return
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234
            email "aibnb@mail.com".
        """
        _input = shlex.split(_input)
        query_key = ''

        if len(_input) == 0:
            print("** class name missing **")
            return
        if _input[0] not in self.airbnb_engine_classes:
            print("** class doesn't exist **")
            return
        if len(_input) == 1:
            print("** instance id missing **")
            return
        if len(_input) > 1:
            query_key = _input[0] + '.' + _input[1]
        if query_key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(_input) == 2:
            print('** attribute name missing **')
            return
        if len(_input) == 3:
            print('** value missing **')
            return
        key_name = _input[2]
        input_value = _input[3]
        setattr(storage.all()[query_key], key_name, input_value)

        storage.all()[query_key].save()

    def default(self, arg):
        """Handles defaults arguments not created
        """
        count = 0
        args = arg.split(".")

        if args[0] in self.airbnb_engine_classes and args[1] == "all()":
            self.do_all(args[0])
        elif args[0] in self.airbnb_engine_classes and args[1] == "count()":
            if (args[0] not in self.airbnb_engine_classes):
                print("** class doesn't exist **")
                return (False)
            else:
                for key in storage.all():
                    if key.startswith(args[0]):
                        count += 1
                print(count)
        elif args[0] in self.airbnb_engine_classes and \
                args[1].startswith('show'):
            arg = args[1].split('"')
            if len(arg) == 3:
                arg1 = args[0] + " " + arg[1]
                self.do_show(arg1)
        elif args[0] in self.airbnb_engine_classes and \
                args[1].startswith('destroy'):
            arg = args[1].split('"')
            if len(arg) == 3:
                arg1 = args[0] + " " + arg[1]
                self.do_destroy(arg1)
        elif args[0] in self.airbnb_engine_classes and \
                args[1].startswith('update'):
            start = 'update('
            end = ')'
            arg = re.findall(re.escape(start)+"(.*)" +
                             re.escape(end), args[1])[0]
            arg = arg.replace('(', '').replace(')', '').replace(',', '')
            arg = arg.replace('"', '')
            arg1 = args[0] + " " + arg
            self.do_update(arg1)
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
