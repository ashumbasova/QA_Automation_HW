import requests

class ApiTest:
    def __init__(self, url, newRole):
        self.url = url
        self.newRole = newRole
        self.roleID = None

    def post(self):
        res = requests.post(self.url, data=self.newRole)
        self.roleID = res.json()['id']
        return res

    def get(self, roleUrl):
        return requests.get(roleUrl)

    def put(self, roleUrl, data):
        return requests.put(roleUrl, data=data)

    def delete(self, roleUrl):
        return requests.delete(roleUrl)
