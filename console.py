#!/usr/bin/python3
"""contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    """
    prompt = "(hbnb) "
    airbnb_engine_classes = {
        "BaseModel": BaseModel
    }

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
            base_model = self.airbnb_engine_classes[arg]()
            base_model.save()
            print(base_model.id)
        except KeyError as ex:
            print("** class doesn't exist **")

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
                print("** class doesn't exist *")
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
                print("** class doesn't exist *")
                return

        except ValueError as ex:
            print("** instance id missing **")
            return

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
