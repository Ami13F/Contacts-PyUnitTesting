from domain.entities import Contact
from repository.repo import ContactRepository, RepositoryException

__author__ = 'Team0'

import unittest


class TestRepository(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.__repo = ContactRepository(
            "/home/Team0/work/py/examen-fp/src/contacte.txt")

    @property
    def repo(self):
        return self.__repo

    def test_repo(self):
        contact = Contact("1", "George", "0747640445", "Prieteni")
        contact1 = Contact("2", "Gigel Frone", "55555", "Altele")

        self.repo.add(contact)
        self.repo.add(contact1)

        self.assertNotEquals(0, self.repo.size())

        self.assertEquals(self.repo.find("George"), contact)

        try:
            self.repo.find("Gigel")
            assert False
        except RepositoryException:
            assert True

        self.assertEqual(self.repo.getAllFor("Prieteni")[0], contact)

        try:
            self.repo.getAllFor("Job")
            assert False
        except RepositoryException:
            assert True
