[![image](https://img.shields.io/pypi/v/its.svg)](https://pypi.org/project/its/)
[![Build Status](https://travis-ci.org/yeger00/its.svg?branch=master)](https://travis-ci.org/yeger00/its)

# its
`its` - an “Issue tracking system” as part of your repository.

# Installation
`its` can be installed from PyPI with the following command:
```
pip3 install its
```
Or installing directly from the repository:
```
git clone https://github.com/yeger00/its.git
cd its
pip3 install -e .
```

# Getting started

## Initialization
Craeting a new `its` repo by using the command:
```
itscli init
```
This will create a new `.its` directory in the current directory.

## Working with issues
Adding a new issue:
```
itscli issue new "title"
```
List all the issue:
```
itscli issue list
```
Adding comment to issue:
```
itsclie issue --id <issue_id> add comment "message"
```



# Tests
You can run the tests with the tox command:
```
tox
```
Or directly with pytest:
```
py.test
```

# Lint
You can run lint with the tox command:
```
tox -e lint
```
