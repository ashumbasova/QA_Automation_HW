import unittest
from rest_api import ApiTest

url = 'http://pulse-rest-testing.herokuapp.com/roles/'
newRole = {
                    "name": "Sir Magician",
                    "type": "Senior Wizard",
                    "level": 500,
                    "book": 1,
  }

class Tests(unittest.TestCase):

    def setUp(self):
        self.role = ApiTest(url, newRole)
        self.role.post()
        self.roleUrl = self.role.url + str(self.role.roleID) + '/'

    def test1(self):
        self.assertEqual(self.role.get(self.roleUrl).json()["name"], 'Sir Magician')
        self.assertEqual(self.role.get(self.roleUrl).json()["level"], 500)
        self.assertEqual(self.role.put(self.roleUrl, {'name': 'Anna S'}).json()['name'], 'Anna S')

    def tearDown(self):
        self.role.delete(self.roleUrl)
