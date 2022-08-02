#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to AirBnB console. Type help or ? to ist commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        quit()
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        quit()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
