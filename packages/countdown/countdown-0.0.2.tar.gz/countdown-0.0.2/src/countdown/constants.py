"""MIT License

Copyright (c) 2023-present Tanner B. Corcoran

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

"""

VALID_FLAGS = {"w", "d", "h", "M", "s", "m", "u", "z"}
SKIPPED_FLAGS = {"z"}
VALID_PLURAL_FLAGS = {"p", "P", "ep", "eP", "Ep", "EP"}
MICROSECONDS_IN_MILLISECOND = 1_000
MICROSECONDS_IN_SECOND = 1_000_000
MICROSECONDS_IN_MINUTE = MICROSECONDS_IN_SECOND * 60
MICROSECONDS_IN_HOUR = MICROSECONDS_IN_MINUTE * 60
MICROSECONDS_IN_DAY = MICROSECONDS_IN_HOUR * 24
MICROSECONDS_IN_WEEK = MICROSECONDS_IN_DAY * 7
