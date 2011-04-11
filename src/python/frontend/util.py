# Copyright (c) 2011 AOL Inc.  All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

## Utility functions.

from lxml import etree as ET

import apiserver.const as C

def response_to_xml(elem):
    'Create a pretty-printed XML response.'
    return ET.tostring(elem, encoding=C.UTF8, pretty_print=True,
                       xml_declaration=True)

def filter_references(namespace, items):
    "Look for references for items in the specified namespace."
    prefix = namespace[0].upper()
    results = set()
    for i in items:
        results.update(map(lambda x: x[1:],
                           filter(lambda x: x[0] == prefix,
                                  i.get(C.REFERENCES, []))))
    return results
