from utils.constants import VALID_GROUPS
from utils.util import Util

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""


class ValidationException(Exception):
    pass


class DuplicationException(Exception):
    pass


class ContactValidator:

    @staticmethod
    def validate(contact):
        """
        Validates a contact, throws ValidationException if incorrect data.
        """

        msg = ""

        if contact.name is "" or None:
            msg += "Name cannot be empty."
        if not contact.group in VALID_GROUPS:
            msg += "Not a valid group."
        if contact.phoneNr is "" or None:
            msg += "Phone nr cannot be null."
        if not Util.isOnlyDigits(contact.phoneNr):
            msg += "Phone nr can only be digits."

        if msg:
            raise ValidationException(msg)

    @staticmethod
    def checkDuplicates(contact, all):
        """
        Throws exception if 2 phone numbers try to relate to the same name
        """
        for c in all:
            if contact.name == c.name:
                raise DuplicationException(
                    "There already is a name associated with this phone number.")

