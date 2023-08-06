import os
import ast
import copy
import types
import typing
import atexit
import functools

from .__util import abstract
from .__message import *

class ConfigLoader:
    def __init__(self, dir: str, name: str, suffix: str, namespace: typing.Dict[str, typing.Any], save_on_exist: bool, required: bool) -> None:
        self.dir = dir
        self.name = name
        self.suffix = suffix or self.suffix
        self.path = os.path.join(self.dir, self.name)
        self.namespace = namespace
        self.required = required
        if self.suffix is not None:
            self.path += f".{self.suffix}"
        if save_on_exist:
            atexit.register(self.dump)
        self.init()
    def __init_subclass__(cls, suffix: typing.Union[str, None]=None) -> None:
        cls.suffix = suffix
    @property
    def filtered_namespace(self) -> typing.Dict[str, typing.Any]:
        return copy.deepcopy({k:v for k,v in self.namespace.items() if self.serializable(k, v)})
    def serializable(self, key: str, value: typing.Any) -> bool:
        try:
            return self.filter(key, value)
        except Exception as e:
            log_failed(key, value, e)
        return False
    def load(self) -> typing.Any:
        if self.required and not os.path.exists(self.path):
            self.dump()
        elif not abstract(self.read) and (self.required or os.path.exists(self.path)):
            data = self.read()
            for key in data:
                if key in self.filtered_namespace:
                    self.namespace[key] = data[key]
            log_loaded(self.__class__, self.path)
        return self.namespace
    def dump(self) -> None:
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        if not abstract(self.write):
            self.write(self.filtered_namespace)
            log_saved(self.__class__, self.path)
    def init(self) -> None: pass
    def write(self, data: typing.Dict[str, typing.Any]) -> None: pass
    def read(self) -> typing.Dict[str, typing.Any]: pass
    def filter(self, key: str, value: typing.Any) -> bool: 
        return not key.startswith("_") and not isinstance(value, types.ModuleType)

class FileConfigLoader(ConfigLoader):
    def __init_subclass__(cls, suffix: typing.Union[str, None]=None, binary: bool=False) -> None:
        super().__init_subclass__(suffix)
        cls.rmode = "rb" if binary else "r"
        cls.wmode = "wb" if binary else "w"
    def load(self) -> typing.Any:
        if self.required and not os.path.exists(self.path):
            self.dump()
        elif not abstract(self.read) and (self.required or os.path.exists(self.path)):
            with open(self.path, self.rmode) as file:
                data = self.read(file)
                for key in data:
                    if key in self.filtered_namespace:
                        self.namespace[key] = data[key]
                log_loaded(self.__class__, self.path)
        return self.namespace
    def dump(self) -> None:
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        if not abstract(self.write):
            with open(self.path, self.wmode) as file:
                self.write(file, self.filtered_namespace)
                log_saved(self.__class__, self.path)
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None: pass
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]: pass

class JSONConfigLoader(FileConfigLoader, suffix="json"):
    def init(self) -> None:
        import json
        self.json = json
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        self.json.dump(data, file)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        return self.json.load(file)
    def filter(self, key: str, value: typing.Any) -> bool:
        b = super().filter(key, value)
        if b: self.json.dumps(value)
        return b

class INIConfigLoader(FileConfigLoader, suffix="ini"):
    def __init__(self, dir: str, name: str, suffix: str, namespace: typing.Dict[str, typing.Any], save_on_exist: bool, required: bool, untitled: str="UNTITLED") -> None:
        super().__init__(dir, name, suffix, namespace, save_on_exist, required)
        import configparser
        self.configparser = configparser
        self.untitled = untitled
    def literal_quote(self, data: typing.Dict[str, typing.Any]) -> None:
        for k,v in data.items():
            if isinstance(v, str):
                data[k] = f'"{v}"'
            elif isinstance(v, dict):
                self.literal_quote(v)
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        ast.literal_eval
        cp = self.configparser.ConfigParser()
        data = {self.untitled: {k:v for k,v in data.items() if not isinstance(v, dict)}, **{k:v for k,v in data.items() if isinstance(v, dict)}}
        self.literal_quote(data)
        cp.read_dict(data)
        cp.write(file)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        cp = self.configparser.ConfigParser()
        cp.readfp(file)
        return {**{k:ast.literal_eval(v) for k,v in dict(cp.items(self.untitled)).items()}, **{s:{k:ast.literal_eval(v) for k,v in dict(cp.items(s)).items()} for s in cp.sections() if s != self.untitled}}

