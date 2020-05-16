from domain.contact import Contact
from utils.constants import SEP, NEWLINE

__author__ = 'Team0'


class RepositoryException(Exception):
    pass


class ContactRepository:

    def __init__(self, _fileName):
        self.__fileName = _fileName

    @property
    def fileName(self):
        return self.__fileName

    def add(self, contact):
        """
        Adds a new contact into the file.
        """

        all = self.__load_from_file()
        all.append(contact)
        self.__save_to_file(all)

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
            f = open(self.fileName, "r")
        except IOError as ioe:
            raise RepositoryException(ioe)

        contacts = []

        line = f.readline().strip()
        while line != "":
            attrs = line.split(SEP)
            _id = attrs[0]
            _name = attrs[1]
            _phoneNr = attrs[2]
            _group = attrs[3]
            contact = Contact(_id, _name, _phoneNr, _group)
            contacts.append(contact)
            line = f.readline().strip()

        f.close()

        return contacts

    def get_all(self):
        return self.__load_from_file()

    def find(self, _name):
        """
        Finds a contact by a given name.
        """
        all = self.get_all()

        for c in all:
            if c.name == _name:
                return c
        raise RepositoryException("Found no contacts with name : " + _name)

    def getAllFor(self, _group):
        """
        Returns all the contacts in a given group.
        Sorted by name.
        """
        all = self.get_all()
        contacts_in_groups = []

        for c in all:
            if c.group == _group:
                contacts_in_groups.append(c)

        if len(contacts_in_groups) == 0:
            raise RepositoryException("Found no contact in group : " + _group)

        sorted_contacts = sorted(contacts_in_groups, key=lambda c: c.name)
        return sorted_contacts

    def size(self):
        return len(self.get_all())
