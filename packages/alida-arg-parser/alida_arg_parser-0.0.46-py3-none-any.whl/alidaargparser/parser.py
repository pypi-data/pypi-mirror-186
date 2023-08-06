import argparse
from .property import Property
from .type_utils import str2bool
import sys
from .dataset import Dataset
from .model import Model
from .translation_dictionary import translation
import json
from .generator import generate_meta_model
import re
from .port import Port
from .map import Map

class ArgumentParser():
    def __init__(self, name, description, mode="batch", area=None, framework="default", docker_image=None):
        self.parser = argparse.ArgumentParser()
        self.properties = []
        self.input_datasets = []
        self.output_datasets = []
        self.input_models = []
        self.output_models = []
        self.ports = {}
        
        self.name = name.lower().replace(" ", "-")
        self.description = description
        self.mode = mode
        self.framework = framework

        # If area is specified by the user then leave it. Otherwise set preparation as default.
        if area is None:
            area = "preparation"
            self.lock_area = False
        else:
            self.lock_area = True
        self.area = area

        if docker_image is not None:
            self.set_docker_image(docker_image)
        else:
            self.docker_image = docker_image


    def add_argument(self, argument, 
                        help="Please fill argument description and upload again your service", 
                        type=str, 
                        default=None,
                        required=False, 
                        action=None,
                        choices=None):


        if action is not None:
            if action == 'store_true':
                type = str2bool
                default = False
            elif action == 'store_false':
                type = str2bool
                default = True
            else:
                print("The action: " + action + " is not currently supported")

        self.properties.append(Property(argument, type=type, help=help, default=default, required=required))
        self.parser.add_argument(argument, help=help, type=type, default=default, required=required, choices=choices)


    def add_input_dataset(self, argument="--input_dataset", help=None, columns_type=None, data_type="table"):
        self.parser.add_argument(argument, help=help, required=True, type=str)
        self.input_datasets.append(Dataset(name=argument[2:], description=help, columns_type=columns_type, data_type=data_type))

    def add_output_dataset(self, argument="--output_dataset", help=None):
        self.parser.add_argument(argument, help=help, required=True, type=str)
        self.output_datasets.append(Dataset(name=argument[2:], description=help))

    def add_input_model(self, argument="--input_model", help=None):
        self.parser.add_argument(argument, help=help, required=True, type=str)
        self.input_models.append(Model(name=argument[2:], description=help))
        self.change_area("analysis")
    
    def expose_port(self, name="default", help="Port to expose.", number=5000, http_model="http"):
        self.parser.add_argument("--ports." + name + ".number", help=help + ". Port number.", type=int, default=number, required=False)
        self.parser.add_argument("--ports." + name + ".http_model", help=help+ ". Port http model.", type=str, default=http_model, required=False)
        self.ports[name] = Port(name=name, description=help, number=number, http_model=http_model)

    def add_output_model(self, argument="--output_model", help=None):
        self.parser.add_argument(argument, help=help, required=True, type=str)
        self.output_models.append(Model(name=argument[2:], description=help))
        self.change_area("analysis")

    def parse_args(self):
        return self.parse_known_args()

    def parse_known_args(self):
        args = sys.argv[1:]

        # Standard python boolean args do not work as in Alida. 
        # Hence, we need to convert boolean args properly.

        # Replace all dashes in the mid of a word with underscores
        args = [replace_dashes(arg) for arg in args]

        alida_compliant_args = []

        # Whenever a --arg_name is found, it is replace with --arg_name=<its-default-value>
        for arg in args:
            # If argument is present in args in the Alida way
            if len(arg.split("="))>1:
                alida_compliant_args.append(arg)
            # If bool is present in the python way put to to alida way
            else:
                default_value = self.get_property_default_value(arg.replace("-", ""))
                if default_value is not None:
                    alida_compliant_args.append(arg + "=" + str(not default_value).lower())

        # If a boolean is not prensent at all in args, add it with its default value
        missing_bool_args = self.find_missing_bool_args(alida_compliant_args)
        for arg in missing_bool_args:
            alida_compliant_args.append(arg + "=" + str(self.get_property_default_value(arg.replace("-", ""))))
        
        self.args, _ = self.parser.parse_known_args(args=alida_compliant_args)
        self.args = Map(vars(self.args))
        return self.args


    def get_property_default_value(self, property_name):
        for property in self.properties:
            if property.name == property_name:
                return property.default


    # Find missing boolean arguments
    def find_missing_bool_args(self, args):
        missing_args = []
        for property in self.properties:
            if property.type is str2bool:
                if "--" + property.name + "=false" not in args and "--" + property.name + "=true" not in args and "--" + property.name + "=False" not in args and "--" + property.name + "=True" not in args :
                    missing_args.append("--" + property.name)
        return missing_args


    def generate_json(self, path):
        
        json_data = generate_meta_model(name = self.name, description=self.description, framework=self.framework,
                                        properties = self.properties, 
                                        input_datasets=self.input_datasets,
                                        output_datasets = self.output_datasets,
                                        input_models = self.input_models,
                                        output_models = self.output_models,
                                        docker_image=self.docker_image,
                                        area = self.area,
                                        mode=self.mode,
                                        ports=self.ports
                                        )

        with open(path, "w") as outputFile:
            json.dump(json.loads(clean_json(json_data)), outputFile, indent=4)    #, sort_keys=True)


    def set_docker_image(self, docker_image):
        self.docker_image = "docker://" + docker_image

    # Based on the class extended by the developer to create his service, find out ALIDA service mode
    def set_mode(self, _class):
        self.mode =_class.alida_service_mode
        if self.mode == "source" or self.mode == "sink":
            self.change_area("ingestion")

    def change_area(self, new_area):
        if not self.lock_area:
            self.area = new_area

    def parse_ports(self):
        for port in self.ports.values():
            self.ports[port.name].number = self.args["ports." + port.name + ".number"]
            self.ports[port.name].http_model = self.args["ports." + port.name + ".http_model"]
        return self.ports

def clean_json(string):
    string = re.sub(",[ \t\r\n]+}", "}", string)
    string = re.sub(",[ \t\r\n]+\]", "]", string)

    return string

def replace_dashes(string):
    key = string.split("=")[0]
    value = string.replace(key, "")
    return "--" + key.replace("-", "_")[2:] + value


