# qrcite
Generate QR Codes from .bib-files.

Example:

![Einstein1905 QR Code](EinsteinUeberErzeugungund1905.png)

Inspired by https://github.com/nucleic-acid/namedropR.


## Installation

    pip install https://codeberg.org/Meph/qrcite


## Usage after installation

    qrcite -i input.bib


    qrcite --help


## Examples

With text, red background

    qrcite -i inputfile.bib -c "#900000" -t png

QR Code only, as pdf

    python -m qrcite --input inputfile.bib --color "#070" --style qrcode --type pdf


<br /><br /><br />

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.  
Follow me on <a rel="me" href="https://nerdculture.de/@M">Mastodon</a>.
