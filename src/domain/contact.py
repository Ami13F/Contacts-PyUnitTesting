from utils.constants import SEP

__author__ = 'Team0'


class Contact:

    def __init__(self, _id, _name, _phoneNr, _group):
        self.__id = _id
        self.__name = _name
        self.__phoneNr = _phoneNr
        self.__group = _group

    @property
    def _id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phoneNr(self):
        return self.__phoneNr

    @property
    def group(self):
        return self.__group

    def __eq__(self, other):
        return self._id == other._id

    def __str__(self, *args, **kwargs):
        return self.name + SEP + self.phoneNr + SEP + self.group
