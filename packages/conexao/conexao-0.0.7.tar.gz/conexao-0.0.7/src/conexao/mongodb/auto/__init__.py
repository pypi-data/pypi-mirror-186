'''
Based on: https://realpython.com/python-import/#example-import-data-files
'''

import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from conexao.mongodb import create_client


class Importer(MetaPathFinder):
    def __init__(self, profile_name):
        self.profile_name = profile_name

    @classmethod
    def find_spec(cls, fullname, path, target=None):
        module, _, profile_name = fullname.rpartition('.')
        if module != 'conexao.mongodb.auto':
            return None
        return ModuleSpec(fullname, cls(profile_name))

    def create_module(self, spec):
        return create_client(self.profile_name)

    def exec_module(self, module):
        pass


sys.meta_path.append(Importer)
