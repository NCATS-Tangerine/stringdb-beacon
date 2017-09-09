#!/usr/bin/python3

urls=[
    'https://string-db.org/download/protein.aliases.v10.5/9606.protein.aliases.v10.5.txt.gz',
    'https://string-db.org/download/species.v10.5.txt',
    'https://string-db.org/download/protein.actions.v10.5/9606.protein.actions.v10.5.txt.gz'
]

from urllib.request import FancyURLopener
import os.path
import gzip
import shutil

class CustomHeaderURLOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

url_opener = CustomHeaderURLOpener()

if __name__ == '__main__':

    files = []
    for url in urls:
        gz = url.split('/')[-1]
        txt = gz.replace('.gz', '')
        files.append((url, gz, txt))

    for url, gz, txt in files:
        if os.path.isfile(gz) or os.path.isfile(txt):
            continue
        print('Downloading', gz, 'from', url)
        url_opener.retrieve(url, gz)

    for url, gz, txt in files:
        if os.path.isfile(txt):
            continue
        print('Unzipping', gz)
        with gzip.open(gz, 'rb') as f_in, open(txt, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    for url, gz, txt in files:
        with open(txt, 'r+') as f:
            line = f.readline()
            lines = [l.strip() for l in line.split('##') if (l is not '##') and (l is not '') and (l is not '\n')]
            fixed = '	'.join(lines)
            if len(lines) > 1 or len(line.strip()) != len(fixed):
                print('Fixing tsv header for', txt)
                while len(fixed) < len(line) - 1:
                    fixed += ' '
                fixed += '\n'
                f.seek(0)
                f.write(line.replace(line, fixed))
