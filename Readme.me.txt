RSS Reader
It is command line utility that recieves RSS URL and print news in human-readable format.

Installation
$https://github.com/akapitonov1999/FinalTaskRssParser.git
$cd rss_reader_kapitonov
$python setup.py bdist bdist_wheel
$cd dist
$pip install rss_reader_kapitonov-4.0.0-py3-none-any.whl
Usage
  usage: rss_reader.py [-h] [--version] [--json] [--verbose]
    [--limit LIMIT] [--custom] source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
  --custom       Allows to customize the output
  --date         Get cached news by date
  --to-epub      Converts to .epub
  --output_path  Provides a custom path for .epub file
  --colored      Colorized stdout
