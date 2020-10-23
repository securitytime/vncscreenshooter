# vncscreenshooter

This scripts utilizes the Python module vncdotool to create a screenshot of a VNC server.

By default, no password will be used. If required, you can set a password via the --password paramter.

## Setup

```
$ python3 -m venv venv
$ ./venv/bin/python -m pip install vncdotool
$ mkdir screenshots
```

## Usage

```
$ ./venv/bin/python vncscreenshooter.py -h
usage: vncscreenshooter.py [-h] --ip IP --screendir SCREENDIR [--password PASSWORD] [--timeout TIMEOUT]

optional arguments:
  -h, --help            show this help message and exit
  --ip IP
  --screendir SCREENDIR
                        Screenshot will be saved in this directory
  --password PASSWORD   Defaults to None
  --timeout TIMEOUT     Defaults to 5

$ ./venv/bin/python vncscreenshooter.py --ip 192.168.0.1 --screendir screenshots/
```

## Scan multiple hosts

Create a new file which contains one IP address per line. Now run the script like this:

```
for ip in $(cat ips.txt); do ./venv/bin/python vncscreenshooter.py --ip $ip --screendir screenshots/; done
```
