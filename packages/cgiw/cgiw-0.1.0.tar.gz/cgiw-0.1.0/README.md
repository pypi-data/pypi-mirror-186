# CGI Wrapper

This is a lightweight, extensible framework for writing CGI scripts in python.

## Install

```
pip install cgiw
```

## Use 

This package takes care of parsing the query, headers and body (if post). It parses some basic mime types such as ```application/json``` and ```application/x-www-form-urlencoded```, and allows the developer to use custom parsers. All handlers must return a tuple containing three items: the status string, a dictionary of headers, and the body. There are some basic response functions implemented to avoid having to construct this tuple from scratch.

### Example
Here is an example that demonstrates the functionality of the framework.

```python
#!/bin/python3

from cgiw import run
from cgiw.responses import json
from cgiw.decorators import body_parser 


def custom_parser(body):
    # do stuff
    return body

@body_parser(custom_parser)
def handler(query, headers):
    # do stuff
    return json({'hello': 'world'})

run(get=handler)
```