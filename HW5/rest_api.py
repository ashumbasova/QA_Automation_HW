import requests

class ApiTest:
    def __init__(self, url, newRole):
        self.url = url
        self.newRole = newRole
        self.roleID = 0

    def post(self):
        res = requests.post(self.url, data=self.newRole)
        self.roleID = res.json()['id']
        return res

    def get(self, bookUrl):
        return requests.get(bookUrl)

    def put(self, bookUrl, data):
        return requests.put(bookUrl, data=data)

    def delete(self, bookUrl):
        return requests.delete(bookUrl)