from domain.contact import Contact
from domain.contactValidator import ContactValidator
from utils.util import Exporter
import os

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""


class AgendaController:

    def __init__(self, repo):
        self.__repo = repo

    def add_contact(self, _id, _name, _phoneNr, _group):
        contact = Contact(_id, _name, _phoneNr, _group)

        ContactValidator.validate(contact)
        ContactValidator.checkDuplicates(contact, self.__repo.get_all())
        self.__repo.add(contact)

    def find(self, _name):
        """
        Finds a contact by name.
        """
        return self.__repo.find(_name)

    def get_from_group(self, _group):
        """
        Get all contacts from a group
        """
        return self.__repo.get_all_from_group(_group)

    def export_csv(self, _group, outFName=os.path.abspath("src/contacte.csv")):
        """
        Exports a group's contact in a .csv file.
        """
        all_in_group = self.get_from_group(_group)

        exporter = Exporter(outFName)
        exporter.exportToCVS(all_in_group)

    def get_all(self):
        return self.__repo.get_all()

    def clear(self):
        self.__repo.clear()
