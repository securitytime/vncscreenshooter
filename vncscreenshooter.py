# -*- coding: utf-8 -*-

import argparse
import os
import sys

from vncdotool import api


def test_ip(args):
    print(f"# Testing {args.ip}")
    try:
        with api.connect(args.ip, password=args.password) as client:
            client.timeout = args.timeout
            try:
                client.refreshScreen()
                screenshot_file = os.path.join(args.screendir, args.ip + '.png')
                client.captureScreen(screenshot_file)
                print(f"Successfully captured screenshot: {screenshot_file}")
            except Exception as e:
                print(e)
            client.disconnect()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', required=True)
    parser.add_argument('--screendir', required=True, help='Screenshot will be saved in this directory')
    parser.add_argument('--password', required=False, help='Defaults to None')
    parser.add_argument('--timeout', required=False, type=int, default=5, help='Defaults to 5')
    args = parser.parse_args()
    test_ip(args)
