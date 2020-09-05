import sys
import os
from github import Github

path = "/Users/hk.dacillo/Google Drive/"
username = "" #Github username
password = "" #Github password

def create():
    folderName = str(sys.argv[1])
    os.mkdir(os.path.join(path, folderName))
    user = Github(username, password).get_user()
    user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
