from utils.constants import NUMBERS, CSV_SEP, NEWLINE

__author__ = 'Team0'


class Util:

    @staticmethod
    def isOnlyDigits(s):
        """
        Return true if a string only contains digits, false otherwise.
        """

        for i in range(len(s)):
            if s[i] not in NUMBERS:
                return False
        return True


class Exporter:

    def __init__(self, _outFName):
        self.__outFName = _outFName

    @property
    def outFName(self):
        return self.__outFName

    def exportToCVS(self, contacts):
        """
        Exports a given list of contacts to a .cvs file.
        """

        f = open(self.outFName, "w")

        for contact in contacts:
            f.write(contact.name + CSV_SEP + contact.phoneNr + NEWLINE)

        f.close()
