#!/bin/bash

function create() {
    cd ~/Google\ Drive/Project-Initialisation-Automation/
    python create_repo.py $1
    cd ~/Google\ Drive/$1
    git init
    git remote add origin https://github.com/hezekiahdacillo/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
}
