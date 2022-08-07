#!/usr/bin/python3
import lib.wrapper as gw
import re, os, sys
from tabulate import tabulate
import requests

home = os.path.expanduser('~')

def setup():
    try:
        os.mkdir(f"{home}/.config/clorg/")
    except:
        pass
    try:
        open(f"{home}/.config/clorg/default.list", "w").write("")
        #url = "https://github.com/UnityTheCoder/Clorg/raw/main/gum"
        #os.system(f"sudo sh -c 'curl -L {url} > /usr/bin/gum'; sudo chmod +x /usr/bin/gum")
    except Exception as e:
        print(e)


def add(name: str, desc: str):
    #re.findall('\[(.*?)\]',s)
    query = f"[{name}] [{desc}] [Uncomplete]"
    open(f"{home}/.config/clorg/default.list", "a").write(query + "\n")

def read():
    activities = []
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
    lines = list.split("\n")
    i=0
    for line in lines:
        ir = re.findall('\[(.*?)\]',line)
        ko = [i]
        for it in ir:
            ko.append(it)
        activities.append(ko)
        i+=1

    all_data = [["ID", "Name", "Description", "Status"]
            ]
    for activity in activities:
        try:
            activity[3] = activity[3].replace("Uncomplete", "").replace("Completed", "")
            all_data.append(activity)
        except:
            return False


    table = tabulate(all_data,headers='firstrow',tablefmt='fancy_grid')

    print(table)

def remove(id: int):
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
    lines = list.split("\n")
    newlist = ""
    i=0
    for line in lines:
        if i == id:
            pass
        else:
            newlist+=line+"\n"
        i+=1
    open(f"{home}/.config/clorg/default.list", "w").write(newlist)

def set(id: int, query: str):
    if query == "completed":
        list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
        lines = list.split("\n")
        newlist = ""
        i=0
        for line in lines:
            if i == id:
                ir = re.findall('\[(.*?)\]',line)
                ir[2] = "Completed"
                string = f"[{ir[0]}] [{ir[1]}] [{ir[2]}]"
                newlist+= string+"\n"
            else:
                newlist+=line+"\n"
            i+=1
        open(f"{home}/.config/clorg/default.list", "w").write(newlist)
    if query == "uncompleted":
        list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
        lines = list.split("\n")
        newlist = ""
        i=0
        for line in lines:
            if i == id:
                ir = re.findall('\[(.*?)\]',line)
                ir[2] = "Uncomplete"
                string = f"[{ir[0]}] [{ir[1]}] [{ir[2]}]"
                newlist+= string+"\n"
            else:
                newlist+=line+"\n"
            i+=1
        open(f"{home}/.config/clorg/default.list", "w").write(newlist)





def cliset():
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip().replace("Uncomplete", "").replace("Completed", "")
    lines = list.split("\n")
    selected = gw.choose(lines).replace("", "Uncomplete").replace("", "Completed")
    opt = ["completed", "uncompleted"]
    selected2 = gw.choose(opt)
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
    lines = list.split("\n")
    i=0
    target = None
    for line in lines:
        if line == selected:
            target = i
            break
        i+=1

    set(target, selected2)



def cliadd():
    name = gw.input("Name")
    desc = gw.input("Description")
    add(name, desc)


def cliremove():
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip().replace("Uncomplete", "").replace("Completed", "")
    lines = list.split("\n")
    selected = gw.choose(lines).replace("", "Uncomplete").replace("", "Completed")
    list = open(f"{home}/.config/clorg/default.list", "r").read().strip()
    lines = list.split("\n")
    i=0
    target = None
    for line in lines:
        if line == selected:
            target = i
            break
        i+=1
    remove(target)






help = """
            USAGE

- set   
- add
- list
- remove  
- setup
"""




if __name__ == "__main__":
    if len(sys.argv) < 2:
        gw.format(help, gw.formattation.markdown)
        sys.exit(1)
    else:
        if sys.argv[1] == "list":
            read()
        elif sys.argv[1] == "set":
            cliset()
        elif sys.argv[1] == "add":
            cliadd()
        elif sys.argv[1] == "setup":
            setup()
        elif sys.argv[1] == "remove":
            cliremove()
