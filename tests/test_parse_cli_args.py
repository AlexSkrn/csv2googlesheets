import sys
import os
import pytest
from argparse import ArgumentParser

from csv2googlesheets.parse_cli_args import parse_cli_args


def test_parse_cli_args_return_correct_values(monkeypatch):
    """When given file arguments, function returns correct default values."""
    argv = ['_', 'dummy.csv', 'dummy_credentials.json']
    monkeypatch.setattr(os.path, 'exists', lambda _: True)
    monkeypatch.setattr(sys, 'argv', argv)

    args = parse_cli_args()

    assert args.csv == 'dummy.csv'
    assert args.credentials_json == 'dummy_credentials.json'


@pytest.mark.parametrize(
    'test_input_1,test_input_2,expected',
    [('non-existing file.csv', 'credentials.json',
      'File non-existing file.csv does not exist.'),
     ('test_data/alpha_data.csv', 'non-existing_creds.json',
      'File non-existing_creds.json does not exist')
     ]
    )
def test_parse_cli_args_raises_error(
  monkeypatch, test_input_1, test_input_2, expected
  ):
    """Must raise errors with appropriate messages when files do not exist."""
    def mockreturn_argparse(dummy_var):
        class Args:
            def __init__(self, csv, json):
                self.csv = csv
                self.credentials_json = json

        args_obj = Args(test_input_1, test_input_2)

        return args_obj

    monkeypatch.setattr(
        ArgumentParser,
        "parse_args",
        mockreturn_argparse
        )

    with pytest.raises(SystemExit) as excinfo:
        parse_cli_args()

    assert expected in str(excinfo.value)
