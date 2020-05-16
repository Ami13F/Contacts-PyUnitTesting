from domain.contact import Contact
from domain.contactValidator import ContactValidator
from utils.util import Exporter
import os

__author__ = 'Team0'


class AgendaController:

    def __init__(self, repo):
        self.__repo = repo
        self.__csvExporter = Exporter()

    @property
    def repo(self):
        return self.__repo

    def addContact(self, _id, _name, _phoneNr, _group):
        contact = Contact(_id, _name, _phoneNr, _group)

        ContactValidator.validate(contact)
        ContactValidator.checkDuplicates(contact, self.repo.get_all())
        self.repo.add(contact)

    def lookup(self, _name):
        """
        Finds a contact by name.
        """
        return self.repo.find(_name)

    def lookupAll(self, _group):
        """
        Finds a contact by group.
        """
        return self.repo.getAllFor(_group)

    def exportCSV(self, _group, outFName=os.path.abspath("src/contacte.csv")):
        """
        Exports contacts in .csv file.
        """
        all_in_group = self.lookupAll(_group)

        exporter = Exporter(outFName)
        exporter.exportToCVS(all_in_group)
