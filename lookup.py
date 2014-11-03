
import re
from sys import stdin
from subprocess import check_output, STDOUT

match = (
    '-{52}\n' # header
    'Name: *(?P<full_name>(\w+? )+\w+)\n'
    'UNI: *(?P<uni>[a-zA-z]{2,3}\d{4})\n'
    'EMail: *(?P<email>[a-zA-z]{2,3}\d{4}@(columbia|barnard)\.edu)\n'
    '\n'
    '  Title: *Student, (?P<school>[\w,&: ]+)\n'
)


def parse(text):
    res = re.search(match, text)
    if res:
        return res.groupdict()
    return None


def lookup(name):
    return check_output(['lookup', name])


if __name__ == '__main__':
    for name in stdin.readline().strip():
        print parse(lookup(name))




