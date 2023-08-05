# txt2ebook

Console tool to convert txt file to different ebook format.

## Installation

Stable version From PyPI:

```console
python3 -m pip install txt2ebook
```

Latest development version from GitHub:

```console
python3 -m pip install -e git+https://github.com/kianmeng/txt2ebook.git
```

## Usage

Showing help message of command-line options:

```console
txt2ebook --help
```

```console
usage: tte [-f {epub,txt}] [-t TITLE] [-l LANGUAGE] [-a AUTHOR]
           [-c IMAGE_FILENAME] [-w WIDTH] [-ps SEPARATOR] [-rd REGEX]
           [-rvc REGEX] [-rv REGEX] [-rc REGEX] [-rt REGEX] [-ra REGEX]
           [-rl REGEX] [-rr REGEX REGEX] [-et TEMPLATE] [-vp] [-tp] [-hn]
           [-fw] [-rw] [-ob] [-ow] [-v] [-d] [-h] [-V]
           TXT_FILENAME [EBOOK_FILENAME]

txt2ebook/tte is a cli tool to convert txt file to ebook format.
  website: https://github.com/kianmeng/txt2ebook
  issues: https://github.com/kianmeng/txt2ebook/issues

positional arguments:
  TXT_FILENAME          source text filename
  EBOOK_FILENAME        converted ebook filename (default: 'TXT_FILENAME.{epub,txt}')

optional arguments:
  -f {epub,txt}, --format {epub,txt}
                        ebook format (default: '['epub', 'txt']')
  -t TITLE, --title TITLE
                        title of the ebook (default: 'None')
  -l LANGUAGE, --language LANGUAGE
                        language of the ebook (default: 'None')
  -a AUTHOR, --author AUTHOR
                        author of the ebook (default: '[]')
  -c IMAGE_FILENAME, --cover IMAGE_FILENAME
                        cover of the ebook
  -w WIDTH, --width WIDTH
                        width for line wrapping
  -ps SEPARATOR, --paragraph_separator SEPARATOR
                        paragraph separator (default: '\n\n')
  -rd REGEX, --regex-delete REGEX
                        regex to delete word or phrase (default: '[]')
  -rvc REGEX, --regex-volume-chapter REGEX
                        regex to parse volume and chapter header (default: by LANGUAGE)
  -rv REGEX, --regex-volume REGEX
                        regex to parse volume header (default: by LANGUAGE)
  -rc REGEX, --regex-chapter REGEX
                        regex to parse chapter header (default: by LANGUAGE)
  -rt REGEX, --regex-title REGEX
                        regex to parse title of the book (default: by LANGUAGE)
  -ra REGEX, --regex-author REGEX
                        regex to parse author of the book (default: by LANGUAGE)
  -rl REGEX, --regex-delete-line REGEX
                        regex to delete whole line (default: '[]')
  -rr REGEX REGEX, --regex-replace REGEX REGEX
                        regex to search and replace (default: '[]')
  -et TEMPLATE, --epub-template TEMPLATE
                        CSS template for epub ebook (default: 'clean')
  -vp, --volume-page    generate each volume as separate page (only 'epub' format)
  -tp, --test-parsing   test parsing for volume/chapter header
  -hn, --header-number  convert section header from words to numbers (only zh-cn/zh-tw)
  -fw, --fullwidth      convert ASCII character from halfwidth to fullwidth (only zh-cn/zh-tw)
  -rw, --raise-on-warning
                        raise exception and stop parsing if there are warnings
  -ob, --overwrite-backup
                        overwrite massaged and backup original TXT_FILENAME
  -ow, --overwrite      overwrite massaged TXT_FILENAME
  -v, --verbose         show verbosity of debugging log, use -vv, -vvv for more details
  -d, --debug           show debugging log and stacktrace
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
```

Convert a txt file into epub:

```console
txt2book ebook.txt
```

## Copyright and License

Copyright (c) 2021,2022,2023 Kian-Meng Ang

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.
