# -*- coding: utf-8 -*-
"""
json to yaml converter
"""
import json

import yaml

from deserialize_json import DeserializeJson


class ConvertJsonToYaml:
    @staticmethod
    def run(deserializeddata: DeserializeJson, destinationfilelocaiton: str):
        print("let's convert something")
        with open(destinationfilelocaiton, 'w', encoding='utf8') as f:
            yaml.dump(deserializeddata, f, allow_unicode=True)
            print("it is done")

    @staticmethod
    def run(json_filepath: str, yaml_filepath: str):
        print("let's convert something")
        tempdata = open(json_filepath, encoding="utf8")
        data = json.load(tempdata)

        with open(yaml_filepath, 'w', encoding='utf8') as f:
            yaml.dump(data, f, allow_unicode=True)
            print("it is done")
