import os
import sys
import argparse

NOT_EXIST_ERROR = 'File "{}" does not exist.'

# What about an optional argument to pass a config file containing
# a custom delimiter and sheet range?


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv',
                        help='Provide path to an csv file')
    parser.add_argument('credentials_json',
                        help='Provide path to Google Api credentials.json')

    args = parser.parse_args()

    if not os.path.exists(args.csv):
        sys.exit(NOT_EXIST_ERROR.format(args.csv))
    if not os.path.exists(args.credentials_json):
        sys.exit(NOT_EXIST_ERROR.format(args.credentials_json))

    return args
