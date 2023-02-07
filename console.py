#!/usr/bin/python3
"""Defines the HBNB"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBNB Command interpreter.
    Attributes:
        prompts (str): The command prompt.
    """

    prompt = "(hbnb)"
    __classes = {
        "BaseModel"
    }

    def emptyline(self):
        """Do Nothing upon receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
