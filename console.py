#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Attributes HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity", "Place", "Review",
                     "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        """
        print("Quit command to exit the program")
        print("")

    def do_show(self, arg):
        """
        Show the string representation of an instance
        """
        com = shlex.split(arg)
        # show User "12w-241"
        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(com) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(com[0], com[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def default(self, arg):
        """
        """
        list_for_arg = arg.split(".")
        # User.show(12w-241) output: ['User', 'show("12w-241")']
        # list_for_arg[0] = 'User'
        # list_for_arg[1] = 'show(12w-241)'
        # User.all() output: ['User', 'all()']
        # list_for_arg[0] = 'User'
        # list_for_arg[1] = 'all()'
        name_class = list_for_arg[0]
        com = list_for_arg[1].split("(")
        # com[0] = 'all'
        # com[1] = ')'
        # com[0] = 'show'
        # com[1] = '"12w-241")'
        name_method = com[0]
        xtra_arg_id = com[1].split(")")[0]
        # ['"12w-241"', '']
        dict_method = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }

        if name_method in dict_method.keys():
            return dict_method[name_method]("{} {}".format(
                name_class, xtra_arg_id))
            # all User or show User 123
            # 'all User'
            # self.all(self, 'User')
        print("*** Unknown syntax : {} ***".format(arg))

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file
        """
        com = shlex.split(arg)
        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(f"{com[0]}()")
            storage.save()
            # new_inst = BaseModel()
            # new_inst.save()
            print(new_inst.id)

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        """
        com = shlex.split(arg)
        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(com) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(com[0], com[1])
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        obj = storage.all()
        com = shlex.split(arg)
        # print(f"{com = }")

        if len(com) == 0:
            for key, value in obj.items():
                print(str(value))
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                if key.split('.')[0] == com[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        """
        obj = storage.all()
        # User.count() City.count()
        # count User or count City
        com = shlex.split(arg)
        # ['User']
        # com[0] = 'User'
        name_class = com[0]
        count = 0
        if com:
            if name_class in self.valid_classes:
                for o in obj.values():
                    if o.__class__.__name__ == name_class:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_all_class(self, arg):
        """
        Print the string representation of all class.
        """
        obj = storage.all()
        print("tous les class :")
        print(self.valid_classes)
        # print("tous les class rempli:")
        # for key, value in obj.items():
        #     print(key)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        """
        com = shlex.split(arg)
        if len(com) == 0:
            print("** class name missing **")
        elif com[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(com) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(com[0], com[1])
            if key not in obj:
                print("** no instance found **")
            elif len(com) < 3:
                print("** attribute name missing **")
            elif len(com) < 4:
                print("** value missing **")
            else:
                obj = obj[key]
                att_name = com[2]
                att_val = com[3]
                try:
                    att_val = eval(att_val)
                except Exception:
                    pass
                setattr(obj, att_name, att_val)
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
