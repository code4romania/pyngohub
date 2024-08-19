from dotenv import find_dotenv, load_dotenv


def pytest_configure():
    load_dotenv(find_dotenv(filename=".env.test"))


class FakeHTTPSConnection:
    def __init__(self, status):
        self.status = status

    def request(self, *args, **kwargs):
        pass

    def getresponse(self):
        return FakeHTTPResponse(self.status)


class FakeHTTPResponse:
    def __init__(self, status):
        self.status = status

    @staticmethod
    def read():
        return b"OK"
