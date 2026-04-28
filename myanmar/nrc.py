# nrc.py - myanmar nrc validation & normalization module
# coding: utf-8
# The MIT License (MIT)
# Copyright (c) 2018 Soe Zayar

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

import re
import json
import pkgutil

township_names = json.loads(
    pkgutil.get_data('myanmar', 'data/nrc_townships.json').decode('utf-8'))

ccode = range(1, 14)

nation_dict = {
    'naing': 'n',
    'pyu': 'p',
    'ae': 'e',
    'n': 'n',
    'p': 'p',
    'e': 'e'
}

# Valid nrc format is ./...(.)......
# But with this program,
# user can write ',''.'' ' instead of '/'
# and ','''.'' ' instead of '()'

city_code_re = r'(\d{1,2}?)\s*'
township_name_re = r'\s*(\b\w.*\s*\w.*\s*\b)\s*'
nation_re = r'(\b\w.*\b)'
number_re = r'\s*(\b[0-9][0-9]{5}\b)'

nrc_format = re.compile(city_code_re + r'[/ .,]' + township_name_re +
                        r'[( .,]' + nation_re + r'[,. )]' + number_re)


def is_valid_nrc(nrc):
    """
    Check whether the given string is
    valid Myanmar national registration ID or not

    >>> is_valid_nrc('12/LMN (N) 144144')
    True
    >>> is_valid_nrc('5/PMN (N) 123456')
    False
    """
    pass


def normalize_nrc(nrc):
    """
    Check the given string is valid myanmar nrc or not and
    normalize the string to simplest form if the string is valid

    >>> normalize_nrc('9/pmn(n)123456')
    '9 pamana n 123456'
    >>> normalize_nrc('1/bkn(n)123456')
    '1 bakana n 123456'
    """
    pass
