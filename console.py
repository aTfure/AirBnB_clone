#!/usr/bin/python3
"""contains the entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program
        """
        return True

    def do_quit(self, line):
        """exit the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
