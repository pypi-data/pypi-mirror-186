csv_map_converter
=========================================================

[![Build Status](https://travis-ci.org/eHanlin/csv-map-converter.svg?branch=master)](https://travis-ci.org/eHanlin/csv-map-converter)

It's able to convert csv data when you need get model from csv.

## Install

```sh
pip install csv-map-converter
```

## Usage

```py
import csv
import io
import csv_map_converter
from csv_map_converter.models.fields import *

class User():
    enabled = BooleanField()
    account = StringField()
    password = StringField()


csv_data = io.StringIO(u"""enabled, account, password
1,tomcat,1234
0,apache,1234
""")

rows = [row for row in csv.reader(csv_data)]

result = csv_map_converter.convert(rows, User)

print(result.models)
```

## Test

```sh
tox
```


