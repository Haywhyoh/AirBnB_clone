#!/usr/bin/python3
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_list = ["BaseModel",
               "User",
               "Place",
               "State",
               "City",
               "Amenity",
               "Review"]
    
    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print('** class name missing ** (ex: $ create)')
        elif arg not in self.class_list:
            print('** class doesn\'t exist **')
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)
    
    def do_show(self, arg):
        if arg == '':
            print('** class name missing **')
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif arg[1] == "":
            print("** instance id missing **")
        else:
            for key in storage.all().items():
                if not 

        










if __name__ == '__main__':
    HBNBCommand().cmdloop()