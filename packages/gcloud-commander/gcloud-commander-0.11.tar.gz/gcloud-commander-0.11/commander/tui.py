import sys
from commander.logger import *
from commander.walker import sidewinder
from argparse import ArgumentParser

# TODO make this function non-blocking if there is no std input, then uncomment in main.
def collect_pipe_input()->str:
    """Collect platform specific standard input text, i.e. from | 

    Returns:
        str: Mutliline str of data from pipe.
    """
    std_in_text = ""
    for line in sys.stdin:
        std_in_text += line
    return std_in_text


def entry_point(std_in_text: str, args: ArgumentParser):
    """Commandline args to pass to the program.
    Examples: --vi enables vim keybinds.
    Or standard input from | char

    Args:
        args (List[str]): program arguments to enable certain settings.
    """
    if std_in_text != "":
        basepath = sidewinder.start_fzf(args, std_in_text)
        sidewinder.surf(args, basepath=basepath)
    else:
        if args.debug:
            logging.info("Starting sidewinder w/ no std input")
        sidewinder.surf(args, "")
        
