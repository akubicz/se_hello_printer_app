import json

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_XML(msg, imie)
    return result


def format_to_json(msg, imie):
    result = {"imie": imie, "msg": msg}
    json_result = json.dumps(result)
    return json_result


def format_to_XML(msg, imie):
    result = "<greetings><name>" + imie + "</name><msg>" + msg
    result += "</msg></greetings>"
    return result


def plain_text(msg, imie):
    return imie + " " + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
