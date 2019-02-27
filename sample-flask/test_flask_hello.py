import unittest
import flask_hello
import ast


class TestFlaskHello(unittest.TestCase):
    def setUp(self):
        self.app = flask_hello.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert response.data.decode() == 'ハローワールド!!'

    def test_hello_world_json(self):
        response = self.app.get('/hello_world_json')
        a = ast.literal_eval(response.data.decode())
        b = {"aa": "bb"}
        assert all((k, v) in a.items()
                   for (k, v) in b.items())


if __name__ == '__main__':
    unittest.main()
