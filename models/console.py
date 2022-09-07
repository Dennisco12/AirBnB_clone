#!/usr/bin/python3
"""This contains the entry point of the program"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This is the class definition"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place', 'State', 'City',
               'Amenity', 'Review']
    objs = storage.all()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """This does nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class and prints the id"""
        if not arg:
            print("** class name is missing **")
            return False
        line_arg = arg.split()
        if line_arg[0] not in type(self).classes:
            print("** class doesn't exist **")
            return False
        if line_arg[0] == "BaseModel":
            prototype = BaseModel()
        elif line_arg[0] == "User":
            prototype = User()
        elif line_arg[0] == "Place":
            prototype = Place()
        elif line_arg[0] == "State":
            prototype = State()
        elif line_arg[0] == "City":
            prototype = City()
        elif line_arg[0] == "Amenity":
            prototype = Amenity()
        elif line_arg[0] == "Review":
            prototype = Review()
        print("{}".format(prototype.id))
        prototype.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        if not arg:
            print("** class name is missing **")
            return False
        line_arg = arg.split()
        if line_arg[0] not in type(self).classes:
            print("** class doesn't exist **")
            return False
        if len(line_arg) < 2:
            print("** instance id missing **")
            return False
        show_key = line_arg[0] + "." + line_arg[1]
        if show_key not in type(self).objs:
            print("** no instance found **")
            return False
        print(type(self).objs[show_key])

    def do_destroy(self, arg):
        """This deletes an instance based on the class name and id"""
        if not arg:
            print("** class name is missing **")
            return False
        line_arg = arg.split()
        if line_arg[0] not in type(self).classes:
            print("** class doesn't exist **")
            return False
        if len(line_arg) < 2:
            print("** instance id missing **")
            return False
        destroy_key = line_arg[0] + "." + line_arg[1]
        if destroy_key not in type(self).objs:
            print("** no instance found **")
            return False
        del type(self).objs[destroy_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name"""
        ans_list = []
        if arg:
            line_arg = arg.split()
            if line_arg[0] not in type(self).classes:
                print("** class doesn't exist **")
                return False
            for k, v in storage.all().items():
                if line_arg[0] in k.split('.'):
                    ans_list.append(v.__str__())
            print(ans_list)
        else:
            for k, v in type(self).objs.items():
                ans_list.append(v.__str__())
            print(ans_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        if not arg:
            print("** class name is missing **")
            return False
        line_arg = arg.split()
        if line_arg[0] not in type(self).classes:
            print("** class doesn't exist **")
            return False
        if len(line_arg) < 2:
            print("** instance id missing **")
            return False
        update_key = line_arg[0] + "." + line_arg[1]
        if update_key not in type(self).objs:
            print("** no instance found **")
            return False
        if len(line_arg) < 3:
            print("** attribute name missing **")
            return False
        if len(line_arg) < 4:
            print("** value missing **")
            return False
        obj = storage.all()[update_key]
        val = line_arg[3]
        obj.__dict__[line_arg[2]] = val
        storage.save()

    def default(self, arg):
        """Called when prefix is not recognised"""
        line_arg = arg.split('.')
        if len(line_arg) > 1 and line_arg[0] in type(self).classes:
            if line_arg[1] == 'all()':
                ans_list = []
                for k, v in type(self).objs.items():
                    if line_arg[0] in k.split('.'):
                        ans_list.append(v.__str__())
                print(ans_list)
            if line_arg[1] == 'count()':
                ans_list = []
                for k, v in type(self).objs.items():
                    if line_arg[0] in k.split('.'):
                        ans_list.append(v.__str__())
                print(len(ans_list))
            if 'show' in line_arg[1].split('('):
                show_id_par = line_arg[1].split('(')
                show_id = show_id_par[1][:-1]
                show_key = line_arg[0] + '.' + show_id
                if len(show_key) == 0:
                    print("** instance id missing **")
                    return False
                if show_key not in type(self).objs:
                    print("** no instance found **")
                    return False
                print(type(self).objs[show_key])
            if 'destroy' in line_arg[1].split('('):
                destroy_id_par = line_arg[1].split('(')
                destroy_id = destroy_id_par[1][:-1]
                destroy_key = line_arg[0] + '.' + destroy_id
                if destroy_key not in type(self).objs:
                    print("** no instance found **")
                    return False
                del type(self).objs[destroy_key]
        else:
            print("** class doesn't exist **")
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
