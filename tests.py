import unittest
from disqus import *

"""Configuration"""
# Must supply a Disqus API key for tests
secret_key = ''

"""Unit Tests"""

class AuthTests(unittest.TestCase):

    def setUp(self):
        self.auth = Auth(secret_key)

    def testValidateKey(self):
        self.auth.validate()

    def testGetUsername(self):
        self.auth.username()


class DisqusAPITests(unittest.TestCase):

    def setUp(self):
        pass
