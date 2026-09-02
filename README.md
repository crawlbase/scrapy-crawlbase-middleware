# Crawlbase API middleware for Scrapy

Processes [Scrapy](http://scrapy.org/) requests using [Crawlbase](https://crawlbase.com) services either with Normal or Javascript tokens

## Installing

Choose a way of installing:

- Clone the repository inside your Scrapy project and run the following:

```bash
python setup.py install
```

- Or use [PyPi](https://pypi.org/project/scrapy-crawlbase-middleware/) Python package manager. `pip install scrapy-crawlbase-middleware`

Then in your Scrapy `settings.py` add the following lines:

```python
# Activate the middleware
CRAWLBASE_ENABLED = True

# The Crawlbase API token you wish to use, either normal of javascript token
CRAWLBASE_TOKEN = 'your token'

# Enable the middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy_crawlbase.CrawlbaseMiddleware': 610
}
```

## Usage

Use the scrapy_crawlbase.CrawlbaseRequest instead of the scrapy built-in Request.
The scrapy_crawlbase.CrawlbaseRequest accepts additional arguments, used in the Crawlbase API:

```python
from scrapy_crawlbase import CrawlbaseRequest

class ExampleScraper(Spider):

    def start_requests(self):
        yield CrawlbaseRequest(
            "http://target-url",
            callback=self.parse_result,
            device='desktop',
            country='US',
            page_wait=1000,
            ajax_wait=True,
            dont_filter=True
        )
```

The target url will be replaced with the Crawlbase API url and parameters will be encoded into the url by the middleware automatically.

## Smart AI Proxy usage

The [Smart AI Proxy](https://crawlbase.com/docs/smart-proxy) is a standard rotating HTTP(S) proxy endpoint, so it can be used from Scrapy without this middleware: set it as the request proxy with your token as the proxy username and an empty password. Crawlbase handles proxy rotation, retries and anti-bot bypass on its side.

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield scrapy.Request(
            'https://httpbin.org/ip',
            meta={'proxy': 'http://YOUR_TOKEN:@smartproxy.crawlbase.com:8012'},
            callback=self.parse,
        )

    def parse(self, response):
        self.logger.info(response.text)
```

Note: the proxy re-signs HTTPS traffic; Scrapy's default TLS context factory does not verify certificates, so no extra configuration is needed. The example uses the plain-HTTP proxy port `8012`, which works with every Scrapy version. See the [Smart AI Proxy documentation](https://crawlbase.com/docs/smart-proxy) for all options.

If you have questions or need help using the library, please open an issue or [contact us](https://crawlbase.com/contact).

---

Copyright 2026 Crawlbase
