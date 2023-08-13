#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter
    """
    prompt = '(hbnb) '
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit the program at end of file (CTRL+D) """
        return True

    def emptyline(self):
        """ Do nothing on an empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        models.storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in objs:
            del objs[obj_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        objs = models.storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if arg == "BaseModel":
            arg = ""
        print([str(objs[obj]) for obj in objs if arg in obj])

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[obj_key]
        setattr(obj, args[2], args[3])
        obj.save()

    def count(self, arg):
        """ Retrieves the number of instances of a class """
        count = 0
        for obj_key in models.storage.all():
            if arg in obj_key:
                count += 1
        print(count)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in objs:
            del objs[obj_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[obj_key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[obj_key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_update_dict(self, arg):
        """ Updates an instance based on the class name and id with a dictionary """
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        obj = objs[obj_key]
        arg_dict = eval(args[2])
        for key, value in arg_dict.items():
            setattr(obj, key, value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
