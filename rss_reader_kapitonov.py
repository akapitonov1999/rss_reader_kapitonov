import argparse as ag
import ast
import csv
import datetime
from ebooklib import epub
import feedparser
import json
import logging
from termcolor import colored


logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - '
                    '%(message)s')
logging.info('Logs go here!')
logging.error('Something went wrong with logs :(')
logging.debug('Logs debug')
log = logging.getLogger()


class ParserRSS(object):
    """Class for RSS Parser"""
    news = {}

    def __init__(self, url, lim=1, clr_fg='no', choice_list=None,
                 printer_flag='small'):
        if choice_list is None:
            choice_list = []
        self.url = url
        self.lim = lim
        self.clr_fg = clr_fg
        self.choice_list = choice_list
        self.printer_flag = printer_flag

    def custom_printer(self):
        """Prints customized news.
        Is started by choicer()"""
        log.info('Start custom_printer function')
        iterator = 0
        key_list = list(self.news.keys())
        keyz = key_list[iterator].capitalize()
        keyz = ''.join([i for i in keyz if not i.isdigit()])
        separator = keyz
        while iterator != len(key_list):
            if self.clr_fg == 'no':
                keyz = key_list[iterator].capitalize()
                keyz = ''.join([i for i in keyz if not i.isdigit()])
                if keyz == separator:
                    print('\nNew block:')
                print(keyz, ': ', self.news[key_list[iterator]])
                iterator += 1
            elif self.clr_fg == 'yes':
                keyz = key_list[iterator].capitalize()
                keyz = ''.join([i for i in keyz if not i.isdigit()])
                if keyz == separator:
                    print(colored('\nNew block:', 'green'))
                print(colored(keyz, 'red'), colored(': ', 'red'),
                      colored(self.news[key_list[iterator]], 'blue'))
                iterator += 1

    def choicer(self):
        """Allows user to choose what to collect.
        Is started by news_collector_custom()
        Starts custom_printer()"""
        log.info('Start choicer function')
        choice = input()
        if choice != 'end':
            try:
                choice = int(choice)
                print(choice)
                if choice not in self.choice_list:
                    self.choice_list.append(choice)
                    self.choice_list.sort()
                    self.choicer()
                else:
                    print('You have already pointed this!\n')
                    self.choicer()
            except ValueError:
                print('You must choose a number!')
                self.choicer()
        elif choice == 'end':
            if not self.choice_list:
                print('The program is quit because '
                      'You have not made a choice!')
            else:
                print(self.choice_list)
                iterator = 0
                while iterator != self.lim:
                    NewsFeed = feedparser.parse(self.url)
                    entry = NewsFeed.entries[iterator]
                    i = 0
                    while i != len(self.choice_list):
                        var = self.choice_list[i]
                        lst = list(entry.keys())
                        self.news[lst[var] + str(iterator)] = entry[lst[var]]
                        i += 1
                    iterator += 1
                self.cache_news()
                self.custom_printer()

    def news_collector_custom(self):
        """Collects news for custom_printer().
        May be started by --custom command or by news_collector()
        Starts choicer()"""
        log.info('Start news_collector_custom function')
        try:
            NewsFeed = feedparser.parse(self.url)
            entry = NewsFeed.entries[1]
        except Exception:
            e = 'No url or url is incorrect!'
            return e
        self.news = {}
        list_of_keys = list(entry.keys())
        ch_dict = {i: list_of_keys[i] for i in range(0, len(list_of_keys))}
        print('Make your choice:\n'
              'Print end if no more choices needed\n', ch_dict)
        self.choicer()

    def news_collector(self):
        """Collects non-custom news.
        Starts from trying collect news for printer().
        If fails, then tries to collect news for small_printer()
        If fails, then initializes news_collector_custom()"""
        log.info('Start news_collector function')
        try:
            NewsFeed = feedparser.parse(self.url)
            entry = NewsFeed.entries[1]
        except Exception:
            e = 'No url or url is incorrect!'
            return e

        iterator = 0
        try:
            # Yahoo&Yahoo-alike News like Tut.by
            if 'title' and 'published' and 'link' and 'media_content' \
                    and 'links' in entry:
                self.printer_flag = 'big'
                while iterator != self.lim:
                    entry = NewsFeed.entries[iterator]
                    self.news['Title' + str(iterator)] = entry.title
                    self.news['Date' + str(iterator)] = entry.published
                    self.news['Link' + str(iterator)] = entry.link
                    self.news['Media' + str(iterator)] = entry.media_content
                    self.news['Links' + str(iterator)] = entry.links
                    iterator += 1
            self.cache_news()

        except AttributeError:
            try:
                # Small collector for BBC&BBC-alike News
                if 'title' and 'link' in entry:
                    self.printer_flag = 'small'
                    self.news = {}
                    while iterator != self.lim:
                        entry = NewsFeed.entries[iterator]
                        self.news['Title' + str(iterator)] = entry.title
                        self.news['Link' + str(iterator)] = entry.link
                        iterator += 1
                self.cache_news()
            except AttributeError:
                # Customized news collection
                self.news_collector_custom()
        except Exception as exc:
            print(exc)

    def printer(self):
        """Prints news from Yahoo&Yahoo-alike News sites"""
        log.info('Start printer function')
        self.news_collector()
        if self.printer_flag == 'small':
            self.small_printer()
        elif self.printer_flag == 'big':
            iterator = 0
            while iterator != len(self.news.keys()):
                if self.clr_fg == 'no':
                    print('\nNew block:',
                          '\nTitle: ', self.news['Title' + str(iterator)],
                          '\nLink: ', self.news['Link' + str(iterator)],
                          '\nDate: ', self.news['Date' + str(iterator)],
                          '\nMedia Content:'
                          ' ', self.news['Media' + str(iterator)],
                          '\nLinks:'
                          ' ', self.news['Links' + str(iterator)], '\n')
                    iterator += 1
                elif self.clr_fg == 'yes':
                    print(colored('\nNew block:', 'red'),
                          colored('\nTitle: ', 'green'),
                          colored(self.news['Title' + str(iterator)], 'blue'),
                          colored('\nLink: ', 'green'),
                          colored(self.news['Link' + str(iterator)], 'blue'),
                          colored('\nDate: ', 'green'),
                          colored(self.news['Date' + str(iterator)], 'blue'),
                          colored('\nMedia Content: ', 'green'),
                          colored(self.news['Media' + str(iterator)], 'blue'),
                          colored('\nLinks: ', 'green'),
                          colored(self.news['Links' + str(iterator)], 'blue'),
                          '\n')
                    iterator += 1

    def small_printer(self):
        """Prints news from BBC&BBC-alike News sites."""
        log.info('Start small_printer function')
        iterator = 0
        while iterator != len(self.news.keys()):
            if self.clr_fg == 'no':
                print('\nNew block:\n',
                      'Title: ', self.news['Title' + str(iterator)], '\n',
                      'Link: ', self.news['Link' + str(iterator)], '\n')
                iterator += 1
            elif self.clr_fg == 'yes':
                print(colored('\nNew block:\n', 'red'),
                      colored('Title: ', 'red'),
                      colored(self.news['Title' + str(iterator)], 'green'),
                      '\n', colored('Link: ', 'red'),
                      colored(self.news['Link' + str(iterator)], 'green'),
                      '\n')
                iterator += 1

    def json_converter(self):
        """Converts collected news to json format."""
        log.info('Start json_converter function')
        self.news_collector()
        parsed = json.dumps(self.news, indent=4, sort_keys=False)
        print(parsed)

    def json_converter_custom(self):
        """Converts collected custom news to json format"""
        log.info('Start json_converter_custom function')
        self.news_collector_custom()
        parsed = json.dumps(self.news, indent=4, sort_keys=False)
        print(parsed)

    def cache_news(self):
        """Caches news to cache_csv.csv file.
        Checks the cache contain to avoid double-caching.
        Creates cache_csv.csv if it does not exist"""
        log.info('Start cache')
        the_date = datetime.datetime.strftime(datetime.datetime.now(),
                                              "%Y.%m.%d %H:%M:%S")
        the_date = the_date[0:10]
        the_date = the_date.replace('.', '')
        keyz = the_date + self.url
        field_names = ['date+url', 'news']
        key_list = []
        try:
            with open('cache_csv.csv', 'r') as file:
                csvread = csv.DictReader(file)
                for row in csvread:
                    if row['date+url'] != 'date+url':
                        key_list.append(row['date+url'])
                if keyz not in key_list:
                    with open('cache_csv.csv', 'a') as f:
                        w = csv.DictWriter(f, field_names)
                        w.writeheader()
                        w.writerow({'date+url': keyz, 'news': self.news})
                        f.close()

        except FileNotFoundError:
            with open('cache_csv.csv', 'w') as f:
                w = csv.DictWriter(f, field_names)
                w.writeheader()
                w.writerow({'date+url': keyz, 'news': self.news})
                f.close()

    def cache_extractor(self):
        """Extracts cache from cache_csv.csv if it exists
        and there is cache for this date and url"""
        print('start cache extraction!')
        key_list = []
        val_list = []
        try:
            with open('cache_csv.csv', 'r') as f:
                csvread = csv.DictReader(f)
                for row in csvread:
                    if row['date+url'] != 'date+url':
                        key_list.append(row['date+url'])
                    if row['news'] != 'news':
                        val_list.append(row['news'])
            news_dct = dict.fromkeys(key_list, val_list)
            try:
                cached_news_list = news_dct[self.url]
                cached_news_str = cached_news_list[0]
                print(cached_news_str)
                self.news = ast.literal_eval(cached_news_str)
                print('\nNews cache for this date and url: \n')
                self.custom_printer()
            except Exception:
                print('No cache for this date/url!')
        except FileNotFoundError:
            print('There is no cache at all!')

    def to_epub(self):
        """ Converts collected news to .epub file"""
        self.news_collector()
        the_date = datetime.datetime.strftime(datetime.datetime.now(),
                                              "%Y.%m.%d %H:%M:%S")
        the_date = the_date[0:10]
        the_date = the_date.replace('.', '')
        keyz = the_date + self.url
        keyz = keyz.replace('/', '')
        keyz = keyz.replace('.', '')
        keyz = keyz.replace(':', '')
        try:
            log.info('Convert to epub')
            book = epub.EpubBook()
            # set metadata
            book.set_identifier('id123456')
            book.set_title('news')
            book.set_language('en')
            book.add_author('Andrey Kapitonov')
            book.add_author('Andrey Kapitonov', file_as='Epub', role='ill',
                            uid='coauthor')
            chapter_file_counter = 1
            ep = ""
            c1 = epub.EpubHtml(title='Intro', file_name='{}.xhtml'.format(
                chapter_file_counter), lang='hr')
            for item in self.news:
                ep += '<br>' + str(item) + '<br>'
                for element in self.news[item]:
                    ep += str(element)
                chapter_file_counter += 1
                c1.content = ep
                # add chapter
                book.add_item(c1)
            # define Table Of Contents
            book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
                        (epub.Section('Simple book'), (c1,)))
            # add default NCX and Nav file
            book.add_item(epub.EpubNcx())
            book.add_item(epub.EpubNav())
            # define CSS style
            style = 'BODY {color: white;}'
            nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css",
                                    media_type="text/css", content=style)
            # add CSS file
            book.add_item(nav_css)
            # basic spine
            book.spine = ['nav', c1]
            # write to the file
            try:
                path = args.output_path
            except Exception:
                path = ''
            file_name = path + '/book' + keyz + '.epub'
            epub.write_epub(file_name, book, {})
            print('Successful', file_name)

        except Exception:
            raise Exception('Unable to convert to .epub')


