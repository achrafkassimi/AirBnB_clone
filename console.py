#!/usr/bin/python3
"""
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    valid_classes = ["BaseModel","User"]

    def emptyline(self):
        """
        """
        pass

    def do_quit(self, arg):
        """
        """
        return True
    
    def help_quit(self):
        """
        """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """
        """
        print()
        return True
    
    def do_show(self, arg):
        """
        Show the string representation of an instance.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(f"{commands[0]}()")
            storage.save()
            # new_inst = BaseModel()
            # new_inst.save()
            print(new_inst.id)

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                att_name = commands[2]
                att_val = commands[3]
                
                try:
                    att_val = eval(att_val)
                except Exception:
                    pass
                setattr(obj, att_name, att_val)

                obj.save()




if __name__ == "__main__":
    HBNBCommand().cmdloop()