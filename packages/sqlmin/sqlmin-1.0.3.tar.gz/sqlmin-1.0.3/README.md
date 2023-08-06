
# SQLMin

Minifies sql files into a single line.

![Logo](docs/logo.jpg)


## Installation

### Using pip

Install sqlmin with pip

```bash
$ pip install sqlmin
```

### From source

Install sqlmin from repository.

```bash
$ git clone https://github.com/enrique-rodriguez/sqlmin.git
$ cd sqlmin
$ pip install .
```
## Usage/Examples

### Reading SQL from STDIN

```bash
$ sqlmin "DROP TABLE IF EXISTS schema.mytable;
SELECT 'a', 'b', 'c'
;
"
DROP TABLE IF EXISTS schema.mytable;SELECT 'a','b','c';
$
```

### Reading SQL from a file and Exporting the Results.

```bash
$ sqlmin -f path/to/file.sql > results.min.sql
```


### Python

#### Example Code

```python
from sqlmin import SQLMinifier

minifier = SQLMinifier()

with open("create_db.sql") as fd:
    sql = minifier.minify(fd.read())
```

## Running Tests

To run tests, run the following command

```bash
  python3 -m unittest discover tests
```


## Contributing

Contributions are always welcome!
