import sys
import os
from github import Github

def create(path, username, password):
    folderName = str(sys.argv[1])
    os.mkdir(os.path.join(path, folderName))
    user = Github(username, password).get_user()
    user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    file = open("credentials.txt")
    data = file.readlines()
    credData = {}
    for i in data:
        cred = i.strip().split("=")
        credData[cred[0]] = cred[1]

    path = credData['path']
    username = credData['username']
    password = credData['password']

    create(path, username, password)
