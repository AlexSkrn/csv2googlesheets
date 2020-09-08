import os

import pytest

from csv2googlesheets.parse_file import build_spreadsheet_title


@pytest.mark.parametrize(
    'test_input,expected',
    [
     (os.path.join('Users', 'username', 'Documents', 'data.csv'), 'data'),
     ('data.csv', 'data'),
     ('data', 'data'),
    ]
)
def test_build_spreadsheet_title(test_input, expected):
    output = build_spreadsheet_title(test_input)
    assert output == expected


def test_build_spreadsheet_title_raises_error():
    with pytest.raises(SystemExit) as excinfo:
        build_spreadsheet_title('')

    expected = f'Failed to built title for .'
    assert expected in str(excinfo.value)
