import unittest
from test.test_entities import TestEntities
from test.test_repo import TestRepository

def repo_level_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestEntities)
    suite.addTest(TestRepository)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(repo_level_suite())