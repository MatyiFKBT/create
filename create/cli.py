# -*- coding: utf-8 -*-

"""Console script for create."""
import sys
import click
from github import Github
import subprocess
import os

def subrun(string):
  subprocess.run(string.split())

@click.command()
@click.argument('project')
def main(project):
    """Console script for create."""
    path = "D:/Google Drive/Works/"
    g = Github("13b7dfed32c0782191dd613da4dcbc6e8f599d9b").get_user()

    try:
        os.makedirs(path+project)
    except:
        print("Cannot create folder")
        return
    os.chdir(path+project)
    subrun("git init")
    g.create_repo(project,private=True)
    subrun("git remote add origin https://github.com/MatyiFKBT/{}.git".format(project))
    subrun("touch README.md")
    subrun("git add .")
    subprocess.run(['git', 'commit', '-m', '"Initial commit"'])
    subrun('git push -u origin master')
    os.system('code .')


if __name__ == "__main__":
    main()