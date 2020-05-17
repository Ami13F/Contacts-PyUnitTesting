from controller.agendaController import AgendaController
from domain.contactValidator import DuplicationException
from repository.contactRepository import ContactRepository

__author__ = 'Team0'

import os
from shutil import copyfile
import unittest


class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.csv_file = "./test/contacts.csv"
        cls.storage = "./test/main_storage.txt"
        cls.filename = "./test/contacts.txt"
        if not os.path.exists(cls.filename):
            copyfile(cls.storage, cls.filename)


    def setUp(self):
        super().setUp()
        repo = ContactRepository(self.filename)
        self.__controller = AgendaController(repo)


    def test_export_csv(self):
        self.__controller.export_csv("Friends",
                self.csv_file)
        self.assertIsNotNone(os.path.exists(self.csv_file))


    def test_add_to_empty_controller(self):
        old_count = len(self.__controller.get_all())
        self.__controller.add_contact("150", "Arthur", "5342453", "Family")
        new_count = len(self.__controller.get_all())

        self.assertGreater(new_count, old_count)


    def tearDown(self):
        super().tearDown()
        print("Tear down after each test")
        self.__controller.clear()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        os.remove(cls.csv_file)
        os.remove(cls.filename)
