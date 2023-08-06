import os
import json
import argparse 
from commander.logger import *
from commander.args import arg_parse_rules
from argparse import ArgumentParser
from commander.tui import entry_point, collect_pipe_input
from commander.constants import CWD
from typing import Tuple

def get_argument_setting_values(arg_settings: dict)->Tuple[list, dict]:
    """This function takes the settings for any arg in the args/json/*.json file and parses them.

    Args:
        arg_settings (dict): The collection of settings under any arg.

    Returns:
        tuple[list, dict]: list, is the positional parameters and dict is the kwargs to unpack to argparser.parse_args() function.
    """
    positional_args = [arg_settings["flags"]["small_form"], arg_settings["flags"]["long_form"]]
    kwargs = {"help": arg_settings["help"], "required": arg_settings["required"]}

    kwargs = arg_parse_rules.should_type_be_added(arg_settings, kwargs)
    kwargs = arg_parse_rules.should_action_be_added(arg_settings, kwargs)
    kwargs = arg_parse_rules.should_choice_be_added(arg_settings, kwargs)
    kwargs = arg_parse_rules.should_default_be_added(arg_settings, kwargs)

    return positional_args, kwargs

def build_args_and_parse(arg_json_directory: str)->ArgumentParser:
    parser: argparse.Argu = argparse.ArgumentParser(description="My application description")

    for filename in os.listdir(arg_json_directory):
        filepath = os.path.join(arg_json_directory, filename)
        with open(filepath) as json_file:
            data: dict = json.load(json_file)
            for arg_name, arg in data.items():
                positional_parameters, kwparameters = get_argument_setting_values(arg_settings=arg)

                try:
                    parser.add_argument(*positional_parameters, **kwparameters)
                except Exception as e:
                    print(f"There was a problem processing the values in {filepath} for argument '{arg_name}'")
                    logging.warn(f"There was a problem processing the values in {filepath} for argument '{arg_name}'")
                    logging.warn("Full params: " + arg)
                    logging.warn("Filtered params\n"+ positional_parameters + "\n" + kwparameters)
                    logging.warn("Trace:"+ e)

    args = parser.parse_args()

    if args.debug == True:
        logging.info("Created Arguments:", args)
    return args

def main():
    try:
        arg_json_directory = f"{CWD}/args/json/"

        args: ArgumentParser = build_args_and_parse(arg_json_directory)

        # entry_point(collect_pipe_input(), args)
        entry_point("", args)
    except KeyboardInterrupt as e:
        print("Process closed due to keyboard interrupt.")

if __name__ == "__main__":
    main()