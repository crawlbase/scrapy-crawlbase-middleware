import logging
from .request import CrawlbaseRequest

try:
    # For Python 3.0 and later
    from urllib.parse import quote_plus
except ImportError:
    # Fall back to Python 2's
    from urllib import quote_plus

log = logging.getLogger('scrapy.crawlbase')


class CrawlbaseMiddleware(object):
    def __init__(self, settings):
        self.crawlbase_enabled = settings.get('CRAWLBASE_ENABLED', True)
        self.crawlbase_token = settings.get('CRAWLBASE_TOKEN')
        self.crawlbase_url = 'https://api.crawlbase.com'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        """Process a request using the crawlbase API if applicable"""

        if not self.crawlbase_enabled:
            log.warning('Skipping Crawlbase API CALL disabled!')
            return None

        if not isinstance(request, CrawlbaseRequest):
            return None

        if self.crawlbase_url not in request.url:
            new_url = self._get_proxied_url(request.url, request.query_params_str)
            log.debug('Using Crawlbase API, Request overridden with URL: {}'.format(new_url))
            return request.replace(url=new_url)

    def process_response(self, request, response, spider):
        """Process a response coming from crawlbase API if applicable"""

        if not isinstance(request, CrawlbaseRequest):
            return response

        # Replace url again with the original url saved in request
        log.debug('Using Crawlbase API, Response overridden with URL: {}'.format(request.original_url))
        return response.replace(url=request.original_url)

    def _get_proxied_url(self, url, query_params):
        """
        Transform the url into a call to proxy crawl api, sending the target url as query parameter.
        """
        original_url_encoded = quote_plus(url, safe='')
        crawlbase_url = self.crawlbase_url
        crawlbase_token = self.crawlbase_token
        crawlbase_query_params = query_params
        proxied_url = '{}/?token={}&{}&url={}'.format(
            crawlbase_url,
            crawlbase_token,
            crawlbase_query_params,
            original_url_encoded
        )
        return proxied_url
