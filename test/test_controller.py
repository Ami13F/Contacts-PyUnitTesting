from controller.agendaController import AgendaController
from domain.contactValidator import DuplicationException
from repository.contactRepository import ContactRepository

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

import os
import unittest


class TestController(unittest.TestCase):
    
    def setUp(self):
        super().setUp()
        repo = ContactRepository("./test/contacts.txt")
        self.__controller = AgendaController(repo)
        self.__csv_file = "./test/contacts.csv"


    def test_export_csv(self):
        self.__controller.export_csv("Friends",
                self.__csv_file)
        self.assertIsNotNone(os.path.exists(self.__csv_file))


    def test_add_to_empty_controller(self):
        old_count = len(self.__controller.get_all())

        self.__controller.add_contact("100", "Arthur", "102938114", "Family")
        new_count = len(self.__controller.get_all())

        self.assertGreater(new_count, old_count)


    def tearDown(self):
        super().tearDown()
        print("Tear down after each test")
        self.__controller.clear()
        os.remove(self.__csv_file)
