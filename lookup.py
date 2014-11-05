
import re
import csv
from sys import argv
from subprocess import Popen, PIPE


match = (
    '-{52}\n'  # header
    'Name: *(?P<full_name>(\w+? )+\w+)\n'
    'UNI: *(?P<uni>[a-zA-z]{2,3}\d{4})\n'
    'EMail: *(?P<email>[a-zA-z]{2,3}\d{4}@(columbia|barnard)\.edu)\n'
    '\n'
    '  Title: *Student(?P<school>.*)\n'
)


def parse(text):
    res = re.search(match, text)
    if res:
        return res.groupdict()
    return None


def lookup(name):
    p = Popen(['lookup', '-I', name], stdout=PIPE)
    p.wait()
    stdout = p.communicate()[0]
    if len([i for i in re.finditer('-'*52, stdout)]) > 1:
        filename = '{0}_options.txt'.format(name)
        print '> 1 match found for {0}, output saved to: {1}'.format(
            name, filename)
        with open(filename, 'w') as f:
            f.write(stdout)
    return stdout


if __name__ == '__main__':

    f = open(argv[1])
    w = open(argv[2], 'wb')
    no_matches = open('no_matches.txt', 'w+')

    uni_writer = csv.DictWriter(w, ['full_name', 'uni', 'email', 'school'])
    for name in f:
        name = name.strip()
        if not name:
            continue

        print name
        data = parse(lookup(name))
        if data:
            uni_writer.writerow(data)
        else:
            print 'No matches found for {0}'.format(name)
            no_matches.write("{0}\n".format(name))

    f.close()
    w.close()
    no_matches.close()
