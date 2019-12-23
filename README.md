# rss_reader_kapitonov

# RSS Reader
It is command line utility that recieves RSS URL and print news in human-readable format.<br/>


# Installation
$https://github.com/akapitonov1999/rss_reader_kapitonov.git<br/>
$cd rss_reader_kapitonov<br/>
$python setup.py bdist bdist_wheel<br/>
$cd dist<br/>
$pip install rss_reader_kapitonov-4.0.0-py3-none-any.whl<br/>


# Usage:
usage: rss_reader_kapitonov.py [-h] [--version] [--json]<br/>
    [--verbose] [--limit LIMIT] [--custom] source<br/>

Pure Python command-line RSS reader.<br/>

positional arguments:<br/>
  source         RSS URL<br/>

optional arguments:<br/>
  -h, --help     show this help message and exit<br/>
  --version      Print version info<br/>
  --json         Print result as JSON in stdout<br/>
  --verbose      Outputs verbose status messages<br/>
  --limit LIMIT  Limit news topics if this parameter provided<br/>
  --custom       Allows to customize the output<br/>
  --date         Get cached news by date<br/>
  --to-epub      Converts to .epub<br/>
  --output_path  Provides a custom path for .epub file<br/>
  --colored      Colorized stdout<br/>
  
  # Processed news examples:
  # Yahoo&Yahoo-alike News sites:
  
  New block:<br/>
Title:  Taliban claim attack that killed US soldier in Afghanistan<br/>
Link:  https://news.yahoo.com/taliban-claim-attack-killed-us-soldier-afghanistan-063449364.html<br/>
Date:  Mon, 23 Dec 2019 04:33:26 -0500<br/>
Media Content:  [{'height': '86', 'url': 'http://l1.yimg.com/uu/api/res/1.2/xrK.hzayBCMQ7cHZBFyASQ-<br/>-/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/http://media.zenfs.com/en_us/News/afp.com/2f5c7bc19e3e7e507a28879042a9d72e2a2670f8.jpg', 'width': '130'}]<br/>
<br/>Links:  [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://news.yahoo.com/taliban-claim-attack-killed-us-soldier-afghanistan-063449364.html'}]<br/>
  
  # BBC&BBC-alike News sites:
  
  New block:<br/>
 Title:  Your Tuesday Briefing<br/>
 Link:  https://www.nytimes.com/2019/12/23/briefing/boeing-jamal-khashoggi-saudi-arabia-fukushima.html<br/>
 
 # Custom News:
 
 New block:<br/>
Authors :  [{'name': '/u/chiick', 'href': 'https://www.reddit.com/user/chiick'}]<br/>
Tags :  [{'term': 'worldnews', 'scheme': None, 'label': 'r/worldnews'}]<br/>
Id :  https://www.reddit.com/r/worldnews/t3_eeij5a<br/>
  
  
  # JSON structure examples:
  # Yahoo&Yahoo-alike News sites:
  
  {<br/>
    "Title0": "Will Israel\u2019s New F-35 Be Used Against Iran\u2019s Cruise Missile Threat?",<br/>
    "Date0": "Sun, 22 Dec 2019 04:45:00 -0500",<br/>
    "Link0": "https://news.yahoo.com/israel-f-35-used-against-094500695.html",<br/>
    "Media0": [<br/>
        {<br/>
            "height": "86",<br/>
            "url": "http://l2.yimg.com/uu/api/res/1.2/DqJZIWRY8pbwcgBQJnX3IQ-<br/>-/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/the_national_interest_705/d00b42702b6f1f2293b9af5c0b8ba065",<br/>
            "width": "130"<br/>
        }<br/>
    ],<br/>
    "Links0": [<br/>
        {<br/>
            "rel": "alternate",<br/>
            "type": "text/html",<br/>
            "href": "https://news.yahoo.com/israel-f-35-used-against-094500695.html"<br/>
        }<br/>
    ]<br/>
}<br/>

# BBC&BBC-alike News sites:

{<br/>
    "Title0": "Your Tuesday Briefing",<br/>
    "Link0": "https://www.nytimes.com/2019/12/23/briefing/boeing-jamal-khashoggi-saudi-arabia-fukushima.html"<br/>
}<br/>

# Custom json (just print 'end' again if there are problems with choice):<br/>

{<br/>
    "authors0": [<br/>
        {<br/>
            "name": "/u/Minscota",<br/>
            "href": "https://www.reddit.com/user/Minscota"<br/>
        }<br/>
    ],<br/>
    "tags0": [<br/>
        {<br/>
            "term": "worldnews",<br/>
            "scheme": null,<br/>
            "label": "r/worldnews"<br/>
        }<br/>
    ],<br/>
    "id0": "https://www.reddit.com/r/worldnews/t3_eeoe6s"<br/>
}<br/>

# Convertion to .epub:<br/>
Use --to-epub      Converts to .epub<br/>
    --output_path  Provides a custom path for .epub file<br/>
  
 # Colorized output:
 Use --colored<br/>
 
 # Cache:
 cache_csv.csv<br/>
 
  #Logs:
 logs.log<br/>
