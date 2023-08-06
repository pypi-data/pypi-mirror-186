#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from arg_parse import arg_parse
from parse_config import parse_config
from get_software import get_software

home_dir = os.path.expanduser("~")
config_file = home_dir + "/.config/robin/software_deployment.yaml"

if __name__ == "__main__":

    
    arg_parse(config_file, home_dir)
    # config = parse_config()
    # get_software(config)
