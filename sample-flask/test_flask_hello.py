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

    def test_hello_world_get_parameter(self):
        response = self.app.get('/hello_world_get_parameter/aaa?parameter_variable=bbb')
        a = ast.literal_eval(response.data.decode())
        b = {
            "path_variable": "aaa",
            "parameter_variable": "bbb"
        }
        assert all((k, v) in a.items()
                   for (k, v) in b.items())

    def test_hello_world_post_parameter(self):
        response = self.app.post('/hello_world_post_parameter/aaa', data=dict(parameter_variable="bbb"))
        a = ast.literal_eval(response.data.decode())
        b = {
            "path_variable": "aaa",
            "parameter_variable": "bbb"
        }
        assert all((k, v) in a.items()
                   for (k, v) in b.items())

    def test_hello_world_post_parameter_json(self):
        response = self.app.post('/hello_world_post_parameter_json/aaa',
                                 json={"parameter_variable": "bbb"},
                                 content_type="application/json")
        a = ast.literal_eval(response.data.decode())
        b = {
            "path_variable": "aaa",
            "parameter_variable": "bbb"
        }
        assert all((k, v) in a.items()
                   for (k, v) in b.items())

    def test_hello_world_post_parameter_json_error(self):
        response = self.app.post('/hello_world_post_parameter_json/aaa',
                                 json={"parameter_variable": "bbb"},
                                 content_type="application/x-www-form-urlencoded")
        a = ast.literal_eval(response.data.decode())
        b = {
            "status": "error"
        }
        assert all((k, v) in a.items()
                   for (k, v) in b.items())


if __name__ == '__main__':
    unittest.main()