class PYConfigLoader(FileConfigLoader, suffix="py"):
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        import importlib.util
        spec = importlib.util.spec_from_file_location(self.path, self.path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return vars(module)

class YAMLConfigLoader(FileConfigLoader, suffix="yml"):
    def init(self) -> None:
        import yaml
        self.yaml = yaml
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        self.yaml.safe_dump(data, file)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        return self.yaml.safe_load(file)

class TOMLConfigLoader(FileConfigLoader, suffix="toml"):
    def init(self) -> None:
        import toml
        self.toml = toml
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        self.toml.dump(data, file)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        return self.toml.load(file)

class XMLConfigLoader(FileConfigLoader, suffix="xml"):
    def init(self) -> None:
        import xml.etree.cElementTree
        self.tree = xml.etree.cElementTree
    def search_write(self, root, data: typing.Dict[str, typing.Any]) -> None:
        root: self.tree.Element = root
        for k,v in data.items():
            e = self.tree.Element(k)
            root.append(e)
            if not isinstance(v, dict):
                e.text = f'"{v}"' if isinstance(v, str) else str(v)
            else:
                self.search_write(e, v)
    def search_read(self, root, data: dict) -> None:
        root: self.tree.Element = root
        for e in root.findall("*"):
            childs = e.findall("*")
            if len(childs) == 0:
                data[e.tag] = ast.literal_eval(e.text)
            else:
                data[e.tag] = {}
                self.search_read(e, data[e.tag])
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        root = self.tree.Element("root")
        self.search_write(root, data)
        self.tree.ElementTree(root).write(self.path)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        tree = self.tree.parse(file)
        data = {}
        self.search_read(tree.getroot(), data)
        return data

class PickleConfigLoader(FileConfigLoader, suffix="pkl", binary=True):
    def init(self) -> None:
        import pickle
        self.pickle = pickle
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        self.pickle.dump(data, file)
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        return self.pickle.load(file)

class SqliteConfigLoader(ConfigLoader, suffix="db"):
    TYPES = {
        None: "NULL",
        int: "INTEGER",
        float: "REAL",
        str: "TEXT",
        bytes: "BLOB",
        list: "TEXT"
    }
    def init(self) -> None:
        import sqlite3
        self.sqlite3 = sqlite3
        self.cols = {}
    def search_write(self, data: typing.Dict[str, typing.Any], paths=[]) -> None:
        for k,v in data.items():
            if isinstance(v, dict):
                self.search_write(v, [*paths, k])
            elif isinstance(v, list):
                self.cols["_".join([*paths, k])] = str(v)
            elif isinstance(v, str):
                self.cols["_".join([*paths, k])] = f'"{v}"'
            else:
                self.cols["_".join([*paths, k])] = v
    def write(self, data: typing.Dict[str, typing.Any]) -> None:
        db = self.sqlite3.connect(self.path)
        self.search_write(data)
        db.execute("drop table if exists {}".format(self.name))
        db.execute("create table {}({})".format(self.name, ", ".join(["{} {}".format(k, self.TYPES[type(v)]) for k,v in self.cols.items()])))
        db.execute("insert into {} values ({})".format(self.name, ", ".join(["?" for _ in self.cols])), list(self.cols.values()))
        db.commit()
    def read(self) -> typing.Dict[str, typing.Any]:
        db = self.sqlite3.connect(self.path)
        cur = db.execute("select * from {}".format(self.name))
        row = cur.fetchone()
        data = {}
        for i in range(len(cur.description)):
            names = cur.description[i][0].split("_")
            d = data
            for name in names[:-1]:
                d[name] = {}
                d = d[name]
            if isinstance(row[i], str):
                d[names[-1]] = ast.literal_eval(row[i])
            else:
                d[names[-1]] = row[i]
        return data

class TextLineConfigLoader(FileConfigLoader, suffix="txt"):
    def __init__(self, dir: str, name: str, suffix: str, namespace: typing.Dict[str, typing.Any], save_on_exist: bool, required: bool, quote_string: bool=False) -> None:
        super().__init__(dir, name, suffix, namespace, save_on_exist, required)
    def write(self, file: typing.TextIO, data: typing.Dict[str, typing.Any]) -> None:
        file.write("\n".join(map(str, data.values())))
    def read(self, file: typing.TextIO) -> typing.Dict[str, typing.Any]:
        result = {}
        lines = file.readlines()
        for i,(k,v) in enumerate(self.filtered_namespace.items()):
            if isinstance(v, str):
                result[k] = lines[i]
            else:
                result[k] = ast.literal_eval(lines[i])
        return result

class ArgParseConfigLoader(FileConfigLoader):
    def __init__(self, namespace: typing.Dict[str, typing.Any], parser=None) -> None:
        super().__init__("", "", None, namespace, False, False)
        import argparse
        self.argparse = argparse
        self.parse_args = parser is None
        self.parser: argparse.ArgumentParser = parser or argparse.ArgumentParser()
        _namespace = namespace
        class Action(argparse.Action):
            def __call__(self, parser, namespace, values, option_string=None) -> None:
                paths = self.dest.split(".")
                data = _namespace
                for path in paths[:-1]:
                    data = data[path]
                data[paths[-1]] = values
        self.action = Action
    def search(self, data: typing.Dict[str, typing.Any], paths=[]):
        for k,v in data.items():
            if isinstance(v, dict):
                self.search(v, [*paths, k])
            else:
                self.parser.add_argument("--{}".format(".".join([*paths, k])), action=self.action, default=v, type=type(v))
    def load(self) -> typing.Any:
        self.search(self.filtered_namespace)
        log_loaded(self.__class__, self.path)
        if self.parse_args:
            self.parser.parse_args()
        return self.parser

def load_from(loader: typing.Type[FileConfigLoader], namespace, dir=".", name="config", suffix=None, save_on_exit=True, required=False, **kwargs) -> typing.Any:
    return loader(dir, name, suffix, namespace, save_on_exit, required, **kwargs).load()

def load_from_appdir(loader: typing.Type[FileConfigLoader], appname, appauthor, namespace, name="config", suffix=None, save_on_exit=True, required=False, **kwargs) -> typing.Any:
    import appdirs
    dir = appdirs.user_config_dir(appname, appauthor)
    return load_from(loader, namespace, dir, name, suffix, save_on_exit, required, **kwargs)

load_json = functools.partial(load_from, JSONConfigLoader)
load_ini = functools.partial(load_from, INIConfigLoader)
load_py = functools.partial(load_from, PYConfigLoader)
load_yaml = functools.partial(load_from, YAMLConfigLoader)
load_toml = functools.partial(load_from, TOMLConfigLoader)
load_xml = functools.partial(load_from, XMLConfigLoader)
load_pkl = functools.partial(load_from, PickleConfigLoader)
load_sqlite = functools.partial(load_from, SqliteConfigLoader)
load_textline = functools.partial(load_from, TextLineConfigLoader)
def load_argparse(namespace, parser=None) -> typing.Any: return ArgParseConfigLoader(namespace, parser).load()
load_json_from_appdir = functools.partial(load_from_appdir, JSONConfigLoader)
load_ini_from_appdir = functools.partial(load_from_appdir, INIConfigLoader)
load_py_from_appdir = functools.partial(load_from_appdir, PYConfigLoader)
load_yaml_from_appdir = functools.partial(load_from_appdir, YAMLConfigLoader)
load_toml_from_appdir = functools.partial(load_from_appdir, TOMLConfigLoader)
load_xml_from_appdir = functools.partial(load_from_appdir, XMLConfigLoader)
load_pkl_from_appdir = functools.partial(load_from_appdir, PickleConfigLoader)
load_sqlite_from_appdir = functools.partial(load_from_appdir, SqliteConfigLoader)
load_textline_from_appdir = functools.partial(load_from_appdir, TextLineConfigLoader)