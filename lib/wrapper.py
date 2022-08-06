import os
import subprocess


def choose(options: list, limit: bool=True):
    oxot = []
    for option in options:
        oxot.append(f'"{option}"')
    options = ' '.join(oxot)
    if not limit:
        result = os.popen(f"gum choose --no-limit {options}")
    else:
        result = os.popen(f"gum choose {options}")
    if not limit:
        return result.read().replace(r"\n", "\n").strip().split("\n")
    else:
        return result.read().replace(r"\n", "\n").strip()

def input(placeholder: str=None, password: bool=False):
    if not placeholder:
        if not password:
            result = os.popen(f"gum input")
        else:
            result = os.popen(f"gum input --password")
        return result.read().replace(r"\n", "\n").strip()
    else:
        if not password:
            result = os.popen(f'gum input --placeholder "{placeholder}"')
        else:
            result = os.popen(f'gum input --password --placeholder "{placeholder}"')
        return result.read().replace(r"\n", "\n").strip()

def write(placeholder: str=None):
    if not placeholder:
        result = os.popen(f"gum write")
        return result.read().replace(r"\n", "\n").strip()
    else:
        result = os.popen(f'gum write --placeholder "{placeholder}"')
        return result.read().replace(r"\n", "\n").strip()

def confirm(text: str):
    args = [f'gum confirm "{text}"']
    res = subprocess.Popen(args, shell=True)
    res.wait()
    rco = res.returncode
    if rco == 0:
        return True
    else:
        return False


class symbols:
    line = "line"
    dot = "dot"
    minidot = "minidot"
    jump = "jump"
    pulse = "pulse" 
    points = "points"
    globe = "globe" 
    moon = "moon" 
    monkey = "monkey" 
    meter = "meter" 
    hamburger = "hamburger"

def spin(cmd: str, title:str=None,line: str=None):
    if not title:
        if not line:
            os.system(f'gum spin "{cmd}"')
        else:
            os.system(f'gum spin -s {line} "{cmd}"')
    else:
        if not line:
            os.system(f'gum spin --title "{title}" "{cmd}"')
        else:
            os.system(f'gum spin --title "{title}" -s {line} "{cmd}"')


class formattation:
    markdown = "markdown"
    code = "code"
    templace = "template"
    emoji = "emoji"


def format(text: str, format: str):
    os.system(f'echo "{text}" | gum format -t {format}')


