from requests.auth import HTTPBasicAuth


class AcodisAuth():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __call__(self):
        return HTTPBasicAuth(self.user, self.password)
