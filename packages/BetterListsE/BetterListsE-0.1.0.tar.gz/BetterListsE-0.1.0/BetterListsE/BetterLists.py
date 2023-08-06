### py -m twine upload dist/*
###python -m setup.py sdist bdist_wheel

import colorama
from colorama import Fore


class BList():
    def add(list ,object):
        try:
            list.append(object)
        except:
            print(Fore.GREEN,"""BetterListsE:""",Fore.RED,""" Data Error Object is Not a List or Item is already in List""")
    def rem(list,item):
        try:
            list.remove(item)
        except:
            print(Fore.GREEN,"""BetterListsE:""",Fore.RED,""" Data Error Object is Not a List or Item is Not in List""")
    def lenght(list):
        try:
            return len(list)
        except:
            print(Fore.GREEN, """BetterListsE:""", Fore.RED,
                  """ Data Error Object is Not a List or Item is Not in List""")

    def typ(list):
        try:
            return type(list)
        except:
            print(Fore.GREEN, """BetterListsE:""", Fore.RED,
                  """ Data Error Object is Not a List or Item is Not in List""")
    def delete(list_to_delete):
        try:
            #clears list
            list_to_delete.clear()
        except:
            print(Fore.GREEN, """BetterListsE:""", Fore.RED,
                  """ Data Error Object is Not a List or Item is Not in List""")
    def cut(list,location):
        try:
            location = location - 1
            list.pop(location)
        except:
            print(Fore.GREEN, """BetterListsE:""", Fore.RED,
                  """ Data Error Object is Not a List, Item is Not in List or Location Not in Range""")
