#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
            new_place = Place()
            new_place.save()
            print(new_place.id)
        elif arg == self.classes[3]:
            # Incomplete, still waiting for FileStorage
            new_state = State()
            new_state.save()
            print(new_state.id)
        elif arg == self.classes[4]:
            # Incomplete, still waiting for FileStorage
            new_city = City()
            new_city.save()
            print(new_city.id)
        elif arg == self.classes[5]:
            # Incomplete, still waiting for FileStorage
            new_amenity = Amenity()
            new_amenity.save()
            print(new_amenity.id)
        else:
            # Incomplete, still waiting for FileStorage
            new_review = Review()
            new_review.save()
            print(new_review.id)

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
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[3]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[4]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[5]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        print(storage.all()[arg[0] + "." + arg[1]])
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            else:
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
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[3]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[4]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            elif arg[0] == self.classes[5]:
                try:
                    if arg[0] + "." + arg[1] in storage.all():
                        storage.all().__delitem__(arg[0] + "." + arg[1])
                        storage.save()
                    else:
                        print('** no instance found **')
                except (IndexError):
                    print("** instance id missing **")
            else:
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
            elif arg[0] == self.classes[0]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            elif arg[0] == self.classes[1]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            elif arg[0] == self.classes[2]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            elif arg[0] == self.classes[3]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            elif arg[0] == self.classes[4]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            elif arg[0] == self.classes[5]:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
            else:
                try:
                    key = arg[0] + "." + arg[1]
                    if key in storage.all():
                        try:
                            if arg[2] in storage.all()[key].to_dict():
                                try:
                                    setattr(storage.all()[key], arg[2], arg[3])
                                    storage.all()[key].save()
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