def main():
    """Gets optional arguments and initializes ParserRSS class"""
    try:
        parser = ag.ArgumentParser(description='Processes something')

        parser.add_argument('--version', action='store_true',
                            help='Prints version info')
        parser.add_argument('--json', action='store_true',
                            help='Prints result as JSON in stdout')
        parser.add_argument('--verbose', action='store_true',
                            help='Outputs verbose status info')
        parser.add_argument('--limit', action='store', dest='limit',
                            help='Limits news topics if this parameter '
                                 'provided', default=1)
        parser.add_argument('--custom', action='store_true',
                            help='Allows to customize the output')
        parser.add_argument('--date', action='store', dest='date',
                            help='Get cached news by date')
        parser.add_argument('--to_epub', action='store_true',
                            help='Converts to .epub')
        parser.add_argument('--output_path', action='store', dest='path',
                            help='provides a custom path for .epub-file')
        parser.add_argument('--colored', action='store_true',
                            help='Colorizes stdout')
        parser.add_argument('string', metavar='Source', type=str)

        args = parser.parse_args()
        log.info('Start')
        custom_flag = 'no'
        cache_flag = 'no'
        conversation_flag = 'no'
        color_flag = 'no'

        if args.date:
            obj = ParserRSS(str(args.date) + str(args.string))
            obj.cache_extractor()
            cache_flag = 'yes'

        if args.colored:
            color_flag = 'yes'

        prss = ParserRSS(args.string, int(args.limit), color_flag)

        if args.to_epub:
            prss.to_epub()
            conversation_flag = 'yes'

        if args.version:
            print('version 1')
            log.info('Printed Version')

        if args.custom:
            custom_flag = 'yes'
            log.info('Changed custom_flag')

        if args.json:
            if custom_flag == 'no' and cache_flag == 'no' \
                    and conversation_flag == 'no':
                prss.json_converter()
                log.info('Started as custom json-collector')
            elif custom_flag == 'yes' and cache_flag == 'no' \
                    and conversation_flag == 'no':
                prss.json_converter_custom()
                log.info('Started as standard json-collector')

        if args.verbose:
            with open("logs.log", 'r+') as f:
                date = f.read()
                print(date)
            log.info('Logs to stdout')

        if args.limit:
            if custom_flag == 'no' and cache_flag == 'no' \
                    and conversation_flag == 'no':
                prss.printer()
                log.info('Started as standard news-collector')
            elif custom_flag == 'yes' and cache_flag == 'no' \
                    and conversation_flag == 'no':
                prss.news_collector_custom()
                log.info('Started as custom news-collector')

        else:
            prss.printer()
            log.info('Started with no optional arguments')
            prss.cache_news()

    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    print('''usage: rss_reader_kapitonov.py [-h] [--version] [--json]
    [--verbose] [--limit LIMIT] [--custom] source
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
  --colored      Colorized stdout''')
    main()
