# lampip: Simple CLI tool for creating python custom lambda layers

[![image](https://img.shields.io/pypi/l/lampip)](https://python.org/pypi/lampip)
[![image](https://img.shields.io/pypi/v/lampip)](https://python.org/pypi/lampip)
[![image](https://img.shields.io/pypi/pyversions/lampip)](https://python.org/pypi/lampip)
[![image](https://github.com/hayashiya18/lampip/actions/workflows/pytest.yml/badge.svg)](https://github.com/hayashiya18/lampip/actions/workflows/pytest.yml)

---

## Features

- Build Python(3.7, 3.8, 3.9)-compatible custom lambda layers using Docker and pip, and push it to AWS.

- Reduce the package size using some approachs.
  - [Byte-Compile](https://docs.python.org/3.8/library/compileall.html) (that remove source comments and docstrings).
  - Remove `*.dist-info`.

## Requirements

- Python3
- Docker
- AWS Account

## Installation

You can obtain this packages using pip.

```console
$ pip3 install lampip
```

Then you can use `lampip` command.

```console
$ lampip --help
Usage: lampip [OPTIONS] COMMAND [ARGS]...

  Simple CLI tool for creating python custom lambda layers

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  deploy  Build and push lambda layer
  new     Create the scaffold

```

## Usage

At the first create the scaffold

```console
$ lampip new science
```

Go to the generated directory

```console
$ cd science
$ ls
lampip-config.toml  other_resources  requirements.txt
```

Edit `requirements.txt`

```text
numpy
scipy
pandas
```

Edit `lampip-config.toml`

```toml
[lampip]
layername = "science"
description = "numpy, scipy, and pandas"
pyversions = ["3.7", "3.8", "3.9"]

[lampip.shrink]
compile = true
compile_optimize_level = 2
remove_dist_info = true

# [lampip.shrink.plotly]
# remove_jupyterlab_plotly = true
# remove_data_docs = true
```

Before you deploy the lambda layer, be sure you have AWS credentials configured.

```console
(If you do not configure AWS credentials yet, ...)
$ aws configure
AWS Access Key ID: ?????
AWS Secret Acess Key: ?????
Default region name: ?????
```

(Option) You can switch the aws credentials using environments variables.

```console
(Case1: Using AWS CLI profile)
$ export AWS_PROFILE="subaccount"

(Case2: Using AWS access key directly)
$ export AWS_ACCESS_KEY_ID=????
$ export AWS_SECRET_ACCESS_KEY=?????
$ export AWS_DEFAULT_REGION=?????
```

Deploy

```console
$ lampip deploy
Start to make dist/science_1631253196_3.7.zip
...
Publish the custom layer: arn:aws:lambda:ap-northeast-1:XXXXXXXXXXXX:layer:science-py38:1
DONE: dist/science_1631253312_3.8.zip created

$ ls -lh dist
-rw-r--r-- 1 root root 73M  9月 10 23:54 science_1631253254_3.7.zip
-rw-r--r-- 1 root root 73M  9月 10 23:55 science_1631253312_3.8.zip
...


(The --no-upload option suppress uploading zip files)
$ lampip deploy --no-upload
```

Then you can check deployed layers on AWS Console.

![image](./assets/lambda_console.webp)
