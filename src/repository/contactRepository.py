from domain.contact import Contact
from utils.constants import SEP, NEWLINE

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""


class RepositoryException(Exception):
    pass


class ContactRepository:

    def __init__(self, _fileName):
        self.__fileName = _fileName
        self.__items = self.__load_from_file()

    @property
    def fileName(self):
        return self.__fileName

    def add(self, contact):
        """
        Adds a new contact into the file.
        """
        self.__items.append(contact)
        self.__save_to_file([contact])

    def __save_to_file(self, contacts):
        try:
            f = open(self.fileName, "w")
        except IOError as ioe:
            raise RepositoryException(ioe)

        for contact in contacts:
            f.write(contact._id + SEP + contact.name + SEP +
                    contact.phoneNr + SEP + contact.group + NEWLINE)

        f.close()

    def __load_from_file(self):
        try:
            contacts = []
            with open(self.fileName, "r") as f:
                for line in f.readlines():
                    attrs = line.strip().split(SEP)
                    _id = attrs[0]
                    _name = attrs[1]
                    _phoneNr = attrs[2]
                    _group = attrs[3]
                    contact = Contact(_id, _name, _phoneNr, _group)
                    contacts.append(contact)
            return contacts
        except IOError as ioe:
            raise RepositoryException(ioe)

    def get_all(self):
        return self.__items

    def find(self, _name):
        """
        Finds a contact by a given name.
        """
        for c in self.__items:
            if c.name == _name:
                return c
        raise RepositoryException("Found no contacts with name : " + _name)

    def get_all_from_group(self, _group):
        """
        Returns all the contacts in a given group.
        Sorted by name.
        """
        contacts_in_groups = []

        for c in self.__items:
            if c.group == _group:
                contacts_in_groups.append(c)

        if len(contacts_in_groups) == 0:
            raise RepositoryException("Found no contact in group : " + _group)

        sorted_contacts = sorted(contacts_in_groups, key=lambda c: c.name)
        return sorted_contacts

    def size(self):
        return len(self.__items)

    def clear(self):
        self.__items.clear()