from utils.constants import SEP

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""


class Contact:

    def __init__(self, _id=None, _name=None, _phoneNo=None, _group=None):
        self.__id = _id
        self.__name = _name
        self.__phoneNo = _phoneNo
        self.__group = _group

    @property
    def _id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phoneNr(self):
        return self.__phoneNo

    @property
    def group(self):
        return self.__group

    def __eq__(self, other):
        return self._id == other._id

    def __str__(self, *args, **kwargs):
        return self.name + SEP + self.phoneNo + SEP + self.group
