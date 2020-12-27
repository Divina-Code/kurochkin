#!/bin/bash

git status
git add -A
read -p "Enter something to commit: " $commit
echo $commit
git commit -m $commit
git push