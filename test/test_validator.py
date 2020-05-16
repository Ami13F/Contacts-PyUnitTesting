from domain.entities import Contact
from domain.validator import ContactValidator, ValidationException

__author__ = 'Team0'

import unittest


class TestValidator(unittest.TestCase):

    def test_validator(self):

        contact = Contact("1", "George", "0747640445", "Prieteni")
        ContactValidator.validate(contact)

        bad_digits_contact = Contact("1", "George", "074a7640445", "Prieteni")
        try:
            ContactValidator.validate(bad_digits_contact)
            assert False
        except ValidationException:
            assert True

        bad_name_contact = Contact("2", "", "0444334", "Familie")
        try:
            ContactValidator.validate(bad_name_contact)
            assert False
        except ValidationException:
            assert True

        bad_group_contact = Contact("3", "Gabi", "055", "Programatori")
        try:
            ContactValidator.validate(bad_group_contact)
            assert False
        except ValidationException:
            assert True

