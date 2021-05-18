import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED
import xml.etree.ElementTree as ET_data
import xml.etree.ElementTree as ET_expected


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get("/outputs")
        s = str(rv.data)
        ",".join(SUPPORTED) in s

    def test_json_with_output(self):
        rv = self.app.get("/?output=json")
        test_value = json.dumps({"imie": "Anna", "msg": "Hello World!"})
        self.assertEqual(bytes(test_value.encode("utf-8")), rv.data)

    def test_xml_with_output(self):
        rv = self.app.get("/?output=xml")
        greetings = ET_expected.Element("greetings")
        expected_name = ET_expected.SubElement(greetings, "name")
        expected_msg = ET_expected.SubElement(greetings, "msg")
        expected_name.text = "Anna"
        expected_msg.text = "Hello World!"
        actual = ET_data.fromstring(rv.data)
        actual_name = actual.find("name")
        actual_msg = actual.find("msg")
        self.assertEqual(expected_msg.text, actual_msg.text)
        self.assertEqual(expected_name.text, actual_name.text)

    def test_specific_name_xml_with_output(self):
        rv = self.app.get("/?name=apolonia&output=xml")
        greetings = ET_expected.Element("greetings")
        expected_name = ET_expected.SubElement(greetings, "name")
        expected_msg = ET_expected.SubElement(greetings, "msg")
        expected_name.text = "Apolonia"
        expected_msg.text = "Hello World!"
        actual = ET_data.fromstring(rv.data)
        actual_name = actual.find("name")
        actual_msg = actual.find("msg")
        self.assertEqual(expected_msg.text, actual_msg.text)
        self.assertEqual(expected_name.text, actual_name.text)

    def test_specific_name_json_with_output(self):
        rv = self.app.get("/?name=apolonia&output=json")
        expected = '{"imie": "Apolonia", "msg": "Hello World!"}'
        self.assertEqual(bytes(expected.encode("utf-8")), rv.data)
