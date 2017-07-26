import unittest
import requests

url = 'http://pulse-rest-testing.herokuapp.com/roles/'
newRole = {
                    "name": "Sir Magician",
                    "type": "Senior Wizard",
                    "level": 500,
                    "book": 1,
  }


class Tests(unittest.TestCase):

    def setUp(self):
        self.url = 'http://pulse-rest-testing.herokuapp.com/roles/'
        self.role = {
                    "name": "Sir Magician",
                    "type": "Senior Wizard",
                    "level": 500,
                    "book": 1,
                    }
        self.roleURL = None

    def test_post(self):
        res = self.create_role()
        self.assertEqual(res.json()['name'], "Sir Magician")
        self.roleURL = self.url + str(res.json()['id'])
        requests.delete(self.roleURL)


    def test_get(self):
        self.roleID = self.create_role().json()['id']
        self.roleURL = self.url + str(self.roleID)
        res = requests.get(self.roleURL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['type'], 'Senior Wizard')
        requests.delete(self.roleURL)

    def test_put(self):
        self.roleID = self.create_role().json()['id']
        self.roleURL = self.url + str(self.roleID) + '/'
        res = requests.put(self.roleURL, data ={'type':'qa'})
        self.assertEqual(res.json()['type'], 'qa')
        requests.delete(self.roleURL)



    def create_role(self):
        res = requests.post(self.url, data=self.role)
        return res


    # def delete_role(self, id = None):
    #     if id:
    #         return requests.delete(self.url + str(id))
