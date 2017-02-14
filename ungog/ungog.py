# ungog.py
# de-googleify your motherfucking css
# Do What The Fuck You Want License
# (c) Wu Ming, 2017

"""
UnGoogleify your css
"""

import re
import urllib.request
from glob import glob
from os import makedirs, remove
import sys


TAINTEDAPI = 'fonts.googleapis.com'
TAINTEDASSET = 'fonts.gstatic.com'
RE_FONTURI = 'url\((?P<url>[\w|./?=+:]+)\)'
RE_FONTNAME = r'local\(\'(?P<local>[\s|\w]+)\'\)'
LFOLDER = 'fonts'


def ungog(cssfile):
    _downloadFonts(cssfile)
    makedirs(LFOLDER, exist_ok=True)
    _processGFonts()
    _rewriteCss(cssfile)
    _cleanup()
    print('[+] done')


def _downloadFonts(cssfile):
    for i, uri in enumerate(_filterFonts(_parseFile(cssfile))):
        _getPage(uri, '__gfont{0}.css'.format(i))


def _processGFonts():
    for font_file in glob('__gfont*.css'):
        _processGFontFile(font_file)


def _processGFontFile(font_file):
    newlines = []
    for line in _parseFile(font_file):
        if TAINTEDASSET in line:
            name = re.findall(RE_FONTNAME, line)[0]
            uri = re.findall(RE_FONTURI, line)[0]
            lpath = LFOLDER + '/' + name.lower().replace(' ', '_') + '.ttf'
            _getPage(uri, lpath, text=False)
            newline = re.sub(RE_FONTURI, "url('{0}')".format(lpath), line)
            print('[+] replacing from:', line[:-1])
            print('[+] replacing to:  ', newline[:-1])
            newlines.append(newline)
        else:
            newlines.append(line)
    with open(font_file + '.replaced', 'w') as f:
        f.write(''.join(newlines))


def _rewriteCss(cssfile):
    newlines = []
    for newfile in glob('__*.replaced'):
        newlines = _parseFile(newfile) + newlines
    newlines += list(filter(lambda s: TAINTEDAPI not in s,
                            _parseFile(cssfile)))
    with open(cssfile + '.new', 'w') as f:
        f.write(''.join(newlines))


def _getPage(uri, filename, text=True):
    response = urllib.request.urlopen(uri)
    print('[+] got {0}'.format(uri))
    out = response.read()
    if text:
        out = out.decode('utf-8')
        with open(filename, 'w') as f:
            f.write(out)
    else:
        with open(filename, 'wb') as f:
            f.write(out)


def _parseFile(cssfile):
    return open(cssfile, 'r').readlines()


def _filterFonts(css_lines):
    font_list = [
        'https:' +
        re.findall(RE_FONTURI, line)[0] for line in
        filter(lambda l: TAINTEDAPI in l, css_lines)]
    return font_list


def _cleanup():
    leftovers = []
    leftovers += glob('__*.css')
    leftovers += glob('__*.replaced')
    for leftover in leftovers:
        remove(leftover)


def main():
    if len(sys.argv) != 2:
        print('Usage: ungog main.css')
        exit(1)
    cssfile = sys.argv[1]
    ungog(cssfile)


if __name__ == '__main__':
    main()
