import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get("/outputs")
        s = str(rv.data)
        ",".join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get("/?output=json")
        self.assertEqual(b'{ "imie":"Anna", "msg":"Hello World!"}', rv.data)

    def test_xml_with_output(self):
        rv = self.app.get("/?output=xml")
        expected = "<greetings><name>Anna</name>" "<msg>Hello World!"
        expected += "</msg></greetings>"

        self.assertEqual(bytes(expected, encoding="utf-8"), rv.data)

    def test_name_xml_with_output(self):
        rv = self.app.get("/?name=apolonia&output=xml")
        expected = "<greetings><name>apolonia</name>"
        expected += "<msg>Hello World!</msg></greetings>"
        self.assertEqual(bytes(expected, encoding="utf-8"), rv.data)

    def test_name_json_with_output(self):
        rv = self.app.get("/?name=apolonia&output=json")
        expected = '{ "imie":"apolonia", "msg":"Hello World!"}'
        self.assertEqual(bytes(expected, encoding="utf-8"), rv.data)
