#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
import time
import inspect


def sleep(seconds, mute=False):
    """sleep with countdown show and prevent pause or sleep of PC"""
    end = time.time() + seconds
    while time.time() < end:
        if not mute:
            print(f"ETA {seconds:.0f}/{end - time.time():.0f}  s\t", end="\r")
        time.sleep(1)


def simple_color(value, color_name="BLUE"):
    """
    return text with color, default in blue.
    "Why is it blue?"
    "It's always blue."
    """
    if sys.platform == "win32":
        return value
    colors = {
        "RED": 31,
        "GREEN": 32,
        "YELLOW": 33,
        "BLUE": 34,
        "MAGENTA": 35,
        "CYAN": 36,
    }
    return f"\033[1;{colors[color_name]}m{value}\033[0m"


def color(value, color_name="BLUE"):
    """if have colorama then use it"""
    if sys.platform == "win32":
        try:
            from colorama import Fore, Style, init

            init()
            value = getattr(Fore, color_name) + Style.BRIGHT + value + Fore.RESET
        finally:
            return value
    return simple_color(value, color_name)


class NestedData:
    """utils for nested data"""

    def __init__(self, obj):
        self.data = obj

    def _find(self, obj, path=""):
        """return generator"""
        if isinstance(obj, dict):
            iter_obj = obj.items()
        elif isinstance(obj, (list, tuple)):
            iter_obj = enumerate(obj)
        else:
            return
        for k, v in iter_obj:
            new_path = f"{path}[{repr(k)}]"
            try:
                if self._condition(k, v):
                    yield obj, new_path
                    continue
            except Exception as exc:
                if not self.ignore_exc:
                    raise exc
            yield from self._find(v, new_path)

    def find(self, condition, ignore_exc=False):
        """return generator with (obj, path)"""
        self.ignore_exc = ignore_exc
        self._condition = condition
        return self._find(self.data)

    def find_keys(self, key):
        """find all data with path matches key in generator"""
        return self.find(lambda k, v: k == key)

    def find_values(self, value):
        """find all data that matches value and path for data"""
        return self.find(lambda k, v: v == value)

    def find_keyvalues(self, key, value):
        """find all data that matches value and path for data"""
        return self.find(lambda k, v: (k, v) == (key, value))

    def find_any_keyvalues(self, var):
        """find all data that matches key or value and path for data"""
        return self.find(lambda k, v: var in (k, v), ignore_exc=True)

    def find_any(self, var):
        self.path = None
        for obj, path in self.find_any_keyvalues(var):
            self.path = path
            return obj
        return None

    def find_key(self, key):
        """find key and path for data"""
        self.path = None
        for obj, path in self.find_keys(key):
            self.path = path
            return obj[key]
        return None

    def find_value(self, value):
        """find key and path for data"""
        self.path = None
        for obj, path in self.find_values(value):
            self.path = path
            return obj
        return None

    def find_keyvalue(self, key, value):
        """find key and path for data"""
        self.path = None
        for obj, path in self.find_keyvalues(key, value):
            self.path = path
            return obj
        return None


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonWithArgs:
    """带参数的单例模式, 通过继承使用，需放到第一继承位"""

    def __new__(cls, *args, **kwargs):
        arg = f"{args}{kwargs}"
        if not hasattr(cls, "_instances"):
            cls._instances = {}
        return cls._instances.setdefault(arg, super().__new__(cls))


class ArgMethodBase:
    """auto generator arguments by static methods"""

    def __init__(self, epilog=None):
        """initialize arguments parser"""
        parser = argparse.ArgumentParser(
            description=self.__doc__,
            epilog=epilog,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        subparsers = parser.add_subparsers(title="commands", dest="command")
        for arg_map in self.__get_arg_lists__():
            sub_parser = subparsers.add_parser(arg_map["command"], help=arg_map["help"])
            for arg in arg_map["required_args"]:
                sub_parser.add_argument(arg)
            for arg, value in arg_map["optional_args"]:
                sub_parser.add_argument("--%s" % arg, type=type(value), default=value)

        args = parser.parse_args()
        if args.command is None:
            parser.print_help()
        elif self.__run_command__(**vars(args)) is False:
            print(color("ERROR", "RED"), file=sys.stderr)
            exit(-1)
        else:
            print(color("OK", "GREEN"), file=sys.stderr)

    def __run_command__(self, command, **args):
        """run a certain staticmethod"""
        return getattr(self, command)(**args)

    def __get_arg_lists__(self):
        """get arguments info lists from self class staticmethods"""
        for obj_name in dir(self):
            func = getattr(self, obj_name)
            if obj_name.startswith("__") or not callable(func):
                continue
            default_len = 0
            default_values = []
            if func.__defaults__ is not None:
                default_len = len(func.__defaults__)
                default_values = func.__defaults__
            argcount = func.__code__.co_argcount
            required_args = func.__code__.co_varnames[: argcount - default_len]
            optional_args = func.__code__.co_varnames[argcount - default_len : argcount]  # noqa
            yield {
                "command": obj_name,
                "help": func.__doc__,
                "required_args": required_args,
                "optional_args": zip(optional_args, default_values),
            }


def monkey_patch(module, obj_name, obj, package=None):
    """recursively patch obj in module"""
    if isinstance(module, str):
        # to-do if '.' in module  # seems no need to bother
        module = sys.modules[module]
    if not inspect.ismodule(module):
        raise TypeError(f"'{module}' is not module")
    if package is None:
        package = module.__package__
    if obj_name in module.__dict__:
        module.__dict__[obj_name] = obj
        print(f"Monkey patched <{obj_name}> in <{module.__name__}>", file=sys.stderr)
    for k, v in module.__dict__.items():
        if inspect.ismodule(v) and v.__package__ == package:
            monkey_patch(v, obj_name, obj, package)


if __name__ == "__main__":
    data = {
        "d": [
            {"id": 1},
            {"id": 2},
            {"id": 3},
            {"id": 4},
            [{"id": 3}],
            "ixxx",
        ]
    }
    n = NestedData(data)

    from pprint import pprint

    pprint(list(n.find_keys("id")))
    pprint(list(n.find(lambda k, v: "i" in v, ignore_exc=True)))
