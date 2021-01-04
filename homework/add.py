#!/usr/bin/env python3

import git
repo = git.Repo('~/Programs/pch_projects/kurochkin')
print(repo.git.status())
print(repo.git.add())
commit = str(input("Enter commit: "))
print(repo.git.commit(m=commit))
