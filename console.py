#!/usr/bin/python3

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnB console. Type help or ? to ist commands.\n'
    prompt = '(hbnb) '

    def do_create(self, arg):
        '''
Creates a new instance of BaseModel,
saves it (to the JSON file) and prints the id.
Ex: $ create BaseModel
        '''
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)

    def do_show(self, *arg):
        '''
Prints the string representation of an instance
based on the class name and id.
Ex: $ show BaseModel 1234-1234-1234
        '''
        if arg[0] == "":
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg[1] == "":
            print("** instance id missing **")
            # Incomplete, still waiting for FileStorage

    def do_destroy(self, *arg):
        '''
Deletes an instance based on the class name
and id (save the change into the JSON file).
$ destroy BaseModel 1234-1234-1234
        '''
        if arg[0] == "":
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg[1] == "":
            print("** instance id missing **")
            # Incomplete, still waiting for FileStorage

    def do_all(self, arg):
        '''
Prints all string representation of all instances
based or not on the class name.
Ex: $ all BaseModel or $ all.
        '''
        if arg != "BaseModel":
            print("** class doesn't exist **")
            # Incomplete, still waiting for FileStorage

    def do_update(self, arg):
        '''
Updates an instance based on the class name
and id by adding or updating attribute
(save the change into the JSON file).
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        if arg[0] == "":
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg[1] == "":
            print("** instance id missing **")
            # Incomplete, still waiting for FileStorage
        elif arg[2] == "":
            print("** attribute name missing **")
            # Incomplete, still waiting for FileStorage

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        quit()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
