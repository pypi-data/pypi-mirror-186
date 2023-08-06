# Pywifiscan

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ferreirad08/pywifiscan/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pywifiscan.svg)](https://badge.fury.io/py/pywifiscan)
![Tests](https://github.com/ferreirad08/pywifiscan/actions/workflows/tests.yml/badge.svg)
![Custom badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fjsonblob.com%2Fapi%2FjsonBlob%2F1065454290407276544)
[![Downloads](https://pepy.tech/badge/pywifiscan)](https://pepy.tech/project/pywifiscan)
[![Downloads](https://pepy.tech/badge/pywifiscan/month)](https://pepy.tech/project/pywifiscan)
[![Supported versions](https://img.shields.io/pypi/pyversions/pywifiscan.svg)](https://pypi.org/project/pywifiscan)

Library to get the received signal strength indicator (RSSI) from Wi-Fi networks.

## Dependencies

```bash
$ sudo apt install net-tools wireless-tools
```

## Installation

Simply install **pywifiscan** package from [PyPI](https://pypi.org/project/pywifiscan/)

```bash
$ pip install pywifiscan
```

## Examples

```python
>>> from pywifiscan import get_interface, scan_networks
>>> # Getting the default Network Interface
>>> iface = get_interface()
>>> networks = scan_networks(iface)
>>> print(networks)
{
    'networkName0': -70,
    'networkName1': -75,
    ...
    'networkNameN': -91
}
```
