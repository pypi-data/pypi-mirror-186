"""
This file contains filtering rules for which options should be passed to the argparser.parse_args() function.
It takes the .json value of an argument from args/json/*.json and filters it to decide if it should add an option to the final dict{}
"""

def should_default_be_added(settings: dict, arg_parse_params: dict)->dict:
    if settings['action'] not in ["store_true"] and settings['default'] != '':
        arg_parse_params.update({"default": settings["default"]})
    return arg_parse_params

def should_action_be_added(settings: dict, arg_parse_params: dict)->dict:
    if settings['action'] != '':
        arg_parse_params.update({"action": settings['action']})
    return arg_parse_params

def should_type_be_added(settings: dict, arg_parse_params: dict)->dict:
    if settings['action'] != '' and settings['type'] != '':
        if settings['type'] == 'int':
            arg_parse_params.update({"type": int})
        elif settings['type'] == 'str':
            arg_parse_params.update({"type": str})
    return arg_parse_params

def should_choice_be_added(settings: dict, arg_parse_params: dict)->dict:
    if settings['choices'] != [] and settings['action'] == '':
        arg_parse_params.update({"choices": settings['choices']})
    return arg_parse_params