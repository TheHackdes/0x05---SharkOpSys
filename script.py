#!/usr/bin/env python3
import argparse
from rich import print as rprint
from rich.table import Table
from rich.console import Console
from rich_argparse import RichHelpFormatter
import os
import subprocess
import sys
import time
import docker
from rich.progress import Progress
import time 

parser = argparse.ArgumentParser(prog="sharkopsys",
        description="The SharkOpSys is a script to install best tools and environment for developper",
                                 #        epilog="Fin de mon programme",
        formatter_class=RichHelpFormatter)
parser.add_argument("-a", "--alias", help="Install the aliases")
#parser.add_argument("-p", "--project", choices=['exegol','htop'], default="htop", help="Name project")
#parser.add_argument("-w", "--workspace", help="Select the workspace")
#parser.add_argument("-i", "--image", choices=["debian", "redhat"], default="redhat", help="The name of the image")
#parser.add_argument("name", help="The name of the container")
args = parser.parse_args()

#config = vars(args)
#print(config)

path_aliases = "/etc/bash.aliases"

status = subprocess.run(['test','-e',path_aliases], capture_output=True, text=True)
print(status)
# If Existe
if status.returncode == 0 :
    timestamp = time.time()
    current_date = time.strftime('%Y.%m.%d_%H:%M:%S')
    print(current_date)
    backup_aliases = subprocess.run(['cp',path_aliases,path_aliases + current_date], capture_output=True, text=True)
    print(backup_aliases)
elif status.returncode == 1 :
    copy_aliases = subprocess.run(['cp', './aliases', path_aliases], capture_output=True, text=True)
    print(copy_aliases)
    



# Set the username
#username = subprocess.run(['whoami'], capture_output=True, text=True)
#if username.returncode != 0 :
#    rprint(":warning: [italic red]Username error ![/italic red]")
#    sys.exit(1)
#
#uuid = subprocess.run(['id', '-u', username.stdout.strip()], capture_output=True, text=True)
#if uuid.returncode != 0 :
#    rprint(":warning: [italic red]UUID error ![/italic red]")
#    sys.exit(1)
#
#guid = subprocess.run(['id', '-g', username.stdout.strip()], capture_output=True, text=True)
#if guid.returncode != 0 :
#    rprint(":warning: [italic red]GUID error ![/italic red]")
#    sys.exit(1)
#
#table = Table(show_header=False)
#
#table.add_row(":man:" + " [green]Username[/green]" , "[cyan]" + username.stdout.strip() + "[/cyan]")
#table.add_row(":id:" + " [green]UUID[/green]" , "[cyan]" + uuid.stdout.strip() + "[/cyan]")
#table.add_row(":id:" + " [green]GUID[/green]" , "[cyan]" + guid.stdout.strip() + "[/cyan]")
#if args.workspace:
#    table.add_row(":file_folder:" + " [green]Workdir[/green]" , "[purple]" + args.workspace + "[/purple]")
#else:
#    table.add_row(":file_folder:" + " [green]Workdir[/green]" , "[red]No Workspace setup[/red]")
#table.add_row(":file_folder:" + " [green]Project[/green]" , "[cyan]"  + args.project + "[/cyan]")

#console = Console()
#console.print(table)



#os.system("docker run --rm -ti --name " + args.name + " " + args.image)
#if args.image == 'debian':
#    rprint("debian")
#    if args.project == 'exegol':
#        rprint("exegol")
#        IMAGE_NAME='debian.exegol'
#        client = docker.from_env()
#        rprint("image")
#        client.images.build(path='./Dockerfile/', dockerfile=IMAGE_NAME, tag=IMAGE_NAME)
#        rprint("container")
#        client.containers.run(tty=True, name=args.name, remove=True, stdin_open=True, image=IMAGE_NAME)
#
#
#
#
#
#
#
#
#
#
            #subprocess.run(['docker', 'build', '-f', './Dockerfile/debian.exegol', '-t', 'debian.exegol:latest', '.'], capture_output=True)
