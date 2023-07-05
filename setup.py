"""Crawlbase Scrapy middleware."""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

readme = open('README.md').read()

setup(
    name = 'scrapy-crawlbase-middleware',
    license = 'Apache-2.0',
    version = '1.0.0',
    description = 'Scrapy Crawlbase Proxy Middleware: Crawlbase interfacing middleware for Scrapy',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'Crawlbase',
    author_email = 'info@crawlbase.com',
    url = 'https://github.com/crawlbase-source/scrapy-crawlbase-middleware',
    keywords = 'scrapy middleware scraping scraper crawler crawling crawlbase api',
    include_package_data = True,
    packages = find_packages(),
    classifiers = (
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    )
)
