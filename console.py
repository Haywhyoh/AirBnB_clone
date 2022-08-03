#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnB console. Type help or ? to list commands.\n'
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
        elif arg == self.classes[0]:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
        elif arg == self.classes[1]:
            # Incomplete, still waiting for FileStorage
            new_user = User()
            new_user.save()
            print(new_user.id)
        elif arg == self.classes[2]:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)
        elif arg == self.classes[3]:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)
        elif arg == self.classes[4]:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)
        elif arg == self.classes[5]:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)
        else:
            # Incomplete, still waiting for FileStorage
            new_model = BaseModel()
            print(new_model.id)

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
            elif arg[0] == self.classes[0]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[1]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[2]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[3]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[4]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[5]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            else:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
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
            elif arg[0] == self.classes[0]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[1]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[2]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[3]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[4]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[5]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            else:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
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
        else:
            res = []
            for key in storage.all():
                res.append(str(storage.all()[key]))
            print(res)
            # Incomplete, still waiting for FileStorage

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
            elif arg[0] == self.classes[0]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                print("okay")
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
                                except (IndexError):
                                    print("** value missing **")
                            else:
                                print("** value missing **")
                                print(storage.all())
                        except (IndexError):
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[1]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                print("okay")
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
                                except (IndexError):
                                    print("** value missing **")
                            else:
                                print("** value missing **")
                                print(storage.all())
                        except (IndexError):
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[2]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                    try:
                        print(arg[2])
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[3]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                    try:
                        print(arg[2])
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[4]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                    try:
                        print(arg[2])
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            elif arg[0] == self.classes[5]:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                    try:
                        print(arg[2])
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
            else:
                # Incomplete, still waiting for FileStorage
                try:
                    print(arg[1])
                    try:
                        print(arg[2])
                        try:
                            print(arg[3])
                        except (IndexError):
                            print("** value missing **")
                            # Incomplete, still waiting for FileStorage
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
                except (IndexError):
                    print("** instance id missing **")
                # Incomplete, still waiting for FileStorage
                    try:
                        print(arg[2])
                    except (IndexError):
                        print("** attribute name missing **")
                        # Incomplete, still waiting for FileStorage
        except (IndexError):
            print("** class name missing **")

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
