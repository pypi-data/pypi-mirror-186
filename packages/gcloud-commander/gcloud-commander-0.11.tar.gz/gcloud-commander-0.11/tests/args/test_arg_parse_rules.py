from commander.args.arg_parse_rules import *

# should_default_be_added(settings: dict, arg_parse_params: dict)->dict:

# arg_settings = {'required': False, 'flags': {'small_form': '-b', 'long_form': '--basepath'}, 'action': '', 'help': 'A flag to predefine basepath', 'type': 'int', 'default': '', 'nargs': '+', 'choices': []}
# kwargs = {"help": arg_settings["help"], "required": arg_settings["required"]}

# NOTE to-self, dicts are passed by reference, so if you modify a dict in a function then it will modify it outside the function.

def test_should_default_be_added():
    kwargs = {}
    arg_settings = {'action': '', 'default': 'test'}
    assert should_default_be_added(arg_settings, kwargs.copy()) == {'default': 'test'}
    arg_settings = {'action': '', 'default': 'default behavior here'}
    assert should_default_be_added(arg_settings, kwargs.copy()) == {'default': 'default behavior here'}


def test_should_action_be_added():
    kwargs = {}
    arg_settings = {'action': 'store_true'}
    assert should_action_be_added(arg_settings, kwargs.copy()) == {'action': 'store_true'}
    arg_settings['action'] = 'test'
    assert should_action_be_added(arg_settings, kwargs.copy()) == {'action': 'test'}


def test_should_type_be_added():
    kwargs = {}
    arg_settings = {'action': 'test', 'type': 'int'}
    assert should_type_be_added(arg_settings, kwargs.copy()) == {'type': int}
    arg_settings['type'] = 'str'
    assert should_type_be_added(arg_settings, kwargs.copy()) == {'type': str}

    arg_settings = {'action': '', 'type': 'int'}
    assert should_type_be_added(arg_settings, kwargs.copy()) == {}
    arg_settings['type'] = 'str'
    assert should_type_be_added(arg_settings, kwargs.copy()) == {}

    arg_settings['type'] = ''
    assert should_type_be_added(arg_settings, kwargs.copy()) == {}

    arg_settings['action'] = 'x'
    assert should_type_be_added(arg_settings, kwargs.copy()) == {}


def test_should_choice_be_added():
    kwargs = {}
    arg_settings = {'action': '', 'choices': ['choice1', 'choice2']}
    print(kwargs)
    assert should_choice_be_added(arg_settings, kwargs.copy()) == {'choices': ['choice1', 'choice2']}
    print(kwargs)
    arg_settings = {'action': '', 'choices': ['sample2']}
    assert should_choice_be_added(arg_settings, kwargs.copy()) == {'choices': ['sample2']}
    print(kwargs)

    arg_settings = {'action': '', 'choices': []}
    assert should_choice_be_added(arg_settings, kwargs.copy()) == {}
    arg_settings = {'action': 'x', 'choices': []}
    assert should_choice_be_added(arg_settings, kwargs.copy()) == {}
