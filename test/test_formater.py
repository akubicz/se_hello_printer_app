from hello_world.formater import (
    plain_text_upper_case,
    plain_text_lower_case,
    plain_text,
)
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lowercase(self):
        r = plain_text_lower_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_text(self):
        r = plain_text("www", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.islower())
