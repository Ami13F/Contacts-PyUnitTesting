from domain.contact import Contact

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

import unittest


class TestEntities(unittest.TestCase):

    def test_entity(self):
        contact = Contact("1", "Francis", "0747640445", "Friends")
        self.assertEqual(contact._id, "1")
        self.assertIs(contact.name, "Francis")
        self.assertEqual(contact.phoneNr, "0747640445")
        self.assertEqual(contact.group, "Friends")

    def test_empty_entity(self):
        contact = Contact(_name="John")
        self.assertIsNone(contact.group)
        self.assertIsNotNone(contact.name)
        self.assertIsNone(contact.phoneNr)
        self.assertIsNone(contact._id)
