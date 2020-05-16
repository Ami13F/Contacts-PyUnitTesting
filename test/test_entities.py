from domain.entities import Contact

__author__ = 'Team0'

import unittest


class TestEntities(unittest.TestCase):

    def test_entity(self):
        contact = Contact("1", "George", "0747640445", "Prieteni")
        self.assertEqual(contact._id, "1")
        self.assertEqual(contact.name, "George")
        self.assertEqual(contact.phoneNr, "0747640445")
        self.assertEqual(contact.group, "Prieteni")
