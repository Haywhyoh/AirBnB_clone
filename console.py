#!/usr/bin/python3

import cmd
from ast import literal_eval
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    #intro = 'Welcome to AirBnB console. Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    classes = ["BaseModel",
               "User",
               "Place",
               "State",
               "City",
               "Amenity",
               "Review"]

    def do_create(self, arg):
        '''
Creates a new instance of BaseModel,
saves it (to the JSON file) and prints the id.
Ex: $ create BaseModel
        '''
        if arg == "":
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        '''
Prints the string representation of an instance
based on the class name and id.
Ex: $ show BaseModel 1234-1234-1234
        '''
        arg = arg.split()
        try:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif arg[0] in self.classes:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
        except (IndexError):
            print("** class name missing **")

    def do_destroy(self, arg):
        '''
Deletes an instance based on the class name
and id (save the change into the JSON file).
$ destroy BaseModel 1234-1234-1234
        '''
        arg = arg.split()
        try:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif arg[0] in self.classes:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
        except (IndexError):
            print("** class name missing **")

    def do_all(self, arg):
        '''
Prints all string representation of all instances
based or not on the class name.
Ex: $ all BaseModel or $ all.
        '''
        if arg not in self.classes and arg != '':
            print("** class doesn't exist **")
        elif arg == "":
            res = []
            for key in storage.all():
                res.append(str(storage.all()[key]))
            print(res)
        else:
            res = []
            for key in storage.all():
                if key.split('.')[0] == arg:
                    res.append(str(storage.all()[key]))
            print(res)

    def do_update(self, arg):
        '''
Updates an instance based on the class name
and id by adding or updating attribute
(save the change into the JSON file).
Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''
        arg = arg.split()
        try:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif arg[0] in self.classes:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    if arg[3][1:-1] != "":
                                        setattr(storage.all()[key], arg[2], arg[3][1:-1])
                                        storage.all()[key].save()
                                    else:
                                        print("** value missing **")
                                except (IndexError):
                                    print("** value missing **")
                            else:
                                print("** value missing **")
                        except (IndexError):
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                except (IndexError):
                    print("** instance id missing **")
        except (IndexError):
            print("** class name missing **")

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        quit()
        #return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        quit()
        #return True

    def emptyline(self):
        pass

    def default(self, line: str) -> None:
        commands = ["show",
                    "all()",
                    "destroy",
                    "update",
                    "count()"]
        line = line.split('.')
        try:
            if line[0] in self.classes:
                if line[1] == commands[1]:
                    self.do_all(line[0])
                elif line[1] == commands[4]:
                    res = []
                    for key in storage.all():
                        if key.split('.')[0] == line[0]:
                            res.append(str(storage.all()[key]))
                    print(len(res))
                elif line[1].split('(')[0] == commands[0]:
                    key = line[0] + "." + line[1].split('(')[1][1:-2]
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print('** no instance found **')
                elif line[1].split("(")[0] == commands[2]:
                    key = line[0] + "." + line[1].split('(')[1][1:-2]
                    if key in storage.all():
                        storage.all().__delitem__(key)
                        storage.save()
                    else:
                        print('** no instance found **')
                elif line[1].split("(")[0] == commands[3]:
                    if line[1][-2] != "}":
                        data = line[1].split("(")[1][1:-2].split('", "')
                        key = line[0] + "." + data[0]
                        if key in storage.all():
                            try:
                                if data[1] in storage.all()[key].to_dict():
                                    try:
                                        setattr(storage.all()[key],
                                                data[1], data[2])
                                        storage.all()[key].save()
                                    except (IndexError):
                                        print("** value missing **")
                                else:
                                    print("** value missing **")
                            except (IndexError):
                                print("** attribute name missing **")
                        else:
                            print('** no instance found **')
                    else:
                        data = line[1].split("(")[1][1:-1].split('", ')
                        key = line[0] + "." + data[0]
                        new_dict = '", '.join(data[1:])
                        if key in storage.all():
                            try:
                                new_dict = literal_eval(new_dict)
                                if len(new_dict) == 0:
                                    print("** attribute name missing **")
                                elif type(new_dict) == set:
                                    print("** value missing **")
                                else:
                                    for k in new_dict:
                                        if k in storage.all()[key].to_dict():
                                            setattr(storage.all()[key], k,
                                                    new_dict[k])
                                            storage.all()[key].save()
                                        else:
                                            print("** value for " + str(k) +
                                                  " missing **")
                            except (IndexError, SyntaxError):
                                print("omoo this your dictionary ehn")
                        else:
                            print('** no instance found **')
                else:
                    print("** command not found **")
            else:
                print("*** Unknown syntax:", line[0])
        except (IndexError):
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()