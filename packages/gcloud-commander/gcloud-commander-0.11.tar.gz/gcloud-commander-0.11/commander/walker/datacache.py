from commander.logger import *
from argparse import ArgumentParser
from commander.constants import CACHE_DIR


def cache_data(args: ArgumentParser, str_to_cache: str, fname: str, filemode: str = 'a'):
    """Saves data to the cache locaton

    Args:
        args (ArgumentParser): Command line args for the program.
    """
    filename = f"{CACHE_DIR}{fname}"
    not_duplicate = filter_duplicates(args, item_to_find=str_to_cache, filename=filename)
    if not_duplicate:
        if args.debug == True:
            logging.info(f"Opening cache file at {filename}")
        with open(filename, filemode) as f:
            f.write(str_to_cache + '\n')

def load_cache_data(args: ArgumentParser, fname: str)->str:
    filename = f"{CACHE_DIR}{fname}"
    try:
        with open(filename, 'r') as f:
            return f.read()
    except (FileNotFoundError, EOFError):
        if args.debug == True:
            logging.warn(f"Was unable to open cache file {filename} verify if it should've been created.")
        return None

def filter_duplicates(args: ArgumentParser, item_to_find, filename: str)->bool:
    """Used to check if item is already in cache file.
    Returns:
        bool: Returns True if item not in cache file(new item), False otherwise
    """
    cache_file_contents = load_cache_data(args, filename.split('/')[-1:][0])
    if cache_file_contents == None:
        return True

    if item_to_find+'\n' not in cache_file_contents:
        if args.debug == True:
            logging.info(f"Found new basepath {item_to_find} to add to {filename}")
        return True

    return False