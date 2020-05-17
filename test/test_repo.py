from domain.contact import Contact
from repository.contactRepository import ContactRepository, RepositoryException

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

import unittest


class TestRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.__repo = ContactRepository("./test/contacts.txt")


    @classmethod
    def tearDownClass(cls):
        """
        clear after all tests
        """
        super().tearDownClass()
        cls.__repo.clear()


    @property
    def repo(self):
        return self.__repo


    def test_add_success(self):
        contact = Contact("1", "Robert", "0747640445", "Friends")

        self.repo.add(contact)
        self.assertNotEqual(0, self.repo.size())
        self.assertEqual(self.repo.find(contact.name), contact)


    def test_add_failed(self):
        pass


    def test_contact_not_exists(self):
        try:
            self.repo.find("Alvin")
            assert False
        except RepositoryException:
            assert True

        self.assertEqual(self.repo.get_all_from_group("Friends")[0], contact)

        try:
            self.repo.get_all_from_group("Job")
            assert False
        except RepositoryException:
            assert True


    @unittest.expectedFailure
    def test_not_find(self):
        self.repo.find("Jannine")


suite = unittest.TestLoader().loadTestsFromTestCase(TestRepository)
unittest.TextTestRunner(verbosity=2).run(suite)