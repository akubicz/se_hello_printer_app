import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Ania", "msg":"Hello World!"}', rv.data)

    def test_xml_with_output(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Ania</name><msg>Hello World!</msg></greetings>', rv.data)

    def test_name_xml_with_output(self):
        rv = self.app.get('/?name=apolonia&output=xml')
        self.assertEqual(b'<greetings><name>apolonia</name><msg>Hello World!</msg></greetings>', rv.data)

    def test_name_json_with_output(self):
        rv = self.app.get('/?name=apolonia&output=json')
        self.assertEqual(b'{ "imie":"apolonia", "msg":"Hello World!"}', rv.data)
