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

        # def test_post(self):
        #     self.assertEqual(self.role.post().status_code, 201)
        #     self.role.delete(self.roleUrl)

    def test_get(self):
        res = self.role.get(self.roleUrl)
        self.assertEqual(res.json()["name"], 'Sir Magician')
        self.assertEqual(res.json()["type"], 'Senior Wizard')
        self.assertEqual(res.json()["level"], 500)
        self.assertEqual(res.json()['book'], 1)
        self.assertEqual(res.status_code, 200)

    def test_put(self):
        res = self.role.put(self.roleUrl, {'name': 'Anna S', 'type': 'QA'})
        self.assertEqual(res.json()['name'], 'Anna S')
        self.assertEqual(res.json()['type'], 'QA')
        self.assertEqual(res.status_code, 200)

    def test_del(self):
        self.assertEqual(self.role.delete(self.roleUrl).status_code, 204)

        # def test_get_neg(self):
        #     self.assertEqual(self.role.get(self.roleUrl), 400)


    def tearDown(self):
        self.role.delete(self.roleUrl)
