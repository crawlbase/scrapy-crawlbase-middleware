try:
    # Python 2
    from crawlbase import CrawlbaseMiddleware
    from request import CrawlbaseRequest
    from response import CrawlbaseResponse, CrawlbaseTextResponse
except ImportError:
    # Python 3
    from .crawlbase import CrawlbaseMiddleware
    from .request import CrawlbaseRequest
