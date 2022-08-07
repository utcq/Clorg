#!/usr/bin/python3
import lib.wrapper as gw
import re, os, sys
from tabulate import tabulate
import requests
from colorama import *
import shutil


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


def add(name: str, desc: str, choosen):
    #re.findall('\[(.*?)\]',s)
    query = f"[{name}] [{desc}] [Uncomplete]"
    open(f"{home}/.config/clorg/{choosen}.list", "a").write(query + "\n")

def read():
    lists = retrieveLists()
    for listx in lists:
        lilen = len(listx)
        ascii = f"""


    ╒═══════════════════════{"══" * int(lilen/2)}╕
    │           {listx}     {" " * int(lilen - 1)}│
    ╘═══════════════════════{"══" * int(lilen/2)}╛"""
        activities = []
        list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
        if list == "":
            continue
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
                table = tabulate(all_data,headers='firstrow',tablefmt='fancy_grid')
                print(ascii)
                print(table)

            except:
                continue
            



def remove(id: int, listx):
    list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
    lines = list.split("\n")
    newlist = ""
    i=0
    for line in lines:
        if i == id:
            pass
        else:
            newlist+=line+"\n"
        i+=1
    open(f"{home}/.config/clorg/{listx}.list", "w").write(newlist)

def set(id: int, query: str, listx):
    if query == "completed":
        list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
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
        open(f"{home}/.config/clorg/{listx}.list", "w").write(newlist)
    if query == "uncompleted":
        list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
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
        open(f"{home}/.config/clorg/{listx}.list", "w").write(newlist)





def cliset():
    lists = retrieveLists()
    listx = gw.choose(lists)
    list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip().replace("Uncomplete", "").replace("Completed", "")
    lines = list.split("\n")
    selected = gw.choose(lines).replace("", "Uncomplete").replace("", "Completed")
    opt = ["", ""]
    selected2 = gw.choose(opt).replace("", "completed").replace("", "uncompleted")
    list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
    lines = list.split("\n")
    i=0
    target = None
    for line in lines:
        if line == selected:
            target = i
            break
        i+=1

    set(target, selected2, listx)



def cliadd():
    lists = retrieveLists()
    listx = gw.choose(lists)
    name = gw.input("Name")
    desc = gw.input("Description")
    add(name, desc, listx)


def cliremove():
    lists = retrieveLists()
    listx = gw.choose(lists)
    list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip().replace("Uncomplete", "").replace("Completed", "")
    lines = list.split("\n")
    selected = gw.choose(lines).replace("", "Uncomplete").replace("", "Completed")
    confirm = gw.confirm("Confirm?")
    if confirm:
        list = open(f"{home}/.config/clorg/{listx}.list", "r").read().strip()
        lines = list.split("\n")
        i=0
        target = None
        for line in lines:
            if line == selected:
                target = i
                break
            i+=1
        remove(target, listx)



def climport():
    path = gw.input("path").replace("~", home)
    if os.path.exists(path):
        pass
    else:
        print(Fore.RED + "[-] Invalid Path!" + Fore.RESET)
        return False
    if path.endswith(".list"):
        pass
    else:
        print(Fore.RED + "[-] File must be a .list!" + Fore.RESET)
        return False
    shutil.copy(path, f"{home}/.config/clorg/")
    print(Fore.GREEN + "Imported!" + Fore.RESET)

def retrieveLists():
    path = home + "/.config/clorg/"
    lists = []
    for files in os.listdir(path):
        filep = os.path.join(path, files)
        if os.path.isfile(filep) and filep.endswith(".list"):
            lists.append(files.replace(".list", ""))
    return lists


def cliexport():
    lists = retrieveLists()
    sel = gw.choose(lists, False)
    for s in sel:
        pfile = f"{home}/.config/clorg/{s}.list"
        shutil.copy(pfile, home)
        print(Fore.GREEN + "[+] Copied List in ~/" + s + ".list")





def newlistcli():
    name = gw.input("Name")
    open(f"{home}/.config/clorg/{name}.list", 'w').write("")


def removelistcli():
    lists = retrieveLists()
    choosen = gw.choose(lists, False)
    for name in choosen:
        os.remove(f"{home}/.config/clorg/{name}.list")





help = """
            USAGE

- set   
- add
- list
- remove  
- setup
- import
- export
- newlist
- removelist
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
        elif sys.argv[1] == "import":
            climport()
        elif sys.argv[1] == "export":
            cliexport()
        elif sys.argv[1] == "newlist":
            newlistcli()
        elif sys.argv[1] == "removelist":
            removelistcli()


