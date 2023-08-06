import os
import subprocess
from commander.logger import *
from google.cloud import storage
from prompt_toolkit import prompt
from argparse import ArgumentParser
from typing import Tuple
from commander.constants import OPTIONS, PLATFORM
from commander.walker.datacache import cache_data, load_cache_data
from prompt_toolkit.completion import Completer, Completion, ThreadedCompleter

class SideCompletion(Completer):
    def __init__(self):
        self.options = []

    def get_completions(self, document, complete_event):
        # Provide custom autocomplete suggestions based on the current input
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        if word_before_cursor:
            try:
                if(word_before_cursor.startswith('gs://')):
                    # TODO self.options = gcp.listdir
                    pass
                else:
                    self.options = os.listdir(word_before_cursor)
            except:
                pass

            last_word = word_before_cursor.split('/')[-1:][0]


            for opt in self.options:
                # if last_word in opt:
                if opt.startswith(last_word):
                    rest_of_word = opt[len(last_word):]
                    yield Completion(rest_of_word)

def echo_localdir(args: ArgumentParser, action: str,base_path_to_fzf: str, fzf: subprocess.Popen)->None:
    for dirpath, dirnames, filenames in os.walk(base_path_to_fzf):
        dirpath = dirpath.replace('\\', '/')
        for filename in filenames:
            line = ""
            if action.startswith("ls"):
                line = f"{dirpath}/\n"
            else:
                line = f"{dirpath}/{filename}\n"
            fzf.stdin.write((line).encode())

def echo_gcpdir(args: ArgumentParser, action: str, bucket_name: str, fzf: subprocess.Popen)->None:
    client = storage.Client()
    bucket_contents = client.list_blobs(bucket_name)
    for i in bucket_contents:
        fzf.stdin.write((i).encode())


def walkdir(args: ArgumentParser, action: str, base_path_to_fzf: str)->str:
    base_path_to_fzf = base_path_to_fzf.replace('\n', '')
    fzf = subprocess.Popen(["fzf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        if base_path_to_fzf.startswith("gs://"):
            echo_gcpdir(args, action, base_path_to_fzf, fzf)
        else:
            echo_localdir(args, action, base_path_to_fzf, fzf)
    except:
        pass

    output, _ = fzf.communicate()
    output = output.decode()
    return output

def start_fzf(args: ArgumentParser, to_send: str)->str:
    fzf = subprocess.Popen(["fzf"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, _ = fzf.communicate(to_send.encode())
    output = output.decode()

    if args.debug:
        logging.info("Selected item: ", output)
    return output

def ls_logic(args: ArgumentParser, action:str, base_path_to_fzf: str)->Tuple[str, str]:
        left_selected: str = walkdir(args, action, base_path_to_fzf) 
        right_selected: str = ""
        return left_selected, right_selected

def mv_logic(args: ArgumentParser, action:str, base_path_to_fzf: str)->Tuple[str, str]:
        left_selected: str = walkdir(args, action, base_path_to_fzf) 
        basepath_options = load_cache_data(args, fname="basepaths")
        right_selected: str = start_fzf(args, basepath_options)

        side_winder_completer = SideCompletion()
        thread_completer = ThreadedCompleter(side_winder_completer)
        if args.vim == True:
            right_selected = prompt("Move to: ", default=right_selected.replace('\n', ''), completer=thread_completer, vi_mode=True)
        else: 
            right_selected = prompt("Move to: ", default=right_selected.replace('\n', ''), completer=thread_completer,)
        return left_selected, right_selected

def cp_logic(args: ArgumentParser, action:str, base_path_to_fzf: str)->Tuple[str, str]:
        left_selected: str = walkdir(args, action, base_path_to_fzf) # TODO add OPEN in browser option
        basepath_options = load_cache_data(args, fname="basepaths")
        right_selected: str = start_fzf(args, basepath_options)
        if args.vim == True:
            right_selected = prompt("Copy to: ", default=right_selected.replace('\n', ''), vi_mode=True)
        else: 
            right_selected = prompt("Copy to: ", default=right_selected.replace('\n', ''))
        return left_selected, right_selected

def rm_logic(args: ArgumentParser, action:str, base_path_to_fzf: str)->Tuple[str, str]:
        left_selected: str = walkdir(args, action, base_path_to_fzf) # TODO add OPEN in browser option
        right_selected: str = ""
        return left_selected, right_selected

def action_logic(args: ArgumentParser, action: str, base_path_to_fzf: str)->str:
    left_selected = ""
    right_selected = ""
    if action.startswith("ls"):
        left_selected, right_selected = ls_logic(args, action, base_path_to_fzf)
    elif action.startswith("mv"):
        left_selected, right_selected = mv_logic(args, action, base_path_to_fzf)
    elif action.startswith("cp"):
        left_selected, right_selected = cp_logic(args, action, base_path_to_fzf)
    elif action.startswith("rm"):
        left_selected, right_selected = rm_logic(args, action, base_path_to_fzf)
    else:
        print(f"Invalid movement option: {action}")

    cmd = ""
    if base_path_to_fzf.startswith('gs://'):
        cmd = f"gsutil -m {action} {left_selected} {right_selected}".replace('\n', ' ')
    else:
        cmd = f"{action} {left_selected} {right_selected}".replace('\n', ' ')

    return cmd


def surf(args: ArgumentParser, basepath: str):
    """Start sidewinder, event_loop for the TUI application.
    """
    if args.basepath != "":
        cache_data(args, str_to_cache=args.basepath, fname="basepaths")
        basepath_options = load_cache_data(args, fname="basepaths")
        action: str = start_fzf(args, OPTIONS)
        base_path_to_fzf = start_fzf(args, basepath_options)
        print("Base path to look inside of ",base_path_to_fzf)

        if(base_path_to_fzf.startswith("gs://")):
            google_env_variable = 'GOOGLE_APPLICATION_CREDENTIALS'
            try: 
                os.environ[google_env_variable] 
            except: 
                print(f"gsutil credentials environment variable not set. \nCheck the {google_env_variable} environment variable.")


        result_cmd = action_logic(args, action, base_path_to_fzf)

        side_winder_completer = SideCompletion()
        thread_completer = ThreadedCompleter(side_winder_completer)
        if args.vim == True:
            result_cmd = prompt("Run this command? ", default=result_cmd, completer=thread_completer,vi_mode=True)
        else: 
            result_cmd = prompt("Run this command? ", default=result_cmd, completer=thread_completer)

        if args.debug == True:
            print("would execute: ", result_cmd)
        else:
            if result_cmd != "":
                command_exec = ""
                if PLATFORM.startswith("win"):
                    command_exec = subprocess.run(["powershell.exe", "-Command", result_cmd],
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()
                else:
                    command_exec = subprocess.run([result_cmd],
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()

                print(command_exec)