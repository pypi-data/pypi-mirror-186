# qrcite
Small python tool to generate qr codes with doi links out of .bib files.

Inspired by https://github.com/nucleic-acid/namedropR.

## Requires:
- bibtexparser
- qrcode

install them via pip

## usage:

    python qrcite.py -i inputfile.bib -c "#900000" -t png

or    

    python qrcite.py --input inputfile.bib --color "#070" --type pdf


## installation:

    pip install https://codeberg.org/Meph/qrcite

Usage after installation:

    qrcite
    # or
    python -m qrcite


<br /><br /><br />

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.  
Follow me on <a rel="me" href="https://nerdculture.de/@M">Mastodon</a>.
