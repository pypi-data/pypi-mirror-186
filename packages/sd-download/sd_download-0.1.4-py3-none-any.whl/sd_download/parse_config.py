import os
import yaml
import validators

home_dir = os.path.expanduser("~")
config_file = home_dir + "/.config/robin/software_deployment.yaml"


def parse_config():
    if os.path.isfile(config_file):
        with open(config_file, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                return config
            except yaml.YAMLError as exc:
                print(exc)
    else:
        print("Config file is missing at " + config_file)
        exit(1)

    # Validate types
    if type(config['robin_email']) is not str:
        print("robin_email is not a string")
        exit(1)
    
    if type(config['robin_password']) is not str:
        print("robin_password is not a string")
        exit(1)

    if not validators.url(config['api_url']):
        print("api_url is not a valid URL")
        exit(1)

    if type(config['radar_id']) is not str:
        print("radar id is not a string")
        # print out the type of the radar_id
        # print(type(config['radar_id']))
        exit(1)