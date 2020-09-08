[![Build Status](https://travis-ci.org/AlexSkrn/csv2googlesheets.svg?branch=master)](https://travis-ci.org/AlexSkrn/csv2googlesheets)

[![PyPI version](https://badge.fury.io/py/csv2googlesheets.svg)](https://badge.fury.io/py/csv2googlesheets)


# csv2googlesheets

Программа предназначена для извлечения данных из csv-файла и записи этих данных в Google Sheets.

## Установка

Чтобы использовать эту программу, сначала нужно перейти по следующей ссылке:

https://developers.google.com/sheets/api/quickstart/python

И выполнить требования в разделе **Prerequisites** и в разделе **Step 1: Turn on the Google Sheets API**

После этого в командной строке:

```
$ mkdir YOUR_NEW_DIR_NAME
$ cd YOU_NEW_DIR_NAME
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install csv2googlesheets
```

## Использование
```
$ csv2g test_data/alpha_data.csv credentials.json

Created spreadsheet ID: 11potDwqU96ckscLNQeU1pm_GPwSuIx0NwlVl2K_uu0w
8 cells updated.
```
