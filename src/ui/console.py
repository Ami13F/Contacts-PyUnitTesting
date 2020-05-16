from domain.contactValidator import ValidationException, DuplicationException
from repository.contactRepository import RepositoryException
from utils.constants import NEWLINE

__author__ = 'Team0'


class Console:
    def __init__(self, _ctr):
        self.__ctr = _ctr

    @property
    def ctr(self):
        return self.__ctr

    def __print_contact(self, contact):
        print(str(contact) + NEWLINE)

    def __print_contacts(self, contacts):
        for c in contacts:
            self.__print_contact(c)

    def __show_menu(self):
        print("1. Adauga contact. \n"
              "2. Cautare dupa nume.\n"
              "3. Cautare dupa grup.\n"
              "4. Exporta in CSV.\n"
              "5. Exit.\n")

    def __add(self):
        _id = input("Id = ")
        _name = input("Nume = ")
        _phoneNr = input("Nr Telefon = ")
        _group = input("Group = ")
        self.ctr.addContact(_id, _name, _phoneNr, _group)
        print("Added contact!")

    def __search_name(self):
        _name = input("Nume = ")
        result = self.ctr.lookup(_name)
        self.__print_contact(result)

    def __search_group(self):
        _group = input("Grup = ")
        result = self.ctr.lookupAll(_group)
        self.__print_contacts(result)

    def __export(self):
        _group = input("Grup = ")
        self.ctr.exportCSV(_group)

    def run_ui(self):

        opt_map = {"1": self.__add, "2": self.__search_name,
                   "3": self.__search_group, "4": self.__export}

        while True:
            try:
                self.__show_menu()
                opt = input("Optiune = ")

                if opt == "5":
                    print("Goodbye!")
                    break

                opt_map[opt]()
            except KeyError:
                print("Optiunea nu este implementata.")
            except ValidationException as ve:
                print(ve)
            except DuplicationException as de:
                print(de)
            except RepositoryException as re:
                print(re)
