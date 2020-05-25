import feedparser
from pprint import pprint
feed = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale')

pprint(feed, indent=4)
