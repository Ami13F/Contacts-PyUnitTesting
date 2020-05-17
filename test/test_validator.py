from domain.contact import Contact
from domain.contactValidator import ContactValidator, ValidationException

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

import unittest


class TestValidator(unittest.TestCase):

    def test_validator_old(self):

        contact = Contact("1", "George", "0747640445", "Friends")
        ContactValidator.validate(contact)

        bad_digits_contact = Contact("1", "George", "074a7640445", "Friends")
        try:
            ContactValidator.validate(bad_digits_contact)
            assert False
        except ValidationException:
            assert True

        bad_name_contact = Contact("2", "", "0444334", "Family")
        try:
            ContactValidator.validate(bad_name_contact)
            assert False
        except ValidationException:
            assert True

        bad_group_contact = Contact("3", "Gabi", "055", "Pets")
        try:
            ContactValidator.validate(bad_group_contact)
            assert False
        except ValidationException:
            assert True

    def test_validator_new(self):
        bad_name_contact = Contact("2", "", "0444334", "Family")
        self.assertRaises(ValidationException, ContactValidator.validate, bad_name_contact)

        with self.assertRaises(ValidationException) as context:
            ContactValidator.validate(bad_name_contact)

        self.assertIsInstance(context.exception, ValidationException)


    @unittest.skip("This group will be added")
    def test_fail(self):
        bad_group_contact = Contact("4", "John", "123", "Programmers")        
        ContactValidator.validate(bad_group_contact)
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
unittest.TextTestRunner(verbosity=2).run(suite)