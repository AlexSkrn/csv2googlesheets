import os
import pytest

from csv2googlesheets.parse_file import parse_file


def test_parse_file(tmpdir):
    filename = 'data.csv'
    data_file = tmpdir.join(filename)
    data_file.write('2,3,4\n5,6,7')

    output = parse_file(path=os.path.join(tmpdir, filename))

    assert output == [['2', '3', '4'], ['5', '6', '7']]


def test_parse_file_raises_error_and_prints_info(tmpdir):
    filename = 'data.csv'
    data_file = tmpdir.join(filename)
    data_file.write('')

    with pytest.raises(SystemExit) as excinfo:
        path = os.path.join(tmpdir, filename)
        parse_file(path)

    expected = f'Failed to extract any data from "{path}"'
    assert expected in str(excinfo.value)
