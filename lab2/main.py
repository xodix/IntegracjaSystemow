from convert_json_to_yaml import ConvertJsonToYaml
from serialize_json import SerializeJson
from deserialize_json import DeserializeJson
import yaml

if __name__ == "__main__":
    tempconffile = open('Assets/basic_config.yaml',
                        encoding="utf8")
    confdata = yaml.load(tempconffile, Loader=yaml.FullLoader)
    print("hey, it's me - Python!")
    newDeserializator = DeserializeJson(
        confdata['paths']['source_folder']+confdata['paths']['json_source_file'])
    newDeserializator.somestats()

    SerializeJson.run(newDeserializator, confdata['paths']['source_folder'] +
                      confdata['paths']['json_destination_file'])
    ConvertJsonToYaml.run(confdata['paths']['source_folder'] +
                          confdata['paths']['json_destination_file'], confdata['paths']['source_folder'] +
                          confdata['paths']['yaml_destination_file'])
