#from cis301.phonebill.abstract_phonebill import abstractmethod
from typing import list, TypeVar

class Phonebill(AbstractPhoneBill):
    def __init__(self,name):
        self.__name = name
        self.__phoneRecords = list()
    def get_phonecalls(self) -> List[T]:
        return self.__name

    def add_phonecall(self, phonecall):
        self.__phoneRecords.append(phonecall)

    def get_customer(self) -> str:
        return self.__name


import sys

def main(args=None):

    if args is None:
        args = sys.argv[1:]
    print (args)
    print(f"Missing command line arguments")
    parse_cli_argv(args)


def parse_cli_argv(argv):
    if len(argv)<5:
        print(usage("invalid number of argumets"))
        exit(1)
    if "-README" in argv:
        print(usage(""))
        exit(0)
    for arg in argv:
        if arg[0] == '-':
            option = arg[1:]
            if option not in expected_options:
                raise Exception(f'unknown option'{option})
                option_map[option] = true

    raise NotImplementedError('not implemented yet')


