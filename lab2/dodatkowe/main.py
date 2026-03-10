from dataclasses import dataclass
import json
import xml.etree.ElementTree as ET
from typing import Any, Dict, Literal, Optional, Union
import argparse
from pathlib import Path
import xmltodict


@dataclass
class Config:
    input_path: Path
    output_path: Path
    mode: Literal["xml_to_json"] | Literal["json_to_xml"]


def filterObject(obj: Dict, config_path: str = "config.json") -> Dict:
    with open(config_path, "r") as f:
        config = json.load(f)

    def filter_by_config(data: Any, schema: Any) -> Any:
        if isinstance(schema, dict):
            if all(isinstance(v, bool) for v in schema.values()):
                if isinstance(data, dict):
                    return {
                        key: data[key]
                        for key, value in schema.items()
                        if value and key in data
                    }
                return data
            else:
                if isinstance(data, dict):
                    return {
                        key: filter_by_config(data.get(key), schema[key])
                        for key in schema.keys()
                        if key in data
                    }
                return data
        elif isinstance(schema, list):
            if isinstance(data, list) and len(schema) > 0:
                item_schema = schema[0]
                return [filter_by_config(item, item_schema) for item in data]
            return data
        else:
            return data

    return filter_by_config(obj, config)


def xml_to_json(xml_path: Path, json_path: Path):
    with open(xml_path, "r") as infile:
        xmlObject = xmltodict.parse(infile.read())
        xmlObject = filterObject(xmlObject)
        jsonString = json.dumps(xmlObject)
        with open(json_path, 'w') as f:
            f.write(jsonString)


def json_to_xml(json_path: Path, xml_path: Path):
    with open(json_path, "r") as infile:
        jsonObject = json.load(infile)
        jsonObject = filterObject(jsonObject)
        xmlString = xmltodict.unparse(jsonObject)
        with open(xml_path, 'w') as f:
            f.write(xmlString)


def get_args() -> Config:
    parser = argparse.ArgumentParser(description='JSON to XML and XML to JSON')
    parser.add_argument('--input', required=True, type=str, help='input_file')
    parser.add_argument('--output', required=True,
                        type=str, help='output_file')
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    input_extension = input_path.suffix.lstrip('.')
    output_extension = output_path.suffix.lstrip('.')

    if input_extension != "xml" and output_extension != "xml":
        print("There is no xml path present")
        exit(1)
    elif input_extension != "json" and output_extension != "json":
        print("There is no json path present")
        exit(1)
    elif input_extension == output_extension:
        print("The input extension and output extensions are the same")
        exit(1)

    return Config(input_path, output_path, mode=("json_to_xml" if input_extension == "json" else "xml_to_json"))


if __name__ == "__main__":
    config = get_args()
    print(config)
    match config.mode:
        case "xml_to_json":
            xml_to_json(config.input_path, config.output_path)
        case "json_to_xml":
            json_to_xml(config.input_path, config.output_path)
