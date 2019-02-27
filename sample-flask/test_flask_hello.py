import unittest
import flask_hello


class TestFlaskHello(unittest.TestCase):
    def setUp(self):
        self.app = flask_hello.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert response.data.decode() == 'ハローワールド!!'


if __name__ == '__main__':
    unittest.main()
