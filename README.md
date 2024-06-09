# dumptls

A tool to download TLS certificates including intermediate and root CA certs.

## Installation

You can install the package using pip:


## Usage

To use the tool, simply run:

```bash
dumptls example.com

```

You can also specify a port and a resolve IP address:

```bash
dumptls example.com --port 8443 --resolve-ip-address 192.168.1.1
```

##  Building and Installing the Package

Navigate to the directory containing setup.py and run the following command to build the package:

```bash
python setup.py sdist bdist_wheel
```

To install the package locally:

```bash
pip install .
```