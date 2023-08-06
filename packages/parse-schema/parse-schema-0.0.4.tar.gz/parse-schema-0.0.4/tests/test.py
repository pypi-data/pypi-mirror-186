from parse_schema import Schema
import json


def test_rel_path():
    schema = Schema("./tests/xpath.xml")
    assert len(schema)


def test_to_json():
    schema = Schema("/home/zavx0z/projects/parse_schema/tests/xpath.xml")
    json_string = json.dumps(schema)
    assert type(json_string) == str
