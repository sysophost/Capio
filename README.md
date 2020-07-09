# Capio
Proxy capable async screenshot grabber for http endpoints using [pyShot](https://github.com/sysophost/pyShot)

## Installation
`git clone --recurse-submodules https://github.com/sysophost/Capio`

**remember to use `--recurse-submodules` to ensure you pick up the `pyShot` submodule**

## Usage
`--url` / `-u`

URL of the remote host to capture

*This can be specified multiple times to screenshot multiple hosts*

*Ports can be specified in the typical manner `protocol://host:port`*

`--inputfile` / `-if`

Path to input file containing URLs

One line per URL in the format `protocol://host[:port]`

`--proxy` /  `-p`

Proxy to use for outgoing connections

This currently supports `HTTP` and `SOCKS4/5`

## Examples
`python capio.py --url 'https://something.com'`

`python capio.py --url 'https://something.com' --url 'http://something.else.com'`

`python capio.py --url 'https://something.com' --url 'http://something.else.com:8080'`

`python capio.py --inputfile /path/to/url/file`

### Using Proxies
#### HTTP Proxy
`python capio.py --url 'http://something.com' --proxy 'http://127.0.0.1:8080'`

#### SOCKS5 Proxy
`python capio.py --url 'http://something.com' --proxy 'socks5://127.0.0.1:1090'`