# MIT License
#
# Copyright (c) 2023 mmlvgx
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
'''URL Generator'''

from random import choice
from random import randint

from string import ascii_lowercase


CHARACTERS = ascii_lowercase

SCHEMES = ['https', 'http']
EXTENSIONS = ['com', 'org', 'net', 'edu', 'gov', 'mil']

A = 1
B = 10


class URLGenerator:
    '''URL Generator'''

    @staticmethod
    def generate() -> str:
        '''Main URL Generator method to generate url'''
        domain = ''.join([choice(CHARACTERS) for _ in range(randint(A, B))])

        scheme = choice(SCHEMES)
        extension = choice(EXTENSIONS)

        url = f'{scheme}://{domain}.{extension}'

        return url
