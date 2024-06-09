# dumptls

A tool to download TLS certificates including intermediate and root CA certs.

## Installation

You can install the package using pip:


## Usage

To use the tool, simply run:

```bash
dumptls www.google.com
```

You can also specify a port and a resolve IP address:

```bash
dumptls example.com --port 8443 --resolve-ip-address 192.168.1.1
```

Example output:

- output file in base64 (pem) format

- stdout with following example output (common names for all TLS certificates and their seria numbers)

```
Certificates have been saved to cert_chain.pem
Common Name: www.google.com, Serial Number: 276676235549746405282904896944097780989
Common Name: GTS CA 1C3, Serial Number: 159612451717983579589660725350
Common Name: GTS Root R1, Serial Number: 159159747900478145820483398898491642637
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
