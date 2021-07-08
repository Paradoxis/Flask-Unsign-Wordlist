# Flask Unsign Wordlist
[![Build Status](https://travis-ci.com/Paradoxis/Flask-Unsign-Wordlist.svg?branch=master)](https://travis-ci.com/Paradoxis/Flask-Unsign-Wordlist)
[![PyPI version](https://badge.fury.io/py/flask-unsign-wordlist.svg)](https://badge.fury.io/py/flask-unsign-wordlist)
[![codecov](https://codecov.io/gh/Paradoxis/Flask-Unsign-Wordlist/branch/master/graph/badge.svg)](https://codecov.io/gh/Paradoxis/Flask-Unsign-Wordlist)

The following package is the standalone wordlist-only component to 
[flask-unsign](https://github.com/Paradoxis/Flask-Unsign). The two parts are separated to prevent you from having to also download the rather bulky wordlists if you only want to use the code.

## Installation
To install the application, simply use pip:

```
$ pip install flask-unsign-wordlist
```

To install the tool for development purposes, run the following command (after downloading a copy):

```
$ pip install -e .[test]
```

## Usage

To use the wordlists, either download them directly from [GitHub](https://github.com/Paradoxis/Flask-Unsign-Wordlist/tree/master/flask_unsign_wordlist/wordlists) or install them with pip and either run the command line tool:

``` 
$ flask-unsign-wordlist
$ flask-unsign-wordlist <wordlist>
```

Or import the code in Python to get the path:

```python
import flask_unsign_wordlist
print(flask_unsign_wordlist.get('all'))
```

## License
MIT License

Copyright (c) 2019 Luke Paris (Paradoxis)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
